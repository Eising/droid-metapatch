"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Algoquencer(DroidCircuit):
    """ Algorithmic sequencer

    Args:
        clock (trigger):
          Clock input. This is mandatory. For each clock pulse the sequencer is advanced
          by one step.
        reset (trigger):
          Reset input. A trigger here switches back to step 1.
        button1 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button2 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button3 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button4 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button5 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button6 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button7 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button8 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button9 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button10 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button11 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button12 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button13 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button14 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button15 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        button16 (gate):
          1 ... 16 step button. Assign these buttons to buttons on your controllers.
        length (integer):
          Sets the length of the pattern. Note: if you use lengthbutton, this input is
          ignored as soon as the length button has been used for the first time. If you
          have assigned at least one button, the default value of length is the number
          of buttons you have assigned. Otherwise it defaults to 16. The maximum length
          is 64. Any larger number will be truncated to 64.
        pattern (integer):
          Selects a pattern of pseudo random values. If you set dejavu to 1, all
          “random” decision are deterministic and repeat again and again. If you do not
          like these choices, you can choose a different pattern, just by setting this
          input to any integer number you like. The default pattern is 0. If you patch a
          pot here, simply multiply it by the number of different patterns you want to
          select, e.g. pattern = P1.1 * 10. This will allow you to select one of the
          pattern 0, 1, ... 10.
          You can use pattern in combination with nextpattern, prevpattern and reroll.
          These three inputs create an offset to the chosen pattern. E.g. if you set
          pattern = 5 and send one trigger to nextpattern, the actually used pattern is
          6.

        nextpattern (trigger):
          Switches forward to the next pseudo random pattern.
        prevpattern (trigger):
          Switches back to the previous pseudo random pattern.
        reroll (trigger):
          Select one of the pseudo random patterns completely by random.
        clearpage (trigger):
          A trigger here unselects all step buttons in the currently active page
          (normal, alternate, accent).
        pitchlow (cv):
          This set a lower voltage boundary for the pitch output for notes that are
          randomized.
        pitchhigh (cv):
          This set an upper voltage boundary for the pitch output for notes that are
          randomized.
        pitchresolution (integer):
          If this is non-zero, it make the pitch output adopt that number of possible
          discrete values. E.g. if you set it to 2, only the values set by pitchlow and
          pitchhigh are possible. A value of 3 will allow an additional value in the
          middle, and so on.
        gatelength (cv):
          The gate length in input clock cycles. A value of 0.5 (5 V) thus means half a
          clock cycle. A steady input clock is needed for this to work. Please note that
          if the gate length is >= 1.0, two succeeding notes will get a steady gate,
          which essentially means legato.  When playing rolls, i.e. more than one beat
          per step, the gate length is divided by the number of rolls. That way the
          gates get shorter and even at a gatelength close to 1.0 the gates are still
          audible and do not merge together.
        lengthbutton (gate):
          Map this to a button like B1.1. While you press and hold this button the
          sequencer switches to change length mode. While in this mode a press of one of
          the step buttons will change the length of the pattern. Also while in this
          mode the LEDs of the step buttons will show the current length. If you do not
          like to hold the button but switch it on and off, you can create a toggle
          button with [button] and send its output here.
        repeats (integer):
          Usually one bar has the length of one pattern. Setting this to 2 will consider
          one bar as a run of two times through the pattern. So if you have 8 buttons
          and bars = 2, one bar will be 16 steps, where the 1 and 9 step are set by
          button1, 2 and 10 by button2 and so on.  Why should that be useful? Well – the
          difference shows up when you use fills, or branches or work with the alternate
          pattern. These three algorithms work based on bars. And repeats = 2 makes one
          bar have 16 steps, even if you just have eight buttons.
        alternaterepeats (integer):
          If you are use using repeats and alternatebars / alternatebutton at the same
          time, with this input you can specify a different value for repeats when it
          comes to selecting the alternate button page.  Assume you have eight buttons
          and repeats = 2 and alternatebars = 2. Then Algoquencer will play two times
          your 8-step pattern normally and two times alternated (since two times the 8
          steps form one bar). This results in a form of A A B B.  If you want your form
          rather to be A B A B, set alternaterepeats = 1. This way, when it comes to
          alteration, the length of one bar is just normal length (8 steps here).
        branches (integer):
          Enables the branching feature (sometimes also called fractal sequencing. When
          branches = 1, then every second bar will be using other random values – giving
          a sequence of the bars A B.  With branches = 2 you get a sequence of the form
          A B A C.  A value of 3 creates an even longer sequence that repeats itself
          after eight bars: A B A C A B A D.  Note: this only takes effect when you set
          dejavu >0. The largest effect is when it is set to 1. And the you need to use
          either variation or set activity to a value greater than 0.5. Because
          otherwise Algoquencer will strictly play the gates that you've set with your
          buttons and then every bar will be the same, of course.
        mutebutton (trigger):
          Wire this to a button like B1.2. When you press the button once, all triggers
          are muted. Pressing again unmutes them. So this behaves like a toggle [button]
          in itself. You probably want to wire muteled to the LED in that button, e.g.
          L1.2. It show the mute state. The mute button works together with the unmute
          button (see below). Note: even if you use the select jack in order to overlay
          your buttons with several algoquencers, the mutebutton will always be active.
          The idea is to always have direct access to this button.
        unmutebutton (trigger):
          A trigger to this jack resets the mute button exactly at the beginning of the
          next bar. While waiting for that to happen, the output unmuteled will blink.
          Wire this to the LED in the button. Note: even if you use the select jack in
          order to overlay your buttons with several algoquencers, the mutebutton will
          always be active. The idea is to always have direct access to this button.
        accentbutton (gate):
          While this input is high you are in accent editing mode. This is very similar
          to the mode where you set the length. But now for each step you edit whether
          this step is outputting an accent when triggered. You might want to use a
          toggle button for this function, so you can operate without holding down the
          button all the time.
        alternatebutton (gate):
          If this input is high, you are in alternate editing mode. Every Algoquencer
          has an alternate set of steps. Each step that is currenty activated toggles
          the state of the normal step, but only for each even bar. This allows to
          introduce variations of the pattern that occur every second bar.
        alternatebars (integer):
          With this input you can change the influence of the alternatebutton. Per
          default the pattern alternation is done every second bar. You can change this
          to any number you like with this input. Values less than 1 will be considered
          as one – which means that every bar is alternated.
        accentlow (cv):
          This value is output at accent when a note without an accent is being
          triggered or when no note is triggered at all.
        accenthigh (cv):
          This value is output at accent while a note with an accent is triggered. The
          value will be kept for the full time of the clock cycle.
        activity (bipolar):
          This is the most important parameter and  you will probably wire it to a pot
          like P1.1. The activity controls, how “busy” the sequencer is playing, or in
          other words how often a step gets an active gate (und thus a changing output
          pitch).  Let's first assume that variation is set to 0.0 (which is the
          default). Then at a value of 0.5 (or pot at 12'clock) Algoquencer will exactly
          play that pattern that you have set with the step buttons. Turning the knob
          CCW will remove more and more beats from the pattern until it is completely
          silent at a value of 0.0 (or pot fully CCW). But if you turn up the knob above
          the middle position then more and more additional beats will be placed into
          you pattern in a random way until – at 1.0 – a trigger will happen at every
          beat.  Note: If you do not use step buttons, this parameter behaves slightly
          different: A value of 0.5 then means an activity of 50%, which means that
          exactly the half of the steps will get an event. This is different from a
          situation where you have defined buttons but all are deselected. In that case
          0.5 means that exactly the number of beats of your pattern are being played,
          which is zero in that case.
        variation (fraction):
          The variation controls how strictly Algoquencer will stick to the pattern that
          you have set with your step buttons. You probably want to wire this to a knob.
          A value of 0.0 (or the knob fully CCW) will allow no variations. Your pattern
          will be played exactly as it is. If the activity goes beyond 0.5, additional
          beats will be placed, of course. And these are random.  If you increase the
          variation, more and more beats of your pattern are being replaced with other
          beats – while keeping the total number of beats the same. If you set variation
          to 1.0 (or the pot fully CW) then your pattern is completely ignored except
          for the actual number of beats it contains.
        dejavu (fraction):
          The dejavu parameter controls what random should mean. If dejavu = 0.0, then
          all random decisions are completely chaotic – and every time a decision is
          taken the dice are being rolled again.  At dejavu = 1.0 on the other hand –
          once a random decision has been taken for a certain step in a certain bar, it
          will stay always the same from now on. This will lead to repeating exactly the
          pattern bars over and over again. We sometimes call this random to be
          “deterministic”.  Any position in between will choose some of the steps as
          chaotic random and some of the steps as deterministic.
        morphs (fraction):
          This parameter will introduce changes in formerly taken random decisions from
          time to time. If you set it above zero, at every start of a bar some of the
          deterministic random decisions will be remade. Setting morphs = 1 will
          essentially disable dejavu, since all decisions are redone every bar anyway
          then.
          If you know the Turing Machine: In principle that has the same idea, but
          Algoquencer has a few improvements:
          * The number of random changes is exactly controlled by the setting. At each
            specific setting of morphs the same number of changes will be done at each
            bar.
          * Changes only appear at the beginning of each bar. If you use branches, they
            will appear whenever you sequence is over.
          * Small settings will introduce just one morph each 64 step.

        offbeats (bipolar):
          Whenever random beats are being placed then this setting controlls whether
          downbeats or offbeats should be preferred. At at setting of 0.5 there will be
          no difference. If you increase the value then more and more offbeats will
          appear. Offbeats are steps with an even number, like 2, 4, 6 and so on. Value
          smaller than 0.5 will prefer downbeats.  Offbeats sound more “complex” and
          downbeats more simple or “down to earth”.
        distribution (bipolar):
          This is very similar to offbeats, but this time you decide whether beats
          should be placed rather in the first half of the bar or in the second half.
        fills (fraction):
          When this parameter is set above 0.0, additional beats will be placed in order
          to make the beat more “active”. This happens at musically useful times
          controlled by fillorder (see below). The additional beats within the bar are
          placed in a way that prefers the end of the bar. If there are already too many
          beats in the bar then the fill will remove or change some instead.
        fillorder (integer):
          This integer number controls how fills are being placed:  0every bar 1every
          second bar 2small fill in bar 2, big fill in bar 4 3tiny fill in bar 2 and 6,
          medium fill in bar 4, big fill in bar 8
        rolls (fraction):
          This parameter controls if drum rolls (or ratchets as you might call it) are
          being created. At 0.0 no rolls are being created. At 1.0 every beat will be
          converted into a roll. Rolls always happen before the actual beat, they lead
          to it. If you using this feature for snare rolls you might want to use the
          output rollvelocity for controlling the snare volume.
        rollcount (integer):
          Number of additional beats for playing the roll. Setting rollcount = 0 would
          disable rolls. All these beats are distributed in the clock tick before the
          beat the roll is leading to. The first beat of the roll is exactly one tick
          before that beat – or more if you increase rollsteps.
        rollsteps (integer):
          Length of the roll in clock ticks (steps). The total number of additional
          beats is thus rollcount × rollsteps
        rollstartvelo (cv):
          Rolls can be played with an increasing velocity. This first beat starts with
          the velocity set with this parameter. Then every beat gets a bit louder until
          the last beat is played with velocity 1.0. The velocity for rolls is output at
          the jack rollvelocity.
        pitch1 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch2 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch3 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch4 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch5 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch6 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch7 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch8 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch9 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch10 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch11 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch12 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch13 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch14 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch15 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
        pitch16 (cv):
          You can use these inputs, if you want the pitches of the pitch output play a
          certain melody. That way the Algoquencer behaves like a normal melody
          sequencer – but all the algorithmic parameters will be applied. For example
          variation will also be applied to these notes. Note: If length is larger than
          16, these pitch inputs will be cycled through, so step 17 uses pitch1, step 18
          uses pitch2 and so on.
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
        trigger (trigger):
          Here comes the trigger output. Patch this to the trigger input of your drum or
          synth voice.
        gate (gate):
          The gate output is alternative to the trigger and has a variable length. It is
          useful when Algoquencer is used for creating melodies. Patch the gate input of
          an envelope or something similar here.
        pitch (stepped):
          Outputs the (pseudo-)random voltage (unquantized) at each step with an active
          gate. This honors all the settings that control the randomness and variation,
          like dejavu, variation, fills and branches.
        accent (cv):
          Whenever a beat with an accent is being played, the value set by accenthigh is
          sent here, otherwise accentlow. If you are wiring this to one of the jacks of
          the G8 expander then that will output just 0V and 5V of course.
        led1 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led2 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led3 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led4 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led5 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led6 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led7 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led8 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led9 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led10 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led11 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led12 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led13 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led14 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led15 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        led16 (stepped):
          1 ... 16 LEDs of the step buttons. Assign these to the LEDs in the step
          buttons.
        barled1 (gate):
          Patch these output to some LEDs in order to show you the current bar in the
          sequence.
        barled2 (gate):
          Patch these output to some LEDs in order to show you the current bar in the
          sequence.
        barled3 (gate):
          Patch these output to some LEDs in order to show you the current bar in the
          sequence.
        barled4 (gate):
          Patch these output to some LEDs in order to show you the current bar in the
          sequence.
        rollvelocity (cv):
          If you enable rolls, then the velocity of the roll beats will be output here.
          For normal beats this will always be 1.0.
        startofbar (trigger):
          At the beginning of every bar a trigger is output here.
        muteled (gate):
          Wire this to the LED in your mute button. It will then be lit while the voice
          is muted.
        unmuteled (gate):
          Wire this to the LED in your unmute button (if used). It will blink while the
          unmute is waiting for the start of the next bar.
        morphled (gate):
          This output will get a trigger every time a morph happens. It is intended to
          be wired to an LED.
        fillsled (gate):
          This output will get a trigger every time a fill beat is being played. Wire
          this to some LED if you like.
        branch (integer):
          This output will output the current branch number, e.g. 1, 2, 3 and so on. If
          you do not use branches then it is always 1.
        lengthoutput (integer):
          Outputs the currently selected length. This is useful if you are using the
          lengthbutton for interactively changing the length of the pattern and want to
          share that setting with other circuits.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 880

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
    button1: str | None = Field(
        default=None,
        serialization_alias="button1",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b1"},
    )
    button2: str | None = Field(
        default=None,
        serialization_alias="button2",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b2"},
    )
    button3: str | None = Field(
        default=None,
        serialization_alias="button3",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b3"},
    )
    button4: str | None = Field(
        default=None,
        serialization_alias="button4",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b4"},
    )
    button5: str | None = Field(
        default=None,
        serialization_alias="button5",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b5"},
    )
    button6: str | None = Field(
        default=None,
        serialization_alias="button6",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b6"},
    )
    button7: str | None = Field(
        default=None,
        serialization_alias="button7",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b7"},
    )
    button8: str | None = Field(
        default=None,
        serialization_alias="button8",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "b8"},
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
    length: str | None = Field(
        default=None,
        serialization_alias="length",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "l"},
    )
    pattern: str | None = Field(
        default=None,
        serialization_alias="pattern",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pt"},
    )
    nextpattern: str | None = Field(
        default=None,
        serialization_alias="nextpattern",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "np"},
    )
    prevpattern: str | None = Field(
        default=None,
        serialization_alias="prevpattern",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pp"},
    )
    reroll: str | None = Field(
        default=None,
        serialization_alias="reroll",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "rr"},
    )
    clearpage: str | None = Field(
        default=None,
        serialization_alias="clearpage",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cp"},
    )
    pitchlow: str | None = Field(
        default=None,
        serialization_alias="pitchlow",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pl"},
    )
    pitchhigh: str | None = Field(
        default=None,
        serialization_alias="pitchhigh",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ph"},
    )
    pitchresolution: str | None = Field(
        default=None,
        serialization_alias="pitchresolution",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pre"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "gl"},
    )
    lengthbutton: str | None = Field(
        default=None,
        serialization_alias="lengthbutton",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lb"},
    )
    repeats: str | None = Field(
        default=None,
        serialization_alias="repeats",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rp"},
    )
    alternaterepeats: str | None = Field(
        default=None,
        serialization_alias="alternaterepeats",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "arp"},
    )
    branches: str | None = Field(
        default=None,
        serialization_alias="branches",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "bs"},
    )
    mutebutton: str | None = Field(
        default=None,
        serialization_alias="mutebutton",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "mb"},
    )
    unmutebutton: str | None = Field(
        default=None,
        serialization_alias="unmutebutton",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ub"},
    )
    accentbutton: str | None = Field(
        default=None,
        serialization_alias="accentbutton",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ab"},
    )
    alternatebutton: str | None = Field(
        default=None,
        serialization_alias="alternatebutton",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "alb"},
    )
    alternatebars: str | None = Field(
        default=None,
        serialization_alias="alternatebars",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "aba"},
    )
    accentlow: str | None = Field(
        default=None,
        serialization_alias="accentlow",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "al"},
    )
    accenthigh: str | None = Field(
        default=None,
        serialization_alias="accenthigh",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ah"},
    )
    activity: str | None = Field(
        default=None,
        serialization_alias="activity",
        json_schema_extra={"essential": 1, "type": "bipolar", "shortname": "a"},
    )
    variation: str | None = Field(
        default=None,
        serialization_alias="variation",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "v"},
    )
    dejavu: str | None = Field(
        default=None,
        serialization_alias="dejavu",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "d"},
    )
    morphs: str | None = Field(
        default=None,
        serialization_alias="morphs",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "m"},
    )
    offbeats: str | None = Field(
        default=None,
        serialization_alias="offbeats",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "ob"},
    )
    distribution: str | None = Field(
        default=None,
        serialization_alias="distribution",
        json_schema_extra={"essential": 0, "type": "bipolar", "shortname": "di"},
    )
    fills: str | None = Field(
        default=None,
        serialization_alias="fills",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "f"},
    )
    fillorder: str | None = Field(
        default=None,
        serialization_alias="fillorder",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fo"},
    )
    rolls: str | None = Field(
        default=None,
        serialization_alias="rolls",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "rl"},
    )
    rollcount: str | None = Field(
        default=None,
        serialization_alias="rollcount",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rc"},
    )
    rollsteps: str | None = Field(
        default=None,
        serialization_alias="rollsteps",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rs"},
    )
    rollstartvelo: str | None = Field(
        default=None,
        serialization_alias="rollstartvelo",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rsv"},
    )
    pitch1: str | None = Field(
        default=None,
        serialization_alias="pitch1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p1"},
    )
    pitch2: str | None = Field(
        default=None,
        serialization_alias="pitch2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p2"},
    )
    pitch3: str | None = Field(
        default=None,
        serialization_alias="pitch3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p3"},
    )
    pitch4: str | None = Field(
        default=None,
        serialization_alias="pitch4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p4"},
    )
    pitch5: str | None = Field(
        default=None,
        serialization_alias="pitch5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p5"},
    )
    pitch6: str | None = Field(
        default=None,
        serialization_alias="pitch6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p6"},
    )
    pitch7: str | None = Field(
        default=None,
        serialization_alias="pitch7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p7"},
    )
    pitch8: str | None = Field(
        default=None,
        serialization_alias="pitch8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p8"},
    )
    pitch9: str | None = Field(
        default=None,
        serialization_alias="pitch9",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p9"},
    )
    pitch10: str | None = Field(
        default=None,
        serialization_alias="pitch10",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p10"},
    )
    pitch11: str | None = Field(
        default=None,
        serialization_alias="pitch11",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p11"},
    )
    pitch12: str | None = Field(
        default=None,
        serialization_alias="pitch12",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p12"},
    )
    pitch13: str | None = Field(
        default=None,
        serialization_alias="pitch13",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p13"},
    )
    pitch14: str | None = Field(
        default=None,
        serialization_alias="pitch14",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p14"},
    )
    pitch15: str | None = Field(
        default=None,
        serialization_alias="pitch15",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p15"},
    )
    pitch16: str | None = Field(
        default=None,
        serialization_alias="pitch16",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "p16"},
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
    trigger: str | None = Field(
        default=None,
        serialization_alias="trigger",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "t"},
    )
    gate: str | None = Field(
        default=None,
        serialization_alias="gate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g"},
    )
    pitch: str | None = Field(
        default=None,
        serialization_alias="pitch",
        json_schema_extra={"essential": 2, "type": "stepped", "shortname": "p"},
    )
    accent: str | None = Field(
        default=None,
        serialization_alias="accent",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "ac"},
    )
    led1: str | None = Field(
        default=None,
        serialization_alias="led1",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l1"},
    )
    led2: str | None = Field(
        default=None,
        serialization_alias="led2",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l2"},
    )
    led3: str | None = Field(
        default=None,
        serialization_alias="led3",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l3"},
    )
    led4: str | None = Field(
        default=None,
        serialization_alias="led4",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l4"},
    )
    led5: str | None = Field(
        default=None,
        serialization_alias="led5",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l5"},
    )
    led6: str | None = Field(
        default=None,
        serialization_alias="led6",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l6"},
    )
    led7: str | None = Field(
        default=None,
        serialization_alias="led7",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l7"},
    )
    led8: str | None = Field(
        default=None,
        serialization_alias="led8",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l8"},
    )
    led9: str | None = Field(
        default=None,
        serialization_alias="led9",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l9"},
    )
    led10: str | None = Field(
        default=None,
        serialization_alias="led10",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l10"},
    )
    led11: str | None = Field(
        default=None,
        serialization_alias="led11",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l11"},
    )
    led12: str | None = Field(
        default=None,
        serialization_alias="led12",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l12"},
    )
    led13: str | None = Field(
        default=None,
        serialization_alias="led13",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l13"},
    )
    led14: str | None = Field(
        default=None,
        serialization_alias="led14",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l14"},
    )
    led15: str | None = Field(
        default=None,
        serialization_alias="led15",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l15"},
    )
    led16: str | None = Field(
        default=None,
        serialization_alias="led16",
        json_schema_extra={"essential": 0, "type": "stepped", "shortname": "l16"},
    )
    barled1: str | None = Field(
        default=None,
        serialization_alias="barled1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bl1"},
    )
    barled2: str | None = Field(
        default=None,
        serialization_alias="barled2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bl2"},
    )
    barled3: str | None = Field(
        default=None,
        serialization_alias="barled3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bl3"},
    )
    barled4: str | None = Field(
        default=None,
        serialization_alias="barled4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bl4"},
    )
    rollvelocity: str | None = Field(
        default=None,
        serialization_alias="rollvelocity",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rv"},
    )
    startofbar: str | None = Field(
        default=None,
        serialization_alias="startofbar",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sb"},
    )
    muteled: str | None = Field(
        default=None,
        serialization_alias="muteled",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ml"},
    )
    unmuteled: str | None = Field(
        default=None,
        serialization_alias="unmuteled",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ul"},
    )
    morphled: str | None = Field(
        default=None,
        serialization_alias="morphled",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "mol"},
    )
    fillsled: str | None = Field(
        default=None,
        serialization_alias="fillsled",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "fl"},
    )
    branch: str | None = Field(
        default=None,
        serialization_alias="branch",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "br"},
    )
    lengthoutput: str | None = Field(
        default=None,
        serialization_alias="lengthoutput",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "lo"},
    )


class Arpeggio(DroidCircuit):
    """ Arpeggiator – pattern based melody generator

    Args:
        pitch (voltperoctave):
          Sets the base pitch of the arpeggio. The first note of the pattern will be the
          nearest selected note just above that pitch.
        range (voltperoctave):
          Selects the range between the lowest and highest note of the arpeggio. A range
          of 0 means that there is just one single note possible and the arpeggio will
          stick to that note. A value of 1 V (or 0.1) means that the arpeggio will run
          over one octave. The maximum allowed range is 0.8 (8 octaves). Higher values
          will be capped to that.
        clock (trigger):
          This input is vital: each trigger here make the arpeggio move forward by one
          step and adapt the pitch output. Without a clock the arpeggio will do nothing
          but stick to the same note all the time.
        reset (trigger):
          Resets the arpeggio to the first step of the current pattern.
        pattern (integer):
          Selects one of a list of arpeggio pattern. The following patterns are
          available:   0step forward through the allowed notes→ 1two steps forward, one
          step backward→ → ← 2double step forward, one step backward⇒ ← 3double step
          forward, double step backward, single step forward⇒ ⇐  → 4double step forward,
          single step forward, double step backward, single step forward⇒ → ⇐ → 5random
          single step forward or backward↔ 6random jump to any allowed (other) note⇕
        direction (gate):
          Sets the general direction in which the pattern moves. 0 means upwards and 1
          means downwards.
        pingpong (gate):
          If set to 1, the pattern will reverse its direction once it has reached the
          end of the range. Otherwise it restarts from the beginning. So enabling
          pingpong is a bit like a triangle wave, whereas otherwise it's more like a
          sawtooth.
        butterfly (gate):
          If set to 1, every second note in the range of selected notes will be
          mirrored. So for example you have selected the notes 1 - 10, the new order
          will be 1, 10, 2, 9, 3, 8, 4, 7, 5, 6
        drop (integer):
          Selects a scheme of skipping some of the allowed scale notes. Four different
          values are allowed:   0Do not skip any notes202 203 204 205 206 207 1Skip
          every second selected note202 193 204 195 206 197 2Skip every third selected
          note202 203 194 205 206 197 3Skip the 2 and 3 note of each group of three202
          193 194 205 196 197
        octaves (gate):
          When this is set to 1 or 2, each note will be followed by the same note one
          octave up (for 1) or down (for 2) respectively. These additional octave notes
          are in addition to the selected range.   0Don't play octaves 1Each note is
          followed by the same note one octave up 2Each note is followed by the same
          note one octave down
        startnote (integer):
          When startnote is set to non-zero, it will force the pattern to begin with a
          certain scale note regardless of the current note selection. 1 will select the
          first note of the scale (root), 2 the second and so on until 7, which selects
          the 7 as start note.  Using startnote effectively reduces the range of notes.
          Instead of the the full range of pitch … pitch + range a reduced range is
          played, since some of the lower notes are skipped, if the direction is
          upwards, and some of the upper notes, if the direction is downwards.  The
          start note is used in all situations where the pattern is reset to its
          beginning. This is after an external reset or if the pattern has reached the
          end of the range. Note: If you have set pingpong = 1, the pattern is never
          reset by itself, so startnote is just used after an external reset, here.
          Don't mess up the start note with the lowest note in the arpeggio. If want to
          control the lowest note, used pitch instead of startnote. Sometimes this has a
          similar effect, but not always.
        autoreset (integer):
          When autoreset a non-zero number, the arpeggio melody will be reset to the
          start after that number of clock ticks. For example if you set autoreset = 5,
          and the pattern would play 7 notes until it loops back to its start, after the
          5 step a restart is forced. That's also true if the pattern is shorter. If
          autoreset = 5 and the melody already loops after 3 steps, it is played once in
          full (3 steps) and once just the first 2 steps, since then the auto reset
          happens.  A trigger to reset makes autoreset set it's internal counter to 0.
          Autoreset gives you direct control over the rhythmic feel that your arpeggio
          melodies have.
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
          This is what it's all about: here comes the pitch CV for the current arpeggio
          note.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 144

    pitch: str | None = Field(
        default=None,
        serialization_alias="pitch",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "p"},
    )
    range: str | None = Field(
        default=None,
        serialization_alias="range",
        json_schema_extra={"essential": 1, "type": "voltperoctave", "shortname": "ra"},
    )
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
    pattern: str | None = Field(
        default=None,
        serialization_alias="pattern",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "pt"},
    )
    direction: str | None = Field(
        default=None,
        serialization_alias="direction",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "d"},
    )
    pingpong: str | None = Field(
        default=None,
        serialization_alias="pingpong",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "pp"},
    )
    butterfly: str | None = Field(
        default=None,
        serialization_alias="butterfly",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "by"},
    )
    drop: str | None = Field(
        default=None,
        serialization_alias="drop",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "dr"},
    )
    octaves: str | None = Field(
        default=None,
        serialization_alias="octaves",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "oc"},
    )
    startnote: str | None = Field(
        default=None,
        serialization_alias="startnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sn"},
    )
    autoreset: str | None = Field(
        default=None,
        serialization_alias="autoreset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ar"},
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


