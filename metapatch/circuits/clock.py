"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Bernoulli(DroidCircuit):
    """ Random gate distributor

    Args:
        input (gate):
          Send gate or trigger signals here.
        distribution (bipolar):
          This controls the probability of a gate to be forwarded to output1. A value of
          0.5 means 50%.
        output1 (gate):
          Gates from input are forwarded here if the random decision was in favour of
          output 1.
        output2 (gate):
          Gates from input are forwarded here if the random decision was in favour of
          output 2.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "i"},
    )
    distribution: str | None = Field(
        default=None,
        serialization_alias="distribution",
        json_schema_extra={"essential": 1, "type": "bipolar", "shortname": "di"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "o2"},
    )


class Burst(DroidCircuit):
    """ Generate burst of pulses

    Args:
        rate (cv):
          Frequency control: The default frequency of the burst rate is 1 Hz (one
          trigger per second or 60 BPM if you like). Each volt doubles the frequency. So
          an input of 1 V (a number of 0.1) speeds up to two triggers per second
          (120 BPM), 2 V (0.2) creates triggers at 4 Hz (240 BPM) and so on. On the
          other hand negative voltages reduce the speed, so -1 V (-0.1) will give 0.5 Hz
          (30 BPM) and so on.
        taptempo (trigger):
          Feed a reference clock here and the burst will run at the speed of that clock
          – albeit optionally modified by rate. Please see page 23 for details on using
          taptempo inputs.
        hz (cv):
          Set the frequency in Hz directly by setting a number here. This is exclusive
          to taptempo, but will work in combination with rate.
        trigger (trigger):
          Send a trigger here in order to start the bursts
        reset (trigger):
          Send a trigger here to immediately stop any ongoing burst.
        count (integer):
          Number of triggers to send in one burst.
        skip (integer):
          Number of time slots to wait before starting with the burst.
        output (trigger):
          The triggers are output here.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 40

    rate: str | None = Field(
        default=None,
        serialization_alias="rate",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "ra"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "tt"},
    )
    hz: str | None = Field(
        default=None,
        serialization_alias="hz",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": ""},
    )
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "t"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "r"},
    )
    count: str | None = Field(
        default=None,
        serialization_alias="count",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "c"},
    )
    skip: str | None = Field(
        default=None,
        serialization_alias="skip",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "o"},
    )


