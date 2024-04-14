"""Generate boilerplate from templates."""

from textwrap import dedent
from typing import Dict, List, Optional
import keyword
from .context import TemplateContext
from .formatting import format_line

DEFAULT_TITLE = "Draft Patch Generator"
DEFAULT_DESCRIPTION = "A short description"
DEFAULT_CLASSNAME = "PatchGenerator"


TCircuitParams = Dict[str, str]
TCircuit = Dict[str, TCircuitParams]

TModDefinition = List[str]


def header(with_list: bool = False) -> str:
    """Generate header."""
    context = TemplateContext()
    module_docstring = "Patch generator auto-generated by the droid-metapatch utility."
    context.apply_template("docstring_short", docstring=module_docstring)
    if with_list:
        context.apply_template("selective_import", library="typing", modulename="List")
    context.apply_template("module_import", modulename="metapatch", newlines=2)

    return str(context)


def footer(classname: str = DEFAULT_CLASSNAME) -> str:
    """Generate footer."""
    context = TemplateContext()
    context.add('if __name__ == "__main__":')
    with context.next_level() as in_if:
        in_if.add(f"{classname}.run()")

    return str(context)


def pg_class(
    title: str = DEFAULT_TITLE,
    description: str = DEFAULT_DESCRIPTION,
    classname: str = DEFAULT_CLASSNAME,
) -> str:
    """Generate a patch generator class."""
    context = TemplateContext()
    docstring_start = "Auto-generated patch generator."
    docstring_continued = dedent(
        """Change this to something more meaningful.
    Also remember to add parameters and presets."""
    )
    # class PatchGenerator(metapatch.PatchGenerator):
    context.apply_template(
        "class_definition", classname=classname, parent="metapatch.PatchGenerator"
    )
    # Docstring
    with context.next_level() as next_level:
        next_level.apply_template(
            "docstring_long",
            first_line=docstring_start,
            lines=docstring_continued,
            newlines=2,
        )

        next_level.apply_template("classvar", var="title", val=title)
        next_level.apply_template(
            "classvar", var="description", val=description, newlines=2
        )
    return str(context)


def generate_section_function(
    circuits: List[TCircuit], functionname: str, section_name: str
) -> str:
    """Generate a section function."""
    # Start a local context one level in.
    context = TemplateContext(level=1)
    context.apply_template(
        "function_definition",
        function=functionname,
        args="self",
        retval="List[metapatch.DroidCircuit]",
    )

    with context.next_level() as in_function:
        in_function.apply_template(
            "docstring_short",
            docstring=f"Generate contents of section '{section_name}'.",
        )
        in_function.add("return [")
        with in_function.next_level() as in_circuit:
            for circuit in circuits:
                for circuitname, circuitparams in circuit.items():
                    in_circuit.buffer.append(
                        generate_circuit(
                            circuitname,
                            circuitparams,
                            level=in_circuit.level,
                            comma=True,
                        )
                    )
        in_function.add("]\n\n")

    return str(context)


def _generate_circuit_params(circuit: TCircuitParams, level: int = 2) -> str:
    """Generate the parameters for a circuit."""
    context = TemplateContext(level)
    for key, value in circuit.items():
        if key.startswith("__"):
            continue
        if key in keyword.kwlist:
            key += "_"
        statement = context.eval_template(
            "fun_quoted_assignment", key=key, val=value, comma=True
        )
        statement = format_line(statement) + "\n"
        context.buffer.append(statement)

    return str(context)


def generate_circuit(
    circuitname: str, circuit: TCircuitParams, level: int = 1, comma: bool = False
) -> str:
    """Generate a circuit."""
    context = TemplateContext(level)

    function_name = f"metapatch.circuits.{circuitname.capitalize()}("
    context.add(function_name)
    with context.next_level() as arg_context:
        arg_context.buffer.append(_generate_circuit_params(circuit, arg_context.level))
    if comma:
        context.add("),")
    else:
        context.add(")")
    return str(context)


def generate_pg_function(modules: TModDefinition) -> str:
    """Generate the generate function, and insert modules."""
    context = TemplateContext(level=1)
    context.apply_template(
        "function_definition", function="generate", args="self", retval="None"
    )
    docstring_first = "Patch generator function."
    docstring_lines = (
        "This function is the entrypoint function when generating the patch."
    )
    with context.next_level() as in_function:
        in_function.apply_template(
            "docstring_long", first_line=docstring_first, lines=docstring_lines
        )
        for index, module in enumerate(modules, start=1):
            in_function.apply_template(
                "funcall", fun="self.add_controller", params=f'"{module}", {index}'
            )

    return str(context)


def generate_transformation(
    funcname: str,
    sectionname: str,
    transforms: Dict[str, str],
    ignore: List[str],
    replace: Optional[Dict[str, str]] = None,
) -> str:
    """Generate a transformation.

    self.add_circuits(
        self.myfunc(),
        'my section',
        ignore=[
            'foo',
            'bar',
        ],
        replace=[
            ('foo', 'bar'),
        ]
        **transforms,

    )
    """
    context = TemplateContext(level=2)
    context.add("self.add_circuits(")
    with context.next_level() as in_fun:
        in_fun.apply_template("funcall", fun=f"self.{funcname}", params="", comma=True)
        in_fun.add(f'"{sectionname},"')
        for action, value in transforms.items():
            in_fun.apply_template("fun_assignment", key=action, val=value, comma=True)
        if ignore:
            in_fun.add("ignore=[")
            with in_fun.next_level() as in_ignore:
                for ignored in ignore:
                    in_ignore.apply_template(
                        "quoted_statement", statement=ignored, comma=True
                    )
            in_fun.add("],")

        if replace:
            in_fun.add("replace=[")
            with in_fun.next_level() as in_replace:
                for left, right in replace:
                    in_replace.add(f'("{left}", "{right}"),')
            in_fun.add("],")
    context.add(")", newlines=2)
    return str(context)


def generate_add_circuit(
    circuitname: str, circuit: TCircuitParams, level: int = 0
) -> str:
    """Generate a single add circuit statement."""
    context = TemplateContext(level)
    context.add("self.add(")
    with context.next_level() as in_fun:
        in_fun.add(f"metapatch.circuits.{circuitname.capitalize()}(")
        with in_fun.next_level() as in_args:
            in_args.buffer.append(
                _generate_circuit_params(circuit, level=in_args.level)
            )
        in_fun.add(")")
    context.add(")")
    return str(context)


def generate_add_controllers(controllers: TModDefinition, level: int = 0) -> str:
    """Generate the add controller statements."""
    context = TemplateContext(level)
    for index, module in enumerate(controllers, start=1):
        context.apply_template(
            "funcall", fun="self.add_controller", params=f'"{module}, {index}"'
        )
    return str(context)
