"""metapatch without preset."""

import metapatch


class TestMetaPatch(metapatch.PatchGenerator):
    """Test metapatch."""

    title = "Test"
    description = "A test patch."

    testbool = metapatch.option("Boolean")
    testnumber = metapatch.option("Number", minimum=1, maximum=10)
    testchoice = metapatch.option(
        "Choice", choices=[("first", "First choice"), ("second", "Second choice")]
    )

    def generate(self) -> None:
        """Generate patch."""
        input_name = f"{self.testchoice.upper()}"
        self.add_controller("B32", 1)
        self.add_controller("E4", 2)
        self.add_circuit("copy", {"input": f"_{input_name}", "output": "_OUTPUT"})