class Clocktool(DroidCircuit):
    """ Clock divider / multiplier / shifter

    Args:
        clock (trigger):
          Patch a steady clock here for this circuit to be of any use
        reset (trigger):
          A trigger here resets the internal counters. This is useful if you use the
          clock divider and want to restart the internal counting from 0, in order to
          align the clock divider with some external sequencers or the like
        divide (integer):
          Number to divide the clock through. This will be rounded to the nearest
          integer number. Note: if you want to use an external CV then you need to
          multiply that with some useful number, since otherwise you will get a number
          between 0 and 1 which is not useful at all. Remember: 10 V translates to a
          number of 1.
        multiply (integer):
          Number to multiply the clock with. Same considerations hold as for divide.
        dutycycle (bipolar):
          Output duty cycle of the clock – which is essentially a square wave – in a
          range from 0.0 to 1.0 or 0% to 100%. If you don't patch anything here, the
          length of the trigger output pulses will be 10 ms ('s standard trigger
          duration).
        gatelength (cv):
          This jack is alternative to dutycycle and will override it if it is used.
          It sets the length of each output pulse to a fixed value that is independent
          of the incoming clock. A value of 0.5 (a CV of 5 volts) translates into a gate
          length of 0.5 seconds.
        delay (cv):
          This CV allows you to shift the input clock beat around in time. A value of
          0.1 will delay each beat by 10% of a clock cycle. A value of -0.1 is also
          allowed and shifts the beat 10% ahead.  For an unmodulated delay -0.1 and 0.9
          is just the same, because the output clock will have the same relation to the
          input clock. But if you modify the delay from 0.0 to 0.9, the next tick will
          be delayed by 90% of one cycle, where is a modification from 0.0 to -0.1 will
          play the next tick by 10% earlier.
        output (gate):
          Here comes the modified clock
        inputpitch (cv):
          Experimental output that outputs a representation of the input clock's pitch
          on a 1V/octave base, based on the reference of 60 BPM (1 Hz). This means that
          an input clock of 120 BPM will output 1V (a value of 0.1), since 120 BPM it is
          one octave higher than 60 BPM. If you feed that value to the rate input of an
          LFO you get that running at exactly the same speed (not in the same phase,
          however).
        outputpitch (cv):
          Same for the modified output clock
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 96

    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "c"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    divide: str | None = Field(
        default=None,
        serialization_alias="divide",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "d"},
    )
    multiply: str | None = Field(
        default=None,
        serialization_alias="multiply",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "m"},
    )
    dutycycle: str | None = Field(
        default=None,
        serialization_alias="dutycycle",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "dc"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "gl"},
    )
    delay: str | None = Field(
        default=None,
        serialization_alias="delay",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "dl"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "o"},
    )
    inputpitch: str | None = Field(
        default=None,
        serialization_alias="inputpitch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ip"},
    )
    outputpitch: str | None = Field(
        default=None,
        serialization_alias="outputpitch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "op"},
    )


class Flipflop(DroidCircuit):
    """ Simple flip flop

    Args:
        toggle (trigger):
          A trigger here inverts the state of the flip flop. It changes 0 to 1 and 1 to
          0.
        set (trigger):
          Sets the flip flop to 1.
        reset (trigger):
          Sets the flip flop to 0.
        clear (trigger):
          Sets the flip flop to the value defined by startvalue.
        startvalue (gate):
          The flip flop starts its live with this value. Also clear will set the flip
          flop to this value.
        load (trigger):
          Loads the value into the flip flop that's defined with loadvalue.
        loadvalue (gate):
          Value to set the flip flop to, when load is triggered.
        output (gate):
          Outputs the current value of the flip flop: either 0 or 1.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 40

    toggle: str | None = Field(
        default=None,
        serialization_alias="toggle",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "t"},
    )
    set: str | None = Field(
        default=None,
        serialization_alias="set",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "s"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "r"},
    )
    clear: str | None = Field(
        default=None,
        serialization_alias="clear",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cl"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sv"},
    )
    load: str | None = Field(
        default=None,
        serialization_alias="load",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ld"},
    )
    loadvalue: str | None = Field(
        default=None,
        serialization_alias="loadvalue",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lv"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "o"},
    )


class Gatetool(DroidCircuit):
    """ Operate on triggers and gates, modify gatelength

    Args:
        inputgate (gate):
          Input gate. Use this if the length of the input gate is relevant.
        inputtrigger (trigger):
          Input trigger. Use this if the length of the input gate should be ignored.
        inputedge (gate):
          Input edge: Use this if every low/high or high/low transition should count as
          a trigger.
        gatelength (cv):
          Sets the length of the gate of outputgate in seconds. If you use taptempo the
          length is in fractions of a clock tick, instead.
        gatestretch (cv):
          Makes the output gate longer than the input gate by the given percentage. This
          parameter is ignored if gatelength is used.
        mingatelength (cv):
          Defines a minimum length of the output gate in seconds or clock ticks.
        maxgatelength (cv):
          Defines a maximum length of the output gate in seconds or clock ticks.
        taptempo (trigger):
          If you patch a reference clock here, gatelength, mingatelength and
          maxgatelength are fractions of one clock tick, not seconds anymore. Please see
          page 23 for details on using taptempo inputs.
        outputgate (gate):
          Outputs a gate with controllable length for every gate, trigger or edge event.
        outputtrigger (trigger):
          Outputs a 10 ms trigger for every gate, trigger or edge event.
        outputedge (gate):
          Toggle between 0 and 1 at every gate, trigger or edge event.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    inputgate: str | None = Field(
        default=None,
        serialization_alias="inputgate",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "ig"},
    )
    inputtrigger: str | None = Field(
        default=None,
        serialization_alias="inputtrigger",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "it"},
    )
    inputedge: str | None = Field(
        default=None,
        serialization_alias="inputedge",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ie"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "gl"},
    )
    gatestretch: str | None = Field(
        default=None,
        serialization_alias="gatestretch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "s"},
    )
    mingatelength: str | None = Field(
        default=None,
        serialization_alias="mingatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "m"},
    )
    maxgatelength: str | None = Field(
        default=None,
        serialization_alias="maxgatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "x"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "tt"},
    )
    outputgate: str | None = Field(
        default=None,
        serialization_alias="outputgate",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "og"},
    )
    outputtrigger: str | None = Field(
        default=None,
        serialization_alias="outputtrigger",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ot"},
    )
    outputedge: str | None = Field(
        default=None,
        serialization_alias="outputedge",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "oe"},
    )


class Once(DroidCircuit):
    """ Output one trigger after the Droid has started

    Args:
        delay (cv):
          Set a delay in seconds after the Droid's start before the trigger triggers.
          Note: the default value is 10 ms, not zero. This allows all attached
          controllers to have sent at least one update before and the real pot values
          etc. are available at the circuits.
        onlycoldstart (gate):
          If you set this input to 1, once just sends a trigger after a cold start,
          only. A cold start means that the Droid has been powered up. Pressing the
          button for loading a new patch and does a warm start.
        trigger (trigger):
          The trigger is output here.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 24

    delay: str | None = Field(
        default=None,
        serialization_alias="delay",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "dl"},
    )
    onlycoldstart: str | None = Field(
        default=None,
        serialization_alias="onlycoldstart",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "c"},
    )
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "t"},
    )


