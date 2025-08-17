"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Contour(DroidCircuit):
    """ Contour generator

    Args:
        gate (gate):
          Patch a gate signal here that triggers the envelope. Gate means that the
          length of the signal is relevant. While the gate is high the sustain phase
          holds on. As soon as gate is going low the release phase is being entered.
        trigger (trigger):
          This is an alternative method of starting the envelope. If you use trigger
          instead of gate, there are the following differences:
          * The duration of the trigger signal is being ignored.
          * There is no decay / sustain phase. Attack and hold are immediately followed
            by release. The inputs sustain and decay have no impact anymore.
          * The predelay and attack phases are continued until their end even when the
            trigger signal ends (When using gate and the gate signal ends during
            predelay, the envelope does not start. When it ends during attack, decay /
            sustain are being skipped and release starts at the current level of the
            envelope. That way short gates can result in “quieter” envelopes).

        retrigger (gate):
          If you patch 0 or off here, a gate or trigger impulse will not immediately
          restart the envelope unless it already has reached its release phase.  The
          default on, which means that a trigger will immediately restart the envelope
          in any case.
        startfromzero (gate):
          If you set this to 1 or on, a trigger or gate will reset the envelope's
          current level immediately to zero. This is sometimes called “digital mode”. In
          the normal analog mode the envelope resumes from where it is. This means that
          when a trigger occurs right in the release phase where the level is still
          high, will start it's attack not from zero but from this hight value.
        abortattack (gate):
          This is an on / off setting that decides what happens if the input gate goes
          off while the predelay or attack phase is still not finished. Per default that
          phase will be finalized regardless of the gate state.  If abortattack is on,
          the end of the gate will immediately stop the attack phase and move on to
          hold. Note: In this case the value of the envelope will not reach the maximum
          level. If the gate ends during the predelay phase, no envelope will be started
          at all.  Note: This setting is only functional when the gate input is being
          used for triggering the envelope. If you use trigger, the attack phase is
          always completely executed and this setting has no influence.
        loop (gate):
          This is an on / off input that switches loop on or off. When loop is on, the
          envelope will immediately start again once it has finished. It also starts
          without triggering. This converts contour into a kind of fancy LFO.  gate /
          trigger and loop can be combined. Any gate or trigger will restart the
          envelope just as usual – even in loop mode.
        predelay (cv):
          The predelay phase inserts a delay between the incoming gate and the begin of
          the envelope. The length of the predelay is 0.1 seconds per volt, so a value
          of 1.0 means 1 second
        attack (cv):
          Length of the attack phase, i.e. the time from the beginning of the gate until
          the maximum level is reached. See the general description for information
          about the scaling of this input.
        hold (cv):
          If this is none-zero, the envelopes lingers a certain amount of time at its
          maximum level after the attack and before the decay phase. The input value
          specifies a number of seconds. A value of 0.5 (this is 5 V) will create a hold
          time of 0.5 seconds.
        decay (cv):
          Time of the decay phase
        sustain (fraction):
          Sustain level
        swell (fraction):
          If this jack is set to a value greater than 0.0, the level of the envelope
          will go up or down again during the sustain phase until it reaches swelllevel.
        swelltime (cv):
          Time of the swell phase
        swelllevel (cv):
          Level the swell phase is approaching. Setting this to the same as sustain
          effectively disables swell.
        release (cv):
          Timing of the release phase
        level (cv):
          Maximum level and scaling of the envelope. It is basically an output
          attenuator of the envelope. Sudden changes in the level will immediately have
          an (audible) impact on the envelope.
        velocity (fraction):
          energy of the attack: The velocity is similar to the level, but is effective
          just during the attack phase. During that phase that maximum voltage that is
          read from the velocity jack and will be used as the velocity of the envelope.
          Further changes during the other phases will be ignored. This makes it ideal
          of using with a sequencer. For example you can patch an accent output here and
          add some offset. Sudden changes in this input will not affect the shape of the
          envelope.
        pitch (voltperoctave):
          This is a one volt per octave input affecting all timings of the envelope.
          When you set this to 0 (the default), it is neutral. A value of 0.1 (1 Volt)
          will exactly double the speed of all phases - just as one octave up doubles
          the frequency of an oscillator. This jack can be used to easily implement
          envelopes where the length very naturally follows this pitch - just like on a
          piano, glockenspiel or marimba lower notes last longer than higher ones.
        taptempo (trigger):
          Tap tempo is an alternative method of specifying a pitch information. When you
          patch a clock to tap tempo, all time parameters in the envelope are relative
          to that clock. If the clock speeds up, the envelope gets faster and vice
          versa. The reference speed is 120 BPM. This means that if you patch a 120 BPM
          clock here, nothing changes. Clocks faster than 120 BPM will speed up the
          envelope. Clocks slower than 120 BPM will slow it down.  Please see page 23
          for details on using taptempo inputs.
        shape (bipolar):
          If you use this jack, it sets the shape for all of the relevant phases, which
          are attack, decay, swell and release. Note: this input is only effective for
          those phases where the dedicated input (like attackshape, etc.) is not being
          used.
        attackshape (bipolar):
          Shape of the attack curve. If nothing is patched here, the value of shape will
          be used. See the general description for how curve shapes work.
        decayshape (bipolar):
          Shape of the curve in the decay phase. If nothing is patched here, the value
          of shape will be used.
        swellshape (bipolar):
          Shape of curve during the swell phase. If nothing is patched here, the value
          of shape will be used.
        releaseshape (bipolar):
          Shape of the curve in the release phase. If nothing is patched here, the value
          of shape will be used.
        zerocrossing (cv):
          This is an experimental feature: If you patch the output of an oscillator
          here, an incoming gate or trigger signal will be delayed until the next zero
          crossing of that signal. That allows you to start the envelope exactly when
          the audio signal is at 0 and avoid nasty klicks, even if the attack is set to
          0. It comes at a price, however. The delay between the trigger and the first
          zero crossing might vary a lot from note to note and that could make your
          rhythm untight, especially if the frequency of the oscillator is low.
        output (cv):
          Main output of the envelope. Patch this to your filter, VCA or wherever you
          like.
        negated (cv):
          The negated output is the same as the output but in negative voltage.
        inverted (cv):
          The inverted output always outputs positive voltages but is inverted relative
          to the level of the envelope. When the normal output outputs 0 V, the inverted
          output outputs level and vice versa
        endofpredelay (trigger):
          This output will emit a trigger with a length of 10 ms when the predelay phase
          has ended.
        endofattack (trigger):
          This output will emit a trigger with a length of 10 ms when the attack phase
          has ended.
        endofhold (trigger):
          This output will emit a trigger with a length of 10 ms when the hold phase has
          ended.
        endofdecay (trigger):
          This output will emit a trigger with a length of 10 ms when the decay phase
          has ended.
        endofrelease (trigger):
          This output will emit a trigger with a length of 10 ms when the release phase
          has ended.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 112

    gate: str | None = Field(
        default=None,
        serialization_alias="gate",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g"},
    )
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t"},
    )
    retrigger: str | None = Field(
        default=None,
        serialization_alias="retrigger",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "rt"},
    )
    startfromzero: str | None = Field(
        default=None,
        serialization_alias="startfromzero",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sz"},
    )
    abortattack: str | None = Field(
        default=None,
        serialization_alias="abortattack",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "aa"},
    )
    loop: str | None = Field(
        default=None,
        serialization_alias="loop",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lo"},
    )
    predelay: str | None = Field(
        default=None,
        serialization_alias="predelay",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pd"},
    )
    attack: str | None = Field(
        default=None,
        serialization_alias="attack",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "a"},
    )
    hold: str | None = Field(
        default=None,
        serialization_alias="hold",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "h"},
    )
    decay: str | None = Field(
        default=None,
        serialization_alias="decay",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "d"},
    )
    sustain: str | None = Field(
        default=None,
        serialization_alias="sustain",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "s"},
    )
    swell: str | None = Field(
        default=None,
        serialization_alias="swell",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "sw"},
    )
    swelltime: str | None = Field(
        default=None,
        serialization_alias="swelltime",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "st"},
    )
    swelllevel: str | None = Field(
        default=None,
        serialization_alias="swelllevel",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sl"},
    )
    release: str | None = Field(
        default=None,
        serialization_alias="release",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "r"},
    )
    level: str | None = Field(
        default=None,
        serialization_alias="level",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l"},
    )
    velocity: str | None = Field(
        default=None,
        serialization_alias="velocity",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v"},
    )
    pitch: str | None = Field(
        default=None,
        serialization_alias="pitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "tt"},
    )
    shape: str | None = Field(
        default=None,
        serialization_alias="shape",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "sh"},
    )
    attackshape: str | None = Field(
        default=None,
        serialization_alias="attackshape",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "as"},
    )
    decayshape: str | None = Field(
        default=None,
        serialization_alias="decayshape",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "ds"},
    )
    swellshape: str | None = Field(
        default=None,
        serialization_alias="swellshape",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "ss"},
    )
    releaseshape: str | None = Field(
        default=None,
        serialization_alias="releaseshape",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "rs"},
    )
    zerocrossing: str | None = Field(
        default=None,
        serialization_alias="zerocrossing",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "z"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "o"},
    )
    negated: str | None = Field(
        default=None,
        serialization_alias="negated",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "n"},
    )
    inverted: str | None = Field(
        default=None,
        serialization_alias="inverted",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "iv"},
    )
    endofpredelay: str | None = Field(
        default=None,
        serialization_alias="endofpredelay",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ep"},
    )
    endofattack: str | None = Field(
        default=None,
        serialization_alias="endofattack",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ea"},
    )
    endofhold: str | None = Field(
        default=None,
        serialization_alias="endofhold",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "eh"},
    )
    endofdecay: str | None = Field(
        default=None,
        serialization_alias="endofdecay",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ed"},
    )
    endofrelease: str | None = Field(
        default=None,
        serialization_alias="endofrelease",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "er"},
    )


class Lfo(DroidCircuit):
    """ Low frequency oscillator (LFO)

    Args:
        rate (cv):
          Frequency control: The default frequency of the LFO is 1 Hz (one cycle per
          second). Each volt doubles the frequency. So an input of 1 V (a number of 0.1)
          speeds up the LFO to 2 Hz, 2 V (0.2) create 4 Hz and so on. On the other hand
          negative voltages reduce the speed, so -1 V (-0.1) will give 0.5 Hz and so on.
        taptempo (trigger):
          Feed a reference clock here and the LFO will run at the speed of that clock –
          albeit optionally modified by rate and hz. Please see page 23 for details on
          using taptempo inputs.
        hz (cv):
          Set the frequency in Hz directly by setting a number here. Note: you cannot
          use hz at that same time as taptempo. But both can be combined with rate.
        level (cv):
          The maximum positive output level of the LFO. The default of 1.0 means a swing
          between 0 V and 10 V – unless you enable bipolar, in which case it moves from
          -10 V to 10 V.
        randomize (fraction):
          Randomization is an experimental new feature that combines random voltages
          with an LFO. If you turn this parameter up, then for each hill of the LFO's
          waveform output a new random attenuation is being chosen and multiplied with
          the current level. The result is an output, where each cycle of the waveform
          has a different level.
        offset (cv):
          The output of the LFO is shifted by that voltage right before the output. This
          is the same as adding or mixing a fixed voltage to the output. Not very fancy,
          but practical if you want to output a modulation voltage within a certain
          range.
        bipolar (gate):
          If this switch is set to on, then the LFO will output a full swing from -level
          to +level. When set to off it will swing between 0V and +level.
        phase (fraction):
          Shift the LFOs phase by this value. A value of 0.0 leaves the LFO run in its
          normal phase. 0.5 will shift bei 180^∘. And 1.0 will shift by a complete phase
          of 360^∘, which is the same as 0.0.
        pulsewidth (bipolar):
          This sets the pulse width of the square LFO and only affects the output
          square. It ranges from 0.0 to 1.0. Please note that a pulse width of exactly
          0.0 or 1.0 will make the output stick to the respective lower or upper level.
        skew (bipolar):
          Modifies the symmetry of the triangle output by shifting the “peak” of the
          triangle left and right. The default of 0.5 creates a symmetric waveform.
          Smaller values speed up the rising part of the triangle and create more and
          more a ramp like waveform until a skew of 0.0 creates an exact ramp – just the
          same as the ramp output. A skew of 1.0 create a sawtooth waveform.
        sync (trigger):
          A positive trigger edge at this input will reset the LFO. It will force to
          restart the waveform at its “beginning”. By using the input syncphase you can
          change that behaviour.
        syncphase (fraction):
          This input changes the behaviour of the sync input. I changes the phase the
          waveform restarts at when it receives a sync trigger. E.g. by setting this to
          0.5 a sync trigger will restart the waveform right at its middle. This is an
          interesting feature that cannot be found in analog LFOs since it would be very
          hard to build in actual circuits.
        waveform (cv):
          If you use output – rather than the individual waveform outputs like square,
          saw and so on – this input selects the Wave form. An integer number from 0 to
          6 selects one of the seven available waveforms. Any number in between selects
          a mixture of the two neighboring waveforms. That way you can smoothly morph
          through all the available waveforms. The codes for the waveforms are:
          0square 1sawtooth 2triangle 3ramp 4paraboloid 5sine 6cosine
        output (cv):
          Main output of the LFO.
        square (cv):
          A square waveform – modified by pulsewidth.
        sawtooth (cv):
          Outputs a sawtooth waveform – i.e. a rising ramp
        triangle (cv):
          Outputs a triangle waveform – modified by skew.
        ramp (cv):
          Outputs a falling ramp – like a sawtooth that is mirrored. Note: if the LFO is
          set to bipolar then this is the negation of sawtooth. If it is set to unipolar
          then this is not the case. The waveform will be positive then!
        paraboloid (cv):
          An experimental waveform that looks very similar to a sine wave but is derived
          from a triangle by computing the square of each waypoint's distance to level.
        sine (cv):
          A sine waveform.
        cosine (cv):
          A sine waveform shifted by 90^∘. This output is for your convenience and
          avoids needing two LFO circuits in cases where you want to make quadrature
          applications. Please note that 180^∘ and 270^∘ can easily be achieved by
          negating the outputs sine and cosine at a later stage.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 216

    rate: str | None = Field(
        default=None,
        serialization_alias="rate",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ra"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "tt"},
    )
    hz: str | None = Field(
        default=None,
        serialization_alias="hz",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": ""},
    )
    level: str | None = Field(
        default=None,
        serialization_alias="level",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "l"},
    )
    randomize: str | None = Field(
        default=None,
        serialization_alias="randomize",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "r"},
    )
    offset: str | None = Field(
        default=None,
        serialization_alias="offset",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "of"},
    )
    bipolar: str | None = Field(
        default=None,
        serialization_alias="bipolar",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b"},
    )
    phase: str | None = Field(
        default=None,
        serialization_alias="phase",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p"},
    )
    pulsewidth: str | None = Field(
        default=None,
        serialization_alias="pulsewidth",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "pw"},
    )
    skew: str | None = Field(
        default=None,
        serialization_alias="skew",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "sk"},
    )
    sync: str | None = Field(
        default=None,
        serialization_alias="sync",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sy"},
    )
    syncphase: str | None = Field(
        default=None,
        serialization_alias="syncphase",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "sp"},
    )
    waveform: str | None = Field(
        default=None,
        serialization_alias="waveform",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "w"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "o"},
    )
    square: str | None = Field(
        default=None,
        serialization_alias="square",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "q"},
    )
    sawtooth: str | None = Field(
        default=None,
        serialization_alias="sawtooth",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "st"},
    )
    triangle: str | None = Field(
        default=None,
        serialization_alias="triangle",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "t"},
    )
    ramp: str | None = Field(
        default=None,
        serialization_alias="ramp",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "rp"},
    )
    paraboloid: str | None = Field(
        default=None,
        serialization_alias="paraboloid",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pb"},
    )
    sine: str | None = Field(
        default=None,
        serialization_alias="sine",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "si"},
    )
    cosine: str | None = Field(
        default=None,
        serialization_alias="cosine",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "cs"},
    )


