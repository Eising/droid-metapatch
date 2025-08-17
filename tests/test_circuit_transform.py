"""Tests for the transform actions on circuits."""

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
        circuitdict = circuit.model_dump(by_alias=False, exclude_none=True)
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
    transformed = metapatch.transform(circuits, new_input="I2")
    assert transformed[2].input == "I2"

    # This should fail
    circuits2 = [
        metapatch.circuits.Math(input1="I3", input2="I4", difference="_DIFFERENCE"),
        metapatch.circuits.Algoquencer(clock="_CLOCK"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    with pytest.raises(ValueError):
        metapatch.transform(circuits2, new_input="I2")

    transformed = metapatch.transform(circuits2, new_input="I2", ignore=["I1", "I4"])
    assert transformed[0].input1 == "I2"


def test_rewrite_output():
    """Test rewriting inputs."""
    circuits = [
        metapatch.circuits.Math(input1="_SOMETHING"),
        metapatch.circuits.Algoquencer(clock="_CLOCK"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    transformed = metapatch.transform(circuits, new_output="O1")
    assert transformed[2].output == "O1"

    # This should fail
    circuits2 = [
        metapatch.circuits.Math(input1="I3", input2="I4", difference="_DIFFERENCE"),
        metapatch.circuits.Algoquencer(clock="_CLOCK", pitch="O3"),
        metapatch.circuits.Copy(input="I1", output="O2"),
        metapatch.circuits.Button(button="B1.1", led="L1.1"),
    ]
    with pytest.raises(ValueError):
        metapatch.transform(circuits2, new_output="O1")


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


def test_voice_transformation():
    """Test common operations on a voice.."""
    test_circuits = [
        metapatch.circuits.Algoquencer(
            clock="_CLOCK",
            reset="_RESET",
            button1="B1.1",
            button2="B1.2",
            button3="B1.3",
            button4="B1.4",
            button5="B1.5",
            button6="B1.6",
            button7="B1.7",
            button8="B1.8",
            led1="L1.1",
            led2="L1.2",
            led3="L1.3",
            led4="L1.4",
            led5="L1.5",
            led6="L1.6",
            led7="L1.7",
            led8="L1.8",
            gate="_GATE",
            pitch="_PITCH_U",
            activity="_ACTIVITY",
        ),
        metapatch.circuits.Pot(pot="P1.1", notch="0.1", output="_ACTIVITY"),
        metapatch.circuits.Minifonion(
            input="_PITCH_U",
            root="_ROOT",
            degree="_DEGREE",
            select1="1",
            select3="1",
            select5="1",
            select7="1",
            select9="1",
            select11="1",
            select13="1",
            tuningmode="_TUNINGMODE",
            tuningpitch="3V",
            output="O1",
        ),
        metapatch.circuits.Button(
            button="B1.9", led="L1.9", onvalue="0", offvalue="1", output="_MUTED"
        ),
        metapatch.circuits.Copy(input="_GATE * _MUTED", output="G1.1"),
    ]
    voice_1 = metapatch.transform(
        test_circuits,
        ignore=["_ROOT", "_DEGREE", "_CLOCK", "_RESET", "_TUNINGMODE"],
        prepend="VOICE_1",
        new_output="O2",
        gate="G1.2",
        replace=[("P1.1", "P1.2")],
    )
    assert voice_1[2].output == "O2"
    assert voice_1[2].root == "_ROOT"
    assert voice_1[0].pitch == "_VOICE_1_PITCH_U"
    assert voice_1[2].input == "_VOICE_1_PITCH_U"
    assert voice_1[1].pot == "P1.2"
