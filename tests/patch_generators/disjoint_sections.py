"""Disjoint sections."""

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
        self.add_section("Voice 1")
        self.add_circuit("copy", {"input": "I1", "output": "O1"})
        self.add_section("Buttons")
        self.add_circuit("button", {"button": "B1.1", "led": "L1.1"})
        self.add_section("Voice 2")
        self.add_circuit("copy", {"input": "I2", "output": "O2"})
        self.add_section("Buttons")
        self.add_circuit("button", {"button": "B1.2", "led": "L1.2"})
