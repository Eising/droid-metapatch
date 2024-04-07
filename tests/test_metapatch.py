"""Metapatch tests."""

import pytest
import metapatch


@pytest.fixture
def testpatch():
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

        def testfun(self) -> None:
            """Test function."""
            assert self.testbool is False
            assert self.testnumber == 7
            assert self.testchoice == "first"

        def generate(self) -> None:
            """Generate patch."""
            input_name = f"{self.testchoice.upper()}"
            self.add_controller("B32", 1)
            self.add_controller("E4", 2)
            self.add_circuit("copy", {"input": f"_{input_name}", "output": "_OUTPUT"})

    return TestMetaPatch


def test_opts(testpatch):
    mytest = testpatch(testbool=False, testchoice="first", testnumber=7)
    mytest.testfun()

    # test metaclass function
    synopsis = testpatch.synopsis
    assert isinstance(synopsis, dict)
    assert synopsis["title"] == "Test"
    assert isinstance(synopsis["sections"], list)
    options = synopsis["sections"][0]
    assert options["title"] == "Options"
    assert isinstance(options["options"], list)
    assert len(options["options"]) == 3
    assert isinstance(synopsis["presets"], list)
    assert synopsis["presets"][0]["name"] == "default"
    assert synopsis["presets"][0]["title"] == "My Default"
    preset = synopsis["presets"][0]
    assert isinstance(preset["parameters"], dict)
    preset_params = synopsis["presets"][0]["parameters"]
    assert "testbool" in preset_params


def test_preset(testpatch):
    """Test preset loading."""
    mypatch = testpatch.load_preset("default")
    assert mypatch.testbool is True


def test_generate(testpatch):
    """Test patch generation."""
    mytest = testpatch.load_preset("default")
    patch = str(mytest)
    assert patch == "[B32]\n[E4]\n\n[copy]\n    input = _FIRST\n    output = _OUTPUT\n"
