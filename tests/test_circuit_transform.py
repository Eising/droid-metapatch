"""Tests for the transform actions on circuits."""

from dataclasses import asdict
import metapatch
import metapatch.circuits
import pytest


@pytest.fixture
def circuits_no_selects():
    """Circuit fixture."""
    circuits = [
        metapatch.circuits.Button(button="B3.1", led="L3.1", output="_TEST_BUTTON"),
        metapatch.circuits.Button(button="B3.2", led="L3.2", output="_TEST_BUTTON2"),
        metapatch.circuits.Copy(input="_TEST", output="_TEST_OUT"),
        metapatch.circuits.Button(
            select="_UNRELATED", button="B3.3", led="L3.3", output="_TEST_BUTTON3"
        ),
    ]
    return circuits


@pytest.fixture
def circuits_with_selects():
    """Circuits where we add a different selectat."""
    circuits = [
        metapatch.circuits.Button(
            button="B3.1",
            led="L3.1",
            select="_VOICE",
            selectat="1",
            output="_TEST_BUTTON",
        ),
        metapatch.circuits.Button(
            button="B3.2",
            led="L3.2",
            select="_VOICE",
            selectat="1",
            output="_TEST_BUTTON2",
        ),
        metapatch.circuits.Button(
            button="B3.3",
            led="L3.3",
            select="_VOICE",
            selectat="1",
            output="_TEST_BUTTON3",
        ),
        metapatch.circuits.Button(
            button="B3.4",
            led="L3.4",
            select="_VOICE",
            selectat="1",
            output="_TEST_BUTTON4",
        ),
        metapatch.circuits.Copy(input="I1", output="O1"),
    ]
    return circuits


def test_add_select(circuits_no_selects):
    """Add selects."""
    circuits = metapatch.transform(circuits_no_selects, select="_MYSELECT")
    assert circuits[0].button == "B3.1"
    assert circuits[0].select == "_MYSELECT"
    assert circuits[1].select == "_MYSELECT"
    assert getattr(circuits[2], "select", None) is None
    assert circuits[3].select == "_UNRELATED"


def test_transform_selectat(circuits_with_selects):
    """Change the selectat."""
    circuits = metapatch.transform(
        circuits_with_selects, select="_VOICE", select_at="2"
    )
    for i in range(0, 4):
        assert circuits[i].select == "_VOICE"
        assert circuits[i].selectat == "2"


def test_prepend(circuits_with_selects):
    """Test prepending a string."""
    circuits = metapatch.transform(circuits_with_selects, prepend="_VOICE_1")
    for circuit in circuits:
        if circuit.output.startswith("_"):
            assert circuit.output.startswith("_VOICE_1")
    assert circuits[-1].output == "O1"


def test_multiple(circuits_with_selects):
    """Test multiple actions."""
    circuits = metapatch.transform(
        circuits_with_selects, append="_VOICE_1", select="_VOICE", select_at="1"
    )
    for circuit in circuits:
        circuitdict = asdict(circuit)
        for value in list(circuitdict.values()):
            if value is None:
                continue
            if value.startswith("_"):
                assert value.endswith("_VOICE_1")
        if "select" in circuitdict and circuitdict["select"] != "_UNRELATED":
            assert circuitdict["selectat"] == "1"


def test_rewrite_input():
    """Test rewriting inputs."""
    circuits = [
        metapatch.circuits.Math(input1="_SOMETHING"),
        metapatch.circuits.Algoquencer(clock="_CLOCK"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    transformed = metapatch.transform(circuits, input="I2")
    assert transformed[2].input == "I2"

    # This should fail
    circuits2 = [
        metapatch.circuits.Math(input1="I3", input2="I4", difference="_DIFFERENCE"),
        metapatch.circuits.Algoquencer(clock="_CLOCK"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    with pytest.raises(ValueError):
        metapatch.transform(circuits2, input="I2")


def test_rewrite_output():
    """Test rewriting inputs."""
    circuits = [
        metapatch.circuits.Math(input1="_SOMETHING"),
        metapatch.circuits.Algoquencer(clock="_CLOCK"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    transformed = metapatch.transform(circuits, output="O1")
    assert transformed[2].output == "O1"

    # This should fail
    circuits2 = [
        metapatch.circuits.Math(input1="I3", input2="I4", difference="_DIFFERENCE"),
        metapatch.circuits.Algoquencer(clock="_CLOCK", pitch="O3"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    with pytest.raises(ValueError):
        metapatch.transform(circuits2, output="O1")


def test_rewrite_gate():
    """Test rewriting inputs."""
    circuits = [
        metapatch.circuits.Math(input1="_SOMETHING"),
        metapatch.circuits.Algoquencer(clock="_CLOCK", trigger="G1.1"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    transformed = metapatch.transform(circuits, gate="G1.2")
    assert transformed[1].trigger == "G1.2"

    # This should fail
    circuits2 = [
        metapatch.circuits.Math(input1="I3", input2="I4", difference="_DIFFERENCE"),
        metapatch.circuits.Algoquencer(clock="_CLOCK", trigger="G1.1"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1", output="G9"),
    ]
    with pytest.raises(ValueError):
        metapatch.transform(circuits2, gate="G1.1")
