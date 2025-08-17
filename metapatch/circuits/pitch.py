"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Calibrator(DroidCircuit):
    """ VCO Calibrator

    Args:
        input (voltperoctave):
          Patch your V/Oct pitch input here.
        nudgeup (trigger):
          A trigger here (most likely a button press) will modify the tuning of the
          currently played note (as read by input) upwards by one cent (or by
          nudgeamount if that is used.
        nudgedown (trigger):
          A trigger here will modify the tuning of the currently played note down.
        clearhere (trigger):
          A trigger here sets the correction of the currently played note to zero. This
          might affect a range of up to two octaves.
        nudgeamount (cv):
          Changes the amount each button press detunes. A value of one would mean one
          semitone, so the default value of 0.01 corresponds to one cent (1/100) of a
          semitone.
        tune0 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune1 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune2 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune3 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune4 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune5 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune6 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune7 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tune8 (cv):
          Explicit tuning of the octaves 0 through 8 – if you do not want to nudge
          manually. tune0 sets the tuning for the input pitch of 0 V, tune1 for 1 V and
          so on. A value of 1 means a tune adjustment of one semitone – which is 100
          cent. The maximum detuning is ± 1 Octave ( at a value of ± 12).
        tunelowtail (cv):
          Tuning adaption for the negative voltage range. A value of 1 means an upwards
          tuning of one semitone per octave, -1 likewise downwards.
        tunehightail (cv):
          Tuning adaption for voltages > 8 V. A value of 1 means an upwards tuning of
          one semitone per octave, -1 likewise downwards.
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
        output (voltperoctave):
          The calibrated pitch goes out here.
        ledup (fraction):
          When nudgeup is mapped to a button (which is most likely), map this output to
          the according LED and it will indicate whenever it's currently adjusting the
          output pitch upwards.
        leddown (fraction):
          This is the LED for nudgedown, which indicates downwards adjustment.
        correction (cv):
          This output gives you information about the current amout of pitch correction.
          It is positive if the pitch is corrected upwards, else negative. It is scaled
          in semitones, so a value of 0.2 means a 20% of a semitone, which is the same
          is 20 cents.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 224

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i"},
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
    clearhere: str | None = Field(
        default=None,
        serialization_alias="clearhere",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ch"},
    )
    nudgeamount: str | None = Field(
        default=None,
        serialization_alias="nudgeamount",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "na"},
    )
    tune0: str | None = Field(
        default=None,
        serialization_alias="tune0",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t0"},
    )
    tune1: str | None = Field(
        default=None,
        serialization_alias="tune1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t1"},
    )
    tune2: str | None = Field(
        default=None,
        serialization_alias="tune2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t2"},
    )
    tune3: str | None = Field(
        default=None,
        serialization_alias="tune3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t3"},
    )
    tune4: str | None = Field(
        default=None,
        serialization_alias="tune4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t4"},
    )
    tune5: str | None = Field(
        default=None,
        serialization_alias="tune5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t5"},
    )
    tune6: str | None = Field(
        default=None,
        serialization_alias="tune6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t6"},
    )
    tune7: str | None = Field(
        default=None,
        serialization_alias="tune7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t7"},
    )
    tune8: str | None = Field(
        default=None,
        serialization_alias="tune8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t8"},
    )
    tunelowtail: str | None = Field(
        default=None,
        serialization_alias="tunelowtail",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "tl"},
    )
    tunehightail: str | None = Field(
        default=None,
        serialization_alias="tunehightail",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "th"},
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
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o"},
    )
    ledup: str | None = Field(
        default=None,
        serialization_alias="ledup",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lu"},
    )
    leddown: str | None = Field(
        default=None,
        serialization_alias="leddown",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ld"},
    )
    correction: str | None = Field(
        default=None,
        serialization_alias="correction",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c"},
    )


class Chord(DroidCircuit):
    """ Chord generator

    Args:
        pitch (voltperoctave):
          This sets the minimum pitch of the lowest note of the chord.
        spread (voltperoctave):
          Selects the range between the lowest and highest note of the chord measured in
          1V/oct, while a spread of 0 means that all chord notes are within one octave,
          a spread of 1 V means that the notes are spread out over two octaves and so
          on.
        inversion (integer):
          Selects the inversion of the chord. 1 means that the root note should be the
          lowest note, 2 will make the second selected note the lowest note, 3 the 3 and
          4 the 4. The default, however, is 0 and doesn't fix the inversion. Rather that
          inversion is chosen that creates the chord closest to the input pitch.
        trigger (trigger):
          This jack is optional. If you patch it, the Chord generator just reads a new
          input pitch when it receives a trigger.
        root (integer):
          Set the root note here. 0 means C, 1 means C♯, 2 means D and so on. If you
          multiply the value of an input like I1 with 120, then you can use a 1V/Oct
          input for selecting the root note via a sequencer, MIDI keyboard or the like.
          Also then you are compatible with the ROOT CV input of the Sinfonion.   0C 1C♯
          2D 3D♯ 4E 5F 6F♯ 7G 8G♯ 9A 10A♯ 11B 12C
        degree (integer):
          Set the musical scale. This is a number from 0 to 107. Below are the first 12
          and most important scales. You find a list of all 108 scales on page 107.
          0lyd – Lydian major scale (it has a ♯ 4) 1maj – Normal major scale (ionian)
          2X^7 – Mixolydian (dominant seven chords) 3sus – mixolydian with 3/4 swapped
          4alt – Altered scale 5hm^5 – Harmonic minor scale from the 5 6dor – Dorian
          minor (minor with ♯ 13) 7min – Natural minor (aeolian) 8hm – Harmonic minor (♭
          6 but ♯ 7) 9phr – Phrygian minor scale (with ♭ 9) 10dim – Diminished scale
          (whole/half tone) 11aug – Augmented scale (just whole tones)   Note:
          Alltogether there are 108 scales. Please see page 107 for a complete list
        select1 (gate):
          Gate input for selecting the root note as being an allowed interval. When you
          want to create a playing interface for live operation you can patch the output
          of a toggle button (made with the circuit [button]) here.  Note: When all
          select and selectfill inputs are 0, automatically all seven scale notes are
          selected, i.e. select1 ... select13 will be set to one.
        select3 (gate):
          Gate input for selecting the 3.
        select5 (gate):
          Gate input for selecting the 5.
        select7 (gate):
          Gate input for selecting the 7.
        select9 (gate):
          Gate input for selecting the 9 (which is the same as the 2).
        select11 (gate):
          Gate input for selecting the 11 (which is the same as the 4).
        select13 (gate):
          Gate input for selecting the 13 (which is the same as the 6).
        selectfill1 (gate):
          Selects the alternative 9 (i.e. the 9 that is not in the scale.
        selectfill2 (gate):
          Selects the alternative 3 (i.e. the 3 that is not in the scale).
        selectfill3 (gate):
          Selects the alternative 4 or 5. In most cases this is the diminished 5.
        selectfill4 (gate):
          Selects the alternative 13 (i.e. the 13 that is not in the scale).
        selectfill5 (gate):
          Selects the alternative 7 (i.e. the 7 that is not in the scale).
        harmonicshift (integer):
          This input can reduce harmonic complexity by disabling some of the scale or
          non-scale notes. It is an idea first found in the Sinfonion and also provided
          by the circuit sinfonionlink.  harmonicshift is staged after the select...
          inputs and further filters out (disables) notes based on their relation to the
          current scale. This means that first the 12 select... inputs select a subset
          of the 12 possible notes. After that harmonicshift can reduce this set further
          (it will never add notes).  If harmonicshift is not zero, depending on its
          value some or more of the scale notes are disabled, even if they would be
          allowed by select....  Or in other words: the harmonic material is reduced.
          You also can use negative values. These create rather strange sounds by
          removing the simple chord functions instead of the complex ones first.  Here
          are the possible values:   0off – all selected notes are allowed 1disable all
          fill notes (non-scale notes) 2disable fills and 11þ 3disable fills, 11þand 13þ
          4disable fills, 11þ, 13þand 9 5disable fills, 11þ, 13þ, 9 and 7 6disable
          fills, 11þ, 13þ, 9, 7 and 3 7disable fills, 11þ, 13þ, 9, 7, 3 and 5 -1disable
          the root note -2disable the root note and the 5 -3disable root, 3, 5 -4disable
          root, 3, 5, 7 -5disable root, 3, 5, 7, 9 -6disable root, 3, 5, 7, 9 and 13þ
          -7disable all scale notes (fill notes untouched)
        noteshift (integer):
          Shifts the resulting output note(s) by this number of scale notes up or down
          (if negative). So the output note still is part of the scale but may be a note
          that is none of the selected ones. The maximum shift range is limited to -24 …
          +24.
        selectnoteshift (integer):
          Shifts the output note by this number of selected scale notes up or down (if
          negative). If you use noteshift at the same time, first selectnoteshift is
          applied, then noteshift. The maximum shift range is limited to -24 … +24.
        tuningmode (gate):
          While this is 1, the circuit will output the value set by tuningpitch instead
          of the actual pitch. This is ment to be a help for tuning your VCOs.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        transpose (voltperoctave):
          This value is being added to the output pitch when not in tuning mode. It can
          be used for musical transposition or adding a vibrato.
        output1 (voltperoctave):
          1 ... 4 pitch output
        output2 (voltperoctave):
          1 ... 4 pitch output
        output3 (voltperoctave):
          1 ... 4 pitch output
        output4 (voltperoctave):
          1 ... 4 pitch output
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 136

    pitch: str | None = Field(
        default=None,
        serialization_alias="pitch",
        json_schema_extra={"essential": 1, "type": "voltperoctave", "shortname": "p"},
    )
    spread: str | None = Field(
        default=None,
        serialization_alias="spread",
        json_schema_extra={"essential": 1, "type": "voltperoctave", "shortname": "s"},
    )
    inversion: str | None = Field(
        default=None,
        serialization_alias="inversion",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "iv"},
    )
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t"},
    )
    root: str | None = Field(
        default=None,
        serialization_alias="root",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ro"},
    )
    degree: str | None = Field(
        default=None,
        serialization_alias="degree",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "dg"},
    )
    select1: str | None = Field(
        default=None,
        serialization_alias="select1",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s1"},
    )
    select3: str | None = Field(
        default=None,
        serialization_alias="select3",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s3"},
    )
    select5: str | None = Field(
        default=None,
        serialization_alias="select5",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s5"},
    )
    select7: str | None = Field(
        default=None,
        serialization_alias="select7",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s7"},
    )
    select9: str | None = Field(
        default=None,
        serialization_alias="select9",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s9"},
    )
    select11: str | None = Field(
        default=None,
        serialization_alias="select11",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s11"},
    )
    select13: str | None = Field(
        default=None,
        serialization_alias="select13",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s13"},
    )
    selectfill1: str | None = Field(
        default=None,
        serialization_alias="selectfill1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf1"},
    )
    selectfill2: str | None = Field(
        default=None,
        serialization_alias="selectfill2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf2"},
    )
    selectfill3: str | None = Field(
        default=None,
        serialization_alias="selectfill3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf3"},
    )
    selectfill4: str | None = Field(
        default=None,
        serialization_alias="selectfill4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf4"},
    )
    selectfill5: str | None = Field(
        default=None,
        serialization_alias="selectfill5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf5"},
    )
    harmonicshift: str | None = Field(
        default=None,
        serialization_alias="harmonicshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "has"},
    )
    noteshift: str | None = Field(
        default=None,
        serialization_alias="noteshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "nos"},
    )
    selectnoteshift: str | None = Field(
        default=None,
        serialization_alias="selectnoteshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sns"},
    )
    tuningmode: str | None = Field(
        default=None,
        serialization_alias="tuningmode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "tm"},
    )
    tuningpitch: str | None = Field(
        default=None,
        serialization_alias="tuningpitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tp"},
    )
    transpose: str | None = Field(
        default=None,
        serialization_alias="transpose",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tr"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o3"},
    )
    output4: str | None = Field(
        default=None,
        serialization_alias="output4",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o4"},
    )


