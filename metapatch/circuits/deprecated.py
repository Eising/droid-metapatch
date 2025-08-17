"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Fourstatebutton(DroidCircuit):
    """ Button switching through 4 states (OBSOLETE)

    Args:
        button (trigger):
          The button.
        reset (trigger):
          A positive trigger here will reset the button to the first state.
        value1 (cv):
          The values that output should get when the four various states are active.
        value2 (cv):
          The values that output should get when the four various states are active.
        value3 (cv):
          The values that output should get when the four various states are active.
        value4 (cv):
          The values that output should get when the four various states are active.
        startvalue (integer):
          By setting this to 0, 1, 2 or 3 you set the initial state of the button when
          the is powered up to state 1, 2, 3 or 4. It also disabled the automatic saving
          of the button's state in the 's internal flash memory.
        output (cv):
          Depending on the current state of the button here the value of input1, input2,
          input3 or input4 will be copied.
        led (fraction):
          The LED in the button
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 40

    button: str | None = Field(
        default=None,
        serialization_alias="button",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "r"},
    )
    value1: str | None = Field(
        default=None,
        serialization_alias="value1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v1"},
    )
    value2: str | None = Field(
        default=None,
        serialization_alias="value2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v2"},
    )
    value3: str | None = Field(
        default=None,
        serialization_alias="value3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v3"},
    )
    value4: str | None = Field(
        default=None,
        serialization_alias="value4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v4"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sv"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o"},
    )
    led: str | None = Field(
        default=None,
        serialization_alias="led",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l"},
    )


class Notchedpot(DroidCircuit):
    """ Helper circuit for pots (OBSOLETE)

    Args:
        pot (fraction):
          Wire your pot here, e.g. P1.1
        notch (cv):
          Optionally set the notch size, if you do not like the default of 0.1. The
          maximum allowed value is 0.5. Greater values will be reduced to that.
        output (fraction):
          Your pot output comes here. It still goes from 0.0 to 1.0.
        bipolar (cv):
          Optional output with a range from -1.0 to 1.0, where the center notch is at
          0.0.
        absbipolar (cv):
          A variation of bipolar that always outputs a positive value, i.e. the pot will
          go 1 ... 0.5 ... 0 ... 0.5 ... 1
        lefthalf (cv):
          This output allows you to split the pot into two hemispheres. Here you get 1.0
          ... 0.0 while the pot is in the left half. In the middle and right of it you
          always get 0.
        righthalf (cv):
          This is the same but for the right half. It outputs 0 while the pot is in the
          left half and 0.0 ... 1.0 from the middle to the fully right position.
        lefthalfinv (cv):
          This outputs 1.0 - lefthalf, i.e. the value range 0.0 ... 1.0 ... 1.0 when the
          pot moves left → mid → right.
        righthalfinv (cv):
          This outputs 1.0 - righthalf, i.e. the value range 1.0 ... 1.0 ... 0.0 when
          the pot moves left → mid → right.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 40

    pot: str | None = Field(
        default=None,
        serialization_alias="pot",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p"},
    )
    notch: str | None = Field(
        default=None,
        serialization_alias="notch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "no"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o"},
    )
    bipolar: str | None = Field(
        default=None,
        serialization_alias="bipolar",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "b"},
    )
    absbipolar: str | None = Field(
        default=None,
        serialization_alias="absbipolar",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ab"},
    )
    lefthalf: str | None = Field(
        default=None,
        serialization_alias="lefthalf",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l"},
    )
    righthalf: str | None = Field(
        default=None,
        serialization_alias="righthalf",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "r"},
    )
    lefthalfinv: str | None = Field(
        default=None,
        serialization_alias="lefthalfinv",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "li"},
    )
    righthalfinv: str | None = Field(
        default=None,
        serialization_alias="righthalfinv",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ri"},
    )


