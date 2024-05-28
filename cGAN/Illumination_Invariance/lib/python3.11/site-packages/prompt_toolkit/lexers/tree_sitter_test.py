import tree_sitter_languages
from tree_sitter import Parser


def _traverse_tree(tree):
    # https://github.com/tree-sitter/py-tree-sitter/issues/33#issuecomment-864557166
    cursor = tree.walk()

    reached_root = False
    while reached_root is False:
        yield cursor.node

        if cursor.goto_first_child():
            continue

        if cursor.goto_next_sibling():
            continue

        retracing = True
        while retracing:
            if not cursor.goto_parent():
                retracing = False
                reached_root = True

            if cursor.goto_next_sibling():
                retracing = False


source = "def hello(): ..."

p = Parser()
python = tree_sitter_languages.get_language("python")
p.set_language(python)

t = p.parse(source.encode())

for node in _traverse_tree(t):
    pass

# ---

from typing import Callable

from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text.base import StyleAndTextTuples

from .base import Lexer


class TreeSitterLexer(Lexer):
    def __init__(self, language: str = "python"):
        self.language = tree_sitter_languages.get_language(language)

    def lex_document(self, document: Document) -> Callable[[int], StyleAndTextTuples]:
        parser = Parser()
        p.set_language(self.language)

        tree = parser.parse(document.text)

        for node in _traverse_tree(tree):
            pass
