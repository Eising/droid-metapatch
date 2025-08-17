"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Button(DroidCircuit):
    """ Does all sorts of useful things with buttons

    Args:
        button (gate):
          The actual push button. Usually you want to wire this to B1.1, B1.2 and so on:
          to one of the push buttons of your controllers. Each time that input goes from
          low to high, the state of the push button will toggle.
        onvalue (cv):
          Value sent to output when the push button is on. You can also use a dynamic
          signal here. This is an alternative name for the input value1.
        offvalue (cv):
          Value sent to output when the push button is off. This is an alternative name
          for the input value2.
        value1 (cv):
          The up to four values to output at output when the button is on the according
          state. value1 is the same as offvalue and value2 is the same as onvalue. The
          default values of these four inputs are 0, 1, 2 and 3, so in many cases you
          don't need to specify them.
        value2 (cv):
          The up to four values to output at output when the button is on the according
          state. value1 is the same as offvalue and value2 is the same as onvalue. The
          default values of these four inputs are 0, 1, 2 and 3, so in many cases you
          don't need to specify them.
        value3 (cv):
          The up to four values to output at output when the button is on the according
          state. value1 is the same as offvalue and value2 is the same as onvalue. The
          default values of these four inputs are 0, 1, 2 and 3, so in many cases you
          don't need to specify them.
        value4 (cv):
          The up to four values to output at output when the button is on the according
          state. value1 is the same as offvalue and value2 is the same as onvalue. The
          default values of these four inputs are 0, 1, 2 and 3, so in many cases you
          don't need to specify them.
        doubleclickmode (gate):
          This input can enable a double click mode when set to 1. In that mode the
          button only toggles it's constant state if you double press it in a short
          time. Otherwise it behaves like a momentary button, that inverts the persisted
          state (which you toggle with the double click). Note: The double clock mode is
          only makes sense if the number of states is 2.
        longpresstime (cv):
          The number of seconds after which a button press is considered as a long
          press.
        states (integer):
          Number of states this button can have. The default value is 2, which creates a
          toggle button which changes between on and off at each press. A value of 1
          creates a momentary button. Note: If you just need a plain momentary button,
          you can directly use B1.1, B1.2 and so on. You don't need an extra circuit.
          But if you want things like overloading (with select) or the longpress output,
          this does make sense. The maximum number of states is 4. When the button has 3
          or 4 states, every press will switch to the next state and then back to the
          first state again.
        startvalue (integer):
          State of the push button when you switch on your system or on a trigger to
          clear. If you have three states, the start value needs to be 0, 1 or 2. With
          four states, it can also be 3.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        led (cv):
          When the button state is on, a value of 1.0 will be sent to that output –
          regardless of the values in onvalue and offvalue. If the number of states is 3
          or 4 the output get's intermediate values so the attached LED will be dimmed
          into different brightness levels. Usually you wire that output to a LED
          register, e.g. to L1.1, L1.2 and so on.
        output (cv):
          This output will output the current button states. This is usually 0 for off
          and 1 for on. If states is 3 or 4, the values 2 or 3 are output for the
          additional states. You can modify all four values with the inputs
          offvalue/value1, onvalue/value2, value3 and value4. Note: if you haven't
          changed any of these inputs and states is unchanged or 1 or 2, the led output
          will output the same values.
        inverted (cv):
          The same as output, but sends onvalue when the button is off and offvalue when
          the button is on. If states is 3 or 4, the order of the four output values
          will be mirrored (probably a feature that is rarely of any use).
        negated (gate):
          Similar to inverted, but always sends 1 when the button is off and 0 when the
          button is on – independent of the values of onvalue and offvalue. When states
          is 3 or 4, this output will be 1 if the button is off and 0 in the other three
          states.
        longpress (gate):
          Goes from 0 to 1, when the button is pressed and hold for at least 1.5
          seconds. If this output is used, the effect of toggling the button's state is
          delayed until the button is released. When it's released after 1.5 secs, no
          toggling happens. This will avoid double actions for long presses.
        shortpress (trigger):
          Emits a trigger, when the button is pressed, regardless of the settings of
          states. If at the same time longpress is used (which is the whole point in
          this output), the trigger is delayed until the button is released and only
          sent, if it was not a long press.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 96

    button: str | None = Field(
        default=None,
        serialization_alias="button",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b"},
    )
    onvalue: str | None = Field(
        default=None,
        serialization_alias="onvalue",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "ov"},
    )
    offvalue: str | None = Field(
        default=None,
        serialization_alias="offvalue",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "fv"},
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
    doubleclickmode: str | None = Field(
        default=None,
        serialization_alias="doubleclickmode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dm"},
    )
    longpresstime: str | None = Field(
        default=None,
        serialization_alias="longpresstime",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lt"},
    )
    states: str | None = Field(
        default=None,
        serialization_alias="states",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "st"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sv"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    led: str | None = Field(
        default=None,
        serialization_alias="led",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "l"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "o"},
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
    longpress: str | None = Field(
        default=None,
        serialization_alias="longpress",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lop"},
    )
    shortpress: str | None = Field(
        default=None,
        serialization_alias="shortpress",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "shp"},
    )


class Buttongroup(DroidCircuit):
    """ Connected buttons

    Args:
        minactive (integer):
          Minimum number of active buttons. If you set this to 2, then it is guaranteed
          that at least 2 buttons are active. If you set this to 0, then it is possible
          to switch off all buttons. The output will be set to 0.0 in that case.
        maxactive (integer):
          Maximum number of active buttons. It is an error to set this to 0, since this
          would make this circuit useless.
        longpresstime (cv):
          The number of seconds after which a button press is considered as a long
          press.
        button1 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button2 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button3 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button4 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button5 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button6 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button7 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button8 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button9 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button10 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button11 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button12 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button13 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button14 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button15 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button16 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button17 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button18 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button19 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button20 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button21 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button22 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button23 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button24 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button25 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button26 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button27 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button28 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button29 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button30 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button31 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        button32 (trigger):
          1 ... 32 button of the group. Any positive trigger seen here will toggle this
          button. And another button might go on or off in order to make sure that the
          number of active buttons is withing the allowed range.
        value1 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value2 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value3 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value4 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value5 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value6 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value7 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value8 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value9 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value10 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value11 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value12 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value13 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value14 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value15 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value16 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value17 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value18 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value19 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value20 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value21 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value22 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value23 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value24 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value25 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value26 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value27 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value28 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value29 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value30 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value31 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        value32 (cv):
          Value that will be sent to the output if the 1 ... 32 button is active. These
          inputs default to 0 for value1, 1 for value2 and so on and 31 for value32.
        startbutton (integer):
          If you set this parameter to the number of a button, that button will be
          selected (and all other deselected) at the start when no state is loaded or at
          a trigger to clear. This allows you to set useful default values for your
          button groups. Note: this only makes sense if maxactive is not 0.  if
          minactive = 0, you also can set startbutton = 0. Then a clear will clear all
          buttons.  If you set startbutton = -1, the maximum number of allowed buttons
          will be set. This is useful in situations where maxactive is greater than 1.
          If maxactive is less than the number of buttons, the selected buttons are
          filled from the start.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        led1 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led2 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led3 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led4 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led5 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led6 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led7 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led8 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led9 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led10 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led11 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led12 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led13 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led14 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led15 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led16 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led17 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led18 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led19 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led20 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led21 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led22 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led23 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led24 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led25 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led26 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led27 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led28 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led29 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led30 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led31 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        led32 (gate):
          This output will be on / 1.0, whenever the 1 ... 32 button is active and off /
          0.0 otherwise. Wire this to the LED in the button. If you have wired select,
          these LED outputs will do nothing (not even send 0) unless this circuit is
          selected.
        buttonoutput1 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput2 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput3 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput4 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput5 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput6 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput7 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput8 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput9 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput10 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput11 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput12 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput13 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput14 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput15 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput16 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput17 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput18 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput19 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput20 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput21 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput22 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput23 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput24 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput25 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput26 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput27 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput28 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput29 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput30 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput31 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        buttonoutput32 (cv):
          These are individual outputs for every button in the group. They output
          button's value when it is active, otherwise 0. If valueX is not defined for
          buttonX, the value 1 is output (not the button's number!).  Note: in contrast
          to the led output, these outputs are not affected by select but always
          functional.  One application of these outputs is to use a buttongroup with
          maxactive =  X and minactive = 0 as a cheap bunch of X toggle buttons in one
          single circuit and still use select.
        output (cv):
          The sum of the values of all active buttons will be sent here. if no button is
          active, 0.0 is being output.
        buttonpress (trigger):
          Emits a trigger if any button is being pressed
        longpress (trigger):
          Emits a trigger, when any button is pressed for at least 1.5 seconds. If this
          jack is used, buttonpress will emit a signal if the button in question is
          released before the 1.5 seconds, not immediately. This way you trigger either
          at buttonpress or at longpress, not at both.
        selectionchanged (trigger):
          Emits a trigger when the selection of the buttons has changed. This is not
          quite the same as buttonpress, since a button press might not lead to a
          change. Also in multi button situations (e.g. maxactive = 4 where you have 7
          buttons) the change is delayed up to 25 ms due to detection of bursts of quasi
          simultanous presses.
        extrapress (trigger):
          Emits a trigger, when one of the buttons was pressed but the selection has not
          changed. This can be used to build clever interfaces like in the Motor Fader
          Performance Sequencer, where a press on the already selected track toggles the
          current page.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 440

    minactive: str | None = Field(
        default=None,
        serialization_alias="minactive",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ma"},
    )
    maxactive: str | None = Field(
        default=None,
        serialization_alias="maxactive",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "xa"},
    )
    longpresstime: str | None = Field(
        default=None,
        serialization_alias="longpresstime",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lt"},
    )
    button1: str | None = Field(
        default=None,
        serialization_alias="button1",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b1"},
    )
    button2: str | None = Field(
        default=None,
        serialization_alias="button2",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b2"},
    )
    button3: str | None = Field(
        default=None,
        serialization_alias="button3",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b3"},
    )
    button4: str | None = Field(
        default=None,
        serialization_alias="button4",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b4"},
    )
    button5: str | None = Field(
        default=None,
        serialization_alias="button5",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b5"},
    )
    button6: str | None = Field(
        default=None,
        serialization_alias="button6",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b6"},
    )
    button7: str | None = Field(
        default=None,
        serialization_alias="button7",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b7"},
    )
    button8: str | None = Field(
        default=None,
        serialization_alias="button8",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b8"},
    )
    button9: str | None = Field(
        default=None,
        serialization_alias="button9",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b9"},
    )
    button10: str | None = Field(
        default=None,
        serialization_alias="button10",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b10"},
    )
    button11: str | None = Field(
        default=None,
        serialization_alias="button11",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b11"},
    )
    button12: str | None = Field(
        default=None,
        serialization_alias="button12",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b12"},
    )
    button13: str | None = Field(
        default=None,
        serialization_alias="button13",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b13"},
    )
    button14: str | None = Field(
        default=None,
        serialization_alias="button14",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b14"},
    )
    button15: str | None = Field(
        default=None,
        serialization_alias="button15",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b15"},
    )
    button16: str | None = Field(
        default=None,
        serialization_alias="button16",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b16"},
    )
    button17: str | None = Field(
        default=None,
        serialization_alias="button17",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b17"},
    )
    button18: str | None = Field(
        default=None,
        serialization_alias="button18",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b18"},
    )
    button19: str | None = Field(
        default=None,
        serialization_alias="button19",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b19"},
    )
    button20: str | None = Field(
        default=None,
        serialization_alias="button20",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b20"},
    )
    button21: str | None = Field(
        default=None,
        serialization_alias="button21",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b21"},
    )
    button22: str | None = Field(
        default=None,
        serialization_alias="button22",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b22"},
    )
    button23: str | None = Field(
        default=None,
        serialization_alias="button23",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b23"},
    )
    button24: str | None = Field(
        default=None,
        serialization_alias="button24",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b24"},
    )
    button25: str | None = Field(
        default=None,
        serialization_alias="button25",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b25"},
    )
    button26: str | None = Field(
        default=None,
        serialization_alias="button26",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b26"},
    )
    button27: str | None = Field(
        default=None,
        serialization_alias="button27",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b27"},
    )
    button28: str | None = Field(
        default=None,
        serialization_alias="button28",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b28"},
    )
    button29: str | None = Field(
        default=None,
        serialization_alias="button29",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b29"},
    )
    button30: str | None = Field(
        default=None,
        serialization_alias="button30",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b30"},
    )
    button31: str | None = Field(
        default=None,
        serialization_alias="button31",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b31"},
    )
    button32: str | None = Field(
        default=None,
        serialization_alias="button32",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b32"},
    )
    value1: str | None = Field(
        default=None,
        serialization_alias="value1",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "v1"},
    )
    value2: str | None = Field(
        default=None,
        serialization_alias="value2",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "v2"},
    )
    value3: str | None = Field(
        default=None,
        serialization_alias="value3",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "v3"},
    )
    value4: str | None = Field(
        default=None,
        serialization_alias="value4",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "v4"},
    )
    value5: str | None = Field(
        default=None,
        serialization_alias="value5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v5"},
    )
    value6: str | None = Field(
        default=None,
        serialization_alias="value6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v6"},
    )
    value7: str | None = Field(
        default=None,
        serialization_alias="value7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v7"},
    )
    value8: str | None = Field(
        default=None,
        serialization_alias="value8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v8"},
    )
    value9: str | None = Field(
        default=None,
        serialization_alias="value9",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v9"},
    )
    value10: str | None = Field(
        default=None,
        serialization_alias="value10",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v10"},
    )
    value11: str | None = Field(
        default=None,
        serialization_alias="value11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v11"},
    )
    value12: str | None = Field(
        default=None,
        serialization_alias="value12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v12"},
    )
    value13: str | None = Field(
        default=None,
        serialization_alias="value13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v13"},
    )
    value14: str | None = Field(
        default=None,
        serialization_alias="value14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v14"},
    )
    value15: str | None = Field(
        default=None,
        serialization_alias="value15",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v15"},
    )
    value16: str | None = Field(
        default=None,
        serialization_alias="value16",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v16"},
    )
    value17: str | None = Field(
        default=None,
        serialization_alias="value17",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v17"},
    )
    value18: str | None = Field(
        default=None,
        serialization_alias="value18",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v18"},
    )
    value19: str | None = Field(
        default=None,
        serialization_alias="value19",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v19"},
    )
    value20: str | None = Field(
        default=None,
        serialization_alias="value20",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v20"},
    )
    value21: str | None = Field(
        default=None,
        serialization_alias="value21",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v21"},
    )
    value22: str | None = Field(
        default=None,
        serialization_alias="value22",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v22"},
    )
    value23: str | None = Field(
        default=None,
        serialization_alias="value23",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v23"},
    )
    value24: str | None = Field(
        default=None,
        serialization_alias="value24",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v24"},
    )
    value25: str | None = Field(
        default=None,
        serialization_alias="value25",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v25"},
    )
    value26: str | None = Field(
        default=None,
        serialization_alias="value26",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v26"},
    )
    value27: str | None = Field(
        default=None,
        serialization_alias="value27",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v27"},
    )
    value28: str | None = Field(
        default=None,
        serialization_alias="value28",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v28"},
    )
    value29: str | None = Field(
        default=None,
        serialization_alias="value29",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v29"},
    )
    value30: str | None = Field(
        default=None,
        serialization_alias="value30",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v30"},
    )
    value31: str | None = Field(
        default=None,
        serialization_alias="value31",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v31"},
    )
    value32: str | None = Field(
        default=None,
        serialization_alias="value32",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v32"},
    )
    startbutton: str | None = Field(
        default=None,
        serialization_alias="startbutton",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sb"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    led1: str | None = Field(
        default=None,
        serialization_alias="led1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "l1"},
    )
    led2: str | None = Field(
        default=None,
        serialization_alias="led2",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "l2"},
    )
    led3: str | None = Field(
        default=None,
        serialization_alias="led3",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "l3"},
    )
    led4: str | None = Field(
        default=None,
        serialization_alias="led4",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "l4"},
    )
    led5: str | None = Field(
        default=None,
        serialization_alias="led5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l5"},
    )
    led6: str | None = Field(
        default=None,
        serialization_alias="led6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l6"},
    )
    led7: str | None = Field(
        default=None,
        serialization_alias="led7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l7"},
    )
    led8: str | None = Field(
        default=None,
        serialization_alias="led8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l8"},
    )
    led9: str | None = Field(
        default=None,
        serialization_alias="led9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l9"},
    )
    led10: str | None = Field(
        default=None,
        serialization_alias="led10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l10"},
    )
    led11: str | None = Field(
        default=None,
        serialization_alias="led11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l11"},
    )
    led12: str | None = Field(
        default=None,
        serialization_alias="led12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l12"},
    )
    led13: str | None = Field(
        default=None,
        serialization_alias="led13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l13"},
    )
    led14: str | None = Field(
        default=None,
        serialization_alias="led14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l14"},
    )
    led15: str | None = Field(
        default=None,
        serialization_alias="led15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l15"},
    )
    led16: str | None = Field(
        default=None,
        serialization_alias="led16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l16"},
    )
    led17: str | None = Field(
        default=None,
        serialization_alias="led17",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l17"},
    )
    led18: str | None = Field(
        default=None,
        serialization_alias="led18",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l18"},
    )
    led19: str | None = Field(
        default=None,
        serialization_alias="led19",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l19"},
    )
    led20: str | None = Field(
        default=None,
        serialization_alias="led20",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l20"},
    )
    led21: str | None = Field(
        default=None,
        serialization_alias="led21",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l21"},
    )
    led22: str | None = Field(
        default=None,
        serialization_alias="led22",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l22"},
    )
    led23: str | None = Field(
        default=None,
        serialization_alias="led23",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l23"},
    )
    led24: str | None = Field(
        default=None,
        serialization_alias="led24",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l24"},
    )
    led25: str | None = Field(
        default=None,
        serialization_alias="led25",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l25"},
    )
    led26: str | None = Field(
        default=None,
        serialization_alias="led26",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l26"},
    )
    led27: str | None = Field(
        default=None,
        serialization_alias="led27",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l27"},
    )
    led28: str | None = Field(
        default=None,
        serialization_alias="led28",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l28"},
    )
    led29: str | None = Field(
        default=None,
        serialization_alias="led29",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l29"},
    )
    led30: str | None = Field(
        default=None,
        serialization_alias="led30",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l30"},
    )
    led31: str | None = Field(
        default=None,
        serialization_alias="led31",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l31"},
    )
    led32: str | None = Field(
        default=None,
        serialization_alias="led32",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l32"},
    )
    buttonoutput1: str | None = Field(
        default=None,
        serialization_alias="buttonoutput1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo1"},
    )
    buttonoutput2: str | None = Field(
        default=None,
        serialization_alias="buttonoutput2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo2"},
    )
    buttonoutput3: str | None = Field(
        default=None,
        serialization_alias="buttonoutput3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo3"},
    )
    buttonoutput4: str | None = Field(
        default=None,
        serialization_alias="buttonoutput4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo4"},
    )
    buttonoutput5: str | None = Field(
        default=None,
        serialization_alias="buttonoutput5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo5"},
    )
    buttonoutput6: str | None = Field(
        default=None,
        serialization_alias="buttonoutput6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo6"},
    )
    buttonoutput7: str | None = Field(
        default=None,
        serialization_alias="buttonoutput7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo7"},
    )
    buttonoutput8: str | None = Field(
        default=None,
        serialization_alias="buttonoutput8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo8"},
    )
    buttonoutput9: str | None = Field(
        default=None,
        serialization_alias="buttonoutput9",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo9"},
    )
    buttonoutput10: str | None = Field(
        default=None,
        serialization_alias="buttonoutput10",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo10"},
    )
    buttonoutput11: str | None = Field(
        default=None,
        serialization_alias="buttonoutput11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo11"},
    )
    buttonoutput12: str | None = Field(
        default=None,
        serialization_alias="buttonoutput12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo12"},
    )
    buttonoutput13: str | None = Field(
        default=None,
        serialization_alias="buttonoutput13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo13"},
    )
    buttonoutput14: str | None = Field(
        default=None,
        serialization_alias="buttonoutput14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo14"},
    )
    buttonoutput15: str | None = Field(
        default=None,
        serialization_alias="buttonoutput15",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo15"},
    )
    buttonoutput16: str | None = Field(
        default=None,
        serialization_alias="buttonoutput16",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo16"},
    )
    buttonoutput17: str | None = Field(
        default=None,
        serialization_alias="buttonoutput17",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo17"},
    )
    buttonoutput18: str | None = Field(
        default=None,
        serialization_alias="buttonoutput18",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo18"},
    )
    buttonoutput19: str | None = Field(
        default=None,
        serialization_alias="buttonoutput19",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo19"},
    )
    buttonoutput20: str | None = Field(
        default=None,
        serialization_alias="buttonoutput20",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo20"},
    )
    buttonoutput21: str | None = Field(
        default=None,
        serialization_alias="buttonoutput21",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo21"},
    )
    buttonoutput22: str | None = Field(
        default=None,
        serialization_alias="buttonoutput22",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo22"},
    )
    buttonoutput23: str | None = Field(
        default=None,
        serialization_alias="buttonoutput23",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo23"},
    )
    buttonoutput24: str | None = Field(
        default=None,
        serialization_alias="buttonoutput24",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo24"},
    )
    buttonoutput25: str | None = Field(
        default=None,
        serialization_alias="buttonoutput25",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo25"},
    )
    buttonoutput26: str | None = Field(
        default=None,
        serialization_alias="buttonoutput26",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo26"},
    )
    buttonoutput27: str | None = Field(
        default=None,
        serialization_alias="buttonoutput27",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo27"},
    )
    buttonoutput28: str | None = Field(
        default=None,
        serialization_alias="buttonoutput28",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo28"},
    )
    buttonoutput29: str | None = Field(
        default=None,
        serialization_alias="buttonoutput29",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo29"},
    )
    buttonoutput30: str | None = Field(
        default=None,
        serialization_alias="buttonoutput30",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo30"},
    )
    buttonoutput31: str | None = Field(
        default=None,
        serialization_alias="buttonoutput31",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo31"},
    )
    buttonoutput32: str | None = Field(
        default=None,
        serialization_alias="buttonoutput32",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bo32"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "o"},
    )
    buttonpress: str | None = Field(
        default=None,
        serialization_alias="buttonpress",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "bp"},
    )
    longpress: str | None = Field(
        default=None,
        serialization_alias="longpress",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lop"},
    )
    selectionchanged: str | None = Field(
        default=None,
        serialization_alias="selectionchanged",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sc"},
    )
    extrapress: str | None = Field(
        default=None,
        serialization_alias="extrapress",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ep"},
    )