class Random(DroidCircuit):
    """ Random number generator

    Args:
        clock (trigger):
          Optional triggger: if this input is used then the output holds the current
          random number until the next clock impulse (sample & hold)
        minimum (cv):
          Minimum possible random number
        maximum (cv):
          Maximum possible random number
        steps (integer):
          Number of different voltage levels. If this is set to 0 (default), any voltage
          can appear, there is no limit. If this is 1, then there is no random any more
          since there is only one allowed step (which is the average between minimum and
          maximum. At 2 the only two possible output values are minimum and maximum. At
          3 the possible levels are minimum, minimum +  maximum/2 and maximum and so
          on...
        output (cv):
          Output of the random number / voltage
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
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
    steps: str | None = Field(
        default=None,
        serialization_alias="steps",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "s"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Spring(DroidCircuit):
    """ Physical spring simulation

    Args:
        mass (cv):
          The mass of the object on the spring. The heavier it is, the farther the
          spring will move up and down.
        gravity (cv):
          The gravity of the simulated planet the spring is mounted at. If you set the
          gravity to zero, the mass will move exactly around the zero position from
          positive to negative and back. But you need to shove it or set a start
          position other than 0, in order to get it started.
        springforce (cv):
          The force of the string per m it is stretched. In an ideal spring the force is
          proportional to the current elongation.
        flowresistance (cv):
          Setting this to a value > 0 will dampen the oscillation in a way, that higher
          velocities will be damped more then slower ones. This means that impact of the
          friction will get less and less as time goes by and the movement slows down.
        friction (cv):
          Setting this to a value > 0 will also dampen the oscillation, but in a way
          that is independent of the current speed of the mass.
        speed (cv):
          This parameter speeds up or slows down the perceived time. It works on a
          1V/Oct base. Every positive 1V (or 0.1) doubles the speed. So if you set speed
          to 2V or 0.2 it will speed up the movement by a factor of 4. An input of -1V
          will slow down the movement to the half.
        shove (gate):
          While this gate input is logical 1, an extra force of 1 N is applied to the
          mass pointing downwards. You can change that force with shoveforce.
        shoveforce (cv):
          This is the force being applied to the mass while shove is active
        reset (trigger):
          Resets the whole system to its start position.
        startvelocity (cv):
          Sets the velocity the mass has which starts of a reset is triggered
        startposition (cv):
          Sets the position the spring has which starts of a reset is triggered
        velocity (cv):
          Outputs the current velocity of the mass
        position (cv):
          Output the current length of the string. If the string goes upwards (which is
          possible with certain modulations), this can be negative.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    mass: str | None = Field(
        default=None,
        serialization_alias="mass",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "m"},
    )
    gravity: str | None = Field(
        default=None,
        serialization_alias="gravity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "g"},
    )
    springforce: str | None = Field(
        default=None,
        serialization_alias="springforce",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "f"},
    )
    flowresistance: str | None = Field(
        default=None,
        serialization_alias="flowresistance",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "fr"},
    )
    friction: str | None = Field(
        default=None,
        serialization_alias="friction",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "fi"},
    )
    speed: str | None = Field(
        default=None,
        serialization_alias="speed",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sp"},
    )
    shove: str | None = Field(
        default=None,
        serialization_alias="shove",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sh"},
    )
    shoveforce: str | None = Field(
        default=None,
        serialization_alias="shoveforce",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sf"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "r"},
    )
    startvelocity: str | None = Field(
        default=None,
        serialization_alias="startvelocity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sv"},
    )
    startposition: str | None = Field(
        default=None,
        serialization_alias="startposition",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "spo"},
    )
    velocity: str | None = Field(
        default=None,
        serialization_alias="velocity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "v"},
    )
    position: str | None = Field(
        default=None,
        serialization_alias="position",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "p"},
    )