class Encoquencer(DroidCircuit):
    """ Performance sequencer using E4 encoders

    Args:
        zorder (integer):
          This parameter changes to order of the encoders in the sequence. The natural
          order (at the default value of zorder = 0) assignes the sequence steps to the
          encoders in their order of appearance in your controllers. The step counter
          moves downwards the four encoders of one E4, then jumps to the first encoder
          of the next E4 and so on. There are four different choices. The choices 2 and
          3 are for situations where you mount the master at the right of your
          controllers.   0sequence step moves downwards, E4 by E4 1sequence step moves
          left to right, row by row 2Like 0, but start with last E4 3right to left, row
          by row   The name zorder resembles the fact that if you draw the order of the
          encoders with a pen on a paper, the setting zorder = 1 looks like three times
          the letter Z.
        nume4s (integer):
          Define the number of E4 modules the sequencer should occupy if zorder is 1 or
          3. If you don't used this variable, the number is set to numfaders / 4. If you
          have eight E4 and want to create a sequencer with just the first row, set
          numfaders = 8 and zorder = 1 and nume4s = 8. For using the first two rows, do
          the same with numfaders = 16. By choosing a specific encoder to be the first,
          with firstfader, you can move this rectangle of encoders to a different
          position in your E4 matrix.
        ledpreview (gate):
          Set this to 1 if you want the inactive states (or possible settings) to be
          illuminated in the LED ring.
        firstfader (integer):
          First M4 fader of the sequencer (starting with 1). If you omit this, it starts
          at the first fader of your first M4.
        numfaders (integer):
          Number of faders to use for your sequencer. The typical numbers are 4, 8, 16
          and 32. 32 is the maximum (eight M4 units). If you omit this, all of your M4
          faders will be used.
        numsteps (integer):
          Number of steps your sequence consists of (at maximum). The number of steps
          can be greater than the number of faders. In that case use page for paging
          your faders so that you can edit all of the steps. Having the number of steps
          less than the faders, makes no sense – it's just a waste of faders. The
          maximum number of steps is 32.  If you don't set this parameter, the number of
          steps will be set to the number of faders.  Note: changing this setting
          dynamically can provoke various surprising behaviours. For example the number
          of pages (see parameter page) might be reduced. Or the end marker is forcibly
          moved around. If you want to change the length of the sequence via CV, better
          use endstep or autoreset.  Another note: Setting numsteps will not restrict
          the number of faders. If you set numsteps = 4 but have eight faders available,
          the circuit will use all these, even if faders 5, 6, 7 and 8 will be useless.
          You need to set numfaders = 4 in this situation.
        page (integer):
          Use this parameter, if you have less faders than steps. The first page is 0,
          not 1. For example if you have 4 faders but 16 steps, you can select between
          the four “pages” of four faders each, by settings bar to 0, 1, 2 or 3. The
          output of a buttongroup with one button per page is a good match for this
          parameter.
        clock (trigger):
          Patch an input clock here. If you want to use ratcheting, that clock needs to
          be stable and regular, because the sequencer needs to interpolate the clock
          and create evenly distributed new beats within two clock ticks. If you don't
          use ratching, you can use any rhythm you like here – may it be shuffled,
          euklidean, the output from another sequencer or whatever you like. Each clock
          tick will advance the sequence to the next step (or to the next repition of
          the current step).
        taptempo (trigger):
          If your clock is not steady but might be stopped and restarted, you should
          patch a steady clock here. This avoids problems with the computation of the
          gate length right after starting the clock. The tap tempo computation needs a
          series of at least two clock pulses so the gate length of the first step is
          wrong after the clock has stopped for a while.
        reset (trigger):
          A trigger here resets the sequencer to its start step. The next clock tick (or
          a tick that is roughly at the same time as the reset) will play step 1. Note:
          If there is a reset without a clock tick at the same time, the sequencer will
          go to “step 0”, which is a special state where it waits for the clock to
          advance to the first step. Without that fancy logic, a reset plus clock would
          skip step 1 and start with step 2.
        run (gate):
          If you set this input to 0, the sequencer will ignore all incoming clock
          ticks. It stops. The default of 1 is normal operation, where it runs. This
          input is a better way to temporarily stop the sequencer than to stop the
          clock. The reason: for computing the gate length and ratchets a steady input
          clock is needed. If you stop the clock, the next gate length and ratches right
          after the next start will have the wrong duration since at least two clock
          ticks are neccessary for computing its speed.  Note: This input is not a
          replacement for mute, since a muted sequencer leaves the clock running and
          advances steps. It just mutes the gate output.
        composemode (gate):
          Enabling “compose mode” makes it easier to find the right note in a step, when
          creating more complex melodies.  When composemode is set to 1, the sequencer
          stops clocking. Instead – every time you change the CV of a step, it
          immediately jumps to that step, outputs the changed CV and opens the gate for
          a short time, so you can listen to the changed note.
        mute (gate):
          If you set this to 1, the gate output of the sequencer is muted (will always
          be 0). Any changes of the CV output still happen.
        cvbase (cv):
          Here you set the voltage the sequencer will output if the CV fader is at the
          bottom position. The allowed range is -1 … 1 (which is the same as the range
          from -10 V to +10 V, if you output the CV directly to an output).
        cvrange (cv):
          CV range of the faders. So the resulting CV lies somewhere between cvbase and
          cvbase + cvrange. The CV range cannot be negative and is capped at 1. If you
          need a greater range, consider multiplying the output value of the cv output
          of the sequencer.
        invert (gate):
          Inverts the CV or pitch output. This is like mirroring the fader position. Now
          if the fader is up, the output is low and vice versa. In scale quantized mode,
          the melody still stays within the scale.
        quantize (integer):
          Switches on quantization in two levels. At 0, the faders run freely and output
          a continous CV.  At 1, the output is quantized to semitones, which is 1/12V
          steps. Also the faders will get artifical notches – one for each semitone.
          That is, unless your range is too large. The maximum number of notches with
          force feedback is 25, so if your range exceeds two octaves (0.2), the notches
          are turned off.  At 2, the output is quantized to the scale that root and
          degree define. Furthermore the individual scale notes can be switched on or
          off with the parameters select1, select3 and so on. Note: the root input does
          not select the lowest note of the CV range. That is still set with cvbase. It
          is just used for selecting the scale.  0no quantization 1quantize to semitones
          (1/12V steps) 2quantize to the scale set by root and degree
        cvnotches (integer):
          Usually the CVs of the steps are ment to be note pitches (when quantize is 1
          or 2), or just free CVs (quantize = 0). There is an alternative mode, however,
          that allows you to assign integer values like 0, 1, 2 and so on to each step.
          To do this set cvnotches to a value of 2 or greater. This defines the number
          of discrete values (and hence notches) for each step and put CVs of the
          sequence into notched mode. 1 makes no sense, of course, since in this “pitch
          bend mode” the faders would always return to the neutral position.  In notched
          mode the cv output does not output a pitch but a notch number starting from 0.
          cvbase, cvrange and quantize are ignored.  The maximum number of notches is
          127, but the haptic force feedback of the motor faders is disabled starting at
          26.
        shiftsteps (integer):
          Shifts all your steps by that number to the left (negative numbers shift to
          the right). So if shiftsteps is 1, right after a reset, the sequencer will not
          play step 1, but step 2. The shifting wraps around at the end of your
          sequence, so if you have 24 steps and shift is 1, the sequencer will play step
          1 instead of step 24.  Note: Other things like startstep, endstep, playmode,
          from and autoreset take place after shifting.
        startstep (integer):
          Sets the first step to be used.  This means that after a reset or when the
          sequencer comes to the end of the sequence, it will begin at this step.  There
          is also a way for settings start and end with buttons (see below at
          buttonmode). If you use the interactive mode, the startstep and endstep
          settings will be overridden. The are reactived if you clear everything.  Note:
          startstep and endstep take place after applying shiftsteps.
        endstep (integer):
          Sets the last of the steps to be played. The default is to play all steps.
          After playing the end step, the sequencer moves on to the start step at the
          next clock tick.  If startstep is equal to endstep, the sequence just consists
          of one single step.  Settings startstep larger then endstep is allowed and
          reverses the playing order.
        form (integer):
          This is an advanced feature that allows you to slice your steps into two or
          three parts and create musical song forms like AAAB or ABAC. Each of the parts
          A, B or C are then played according to the playmode.
          The form AAAB, for example, creates a 32 step form from just 16 steps, by
          playing the first 8 steps three times and then the second 8 steps once.
          The following forms are available:
          0A (forms are basically deactivated) 1AAAB 2AABB 3ABAC 4AAABAAAC 5AB 6AAB
          Notes:
          * The splitting of the steps into parts takes place after accounting for
            startstep and endstep.
          * Forms with A, B and C split the pattern into three parts. These parts can
            only be of equal size if the number of steps is dividable by 3, of course.
          * The pattern AB is really not the same as A, e.g when direction is set 1
            (reverse). In that case each of the parts is played backwards, but the parts
            themselves move forwards on your steps.

        direction (gate):
          Sets the general direction in which the sequencer moves through the steps. 0
          means forwards and 1 means backwards.
        pingpong (gate):
          If set to 1, the sequencer will change the direction every time it reaches the
          start or end of the sequence.
        pattern (integer):
          Selects one of a list of movement patterns. That way, the sequence steps are
          not played in linear order but in a more sophisticated movement.  Available
          pattern are:   0go step by step to the sequence (normal)→ 1two steps forward,
          one step backward→ → ← 2double step forward, one step backward⇒ ← 3double step
          forward, double step backward, single step forward⇒ ⇐  → 4double step forward,
          single step forward, double step backward, single step forward⇒ → ⇐ → 5random
          single step forward or backward↔ 6go forward by a small random number of
          steps→ × ?  7random jump to any allowed (other) note⇕
        repeatshift (integer):
          This is a number in the range -24 … +24. If you set this to non-zero, each
          repetition of a step shifts the played note by that many notes within the
          selected scale notes. This only has effect on steps where the number of
          repeats is greater than 1. Also it is only is applied when the quantize = 2.
        ratchetshift (integer):
          This is a number in the range -24 … +24. If you set this to non-zero, each
          ratchet of a step shifts the played note by that many notes within the
          selected scale notes. This only has effect on steps where the number of
          ratchets is greater than 1. Also it is only is applied when the quantize = 2.
          If you combine ratchetshift with repeatshift, both shifts are added together.
          And the ratchet shifting is reset for each repetition of the step.
        accumulatorrange (integer):
          Using this parameter enables the pitch accumulator. The value sets the maximum
          value the accumulator can get.  The maximum is 16. If you set this to 0, the
          fader mode for pitch randomization still is in the special mode where the
          upper four positions control the impact of the accumulator.  Please consult
          the manual of motoquencer for details on the pitch accumulator.
        constantlength (gate):
          This input enables a feature that (tries to) keep the actual length of the
          sequence constant. There are two levels. If constantlength = 1, every change
          in the repeats of a step is compensated by changing the repeats in the
          following steps. E.g. if you increase the number of repeats from 4 to 5 in
          step 3 (by moving the fader in the appropriate fader mode), the repeats in
          step 4 are reduced by 1. If they are already 1, step 5 is tried an so on,
          until it wrap around to step 1.  The second level is constantlength = 2. Here
          also the skip setting of steps is honored and modified in order to keep the
          length constant. A skipped step essentially has the length 0 (or 0 repeats).
          The componsation is now done not only when the repeats are changed but also
          when skip is switched on or off on a step.  All the compensation is only
          active with the range that is set with the start and end step.
        autoreset (integer):
          If set to non-zero, automatically issues a reset (just like a trigger to
          reset) every N clock ticks.
        metricsaver (gate):
          The Metric Saver ™ helps you to reliably come back to your original metric and
          time after playing around with all sorts of parameters that change the played
          number of steps in the sequence.  These are: startstep, endstep (also when
          changed interactively), form, direction, pingpong, pattern, autoreset and
          repeats and skips of individual steps. Therefore it counts the actual number
          of clock cycles since the last external reset (or system start). And when all
          of these features are deactivated, it snaps back the clock to the position it
          would have been by now if you never had played around with all the funny
          stuff.  That way, during a live performance, you can safely play around with
          all this polymetric and otherwise time disrupting stuff and as soon as you
          clean up your mess – voila: you are back on track and in sync with the rest of
          the “band”.  The metric saver is turned on by default. But you can disable it
          by setting the parameter to 0.
        fadermode (integer):
          Switches the current meaning of the motor faders. You probably want to connect
          the output of a buttongroup here. Here are the possible modes:  0pitch / CV
          1randomize CV 2gate propability 3repeats (up to 16) 4gate pattern 5ratchets
          (up to 8) 6gate 7skip
        buttonmode (integer):
          Switches the current meaning of the touch buttons below the faders. You
          probably want to connect the output of a buttongroup here. Here are the
          possible modes:  0gates 1start / end 2gate pattern 3skip
        holdcv (gate):
          This setting determines wether the CV output changes every time the sequencer
          moves to the next step or just when that step is active (a gate is being
          played). The latter is the default. But if you set this to 0, the CV values of
          steps without gates will also influence the output CV.  Note: regardless of
          this setting, the CV will never change inbetween. Any change of the CV faders,
          the cvbase and cvrange and so on will only take effect when the next step is
          played. This also ensures that repeats or ratchets are always in the same
          pitch.
        defaultcv (cv):
          Set the CV the steps should be set to on a trigger to clear. That value must
          be within the range set by cvbase and cvrange, or it will be truncated to that
          range.  If you have set cvnotches, however, the value is expected to be an
          integer in the range 0 ... cvnotches - 1.
        defaultgate (gate):
          Here you set to which state (on / off) the gates should be set on a trigger to
          clear.
        clearskips (trigger):
          A trigger here removes the “skip” setting from all steps.
        clearrepeats (trigger):
          A trigger here resets the number of repeats to 1 for each step.
        clearstartend (trigger):
          A trigger here clears the manual settings of the start and end step. So the
          sequence will be played in its full length (again) .
        gatelength (cv):
          The gate length in input clock cycles. A value of 0.5 thus means half a clock
          cycle. A steady input clock is needed for this to work. Please note that if
          the gate length is >= 1.0, two succeeding notes will get a steady gate, which
          essentially means legato.  If you don't use a steady clock, set this parameter
          to 0. This will output a minimal gate length of about 10 ms (basically just a
          trigger).
        keyboardmode (integer):
          This input sets how a keyboard, that is hooked to keyboardcv, and keyboardgate
          should be used for directly playing notes. You can set it to 0, 1 or 2.
          0ignore the keyboard inputs 1keyboard and sequencer play together, keyboard
          has precedence 2mute sequencer, just play keyboard
        keyboardcv (voltperoctave):
           The pitch input of a keyboard. This is used for playing along with the
          keyboardmode or recording with recordmode.
        keyboardgate (gate):
           The gate input of a keyboard. A positive gate enabled play along (see
          keyboardmode) and also recording, if recordmode is set accordingly.
        recordmode (integer):
           Use this input to record melodies played with a keyboard (namely keyboardcv
          and keyboardgate) into the sequencer. There are three possible settings:
          0don't record 1record, notes longer than one step will automatically tie steps
          via the gate pattern 2record, don't tie notes. Ignore the length of the input
          note
        recordsilence (gate):
          When this input is set to 1 while recording, silence will be recorded while
          keyboardgate is off. Otherwise you can just add notes to the sequence.
        copy (trigger):
          A trigger here copies the current page of the sequence to an internal
          clipboard. The clipboard is not part of any preset and is also not saved to
          the SD card. It can be used later for pasting it's data to another preset or
          another page of a sequence.
        paste (trigger):
          A trigger here copies the steps from the clipboard to the current page.
        pastefaders (trigger):
          This is like paste, but just the values of the faders of the current fadermode
          are copied.
        pastebuttons (trigger):
          This is like paste, but just the values of the faders of the current
          buttonmode are copied. Note: the button mode “start / end” is not supported by
          copy and paste.
        linktonext (gate):
          This settings allows you to create motoquencer tracks that have more than one
          CV or gate output for each step. If you set this to 1, the next motoquencer
          circuit in your patch will by synchronized to this one. This means that it
          always plays the same step number – including all fancy operating like
          shiftsteps, startstep, endstep, form, pattern and autoreset. All those inputs
          and also clock and reset are ignored by the next motoquencer.  The same holds
          for the “repeats” and “skip” setting of the steps.  fadermode and buttonmode
          are extended to the next motoquencers by adding 10 for each motoquencer to
          follow. So fadermode = 10 will show the CV of next motoquencer in the faders.
          fadermode = 11 the CV randomization of the next motoquencer. fadermode = 20
          show the CV of the third linked motoquencer and so on.  Don't set fadermode or
          buttonmode on the linked motoquencers. They will be ignored there.  Note: The
          linktonext setting cannot by dynamically changed. It needs to be fixed 0 or 1.
          You cannot use any button or internal cable or other methods to change it
          while the patch is running.
        luckychance (fraction):
          Sets tha chance for a step to be affected by the next “lucky” operation (see
          triggers below).
        luckyscope (integer):
          Determines which part of the sequence is affected by the “lucky” operations.
          Depending on this setting the following steps are affected:   0All steps
          between the current start and end step 1All steps 2All steps between start and
          end on the current page 3All steps on the current page
        luckyamount (fraction):
          Sets the amount of change that a “lucky” operation does to a step. The meaning
          depends on the operation. See the parameters below.
        luckycvbase (fraction):
          This parameter affects only the operation luckycvs and luckyfaders when the
          fader mode is set to 0. It adds a fixed amount of CV to the random result, so
          that lies in the range luckycvbase … (luckycvbase + luckyamount).
        luckyfaders (trigger):
          Moves the currently selected faders (according to fadermode) to new random
          positions. luckyamount sets the maximum value of the fader, where 1 allows the
          maximum.
        luckybuttons (trigger):
          Randomly toggles the currently selected buttons (according to buttonmode).
          luckyamount only has an effect when the gate patterns are selected, since
          here, four different values are possible. luckamount restricts them if it is
          lower than 1.
        luckycvs (trigger):
          Replaces the affected steps' CVs with a new random CVs. The lowest possible CV
          is cvbase. If luckyamount is 1, the highest possible CV is cvbase + cvrange,
          otherwise it is cvbase + luckyamount × cvrange.
        luckycvdrift (trigger):
          Modifies the affected steps' CV randomly up or down. They will stay in the CV
          range set by cvbase and cvrange. luckyamount controls the amount of change.
        luckyspread (trigger):
          First computes the average CV of all steps. Then changes the CV values of the
          affected steps such that their distance to the average increases or decreases.
          If luckyamount is greater than 0.5, the distance is increased. Otherwise it is
          decreased.
        luckyinvert (trigger):
          Inverts the CVs of the affected steps within the allowed CV range. luckyamount
          has no influence.
        luckyrandomizecv (trigger):
          Sets the “randomize CV” values of the affected steps to random values (yes,
          this is double randomization). The luckyamount sets the maximum randomization
          value that will be set.
        luckygates (trigger):
          Sets the gates of the affected steps randomly to on or off. The chance for on
          is determined by luckyamount. So with luckyamount = 0 you clear all gates and
          with luckyamount = 1 you set all gates.
        luckyskips (trigger):
          Sets the “skip this step” setting of the affected steps randomly to skip or
          normal. The chance for skip is determined by luckyamount.
        luckyties (trigger):
          Sets the “tie this step to the next” setting of the affected steps randomly to
          tie or normal. This is the same as setting the gate pattern to the upper most
          position. The chance for tie is determined by luckyamount.
        luckygatepattern (trigger):
          Randomizes the gate pattern of the selected steps (there are four different
          values: once, all, hold and tie). Use luckyamount to reduce that set.
        luckygateprob (trigger):
          Sets the “randomize gate” values of the affected steps to random values (yes,
          this is double randomization). The luckyamount sets the minimum randomization
          value that will be set (yes, this is inverted). So with luckyamount = 1 you
          disable randomization and make the gates play always. With luckymount = 0 you
          set the gate propability to the lowest possible value (still not 0).
        luckyrepeats (trigger):
          Randomly sets the number of repeats of the affected steps to something between
          1 and 16 (the maximum). The luckyamount determines the maximum repetition
          number, where 1 stands for a maximum of 16 repetitions.
        luckyratchets (trigger):
          Randomly sets the number of ratches of the affected steps to something between
          1 and 8 (the maximum). The luckyamount determines the maximum ratchet number,
          where 1 stands for a maximum of 8 ratchets.
        luckyshuffle (trigger):
          Randomly swaps all affected affected steps (their playing order) together will
          all their attributes. luckyamount has no influence.
        buttoncolor (cv):
          Set a user defined color for the gate buttons. This color is only used when
          buttonmode = 0. The main purpose of this option is to allow a separate color
          for the gate button in a linked sequencer, that does something else than
          gates.
        luckyreverse (trigger):
          Reverses the playin gorder of the affected steps. luckyamount has not
          influence.
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
        cv (cv):
          The CV output (or pitch output, if you use quantize).
        gate (gate):
          The gate output.
        startofsequence (trigger):
          Outputs a trigger whenever the sequencer starts playing from the beginning.
          This can be used for synchronizing with other sequencers. An external reset
          will also cause this output to trigger.
        startofpart (trigger):
          Outputs a trigger whenever a form part starts again. This is only interesting
          when you use form.
        startstepout (integer):
          Outputs the current start step. This is useful in case it has been
          interactively set with the buttons and you need that information for another
          circuit.
        endstepout (integer):
          Outputs the current end step. This is useful in case it has been interactively
          set with the buttons and you need that information for another circuit.
        currentstep (integer):
          Outputs the number of the step that is currently being played (starting from
          0).
        currentpage (integer):
          Outputs the number of the fader page that is currently played, i.e. the value
          you would have to feed into page in order to see the currently being played
          step.
        accumulator (integer):
          The current value of the pitch accumulator (an integer number in the range 0 …
          16.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 1336

    zorder: str | None = Field(
        default=None,
        serialization_alias="zorder",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "z"},
    )
    nume4s: str | None = Field(
        default=None,
        serialization_alias="nume4s",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n4"},
    )
    ledpreview: str | None = Field(
        default=None,
        serialization_alias="ledpreview",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pv"},
    )
    firstfader: str | None = Field(
        default=None,
        serialization_alias="firstfader",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "f"},
    )
    numfaders: str | None = Field(
        default=None,
        serialization_alias="numfaders",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n"},
    )
    numsteps: str | None = Field(
        default=None,
        serialization_alias="numsteps",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ns"},
    )
    page: str | None = Field(
        default=None,
        serialization_alias="page",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "p"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "c"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "tt"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    run: str | None = Field(
        default=None,
        serialization_alias="run",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ru"},
    )
    composemode: str | None = Field(
        default=None,
        serialization_alias="composemode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "cm"},
    )
    mute: str | None = Field(
        default=None,
        serialization_alias="mute",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "m"},
    )
    cvbase: str | None = Field(
        default=None,
        serialization_alias="cvbase",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "cb"},
    )
    cvrange: str | None = Field(
        default=None,
        serialization_alias="cvrange",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "cr"},
    )
    invert: str | None = Field(
        default=None,
        serialization_alias="invert",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "iv"},
    )
    quantize: str | None = Field(
        default=None,
        serialization_alias="quantize",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "q"},
    )
    cvnotches: str | None = Field(
        default=None,
        serialization_alias="cvnotches",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn"},
    )
    shiftsteps: str | None = Field(
        default=None,
        serialization_alias="shiftsteps",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sh"},
    )
    startstep: str | None = Field(
        default=None,
        serialization_alias="startstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ss"},
    )
    endstep: str | None = Field(
        default=None,
        serialization_alias="endstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "es"},
    )
    form: str | None = Field(
        default=None,
        serialization_alias="form",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fo"},
    )
    direction: str | None = Field(
        default=None,
        serialization_alias="direction",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "d"},
    )
    pingpong: str | None = Field(
        default=None,
        serialization_alias="pingpong",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "pp"},
    )
    pattern: str | None = Field(
        default=None,
        serialization_alias="pattern",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pt"},
    )
    repeatshift: str | None = Field(
        default=None,
        serialization_alias="repeatshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rs"},
    )
    ratchetshift: str | None = Field(
        default=None,
        serialization_alias="ratchetshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ras"},
    )
    accumulatorrange: str | None = Field(
        default=None,
        serialization_alias="accumulatorrange",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ac"},
    )
    constantlength: str | None = Field(
        default=None,
        serialization_alias="constantlength",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "co"},
    )
    autoreset: str | None = Field(
        default=None,
        serialization_alias="autoreset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ar"},
    )
    metricsaver: str | None = Field(
        default=None,
        serialization_alias="metricsaver",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ms"},
    )
    fadermode: str | None = Field(
        default=None,
        serialization_alias="fadermode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fm"},
    )
    buttonmode: str | None = Field(
        default=None,
        serialization_alias="buttonmode",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "bm"},
    )
    holdcv: str | None = Field(
        default=None,
        serialization_alias="holdcv",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "hc"},
    )
    defaultcv: str | None = Field(
        default=None,
        serialization_alias="defaultcv",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "dc"},
    )
    defaultgate: str | None = Field(
        default=None,
        serialization_alias="defaultgate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dfg"},
    )
    clearskips: str | None = Field(
        default=None,
        serialization_alias="clearskips",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cs"},
    )
    clearrepeats: str | None = Field(
        default=None,
        serialization_alias="clearrepeats",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "crp"},
    )
    clearstartend: str | None = Field(
        default=None,
        serialization_alias="clearstartend",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cse"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "gl"},
    )
    keyboardmode: str | None = Field(
        default=None,
        serialization_alias="keyboardmode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "km"},
    )
    keyboardcv: str | None = Field(
        default=None,
        serialization_alias="keyboardcv",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "kc"},
    )
    keyboardgate: str | None = Field(
        default=None,
        serialization_alias="keyboardgate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "kg"},
    )
    recordmode: str | None = Field(
        default=None,
        serialization_alias="recordmode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rm"},
    )
    recordsilence: str | None = Field(
        default=None,
        serialization_alias="recordsilence",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "rsi"},
    )
    copy_: str | None = Field(
        default=None,
        serialization_alias="copy",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cy"},
    )
    paste: str | None = Field(
        default=None,
        serialization_alias="paste",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pa"},
    )
    pastefaders: str | None = Field(
        default=None,
        serialization_alias="pastefaders",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pf"},
    )
    pastebuttons: str | None = Field(
        default=None,
        serialization_alias="pastebuttons",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pb"},
    )
    linktonext: str | None = Field(
        default=None,
        serialization_alias="linktonext",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ln"},
    )
    luckychance: str | None = Field(
        default=None,
        serialization_alias="luckychance",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "lc"},
    )
    luckyscope: str | None = Field(
        default=None,
        serialization_alias="luckyscope",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ls"},
    )
    luckyamount: str | None = Field(
        default=None,
        serialization_alias="luckyamount",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "la"},
    )
    luckycvbase: str | None = Field(
        default=None,
        serialization_alias="luckycvbase",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "lv"},
    )
    luckyfaders: str | None = Field(
        default=None,
        serialization_alias="luckyfaders",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lf"},
    )
    luckybuttons: str | None = Field(
        default=None,
        serialization_alias="luckybuttons",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lb"},
    )
    luckycvs: str | None = Field(
        default=None,
        serialization_alias="luckycvs",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lcv"},
    )
    luckycvdrift: str | None = Field(
        default=None,
        serialization_alias="luckycvdrift",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ld"},
    )
    luckyspread: str | None = Field(
        default=None,
        serialization_alias="luckyspread",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lr"},
    )
    luckyinvert: str | None = Field(
        default=None,
        serialization_alias="luckyinvert",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "li"},
    )
    luckyrandomizecv: str | None = Field(
        default=None,
        serialization_alias="luckyrandomizecv",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrc"},
    )
    luckygates: str | None = Field(
        default=None,
        serialization_alias="luckygates",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lg"},
    )
    luckyskips: str | None = Field(
        default=None,
        serialization_alias="luckyskips",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lk"},
    )
    luckyties: str | None = Field(
        default=None,
        serialization_alias="luckyties",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lt"},
    )
    luckygatepattern: str | None = Field(
        default=None,
        serialization_alias="luckygatepattern",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lgp"},
    )
    luckygateprob: str | None = Field(
        default=None,
        serialization_alias="luckygateprob",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lga"},
    )
    luckyrepeats: str | None = Field(
        default=None,
        serialization_alias="luckyrepeats",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrp"},
    )
    luckyratchets: str | None = Field(
        default=None,
        serialization_alias="luckyratchets",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrt"},
    )
    luckyshuffle: str | None = Field(
        default=None,
        serialization_alias="luckyshuffle",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lsh"},
    )
    buttoncolor: str | None = Field(
        default=None,
        serialization_alias="buttoncolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bc"},
    )
    luckyreverse: str | None = Field(
        default=None,
        serialization_alias="luckyreverse",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrv"},
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
    cv: str | None = Field(
        default=None,
        serialization_alias="cv",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": ""},
    )
    gate: str | None = Field(
        default=None,
        serialization_alias="gate",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g"},
    )
    startofsequence: str | None = Field(
        default=None,
        serialization_alias="startofsequence",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ssq"},
    )
    startofpart: str | None = Field(
        default=None,
        serialization_alias="startofpart",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "spa"},
    )
    startstepout: str | None = Field(
        default=None,
        serialization_alias="startstepout",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sso"},
    )
    endstepout: str | None = Field(
        default=None,
        serialization_alias="endstepout",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "eso"},
    )
    currentstep: str | None = Field(
        default=None,
        serialization_alias="currentstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cst"},
    )
    currentpage: str | None = Field(
        default=None,
        serialization_alias="currentpage",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cpg"},
    )
    accumulator: str | None = Field(
        default=None,
        serialization_alias="accumulator",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "acc"},
    )


class Euklid(DroidCircuit):
    """ Euclidean rhythm generator

    Args:
        clock (gate):
          Patch a clock signal here. It does not need to be steady – even if this is the
          most usual application. Note: this input is classified as a gate input, since
          the length of the gate is being preserved when forwarded to output and
          offbeats.
        reset (trigger):
          A trigger here resets the pattern to the start
        outputsignal (cv):
          Usually on active steps euklid just lets the original input clock get through
          to the output. If this parameter is used, it will be sent to the output on
          active steps instead. The easiest application is just setting it to 1. The
          output will then become 1 the whole time while the current step is active.
          This is useful if you want to use euklid as modulation CV rather than as
          trigger.
        length (integer):
          The length of a pattern. This is interpreted as an integer number, which must
          be greater than 0. If it is not then 1 is assumed. If you CV control the
          length, use multiplication. The maximum accepted length is 64.
        beats (integer):
          The number of active beats that should be distributed amongst the length
          steps. If that number is greater than length, it is capped to that number.
        offset (integer):
          rotates or shifts the pattern by that number of steps. This number can be
          positive or negative.
        output (gate):
          Output of the beats in the current pattern. The gate length is directly taken
          from the input clock – just as the voltage.
        offbeats (gate):
          Here those impulses will be output where there is no beat in the pattern.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 48

    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "c"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    outputsignal: str | None = Field(
        default=None,
        serialization_alias="outputsignal",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "os"},
    )
    length: str | None = Field(
        default=None,
        serialization_alias="length",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "l"},
    )
    beats: str | None = Field(
        default=None,
        serialization_alias="beats",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "b"},
    )
    offset: str | None = Field(
        default=None,
        serialization_alias="offset",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "of"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "o"},
    )
    offbeats: str | None = Field(
        default=None,
        serialization_alias="offbeats",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ob"},
    )