class Encoderbank(DroidCircuit):
    """ Create bank of up to 8 virtual input knobs from E4 encoders

    Args:
        firstencoder (integer):
          The first encoder to use. You can either use it's register name, like E8.2 for
          encoder 2 on controller 8. As an alternative you can use a number like 6. That
          would specify the 6 encoder of your setup: the encoder number 2 on your second
          E4.  For each of the output jacks you use, one encoder is used, following the
          order of your controllers.  This value is read just once when the starts.
          Making this parameter dynamic does not work.
        led1 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led2 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led3 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led4 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led5 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led6 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led7 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        led8 (fraction):
          You can use the rings of LEDs around the encoders as virtual LEDs using this
          parameter. This is similar to using the according L registers of the E4, but
          honors the select input.
        startvalue (cv):
          This sets the value the encoder gets when you start this circuit for the first
          time or when you send trigger to clear.  Note: the range of this value refers
          to the situation before outputscale and outputoffset is applied. So if mode is
          unused or at 0, a startvalue of 0.5 sets the encoder's virtual value exactly
          to the center – regardless of any scaling or offsetting that happens
          afterwards.
        notch (cv):
          This parameter helps you to dial in exactly the center of the selected range,
          which is 0.5 in normal mode and 0.0 in bipolar mode.  The value of notch
          specifies the portion of one complete 360 cycle of the pot during which the
          center position should be assumed. 0.1 is probably a good value.  Notch does
          not work if mode selects positive or negative infinity.
        outputscale (cv):
          The output is multiplied by this value. This is just for convenience and may
          save a copy circuit in some situations.
        outputoffset (cv):
          After scaling the virtual value with outputscale, this value is being added
          before sending the result to the output.
        mode (integer):
          Selects the possible range of the virtual value.   0Off: the encoder is unsed,
          its LEDs are off 1Normal mode: fixed range between 0.0 and 1.0 2Bipolar mode:
          fixed range between -1.0 and 1.0 3Positive infinity: open range between 0.0
          and ∞ 4Negative infinity: open range between -∞ and 0.0 5Bipolar infinity:
          open range between -∞ and ∞ 6Circular infinity: range is 0.0 … 1.0, but
          repeats over in both directions   This setting is ignored if discrete is in
          use.  Note: The mode 0 is for situations where encoders are overlayed with
          select and an encoder is unused. Setting mode = 0 can be used to disable this
          encoder and blank its LEDs.
        smooth (cv):
          Unlike a potentiometer, an encoder does not output continous values but steps.
          If you directly wire the output of an encoder to a CV input of an audio
          module, the steps might become audible.  Therefore the final values of the
          encoder are smoothed out by a simulation of a low pass filter. That's
          essentially the same as in the slew circuit. The smoothing is enabled per
          default but you can change it with this parameter.  A value of 0.0 turns off
          smoothing and you get access to the tiny steps of the encoder. 1.0 selects a
          maximum smoothing, which has also the effect that fast turns of the encoder
          are slowed down a bit. The default value of 0.5 does just a mild slew
          limiting.  If you use discrete, the smoothing is not applied.
        discrete (integer):
          Set this to an integer number of 2 or higher to enable discrete mode. In this
          mode the encoder works like a rotary switch for selecting one of the numbers
          0, 1, 2 and so on. The number you set for discrete selects the number of
          positions in this “switch”. For example discrete = 4 produces the values 0, 1,
          2 or 3.  In this mode the inputs notch, mode and smooth are ignored.
        snapto (cv):
          Use this parameter to define a position where the encoder value automatically
          returns to if it is not turned. This behaves a bit like a pitch bend wheel.
          You can get crazy CV modulations if you use a dynamic CV for snapto, such as
          the output of an LFO. The encoder's value will try to follow the LFO but you
          can still turn the encoder and work “against” the LFO.  This mechanism also
          works if the encoder is not selected.
        snapforce (cv):
          Specifies the speed or “force” with that the encoder moves back to the snapto
          position if that is used. A force of 0.0 deactivates snapto.
        sensivity (cv):
          The sensivity determines how far you need to turn the knob to get which amout
          of value change. Per default one turn of 360 degrees changes to the value from
          0.0 to 1.0.  A sensitivity of 2, doubles the speed of change, 0.5 slows it
          down to the half.  If you use mode to enable infinity, there is no total
          range. In this case one turn changes the value by sensivity.  If you use
          discrete, one turn of the knob changes the virtual switch by eight positions,
          if sensitivity is at 1.0, and accordingly faster or slower if you change that.
        autozoom (fraction):
          The “auto zoom” feature allows you to fine adjust values when turning the knob
          slowly and coarse adjust when you turn it fast. If autozoom is at the maximum
          value of 1.0, turning the knob just slowly changes the value by super tiny
          amounts, while turning it fast operates way faster than usual. Use any value
          between 0.0 and 1.0 for autozoom to select the level of this slowing down for
          slow movements.  autozoom has no effect if discrete is used.
        color (cv):
          Color of the pointer in the LED ring. Here are some example color values:
          0.2cyan 0.4green 0.6yellow 0.73orange 0.8red 1.0magenta 1.1violet 1.2blue
        negativecolor (cv):
          If you use this parameter, it defines the color of the LEDs in case the
          current logical value is negative.
        ledfill (integer):
          Selects whether the LED ring displays the current value with just a single
          colored dot (ledfill = 0) or by additionally illuminating all LEDs between 0
          and the current value in half brightness (ledfill = 1).
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output1 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output2 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output3 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output4 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output5 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output6 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output7 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        output8 (cv):
          Output the current value if the virtual encoder value (don't use this if you
          are using sharewithnext).
        button1 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button2 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button3 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button4 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button5 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button6 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button7 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        button8 (gate):
          This outputs provides you with the current states of the push buttons in the
          encoders, but only if the circuit is selected. While you could do this with an
          extra button circuits, using this output is more convenient in some
          situations.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 736

    firstencoder: str | None = Field(
        default=None,
        serialization_alias="firstencoder",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "e"},
    )
    led1: str | None = Field(
        default=None,
        serialization_alias="led1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l1"},
    )
    led2: str | None = Field(
        default=None,
        serialization_alias="led2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l2"},
    )
    led3: str | None = Field(
        default=None,
        serialization_alias="led3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l3"},
    )
    led4: str | None = Field(
        default=None,
        serialization_alias="led4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l4"},
    )
    led5: str | None = Field(
        default=None,
        serialization_alias="led5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l5"},
    )
    led6: str | None = Field(
        default=None,
        serialization_alias="led6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l6"},
    )
    led7: str | None = Field(
        default=None,
        serialization_alias="led7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l7"},
    )
    led8: str | None = Field(
        default=None,
        serialization_alias="led8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l8"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    notch: str | None = Field(
        default=None,
        serialization_alias="notch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "no"},
    )
    outputscale: str | None = Field(
        default=None,
        serialization_alias="outputscale",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "os"},
    )
    outputoffset: str | None = Field(
        default=None,
        serialization_alias="outputoffset",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "oo"},
    )
    mode: str | None = Field(
        default=None,
        serialization_alias="mode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "m"},
    )
    smooth: str | None = Field(
        default=None,
        serialization_alias="smooth",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sm"},
    )
    discrete: str | None = Field(
        default=None,
        serialization_alias="discrete",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "d"},
    )
    snapto: str | None = Field(
        default=None,
        serialization_alias="snapto",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sn"},
    )
    snapforce: str | None = Field(
        default=None,
        serialization_alias="snapforce",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sf"},
    )
    sensivity: str | None = Field(
        default=None,
        serialization_alias="sensivity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "se"},
    )
    autozoom: str | None = Field(
        default=None,
        serialization_alias="autozoom",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "a"},
    )
    color: str | None = Field(
        default=None,
        serialization_alias="color",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "co"},
    )
    negativecolor: str | None = Field(
        default=None,
        serialization_alias="negativecolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "nc"},
    )
    ledfill: str | None = Field(
        default=None,
        serialization_alias="ledfill",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "lf"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o3"},
    )
    output4: str | None = Field(
        default=None,
        serialization_alias="output4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o4"},
    )
    output5: str | None = Field(
        default=None,
        serialization_alias="output5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o5"},
    )
    output6: str | None = Field(
        default=None,
        serialization_alias="output6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o6"},
    )
    output7: str | None = Field(
        default=None,
        serialization_alias="output7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o7"},
    )
    output8: str | None = Field(
        default=None,
        serialization_alias="output8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o8"},
    )
    button1: str | None = Field(
        default=None,
        serialization_alias="button1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b1"},
    )
    button2: str | None = Field(
        default=None,
        serialization_alias="button2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b2"},
    )
    button3: str | None = Field(
        default=None,
        serialization_alias="button3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b3"},
    )
    button4: str | None = Field(
        default=None,
        serialization_alias="button4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b4"},
    )
    button5: str | None = Field(
        default=None,
        serialization_alias="button5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b5"},
    )
    button6: str | None = Field(
        default=None,
        serialization_alias="button6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b6"},
    )
    button7: str | None = Field(
        default=None,
        serialization_alias="button7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b7"},
    )
    button8: str | None = Field(
        default=None,
        serialization_alias="button8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b8"},
    )


class Encoder(DroidCircuit):
    """ Provide access to a knob on the E4 controller

    Args:
        encoder (integer):
          The encoder to use. You can either use it's register name, like E8.2 for
          encoder 2 on controller 8. As an alternative you can use a number like 6. That
          would specify the 6 encoder of your setup: the encoder number 2 on your second
          E4.  This value is read just once when the starts. Making this parameter
          dynamic does not work.
        override (cv):
          Use this parameter to convert the encoder into a mere display. The knob is
          completely ignored and the value from the input is used as the value that is
          displayed in the LED ring.  The parameter discrete still works, so you can use
          the LED ring for displaying a discrete number such as the current step in a
          sequence.  Also mode is honored. Values that do not fit into the selected
          range or number of discrete values will be rounded to the nearest allowed
          value.  override honors select, so if you use select, it does nothing to the
          LEDs while the encoder circuit is not selected.
        sharewithnext (gate):
          If set this to 1, the output output will not be used but the circuit shares
          it's output with the next encoder circuit and operates on the same virtual
          value as that. Use this if you want to control the same value with two
          different encoder circuits (which might be available in different contexts of
          your user interface).  If you do this, make sure that both encoder circuits
          have the same settings of mode and discrete.
        movementticks (integer):
          Specifies the number of encoder ticks you need to turn to get one trigger at
          movedup or moveddown. One complete rotation of the encoder creates 96 such
          ticks.
        led (fraction):
          You can use the ring of LEDs around the encoder as one virtual LED using this
          parameter. This is similar to using the according L register of the E4, but
          honors the select input.  If you set led to 1, all LEDs will get brighter or
          white, if they would be black otherwise.
        startvalue (cv):
          This sets the value the encoder gets when you start this circuit for the first
          time or when you send trigger to clear.  Note: the range of this value refers
          to the situation before outputscale and outputoffset is applied. So if mode is
          unused or at 0, a startvalue of 0.5 sets the encoder's virtual value exactly
          to the center – regardless of any scaling or offsetting that happens
          afterwards.
        notch (cv):
          This parameter helps you to dial in exactly the center of the selected range,
          which is 0.5 in normal mode and 0.0 in bipolar mode.  The value of notch
          specifies the portion of one complete 360 cycle of the pot during which the
          center position should be assumed. 0.1 is probably a good value.  Notch does
          not work if mode selects positive or negative infinity.
        outputscale (cv):
          The output is multiplied by this value. This is just for convenience and may
          save a copy circuit in some situations.
        outputoffset (cv):
          After scaling the virtual value with outputscale, this value is being added
          before sending the result to the output.
        mode (integer):
          Selects the possible range of the virtual value.   0Off: the encoder is unsed,
          its LEDs are off 1Normal mode: fixed range between 0.0 and 1.0 2Bipolar mode:
          fixed range between -1.0 and 1.0 3Positive infinity: open range between 0.0
          and ∞ 4Negative infinity: open range between -∞ and 0.0 5Bipolar infinity:
          open range between -∞ and ∞ 6Circular infinity: range is 0.0 … 1.0, but
          repeats over in both directions   This setting is ignored if discrete is in
          use.  Note: The mode 0 is for situations where encoders are overlayed with
          select and an encoder is unused. Setting mode = 0 can be used to disable this
          encoder and blank its LEDs.
        smooth (cv):
          Unlike a potentiometer, an encoder does not output continous values but steps.
          If you directly wire the output of an encoder to a CV input of an audio
          module, the steps might become audible.  Therefore the final values of the
          encoder are smoothed out by a simulation of a low pass filter. That's
          essentially the same as in the slew circuit. The smoothing is enabled per
          default but you can change it with this parameter.  A value of 0.0 turns off
          smoothing and you get access to the tiny steps of the encoder. 1.0 selects a
          maximum smoothing, which has also the effect that fast turns of the encoder
          are slowed down a bit. The default value of 0.5 does just a mild slew
          limiting.  If you use discrete, the smoothing is not applied.
        discrete (integer):
          Set this to an integer number of 2 or higher to enable discrete mode. In this
          mode the encoder works like a rotary switch for selecting one of the numbers
          0, 1, 2 and so on. The number you set for discrete selects the number of
          positions in this “switch”. For example discrete = 4 produces the values 0, 1,
          2 or 3.  In this mode the inputs notch, mode and smooth are ignored.
        snapto (cv):
          Use this parameter to define a position where the encoder value automatically
          returns to if it is not turned. This behaves a bit like a pitch bend wheel.
          You can get crazy CV modulations if you use a dynamic CV for snapto, such as
          the output of an LFO. The encoder's value will try to follow the LFO but you
          can still turn the encoder and work “against” the LFO.  This mechanism also
          works if the encoder is not selected.
        snapforce (cv):
          Specifies the speed or “force” with that the encoder moves back to the snapto
          position if that is used. A force of 0.0 deactivates snapto.
        sensivity (cv):
          The sensivity determines how far you need to turn the knob to get which amout
          of value change. Per default one turn of 360 degrees changes to the value from
          0.0 to 1.0.  A sensitivity of 2, doubles the speed of change, 0.5 slows it
          down to the half.  If you use mode to enable infinity, there is no total
          range. In this case one turn changes the value by sensivity.  If you use
          discrete, one turn of the knob changes the virtual switch by eight positions,
          if sensitivity is at 1.0, and accordingly faster or slower if you change that.
        autozoom (fraction):
          The “auto zoom” feature allows you to fine adjust values when turning the knob
          slowly and coarse adjust when you turn it fast. If autozoom is at the maximum
          value of 1.0, turning the knob just slowly changes the value by super tiny
          amounts, while turning it fast operates way faster than usual. Use any value
          between 0.0 and 1.0 for autozoom to select the level of this slowing down for
          slow movements.  autozoom has no effect if discrete is used.
        color (cv):
          Color of the pointer in the LED ring. Here are some example color values:
          0.2cyan 0.4green 0.6yellow 0.73orange 0.8red 1.0magenta 1.1violet 1.2blue
        negativecolor (cv):
          If you use this parameter, it defines the color of the LEDs in case the
          current logical value is negative.
        ledfill (integer):
          Selects whether the LED ring displays the current value with just a single
          colored dot (ledfill = 0) or by additionally illuminating all LEDs between 0
          and the current value in half brightness (ledfill = 1).
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output (cv):
          Outputs the current virtual value of this circuit. Don't use this if you are
          using sharewithnext.
        button (gate):
          This output provides you with the current state of the push button in the
          encoder, but only if the circuit is selected. While you could do this with an
          extra button circuit, using this output is more convenient in some situations.
          While the circuit is not selected, the output is set to 0.
        moveddown (trigger):
          Outputs a trigger whenever you have turned the encoder left (counter clock
          wise) by a certain amount (which can be altered by movementticks. Beware: If
          you turn too fast, triggers might overlap and merge together.
        movedup (trigger):
          Outputs a trigger whenever you have turned the encoder right ( clock wise) by
          a certain amount (which can be altered by movementticks). Beware: If you turn
          too fast, triggers might overlap and merge together.
        valuechanged (trigger):
          Outputs a trigger whenever the virtual value has changed.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 184

    encoder: str | None = Field(
        default=None,
        serialization_alias="encoder",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "e"},
    )
    override: str | None = Field(
        default=None,
        serialization_alias="override",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "or"},
    )
    sharewithnext: str | None = Field(
        default=None,
        serialization_alias="sharewithnext",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sw"},
    )
    movementticks: str | None = Field(
        default=None,
        serialization_alias="movementticks",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "mv"},
    )
    led: str | None = Field(
        default=None,
        serialization_alias="led",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "l"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    notch: str | None = Field(
        default=None,
        serialization_alias="notch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "no"},
    )
    outputscale: str | None = Field(
        default=None,
        serialization_alias="outputscale",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "os"},
    )
    outputoffset: str | None = Field(
        default=None,
        serialization_alias="outputoffset",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "oo"},
    )
    mode: str | None = Field(
        default=None,
        serialization_alias="mode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "m"},
    )
    smooth: str | None = Field(
        default=None,
        serialization_alias="smooth",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sm"},
    )
    discrete: str | None = Field(
        default=None,
        serialization_alias="discrete",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "d"},
    )
    snapto: str | None = Field(
        default=None,
        serialization_alias="snapto",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sn"},
    )
    snapforce: str | None = Field(
        default=None,
        serialization_alias="snapforce",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sf"},
    )
    sensivity: str | None = Field(
        default=None,
        serialization_alias="sensivity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "se"},
    )
    autozoom: str | None = Field(
        default=None,
        serialization_alias="autozoom",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "a"},
    )
    color: str | None = Field(
        default=None,
        serialization_alias="color",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "co"},
    )
    negativecolor: str | None = Field(
        default=None,
        serialization_alias="negativecolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "nc"},
    )
    ledfill: str | None = Field(
        default=None,
        serialization_alias="ledfill",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "lf"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )
    button: str | None = Field(
        default=None,
        serialization_alias="button",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b"},
    )
    moveddown: str | None = Field(
        default=None,
        serialization_alias="moveddown",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "md"},
    )
    movedup: str | None = Field(
        default=None,
        serialization_alias="movedup",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "mu"},
    )
    valuechanged: str | None = Field(
        default=None,
        serialization_alias="valuechanged",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "vc"},
    )