class Switchedpot(DroidCircuit):
    """ Overlay pot with multiple functions (OBSOLETE)

    Args:
        pot (fraction):
          The pot that you want to overlay, e.g. P1.1
        bipolar (gate):
          If this input is set to 1, the usual pot range of 0 ... 1 will be mapped to -1
          ... +1, which converts this to a bipolar potentiometer. This is done by
          multiplying the output with 2.0 and substracting 1.0 afterwards.
        switch1 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch2 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch3 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch4 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch5 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch6 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch7 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        switch8 (gate):
          These inputs select which of the virtual pots should be changed when the
          physical pot is being turned. These should be set to 0 or 1 (or off and on).
        output1 (fraction):
          The output of the up to eight virtual pots.
        output2 (fraction):
          The output of the up to eight virtual pots.
        output3 (fraction):
          The output of the up to eight virtual pots.
        output4 (fraction):
          The output of the up to eight virtual pots.
        output5 (fraction):
          The output of the up to eight virtual pots.
        output6 (fraction):
          The output of the up to eight virtual pots.
        output7 (fraction):
          The output of the up to eight virtual pots.
        output8 (fraction):
          The output of the up to eight virtual pots.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 88

    pot: str | None = Field(
        default=None,
        serialization_alias="pot",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p"},
    )
    bipolar: str | None = Field(
        default=None,
        serialization_alias="bipolar",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b"},
    )
    switch1: str | None = Field(
        default=None,
        serialization_alias="switch1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s1"},
    )
    switch2: str | None = Field(
        default=None,
        serialization_alias="switch2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s2"},
    )
    switch3: str | None = Field(
        default=None,
        serialization_alias="switch3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s3"},
    )
    switch4: str | None = Field(
        default=None,
        serialization_alias="switch4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s4"},
    )
    switch5: str | None = Field(
        default=None,
        serialization_alias="switch5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s5"},
    )
    switch6: str | None = Field(
        default=None,
        serialization_alias="switch6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s6"},
    )
    switch7: str | None = Field(
        default=None,
        serialization_alias="switch7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s7"},
    )
    switch8: str | None = Field(
        default=None,
        serialization_alias="switch8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "s8"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3"},
    )
    output4: str | None = Field(
        default=None,
        serialization_alias="output4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4"},
    )
    output5: str | None = Field(
        default=None,
        serialization_alias="output5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5"},
    )
    output6: str | None = Field(
        default=None,
        serialization_alias="output6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6"},
    )
    output7: str | None = Field(
        default=None,
        serialization_alias="output7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7"},
    )
    output8: str | None = Field(
        default=None,
        serialization_alias="output8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8"},
    )


class Togglebutton(DroidCircuit):
    """ Create on/off buttons (OBSOLETE)

    Args:
        button (trigger):
          The actual push button. Usually you want to wire this to B1.1, B1.2 and so on:
          to one of the push buttons of your controllers. Each time that input goes from
          low to high the state of the push button will toggle.
        reset (trigger):
          A positive trigger edge here will reset the button into the state “not
          pressed” – regardless of its current state
        onvalue (cv):
          Value sent to output when the push button is on. Setting this to a different
          value than the default value saves you attenuating its value later on when you
          use it as a CV.
        offvalue (cv):
          Value sent to output when the push button is off.
        doubleclickmode (gate):
          This input can enable a double click mode when set to 1. In that mode the
          button only toggles it's constant state if you double press it in a short
          time. Otherwise it behaves like a momentary button, that inverts the persisted
          state (which you toggle with the double click).
        startvalue (gate):
          State of the push button when you switch on your system. Setting this to on or
          off will force the button into that state. Using this jack disables the
          persistence of the state! In switched mode this will be used for the other
          button layers as well.
        led (gate):
          When the button's state is on a value of 1.0 will be sent to that output –
          regardless of the values in onvalue and offvalue. Usually you will wire this
          jack to the LED within the button, e.g. to L1.1, L1.2 and so on
        output (cv):
          This jack will output either onvalue or offvalue depending on the state of the
          1 ... 4 button. If you have not wired those inputs then this is the same as
          the led output.
        inverted (cv):
          The same as output1, but sends onvalue when the button is off and offvalue
          when the button is on. Note: there is no inverted version of output2 ...
          output4.
        negated (gate):
          Similar to inverted, but always sends 1 when the button is off and 0 when the
          button is on – independent of the values of onvalue and offvalue.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 48

    button: str | None = Field(
        default=None,
        serialization_alias="button",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "r"},
    )
    onvalue: str | None = Field(
        default=None,
        serialization_alias="onvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ov"},
    )
    offvalue: str | None = Field(
        default=None,
        serialization_alias="offvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "fv"},
    )
    doubleclickmode: str | None = Field(
        default=None,
        serialization_alias="doubleclickmode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dm"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sv"},
    )
    led: str | None = Field(
        default=None,
        serialization_alias="led",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o"},
    )
    inverted: str | None = Field(
        default=None,
        serialization_alias="inverted",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "iv"},
    )
    negated: str | None = Field(
        default=None,
        serialization_alias="negated",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "n"},
    )

