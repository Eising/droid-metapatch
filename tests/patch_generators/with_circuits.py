"""Patch generator with new generated circuits."""

import metapatch
from metapatch import circuits


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
        self.add(circuits.Algoquencer(activity="0.5", length="16", trigger="G1.1"))

        self.add_section("Voice 2")
        self.add(
            circuits.Algoquencer(activity="0.5", length="16", trigger="G1.2"),
            comment="Another algoquencer",
        )
        self.add_section("Logic")
        self.add(circuits.Compare(input="I1", compare="1", ifequal="1", else_="0"))