class Faderbank(DroidCircuit):
    """ Create multiple virtual faders in M4 controller

    Args:
        firstfader (integer):
          First M4 fader of the virtual fader bank (starting with 1).
        notches (integer):
          Number of artifical notches. 0 disables the notches. 1 creates a pitch bend
          wheel. 2 creates a binary switch with the output values 0 and 1. Higher number
          create that number of notches. E.g. 8 creates eight notches and output will
          output one of the value 0, 1, ... 8.  The maximum number of notches is 201.
          But if you select more than 25 notches, the force feedback is turned off as
          the notches would get too small to work.
        startvalue (cv):
          This sets the value the faders should get when the circuit starts for the
          first time or when you send a trigger to clear.
        ledcolor (cv):
          When you use this input, it will set the color of the LED below the faders,
          when the circuit is selected. If the LED is off, this setting has now impact.
        ledvalue1 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue2 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue3 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue4 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue5 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue6 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue7 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue8 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue9 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue10 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue11 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue12 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue13 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue14 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue15 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        ledvalue16 (cv):
          When you use this input, it will override the brightness of the LEDs below the
          faders, but just when this circuit is selected.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output1 (cv):
          The current values of the virtual motor faders are output here.
        output2 (cv):
          The current values of the virtual motor faders are output here.
        output3 (cv):
          The current values of the virtual motor faders are output here.
        output4 (cv):
          The current values of the virtual motor faders are output here.
        output5 (cv):
          The current values of the virtual motor faders are output here.
        output6 (cv):
          The current values of the virtual motor faders are output here.
        output7 (cv):
          The current values of the virtual motor faders are output here.
        output8 (cv):
          The current values of the virtual motor faders are output here.
        output9 (cv):
          The current values of the virtual motor faders are output here.
        output10 (cv):
          The current values of the virtual motor faders are output here.
        output11 (cv):
          The current values of the virtual motor faders are output here.
        output12 (cv):
          The current values of the virtual motor faders are output here.
        output13 (cv):
          The current values of the virtual motor faders are output here.
        output14 (cv):
          The current values of the virtual motor faders are output here.
        output15 (cv):
          The current values of the virtual motor faders are output here.
        output16 (cv):
          The current values of the virtual motor faders are output here.
        button1 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button2 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button3 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button4 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button5 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button6 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button7 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button8 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button9 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button10 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button11 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button12 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button13 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button14 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button15 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        button16 (gate):
          Outputs the current value of the touch buttons of the faders to these output,
          when this circuit is selected. When the circuit is not selected, 0 is output.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 616

    firstfader: str | None = Field(
        default=None,
        serialization_alias="firstfader",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "f"},
    )
    notches: str | None = Field(
        default=None,
        serialization_alias="notches",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    ledcolor: str | None = Field(
        default=None,
        serialization_alias="ledcolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc"},
    )
    ledvalue1: str | None = Field(
        default=None,
        serialization_alias="ledvalue1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv1"},
    )
    ledvalue2: str | None = Field(
        default=None,
        serialization_alias="ledvalue2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv2"},
    )
    ledvalue3: str | None = Field(
        default=None,
        serialization_alias="ledvalue3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv3"},
    )
    ledvalue4: str | None = Field(
        default=None,
        serialization_alias="ledvalue4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv4"},
    )
    ledvalue5: str | None = Field(
        default=None,
        serialization_alias="ledvalue5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv5"},
    )
    ledvalue6: str | None = Field(
        default=None,
        serialization_alias="ledvalue6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv6"},
    )
    ledvalue7: str | None = Field(
        default=None,
        serialization_alias="ledvalue7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv7"},
    )
    ledvalue8: str | None = Field(
        default=None,
        serialization_alias="ledvalue8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv8"},
    )
    ledvalue9: str | None = Field(
        default=None,
        serialization_alias="ledvalue9",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv9"},
    )
    ledvalue10: str | None = Field(
        default=None,
        serialization_alias="ledvalue10",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv10"},
    )
    ledvalue11: str | None = Field(
        default=None,
        serialization_alias="ledvalue11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv11"},
    )
    ledvalue12: str | None = Field(
        default=None,
        serialization_alias="ledvalue12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv12"},
    )
    ledvalue13: str | None = Field(
        default=None,
        serialization_alias="ledvalue13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv13"},
    )
    ledvalue14: str | None = Field(
        default=None,
        serialization_alias="ledvalue14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv14"},
    )
    ledvalue15: str | None = Field(
        default=None,
        serialization_alias="ledvalue15",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv15"},
    )
    ledvalue16: str | None = Field(
        default=None,
        serialization_alias="ledvalue16",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv16"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o3"},
    )
    output4: str | None = Field(
        default=None,
        serialization_alias="output4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o4"},
    )
    output5: str | None = Field(
        default=None,
        serialization_alias="output5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o5"},
    )
    output6: str | None = Field(
        default=None,
        serialization_alias="output6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o6"},
    )
    output7: str | None = Field(
        default=None,
        serialization_alias="output7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o7"},
    )
    output8: str | None = Field(
        default=None,
        serialization_alias="output8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o8"},
    )
    output9: str | None = Field(
        default=None,
        serialization_alias="output9",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o9"},
    )
    output10: str | None = Field(
        default=None,
        serialization_alias="output10",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o10"},
    )
    output11: str | None = Field(
        default=None,
        serialization_alias="output11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o11"},
    )
    output12: str | None = Field(
        default=None,
        serialization_alias="output12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o12"},
    )
    output13: str | None = Field(
        default=None,
        serialization_alias="output13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o13"},
    )
    output14: str | None = Field(
        default=None,
        serialization_alias="output14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o14"},
    )
    output15: str | None = Field(
        default=None,
        serialization_alias="output15",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o15"},
    )
    output16: str | None = Field(
        default=None,
        serialization_alias="output16",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o16"},
    )
    button1: str | None = Field(
        default=None,
        serialization_alias="button1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b1"},
    )
    button2: str | None = Field(
        default=None,
        serialization_alias="button2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b2"},
    )
    button3: str | None = Field(
        default=None,
        serialization_alias="button3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b3"},
    )
    button4: str | None = Field(
        default=None,
        serialization_alias="button4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b4"},
    )
    button5: str | None = Field(
        default=None,
        serialization_alias="button5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b5"},
    )
    button6: str | None = Field(
        default=None,
        serialization_alias="button6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b6"},
    )
    button7: str | None = Field(
        default=None,
        serialization_alias="button7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b7"},
    )
    button8: str | None = Field(
        default=None,
        serialization_alias="button8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b8"},
    )
    button9: str | None = Field(
        default=None,
        serialization_alias="button9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b9"},
    )
    button10: str | None = Field(
        default=None,
        serialization_alias="button10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b10"},
    )
    button11: str | None = Field(
        default=None,
        serialization_alias="button11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b11"},
    )
    button12: str | None = Field(
        default=None,
        serialization_alias="button12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b12"},
    )
    button13: str | None = Field(
        default=None,
        serialization_alias="button13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b13"},
    )
    button14: str | None = Field(
        default=None,
        serialization_alias="button14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b14"},
    )
    button15: str | None = Field(
        default=None,
        serialization_alias="button15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b15"},
    )
    button16: str | None = Field(
        default=None,
        serialization_alias="button16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b16"},
    )


class Fadermatrix(DroidCircuit):
    """ Matrix of up to 4x4 virtual motor faders

    Args:
        firstfader (integer):
          First M4 fader of the virtual fader matrix (starting with 1).
        rowcolumn (integer):
          Currently selected row or column as follows:   0Control output11, output12,
          output13 and output14 1Control output21, output22, output23 and output24
          2Control output31, output32, output33 and output34 3Control output41,
          output42, output43 and output44 4Control output11, output21, output31 and
          output41 5Control output12, output22, output32 and output42 6Control output13,
          output23, output33 and output43 7Control output14, output24, output34 and
          output44  2mm
        notches1 (integer):
          Number of artifical notches in the respective column. For example notches2
          controls the notches of output12, output22, output32 and output42.   0disables
          the notches 1creates a pitch bend wheel 2creates a binary switch 3creates a
          switch with four positions 8creates eight notches 25creates 25 notches
          Enabling notches also changes the output value. When you have two or more
          notches, the output values become discrete. For example with four notches the
          output will be 0, 1, 2 or 3.  Note: The maximum number of notches is 201. But
          if you select more than 25 notches, the force feedback is turned off as the
          notches would get too small to work.
        notches2 (integer):
          Number of artifical notches in the respective column. For example notches2
          controls the notches of output12, output22, output32 and output42.   0disables
          the notches 1creates a pitch bend wheel 2creates a binary switch 3creates a
          switch with four positions 8creates eight notches 25creates 25 notches
          Enabling notches also changes the output value. When you have two or more
          notches, the output values become discrete. For example with four notches the
          output will be 0, 1, 2 or 3.  Note: The maximum number of notches is 201. But
          if you select more than 25 notches, the force feedback is turned off as the
          notches would get too small to work.
        notches3 (integer):
          Number of artifical notches in the respective column. For example notches2
          controls the notches of output12, output22, output32 and output42.   0disables
          the notches 1creates a pitch bend wheel 2creates a binary switch 3creates a
          switch with four positions 8creates eight notches 25creates 25 notches
          Enabling notches also changes the output value. When you have two or more
          notches, the output values become discrete. For example with four notches the
          output will be 0, 1, 2 or 3.  Note: The maximum number of notches is 201. But
          if you select more than 25 notches, the force feedback is turned off as the
          notches would get too small to work.
        notches4 (integer):
          Number of artifical notches in the respective column. For example notches2
          controls the notches of output12, output22, output32 and output42.   0disables
          the notches 1creates a pitch bend wheel 2creates a binary switch 3creates a
          switch with four positions 8creates eight notches 25creates 25 notches
          Enabling notches also changes the output value. When you have two or more
          notches, the output values become discrete. For example with four notches the
          output will be 0, 1, 2 or 3.  Note: The maximum number of notches is 201. But
          if you select more than 25 notches, the force feedback is turned off as the
          notches would get too small to work.
        startvalue1 (cv):
          These inputs allow to set a defined start value for each column. When the
          starts first and there is either no saved state or state saving is disabled
          via dontsave = 1, these start values are used. Also a trigger to clear loads
          the start avlues. There is one start value for each column. All rows share the
          same start value for a column.
        startvalue2 (cv):
          These inputs allow to set a defined start value for each column. When the
          starts first and there is either no saved state or state saving is disabled
          via dontsave = 1, these start values are used. Also a trigger to clear loads
          the start avlues. There is one start value for each column. All rows share the
          same start value for a column.
        startvalue3 (cv):
          These inputs allow to set a defined start value for each column. When the
          starts first and there is either no saved state or state saving is disabled
          via dontsave = 1, these start values are used. Also a trigger to clear loads
          the start avlues. There is one start value for each column. All rows share the
          same start value for a column.
        startvalue4 (cv):
          These inputs allow to set a defined start value for each column. When the
          starts first and there is either no saved state or state saving is disabled
          via dontsave = 1, these start values are used. Also a trigger to clear loads
          the start avlues. There is one start value for each column. All rows share the
          same start value for a column.
        ledvalue11 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs
          will only affect the LED if the according output is selected.
        ledvalue12 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs
          will only affect the LED if the according output is selected.
        ledvalue13 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs
          will only affect the LED if the according output is selected.
        ledvalue14 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs
          will only affect the LED if the according output is selected.
        ledvalue21 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue22 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue23 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue24 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue31 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue32 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue33 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue34 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue41 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue42 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue43 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs
          will only affect the LED if the according output is selected.
        ledvalue44 (cv):
          With these inputs you can address the LEDs below the virtual faders of
          output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs
          will only affect the LED if the according output is selected.
        ledcolor1 (cv):
          Sets the color of the LEDs below the faders if ledvalueXY is used. There are
          just four inputs since every column of outputs has the same LED color (in
          order to identify them). The color works as with the R registers for the LEDs
          on the master module.
        ledcolor2 (cv):
          Sets the color of the LEDs below the faders if ledvalueXY is used. There are
          just four inputs since every column of outputs has the same LED color (in
          order to identify them). The color works as with the R registers for the LEDs
          on the master module.
        ledcolor3 (cv):
          Sets the color of the LEDs below the faders if ledvalueXY is used. There are
          just four inputs since every column of outputs has the same LED color (in
          order to identify them). The color works as with the R registers for the LEDs
          on the master module.
        ledcolor4 (cv):
          Sets the color of the LEDs below the faders if ledvalueXY is used. There are
          just four inputs since every column of outputs has the same LED color (in
          order to identify them). The color works as with the R registers for the LEDs
          on the master module.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output11 (cv):
          Outputs for the CV values of the first row of parmeter.
        output12 (cv):
          Outputs for the CV values of the first row of parmeter.
        output13 (cv):
          Outputs for the CV values of the first row of parmeter.
        output14 (cv):
          Outputs for the CV values of the first row of parmeter.
        output21 (cv):
          Outputs for the CV values of the second row of parmeter.
        output22 (cv):
          Outputs for the CV values of the second row of parmeter.
        output23 (cv):
          Outputs for the CV values of the second row of parmeter.
        output24 (cv):
          Outputs for the CV values of the second row of parmeter.
        output31 (cv):
          Outputs for the CV values of the third row of parmeter.
        output32 (cv):
          Outputs for the CV values of the third row of parmeter.
        output33 (cv):
          Outputs for the CV values of the third row of parmeter.
        output34 (cv):
          Outputs for the CV values of the third row of parmeter.
        output41 (cv):
          Outputs for the CV values of the fourth row of parmeter.
        output42 (cv):
          Outputs for the CV values of the fourth row of parmeter.
        output43 (cv):
          Outputs for the CV values of the fourth row of parmeter.
        output44 (cv):
          Outputs for the CV values of the fourth row of parmeter.
        button11 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the first row is selected.
        button12 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the first row is selected.
        button13 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the first row is selected.
        button14 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the first row is selected.
        button21 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the second row is selected.
        button22 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the second row is selected.
        button23 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the second row is selected.
        button24 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the second row is selected.
        button31 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the third row is selected.
        button32 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the third row is selected.
        button33 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the third row is selected.
        button34 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the third row is selected.
        button41 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the fourth row is selected.
        button42 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the fourth row is selected.
        button43 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the fourth row is selected.
        button44 (gate):
          Give access to the state of the touch button below the faders when the
          respective output in the fourth row is selected.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 640

    firstfader: str | None = Field(
        default=None,
        serialization_alias="firstfader",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "f"},
    )
    rowcolumn: str | None = Field(
        default=None,
        serialization_alias="rowcolumn",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "rc"},
    )
    notches1: str | None = Field(
        default=None,
        serialization_alias="notches1",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n1"},
    )
    notches2: str | None = Field(
        default=None,
        serialization_alias="notches2",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n2"},
    )
    notches3: str | None = Field(
        default=None,
        serialization_alias="notches3",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n3"},
    )
    notches4: str | None = Field(
        default=None,
        serialization_alias="notches4",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n4"},
    )
    startvalue1: str | None = Field(
        default=None,
        serialization_alias="startvalue1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv1"},
    )
    startvalue2: str | None = Field(
        default=None,
        serialization_alias="startvalue2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv2"},
    )
    startvalue3: str | None = Field(
        default=None,
        serialization_alias="startvalue3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv3"},
    )
    startvalue4: str | None = Field(
        default=None,
        serialization_alias="startvalue4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv4"},
    )
    ledvalue11: str | None = Field(
        default=None,
        serialization_alias="ledvalue11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l11"},
    )
    ledvalue12: str | None = Field(
        default=None,
        serialization_alias="ledvalue12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l12"},
    )
    ledvalue13: str | None = Field(
        default=None,
        serialization_alias="ledvalue13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l13"},
    )
    ledvalue14: str | None = Field(
        default=None,
        serialization_alias="ledvalue14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l14"},
    )
    ledvalue21: str | None = Field(
        default=None,
        serialization_alias="ledvalue21",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l21"},
    )
    ledvalue22: str | None = Field(
        default=None,
        serialization_alias="ledvalue22",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l22"},
    )
    ledvalue23: str | None = Field(
        default=None,
        serialization_alias="ledvalue23",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l23"},
    )
    ledvalue24: str | None = Field(
        default=None,
        serialization_alias="ledvalue24",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l24"},
    )
    ledvalue31: str | None = Field(
        default=None,
        serialization_alias="ledvalue31",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l31"},
    )
    ledvalue32: str | None = Field(
        default=None,
        serialization_alias="ledvalue32",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l32"},
    )
    ledvalue33: str | None = Field(
        default=None,
        serialization_alias="ledvalue33",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l33"},
    )
    ledvalue34: str | None = Field(
        default=None,
        serialization_alias="ledvalue34",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l34"},
    )
    ledvalue41: str | None = Field(
        default=None,
        serialization_alias="ledvalue41",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l41"},
    )
    ledvalue42: str | None = Field(
        default=None,
        serialization_alias="ledvalue42",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l42"},
    )
    ledvalue43: str | None = Field(
        default=None,
        serialization_alias="ledvalue43",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l43"},
    )
    ledvalue44: str | None = Field(
        default=None,
        serialization_alias="ledvalue44",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l44"},
    )
    ledcolor1: str | None = Field(
        default=None,
        serialization_alias="ledcolor1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc1"},
    )
    ledcolor2: str | None = Field(
        default=None,
        serialization_alias="ledcolor2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc2"},
    )
    ledcolor3: str | None = Field(
        default=None,
        serialization_alias="ledcolor3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc3"},
    )
    ledcolor4: str | None = Field(
        default=None,
        serialization_alias="ledcolor4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc4"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output11: str | None = Field(
        default=None,
        serialization_alias="output11",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o11"},
    )
    output12: str | None = Field(
        default=None,
        serialization_alias="output12",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o12"},
    )
    output13: str | None = Field(
        default=None,
        serialization_alias="output13",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o13"},
    )
    output14: str | None = Field(
        default=None,
        serialization_alias="output14",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o14"},
    )
    output21: str | None = Field(
        default=None,
        serialization_alias="output21",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o21"},
    )
    output22: str | None = Field(
        default=None,
        serialization_alias="output22",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o22"},
    )
    output23: str | None = Field(
        default=None,
        serialization_alias="output23",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o23"},
    )
    output24: str | None = Field(
        default=None,
        serialization_alias="output24",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o24"},
    )
    output31: str | None = Field(
        default=None,
        serialization_alias="output31",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o31"},
    )
    output32: str | None = Field(
        default=None,
        serialization_alias="output32",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o32"},
    )
    output33: str | None = Field(
        default=None,
        serialization_alias="output33",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o33"},
    )
    output34: str | None = Field(
        default=None,
        serialization_alias="output34",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o34"},
    )
    output41: str | None = Field(
        default=None,
        serialization_alias="output41",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o41"},
    )
    output42: str | None = Field(
        default=None,
        serialization_alias="output42",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o42"},
    )
    output43: str | None = Field(
        default=None,
        serialization_alias="output43",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o43"},
    )
    output44: str | None = Field(
        default=None,
        serialization_alias="output44",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o44"},
    )
    button11: str | None = Field(
        default=None,
        serialization_alias="button11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b11"},
    )
    button12: str | None = Field(
        default=None,
        serialization_alias="button12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b12"},
    )
    button13: str | None = Field(
        default=None,
        serialization_alias="button13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b13"},
    )
    button14: str | None = Field(
        default=None,
        serialization_alias="button14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b14"},
    )
    button21: str | None = Field(
        default=None,
        serialization_alias="button21",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b21"},
    )
    button22: str | None = Field(
        default=None,
        serialization_alias="button22",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b22"},
    )
    button23: str | None = Field(
        default=None,
        serialization_alias="button23",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b23"},
    )
    button24: str | None = Field(
        default=None,
        serialization_alias="button24",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b24"},
    )
    button31: str | None = Field(
        default=None,
        serialization_alias="button31",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b31"},
    )
    button32: str | None = Field(
        default=None,
        serialization_alias="button32",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b32"},
    )
    button33: str | None = Field(
        default=None,
        serialization_alias="button33",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b33"},
    )
    button34: str | None = Field(
        default=None,
        serialization_alias="button34",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b34"},
    )
    button41: str | None = Field(
        default=None,
        serialization_alias="button41",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b41"},
    )
    button42: str | None = Field(
        default=None,
        serialization_alias="button42",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b42"},
    )
    button43: str | None = Field(
        default=None,
        serialization_alias="button43",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b43"},
    )
    button44: str | None = Field(
        default=None,
        serialization_alias="button44",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b44"},
    )


