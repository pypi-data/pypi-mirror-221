"""
This module is adapted from the Python AST standard library.

It adds some hacks on top of the original `walk()` and `iter_child_nodes()`
functions: it returns the parent of each node when recursively walk all child
nodes.

The `walk()` function in this module comes from:
    https://github.com/python/cpython/blob/b87ccc38fe3ab4eca6e026b76f868db4d53c963f/Lib/ast.py#L380-L391

The `iter_child_nodes()` function in this module comes from:
    https://github.com/python/cpython/blob/b87ccc38fe3ab4eca6e026b76f868db4d53c963f/Lib/ast.py#L267-L278

There is an `ast.iter_fields()` function used in `iter_child_nodes()`.
This `ast.iter_fields()` function comes from:
    https://github.com/python/cpython/blob/b87ccc38fe3ab4eca6e026b76f868db4d53c963f/Lib/ast.py#L255-L264
"""
import ast
from collections import deque


def walk(node):
    """
    Recursively yield all descendant nodes in the tree starting at *node*
    (including *node* itself), in no specified order.  This is useful if you
    only want to modify nodes in place and don't care about the context.
    """
    todo = deque([(node, None)])
    while todo:
        node, parent = todo.popleft()
        todo.extend(iter_child_nodes(node))
        yield node, parent


def iter_child_nodes(node):
    """
    Yield all direct child nodes of *node*, that is, all fields that are nodes
    and all items of fields that are lists of nodes.
    """
    parent = node
    for name, field in ast.iter_fields(node):  # noqa: B007
        if isinstance(field, ast.AST):
            yield field, parent
        elif isinstance(field, list):
            for item in field:
                if isinstance(item, ast.AST):
                    yield item, parent