class Timing(DroidCircuit):
    """ Shuffle/swing and complex timing generator

    Args:
        clock (trigger):
          Patch a steady clock here for this circuit to be of any use
        reset (trigger):
          A trigger here resets the internal step counter and restart at step 1.
        timing1 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing2 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing3 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing4 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing5 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing6 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing7 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        timing8 (cv):
          Specifies a relative timing for each step in relation to the input clock. A
          timing of 0.3 will shift the respective beat 30
        output (trigger):
          Here comes the modified output clock
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "c"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    timing1: str | None = Field(
        default=None,
        serialization_alias="timing1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "t1"},
    )
    timing2: str | None = Field(
        default=None,
        serialization_alias="timing2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "t2"},
    )
    timing3: str | None = Field(
        default=None,
        serialization_alias="timing3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t3"},
    )
    timing4: str | None = Field(
        default=None,
        serialization_alias="timing4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t4"},
    )
    timing5: str | None = Field(
        default=None,
        serialization_alias="timing5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t5"},
    )
    timing6: str | None = Field(
        default=None,
        serialization_alias="timing6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t6"},
    )
    timing7: str | None = Field(
        default=None,
        serialization_alias="timing7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t7"},
    )
    timing8: str | None = Field(
        default=None,
        serialization_alias="timing8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t8"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "o"},
    )


class Triggerdelay(DroidCircuit):
    """ Trigger Delay with multi tap and optional clocking

    Args:
        input (gate):
          Patch triggers or gates to be delayed here.
        delay (cv):
          Amount of time the incoming triggers are being delayed. When clock is patched,
          this is in relation to one clock cycle, so a delay of 4 will delay the input
          pattern by exactly 4 beats. Fractions are allowed also. If clock is not
          patched, this parameter is in seconds. So for example in order to delay by
          100 ms you need a delay of 0.1.
        gatelength (cv):
          Unless you patch this jack the length of the output gates is exactly the
          length of the input gates. By use of this parameter you override that length
          and set a fixed length in seconds – or if clock is being used – in clock
          cycles.
        repeats (integer):
          Number of times the delayed trigger is being repeated. Each further repetition
          is with the same delay.
        mute (gate):
          A high gate signal suppresses any further output gates. However, the current
          gate is finished normally.
        clock (trigger):
          When you patch this input, the trigger delay runs in clocked mode. In this
          mode delay is relative to one clock cycle. I.e. a delay if 0.5 will delay the
          trigger by half a clock cycle. The same holds for gatelength. That is measured
          in clock cycles, too.
        output (gate):
          Outputs the delayed triggers/gates, while keeping the gate length – unless you
          have changed that
        overflow (gate):
          Whenever there are more input triggers than this circuit can keep memory of,
          this output outputs a gate of 0.5 sec length. You can wire this to an LED in
          order to know when this happens.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 248

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "i"},
    )
    delay: str | None = Field(
        default=None,
        serialization_alias="delay",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "dl"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "gl"},
    )
    repeats: str | None = Field(
        default=None,
        serialization_alias="repeats",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "rp"},
    )
    mute: str | None = Field(
        default=None,
        serialization_alias="mute",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "m"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "o"},
    )
    overflow: str | None = Field(
        default=None,
        serialization_alias="overflow",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ov"},
    )

