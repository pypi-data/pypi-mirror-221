import dis
import io
import sys
from typing import List, Optional, Set, Tuple, Type, Container
import textwrap

from IPython.display import display

from .utils import (
    hasjabs,
    graph_sort,
    get_origin,
    lowest_common_successors, compareop_to_ast, binop_to_ast, inplace_to_ast, unaryop_to_ast,
)
from .ast_utils import *

try:
    import ast as astunparse

    assert hasattr(astunparse, "unparse")
    print("Using ast.unparse")
except AssertionError:
    import astunparse
from types import CodeType

INDENT = 0
DEBUG = False
DRAW_PROG = "dot"


class set_debug:
    def __init__(self, value=True, prog="dot"):
        global DEBUG, DRAW_PROG
        self.old = (DEBUG, DRAW_PROG)
        DEBUG = value
        DRAW_PROG = prog

    def __enter__(self):
        pass

    def __exit__(self, *args):
        global DEBUG, DRAW_PROG
        DEBUG, DRAW_PROG = self.old


def debug(*args, **kwargs):
    if DEBUG:
        buffer = io.StringIO()
        print(*args, **kwargs, file=buffer)
        print(textwrap.indent(buffer.getvalue(), "  " * INDENT), end="")

def warn(*args):
    # debug but in red
    print("\033[91m", *args, "\033[0m")