class Motoquencer(DroidCircuit):
    """ Motor fader sequencer

    Args:
        firstfader (integer):
          First M4 fader of the sequencer (starting with 1). If you omit this, it starts
          at the first fader of your first M4.
        numfaders (integer):
          Number of faders to use for your sequencer. The typical numbers are 4, 8, 16
          and 32. 32 is the maximum (eight M4 units). If you omit this, all of your M4
          faders will be used.
        numsteps (integer):
          Number of steps your sequence consists of (at maximum). The number of steps
          can be greater than the number of faders. In that case use page for paging
          your faders so that you can edit all of the steps. Having the number of steps
          less than the faders, makes no sense – it's just a waste of faders. The
          maximum number of steps is 32.  If you don't set this parameter, the number of
          steps will be set to the number of faders.  Note: changing this setting
          dynamically can provoke various surprising behaviours. For example the number
          of pages (see parameter page) might be reduced. Or the end marker is forcibly
          moved around. If you want to change the length of the sequence via CV, better
          use endstep or autoreset.  Another note: Setting numsteps will not restrict
          the number of faders. If you set numsteps = 4 but have eight faders available,
          the circuit will use all these, even if faders 5, 6, 7 and 8 will be useless.
          You need to set numfaders = 4 in this situation.
        page (integer):
          Use this parameter, if you have less faders than steps. The first page is 0,
          not 1. For example if you have 4 faders but 16 steps, you can select between
          the four “pages” of four faders each, by settings bar to 0, 1, 2 or 3. The
          output of a buttongroup with one button per page is a good match for this
          parameter.
        clock (trigger):
          Patch an input clock here. If you want to use ratcheting, that clock needs to
          be stable and regular, because the sequencer needs to interpolate the clock
          and create evenly distributed new beats within two clock ticks. If you don't
          use ratching, you can use any rhythm you like here – may it be shuffled,
          euklidean, the output from another sequencer or whatever you like. Each clock
          tick will advance the sequence to the next step (or to the next repition of
          the current step).
        taptempo (trigger):
          If your clock is not steady but might be stopped and restarted, you should
          patch a steady clock here. This avoids problems with the computation of the
          gate length right after starting the clock. The tap tempo computation needs a
          series of at least two clock pulses so the gate length of the first step is
          wrong after the clock has stopped for a while.
        reset (trigger):
          A trigger here resets the sequencer to its start step. The next clock tick (or
          a tick that is roughly at the same time as the reset) will play step 1. Note:
          If there is a reset without a clock tick at the same time, the sequencer will
          go to “step 0”, which is a special state where it waits for the clock to
          advance to the first step. Without that fancy logic, a reset plus clock would
          skip step 1 and start with step 2.
        run (gate):
          If you set this input to 0, the sequencer will ignore all incoming clock
          ticks. It stops. The default of 1 is normal operation, where it runs. This
          input is a better way to temporarily stop the sequencer than to stop the
          clock. The reason: for computing the gate length and ratchets a steady input
          clock is needed. If you stop the clock, the next gate length and ratches right
          after the next start will have the wrong duration since at least two clock
          ticks are neccessary for computing its speed.  Note: This input is not a
          replacement for mute, since a muted sequencer leaves the clock running and
          advances steps. It just mutes the gate output.
        composemode (gate):
          Enabling “compose mode” makes it easier to find the right note in a step, when
          creating more complex melodies.  When composemode is set to 1, the sequencer
          stops clocking. Instead – every time you change the CV of a step, it
          immediately jumps to that step, outputs the changed CV and opens the gate for
          a short time, so you can listen to the changed note.
        mute (gate):
          If you set this to 1, the gate output of the sequencer is muted (will always
          be 0). Any changes of the CV output still happen.
        cvbase (cv):
          Here you set the voltage the sequencer will output if the CV fader is at the
          bottom position. The allowed range is -1 … 1 (which is the same as the range
          from -10 V to +10 V, if you output the CV directly to an output).
        cvrange (cv):
          CV range of the faders. So the resulting CV lies somewhere between cvbase and
          cvbase + cvrange. The CV range cannot be negative and is capped at 1. If you
          need a greater range, consider multiplying the output value of the cv output
          of the sequencer.
        invert (gate):
          Inverts the CV or pitch output. This is like mirroring the fader position. Now
          if the fader is up, the output is low and vice versa. In scale quantized mode,
          the melody still stays within the scale.
        quantize (integer):
          Switches on quantization in two levels. At 0, the faders run freely and output
          a continous CV.  At 1, the output is quantized to semitones, which is 1/12V
          steps. Also the faders will get artifical notches – one for each semitone.
          That is, unless your range is too large. The maximum number of notches with
          force feedback is 25, so if your range exceeds two octaves (0.2), the notches
          are turned off.  At 2, the output is quantized to the scale that root and
          degree define. Furthermore the individual scale notes can be switched on or
          off with the parameters select1, select3 and so on. Note: the root input does
          not select the lowest note of the CV range. That is still set with cvbase. It
          is just used for selecting the scale.  0no quantization 1quantize to semitones
          (1/12V steps) 2quantize to the scale set by root and degree
        cvnotches (integer):
          Usually the CVs of the steps are ment to be note pitches (when quantize is 1
          or 2), or just free CVs (quantize = 0). There is an alternative mode, however,
          that allows you to assign integer values like 0, 1, 2 and so on to each step.
          To do this set cvnotches to a value of 2 or greater. This defines the number
          of discrete values (and hence notches) for each step and put CVs of the
          sequence into notched mode. 1 makes no sense, of course, since in this “pitch
          bend mode” the faders would always return to the neutral position.  In notched
          mode the cv output does not output a pitch but a notch number starting from 0.
          cvbase, cvrange and quantize are ignored.  The maximum number of notches is
          127, but the haptic force feedback of the motor faders is disabled starting at
          26.
        shiftsteps (integer):
          Shifts all your steps by that number to the left (negative numbers shift to
          the right). So if shiftsteps is 1, right after a reset, the sequencer will not
          play step 1, but step 2. The shifting wraps around at the end of your
          sequence, so if you have 24 steps and shift is 1, the sequencer will play step
          1 instead of step 24.  Note: Other things like startstep, endstep, playmode,
          from and autoreset take place after shifting.
        startstep (integer):
          Sets the first step to be used.  This means that after a reset or when the
          sequencer comes to the end of the sequence, it will begin at this step.  There
          is also a way for settings start and end with buttons (see below at
          buttonmode). If you use the interactive mode, the startstep and endstep
          settings will be overridden. The are reactived if you clear everything.  Note:
          startstep and endstep take place after applying shiftsteps.
        endstep (integer):
          Sets the last of the steps to be played. The default is to play all steps.
          After playing the end step, the sequencer moves on to the start step at the
          next clock tick.  If startstep is equal to endstep, the sequence just consists
          of one single step.  Settings startstep larger then endstep is allowed and
          reverses the playing order.
        form (integer):
          This is an advanced feature that allows you to slice your steps into two or
          three parts and create musical song forms like AAAB or ABAC. Each of the parts
          A, B or C are then played according to the playmode.
          The form AAAB, for example, creates a 32 step form from just 16 steps, by
          playing the first 8 steps three times and then the second 8 steps once.
          The following forms are available:
          0A (forms are basically deactivated) 1AAAB 2AABB 3ABAC 4AAABAAAC 5AB 6AAB
          Notes:
          * The splitting of the steps into parts takes place after accounting for
            startstep and endstep.
          * Forms with A, B and C split the pattern into three parts. These parts can
            only be of equal size if the number of steps is dividable by 3, of course.
          * The pattern AB is really not the same as A, e.g when direction is set 1
            (reverse). In that case each of the parts is played backwards, but the parts
            themselves move forwards on your steps.

        direction (gate):
          Sets the general direction in which the sequencer moves through the steps. 0
          means forwards and 1 means backwards.
        pingpong (gate):
          If set to 1, the sequencer will change the direction every time it reaches the
          start or end of the sequence.
        pattern (integer):
          Selects one of a list of movement patterns. That way, the sequence steps are
          not played in linear order but in a more sophisticated movement.  Available
          pattern are:   0go step by step to the sequence (normal)→ 1two steps forward,
          one step backward→ → ← 2double step forward, one step backward⇒ ← 3double step
          forward, double step backward, single step forward⇒ ⇐  → 4double step forward,
          single step forward, double step backward, single step forward⇒ → ⇐ → 5random
          single step forward or backward↔ 6go forward by a small random number of
          steps→ × ?  7random jump to any allowed (other) note⇕
        repeatshift (integer):
          This is a number in the range -24 … +24. If you set this to non-zero, each
          repetition of a step shifts the played note by that many notes within the
          selected scale notes. This only has effect on steps where the number of
          repeats is greater than 1. Also it is only is applied when the quantize = 2.
        ratchetshift (integer):
          This is a number in the range -24 … +24. If you set this to non-zero, each
          ratchet of a step shifts the played note by that many notes within the
          selected scale notes. This only has effect on steps where the number of
          ratchets is greater than 1. Also it is only is applied when the quantize = 2.
          If you combine ratchetshift with repeatshift, both shifts are added together.
          And the ratchet shifting is reset for each repetition of the step.
        accumulatorrange (integer):
          Using this parameter enables the pitch accumulator. The value sets the maximum
          value the accumulator can get.  The maximum is 16. If you set this to 0, the
          fader mode for pitch randomization still is in the special mode where the
          upper four positions control the impact of the accumulator.  Please consult
          the manual of motoquencer for details on the pitch accumulator.
        constantlength (gate):
          This input enables a feature that (tries to) keep the actual length of the
          sequence constant. There are two levels. If constantlength = 1, every change
          in the repeats of a step is compensated by changing the repeats in the
          following steps. E.g. if you increase the number of repeats from 4 to 5 in
          step 3 (by moving the fader in the appropriate fader mode), the repeats in
          step 4 are reduced by 1. If they are already 1, step 5 is tried an so on,
          until it wrap around to step 1.  The second level is constantlength = 2. Here
          also the skip setting of steps is honored and modified in order to keep the
          length constant. A skipped step essentially has the length 0 (or 0 repeats).
          The componsation is now done not only when the repeats are changed but also
          when skip is switched on or off on a step.  All the compensation is only
          active with the range that is set with the start and end step.
        autoreset (integer):
          If set to non-zero, automatically issues a reset (just like a trigger to
          reset) every N clock ticks.
        metricsaver (gate):
          The Metric Saver ™ helps you to reliably come back to your original metric and
          time after playing around with all sorts of parameters that change the played
          number of steps in the sequence.  These are: startstep, endstep (also when
          changed interactively), form, direction, pingpong, pattern, autoreset and
          repeats and skips of individual steps. Therefore it counts the actual number
          of clock cycles since the last external reset (or system start). And when all
          of these features are deactivated, it snaps back the clock to the position it
          would have been by now if you never had played around with all the funny
          stuff.  That way, during a live performance, you can safely play around with
          all this polymetric and otherwise time disrupting stuff and as soon as you
          clean up your mess – voila: you are back on track and in sync with the rest of
          the “band”.  The metric saver is turned on by default. But you can disable it
          by setting the parameter to 0.
        fadermode (integer):
          Switches the current meaning of the motor faders. You probably want to connect
          the output of a buttongroup here. Here are the possible modes:  0pitch / CV
          1randomize CV 2gate propability 3repeats (up to 16) 4gate pattern 5ratchets
          (up to 8) 6gate 7skip
        buttonmode (integer):
          Switches the current meaning of the touch buttons below the faders. You
          probably want to connect the output of a buttongroup here. Here are the
          possible modes:  0gates 1start / end 2gate pattern 3skip
        holdcv (gate):
          This setting determines wether the CV output changes every time the sequencer
          moves to the next step or just when that step is active (a gate is being
          played). The latter is the default. But if you set this to 0, the CV values of
          steps without gates will also influence the output CV.  Note: regardless of
          this setting, the CV will never change inbetween. Any change of the CV faders,
          the cvbase and cvrange and so on will only take effect when the next step is
          played. This also ensures that repeats or ratchets are always in the same
          pitch.
        defaultcv (cv):
          Set the CV the steps should be set to on a trigger to clear. That value must
          be within the range set by cvbase and cvrange, or it will be truncated to that
          range.  If you have set cvnotches, however, the value is expected to be an
          integer in the range 0 ... cvnotches - 1.
        defaultgate (gate):
          Here you set to which state (on / off) the gates should be set on a trigger to
          clear.
        clearskips (trigger):
          A trigger here removes the “skip” setting from all steps.
        clearrepeats (trigger):
          A trigger here resets the number of repeats to 1 for each step.
        clearstartend (trigger):
          A trigger here clears the manual settings of the start and end step. So the
          sequence will be played in its full length (again) .
        gatelength (cv):
          The gate length in input clock cycles. A value of 0.5 thus means half a clock
          cycle. A steady input clock is needed for this to work. Please note that if
          the gate length is >= 1.0, two succeeding notes will get a steady gate, which
          essentially means legato.  If you don't use a steady clock, set this parameter
          to 0. This will output a minimal gate length of about 10 ms (basically just a
          trigger).
        keyboardmode (integer):
          This input sets how a keyboard, that is hooked to keyboardcv, and keyboardgate
          should be used for directly playing notes. You can set it to 0, 1 or 2.
          0ignore the keyboard inputs 1keyboard and sequencer play together, keyboard
          has precedence 2mute sequencer, just play keyboard
        keyboardcv (voltperoctave):
           The pitch input of a keyboard. This is used for playing along with the
          keyboardmode or recording with recordmode.
        keyboardgate (gate):
           The gate input of a keyboard. A positive gate enabled play along (see
          keyboardmode) and also recording, if recordmode is set accordingly.
        recordmode (integer):
           Use this input to record melodies played with a keyboard (namely keyboardcv
          and keyboardgate) into the sequencer. There are three possible settings:
          0don't record 1record, notes longer than one step will automatically tie steps
          via the gate pattern 2record, don't tie notes. Ignore the length of the input
          note
        recordsilence (gate):
          When this input is set to 1 while recording, silence will be recorded while
          keyboardgate is off. Otherwise you can just add notes to the sequence.
        copy (trigger):
          A trigger here copies the current page of the sequence to an internal
          clipboard. The clipboard is not part of any preset and is also not saved to
          the SD card. It can be used later for pasting it's data to another preset or
          another page of a sequence.
        paste (trigger):
          A trigger here copies the steps from the clipboard to the current page.
        pastefaders (trigger):
          This is like paste, but just the values of the faders of the current fadermode
          are copied.
        pastebuttons (trigger):
          This is like paste, but just the values of the faders of the current
          buttonmode are copied. Note: the button mode “start / end” is not supported by
          copy and paste.
        linktonext (gate):
          This settings allows you to create motoquencer tracks that have more than one
          CV or gate output for each step. If you set this to 1, the next motoquencer
          circuit in your patch will by synchronized to this one. This means that it
          always plays the same step number – including all fancy operating like
          shiftsteps, startstep, endstep, form, pattern and autoreset. All those inputs
          and also clock and reset are ignored by the next motoquencer.  The same holds
          for the “repeats” and “skip” setting of the steps.  fadermode and buttonmode
          are extended to the next motoquencers by adding 10 for each motoquencer to
          follow. So fadermode = 10 will show the CV of next motoquencer in the faders.
          fadermode = 11 the CV randomization of the next motoquencer. fadermode = 20
          show the CV of the third linked motoquencer and so on.  Don't set fadermode or
          buttonmode on the linked motoquencers. They will be ignored there.  Note: The
          linktonext setting cannot by dynamically changed. It needs to be fixed 0 or 1.
          You cannot use any button or internal cable or other methods to change it
          while the patch is running.
        luckychance (fraction):
          Sets tha chance for a step to be affected by the next “lucky” operation (see
          triggers below).
        luckyscope (integer):
          Determines which part of the sequence is affected by the “lucky” operations.
          Depending on this setting the following steps are affected:   0All steps
          between the current start and end step 1All steps 2All steps between start and
          end on the current page 3All steps on the current page
        luckyamount (fraction):
          Sets the amount of change that a “lucky” operation does to a step. The meaning
          depends on the operation. See the parameters below.
        luckycvbase (fraction):
          This parameter affects only the operation luckycvs and luckyfaders when the
          fader mode is set to 0. It adds a fixed amount of CV to the random result, so
          that lies in the range luckycvbase … (luckycvbase + luckyamount).
        luckyfaders (trigger):
          Moves the currently selected faders (according to fadermode) to new random
          positions. luckyamount sets the maximum value of the fader, where 1 allows the
          maximum.
        luckybuttons (trigger):
          Randomly toggles the currently selected buttons (according to buttonmode).
          luckyamount only has an effect when the gate patterns are selected, since
          here, four different values are possible. luckamount restricts them if it is
          lower than 1.
        luckycvs (trigger):
          Replaces the affected steps' CVs with a new random CVs. The lowest possible CV
          is cvbase. If luckyamount is 1, the highest possible CV is cvbase + cvrange,
          otherwise it is cvbase + luckyamount × cvrange.
        luckycvdrift (trigger):
          Modifies the affected steps' CV randomly up or down. They will stay in the CV
          range set by cvbase and cvrange. luckyamount controls the amount of change.
        luckyspread (trigger):
          First computes the average CV of all steps. Then changes the CV values of the
          affected steps such that their distance to the average increases or decreases.
          If luckyamount is greater than 0.5, the distance is increased. Otherwise it is
          decreased.
        luckyinvert (trigger):
          Inverts the CVs of the affected steps within the allowed CV range. luckyamount
          has no influence.
        luckyrandomizecv (trigger):
          Sets the “randomize CV” values of the affected steps to random values (yes,
          this is double randomization). The luckyamount sets the maximum randomization
          value that will be set.
        luckygates (trigger):
          Sets the gates of the affected steps randomly to on or off. The chance for on
          is determined by luckyamount. So with luckyamount = 0 you clear all gates and
          with luckyamount = 1 you set all gates.
        luckyskips (trigger):
          Sets the “skip this step” setting of the affected steps randomly to skip or
          normal. The chance for skip is determined by luckyamount.
        luckyties (trigger):
          Sets the “tie this step to the next” setting of the affected steps randomly to
          tie or normal. This is the same as setting the gate pattern to the upper most
          position. The chance for tie is determined by luckyamount.
        luckygatepattern (trigger):
          Randomizes the gate pattern of the selected steps (there are four different
          values: once, all, hold and tie). Use luckyamount to reduce that set.
        luckygateprob (trigger):
          Sets the “randomize gate” values of the affected steps to random values (yes,
          this is double randomization). The luckyamount sets the minimum randomization
          value that will be set (yes, this is inverted). So with luckyamount = 1 you
          disable randomization and make the gates play always. With luckymount = 0 you
          set the gate propability to the lowest possible value (still not 0).
        luckyrepeats (trigger):
          Randomly sets the number of repeats of the affected steps to something between
          1 and 16 (the maximum). The luckyamount determines the maximum repetition
          number, where 1 stands for a maximum of 16 repetitions.
        luckyratchets (trigger):
          Randomly sets the number of ratches of the affected steps to something between
          1 and 8 (the maximum). The luckyamount determines the maximum ratchet number,
          where 1 stands for a maximum of 8 ratchets.
        luckyshuffle (trigger):
          Randomly swaps all affected affected steps (their playing order) together will
          all their attributes. luckyamount has no influence.
        buttoncolor (cv):
          Set a user defined color for the gate buttons. This color is only used when
          buttonmode = 0. The main purpose of this option is to allow a separate color
          for the gate button in a linked sequencer, that does something else than
          gates.
        luckyreverse (trigger):
          Reverses the playin gorder of the affected steps. luckyamount has not
          influence.
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
        cv (cv):
          The CV output (or pitch output, if you use quantize).
        gate (gate):
          The gate output.
        startofsequence (trigger):
          Outputs a trigger whenever the sequencer starts playing from the beginning.
          This can be used for synchronizing with other sequencers. An external reset
          will also cause this output to trigger.
        startofpart (trigger):
          Outputs a trigger whenever a form part starts again. This is only interesting
          when you use form.
        startstepout (integer):
          Outputs the current start step. This is useful in case it has been
          interactively set with the buttons and you need that information for another
          circuit.
        endstepout (integer):
          Outputs the current end step. This is useful in case it has been interactively
          set with the buttons and you need that information for another circuit.
        currentstep (integer):
          Outputs the number of the step that is currently being played (starting from
          0).
        currentpage (integer):
          Outputs the number of the fader page that is currently played, i.e. the value
          you would have to feed into page in order to see the currently being played
          step.
        accumulator (integer):
          The current value of the pitch accumulator (an integer number in the range 0 …
          16.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 1168

    firstfader: str | None = Field(
        default=None,
        serialization_alias="firstfader",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "f"},
    )
    numfaders: str | None = Field(
        default=None,
        serialization_alias="numfaders",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "n"},
    )
    numsteps: str | None = Field(
        default=None,
        serialization_alias="numsteps",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ns"},
    )
    page: str | None = Field(
        default=None,
        serialization_alias="page",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "p"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 2, "type": "trigger", "shortname": "c"},
    )
    taptempo: str | None = Field(
        default=None,
        serialization_alias="taptempo",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "tt"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "r"},
    )
    run: str | None = Field(
        default=None,
        serialization_alias="run",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ru"},
    )
    composemode: str | None = Field(
        default=None,
        serialization_alias="composemode",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "cm"},
    )
    mute: str | None = Field(
        default=None,
        serialization_alias="mute",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "m"},
    )
    cvbase: str | None = Field(
        default=None,
        serialization_alias="cvbase",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "cb"},
    )
    cvrange: str | None = Field(
        default=None,
        serialization_alias="cvrange",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "cr"},
    )
    invert: str | None = Field(
        default=None,
        serialization_alias="invert",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "iv"},
    )
    quantize: str | None = Field(
        default=None,
        serialization_alias="quantize",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "q"},
    )
    cvnotches: str | None = Field(
        default=None,
        serialization_alias="cvnotches",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn"},
    )
    shiftsteps: str | None = Field(
        default=None,
        serialization_alias="shiftsteps",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sh"},
    )
    startstep: str | None = Field(
        default=None,
        serialization_alias="startstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ss"},
    )
    endstep: str | None = Field(
        default=None,
        serialization_alias="endstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "es"},
    )
    form: str | None = Field(
        default=None,
        serialization_alias="form",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fo"},
    )
    direction: str | None = Field(
        default=None,
        serialization_alias="direction",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "d"},
    )
    pingpong: str | None = Field(
        default=None,
        serialization_alias="pingpong",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "pp"},
    )
    pattern: str | None = Field(
        default=None,
        serialization_alias="pattern",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pt"},
    )
    repeatshift: str | None = Field(
        default=None,
        serialization_alias="repeatshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rs"},
    )
    ratchetshift: str | None = Field(
        default=None,
        serialization_alias="ratchetshift",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ras"},
    )
    accumulatorrange: str | None = Field(
        default=None,
        serialization_alias="accumulatorrange",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ac"},
    )
    constantlength: str | None = Field(
        default=None,
        serialization_alias="constantlength",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "co"},
    )
    autoreset: str | None = Field(
        default=None,
        serialization_alias="autoreset",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ar"},
    )
    metricsaver: str | None = Field(
        default=None,
        serialization_alias="metricsaver",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ms"},
    )
    fadermode: str | None = Field(
        default=None,
        serialization_alias="fadermode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fm"},
    )
    buttonmode: str | None = Field(
        default=None,
        serialization_alias="buttonmode",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "bm"},
    )
    holdcv: str | None = Field(
        default=None,
        serialization_alias="holdcv",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "hc"},
    )
    defaultcv: str | None = Field(
        default=None,
        serialization_alias="defaultcv",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "dc"},
    )
    defaultgate: str | None = Field(
        default=None,
        serialization_alias="defaultgate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dfg"},
    )
    clearskips: str | None = Field(
        default=None,
        serialization_alias="clearskips",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cs"},
    )
    clearrepeats: str | None = Field(
        default=None,
        serialization_alias="clearrepeats",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "crp"},
    )
    clearstartend: str | None = Field(
        default=None,
        serialization_alias="clearstartend",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cse"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "gl"},
    )
    keyboardmode: str | None = Field(
        default=None,
        serialization_alias="keyboardmode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "km"},
    )
    keyboardcv: str | None = Field(
        default=None,
        serialization_alias="keyboardcv",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "kc"},
    )
    keyboardgate: str | None = Field(
        default=None,
        serialization_alias="keyboardgate",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "kg"},
    )
    recordmode: str | None = Field(
        default=None,
        serialization_alias="recordmode",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "rm"},
    )
    recordsilence: str | None = Field(
        default=None,
        serialization_alias="recordsilence",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "rsi"},
    )
    copy_: str | None = Field(
        default=None,
        serialization_alias="copy",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "cy"},
    )
    paste: str | None = Field(
        default=None,
        serialization_alias="paste",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pa"},
    )
    pastefaders: str | None = Field(
        default=None,
        serialization_alias="pastefaders",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pf"},
    )
    pastebuttons: str | None = Field(
        default=None,
        serialization_alias="pastebuttons",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pb"},
    )
    linktonext: str | None = Field(
        default=None,
        serialization_alias="linktonext",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ln"},
    )
    luckychance: str | None = Field(
        default=None,
        serialization_alias="luckychance",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "lc"},
    )
    luckyscope: str | None = Field(
        default=None,
        serialization_alias="luckyscope",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ls"},
    )
    luckyamount: str | None = Field(
        default=None,
        serialization_alias="luckyamount",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "la"},
    )
    luckycvbase: str | None = Field(
        default=None,
        serialization_alias="luckycvbase",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "lv"},
    )
    luckyfaders: str | None = Field(
        default=None,
        serialization_alias="luckyfaders",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lf"},
    )
    luckybuttons: str | None = Field(
        default=None,
        serialization_alias="luckybuttons",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lb"},
    )
    luckycvs: str | None = Field(
        default=None,
        serialization_alias="luckycvs",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lcv"},
    )
    luckycvdrift: str | None = Field(
        default=None,
        serialization_alias="luckycvdrift",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ld"},
    )
    luckyspread: str | None = Field(
        default=None,
        serialization_alias="luckyspread",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lr"},
    )
    luckyinvert: str | None = Field(
        default=None,
        serialization_alias="luckyinvert",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "li"},
    )
    luckyrandomizecv: str | None = Field(
        default=None,
        serialization_alias="luckyrandomizecv",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrc"},
    )
    luckygates: str | None = Field(
        default=None,
        serialization_alias="luckygates",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lg"},
    )
    luckyskips: str | None = Field(
        default=None,
        serialization_alias="luckyskips",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lk"},
    )
    luckyties: str | None = Field(
        default=None,
        serialization_alias="luckyties",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lt"},
    )
    luckygatepattern: str | None = Field(
        default=None,
        serialization_alias="luckygatepattern",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lgp"},
    )
    luckygateprob: str | None = Field(
        default=None,
        serialization_alias="luckygateprob",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lga"},
    )
    luckyrepeats: str | None = Field(
        default=None,
        serialization_alias="luckyrepeats",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrp"},
    )
    luckyratchets: str | None = Field(
        default=None,
        serialization_alias="luckyratchets",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrt"},
    )
    luckyshuffle: str | None = Field(
        default=None,
        serialization_alias="luckyshuffle",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lsh"},
    )
    buttoncolor: str | None = Field(
        default=None,
        serialization_alias="buttoncolor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "bc"},
    )
    luckyreverse: str | None = Field(
        default=None,
        serialization_alias="luckyreverse",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "lrv"},
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
    cv: str | None = Field(
        default=None,
        serialization_alias="cv",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": ""},
    )
    gate: str | None = Field(
        default=None,
        serialization_alias="gate",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g"},
    )
    startofsequence: str | None = Field(
        default=None,
        serialization_alias="startofsequence",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ssq"},
    )
    startofpart: str | None = Field(
        default=None,
        serialization_alias="startofpart",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "spa"},
    )
    startstepout: str | None = Field(
        default=None,
        serialization_alias="startstepout",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sso"},
    )
    endstepout: str | None = Field(
        default=None,
        serialization_alias="endstepout",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "eso"},
    )
    currentstep: str | None = Field(
        default=None,
        serialization_alias="currentstep",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cst"},
    )
    currentpage: str | None = Field(
        default=None,
        serialization_alias="currentpage",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cpg"},
    )
    accumulator: str | None = Field(
        default=None,
        serialization_alias="accumulator",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "acc"},
    )


class Polytool(DroidCircuit):
    """ Change number of voices in polyphonic setups

    Args:
        pitchinput1 (any):
          The pitches of up to 16 input voices.
        pitchinput2 (any):
          The pitches of up to 16 input voices.
        pitchinput3 (any):
          The pitches of up to 16 input voices.
        pitchinput4 (any):
          The pitches of up to 16 input voices.
        pitchinput5 (any):
          The pitches of up to 16 input voices.
        pitchinput6 (any):
          The pitches of up to 16 input voices.
        pitchinput7 (any):
          The pitches of up to 16 input voices.
        pitchinput8 (any):
          The pitches of up to 16 input voices.
        pitchinput9 (any):
          The pitches of up to 16 input voices.
        pitchinput10 (any):
          The pitches of up to 16 input voices.
        pitchinput11 (any):
          The pitches of up to 16 input voices.
        pitchinput12 (any):
          The pitches of up to 16 input voices.
        pitchinput13 (any):
          The pitches of up to 16 input voices.
        pitchinput14 (any):
          The pitches of up to 16 input voices.
        pitchinput15 (any):
          The pitches of up to 16 input voices.
        pitchinput16 (any):
          The pitches of up to 16 input voices.
        gateinput1 (gate):
          The gates of up to 16 input voices.
        gateinput2 (gate):
          The gates of up to 16 input voices.
        gateinput3 (gate):
          The gates of up to 16 input voices.
        gateinput4 (gate):
          The gates of up to 16 input voices.
        gateinput5 (gate):
          The gates of up to 16 input voices.
        gateinput6 (gate):
          The gates of up to 16 input voices.
        gateinput7 (gate):
          The gates of up to 16 input voices.
        gateinput8 (gate):
          The gates of up to 16 input voices.
        gateinput9 (gate):
          The gates of up to 16 input voices.
        gateinput10 (gate):
          The gates of up to 16 input voices.
        gateinput11 (gate):
          The gates of up to 16 input voices.
        gateinput12 (gate):
          The gates of up to 16 input voices.
        gateinput13 (gate):
          The gates of up to 16 input voices.
        gateinput14 (gate):
          The gates of up to 16 input voices.
        gateinput15 (gate):
          The gates of up to 16 input voices.
        gateinput16 (gate):
          The gates of up to 16 input voices.
        roundrobin (gate):
          Normally when looking for a free output for playing the next note, this
          circuit will start from pitchoutput1 in its search. This way, if there are not
          more notes than outputs at any time, the notes played first will always be
          played at the lowest numbered outputs. This leads to a deterministic behaviour
          when it comes to playing things like chords. The same voice will always be
          used for the first note in the stream of MIDI events.  When you switch
          roundrobin to 1, this changes. Now the outputs are scanned in a round-robin
          fashion, like in a rotating switch. That way every output has the same chance
          to get a new note. Here it can even make sense to define multiple voices even
          if the track is monophonic. When you use envelopes with longer release times,
          you can transform such a melody into chords with simultaneous notes.  Note:
          When all outputs are currently used by a note, roundrobin has no influence.
          Here voiceallocation selects which of the notes will be dropped.
        voiceallocation (integer):
          When from the pitch inputs, at any given time, more voice are active than you
          have outputs assigned, normally the “oldest” notes would be cancelled. This
          behaviour can be configured here by setting voiceallocation to one of the
          following values:   0The oldest note will be cancelled (default) 1The new note
          will not be played and simply be omitted 2The lowest note will be cancelled
          3The highest note will be cancelled
        pitchoutput1 (any):
          The pitches of up to 16 output voices.
        pitchoutput2 (any):
          The pitches of up to 16 output voices.
        pitchoutput3 (any):
          The pitches of up to 16 output voices.
        pitchoutput4 (any):
          The pitches of up to 16 output voices.
        pitchoutput5 (any):
          The pitches of up to 16 output voices.
        pitchoutput6 (any):
          The pitches of up to 16 output voices.
        pitchoutput7 (any):
          The pitches of up to 16 output voices.
        pitchoutput8 (any):
          The pitches of up to 16 output voices.
        pitchoutput9 (any):
          The pitches of up to 16 output voices.
        pitchoutput10 (any):
          The pitches of up to 16 output voices.
        pitchoutput11 (any):
          The pitches of up to 16 output voices.
        pitchoutput12 (any):
          The pitches of up to 16 output voices.
        pitchoutput13 (any):
          The pitches of up to 16 output voices.
        pitchoutput14 (any):
          The pitches of up to 16 output voices.
        pitchoutput15 (any):
          The pitches of up to 16 output voices.
        pitchoutput16 (any):
          The pitches of up to 16 output voices.
        gateoutput1 (gate):
          The gates of up to 16 output voices.
        gateoutput2 (gate):
          The gates of up to 16 output voices.
        gateoutput3 (gate):
          The gates of up to 16 output voices.
        gateoutput4 (gate):
          The gates of up to 16 output voices.
        gateoutput5 (gate):
          The gates of up to 16 output voices.
        gateoutput6 (gate):
          The gates of up to 16 output voices.
        gateoutput7 (gate):
          The gates of up to 16 output voices.
        gateoutput8 (gate):
          The gates of up to 16 output voices.
        gateoutput9 (gate):
          The gates of up to 16 output voices.
        gateoutput10 (gate):
          The gates of up to 16 output voices.
        gateoutput11 (gate):
          The gates of up to 16 output voices.
        gateoutput12 (gate):
          The gates of up to 16 output voices.
        gateoutput13 (gate):
          The gates of up to 16 output voices.
        gateoutput14 (gate):
          The gates of up to 16 output voices.
        gateoutput15 (gate):
          The gates of up to 16 output voices.
        gateoutput16 (gate):
          The gates of up to 16 output voices.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 240

    pitchinput1: str | None = Field(
        default=None,
        serialization_alias="pitchinput1",
        json_schema_extra={"essential": 2, "type": "any", "shortname": "pi1"},
    )
    pitchinput2: str | None = Field(
        default=None,
        serialization_alias="pitchinput2",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi2"},
    )
    pitchinput3: str | None = Field(
        default=None,
        serialization_alias="pitchinput3",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi3"},
    )
    pitchinput4: str | None = Field(
        default=None,
        serialization_alias="pitchinput4",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi4"},
    )
    pitchinput5: str | None = Field(
        default=None,
        serialization_alias="pitchinput5",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi5"},
    )
    pitchinput6: str | None = Field(
        default=None,
        serialization_alias="pitchinput6",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi6"},
    )
    pitchinput7: str | None = Field(
        default=None,
        serialization_alias="pitchinput7",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi7"},
    )
    pitchinput8: str | None = Field(
        default=None,
        serialization_alias="pitchinput8",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi8"},
    )
    pitchinput9: str | None = Field(
        default=None,
        serialization_alias="pitchinput9",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi9"},
    )
    pitchinput10: str | None = Field(
        default=None,
        serialization_alias="pitchinput10",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi10"},
    )
    pitchinput11: str | None = Field(
        default=None,
        serialization_alias="pitchinput11",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi11"},
    )
    pitchinput12: str | None = Field(
        default=None,
        serialization_alias="pitchinput12",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi12"},
    )
    pitchinput13: str | None = Field(
        default=None,
        serialization_alias="pitchinput13",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi13"},
    )
    pitchinput14: str | None = Field(
        default=None,
        serialization_alias="pitchinput14",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi14"},
    )
    pitchinput15: str | None = Field(
        default=None,
        serialization_alias="pitchinput15",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi15"},
    )
    pitchinput16: str | None = Field(
        default=None,
        serialization_alias="pitchinput16",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "pi16"},
    )
    gateinput1: str | None = Field(
        default=None,
        serialization_alias="gateinput1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "gi1"},
    )
    gateinput2: str | None = Field(
        default=None,
        serialization_alias="gateinput2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi2"},
    )
    gateinput3: str | None = Field(
        default=None,
        serialization_alias="gateinput3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi3"},
    )
    gateinput4: str | None = Field(
        default=None,
        serialization_alias="gateinput4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi4"},
    )
    gateinput5: str | None = Field(
        default=None,
        serialization_alias="gateinput5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi5"},
    )
    gateinput6: str | None = Field(
        default=None,
        serialization_alias="gateinput6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi6"},
    )
    gateinput7: str | None = Field(
        default=None,
        serialization_alias="gateinput7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi7"},
    )
    gateinput8: str | None = Field(
        default=None,
        serialization_alias="gateinput8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi8"},
    )
    gateinput9: str | None = Field(
        default=None,
        serialization_alias="gateinput9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi9"},
    )
    gateinput10: str | None = Field(
        default=None,
        serialization_alias="gateinput10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi10"},
    )
    gateinput11: str | None = Field(
        default=None,
        serialization_alias="gateinput11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi11"},
    )
    gateinput12: str | None = Field(
        default=None,
        serialization_alias="gateinput12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi12"},
    )
    gateinput13: str | None = Field(
        default=None,
        serialization_alias="gateinput13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi13"},
    )
    gateinput14: str | None = Field(
        default=None,
        serialization_alias="gateinput14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi14"},
    )
    gateinput15: str | None = Field(
        default=None,
        serialization_alias="gateinput15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi15"},
    )
    gateinput16: str | None = Field(
        default=None,
        serialization_alias="gateinput16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "gi16"},
    )
    roundrobin: str | None = Field(
        default=None,
        serialization_alias="roundrobin",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "rr"},
    )
    voiceallocation: str | None = Field(
        default=None,
        serialization_alias="voiceallocation",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "va"},
    )
    pitchoutput1: str | None = Field(
        default=None,
        serialization_alias="pitchoutput1",
        json_schema_extra={"essential": 2, "type": "any", "shortname": "po1"},
    )
    pitchoutput2: str | None = Field(
        default=None,
        serialization_alias="pitchoutput2",
        json_schema_extra={"essential": 2, "type": "any", "shortname": "po2"},
    )
    pitchoutput3: str | None = Field(
        default=None,
        serialization_alias="pitchoutput3",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po3"},
    )
    pitchoutput4: str | None = Field(
        default=None,
        serialization_alias="pitchoutput4",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po4"},
    )
    pitchoutput5: str | None = Field(
        default=None,
        serialization_alias="pitchoutput5",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po5"},
    )
    pitchoutput6: str | None = Field(
        default=None,
        serialization_alias="pitchoutput6",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po6"},
    )
    pitchoutput7: str | None = Field(
        default=None,
        serialization_alias="pitchoutput7",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po7"},
    )
    pitchoutput8: str | None = Field(
        default=None,
        serialization_alias="pitchoutput8",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po8"},
    )
    pitchoutput9: str | None = Field(
        default=None,
        serialization_alias="pitchoutput9",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po9"},
    )
    pitchoutput10: str | None = Field(
        default=None,
        serialization_alias="pitchoutput10",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po10"},
    )
    pitchoutput11: str | None = Field(
        default=None,
        serialization_alias="pitchoutput11",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po11"},
    )
    pitchoutput12: str | None = Field(
        default=None,
        serialization_alias="pitchoutput12",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po12"},
    )
    pitchoutput13: str | None = Field(
        default=None,
        serialization_alias="pitchoutput13",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po13"},
    )
    pitchoutput14: str | None = Field(
        default=None,
        serialization_alias="pitchoutput14",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po14"},
    )
    pitchoutput15: str | None = Field(
        default=None,
        serialization_alias="pitchoutput15",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po15"},
    )
    pitchoutput16: str | None = Field(
        default=None,
        serialization_alias="pitchoutput16",
        json_schema_extra={"essential": 0, "type": "any", "shortname": "po16"},
    )
    gateoutput1: str | None = Field(
        default=None,
        serialization_alias="gateoutput1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "go1"},
    )
    gateoutput2: str | None = Field(
        default=None,
        serialization_alias="gateoutput2",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "go2"},
    )
    gateoutput3: str | None = Field(
        default=None,
        serialization_alias="gateoutput3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go3"},
    )
    gateoutput4: str | None = Field(
        default=None,
        serialization_alias="gateoutput4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go4"},
    )
    gateoutput5: str | None = Field(
        default=None,
        serialization_alias="gateoutput5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go5"},
    )
    gateoutput6: str | None = Field(
        default=None,
        serialization_alias="gateoutput6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go6"},
    )
    gateoutput7: str | None = Field(
        default=None,
        serialization_alias="gateoutput7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go7"},
    )
    gateoutput8: str | None = Field(
        default=None,
        serialization_alias="gateoutput8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go8"},
    )
    gateoutput9: str | None = Field(
        default=None,
        serialization_alias="gateoutput9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go9"},
    )
    gateoutput10: str | None = Field(
        default=None,
        serialization_alias="gateoutput10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go10"},
    )
    gateoutput11: str | None = Field(
        default=None,
        serialization_alias="gateoutput11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go11"},
    )
    gateoutput12: str | None = Field(
        default=None,
        serialization_alias="gateoutput12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go12"},
    )
    gateoutput13: str | None = Field(
        default=None,
        serialization_alias="gateoutput13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go13"},
    )
    gateoutput14: str | None = Field(
        default=None,
        serialization_alias="gateoutput14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go14"},
    )
    gateoutput15: str | None = Field(
        default=None,
        serialization_alias="gateoutput15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go15"},
    )
    gateoutput16: str | None = Field(
        default=None,
        serialization_alias="gateoutput16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "go16"},
    )


