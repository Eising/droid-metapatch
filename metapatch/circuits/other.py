"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Droid(DroidCircuit):
    """ General DROID controls

    Args:
        ledbrightness (cv):
          Let's you dim all of the 24 LEDs of the master and the G8. This is mainly for
          those who think they are too bright. But since this parameter can be CV-
          controlled, you could of course also do funny things with it. Beware: if you
          set this to zero, the LEDs will be completely dark. This also includes
          possible error messages.
        maxslope1 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope2 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope3 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope4 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope5 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope6 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope7 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        maxslope8 (cv):
          Sets a threshold for a voltage change between two samples until the internal
          logic of the outputs assumes that this step is intentional and should not be
          smoothed out. A typical case where you do not want smoothing is the pitch
          output of a sequencer.  The default value is 0.25. A value of 0.0 turns off
          smoothing altogether since the slightest voltage change is considered an
          intentional jump.
        lpfilter1 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter2 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter3 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter4 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter5 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter6 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter7 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        lpfilter8 (fraction):
          Configures a digital low pass filter on the output in order to smooth out
          digital noise resulting from the 's main loop. This loop is running somewhere
          between 3 and 6 kHz – depending on the number of circuits you use.  Per
          default this filter is set to 0.25 – which means a mild filtering – thus still
          allowing fast and snappy envelopes and other rapidly changing signals while
          filtering away most of the digital artefacts.  If you use an output for a slow
          envelope that is combined with an audio path in a way that you hear digital
          artifacts then increase that value. This is e.g. the case if you modulate a
          VCA that in turn modulates a very low pitched audio wave with very few
          harmonics (such as a sine or triangle wave).  The maximum value of 1.0 leads
          to a very strong filtering – i.e. removing all fast transients. Snappy
          envelopes will be smoothed out heavily. Square wave LFOs will be converted
          into lower level almost sine waves.
        m4faderspeed (fraction):
          Set the force / speed of the motor faders. Faster speeds need more electrical
          power and might wear off the faders faster. Too slow speeds might lead to poor
          operation. This value goes from 0.0 (slowest possible speed) to 1.0 (maximum
          speed). If you don't use this parameter, some reasonable default is used that
          depends on the firmware of the M4 module.
        statusdump (trigger):
          A trigger here does the same as a double “click” on the master's button: it
          creates a status dump file on the SD card. This trigger allows you automated
          control with a precise timing. Each dump needs a couple of milli seconds to
          write to the SD card. So better do not spam this input with a high frequency
          of triggers.
        m4notchpower (fraction):
          Set the force feedback power of the M4 motor fader units when they operate
          with virtual notches. The range is from 0 (minimum notch power) to 1 (maximum
          notch power). Note: 0 does not turn the notches off, there is still some
          minimal feedback. If you don't use this parameter, the notch force feedback
          operates at some default power, which is dependent on the M4 firmware version.
        calibrate (trigger):
          Immediately enter the calibration procedure, that's contained in the
          maintainance menu (only MASTER). Skips the menu. After calibration is done,
          resets.
        startcontrollerupgrade (trigger):
          Immediately starts the firmware upgrade procedure for controllers like M4 and
          E4. After one succesfull upgrade resets the master.
        startx7upgrade (trigger):
          Immediately starts the X7 firmware upgrade procedure (which is located at
          position 8 of the maintainance menu). After the upgrade of the X7 resets the
          master.
        clear (trigger):
          A trigger here sends a trigger to the clear input of all circuits that support
          this. That brings the state of those circuits to their start state. Circuits
          that have presets do keep those presets untouched. Just the current state is
          affected.  That trigger is not sent to circuits whose clear input is patched.
          Note: Just that part of the state is affected that is saved to the SD card.
          For example the algoquencer does not reset to the first step, it just clears
          it's current pattern.
        clearall (trigger):
          A trigger here sends a trigger to the clearall input of all circuits that
          support this. That's like a global factory reset for all of your circuits.
          Everything is set to its starting state, including all presets of those
          circuits.  That trigger is not sent to circuits whose clearall input is
          patched.  Note: Just that part of the state is affected that is saved to the
          SD card. For example the algoquencer does not reset to the first step, it just
          clears it's current pattern.
        uislowdown (gate):
          Since blue-6 circuits that are ment to build a user interface are executed at
          just one eighth of the normal speed. They are just executed every eighth loop
          cycle. This saves considerable loop time and speeds up all the other more
          musical circuits.  This breaks the rule that all circuits are executed in the
          order of their appearance in the patch, however. So if your patch really
          depends on that and your buttons, buttongroups and pots seem to behave weird,
          try switching off the UI optimization by setting this parameter to 0.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 72

    ledbrightness: str | None = Field(
        default=None,
        serialization_alias="ledbrightness",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "l"},
    )
    maxslope1: str | None = Field(
        default=None,
        serialization_alias="maxslope1",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s1"},
    )
    maxslope2: str | None = Field(
        default=None,
        serialization_alias="maxslope2",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s2"},
    )
    maxslope3: str | None = Field(
        default=None,
        serialization_alias="maxslope3",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s3"},
    )
    maxslope4: str | None = Field(
        default=None,
        serialization_alias="maxslope4",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s4"},
    )
    maxslope5: str | None = Field(
        default=None,
        serialization_alias="maxslope5",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s5"},
    )
    maxslope6: str | None = Field(
        default=None,
        serialization_alias="maxslope6",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s6"},
    )
    maxslope7: str | None = Field(
        default=None,
        serialization_alias="maxslope7",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s7"},
    )
    maxslope8: str | None = Field(
        default=None,
        serialization_alias="maxslope8",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s8"},
    )
    lpfilter1: str | None = Field(
        default=None,
        serialization_alias="lpfilter1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf1"},
    )
    lpfilter2: str | None = Field(
        default=None,
        serialization_alias="lpfilter2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf2"},
    )
    lpfilter3: str | None = Field(
        default=None,
        serialization_alias="lpfilter3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf3"},
    )
    lpfilter4: str | None = Field(
        default=None,
        serialization_alias="lpfilter4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf4"},
    )
    lpfilter5: str | None = Field(
        default=None,
        serialization_alias="lpfilter5",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf5"},
    )
    lpfilter6: str | None = Field(
        default=None,
        serialization_alias="lpfilter6",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf6"},
    )
    lpfilter7: str | None = Field(
        default=None,
        serialization_alias="lpfilter7",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf7"},
    )
    lpfilter8: str | None = Field(
        default=None,
        serialization_alias="lpfilter8",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf8"},
    )
    m4faderspeed: str | None = Field(
        default=None,
        serialization_alias="m4faderspeed",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "m4f"},
    )
    statusdump: str | None = Field(
        default=None,
        serialization_alias="statusdump",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sd"},
    )
    m4notchpower: str | None = Field(
        default=None,
        serialization_alias="m4notchpower",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "m4n"},
    )
    calibrate: str | None = Field(
        default=None,
        serialization_alias="calibrate",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c"},
    )
    startcontrollerupgrade: str | None = Field(
        default=None,
        serialization_alias="startcontrollerupgrade",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "u"},
    )
    startx7upgrade: str | None = Field(
        default=None,
        serialization_alias="startx7upgrade",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "x7"},
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
    uislowdown: str | None = Field(
        default=None,
        serialization_alias="uislowdown",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "us"},
    )


class Outputcalibrator(DroidCircuit):
    """ Tune the calibration of your CV outputs

    Args:
        output (integer):
          Select the output to calibrate. This is a number from 1 to 8.
        referencepoint (integer):
          For each output, two voltages need to be adjusted: 0 V and 5 V. Select either
          0 for 0 V or 1 for 5 V.
        nudgeup (trigger):
          Increase the currently selected output voltage by one minimal step, to match
          the reference voltage.
        nudgedown (trigger):
          Decrease the currently selected output voltage by one minimal step, to match
          the reference voltage.
        save (trigger):
          A trigger here saves the changed calibration values to the internal flash of
          the master and the the SD card.
        cancel (trigger):
          A trigger here restores the previous calibration values from the internal
          flash.
        loaddefaults (trigger):
          A trigger here loads the default calibration values, which are not very
          precise, but a good starting point if you got totally lost.
        dirty (gate):
          Outputs 1 if the current calibration has been changed and needs to be saved.
        calibration (cv):
          Shows the difference between the current calibration of the selected output
          and reference voltage and its default calibration value.
        uncalibrated (fraction):
          Shows you the percentage of uncalibrated outputs. If all eight outputs are
          calibrated (differ from the default calibration value) this outputs 0.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 40

    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "o"},
    )
    referencepoint: str | None = Field(
        default=None,
        serialization_alias="referencepoint",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "r"},
    )
    nudgeup: str | None = Field(
        default=None,
        serialization_alias="nudgeup",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "nu"},
    )
    nudgedown: str | None = Field(
        default=None,
        serialization_alias="nudgedown",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "nd"},
    )
    save: str | None = Field(
        default=None,
        serialization_alias="save",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "sv"},
    )
    cancel: str | None = Field(
        default=None,
        serialization_alias="cancel",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c"},
    )
    loaddefaults: str | None = Field(
        default=None,
        serialization_alias="loaddefaults",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ld"},
    )
    dirty: str | None = Field(
        default=None,
        serialization_alias="dirty",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "d"},
    )
    calibration: str | None = Field(
        default=None,
        serialization_alias="calibration",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "cl"},
    )
    uncalibrated: str | None = Field(
        default=None,
        serialization_alias="uncalibrated",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u"},
    )

