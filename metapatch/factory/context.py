"""String templates for the CLI script."""

import textwrap

from string import Template
from typing import Iterator, List
from contextlib import contextmanager

from .formatting import format_line

class_definition = Template("class ${classname}(${parent}):")

docstring_short = Template('"""${docstring}"""')

docstring_long = Template(
    '''""""${first_line}

${lines}
"""'''
)
function_defintion = Template("def ${function}(${args}) -> ${retval}:")

statement = Template("${statement}")
funcall = Template("${fun}(${params})")

assignment = Template("= ${val}")
classvar = Template('${var} = "${val}"')
fun_assignment = Template("${key}=${val}")
fun_quoted_assignment = Template('${key}="${val}"')
quoted_statement = Template("${statement}")
type_hint = Template(": ${val}")

module_import = Template("import ${modulename}")
selective_import = Template("from ${library} import ${modulename}")


TEMPLATES = {
    "class_definition": class_definition,
    "docstring_short": docstring_short,
    "docstring_long": docstring_long,
    "function_definition": function_defintion,
    "fun_assignment": fun_assignment,
    "fun_quoted_assignment": fun_quoted_assignment,
    "funcall": funcall,
    "statement": statement,
    "classvar": classvar,
    "assignment": assignment,
    "type_hint": type_hint,
    "module_import": module_import,
    "selective_import": selective_import,
    "quoted_statement": quoted_statement,
}


class TemplateContext:

    def __init__(self, level: int = 0) -> None:
        """Initialize context."""
        self.level = level
        self.buffer: List[str] = []
        num_spaces = level * 4
        # for debug
        # self.indent = f"{level}" * num_spaces
        self.indent = " " * num_spaces

    def apply_template(
        self,
        template_name: str,
        newlines: int = 1,
        comma: bool = False,
        **kwargs: str,
    ) -> None:
        """Apply a template with the given arguments."""
        result = self.eval_template(
            template_name, no_indent=False, comma=comma, **kwargs
        )
        self.buffer.append(result)
        for _ in range(0, newlines):
            self.buffer.append("\n")

    def eval_template(
        self,
        template_name: str,
        no_indent: bool = False,
        comma: bool = False,
        **kwargs: str,
    ) -> str:
        """Evaluate a template with the given arguments.

        Returns the string directly.
        """
        template = TEMPLATES[template_name]
        result = template.substitute(kwargs)
        if comma:
            result += ","
        if self.level > 0 and no_indent is False:
            result = textwrap.indent(result, self.indent)

        return result

    def add(self, value: str, newlines: int = 1) -> None:
        """Add something that is too simple for a template."""
        if self.level > 0:
            value = textwrap.indent(value, self.indent)
        self.buffer.append(value)
        for _ in range(0, newlines):
            self.buffer.append("\n")

    @contextmanager
    def next_level(self) -> Iterator["TemplateContext"]:
        """Go in one level."""
        next_context = type(self)(level=self.level + 1)
        yield next_context
        self.buffer.extend(next_context.buffer)

    def __str__(self) -> str:
        """Return the buffer as a string."""
        return "".join(self.buffer)