class Detune(DroidCircuit):
    """ Detune multiple voices in a most disharmonic way

    Args:
        input1 (cv):

        input2 (cv):

        input3 (cv):

        input4 (cv):

        input5 (cv):

        input6 (cv):

        input7 (cv):

        input8 (cv):

        detune (cv):

        tuningmode (gate):
          While this is 1, the circuit will output the value set by tuningpitch instead
          of the actual pitch. This is ment to be a help for tuning your VCOs.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        output1 (cv):

        output2 (cv):

        output3 (cv):

        output4 (cv):

        output5 (cv):

        output6 (cv):

        output7 (cv):

        output8 (cv):

        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    input1: str | None = Field(
        default=None,
        serialization_alias="input1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i1"},
    )
    input2: str | None = Field(
        default=None,
        serialization_alias="input2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i2"},
    )
    input3: str | None = Field(
        default=None,
        serialization_alias="input3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i3"},
    )
    input4: str | None = Field(
        default=None,
        serialization_alias="input4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i4"},
    )
    input5: str | None = Field(
        default=None,
        serialization_alias="input5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "i5"},
    )
    input6: str | None = Field(
        default=None,
        serialization_alias="input6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "i6"},
    )
    input7: str | None = Field(
        default=None,
        serialization_alias="input7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "i7"},
    )
    input8: str | None = Field(
        default=None,
        serialization_alias="input8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "i8"},
    )
    detune: str | None = Field(
        default=None,
        serialization_alias="detune",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "d"},
    )
    tuningmode: str | None = Field(
        default=None,
        serialization_alias="tuningmode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "tm"},
    )
    tuningpitch: str | None = Field(
        default=None,
        serialization_alias="tuningpitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tp"},
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


class Fold(DroidCircuit):
    """ CV folder – keep (pitch) CV within certain bounds

    Args:
        input (cv):
          Input CV to be folded.
        foldby (cv):
          Amount to be added or substracted from the input CV if it is not within the
          allowed range. This CV must be positive. If it is negative or zero, no folding
          will be done.
        minimum (cv):
          Lower bound of the allowed range. If unpatched, no lower bound will be
          applied.
        maximum (cv):
          Upper bound of the allowed range. If unpatched, no upper bound will be
          applied.
        output (cv):
          Folded output voltage
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    foldby: str | None = Field(
        default=None,
        serialization_alias="foldby",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "f"},
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
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Minifonion(DroidCircuit):
    """ Musical quantizer

    Args:
        input (voltperoctave):
          Patch the unquantized input voltage here
        trigger (trigger):
          This jack is optional. If you patch it, the Minifonion will work in triggered
          mode. Here the output pitch is always frozen until the next trigger happens.
        bypass (gate):
          If you set this gate input to 1 then quantization is bypassed and the input
          voltage is directly copied to the output.
        root (integer):
          Set the root note here. 0 means C, 1 means C♯, 2 means D and so on. If you
          multiply the value of an input like I1 with 120, then you can use a 1V/Oct
          input for selecting the root note via a sequencer, MIDI keyboard or the like.
          Also then you are compatible with the ROOT CV input of the Sinfonion.   0C 1C♯
          2D 3D♯ 4E 5F 6F♯ 7G 8G♯ 9A 10A♯ 11B 12C
        degree (integer):
          Set the musical scale. This is a number from 0 to 107. Below are the first 12
          and most important scales. You find a list of all 108 scales on page 107.
          0lyd – Lydian major scale (it has a ♯ 4) 1maj – Normal major scale (ionian)
          2X^7 – Mixolydian (dominant seven chords) 3sus – mixolydian with 3/4 swapped
          4alt – Altered scale 5hm^5 – Harmonic minor scale from the 5 6dor – Dorian
          minor (minor with ♯ 13) 7min – Natural minor (aeolian) 8hm – Harmonic minor (♭
          6 but ♯ 7) 9phr – Phrygian minor scale (with ♭ 9) 10dim – Diminished scale
          (whole/half tone) 11aug – Augmented scale (just whole tones)   Note:
          Alltogether there are 108 scales. Please see page 107 for a complete list
        select1 (gate):
          Gate input for selecting the root note as being an allowed interval. When you
          want to create a playing interface for live operation you can patch the output
          of a toggle button (made with the circuit [button]) here.  Note: When all
          select and selectfill inputs are 0, automatically all seven scale notes are
          selected, i.e. select1 ... select13 will be set to one.
        select3 (gate):
          Gate input for selecting the 3.
        select5 (gate):
          Gate input for selecting the 5.
        select7 (gate):
          Gate input for selecting the 7.
        select9 (gate):
          Gate input for selecting the 9 (which is the same as the 2).
        select11 (gate):
          Gate input for selecting the 11 (which is the same as the 4).
        select13 (gate):
          Gate input for selecting the 13 (which is the same as the 6).
        selectfill1 (gate):
          Selects the alternative 9 (i.e. the 9 that is not in the scale.
        selectfill2 (gate):
          Selects the alternative 3 (i.e. the 3 that is not in the scale).
        selectfill3 (gate):
          Selects the alternative 4 or 5. In most cases this is the diminished 5.
        selectfill4 (gate):
          Selects the alternative 13 (i.e. the 13 that is not in the scale).
        selectfill5 (gate):
          Selects the alternative 7 (i.e. the 7 that is not in the scale).
        harmonicshift (integer):
          This input can reduce harmonic complexity by disabling some of the scale or
          non-scale notes. It is an idea first found in the Sinfonion and also provided
          by the circuit sinfonionlink.  harmonicshift is staged after the select...
          inputs and further filters out (disables) notes based on their relation to the
          current scale. This means that first the 12 select... inputs select a subset
          of the 12 possible notes. After that harmonicshift can reduce this set further
          (it will never add notes).  If harmonicshift is not zero, depending on its
          value some or more of the scale notes are disabled, even if they would be
          allowed by select....  Or in other words: the harmonic material is reduced.
          You also can use negative values. These create rather strange sounds by
          removing the simple chord functions instead of the complex ones first.  Here
          are the possible values:   0off – all selected notes are allowed 1disable all
          fill notes (non-scale notes) 2disable fills and 11þ 3disable fills, 11þand 13þ
          4disable fills, 11þ, 13þand 9 5disable fills, 11þ, 13þ, 9 and 7 6disable
          fills, 11þ, 13þ, 9, 7 and 3 7disable fills, 11þ, 13þ, 9, 7, 3 and 5 -1disable
          the root note -2disable the root note and the 5 -3disable root, 3, 5 -4disable
          root, 3, 5, 7 -5disable root, 3, 5, 7, 9 -6disable root, 3, 5, 7, 9 and 13þ
          -7disable all scale notes (fill notes untouched)
        noteshift (integer):
          Shifts the resulting output note(s) by this number of scale notes up or down
          (if negative). So the output note still is part of the scale but may be a note
          that is none of the selected ones. The maximum shift range is limited to -24 …
          +24.
        selectnoteshift (integer):
          Shifts the output note by this number of selected scale notes up or down (if
          negative). If you use noteshift at the same time, first selectnoteshift is
          applied, then noteshift. The maximum shift range is limited to -24 … +24.
        tuningmode (gate):
          While this is 1, the circuit will output the value set by tuningpitch instead
          of the actual pitch. This is ment to be a help for tuning your VCOs.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        transpose (voltperoctave):
          This value is being added to the output pitch when not in tuning mode. It can
          be used for musical transposition or adding a vibrato.
        output (voltperoctave):
          Here comes your quantized output voltage
        notechange (trigger):
          Whenever the quantization changes to a new note a trigger with the duration
          10 ms is output here. No trigger is output in bypass mode.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 112

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i"},
    )
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "t"},
    )
    bypass: str | None = Field(
        default=None,
        serialization_alias="bypass",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b"},
    )
    root: str | None = Field(
        default=None,
        serialization_alias="root",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ro"},
    )
    degree: str | None = Field(
        default=None,
        serialization_alias="degree",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "dg"},
    )
    select1: str | None = Field(
        default=None,
        serialization_alias="select1",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s1"},
    )
    select3: str | None = Field(
        default=None,
        serialization_alias="select3",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s3"},
    )
    select5: str | None = Field(
        default=None,
        serialization_alias="select5",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s5"},
    )
    select7: str | None = Field(
        default=None,
        serialization_alias="select7",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s7"},
    )
    select9: str | None = Field(
        default=None,
        serialization_alias="select9",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s9"},
    )
    select11: str | None = Field(
        default=None,
        serialization_alias="select11",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s11"},
    )
    select13: str | None = Field(
        default=None,
        serialization_alias="select13",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "s13"},
    )
    selectfill1: str | None = Field(
        default=None,
        serialization_alias="selectfill1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf1"},
    )
    selectfill2: str | None = Field(
        default=None,
        serialization_alias="selectfill2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf2"},
    )
    selectfill3: str | None = Field(
        default=None,
        serialization_alias="selectfill3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf3"},
    )
    selectfill4: str | None = Field(
        default=None,
        serialization_alias="selectfill4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf4"},
    )
    selectfill5: str | None = Field(
        default=None,
        serialization_alias="selectfill5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "sf5"},
    )
    harmonicshift: str | None = Field(
        default=None,
        serialization_alias="harmonicshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "has"},
    )
    noteshift: str | None = Field(
        default=None,
        serialization_alias="noteshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "nos"},
    )
    selectnoteshift: str | None = Field(
        default=None,
        serialization_alias="selectnoteshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sns"},
    )
    tuningmode: str | None = Field(
        default=None,
        serialization_alias="tuningmode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "tm"},
    )
    tuningpitch: str | None = Field(
        default=None,
        serialization_alias="tuningpitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tp"},
    )
    transpose: str | None = Field(
        default=None,
        serialization_alias="transpose",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tr"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o"},
    )
    notechange: str | None = Field(
        default=None,
        serialization_alias="notechange",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "n"},
    )


class Octave(DroidCircuit):
    """ Multi-VCO octave animator

    Args:
        input (voltperoctave):
          The general pitch information on a 1 V / octave base to be used for the three
          VCOs.
        spread (stepped):
          The amount of octave spread between output1 and output3. At a value of 1.0 the
          spread is four octaves.
        detune (fraction):
          The amount of linear detune of VCO 2 and 3. This is not on a 1 V / octave base
          but corresponds to an absolute frequency difference in Hertz. The exact
          frequency difference cannot be set here, since that depends on how you have
          tuned your VCOs. But the rule is the following: If input is a 0 V and detune
          is 1.0, the detune is by four semitones. And for an input of 1 V (one octave
          higher) it is just two semitones, because that results in the same frequency
          difference. For 2 V (two octaves up) it ist just one semitone and for 3 V half
          a semitone (and so on). Best thing is to simply try out and listen!
        fifths (gate):
          Set this to 1 or on if you want to include perfect fifths as intermediate
          steps.
        output1 (voltperoctave):
          Outputs for the 1 V / octave of the three VCOs. output1 is an exact copy of
          input so you could omit that and rather patch VCO 1 to the original pitch CV.
        output2 (voltperoctave):
          Outputs for the 1 V / octave of the three VCOs. output1 is an exact copy of
          input so you could omit that and rather patch VCO 1 to the original pitch CV.
        output3 (voltperoctave):
          Outputs for the 1 V / octave of the three VCOs. output1 is an exact copy of
          input so you could omit that and rather patch VCO 1 to the original pitch CV.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i"},
    )
    spread: str | None = Field(
        default=None,
        serialization_alias="spread",
        json_schema_extra={"essential": 2, "type": "stepped", "shortname": "s"},
    )
    detune: str | None = Field(
        default=None,
        serialization_alias="detune",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "d"},
    )
    fifths: str | None = Field(
        default=None,
        serialization_alias="fifths",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "f"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o3"},
    )