class Transient(DroidCircuit):
    """ Transient generator

    Args:
        start (cv):
          Start value of the transient
        end (cv):
          Target value of the transient
        duration (cv):
          Duration: if the clock input is used, it is in clock ticks. Otherwise it is in
          seconds. A negative duration will be treated as zero. And a zero duration will
          make the output always be at end level.
        loop (gate):
          If this is set to 1, the transient will start over again as soon as it reaches
          the end.
        pingpong (gate):
          If this set to 1, the transient will start moving backwards towards the start
          when it has reached end. It will swing back and forth, in fact looping
          infinitely.
        freeze (gate):
          while this is set to 1, the transient it frozen at its current position.
        reset (trigger):
          A trigger here will immediately set the transient back to its start value.
        clock (trigger):
          If you patch a clock here, the duration will be set in terms of clock ticks,
          not of seconds. This needs to be a steady clock in order to get predictable
          results.
        output (cv):
          Here comes the current value of the transient.
        phase (cv):
          This output reflects the current phase of the transient. It behaves as if
          start would be 0 and end would be 1.
        endoftransient (gate):
          When loop and pingpong is off, this output goes to 1 when the transient has
          reached the end – and stays there. In loop mode just a short trigger is sent.
          In pingpong mode that trigger is not sent when the transient has reach the
          end-value, but when it is back at start (i.e. after one full cycle).
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    start: str | None = Field(
        default=None,
        serialization_alias="start",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "st"},
    )
    end: str | None = Field(
        default=None,
        serialization_alias="end",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "e"},
    )
    duration: str | None = Field(
        default=None,
        serialization_alias="duration",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "d"},
    )
    loop: str | None = Field(
        default=None,
        serialization_alias="loop",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "lo"},
    )
    pingpong: str | None = Field(
        default=None,
        serialization_alias="pingpong",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pp"},
    )
    freeze: str | None = Field(
        default=None,
        serialization_alias="freeze",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "f"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "o"},
    )
    phase: str | None = Field(
        default=None,
        serialization_alias="phase",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p"},
    )
    endoftransient: str | None = Field(
        default=None,
        serialization_alias="endoftransient",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "et"},
    )

