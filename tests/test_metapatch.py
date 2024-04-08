"""Metapatch tests."""

from pathlib import Path
import pytest


@pytest.fixture
def testpatch(helper):
    """Load testpatch."""
    pg = helper("simple_metapatch.py", "TestMetaPatch")
    return pg.patch_generator


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


@pytest.mark.parametrize("name", ["sections", "disjoint_sections", "labels"])
def test_patch(helper, name):
    """Generic test function."""
    helper.test(f"{name}.py", f"{name}.ini")


def test_preset(testpatch):
    """Test preset loading."""
    mypatch = testpatch.load_preset("default")
    assert mypatch.testbool is True


def test_generate(testpatch):
    """Test patch generation."""
    mytest = testpatch.load_preset("default")
    patch = str(mytest)
    assert patch == "[B32]\n[E4]\n\n[copy]\n    input = _FIRST\n    output = _OUTPUT\n"


def test_megadrone(helper):
    """Test megadrone from the example library."""
    megadrone_mod = Path(__file__).parent / ".." / "examples" / "e4megadrone"
    helper.test(
        megadrone_mod,
        "e4megadrone.ini",
        "MegaDrone",
        voices="8",
        midi="True",
        channel="11",
        encoder1="5",
        encoder2="4",
        encoder3="3",
        encoder4="2",
    )


def test_auto_preset(helper):
    """Test auto-generated preset."""
    pg = helper("auto_preset.py")
    synopsis = pg.patch_generator.synopsis
    assert "presets" in synopsis
    assert len(synopsis["presets"]) == 1
    preset = synopsis["presets"][0]
    assert preset["name"] == "default"
    assert preset["title"] == "Default Preset"
    testbool = preset["parameters"].get("testbool")
    testnumber = preset["parameters"].get("testnumber")
    testchoice = preset["parameters"].get("testchoice")
    assert testbool is True
    assert testnumber == 1
    assert testchoice == "first"
