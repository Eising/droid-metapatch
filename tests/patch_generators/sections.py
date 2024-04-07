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
    default = metapatch.preset(
        "My Default",
        parameters={"testbool": "True", "testnumber": "8", "testchoice": "first"},
    )

    def generate(self) -> None:
        """Generate patch."""
        input_name = f"{self.testchoice.upper()}"
        self.add_controller("B32", 1)
        self.add_controller("E4", 2)
        self.add_circuit("copy", {"input": f"_{input_name}", "output": "_OUTPUT"})
        self.add_section("Buttons", "This section contains buttons")
        self.add_circuit("button", {"button": "B1.1", "led": "L1.1"})
        self.add_circuit("button", {"button": "B1.2", "led": "L1.2"})
        self.add_section("Another section", "This is another section")
        self.add_circuit("copy", {}, "This is an empty copy circuit with a comment")