class Sinfonionlink(DroidCircuit):
    """ Sync harmonic state from Sinfonion

    Args:
        root (integer):
          The current root note as an integer number. C = 0, C♯ = 1, D = 2 and so on.
        degree (integer):
          The current scale (the Sinfonion uses the word degree for this). This is an
          integer number. If find a list of all available scales on page 107.
        transpose (voltperoctave):
          The current global transposition of the Sinfonion. This is in 1V/Oct, so you
          can add it to your pitch whereever you output one.
        chaoticdetune (cv):
          The current value of the chaotic detune. You can feed this into the detune
          input of the circuit detune.
        harmonicshift (integer):
          Harmonic shift is a feature of the Sinfonion that allows to reduce harmonic
          complexity via CV (or the builtin pots POT1 or POT2). The idea is that the
          more you rise the CV, the less complex scale notes are allowed.  This output
          gives you access to the current setting of harmonic shift of the Sinfonion. It
          is an integer number between -7 and 7. You can directly feed it into the
          harmonicshift input of circuits like minifonion, chord, arpeggio or
          motoquencer. Harmonic shift is explained in detail in the manual chapter of
          minifonion.
        linkstate (gate):
          Outputs 1 if the link to the Sinfonion is up and active, otherwise 0.
        clock (trigger):
          Gives you a copy of the Sinfonion's clock input
        reset (trigger):
          Outputs a trigger whenever in Song mode the Sinfonion forwards to the first
          bar of the song.
        step (trigger):
          Outputs a trigger for every step of a song.
        beat (trigger):
          Outputs a trigger for every beat (subdivision of a step).
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    root: str | None = Field(
        default=None,
        serialization_alias="root",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ro"},
    )
    degree: str | None = Field(
        default=None,
        serialization_alias="degree",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "dg"},
    )
    transpose: str | None = Field(
        default=None,
        serialization_alias="transpose",
        json_schema_extra={"essential": 1, "type": "voltperoctave", "shortname": "tr"},
    )
    chaoticdetune: str | None = Field(
        default=None,
        serialization_alias="chaoticdetune",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ch"},
    )
    harmonicshift: str | None = Field(
        default=None,
        serialization_alias="harmonicshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "has"},
    )
    linkstate: str | None = Field(
        default=None,
        serialization_alias="linkstate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ls"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    step: str | None = Field(
        default=None,
        serialization_alias="step",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "s"},
    )
    beat: str | None = Field(
        default=None,
        serialization_alias="beat",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "b"},
    )


class Superjust(DroidCircuit):
    """ Perfect intonation of up to eight voices

    Args:
        input1 (voltperoctave):
          1 ... 8 pitch input
        input2 (voltperoctave):
          1 ... 8 pitch input
        input3 (voltperoctave):
          1 ... 8 pitch input
        input4 (voltperoctave):
          1 ... 8 pitch input
        input5 (voltperoctave):
          1 ... 8 pitch input
        input6 (voltperoctave):
          1 ... 8 pitch input
        input7 (voltperoctave):
          1 ... 8 pitch input
        input8 (voltperoctave):
          1 ... 8 pitch input
        tuningmode (gate):
          While this is 1, all outputs output the value set by tuningpitch. This is for
          tuning all outputs. Since perfect tuning is crucial for perfect intonation,
          this is quite useful.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        bypass (gate):
          While this is 1, all inputs are passed through to the outputs without changes.
        transpose (voltperoctave):
          This value is being added to all outputs, but not in tuning or bypass mode. It
          can e.g. be used for making a vibrato on a chord.
        output1 (voltperoctave):
          1 ... 8 pitch output
        output2 (voltperoctave):
          1 ... 8 pitch output
        output3 (voltperoctave):
          1 ... 8 pitch output
        output4 (voltperoctave):
          1 ... 8 pitch output
        output5 (voltperoctave):
          1 ... 8 pitch output
        output6 (voltperoctave):
          1 ... 8 pitch output
        output7 (voltperoctave):
          1 ... 8 pitch output
        output8 (voltperoctave):
          1 ... 8 pitch output
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 64

    input1: str | None = Field(
        default=None,
        serialization_alias="input1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i1"},
    )
    input2: str | None = Field(
        default=None,
        serialization_alias="input2",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i2"},
    )
    input3: str | None = Field(
        default=None,
        serialization_alias="input3",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i3"},
    )
    input4: str | None = Field(
        default=None,
        serialization_alias="input4",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "i4"},
    )
    input5: str | None = Field(
        default=None,
        serialization_alias="input5",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "i5"},
    )
    input6: str | None = Field(
        default=None,
        serialization_alias="input6",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "i6"},
    )
    input7: str | None = Field(
        default=None,
        serialization_alias="input7",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "i7"},
    )
    input8: str | None = Field(
        default=None,
        serialization_alias="input8",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "i8"},
    )
    tuningmode: str | None = Field(
        default=None,
        serialization_alias="tuningmode",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "tm"},
    )
    tuningpitch: str | None = Field(
        default=None,
        serialization_alias="tuningpitch",
        json_schema_extra={"essential": 1, "type": "voltperoctave", "shortname": "tp"},
    )
    bypass: str | None = Field(
        default=None,
        serialization_alias="bypass",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b"},
    )
    transpose: str | None = Field(
        default=None,
        serialization_alias="transpose",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "tr"},
    )
    output1: str | None = Field(
        default=None,
        serialization_alias="output1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o1"},
    )
    output2: str | None = Field(
        default=None,
        serialization_alias="output2",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o2"},
    )
    output3: str | None = Field(
        default=None,
        serialization_alias="output3",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o3"},
    )
    output4: str | None = Field(
        default=None,
        serialization_alias="output4",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "o4"},
    )
    output5: str | None = Field(
        default=None,
        serialization_alias="output5",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "o5"},
    )
    output6: str | None = Field(
        default=None,
        serialization_alias="output6",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "o6"},
    )
    output7: str | None = Field(
        default=None,
        serialization_alias="output7",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "o7"},
    )
    output8: str | None = Field(
        default=None,
        serialization_alias="output8",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "o8"},
    )