class Motorfader(DroidCircuit):
    """ Create virtual fader in M4 controller

    Args:
        fader (integer):
          The number of the motor fader to use, starting with 1 for the first fader in
          the first M4. 5 selects the first fader in the second M4 and so on.
        startvalue (cv):
          This sets the value the fader gets when you start this circuit this first time
          or when a trigger to clear happens.
        notches (integer):
          Number of artifical notches. 0 disables the notches. 1 creates a pitch bend
          wheel. 2 creates a binary switch with the output values 0 and 1. Higher number
          create that number of notches. E.g. 8 creates eight notches and output will
          output one of the value 0, 1, ... 8. The maximum allowed number is 25.
        ledvalue (cv):
          When you use this input, it will override the brightness of the LED below the
          fader, but just when this circuit is selected.  And there is a special trick:
          When you use a negative value for ledvalue, it switches to a magical mode.
          Here the LED is at full brightness when the current setting of the motorfader
          matches its startvalue, whereas the setting of ledvalue is used (made
          positive) in all other cases.
        ledcolor (cv):
          When you use this input, it will set the color of the LED below the fader,
          when the circuit is selected. If the LED is off, this setting has now impact.
        sharewithnext (gate):
          If set to 1, the output output will not be used but the circuit shares it's
          output with the next motorfader circuit.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output (cv):
          Output the current value if the virtual motor fader (don't use this if you are
          using sharewithnext).
        button (gate):
          This output provides you with the current state of the touch button below the
          fader, but only if the circuit is selected. While you could do this with an
          extra button circuit, using this output is more convenient in some situations.
          While the circuit is not selected, the output is set to 0.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 112

    fader: str | None = Field(
        default=None,
        serialization_alias="fader",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "f"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    notches: str | None = Field(
        default=None,
        serialization_alias="notches",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n"},
    )
    ledvalue: str | None = Field(
        default=None,
        serialization_alias="ledvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lv"},
    )
    ledcolor: str | None = Field(
        default=None,
        serialization_alias="ledcolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "lc"},
    )
    sharewithnext: str | None = Field(
        default=None,
        serialization_alias="sharewithnext",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sw"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )
    button: str | None = Field(
        default=None,
        serialization_alias="button",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b"},
    )


class Notebuttons(DroidCircuit):
    """ Note Selection Buttons

    Args:
        button1 (trigger):
          Wire 12 buttons to these 12 inputs.
        button2 (trigger):
          Wire 12 buttons to these 12 inputs.
        button3 (trigger):
          Wire 12 buttons to these 12 inputs.
        button4 (trigger):
          Wire 12 buttons to these 12 inputs.
        button5 (trigger):
          Wire 12 buttons to these 12 inputs.
        button6 (trigger):
          Wire 12 buttons to these 12 inputs.
        button7 (trigger):
          Wire 12 buttons to these 12 inputs.
        button8 (trigger):
          Wire 12 buttons to these 12 inputs.
        button9 (trigger):
          Wire 12 buttons to these 12 inputs.
        button10 (trigger):
          Wire 12 buttons to these 12 inputs.
        button11 (trigger):
          Wire 12 buttons to these 12 inputs.
        button12 (trigger):
          Wire 12 buttons to these 12 inputs.
        clock (trigger):
          When you use this jack, all button presses are quantized in time to the next
          clock pulse arriving here. That makes it easier to switch the note exactly in
          time.
        startnote (integer):
          Specify the note that should be selected when the Droid starts and no state is
          loaded, or when a trigger to clear or clearall happened. This is an integer
          number from 0 to 11.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        led1 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led2 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led3 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led4 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led5 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led6 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led7 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led8 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led9 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led10 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led11 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        led12 (gate):
          Wire the LEDs in the buttons to these 12 outputs.
        output (integer):
          Here you get a number from 0 to 11, according to the currently selected
          button.
        semitone (voltperoctave):
          Here you get the same as output, but divided by 120. When you patch this
          output to a CV output of the , like O1, it will output the note as a semitone
          on a 1 V per octave scheme.
        gate (gate):
          This output is 1 as long as one of the buttons is held. You can use that
          together with the semitone output to use the notebuttons as a CV/gate keyboard
          with 12 keys.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 128

    button1: str | None = Field(
        default=None,
        serialization_alias="button1",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b1"},
    )
    button2: str | None = Field(
        default=None,
        serialization_alias="button2",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b2"},
    )
    button3: str | None = Field(
        default=None,
        serialization_alias="button3",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b3"},
    )
    button4: str | None = Field(
        default=None,
        serialization_alias="button4",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b4"},
    )
    button5: str | None = Field(
        default=None,
        serialization_alias="button5",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b5"},
    )
    button6: str | None = Field(
        default=None,
        serialization_alias="button6",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b6"},
    )
    button7: str | None = Field(
        default=None,
        serialization_alias="button7",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b7"},
    )
    button8: str | None = Field(
        default=None,
        serialization_alias="button8",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b8"},
    )
    button9: str | None = Field(
        default=None,
        serialization_alias="button9",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b9"},
    )
    button10: str | None = Field(
        default=None,
        serialization_alias="button10",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b10"},
    )
    button11: str | None = Field(
        default=None,
        serialization_alias="button11",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b11"},
    )
    button12: str | None = Field(
        default=None,
        serialization_alias="button12",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "b12"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
    )
    startnote: str | None = Field(
        default=None,
        serialization_alias="startnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sn"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    led1: str | None = Field(
        default=None,
        serialization_alias="led1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l1"},
    )
    led2: str | None = Field(
        default=None,
        serialization_alias="led2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l2"},
    )
    led3: str | None = Field(
        default=None,
        serialization_alias="led3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l3"},
    )
    led4: str | None = Field(
        default=None,
        serialization_alias="led4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l4"},
    )
    led5: str | None = Field(
        default=None,
        serialization_alias="led5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l5"},
    )
    led6: str | None = Field(
        default=None,
        serialization_alias="led6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l6"},
    )
    led7: str | None = Field(
        default=None,
        serialization_alias="led7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l7"},
    )
    led8: str | None = Field(
        default=None,
        serialization_alias="led8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l8"},
    )
    led9: str | None = Field(
        default=None,
        serialization_alias="led9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l9"},
    )
    led10: str | None = Field(
        default=None,
        serialization_alias="led10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l10"},
    )
    led11: str | None = Field(
        default=None,
        serialization_alias="led11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l11"},
    )
    led12: str | None = Field(
        default=None,
        serialization_alias="led12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "l12"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "o"},
    )
    semitone: str | None = Field(
        default=None,
        serialization_alias="semitone",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "st"},
    )
    gate: str | None = Field(
        default=None,
        serialization_alias="gate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g"},
    )