class Sequencer(DroidCircuit):
    """ Simple eight step sequencer

    Args:
        clock (trigger):
          Each trigger into this jack advances the sequence by one step.
        reset (trigger):
          A trigger here resets the sequence to the first step
        stages (integer):
          Number of inputs of pitch.., gate.., slew.., cv and repeats that should be
          used. If you set stages to a number higher than the number of used inputs, all
          inputs will be used. If you omit this parameter, all used inputs will be used.
        steps (integer):
          With this input you can force the sequencer to begin from start after a
          certain number of clock cycles. If you omit the parameter or if it is set to
          0, the sequencer will play all stages with all repeats until it resets to the
          beginning.
        transpose (cv):
          This voltage is added to the pitch output.
        outputscaling (cv):
          The output pitch is multiplied by this parameter.
        gatelength (fraction):
          The length of the output gates. If it is unpatched, the original input clock
          is fed through 1:1 (with its own duty cycle). When used, it is a ratio from
          0.0 to 1.0 and relative to the cycle of the input clock. Setting the
          gatelength to 1.0 merges two adjacent gates together since there is not time
          left for a low gate before the next step begins.
        pitch1 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch2 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch3 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch4 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch5 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch6 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch7 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        pitch8 (cv):
          These are the pitches of the various steps. You can put fixed numbers here but
          also of course pots or variable inputs. Note: The number of used input jacks
          defines the length of the sequence, unless you override that with stages.
        cv1 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv2 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv3 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv4 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv5 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv6 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv7 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        cv8 (cv):
          Each step has an optional CV assigned. You can use that CV for modulating
          something or even outputting a second pitch information.
        gate1 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate2 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate3 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate4 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate5 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate6 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate7 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        gate8 (gate):
          The gate inputs should be 0 (off) or 1 (on). For stages with a 0-gate no
          output gate is produced and the pitch information is kept at the previous
          state. Unpatched gates are considered to be on!
        slew1 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew2 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew3 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew4 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew5 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew6 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew7 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        slew8 (cv):
          Enables slew limiting for that stage. The input is not binary but you can set
          the amount of slew here – individually for each step. 0.0 switches the slew
          off, higher values create slower slews.
        repeat1 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat2 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat3 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat4 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat5 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat6 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat7 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        repeat8 (cv):
          Set this to a positive integer number like 1, 2, and so on. It sets the number
          of times this stage should be repeated until the next stage will be
          approached. It is currently not allowed to have 0 repeats – although this
          would make sense in a future version.
        chaintonext (gate):
          If you set this input to 1, the next sequencer circuit's pitch and other step
          inputs will be added to this sequencer. See the general circuit notes for
          details.
        pitchoutput (cv):
          The pitch output. It is unquantized.
        cvoutput (cv):
          The optional CV output, in case you use the cv1 ... cv8 inputs.
        gateoutput (gate):
          The gate output.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 168

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
    stages: str | None = Field(
        default=None,
        serialization_alias="stages",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "sg"},
    )
    steps: str | None = Field(
        default=None,
        serialization_alias="steps",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "s"},
    )
    transpose: str | None = Field(
        default=None,
        serialization_alias="transpose",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "tr"},
    )
    outputscaling: str | None = Field(
        default=None,
        serialization_alias="outputscaling",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "os"},
    )
    gatelength: str | None = Field(
        default=None,
        serialization_alias="gatelength",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "gl"},
    )
    pitch1: str | None = Field(
        default=None,
        serialization_alias="pitch1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p1"},
    )
    pitch2: str | None = Field(
        default=None,
        serialization_alias="pitch2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p2"},
    )
    pitch3: str | None = Field(
        default=None,
        serialization_alias="pitch3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p3"},
    )
    pitch4: str | None = Field(
        default=None,
        serialization_alias="pitch4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p4"},
    )
    pitch5: str | None = Field(
        default=None,
        serialization_alias="pitch5",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p5"},
    )
    pitch6: str | None = Field(
        default=None,
        serialization_alias="pitch6",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p6"},
    )
    pitch7: str | None = Field(
        default=None,
        serialization_alias="pitch7",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p7"},
    )
    pitch8: str | None = Field(
        default=None,
        serialization_alias="pitch8",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "p8"},
    )
    cv1: str | None = Field(
        default=None,
        serialization_alias="cv1",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "1"},
    )
    cv2: str | None = Field(
        default=None,
        serialization_alias="cv2",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "2"},
    )
    cv3: str | None = Field(
        default=None,
        serialization_alias="cv3",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "3"},
    )
    cv4: str | None = Field(
        default=None,
        serialization_alias="cv4",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "4"},
    )
    cv5: str | None = Field(
        default=None,
        serialization_alias="cv5",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "5"},
    )
    cv6: str | None = Field(
        default=None,
        serialization_alias="cv6",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "6"},
    )
    cv7: str | None = Field(
        default=None,
        serialization_alias="cv7",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "7"},
    )
    cv8: str | None = Field(
        default=None,
        serialization_alias="cv8",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "8"},
    )
    gate1: str | None = Field(
        default=None,
        serialization_alias="gate1",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g1"},
    )
    gate2: str | None = Field(
        default=None,
        serialization_alias="gate2",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g2"},
    )
    gate3: str | None = Field(
        default=None,
        serialization_alias="gate3",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g3"},
    )
    gate4: str | None = Field(
        default=None,
        serialization_alias="gate4",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g4"},
    )
    gate5: str | None = Field(
        default=None,
        serialization_alias="gate5",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g5"},
    )
    gate6: str | None = Field(
        default=None,
        serialization_alias="gate6",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g6"},
    )
    gate7: str | None = Field(
        default=None,
        serialization_alias="gate7",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g7"},
    )
    gate8: str | None = Field(
        default=None,
        serialization_alias="gate8",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "g8"},
    )
    slew1: str | None = Field(
        default=None,
        serialization_alias="slew1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw1"},
    )
    slew2: str | None = Field(
        default=None,
        serialization_alias="slew2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw2"},
    )
    slew3: str | None = Field(
        default=None,
        serialization_alias="slew3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw3"},
    )
    slew4: str | None = Field(
        default=None,
        serialization_alias="slew4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw4"},
    )
    slew5: str | None = Field(
        default=None,
        serialization_alias="slew5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw5"},
    )
    slew6: str | None = Field(
        default=None,
        serialization_alias="slew6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw6"},
    )
    slew7: str | None = Field(
        default=None,
        serialization_alias="slew7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw7"},
    )
    slew8: str | None = Field(
        default=None,
        serialization_alias="slew8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sw8"},
    )
    repeat1: str | None = Field(
        default=None,
        serialization_alias="repeat1",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp1"},
    )
    repeat2: str | None = Field(
        default=None,
        serialization_alias="repeat2",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp2"},
    )
    repeat3: str | None = Field(
        default=None,
        serialization_alias="repeat3",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp3"},
    )
    repeat4: str | None = Field(
        default=None,
        serialization_alias="repeat4",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp4"},
    )
    repeat5: str | None = Field(
        default=None,
        serialization_alias="repeat5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp5"},
    )
    repeat6: str | None = Field(
        default=None,
        serialization_alias="repeat6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp6"},
    )
    repeat7: str | None = Field(
        default=None,
        serialization_alias="repeat7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp7"},
    )
    repeat8: str | None = Field(
        default=None,
        serialization_alias="repeat8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rp8"},
    )
    chaintonext: str | None = Field(
        default=None,
        serialization_alias="chaintonext",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "cn"},
    )
    pitchoutput: str | None = Field(
        default=None,
        serialization_alias="pitchoutput",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "po"},
    )
    cvoutput: str | None = Field(
        default=None,
        serialization_alias="cvoutput",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "co"},
    )
    gateoutput: str | None = Field(
        default=None,
        serialization_alias="gateoutput",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "go"},
    )