class Node:
    def __init__(self, code: CodeType, op_idx: int, offset: int, opname: str, arg: int):
        # Two choices when walking the graph, either go to the next node or
        # jump to a different node in case of a (un)conditional jump
        self.next: Optional[Node] = None
        self.jumps: Set[Node] = set()

        # Previous nodes
        self.prev: Set[Node] = set()

        # The node's code
        self.code = code
        self.opname = opname
        self.arg = arg
        self.op_idx = op_idx
        self.offset = offset

        self.stmts: List[ast.AST] = []
        self.stack: List[ast.AST] = None

        # The node's position in the topological sort
        self.index: int = -1
        self.visited: bool = False
        self.loops = set()
        self.is_conditional_while = False
        self.jump_test = None
        self._container = self

    @property
    def container(self):
        if self._container is not self:
            self._container = self._container.container
        return self._container

    def successors(self) -> Set["Node"]:
        if self.next:
            return {self.next, *self.jumps}
        return self.jumps

    def add_stmt(self, stmt):
        debug("Add stmt", self, ":", stmt)
        try:
            debug(
                textwrap.indent(astunparse.unparse(ast.fix_missing_locations(stmt)), "  ")
            )
        except:
            warn("Could not unparse", stmt, "in", self)
        self.stmts.append(stmt)

    def extend_stmts(self, stmts):
        for stmt in stmts:
            self.add_stmt(stmt)

    def add_stack(self, item):
        if self.stack is None:
            self.stack = []
        debug("Add stack", self, ":", item)
        self.stack.append(item)

    def pop_stack(self):
        return self.stack.pop()

    @property
    def arg_value(self):
        opname = self.opname
        if opname.startswith('LOAD_') or opname.startswith('STORE_'):
            opname = opname[5:] if opname.startswith('LOAD_') else opname[6:]

            if opname == "FAST":
                return self.code.co_varnames[self.arg]
            elif opname in ("NAME", "GLOBAL"):
                return self.code.co_names[self.arg]
            elif opname == "DEREF":
                return (self.code.co_cellvars + self.code.co_freevars)[self.arg]
            elif opname == "CONST":
                return repr(self.code.co_consts[self.arg])
            elif opname in ("ATTR", "METHOD"):
                return self.code.co_names[self.arg]
        elif opname.startswith("COMPARE_OP"):
            return dis.cmp_op[self.arg]
        else:
            return self.arg

    def contract_backward(self):
        """
        Merge the node with its predecessor
        """

        # If the node has a single predecessor, merge it with that node

        prev_node = next((n for n in self.prev if n.next is self), None)
        if not self.prev:
            self.loops = frozenset()
        if not (
            prev_node
            and (
                (len(self.prev) == 1) or # and not prev_node.jumps) or
                prev_node.opname in ("NOP",)
            )
        ):
            debug(
                "Could not contract", prev_node, "!<<<!", self, "| next:", self.next, "jumps:", self.jumps, "| prev:", self.prev,
            )
            return None

        prev_node._container = self._container
        debug(
            "Contract backward", prev_node, "<<<", self, "| next:", self.next, ", jumps:", self.jumps, "| prev:", self.prev,
        )
        self.prev.remove(prev_node)
        for pred_pred in prev_node.prev:
            if pred_pred.next is prev_node:
                pred_pred.next = self
            pred_pred.jumps = {
                self if jump is prev_node else jump for jump in pred_pred.jumps
            }
            self.prev.add(pred_pred)

        self.jumps = {
            (self if n is prev_node else n)
            for n in self.jumps | (prev_node.jumps - {self})
        }

        for succ in (self.next, *self.jumps):
            if not succ:
                continue
            if prev_node in succ.prev:
                succ.prev.remove(prev_node)
                succ.prev.add(self)

        self.stmts = prev_node.stmts + self.stmts
        debug("After contraction", self, "| next:", self.next, "jumps:", self.jumps, "| prev:", self.prev)

        return prev_node

    def remove(self):
        """
        Remove the node from the graph
        """
        debug("Remove node", self, "|", self.next, self.jumps, "|", self.prev)
        successors = set((self.next, *self.jumps) if self.next else self.jumps)
        successors.discard(self)
        for succ in successors:
            if not succ:
                continue
            succ.prev.remove(self)
            for pred in self.prev:
                if pred is not self:
                    succ.prev.add(pred)
            print("Now", succ, "predecessors are", succ.prev)
        for pred in self.prev:
            pred.jumps |= successors
            pred.jumps.discard(self)
            if pred.next is self:
                pred.next = self.next
                pred.jumps.discard(self.next)

    @classmethod
    def from_code(cls, code: CodeType, prune: bool = False):
        bytes = code.co_code
        offset = 0
        graph = {}

        while offset < len(bytes):
            op_idx = offset
            op, arg = bytes[offset], bytes[offset + 1]
            opname = dis.opname[op]
            offset += 2

            ex_arg_count = 0
            ex_arg = 0
            while opname == "EXTENDED_ARG":
                ex_arg = arg << (8 * (ex_arg_count + 1))
                op, arg = bytes[offset], bytes[offset + 1]
                opname = dis.opname[op]
                offset += 2
            arg += ex_arg

            if sys.version_info >= (3, 10) and opname in hasjabs:
                arg *= 2

            block = cls(code, op_idx, offset, opname=opname, arg=arg)
            for i in range(op_idx, offset, 2):
                graph[i] = block

        # graph[offset] = Block(code, offset, offset + 2, opname="END", arg=0, graph=graph)

        for block in graph.values():
            opname = block.opname
            arg = block.arg

            if opname in ("RETURN_VALUE",):
                pass
            elif opname == "JUMP_FORWARD":
                block.jumps.add(graph[block.offset + arg])
            elif opname == "JUMP_ABSOLUTE":
                block.jumps.add(graph[arg])
            elif opname in (
                "POP_JUMP_IF_TRUE",
                "POP_JUMP_IF_FALSE",
                "JUMP_IF_NOT_EXC_MATCH",
            ):
                block.next = graph[block.offset]
                block.jumps.add(graph[arg])
            elif opname in (
                  "FOR_ITER",
                  "SETUP_FINALLY",
                  "SETUP_LOOP",
            ):
                block.next = graph[block.offset]

                if graph[block.offset + arg].opname == "POP_BLOCK":
                    block.jumps.add(graph[block.offset + arg + 2])
                else:
                    block.jumps.add(graph[block.offset + arg])
            else:
                if block.offset in graph:
                    block.next = graph[block.offset]

            if block.next:
                block.next.prev.add(block)
            for jump in block.jumps:
                jump.prev.add(block)

        root = graph[0]
        root = rewire_break_loop(root)

        index = 0
        sorted_nodes = []
        for node in graph_sort(root):
            if (
                  node.opname == "NOP" or
                  node.opname == "RERAISE" and node.arg == 0 or
                  node.opname == "POP_BLOCK" or
                  node.opname == "SETUP_LOOP"

            ):
                if node.next:
                    for n in node.prev:
                        if n.next is node:
                            n.next = node.next
                        n.jumps = {node.next if j is node else j for j in n.jumps} - {n.next}
                    node.next.prev = (node.next.prev | node.prev) - {node}
            else:
                node.index = index
                index += 1
                sorted_nodes.append(node)

        graph_nodes = set(sorted_nodes)
        for node in sorted_nodes:
            node.prev &= graph_nodes
        #detect_loops(sorted_nodes[0])

        root = sorted_nodes[0]

        if prune:
            root = contract_jumps(root)

        return root


    def __repr__(self):
        return f"[{self.op_idx}]{self.opname}({self.arg_value})"

    def draw(self, prog=None):
        from IPython.core.display import HTML
        import networkx as nx

        g = nx.DiGraph()

        visited = set()

        def rec(node: Node, pos):
            if node in visited:
                return
            visited.add(node)
            try:
                source = node.to_source().split("\n")
            except:
                source = ["!ERROR!"]
            max_line = max(len(line) for line in source)
            label = "\n".join([
                f"[{node.op_idx}]{'✓' if node.visited else ''}|{len(node.stack) if node.stack else 0}☰|{len(node.prev)}↣",
                #f"↺({','.join(str(i) for i in sorted(node.loops))})",
                f"{node.opname}({node.arg_value})",
                "------------",
                *[line.ljust(max_line) for line in source],
            ])
            g.add_node(
                node,
                pos=",".join(map(str, pos)) + "!",
                label=label,
                fontsize=10,
                color="red" if node is self else "black",
            )
            # positions[node] = pos
            if node.next:
                g.add_edge(node, node.next, label="next", fontsize=10)
                rec(node.next, (pos[0], pos[1] + 1))
            for jump in node.jumps:
                g.add_edge(node, jump, label="jump", fontsize=10)
                rec(jump, (pos[0], pos[1] + 1))

            # for p in node.prev:
            #     rec(p, (pos[0], pos[1] - 1))

        first = detect_first_node(self)
        rec(first, (0, 0))
        agraph = nx.nx_agraph.to_agraph(g)
        # Update some global attrs like LR rankdir, box shape or monospace font
        agraph.graph_attr.update(rankdir="LR", fontname="Menlo")
        agraph.node_attr.update(shape="box", fontname="Menlo")
        agraph.edge_attr.update(fontname="Menlo")
        svg = agraph.draw(prog=DRAW_PROG if prog is None else prog, format="svg")
        return HTML(f'<div style="max-height: 100%; max-width: initial">{svg.decode()}</div>')

    def to_source(self):
        res = []
        for stmt in self.stmts:
            try:
                stmt = ast.fix_missing_locations(stmt)
            except AttributeError:
                pass
            res.append(astunparse.unparse(stmt).strip("\n"))
        return "\n".join(res)

    def last_stmts(self):
        if self.stmts:
            return self.stmts
        prev_visited = [n for n in self.prev if n.visited]
        if len(prev_visited) != 1:
            return self.stmts
        prev = next(iter(prev_visited), None)
        return prev.last_stmts()

    def can_process_node(self, stop_nodes: Container["Node"] = ()):
        if self in stop_nodes:
            return False
        prev_visited = [n for n in self.prev if n.visited]
        if len(prev_visited) > 1:
            return False
        return True

    # noinspection PyMethodParameters,PyMethodFirstArgAssignment
    def _run(
          self: "Node",
          loop_heads: Tuple["Node"] = (),
          stop_nodes: Container["Node"] = (),
    ):
        """
        Convert the graph into an AST
        """
        if not self.can_process_node(stop_nodes):
            return

        node = self

        while True:
            debug("-------------\nProcessing", node, "|", "next:", node.next, "| jumps:", node.jumps,
                  "| prev:", node.prev, "| loops:", loop_heads)
            node.visited = True
            prev_visited = [n for n in node.prev if n.visited]
            prev_unvisited = [n for n in node.prev if not n.visited]
            assert len(prev_visited) <= 1, "Too many prev visited"

            # This marks the start of a loop
            if len(prev_unvisited):
                loop_heads = (*loop_heads, node)

            # Propagate the stack
            if node.stack is None:
                if prev_visited and prev_visited[0].stack is not None:
                    node.stack = list(prev_visited[0].stack)
                else:
                    node.stack = []

            # Process the node depending on its opname
            if node.opname == "LOAD_CLOSURE":
                node.add_stack(None)
            elif node.opname.startswith("LOAD_"):
                process_binding_(node)
            elif node.opname.startswith("STORE_"):
                process_store_(node)
            elif node.opname.startswith("DELETE_") or node.opname.startswith("DEL_"):
                process_binding_(node)
                node.add_stmt(ast.Delete([node.pop_stack()]))
            elif node.opname == "RETURN_VALUE":
                node.add_stmt(ast.Return(node.pop_stack()))
            elif node.opname == "SETUP_FINALLY":
                raise NotImplementedError()
            elif node.opname == "RERAISE":
                node.add_stmt(Reraise())
            elif node.opname == "POP_BLOCK":
                pass
            elif node.opname == "GET_ITER":
                # During eval, pop and applies iter() to TOS
                pass
            elif node.opname == "COMPARE_OP":
                if compareop_to_ast[node.arg] != "exception match":
                    right = node.pop_stack()
                    left = node.pop_stack()
                else:
                    left = node.pop_stack()
                    # right = stack.pop()[1]
                    right = None
                node.add_stack(
                    ast.Compare(
                        left=left,
                        ops=[compareop_to_ast[node.arg]],
                        comparators=[right],
                    ),
                )
            elif node.opname in binop_to_ast:
                right = node.pop_stack()
                left = node.pop_stack()
                node.add_stack(
                    ast.BinOp(left=left, op=binop_to_ast[node.opname], right=right),
                )
            elif node.opname == "CONTAINS_OP":
                right = node.pop_stack()
                left = node.pop_stack()
                node.add_stack(
                    ast.Compare(
                        left=left,
                        ops=[ast.In() if node.arg == 0 else ast.NotIn()],
                        comparators=[right],
                    ),
                )
            elif node.opname == "IS_OP":
                right = node.pop_stack()
                left = node.pop_stack()
                node.add_stack(
                    ast.Compare(
                        left=left,
                        ops=[ast.Is() if node.arg == 0 else ast.IsNot()],
                        comparators=[right],
                    ),
                )
            elif node.opname == "BINARY_SUBSCR":
                slice = node.pop_stack()
                value = node.pop_stack()
                node.add_stack(ast.Subscript(value, slice))
            elif node.opname in unaryop_to_ast:
                value = node.pop_stack()
                node.add_stack(ast.UnaryOp(op=unaryop_to_ast[node.opname], operand=value))
            elif node.opname in inplace_to_ast:
                right = node.pop_stack()
                left = node.pop_stack()
                node.add_stack(
                    ast.AugAssign(target=left, op=inplace_to_ast[node.opname], value=right),
                )
            elif node.opname == "BUILD_SLICE":
                values = [node.pop_stack() for _ in range(node.arg)][::-1]
                if node.arg == 2:
                    values = values + [None]
                node.add_stack(ast.Slice(*values))
            elif node.opname == "BUILD_LIST":
                items = [node.pop_stack() for _ in range(node.arg)][::-1]
                node.add_stack(ast.List(items))
            elif node.opname == "BUILD_TUPLE":
                items = [node.pop_stack() for _ in range(node.arg)][::-1]
                node.add_stack(ast.Tuple(items))
            elif node.opname == "BUILD_CONST_KEY_MAP":
                keys = [ast.Constant(key, kind=None) for key in node.pop_stack().value]
                values = [node.pop_stack() for _ in range(node.arg)][::-1]
                node.add_stack(ast.Dict(keys, values))
            elif node.opname == "BUILD_SET":
                items = [node.pop_stack() for _ in range(node.arg)][::-1]
                node.add_stack(ast.Set(items))
            elif node.opname == "BUILD_MAP":
                keys = []
                values = []
                for _ in range(node.arg):
                    values.append(node.pop_stack())
                    keys.append(node.pop_stack())
                node.add_stack(ast.Dict(keys[::-1], values[::-1]))
            elif node.opname == "LIST_TO_TUPLE":
                value = node.pop_stack()
                node.add_stack(ast.Tuple(value.elts))
            elif node.opname == "UNPACK_SEQUENCE":
                value = node.pop_stack()
                for i in reversed(range(node.arg)):
                    node.add_stack(Unpacking(value, counter=i))
            elif node.opname == "UNPACK_EX":
                # FROM Python's doc:
                # The low byte of counts is the number of values before the list value,
                # the high byte of counts the number of values after it. The resulting
                # values are put onto the stack right-to-left.
                value = node.pop_stack()
                before, after = node.arg & 0xFF, node.arg >> 8

                for i in reversed(range(before + after + 1)):
                    node.add_stack(Unpacking(value, counter=i, starred=i == before))
            elif node.opname in ("LIST_EXTEND", "SET_UPDATE"):
                items = node.pop_stack()
                if isinstance(items, ast.Constant):
                    items = [ast.Constant(x) for x in items.value]
                elif hasattr(items, 'elts'):
                    items = items.elts
                else:
                    items = [ast.Starred(items)]
                obj = node.stack[-node.arg]
                obj = type(obj)(elts=[*obj.elts, *items])
                node.stack[-node.arg] = obj
            elif node.opname in ("DICT_UPDATE", "DICT_MERGE"):
                items = node.pop_stack()
                if isinstance(items, ast.Constant):
                    items = [(ast.Name(n), ast.Constant(v)) for n, v in items.value.items()]
                #elif hasattr(items, 'keys'):
                #    items = [(k, v) for k, v in zip(items.keys, items.values)]
                else:
                    items = [(None, items)]
                obj = node.stack[-node.arg]
                assert isinstance(obj, ast.Dict)
                obj = ast.Dict([*obj.keys, *(k for k, _ in items)],
                               [*obj.values, *(v for _, v in items)])
                node.stack[-node.arg] = obj
            # TODO: check in for/while loop ?
            elif node.opname in ("LIST_APPEND", "SET_ADD"):
                value = node.pop_stack()
                collection = node.stack[-node.arg]
                # if we can loop to the collection beginning
                if loop_heads and explore_until(node, {*loop_heads, collection}) is loop_heads[-1]:
                    node.add_stmt(ComprehensionBody(value, collection))
                else:
                    assert hasattr(collection, 'elts')
                    collection = type(collection)(elts=[*collection.elts, value])
                    node.stack[-node.arg] = collection
            elif node.opname == "MAP_ADD":
                value = node.pop_stack()
                key = node.pop_stack()
                collection = node.stack[-node.arg]
                # if we can loop to the collection beginning
                if loop_heads and explore_until(node, {*loop_heads, collection}) is loop_heads[-1]:
                    node.add_stmt(ComprehensionBody((key, value), collection))
                else:
                    assert hasattr(collection, 'elts')
                    collection = type(collection)(
                        keys=[*collection.keys, key],
                        values=[*collection.values, value],
                    )
                    node.stack[-node.arg] = collection
            elif node.opname == "YIELD_VALUE":
                node.add_stmt(ast.Expr(ast.Yield(node.pop_stack())))
            elif node.opname == "MAKE_FUNCTION":
                assert node.arg in (0, 8), node.arg
                node.pop_stack()  # function name
                func_code: ast.Constant = node.pop_stack()
                if node.arg == 8:
                    node.pop_stack()
                assert isinstance(func_code, ast.Constant)
                code = func_code.value
                function_node = Node.from_code(code)
                if DEBUG:
                    display(function_node.draw())
                sub_function_body = function_node.run().stmts

                node.add_stack(ast.FunctionDef(
                    name=code.co_name,
                    args=ast.arguments(
                        args=[
                            ast.arg(arg=arg, annotation=None)
                            for arg in code.co_varnames[: code.co_argcount]
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                        posonlyargs=[],
                    ),
                    body=sub_function_body,
                    decorator_list=[],
                    returns=None,
                ))
            elif node.opname in ("CALL_FUNCTION", "CALL_METHOD"):
                args = [node.pop_stack() for _ in range(node.arg)][::-1]
                func = node.pop_stack()
                if isinstance(func, ast.FunctionDef):
                    assert len(func.body) == 2
                    cls: Optional[Type[ast.AST]] = None
                    tree = RewriteComprehensionArgs(args, cls).visit(func)

                    if len(func.body) == 1 or isinstance(func.body[1], ast.Return):
                        tree = func.body[0]
                    node.add_stack(tree)
                else:
                    node.add_stack(
                        ast.Call(
                            func=func,
                            args=args,
                            keywords=[],
                        ),
                    )
            elif node.opname == "CALL_FUNCTION_KW":
                keys = node.pop_stack().value
                values = [node.pop_stack() for _ in range(len(keys))][::-1]
                args = [node.pop_stack() for _ in range(node.arg - len(keys))][::-1]
                func = node.pop_stack()
                node.add_stack(
                    ast.Call(
                        func=func,
                        args=args,
                        keywords=[
                            ast.keyword(arg=key, value=value)
                            for key, value in zip(keys, values)
                        ],
                    ),
                )
            elif node.opname == "CALL_FUNCTION_EX":
                if node.arg & 0x01:
                    kwargs = node.pop_stack()
                    args = node.pop_stack()
                else:
                    kwargs = None
                    args = node.pop_stack()
                func = node.pop_stack()
                if isinstance(kwargs, ast.Dict):
                    keywords = [
                        ast.keyword(
                            arg=key.value if key is not None else None, value=value
                        )
                        for key, value in zip(kwargs.keys, kwargs.values)
                    ]
                else:
                    keywords = [ast.keyword(arg=None, value=kwargs)]
                if hasattr(args, "elts"):
                    args = args.elts
                elif isinstance(args, ast.Constant) and isinstance(
                    args.value, (tuple, list)
                ):
                    args = [ast.Constant(value=elt, kind=True) for elt in args.value]
                node.add_stack(
                    ast.Call(
                        func=func,
                        args=args,
                        keywords=keywords,
                    ),
                )
            elif node.opname == "NOP":
                pass
            elif node.opname == "DUP_TOP":
                node.add_stack(node.stack[-1])
            elif node.opname == "ROT_TWO":
                s = node.stack
                s[-1], s[-2] = s[-2], s[-1]
            elif node.opname == "ROT_THREE":
                s = node.stack
                s[-1], s[-2], s[-3] = s[-2], s[-3], s[-1]
            elif node.opname == "ROT_FOUR":
                s = node.stack
                s[-1], s[-2], s[-3], s[-4] = s[-2], s[-3], s[-4], s[-1]
            elif node.opname == "POP_TOP":
                item = node.pop_stack()
                if item and not getattr(item, '_dumped', False):
                    node.add_stmt(ast.Expr(item))
            elif node.opname == "POP_EXCEPT":
                node.pop_stack()
            elif node.opname == "FORMAT_VALUE":
                fmt_spec = None
                conversion = -1
                if node.arg & 0x03 == 0x00:
                    conversion = -1
                elif node.arg & 0x03 == 0x01:
                    conversion = 115
                elif node.arg & 0x03 == 0x02:
                    conversion = 114
                elif node.arg & 0x03 == 0x03:
                    conversion = 97
                if node.arg & 0x04 == 0x04:
                    fmt_spec = node.pop_stack()
                    if not isinstance(fmt_spec, ast.JoinedStr):
                        fmt_spec = ast.JoinedStr([fmt_spec])
                value = node.pop_stack()
                node.add_stack(
                    ast.JoinedStr(
                        [
                            ast.FormattedValue(
                                value=value,
                                conversion=conversion,
                                format_spec=fmt_spec,
                            )
                        ]
                    ),
                )
            elif node.opname == "BUILD_STRING":
                values = [node.pop_stack() for _ in range(node.arg)][::-1]
                values = [
                    part
                    for v in values
                    for part in (v.values if isinstance(v, ast.JoinedStr) else [v])
                ]
                node.add_stack(ast.JoinedStr(values=values))
            elif node.opname == "GEN_START":
                # Python docs say: "Pops TOS. The kind operand corresponds to the type
                # of generator or coroutine. The legal kinds are 0 for generator, 1 f
                # or coroutine, and 2 for async generator."
                # However, there are no item in the stack (from the bytecode
                # perspective) at the start of a generator comprehension function
                # if node.index > 0:
                #    node.pop_stack()
                pass

            elif node.opname in ("POP_JUMP_IF_TRUE", "POP_JUMP_IF_FALSE", "JUMP_IF_NOT_EXC_MATCH"):
                test = node.pop_stack()
                # node.jump_test = test

                body_node = node.next
                else_node: Node = next(iter(node.jumps))

                meet_nodes = lowest_common_successors(
                    body_node,
                    else_node,
                    stop_nodes={*stop_nodes, node},
                )
                assert len(meet_nodes) <= 1

                # if loop_heads:
                #     if_loop_head = explore_until(if_node, loop_heads)
                #     else_loop_head = explore_until(else_node, loop_heads)
                # else:
                #     if_loop_head = else_loop_head = None

                body_node = body_node._run(
                    loop_heads=loop_heads,
                    stop_nodes={*stop_nodes, *meet_nodes},
                )
                else_node = else_node._run(
                    loop_heads=loop_heads,
                    stop_nodes={*stop_nodes, *meet_nodes},
                )

                if DEBUG:
                    display(node.draw())

                # In case where in an inline condition, the branches stacks should
                # contain more elements than the test stack
                body_item = (
                    body_node.pop_stack()
                    if body_node and len(body_node.stack) > len(node.stack)
                    else None
                )
                else_item = (
                    else_node.pop_stack()
                    if else_node and len(else_node.stack) > len(node.stack)
                    else None
                )
                test_origin = get_origin(test)[0].container

                if body_item:
                    node.add_stack(ast.IfExp(
                        test=(
                            test
                            if node.opname == "POP_JUMP_IF_FALSE"
                            else ast.UnaryOp(
                                op=ast.Not(),
                                operand=test,
                            )
                        ),
                        body=body_item,
                        orelse=else_item,
                    ))
                else:
                    # Multiple cases here:
                    if body_node:
                        # - if the body_node has been processed, then we can use its stmts
                        body_stmts = body_node.stmts or [ast.Pass()]
                    elif meet_nodes:
                        print("MEET NODES", "=>", "pass")
                        body_stmts = [ast.Pass()]
                    else:
                        next_node = node.next
                        if loop_heads and next_node is loop_heads[-1]:
                            # - if the test brings us back to the top of the last loop
                            body_stmts = [ast.Continue()]
                        elif loop_heads and next_node in loop_heads[:-1]:
                            # - if the test brings us back to the top of a higher loop
                            body_stmts = [ast.Break()]
                        elif loop_heads:
                            # - if we're in a loop but the test brings to a loop-free zone
                            # TODO: should we check if a break brings us to the else node
                            #       in case of while [...] loops ?
                            body_stmts = [ast.Break()]
                        else: # if not loop_heads
                            # - if we're not in a loop
                            body_stmts = [ast.Pass()]


                    # Multiple cases here:
                    if else_node:
                        # - if the else_node has been processed, we can use its stmts
                        else_stmts = else_node.stmts or [ast.Pass()]
                    # - if this was a simple if without break or continue or return
                    #   and else is empty, and does not have break/continue/... either
                    #   (otherwise the two nodes would not meet), don't add an else
                    #   statement
                    elif meet_nodes:
                        else_stmts = []
                    else:
                        # - if the body does not meet the else node due to a break,
                        #   continue, return, or something else, then we need to
                        #   inspect the various possible cases
                        jump_node = next(iter(node.jumps))
                        if loop_heads and jump_node is loop_heads[-1]:
                            # - if fail brings us back to the top of the last loop
                            else_stmts = [ast.Continue()]
                        elif loop_heads and jump_node in loop_heads[:-1]:
                            # - if fail brings us back to the top of a higher loop
                            else_stmts = [ast.Break()]
                        elif loop_heads:
                            # - if we're in a loop but fail brings to a loop-free zone
                            # TODO: should we check if a break brings us to the else
                            #       node in case of while [...] loops ?
                            else_stmts = [ast.Break()]
                        else: # if not loop_heads
                            # - if we're not in a loop
                            else_stmts = []


                    # To have a full if/else structure, we require that
                    # the two branches meet again at some point
                    has_else = bool(meet_nodes)  #  or else_loop_head is not None
                    node.add_stmt(
                        ast.If(
                            test=(
                                test
                                if node.opname != "POP_JUMP_IF_TRUE"
                                else ast.UnaryOp(
                                    op=ast.Not(),
                                    operand=test,
                                )
                            ),
                            body=body_stmts,
                            orelse=else_stmts if has_else else []
                        )
                    )
                    if not has_else:
                        node.stmts.extend(else_stmts)

                if body_node:
                    body_node.remove()
                if else_node:
                    else_node.remove()

                if DEBUG:
                    display(node.draw())
            else:
                raise NotImplementedError(node.opname)

            # Handle while loops by detecting cycles of length 1
            prev_visited = [n for n in node.prev if n.visited]
            debug("STACKS", "node", node, len(node.stack), node.stack, "prev", prev_visited, len(prev_visited[-1].stack) if prev_visited else 0, prev_visited[-1].stack if prev_visited else None)
            debug("LOOP HEADS", "node", node, "PREV", node.prev, "=>", loop_heads)
            while not prev_visited or len(node.stack) <= len(prev_visited[-1].stack):
                if self.container is not node:
                    prev = node.contract_backward()
                else:
                    prev = None
                if not prev and not node.prev == {node}:
                    break
                if loop_heads and loop_heads[-1] is prev:
                    loop_heads = (*loop_heads[:-1], node)
                if node in node.jumps:
                    node.jumps.remove(node)
                    node.prev.remove(node)

                    body = node.stmts
                    node.stmts = []
                    node.add_stmt(
                        ast.While(
                            test=ast.Constant(value=True, kind=None),
                            body=body,
                            orelse=[],
                            _loop_head=node,
                        )
                    )

                    if loop_heads and loop_heads[-1] is node:
                        loop_heads = loop_heads[:-1]

                    prev_unvisited = [n for n in node.prev if not n.visited]
                    if len(prev_unvisited):
                        loop_heads = (*loop_heads, node)
                prev_visited = [n for n in node.prev if n.visited]
                if DEBUG:
                    display(node.draw())
                debug("STACKS", "node", node, len(node.stack), "prev", prev_visited, len(prev_visited[-1].stack) if prev_visited else 0)

            if DEBUG:
                display(node.draw())

            debug("::: done", node, "|", node.next, node.jumps, "|", node.prev)

            if not node.next:
                if loop_heads:
                    jump_to_head = {
                        n: explore_until(n, (*loop_heads, *stop_nodes))
                        for n in node.jumps
                    }
                    debug("CANDIDATE JUMPS", node, "=>", jump_to_head, "LOOP HEADS", loop_heads)
                    same_level_jumps = [
                        jump for jump, head in jump_to_head.items()
                        if head is loop_heads[-1] or (head is None and len(jump.prev) == 1)
                    ]
                    debug("SAME LEVEL JUMPS", node, "=>", same_level_jumps, "LOOP HEADS", loop_heads)
                else:
                    same_level_jumps = list(node.jumps)

                if len(same_level_jumps) > 1:
                    warn("MULTIPLE CHOICE FOR JUMP", same_level_jumps)
                if same_level_jumps:
                    node.next = sorted(same_level_jumps,
                                       key=lambda j: (0 if j.index > node.index else 1, j.index))[0]
                    node.jumps.remove(node.next)
                # ARE WE SURE OF THIS ?
                # If there is only one outgoing edge, jumping on a different level
                # set it as next but don't continue exploring
                elif len(node.jumps) == 1:
                    node.next = next(iter(node.jumps))
                    node.jumps.remove(node.next)
                    #if node.is_virtual:
                    #    node.next.prev.discard(node)
                    print("Stop after", node, "because not same level")
                    break

            # if node.is_virtual:
            #     for succ in node.jumps:
            #         succ.prev.discard(node)
            if node.next and not node.next.visited and not node.next in stop_nodes:
                node: Node = node.next
            else:
                # if node.is_virtual and node.next:
                #     node.next.prev.discard(node)
                print("Stop after", node, ": next=", node.next, "is visited", node.next.visited if node.next else "-", "| stop nodes: ", stop_nodes)

                if loop_heads and node.next is loop_heads[-1]:
                    # we're brings us back to the top of the last loop
                    node.add_stmt(ast.Continue())
                elif node.next in loop_heads[:-1]:
                    # we're brings us back to the top of a higher loop
                    print("Next node is a loop head, break", node)
                    node.add_stmt(ast.Break())
                elif node.next in stop_nodes:
                    # we're brings us back to a loop-free zone
                    print("Next node is a stop node, break", node)
                    node.add_stmt(ast.Break())
                break

        return node

    def run(self) -> "Node":
        """Decompile a code object"""
        while_fusions = {}
        node = self._run()

        node.stmts = [
            #WhileBreakFixer(while_fusions).visit(
            (RemoveLastContinue().visit(stmt))
            for stmt in node.stmts
        ]

        return node


def decompile(code: CodeType, prune: bool=False) -> str:
    """Decompile a code object"""
    node = Node.from_code(code, prune=prune)
    if DEBUG:
        print("DECOMPILE", node)
        display(node.draw())
    return node.run().to_source()


def detect_first_node(root):
    visited = set()

    best = root

    def rec(node):
        nonlocal best

        if node in visited:
            return

        visited.add(node)

        if node.index < best.index:
            best = node

        for succ in (node.next, *node.jumps, *node.prev):
            if succ is None:
                continue
            rec(succ)

    rec(root)

    return best

def explore_until(root, stops):
    if not stops:
        return None

    stops = list(stops)
    visited = set()

    def rec(node):
        if node in stops:
            return node

        if node in visited:
            return None

        visited.add(node)

        results = [
            rec(succ)
            for succ in (node.next, *node.jumps)
            if succ is not None
        ]
        res = min(filter(bool, results), key=stops.index, default=None)
        return res

    return rec(root)


def process_binding_(node, save_origin=True):
    # assert len(block.pred) <= 1
    opname = node.opname
    arg = node.arg
    code = node.code
    idx = node.op_idx
    opname = opname.split("_")[1]

    origin = (dict(
        _origin_offset=idx,
        _origin_node=node,
    ) if save_origin else {})

    if opname == "FAST":
        node.add_stack(
            ast.Name(
                id=code.co_varnames[arg], **origin,
            )
        )
    elif opname in ("NAME", "GLOBAL"):
        node.add_stack(
            ast.Name(
                id=code.co_names[arg], **origin,
            )
        )
    elif opname == "DEREF":
        node.add_stack(
            ast.Name(
                id=(code.co_cellvars + code.co_freevars)[arg], **origin,
            )
        )
    elif opname == "CONST":
        const_value = code.co_consts[arg]
        if isinstance(const_value, frozenset):
            const_value = set(const_value)
        node.add_stack(
            ast.Constant(
                value=const_value,
                kind=None, **origin,
            )
        )
    # ATTRIBUTES
    elif opname in ("ATTR", "METHOD"):
        value = node.pop_stack()
        node.add_stack(
            ast.Attribute(
                value=value,
                attr=code.co_names[arg], **origin,
            )
        )
    elif opname in ("SUBSCR",):
        value = node.pop_stack()
        node.add_stack(
            ast.Subscript(
                slice=value,
                value=node.pop_stack(), **origin,
            )
        )
    else:
        raise ValueError("Unknown opname", opname) # pragma: no cover


def process_store_(node: Node):
    process_binding_(node)
    target = node.pop_stack()
    value = node.pop_stack()
    if isinstance(value, ast.AugAssign):
        node.add_stmt(value)
    elif isinstance(value, ast.FunctionDef) and isinstance(target, ast.Name):
        node.add_stmt(value)
    else:
        last_stmts = node.last_stmts()#next(iter(node.prev)).stmts if len(node.prev) == 1 else []

        unpacking = value if isinstance(value, Unpacking) else None
        if unpacking:
            value = value.value
            target = ast.Starred(target) if unpacking.starred else target
            multi_targets = [ast.Tuple([target])]
        else:
            multi_targets = [target]


        try:
            is_multi_assignment = (
                len(last_stmts)
                and isinstance(last_stmts[-1], ast.Assign)
                and get_origin(value)[1] <= get_origin(last_stmts[-1].targets)[1]
            )
            debug(f"ORIGIN of {ast.dump(value)}", get_origin(value)[1], f"vs ORIGIN of last {ast.dump(last_stmts[-1])}", get_origin(last_stmts[-1].targets)[1])
        except Exception as e:
            is_multi_assignment = False

        debug("VALUE", value, "LAST", last_stmts, "MULTI", multi_targets, "UNPACKING", unpacking, "=> IS_MULTI:", is_multi_assignment)
        if is_multi_assignment:
            prev = last_stmts.pop()
            prev_multi_targets = prev.targets

            if (
                (not unpacking and prev.value is value)
                or (
                    unpacking
                    and (
                        len(prev_multi_targets) == 0
                        or not isinstance(prev_multi_targets[-1], ast.Tuple)
                    )
                )
                or (unpacking and len(prev_multi_targets[-1].elts) > unpacking.counter)
            ):
                multi_targets = prev_multi_targets + multi_targets
            else:
                if len(prev_multi_targets) > 0 and isinstance(
                    prev_multi_targets[-1], ast.Tuple
                ):
                    multi_targets = [
                        *prev_multi_targets[:-1],
                        ast.Tuple(prev_multi_targets[-1].elts + [target]),
                    ]
                else:
                    multi_targets = [
                        *prev_multi_targets[:-1],
                        ast.Tuple([prev_multi_targets[-1], target]),
                    ]
                if not unpacking:
                    if isinstance(prev.value, ast.Tuple):
                        value = ast.Tuple([*prev.value.elts, value], ctx=ast.Load())
                    else:
                        value = ast.Tuple([prev.value, value], ctx=ast.Load())
                # value is value

        node.add_stmt(
            ast.Assign(
                targets=multi_targets,
                value=value,
            ),
            # start=op_idx,
        )



def contract_jumps(root):
    queue = [root]
    seen = set()

    while queue:
        node = queue.pop(0)

        seen.add(node)

        if node.opname in ("JUMP_FORWARD", "JUMP_ABSOLUTE"):
            (jump_node,) = node.jumps
            root = jump_node if root is node else root
            for prev in node.prev:
                if prev.next is node:
                    prev.next = jump_node
                prev.jumps = {jump_node if x is node else x for x in prev.jumps}
            jump_node.prev = (jump_node.prev - {node}) | node.prev
        else:
            pass

        for succ in (node.next, *node.jumps):
            if succ not in seen and succ:
                queue.append(succ)

    return root


def rewire_break_loop(root):
    queue = [(root, [])]
    seen = set()

    while queue:
        node, loop_jumps = queue.pop(0)
        if not node or node in seen:
            continue
        seen.add(node)
        if node.opname == "SETUP_LOOP":
            #jump_node = next(iter(node.jumps))
            jump_node = node.jumps.pop()
            jump_node.prev.discard(node)
            queue.append((node.next, [*loop_jumps, jump_node]))
            queue.append((jump_node, loop_jumps))
        elif node.opname == "BREAK_LOOP":
            node.opname = "JUMP_ABSOLUTE"
            #node.next_is_virtual = True
            if node.next:
                node.next.prev.discard(node)
                node.next = None
            node.arg = None
            loop_jumps[-1].prev.add(node)
            node.jumps = {loop_jumps[-1]}
            queue.append((node.next, loop_jumps))
        else:
            queue.append((node.next, loop_jumps))
            for jump in node.jumps:
                queue.append((jump, loop_jumps))

    return root