class Vcotuner(DroidCircuit):
    """ measure frequency and tuning of a VCO

    Args:
        tuningnote (integer):
          You can either tune to a specific note, like C or A or whatever you like. In
          this case set tuningnote to a number from 0 to 11, where 0 is C, 1 is C#, 2 is
          D and so on. Or you set it to -1 (which is the default) to tune to the nearest
          semitone.
        concertpitch (cv):
          Set the frequency of the concert pitch here, which is the frequency of A1.
          Most commonly this is 440 Hz, so 440 is the default value of this parameter.
        basepitch (voltperoctave):
          This output sets the reference for the pitch output. It is the voltage for the
          note C0. With analog synths it is common – but not neccessary – that the C
          notes correspond to integer voltage numbers.
        smooth (fraction):
          When measuring the input frequency, a slight smoothing is applied (like a low
          pass filter). It evens out some possible jitter that you might have. You can
          adjust this filter here. Per default smoothing is just subtle. Beware: smooth
          = 1 smoothes strong, so the frequency measurement needs some time to get
          accurate.
        precision (cv):
          This parameter defines the precision for the input frequency to be in tune. It
          is set in cents, where 100 cent correspond to one semitone. If you set the
          precision too low, it is very hard to tune correctly. If you set it too high,
          your tuning is not very precise.
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
        hz (cv):
          Outputs the current input frequency. If you no signal is found, the output is
          0.
        ledflat (fraction):
          Patch this to a LED to show if and how much the input frequency is flat (too
          low). This value ranges from 0.2 to 1.0 if the input frequency is flat and
          goes straight to 0 otherwise. If you use select, this output only works while
          the circuit is selected.
        ledsharp (fraction):
          Patch this to a LED to show if and how much the input frequency is sharp (too
          high). This value ranges from 0.2 to 1.0 if the input frequency is sharp and
          goes straight to 0 otherwise. If you use select, this output only works while
          the circuit is selected.
        ledintune (gate):
          Outputs 1 if the input frequency is “in tune”. Here the precision input is
          applied. If you use select, this output only works while the circuit is
          selected.
        intune (gate):
          Outputs 1 if the input frequency is “in tune”. Here the precision input is
          applied. This output also while while the circuit is not selected. You can use
          it in situations where you want to process this information by some other
          circuit rather than just displaying it.
        tuning (bipolar):
          Outputs the current tuning deviation of the input measured in 1V/octave.
        cents (bipolar):
          Outputs the current tuning deviation in cents, where 100 cents correspond to
          one semitone.
        pitch (voltperoctave):
          Outputs the current pitch of the input frequency in terms of 1V/octave. Here
          the basepitch is applied. You can patch this output to the pitch input of a
          second VCO to have that follow the pitch of the measured VCO.
        referencepitch (voltperoctave):
          Here you get the pitch of the reference tone the tuner currently “locked in”
          into. It is either the nearest semitone or the note selected by tuningnote in
          the nearest octave.
        vcofound (gate):
          This output is 1 whenever a valid input signal is found on the tuning input
          I1.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = None

    tuningnote: str | None = Field(
        default=None,
        serialization_alias="tuningnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "tn"},
    )
    concertpitch: str | None = Field(
        default=None,
        serialization_alias="concertpitch",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "cp"},
    )
    basepitch: str | None = Field(
        default=None,
        serialization_alias="basepitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "b"},
    )
    smooth: str | None = Field(
        default=None,
        serialization_alias="smooth",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "sm"},
    )
    precision: str | None = Field(
        default=None,
        serialization_alias="precision",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pc"},
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
    hz: str | None = Field(
        default=None,
        serialization_alias="hz",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": ""},
    )
    ledflat: str | None = Field(
        default=None,
        serialization_alias="ledflat",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "lf"},
    )
    ledsharp: str | None = Field(
        default=None,
        serialization_alias="ledsharp",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ls"},
    )
    ledintune: str | None = Field(
        default=None,
        serialization_alias="ledintune",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "lt"},
    )
    intune: str | None = Field(
        default=None,
        serialization_alias="intune",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "it"},
    )
    tuning: str | None = Field(
        default=None,
        serialization_alias="tuning",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "t"},
    )
    cents: str | None = Field(
        default=None,
        serialization_alias="cents",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "c"},
    )
    pitch: str | None = Field(
        default=None,
        serialization_alias="pitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p"},
    )
    referencepitch: str | None = Field(
        default=None,
        serialization_alias="referencepitch",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "rp"},
    )
    vcofound: str | None = Field(
        default=None,
        serialization_alias="vcofound",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "vf"},
    )