class Nudge(DroidCircuit):
    """ Modify a value in steps using two buttons

    Args:
        buttonup (trigger):
          Button for nudging the value up by one step
        buttondown (trigger):
          Button for nudging the value down by one step
        amount (cv):
          Amount to modify the value by on each press. This must be a value > 0
        startvalue (cv):
          The value this circuit starts with or is being reset to if you use the clear
          input.
        minimum (cv):
          The minimum possible value. If you do not wire this, the value can go down
          infinitely.
        maximum (cv):
          the maximum possible value. If you do not wire this, the value can go up
          infinitely.
        wrap (gate):
          Set this to 1 in order to have the value wrap around if the minimum or the
          maximum has been exceeded. Note: wrap does only work if you set minimum and
          maximum.
        offset (cv):
          This value is being added to the output.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        ledup (stepped):
          Wire this to the LED in the button for nuding up. It will indicate the current
          value.
        leddown (stepped):
          Wire this to the LED in the button for nuding down. It will indicate the
          current value.
        output (cv):
          The output of the current value plus value if offset.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 144

    buttonup: str | None = Field(
        default=None,
        serialization_alias="buttonup",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "u"},
    )
    buttondown: str | None = Field(
        default=None,
        serialization_alias="buttondown",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "d"},
    )
    amount: str | None = Field(
        default=None,
        serialization_alias="amount",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "am"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    minimum: str | None = Field(
        default=None,
        serialization_alias="minimum",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "m"},
    )
    maximum: str | None = Field(
        default=None,
        serialization_alias="maximum",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "x"},
    )
    wrap: str | None = Field(
        default=None,
        serialization_alias="wrap",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "w"},
    )
    offset: str | None = Field(
        default=None,
        serialization_alias="offset",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "of"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    ledup: str | None = Field(
        default=None,
        serialization_alias="ledup",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "lu"},
    )
    leddown: str | None = Field(
        default=None,
        serialization_alias="leddown",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "ld"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Pot(DroidCircuit):
    """ Helper circuit for pots

    Args:
        pot (fraction):
          Wire your pot here, e.g. P1.1
        outputscale (cv):
          The final output is multiplied with this value. It's a convenient method for
          scaling up and down the pot range.
        notch (cv):
          By setting this parameter to a positive number you create an artificial
          “notch” of that size. We suggest using 0.1 (or 10%.  The maximum allowed value
          is 0.5. Greater values will be reduced to that.  Note: Using this in
          combination with outputscale also moves the notching point.  E.g. with
          outputscale = 2 the notch will be at 1.0.
        discrete (integer):
          Setting this value to 1 or larger switches the pot over to select a discrete
          integer number, rather than a continous value. For example discrete = 5 makes
          the pot output one of the exact values 0, 1, 2, 3 or 4. This is ideal for
          selecting presets and similar. If you enable ledgauge (highly recommended), it
          shows you the value by using the LEDs of the master in an adapted way.  The
          maximum allowed number is 16.  When using discrete, the startvalue input is
          interpreted as a discrete number. So for example if you have discrete = 5, you
          can use startvalue = 3 to set the selected value to the number 3 after a
          trigger to clear. A potential outputscale is applied afterwards.  Notes: The
          options notch and slope do not work in discrete mode. outputscale is still
          applied, though. All outputs other than output are dead and output 0.0.
          discrete = 1 does not really make sense, since there is just one value to
          select from and the output will always be 0.0.
        slope (cv):
          Changes the resolution of the pot in lower or higher ranges. Set slope to 2 or
          more, if you want small values near 0.0 to be “zoomed in”. Set slope to 0.5 or
          0.3 if you want to zoom in value nears 1.0.
        ledgauge (cv):
          The “LED gauge” uses the 16 LEDs of the MASTER in order to indicate the
          current value of the pot (not available on the MASTER18). This is especially
          useful for “virtual” pots – i.e. those pots that you get when you use select
          in order to layer several different functions onto one pot.  In that situation
          the position of the physical pot can be different than that of the virtual
          one, so the gauge shows you the effective virtual value.  Furthermore, by
          illuminating the inner four LEDs, the gauge shows when the pot hits exactly
          0.5. This can only happen if you use the notch parameter. Otherwise its
          practically impossible to hit exactly.  If you have a MASTER18, the gauge is
          displayed in the upper 16 LEDs of your first B32, if you have one.  The LED
          gauge is automatically activated if you use select. If you don't like the LED
          gauge, you can turn it off with ledgauge = off. Otherwise ledgauge set's the
          color of the indicator in the same way as the R-registers do and at the same
          time enables the gauge even if you don't use select.  Here are some color
          examples that you can use for the value of ledgauge:   0.2cyan 0.4green
          0.6yellow 0.73orange 0.8red 1.0magenta 1.1violet 1.2blue   The colors repeat
          over in a kind of wheel at 1.2, so e.g. 1.4 creates the same color as 0.2.
        startvalue (fraction):
          This parameter defines the value your pot will get when there is a trigger to
          clear. This is the value before outputscale is applied.  If you use discrete,
          the parameter does not expect a fraction but a discrete number in the range of
          the discrete values (0, 1, 2, etc.
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        preset (integer):
          This is the preset number to save or to load. Note: the first preset has the
          number 0, not 1! For the whole story on presets please refer to page 21.
        loadpreset (trigger):
          A trigger here loads a preset. As a speciality you can use the trigger for
          selecting a preset at the same time.
        savepreset (trigger):
          A trigger here saves a preset.
        clear (trigger):
          A trigger here loads the default start state into the circuit. The presets are
          not affected, unless you use direct preset switching with the preset input and
          without triggers. And that case the current preset is also cleared.
        clearall (trigger):
          A trigger here loads the default start state into the circuit and into all of
          its presets.
        dontsave (gate):
          If you set this to 1, the state of the circuit will not saved to the SD card
          and not loaded from the SD card when the Droid starts.
        output (fraction):
          Your pot output comes here.
        bipolar (cv):
          Optional output with a range from -1.0 to 1.0, where the center notch is at
          0.0 (or from -outputscale to +outputscale if that is used).
        absbipolar (cv):
          A variation of bipolar that always outputs a positive value, i.e. the pot will
          go 1 ... 0.5 ... 0 ... 0.5 ... 1 (if outputscale is not used).
        lefthalf (cv):
          This output allows you to split the pot into two hemispheres. Here you get
          outputscale ... 0.0 while the pot is in the left half. In the middle and right
          of it you always get 0.
        righthalf (cv):
          This is the same but for the right half. It outputs 0 while the pot is in the
          left half and 0.0 ... outputscale from the middle to the fully right position.
        lefthalfinv (cv):
          This outputs 1.0 - lefthalf, i.e. the value range 0.0 ... 1.0 ... 1.0 when the
          pot moves left → mid → right (and the scaled by outputscale).
        righthalfinv (cv):
          This outputs 1.0 - righthalf, i.e. the value range 1.0 ... 1.0 ... 0.0 when
          the pot moves left → mid → right (and the scaled by outputscale).
        onchange (trigger):
          This output emits a trigger whenever the pot is turned in either direction.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 120

    pot: str | None = Field(
        default=None,
        serialization_alias="pot",
        json_schema_extra={"essential": 2, "type": "fraction", "shortname": "p"},
    )
    outputscale: str | None = Field(
        default=None,
        serialization_alias="outputscale",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "os"},
    )
    notch: str | None = Field(
        default=None,
        serialization_alias="notch",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "no"},
    )
    discrete: str | None = Field(
        default=None,
        serialization_alias="discrete",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "d"},
    )
    slope: str | None = Field(
        default=None,
        serialization_alias="slope",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sl"},
    )
    ledgauge: str | None = Field(
        default=None,
        serialization_alias="ledgauge",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "g"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "sv"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )
    preset: str | None = Field(
        default=None,
        serialization_alias="preset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pr"},
    )
    loadpreset: str | None = Field(
        default=None,
        serialization_alias="loadpreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lp"},
    )
    savepreset: str | None = Field(
        default=None,
        serialization_alias="savepreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    clearall: str | None = Field(
        default=None,
        serialization_alias="clearall",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ca"},
    )
    dontsave: str | None = Field(
        default=None,
        serialization_alias="dontsave",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dos"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "fraction", "shortname": "o"},
    )
    bipolar: str | None = Field(
        default=None,
        serialization_alias="bipolar",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "b"},
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
    onchange: str | None = Field(
        default=None,
        serialization_alias="onchange",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c"},
    )


class Unusedfaders(DroidCircuit):
    """ Declare unused motor faders

    Args:
        firstfader (integer):
          The number of the first unused motor fader motor.
        numfaders (integer):
          The number of unused faders
        select (integer):
          The select input allows you to overlay buttons and LEDs with multiple
          functions. If you use this input, the circuit will process the buttons and
          LEDs just as if select has a positive gate signal (usually you will select
          this to 1). Otherwise it won't touch them so they can be used by another
          circuit. Note: even if the circuit is currently not selected, it will
          nevertheless work and process all its other inputs and its  outputs (those
          that do not deal with buttons or LEDs) in a normal way.
        selectat (integer):
          This input makes the select input more flexible. Here you specify at which
          value select should select this circuit. E.g. if selectat is 0, the circuit
          will be active if select is exactly 0 instead of a positive gate signal. In
          some cases this is more conventient.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    firstfader: str | None = Field(
        default=None,
        serialization_alias="firstfader",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "f"},
    )
    numfaders: str | None = Field(
        default=None,
        serialization_alias="numfaders",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n"},
    )
    select: str | None = Field(
        default=None,
        serialization_alias="select",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    selectat: str | None = Field(
        default=None,
        serialization_alias="selectat",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sa"},
    )

