"""DROID circuits. These circuits are auto-generated from circuits.json."""

from dataclasses import dataclass, field
from typing import Optional

from metapatch.circuits.base import DroidCircuit
from metapatch.circuits import circuit_types as ctype


__droid_version__ = "blue-6"


@dataclass
class Fourstatebutton(DroidCircuit):
    """Button switching through 4 states (OBSOLETE).

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

    __ramsize__ = 40
    button: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    reset: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    value1: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    value2: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    value3: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    value4: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    startvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    led: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )



@dataclass
class Notchedpot(DroidCircuit):
    """Helper circuit for pots (OBSOLETE).

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

    __ramsize__ = 40
    pot: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notch: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    bipolar: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    absbipolar: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    lefthalf: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    righthalf: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    lefthalfinv: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    righthalfinv: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Switchedpot(DroidCircuit):
    """Overlay pot with multiple functions (OBSOLETE).

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

    __ramsize__ = 88
    pot: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    bipolar: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    switch8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    output1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )



@dataclass
class Togglebutton(DroidCircuit):
    """Create on/off buttons (OBSOLETE).

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

    __ramsize__ = 48
    button: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    reset: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    onvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    offvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    doubleclickmode: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    startvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    led: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    inverted: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    negated: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )



