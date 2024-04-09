"""DROID circuits. These circuits are auto-generated from circuits.json."""

from dataclasses import dataclass
from typing import Optional



@dataclass
class Adc:
    """Circuit adc.
      AD Converter with 12 bits

    Inputs:
        input: cv
            Input signal to convert to binary representation.

        minimum: cv
            The lowest assumed input value. This value and all lower
            values will be converted to the bit sequence 000000000000.

        maximum: cv
            The highest assumed input value. This value and all higher
            values will be converted to the bit sequence 111111111111.


    Outputs:
        bit1: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit2: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit3: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit4: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit5: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit6: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit7: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit8: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit9: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit10: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit11: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

        bit12: gate
            The 12 bit outputs. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest output that
            you actually patch. If you do not need the full resolution of
            12 bits, simply just use the first couple of outputs.

    """


    input: Optional[str] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    bit1: Optional[str] = None
    bit2: Optional[str] = None
    bit3: Optional[str] = None
    bit4: Optional[str] = None
    bit5: Optional[str] = None
    bit6: Optional[str] = None
    bit7: Optional[str] = None
    bit8: Optional[str] = None
    bit9: Optional[str] = None
    bit10: Optional[str] = None
    bit11: Optional[str] = None
    bit12: Optional[str] = None


@dataclass
class Algoquencer:
    """Circuit algoquencer.
      Algorithmic sequencer

    Inputs:
        clock: trigger
            Clock input. This is mandatory. For each clock pulse the sequencer
            is advanced by one step.

        reset: trigger
            Reset input. A trigger here switches back to step 1.

        button1: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button2: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button3: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button4: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button5: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button6: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button7: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button8: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button9: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button10: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button11: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button12: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button13: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button14: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button15: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        button16: gate
            1 ... 16 step button. Assign these buttons to
            buttons on your controllers.

        length: integer
            Sets the length of the pattern. Note: if you use
            lengthbutton, this input is ignored as soon as the
            length button has been used for the first time. If you have assigned at
            least one button, the default value of length is the number
            of buttons you have assigned. Otherwise it defaults to 16.
            The maximum length is 64. Any larger number will be truncated
            to 64.

        pattern: integer
            Selects a pattern of pseudo random values. If you set dejavu
            to 1, all “random” decision are deterministic and repeat again
            and again. If you do not like these choices, you can choose a
            different pattern, just by setting this input to any integer number
            you like. The default pattern is 0. If you patch a pot here, simply
            multiply it by the number of different patterns you want to select,
            e.g. pattern = P1.1 * 10. This will allow you to select one of
            the pattern 0, 1, ... 10.

            Note: If you use pattern, the trigger inputs nextpattern,
            prevpattern and reroll are ignored.

        nextpattern: trigger
            Switches forward to the next pseudo random pattern.

        prevpattern: trigger
            Switches back to the previous pseudo random pattern.

        reroll: trigger
            Select one of the pseudo random patterns completely by random.

        clearpage: trigger
            A trigger here unselects all step buttons in the currently active page
            (normal, alternate, accent).

        pitchlow: cv
            This set a lower voltage boundary for the pitch output for
            notes that are randomized.

        pitchhigh: cv
            This set an upper voltage boundary for the pitch output for
            notes that are randomized.

        pitchresolution: integer
            If this is non-zero, it make the pitch output adopt that number of
            possible discrete values. E.g. if you set it to 2, only the values
            set by pitchlow and pitchhigh are possible. A value of 3 will
            allow an additional value in the middle, and so on.

        gatelength: cv
            The gate length in input clock cycles. A value of 0.5 (5 V)
            thus means half a clock cycle. A steady input clock is needed for
            this to work. Please note that if the gate length is >= 1.0,
            two succeeding notes will get a steady gate, which
            essentially means legato.

            When playing rolls, i.e. more than one beat per step, the
            gate length is divided by the number of rolls. That way the gates
            get shorter and even at a gatelength close to 1.0 the gates
            are still audible and do not merge together.

        lengthbutton: gate
            Map this to a button like B1.1. While you press and hold
            this button the sequencer switches to change length mode. While
            in this mode a press of one of the step buttons will change the length
            of the pattern. Also while in this mode the LEDs of the step buttons will
            show the current length. If you do not like to hold the button but
            switch it on and off, you can create a toggle button with [button] and
            send its output here.

        repeats: integer
            Usually one bar has the length of one pattern. Setting this to 2
            will consider one bar as a run of two times through the pattern. So
            if you have 8 buttons and bars = 2, one bar will be 16
            steps, where the 1 and 9 step are set by button1,
            2 and 10 by button2 and so on.

            Why should that be useful? Well – the difference shows up when you
            use fills, or branches or work with the alternate
            pattern. These three algorithms work based on bars. And repeats = 2 makes one bar have 16 steps, even if you just have
            eight buttons.

        alternaterepeats: integer
            If you are use using repeats and alternatebars / alternatebutton
            at the same time, with this input you can specify a different
            value for repeats when it comes to selecting the alternate button
            page.

            Assume you have eight buttons and repeats = 2 and
            alternatebars = 2. Then Algoquencer will play two times your
            8-step pattern normally and two times alternated (since two times
            the 8 steps form one bar). This results in a form of A A B B.

            If you want your form rather to be A B A B, set alternaterepeats
            = 1. This way, when it comes to alteration, the length of one bar
            is just normal length (8 steps here).

        branches: integer
            Enables the branching feature (sometimes also called fractal sequencing.
            When branches = 1, then every second bar will be using other
            random values – giving a sequence of the bars
            [5mm][c]A
            [5mm][c]B.

            With branches = 2 you get a sequence of the form
            [5mm][c]A
            [5mm][c]B
            [5mm][c]A
            [5mm][c]C.

            A value of 3 creates an even longer sequence that repeats itself
            after eight bars:
            [5mm][c]A
            [5mm][c]B
            [5mm][c]A
            [5mm][c]C
            [5mm][c]A
            [5mm][c]B
            [5mm][c]A
            [5mm][c]D.

            Note: this only takes effect when you set dejavu >0. The largest
            effect is when it is set to 1. And the you need to use either
            variation or set activity to a value greater than 0.5.
            Because otherwise Algoquencer will strictly play the gates that you've set
            with your buttons and then every bar will be the same, of course.

        mutebutton: trigger
            Wire this to a button like B1.2. When you press the
            button once, all triggers are muted. Pressing again unmutes
            them. So this behaves like a toggle [button] in itself.
            You probably want to wire muteled to the LED in that button,
            e.g. L1.2. It show the mute state. The mute button works
            together with the unmute button (see below). Note: even if you
            use the select jack in order to overlay your buttons with
            several algoquencers, the mutebutton will always be active.
            The idea is to always have direct access to this button.

        unmutebutton: trigger
            A trigger to this jack resets the mute button exactly
            at the beginning of the next bar. While waiting for that
            to happen, the output unmuteled will blink. Wire this
            to the LED in the button. Note: even if you
            use the select jack in order to overlay your buttons with
            several algoquencers, the mutebutton will always be active.
            The idea is to always have direct access to this button.

        accentbutton: gate
            While this input is high you are in accent editing mode. This
            is very similar to the mode where you set the length. But now for
            each step you edit whether this step is outputting an accent when
            triggered. You might want to use a toggle button for this function, so
            you can operate without holding down the button all the time.

        alternatebutton: gate
            If this input is high, you are in alternate editing mode.
            Every Algoquencer has an alternate set of steps. Each step
            that is currenty activated toggles the state of the normal step,
            but only for each even bar. This allows to introduce variations
            of the pattern that occur every second bar.

        alternatebars: integer
            With this input you can change the influence of the
            alternatebutton. Per default the pattern alternation is
            done every second bar. You can change this to any number you
            like with this input. Values less than 1 will be considered
            as one – which means that every bar is alternated.

        accentlow: cv
            This value is output at accent when a note without an
            accent is being triggered or when no note is triggered at all.

        accenthigh: cv
            This value is output at accent while a note with an
            accent is triggered. The value will be kept for the full time
            of the clock cycle.

        activity: bipolar
            This is the most important parameter and  you will probably
            wire it to a pot like P1.1. The activity controls, how
            “busy” the sequencer is playing, or in other words how often
            a step gets an active gate (und thus a changing output pitch).

            Let's first assume that variation
            is set to 0.0 (which is the default). Then at a value of
            0.5 (or pot at 12'clock) Algoquencer will exactly play that
            pattern that you have set with the step buttons. Turning the knob
            CCW will remove more and more beats from the pattern until it is
            completely silent at a value of 0.0 (or pot fully
            CCW). But if you turn up the knob above the middle position then more
            and more additional beats will be placed into you pattern in
            a random way until – at 1.0 – a trigger will happen at
            every beat.

            Note: If you do not use step buttons, this parameter
            behaves slightly different: A value of 0.5 then means an
            activity of 50%, which means that exactly the half of the steps
            will get an event. This is different from a situation where you
            have defined buttons but all are deselected. In that case
            0.5 means that exactly the number of beats of your pattern
            are being played, which is zero in that case.

        variation: fraction
            The variation controls how strictly Algoquencer will stick
            to the pattern that you have set with your step buttons. You probably
            want to wire this to a knob. A value of 0.0 (or the knob
            fully CCW) will allow no variations. Your pattern will be played exactly
            as it is. If the activity goes beyond 0.5, additional
            beats will be placed, of course. And these are random.

            If you increase the variation, more and more beats of your
            pattern are being replaced with other beats – while keeping the
            total number of beats the same. If you set variation to
            1.0 (or the pot fully CW) then your pattern is completely
            ignored except for the actual number of beats it contains.

        dejavu: fraction
            The dejavu parameter controls what random should mean.
            If dejavu = 0.0, then all random decisions are completely
            chaotic – and every time a decision is taken the dice are being
            rolled again.

            At dejavu = 1.0 on the other hand – once a random decision
            has been taken for a certain step in a certain bar, it will stay
            always the same from now on. This will lead to repeating exactly
            the pattern bars over and over again. We sometimes call this random
            to be “deterministic”.

            Any position in between will choose some of the steps as chaotic
            random and some of the steps as deterministic.

        morphs: fraction
            This parameter will introduce changes in formerly taken
            random decisions from time to time.
            If you set it above zero, at every start of a bar some
            of the deterministic random decisions will be remade. Setting
            morphs = 1 will essentially disable dejavu, since all
            decisions are redone every bar anyway then.

            If you know the Turing Machine: In principle that has the same idea,
            but Algoquencer has a few improvements:



              * The number of random changes is exactly controlled by the setting.
            At each specific setting of morphs the same number of
            changes will be done at each bar.

              * Changes only appear at the beginning of each bar. If
            you use branches, they will appear whenever you sequence
            is over.

              * Small settings will introduce just one morph each 64 step.


        offbeats: bipolar
            Whenever random beats are being placed then this setting controlls
            whether downbeats or offbeats should be preferred. At at
            setting of 0.5 there will be no difference. If you increase the
            value then more and more offbeats will appear. Offbeats are steps with
            an even number, like 2, 4, 6 and so on. Value smaller than
            0.5 will prefer downbeats.

            Offbeats sound more “complex” and downbeats more simple or
            “down to earth”.

        distribution: bipolar
            This is very similar to offbeats, but this time you decide
            whether beats should be placed rather in the first half of the bar
            or in the second half.

        fills: fraction
            When this parameter is set above 0.0, additional
            beats will be placed in order to make the beat more “active”. This
            happens at musically useful times controlled by fillorder (see
            below). The additional beats within the bar are placed in a way that
            prefers the end of the bar. If there are already too many beats in the
            bar then the fill will remove or change some instead.

        fillorder: integer
            This integer number controls how fills are being placed:

            0every bar
            1every second bar
            2small fill in bar 2, big fill in bar 4
            3tiny fill in bar 2 and 6, medium fill in bar 4, big fill in bar 8




        rolls: fraction
            This parameter controls if drum rolls (or ratchets as you might
            call it) are being created. At 0.0 no rolls are being created.
            At 1.0 every beat will be converted into a roll. Rolls
            always happen before the actual beat, they lead to it. If you
            using this feature for snare rolls you might want to use the
            output rollvelocity for controlling the snare volume.

        rollcount: integer
            Number of additional beats for playing the roll. Setting
            rollcount = 0 would disable rolls. All these beats are
            distributed in the clock tick before the beat the roll is
            leading to. The first beat of the roll is exactly one tick before
            that beat – or more if you increase rollsteps.

        rollsteps: integer
            Length of the roll in clock ticks (steps). The total number
            of additional beats is thus rollcount × rollsteps

        rollstartvelo: cv
            Rolls can be played with an increasing velocity. This first
            beat starts with the velocity set with this parameter. Then
            every beat gets a bit louder until the last beat is played with
            velocity 1.0. The velocity for rolls is output at the jack
            rollvelocity.

        pitch1: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch2: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch3: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch4: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch5: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch6: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch7: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch8: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch9: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch10: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch11: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch12: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch13: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch14: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch15: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        pitch16: cv
            You can use these inputs, if you want the pitches of the pitch
            output play a certain melody. That way the Algoquencer behaves like
            a normal melody sequencer – but all the algorithmic parameters will
            be applied. For example variation will also be applied to these
            notes. Note: If length is larger than 16, these pitch inputs
            will be cycled through, so step 17 uses pitch1, step 18 uses
            pitch2 and so on.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        trigger: trigger
            Here comes the trigger output. Patch this to the trigger input
            of your drum or synth voice.

        gate: gate
            The gate output is alternative to the trigger and has a variable
            length. It is useful when Algoquencer is used for creating melodies.
            Patch the gate input of an envelope or something similar here.

        pitch: stepped
            Outputs the (pseudo-)random voltage (unquantized) at each step
            with an active gate. This honors all the settings that control the randomness
            and variation, like dejavu, variation, fills and branches.

        accent: cv
            Whenever a beat with an accent is being played, the value
            set by accenthigh is sent here, otherwise accentlow.
            If you are wiring this to one of the jacks of the G8 expander
            then that will output just 0V and 5V of course.

        led1: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led2: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led3: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led4: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led5: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led6: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led7: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led8: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led9: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led10: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led11: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led12: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led13: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led14: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led15: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        led16: stepped
            1 ... 16 LEDs of the step buttons. Assign these
            to the LEDs in the step buttons.

        barled1: gate
            Patch these output to some LEDs in order to show you the
            current bar in the sequence.

        barled2: gate
            Patch these output to some LEDs in order to show you the
            current bar in the sequence.

        barled3: gate
            Patch these output to some LEDs in order to show you the
            current bar in the sequence.

        barled4: gate
            Patch these output to some LEDs in order to show you the
            current bar in the sequence.

        rollvelocity: cv
            If you enable rolls, then the velocity of the roll beats
            will be output here. For normal beats this will always be 1.0.

        startofbar: trigger
            At the beginning of every bar a trigger is output here.

        muteled: gate
            Wire this to the LED in your mute button. It will then be lit
            while the voice is muted.

        unmuteled: gate
            Wire this to the LED in your unmute button (if used). It will
            blink while the unmute is waiting for the start of the next bar.

        morphled: gate
            This output will get a trigger every time a morph happens. It
            is intended to be wired to an LED.

        fillsled: gate
            This output will get a trigger every time a fill beat is being
            played. Wire this to some LED if you like.

        branch: integer
            This output will output the current branch number, e.g. 1, 2, 3 and
            so on. If you do not use branches then it is always 1.

        lengthoutput: integer
            Outputs the currently selected length. This is useful if you are
            using the lengthbutton for interactively changing the length
            of the pattern and want to share that setting with other circuits.

    """


    clock: Optional[str] = None
    reset: Optional[str] = None
    button1: Optional[str] = None
    button2: Optional[str] = None
    button3: Optional[str] = None
    button4: Optional[str] = None
    button5: Optional[str] = None
    button6: Optional[str] = None
    button7: Optional[str] = None
    button8: Optional[str] = None
    button9: Optional[str] = None
    button10: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    button13: Optional[str] = None
    button14: Optional[str] = None
    button15: Optional[str] = None
    button16: Optional[str] = None
    length: Optional[str] = None
    pattern: Optional[str] = None
    nextpattern: Optional[str] = None
    prevpattern: Optional[str] = None
    reroll: Optional[str] = None
    clearpage: Optional[str] = None
    pitchlow: Optional[str] = None
    pitchhigh: Optional[str] = None
    pitchresolution: Optional[str] = None
    gatelength: Optional[str] = None
    lengthbutton: Optional[str] = None
    repeats: Optional[str] = None
    alternaterepeats: Optional[str] = None
    branches: Optional[str] = None
    mutebutton: Optional[str] = None
    unmutebutton: Optional[str] = None
    accentbutton: Optional[str] = None
    alternatebutton: Optional[str] = None
    alternatebars: Optional[str] = None
    accentlow: Optional[str] = None
    accenthigh: Optional[str] = None
    activity: Optional[str] = None
    variation: Optional[str] = None
    dejavu: Optional[str] = None
    morphs: Optional[str] = None
    offbeats: Optional[str] = None
    distribution: Optional[str] = None
    fills: Optional[str] = None
    fillorder: Optional[str] = None
    rolls: Optional[str] = None
    rollcount: Optional[str] = None
    rollsteps: Optional[str] = None
    rollstartvelo: Optional[str] = None
    pitch1: Optional[str] = None
    pitch2: Optional[str] = None
    pitch3: Optional[str] = None
    pitch4: Optional[str] = None
    pitch5: Optional[str] = None
    pitch6: Optional[str] = None
    pitch7: Optional[str] = None
    pitch8: Optional[str] = None
    pitch9: Optional[str] = None
    pitch10: Optional[str] = None
    pitch11: Optional[str] = None
    pitch12: Optional[str] = None
    pitch13: Optional[str] = None
    pitch14: Optional[str] = None
    pitch15: Optional[str] = None
    pitch16: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    trigger: Optional[str] = None
    gate: Optional[str] = None
    pitch: Optional[str] = None
    accent: Optional[str] = None
    led1: Optional[str] = None
    led2: Optional[str] = None
    led3: Optional[str] = None
    led4: Optional[str] = None
    led5: Optional[str] = None
    led6: Optional[str] = None
    led7: Optional[str] = None
    led8: Optional[str] = None
    led9: Optional[str] = None
    led10: Optional[str] = None
    led11: Optional[str] = None
    led12: Optional[str] = None
    led13: Optional[str] = None
    led14: Optional[str] = None
    led15: Optional[str] = None
    led16: Optional[str] = None
    barled1: Optional[str] = None
    barled2: Optional[str] = None
    barled3: Optional[str] = None
    barled4: Optional[str] = None
    rollvelocity: Optional[str] = None
    startofbar: Optional[str] = None
    muteled: Optional[str] = None
    unmuteled: Optional[str] = None
    morphled: Optional[str] = None
    fillsled: Optional[str] = None
    branch: Optional[str] = None
    lengthoutput: Optional[str] = None


@dataclass
class Arpeggio:
    """Circuit arpeggio.
      Arpeggiator – pattern based melody generator

    Inputs:
        pitch: voltperoctave
            Sets the base pitch of the arpeggio. The first note of the
            pattern will be the nearest selected note just above that pitch.

        range: voltperoctave
            Selects the range between the lowest and highest note of the
            arpeggio. A range of 0 means that there is just one single note
            possible and the arpeggio will stick to that note. A value of
            1 V (or 0.1) means that the arpeggio will run over one octave.
            The maximum allowed range is 0.8 (8 octaves). Higher values will be
            capped to that.

        clock: trigger
            This input is vital: each trigger here make the arpeggio
            move forward by one step and adapt the pitch output. Without
            a clock the arpeggio will do nothing but stick to the same
            note all the time.

        reset: trigger
            Resets the arpeggio to the first step of the current pattern.

        pattern: integer
            Selects one of a list of arpeggio pattern. The following
            patterns are available:

             0step forward through the allowed notes→
            1two steps forward, one step backward→ → ←
            2double step forward, one step backward⇒ ←
            3double step forward, double step backward, single step forward⇒ ⇐  →
            4double step forward, single step forward, double step backward, single step forward⇒ → ⇐ →
            5random single step forward or backward↔
            6random jump to any allowed (other) note⇕




        direction: gate
            Sets the general direction in which the pattern moves.
            0 means upwards and 1 means downwards.

        pingpong: gate
            If set to 1, the pattern will reverse its direction
            once it has reached the end of the range. Otherwise it restarts
            from the beginning. So enabling pingpong is a bit like a triangle
            wave, whereas otherwise it's more like a sawtooth.

        butterfly: gate
            If set to 1, every second note in the range of selected
            notes will be mirrored. So for example you have selected the notes
            1 - 10, the new order will be 1, 10, 2, 9, 3, 8, 4, 7, 5, 6

        drop: integer
            Selects a scheme of skipping some of the allowed scale notes.
            Four different values are allowed:

             0Do not skip any notes202 203 204 205 206 207
            1Skip every second selected note202 193 204 195 206 197
            2Skip every third selected note202 203 194 205 206 197
            3Skip the 2 and 3 note of each group of three202 193 194 205 196 197




        octaves: gate
            When this is set to 1 or 2, each note will be followed
            by the same note one octave up (for 1) or down (for 2)
            respectively. These additional octave notes are in addition to the
            selected range.

             0Don't play octaves
            1Each note is followed by the same note one octave up
            2Each note is followed by the same note one octave down




        startnote: integer
            When startnote is set to non-zero, it will force the pattern
            to begin with a certain scale note regardless of the current note
            selection. 1 will select the first note of the scale (root),
            2 the second and so on until 7, which selects the 7
            as start note.

            Using startnote effectively reduces the range of notes.
            Instead of the the full range of pitch … pitch +
            range a reduced range is played, since some of the lower
            notes are skipped, if the direction is upwards, and some
            of the upper notes, if the direction is downwards.

            The start note is used in all situations where the pattern is
            reset to its beginning. This is after an external reset or
            if the pattern has reached the end of the range. Note: If you have
            set pingpong = 1, the pattern is never reset by itself,
            so startnote is just used after an external reset, here.

            Don't mess up the start note with the lowest note in
            the arpeggio. If want to control the lowest note, used pitch
            instead of startnote. Sometimes this has a similar effect,
            but not always.

        autoreset: integer
            When autoreset a non-zero number, the arpeggio melody will
            be reset to the start after that number of clock ticks. For example
            if you set autoreset = 5, and the pattern would play 7 notes
            until it loops back to its start, after the 5 step a restart
            is forced. That's also true if the pattern is shorter.
            If autoreset = 5 and the melody already loops after 3 steps,
            it is played once in full (3 steps) and once just the first 2 steps,
            since then the auto reset happens.

            A trigger to reset makes autoreset set it's internal
            counter to 0.

            Autoreset gives you direct control over the rhythmic feel that
            your arpeggio melodies have.

        root: integer
            Set the root note here. 0 means C, 1 means
            C♯, 2 means D and so on. If you multiply
            the value of an input like I1 with 120, then you can use a 1V/Oct
            input for selecting the root note via a sequencer, MIDI keyboard
            or the like.
            Also then you are compatible with the ROOT CV input of the Sinfonion.

             0C
            1C♯
            2D
            3D♯
            4E
            5F
            6F♯
            7G
            8G♯
            9A
            10A♯
            11B
            12C




        degree: integer
            Set the musical scale. This is a number from 0 to 107.
            Below are the first 12 and most important scales. You find a list
            of all 108 scales on page 105.

             0lyd – Lydian major scale (it has a ♯ 4)
            1maj – Normal major scale (ionian)
            2X^7 – Mixolydian (dominant seven chords)
            3sus – mixolydian with 3/4 swapped
            4alt – Altered scale
            5hm^5 – Harmonic minor scale from the 5
            6dor – Dorian minor (minor with ♯ 13)
            7min – Natural minor (aeolian)
            8hm – Harmonic minor (♭ 6 but ♯ 7)
            9phr – Phrygian minor scale (with ♭ 9)
            10dim – Diminished scale (whole/half tone)
            11aug – Augmented scale (just whole tones)


            Note: Alltogether there are 108 scales. Please see page 105 for a complete list

        select1: gate
            Gate input for selecting the root note as being an
            allowed interval. When you want to create a playing interface
            for live operation you can patch the output of a toggle button
            (made with the circuit [button]) here.

            Note: When all select and selectfill inputs are 0,
            automatically all seven scale notes are selected, i.e.
            select1 ... select13 will be set to one.

        select3: gate
            Gate input for selecting the 3.

        select5: gate
            Gate input for selecting the 5.

        select7: gate
            Gate input for selecting the 7.

        select9: gate
            Gate input for selecting the 9 (which is the same
            as the 2).

        select11: gate
            Gate input for selecting the 11 (which is the same
            as the 4).

        select13: gate
            Gate input for selecting the 13 (which is the same
            as the 6).

        selectfill1: gate
            Selects the alternative 9 (i.e.
            the 9 that is not in the scale.

        selectfill2: gate
            Selects the alternative 3 (i.e.
            the 3 that is not in the scale).

        selectfill3: gate
            Selects the alternative 4 or 5. In
            most cases this is the diminished 5.

        selectfill4: gate
            Selects the alternative 13 (i.e.
            the 13 that is not in the scale).

        selectfill5: gate
            Selects the alternative 7 (i.e.
            the 7 that is not in the scale).

        harmonicshift: integer
            This input can reduce harmonic complexity by disabling some of
            the scale or non-scale notes. It is an idea first found in the
            Sinfonion and also provided by the circuit sinfonionlink.

            harmonicshift is staged after the select... inputs
            and further filters out (disables) notes based on their relation
            to the current scale. This means that first the 12 select... inputs
            select a subset of the 12 possible notes. After that harmonicshift
            can reduce this set further (it will never add notes).

            If harmonicshift is not zero, depending on its value some or
            more of the scale notes are disabled, even if they would be allowed by
            select....  Or in other words: the harmonic material is reduced.

            You also can use negative values. These create rather strange sounds
            by removing the simple chord functions instead of the complex
            ones first.

            Here are the possible values:

             0off – all selected notes are allowed
            1disable all fill notes (non-scale notes)
            2disable fills and 11
            3disable fills, 11 and 13
            4disable fills, 11, 13 and 9
            5disable fills, 11, 13, 9 and 7
            6disable fills, 11, 13, 9, 7 and 3
            7disable fills, 11, 13, 9, 7, 3 and 5
            -1disable the root note
            -2disable the root note and the 5
            -3disable root, 3, 5
            -4disable root, 3, 5, 7
            -5disable root, 3, 5, 7, 9
            -6disable root, 3, 5, 7, 9 and 13
            -7disable all scale notes (fill notes untouched)




        noteshift: integer
            Shifts the resulting output note(s) by this
            number of scale notes up or down (if negative). So the output
            note still is part of the scale but may be a note that is none
            of the selected ones. The maximum shift range is limited to
            -24 … +24.

        selectnoteshift: integer
            Shifts the output note by this
            number of selected scale notes up or down (if negative).
            If you use noteshift at the same time, first selectnoteshift is applied, then noteshift. The maximum shift range
            is limited to -24 … +24.

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            This value is being added to the output pitch when not
            in tuning mode. It can be used for musical transposition
            or adding a vibrato.


    Outputs:
        output: voltperoctave
            This is what it's all about: here comes the pitch CV for the
            current arpeggio note.

    """


    pitch: Optional[str] = None
    range: Optional[str] = None
    clock: Optional[str] = None
    reset: Optional[str] = None
    pattern: Optional[str] = None
    direction: Optional[str] = None
    pingpong: Optional[str] = None
    butterfly: Optional[str] = None
    drop: Optional[str] = None
    octaves: Optional[str] = None
    startnote: Optional[str] = None
    autoreset: Optional[str] = None
    root: Optional[str] = None
    degree: Optional[str] = None
    select1: Optional[str] = None
    select3: Optional[str] = None
    select5: Optional[str] = None
    select7: Optional[str] = None
    select9: Optional[str] = None
    select11: Optional[str] = None
    select13: Optional[str] = None
    selectfill1: Optional[str] = None
    selectfill2: Optional[str] = None
    selectfill3: Optional[str] = None
    selectfill4: Optional[str] = None
    selectfill5: Optional[str] = None
    harmonicshift: Optional[str] = None
    noteshift: Optional[str] = None
    selectnoteshift: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Bernoulli:
    """Circuit bernoulli.
      Random gate distributor

    Inputs:
        input: gate
            Send gate or trigger signals here.

        distribution: bipolar
            This controls the probability of a gate to be forwarded to
            output1. A value of 0.5 means 50%.


    Outputs:
        output1: gate
            Gates from input are forwarded here if the random decision was
            in favour of output 1.

        output2: gate
            Gates from input are forwarded here if the random decision was
            in favour of output 2.

    """


    input: Optional[str] = None
    distribution: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None


@dataclass
class Burst:
    """Circuit burst.
      Generate burst of pulses

    Inputs:
        rate: cv
            Frequency control: The default frequency of the burst rate is 1 Hz
            (one trigger per second or 60 BPM if you like). Each volt doubles
            the frequency. So an input of 1 V (a number of 0.1) speeds up
            to two triggers per second (120 BPM), 2 V (0.2) creates triggers
            at 4 Hz (240 BPM) and so on. On the other hand negative voltages
            reduce the speed, so -1 V (-0.1) will give 0.5 Hz (30 BPM)
            and so on.

        taptempo: trigger
            Feed a reference clock here and the burst will run at the speed of
            that clock – albeit optionally modified by rate.
            Please see page 23 for details on using
            taptempo inputs.

        hz: cv
            Set the frequency in Hz directly by setting a number here. This
            is exclusive to taptempo, but will work in combination with
            rate.

        trigger: trigger
            Send a trigger here in order to start the bursts

        reset: trigger
            Send a trigger here to immediately stop any ongoing burst.

        count: integer
            Number of triggers to send in one burst.

        skip: integer
            Number of time slots to wait before starting with the burst.


    Outputs:
        output: trigger
            The triggers are output here.

    """


    rate: Optional[str] = None
    taptempo: Optional[str] = None
    hz: Optional[str] = None
    trigger: Optional[str] = None
    reset: Optional[str] = None
    count: Optional[str] = None
    skip: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Button:
    """Circuit button.
      Does all sorts of useful things with buttons

    Inputs:
        button: gate
            The actual push button. Usually you want to wire this to B1.1,
            B1.2 and so on: to one of the push buttons of your
            controllers. Each time that input goes from low to high,
            the state of the push button will toggle.

        onvalue: cv
            Value sent to output when the push button is on. You can also
            use a dynamic signal here. This is an alternative name for the
            input value1.

        offvalue: cv
            Value sent to output when the push button is off. This
            is an alternative name for the input value2.

        value1: cv
            The up to four values to output at output when the button
            is on the according state. value1 is the same as offvalue
            and value2 is the same as onvalue. The default values
            of these four inputs are 0, 1, 2 and 3, so
            in many cases you don't need to specify them.

        value2: cv
            The up to four values to output at output when the button
            is on the according state. value1 is the same as offvalue
            and value2 is the same as onvalue. The default values
            of these four inputs are 0, 1, 2 and 3, so
            in many cases you don't need to specify them.

        value3: cv
            The up to four values to output at output when the button
            is on the according state. value1 is the same as offvalue
            and value2 is the same as onvalue. The default values
            of these four inputs are 0, 1, 2 and 3, so
            in many cases you don't need to specify them.

        value4: cv
            The up to four values to output at output when the button
            is on the according state. value1 is the same as offvalue
            and value2 is the same as onvalue. The default values
            of these four inputs are 0, 1, 2 and 3, so
            in many cases you don't need to specify them.

        doubleclickmode: gate
            This input can enable a double click mode when set to 1.
            In that mode the button only toggles it's constant state if you double
            press it in a short time. Otherwise it behaves like a momentary button,
            that inverts the persisted state (which you toggle with the double click).
            Note: The double clock mode is only makes sense if the number of
            states is 2.

        longpresstime: cv
            The number of seconds after which a button press is considered
            as a long press.

        states: integer
            Number of states this button can have. The default value is 2,
            which creates a toggle button which changes between on and off at each
            press. A value of 1 creates a momentary button. Note: If you just
            need a plain momentary button, you can directly use B1.1, B1.2
            and so on. You don't need an extra circuit. But if you want things like
            overloading (with select) or the longpress output, this does
            make sense. The maximum number of states is 4. When the button has
            3 or 4 states, every press will switch to the next state and then
            back to the first state again.

        startvalue: integer
            State of the push button when you switch on your system or on a
            trigger to clear. If you have three
            states, the start value needs to be 0, 1 or 2. With
            four states, it can also be 3.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        led: cv
            When the button state is on, a value of 1.0 will be sent to that
            output – regardless of the values in onvalue
            and offvalue. If the number of states is 3 or 4 the output get's intermediate
            values so the attached LED will be dimmed into different brightness
            levels. Usually you wire that output to a LED register, e.g.
            to L1.1, L1.2 and so on.

        output: cv
            This output will output the current button states. This is usually
            0 for off and 1 for on. If states is 3 or 4, the
            values 2 or 3 are output for the additional states.
            You can modify all four values with the inputs offvalue/value1,
            onvalue/value2, value3 and value4. Note:
            if you haven't changed any of these inputs and states is
            unchanged or 1 or 2, the led output will output the same
            values.

        inverted: cv
            The same as output, but sends onvalue when the
            button is off and offvalue when the button is on.
            If states is 3 or 4, the order of the four output values will
            be mirrored (probably a feature that is rarely of any use).

        negated: gate
            Similar to inverted, but always sends 1 when the button
            is off and 0 when the button is on – independent of the values
            of onvalue and offvalue. When states is 3 or 4,
            this output will be 1 if the button is off and 0 in
            the other three states.

        longpress: gate
            Goes from 0 to 1, when the button is pressed and hold
            for at least 1.5 seconds. If this output is used, the effect of
            toggling the button's state is delayed until the button is released. When it's released after 1.5 secs, no toggling happens.
            This will avoid double actions for long presses.

        shortpress: trigger
            Emits a trigger, when the button is pressed, regardless of
            the settings of states. If at the same time longpress
            is used (which is the whole point in this output), the trigger
            is delayed until the button is released and only sent, if it
            was not a long press.

    """


    button: Optional[str] = None
    onvalue: Optional[str] = None
    offvalue: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    value3: Optional[str] = None
    value4: Optional[str] = None
    doubleclickmode: Optional[str] = None
    longpresstime: Optional[str] = None
    states: Optional[str] = None
    startvalue: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    led: Optional[str] = None
    output: Optional[str] = None
    inverted: Optional[str] = None
    negated: Optional[str] = None
    longpress: Optional[str] = None
    shortpress: Optional[str] = None


@dataclass
class Buttongroup:
    """Circuit buttongroup.
      Connected buttons

    Inputs:
        minactive: integer
            Minimum number of active buttons. If you set this to 2, then
            it is guaranteed that at least 2 buttons are active. If you
            set this to 0, then it is possible to switch off all buttons.
            The output will be set to 0.0 in that case.

        maxactive: integer
            Maximum number of active buttons. It is an error to set this to
            0, since this would make this circuit useless.

        longpresstime: cv
            The number of seconds after which a button press is considered
            as a long press.

        button1: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button2: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button3: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button4: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button5: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button6: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button7: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button8: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button9: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button10: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button11: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button12: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button13: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button14: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button15: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button16: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button17: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button18: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button19: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button20: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button21: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button22: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button23: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button24: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button25: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button26: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button27: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button28: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button29: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button30: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button31: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        button32: trigger
            1 ... 32 button of the group. Any positive trigger seen here will
            toggle this button. And another button might go on or off in
            order to make sure that the number of active buttons is withing the
            allowed range.

        value1: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value2: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value3: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value4: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value5: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value6: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value7: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value8: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value9: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value10: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value11: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value12: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value13: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value14: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value15: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value16: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value17: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value18: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value19: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value20: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value21: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value22: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value23: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value24: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value25: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value26: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value27: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value28: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value29: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value30: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value31: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        value32: cv
            Value that will be sent to the output if the 1 ...
            32 button is active. These inputs default to 0 for
            value1, 1 for value2 and so on and 31 for value32.

        startbutton: integer
            If you set this parameter to the number of a button, that
            button will be selected (and all other deselected) at the
            start when no state is loaded or at a trigger to clear.
            This allows you to set useful default values for your button groups.
            Note: this only makes sense if maxactive is not 0.
            Also it is not possible to select more than one button, even in
            a group where maxactive is greater than 1.

            if minactive = 0, you also can set startbutton = 0.
            Then a clear will clear all buttons.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        led1: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led2: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led3: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led4: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led5: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led6: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led7: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led8: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led9: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led10: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led11: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led12: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led13: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led14: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led15: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led16: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led17: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led18: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led19: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led20: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led21: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led22: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led23: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led24: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led25: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led26: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led27: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led28: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led29: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led30: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led31: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        led32: gate
            This output will be on / 1.0, whenever the 1 ...
            32 button is active
            and off / 0.0 otherwise. Wire this to the LED in the button. If
            you have wired select, these LED outputs will do nothing
            (not even send 0) unless this circuit is selected.

        buttonoutput1: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput2: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput3: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput4: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput5: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput6: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput7: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput8: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput9: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput10: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput11: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput12: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput13: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput14: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput15: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput16: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput17: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput18: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput19: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput20: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput21: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput22: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput23: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput24: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput25: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput26: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput27: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput28: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput29: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput30: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput31: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        buttonoutput32: cv
            These are individual outputs for every button in the group. They
            output button's value when it is active, otherwise 0.
            If valueX is not defined for buttonX, the value
            1 is output (not the button's number!).

            Note: in contrast to the led output, these outputs are
            not affected by select but always functional.

            One application of these outputs is to use a buttongroup
            with maxactive =  X and minactive = 0 as a cheap
            bunch of X toggle buttons in one single circuit and still
            use select.

        output: cv
            The sum of the values of all active buttons will be sent here.
            if no button is active, 0.0 is being output.

        buttonpress: trigger
            Emits a trigger if any button is being pressed

        longpress: trigger
            Emits a trigger, when any button is pressed for at least 1.5
            seconds. If this jack is used, buttonpress will emit
            a signal if the button in question is released before the 1.5
            seconds, not immediately. This way you trigger either
            at buttonpress or at longpress, not at both.

        selectionchanged: trigger
            Emits a trigger when the selection of the buttons has changed.
            This is not quite the same as buttonpress, since a button
            press might not lead to a change. Also in multi button situations
            (e.g. maxactive = 4 where you have 7 buttons) the change
            is delayed up to 25 ms due to detection of bursts of quasi
            simultanous presses.

    """


    minactive: Optional[str] = None
    maxactive: Optional[str] = None
    longpresstime: Optional[str] = None
    button1: Optional[str] = None
    button2: Optional[str] = None
    button3: Optional[str] = None
    button4: Optional[str] = None
    button5: Optional[str] = None
    button6: Optional[str] = None
    button7: Optional[str] = None
    button8: Optional[str] = None
    button9: Optional[str] = None
    button10: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    button13: Optional[str] = None
    button14: Optional[str] = None
    button15: Optional[str] = None
    button16: Optional[str] = None
    button17: Optional[str] = None
    button18: Optional[str] = None
    button19: Optional[str] = None
    button20: Optional[str] = None
    button21: Optional[str] = None
    button22: Optional[str] = None
    button23: Optional[str] = None
    button24: Optional[str] = None
    button25: Optional[str] = None
    button26: Optional[str] = None
    button27: Optional[str] = None
    button28: Optional[str] = None
    button29: Optional[str] = None
    button30: Optional[str] = None
    button31: Optional[str] = None
    button32: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    value3: Optional[str] = None
    value4: Optional[str] = None
    value5: Optional[str] = None
    value6: Optional[str] = None
    value7: Optional[str] = None
    value8: Optional[str] = None
    value9: Optional[str] = None
    value10: Optional[str] = None
    value11: Optional[str] = None
    value12: Optional[str] = None
    value13: Optional[str] = None
    value14: Optional[str] = None
    value15: Optional[str] = None
    value16: Optional[str] = None
    value17: Optional[str] = None
    value18: Optional[str] = None
    value19: Optional[str] = None
    value20: Optional[str] = None
    value21: Optional[str] = None
    value22: Optional[str] = None
    value23: Optional[str] = None
    value24: Optional[str] = None
    value25: Optional[str] = None
    value26: Optional[str] = None
    value27: Optional[str] = None
    value28: Optional[str] = None
    value29: Optional[str] = None
    value30: Optional[str] = None
    value31: Optional[str] = None
    value32: Optional[str] = None
    startbutton: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    led1: Optional[str] = None
    led2: Optional[str] = None
    led3: Optional[str] = None
    led4: Optional[str] = None
    led5: Optional[str] = None
    led6: Optional[str] = None
    led7: Optional[str] = None
    led8: Optional[str] = None
    led9: Optional[str] = None
    led10: Optional[str] = None
    led11: Optional[str] = None
    led12: Optional[str] = None
    led13: Optional[str] = None
    led14: Optional[str] = None
    led15: Optional[str] = None
    led16: Optional[str] = None
    led17: Optional[str] = None
    led18: Optional[str] = None
    led19: Optional[str] = None
    led20: Optional[str] = None
    led21: Optional[str] = None
    led22: Optional[str] = None
    led23: Optional[str] = None
    led24: Optional[str] = None
    led25: Optional[str] = None
    led26: Optional[str] = None
    led27: Optional[str] = None
    led28: Optional[str] = None
    led29: Optional[str] = None
    led30: Optional[str] = None
    led31: Optional[str] = None
    led32: Optional[str] = None
    buttonoutput1: Optional[str] = None
    buttonoutput2: Optional[str] = None
    buttonoutput3: Optional[str] = None
    buttonoutput4: Optional[str] = None
    buttonoutput5: Optional[str] = None
    buttonoutput6: Optional[str] = None
    buttonoutput7: Optional[str] = None
    buttonoutput8: Optional[str] = None
    buttonoutput9: Optional[str] = None
    buttonoutput10: Optional[str] = None
    buttonoutput11: Optional[str] = None
    buttonoutput12: Optional[str] = None
    buttonoutput13: Optional[str] = None
    buttonoutput14: Optional[str] = None
    buttonoutput15: Optional[str] = None
    buttonoutput16: Optional[str] = None
    buttonoutput17: Optional[str] = None
    buttonoutput18: Optional[str] = None
    buttonoutput19: Optional[str] = None
    buttonoutput20: Optional[str] = None
    buttonoutput21: Optional[str] = None
    buttonoutput22: Optional[str] = None
    buttonoutput23: Optional[str] = None
    buttonoutput24: Optional[str] = None
    buttonoutput25: Optional[str] = None
    buttonoutput26: Optional[str] = None
    buttonoutput27: Optional[str] = None
    buttonoutput28: Optional[str] = None
    buttonoutput29: Optional[str] = None
    buttonoutput30: Optional[str] = None
    buttonoutput31: Optional[str] = None
    buttonoutput32: Optional[str] = None
    output: Optional[str] = None
    buttonpress: Optional[str] = None
    longpress: Optional[str] = None
    selectionchanged: Optional[str] = None


@dataclass
class Calibrator:
    """Circuit calibrator.
      VCO Calibrator

    Inputs:
        input: voltperoctave
            Patch your V/Oct pitch input here.

        nudgeup: trigger
            A trigger here (most likely a button press) will modify the tuning of
            the currently played note (as read by input) upwards by
            one cent (or by nudgeamount if that is used.

        nudgedown: trigger
            A trigger here will modify the tuning of
            the currently played note down.

        clearhere: trigger
            A trigger here sets the correction of the currently played note
            to zero. This might affect a range of up to two octaves.

        nudgeamount: cv
            Changes the amount each button press detunes. A value of one would mean
            one semitone, so the default value of 0.01 corresponds to one cent (1/100)
            of a semitone.

        tune0: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune1: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune2: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune3: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune4: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune5: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune6: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune7: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tune8: cv
            Explicit tuning of the octaves 0 through 8 – if you do not want
            to nudge manually. tune0 sets the tuning for the input
            pitch of 0 V, tune1 for 1 V and so on. A value of 1 means a tune adjustment
            of one semitone – which is 100 cent. The maximum detuning is ± 1 Octave (
            at a value of ± 12).

        tunelowtail: cv
            Tuning adaption for the negative voltage range.
            A value of 1 means an upwards tuning of one semitone
            per octave, -1 likewise downwards.

        tunehightail: cv
            Tuning adaption for voltages > 8 V. A value of 1 means
            an upwards tuning of one semitone per octave, -1 likewise
            downwards.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output: voltperoctave
            The calibrated pitch goes out here.

        ledup: fraction
            When nudgeup is mapped to a button (which is most likely),
            map this output to the according LED and it will indicate whenever
            it's currently adjusting the output pitch upwards.

        leddown: fraction
            This is the LED for nudgedown, which indicates downwards
            adjustment.

        correction: cv
            This output gives you information about the current amout
            of pitch correction. It is positive if the pitch is corrected
            upwards, else negative. It is scaled in semitones, so a value
            of 0.2 means a 20% of a semitone, which is the same is
            20 cents.

    """


    input: Optional[str] = None
    nudgeup: Optional[str] = None
    nudgedown: Optional[str] = None
    clearhere: Optional[str] = None
    nudgeamount: Optional[str] = None
    tune0: Optional[str] = None
    tune1: Optional[str] = None
    tune2: Optional[str] = None
    tune3: Optional[str] = None
    tune4: Optional[str] = None
    tune5: Optional[str] = None
    tune6: Optional[str] = None
    tune7: Optional[str] = None
    tune8: Optional[str] = None
    tunelowtail: Optional[str] = None
    tunehightail: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output: Optional[str] = None
    ledup: Optional[str] = None
    leddown: Optional[str] = None
    correction: Optional[str] = None


@dataclass
class Case:
    """Circuit case.
      Switch choosing from inputs via conditions

    Inputs:
        case1: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case2: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case3: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case4: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case5: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case6: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case7: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case8: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case9: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case10: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case11: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case12: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case13: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case14: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case15: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        case16: cv
            1 ... 16 case input. The first one that is non-zero defines
            which input value to use.

        value1: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value2: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value3: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value4: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value5: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value6: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value7: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value8: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value9: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value10: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value11: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value12: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value13: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value14: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value15: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        value16: cv
            1 ... 16 value input. One of these is copied to the output,
            depending on which of the case inputs is none-zero.

        else_: trigger
            In case none of the case inputs is non-zero, this value is copied
            to the output.


    Outputs:
        output: cv
            To this output the select value input is copied.

    """


    case1: Optional[str] = None
    case2: Optional[str] = None
    case3: Optional[str] = None
    case4: Optional[str] = None
    case5: Optional[str] = None
    case6: Optional[str] = None
    case7: Optional[str] = None
    case8: Optional[str] = None
    case9: Optional[str] = None
    case10: Optional[str] = None
    case11: Optional[str] = None
    case12: Optional[str] = None
    case13: Optional[str] = None
    case14: Optional[str] = None
    case15: Optional[str] = None
    case16: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    value3: Optional[str] = None
    value4: Optional[str] = None
    value5: Optional[str] = None
    value6: Optional[str] = None
    value7: Optional[str] = None
    value8: Optional[str] = None
    value9: Optional[str] = None
    value10: Optional[str] = None
    value11: Optional[str] = None
    value12: Optional[str] = None
    value13: Optional[str] = None
    value14: Optional[str] = None
    value15: Optional[str] = None
    value16: Optional[str] = None
    else_: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Chord:
    """Circuit chord.
      Chord generator

    Inputs:
        pitch: voltperoctave
            This sets the minimum pitch of the lowest note of the chord.

        spread: voltperoctave
            Selects the range between the lowest and highest note of the
            chord measured in 1V/oct, while a spread of 0 means that all chord
            notes are within one octave, a spread of 1 V means that
            the notes are spread out over two octaves and so on.

        inversion: integer
            Selects the inversion of the chord. 1 means that the
            root note should be the lowest note, 2 will make the second
            selected note the lowest note, 3 the 3 and 4 the
            4. The default, however, is 0 and doesn't fix the inversion.
            Rather that inversion is chosen that creates the chord closest
            to the input pitch.

        trigger: trigger
            This jack is optional. If you patch it, the Chord generator just
            reads a new input pitch when it receives a trigger.

        root: integer
            Set the root note here. 0 means C, 1 means
            C♯, 2 means D and so on. If you multiply
            the value of an input like I1 with 120, then you can use a 1V/Oct
            input for selecting the root note via a sequencer, MIDI keyboard
            or the like.
            Also then you are compatible with the ROOT CV input of the Sinfonion.

             0C
            1C♯
            2D
            3D♯
            4E
            5F
            6F♯
            7G
            8G♯
            9A
            10A♯
            11B
            12C




        degree: integer
            Set the musical scale. This is a number from 0 to 107.
            Below are the first 12 and most important scales. You find a list
            of all 108 scales on page 105.

             0lyd – Lydian major scale (it has a ♯ 4)
            1maj – Normal major scale (ionian)
            2X^7 – Mixolydian (dominant seven chords)
            3sus – mixolydian with 3/4 swapped
            4alt – Altered scale
            5hm^5 – Harmonic minor scale from the 5
            6dor – Dorian minor (minor with ♯ 13)
            7min – Natural minor (aeolian)
            8hm – Harmonic minor (♭ 6 but ♯ 7)
            9phr – Phrygian minor scale (with ♭ 9)
            10dim – Diminished scale (whole/half tone)
            11aug – Augmented scale (just whole tones)


            Note: Alltogether there are 108 scales. Please see page 105 for a complete list

        select1: gate
            Gate input for selecting the root note as being an
            allowed interval. When you want to create a playing interface
            for live operation you can patch the output of a toggle button
            (made with the circuit [button]) here.

            Note: When all select and selectfill inputs are 0,
            automatically all seven scale notes are selected, i.e.
            select1 ... select13 will be set to one.

        select3: gate
            Gate input for selecting the 3.

        select5: gate
            Gate input for selecting the 5.

        select7: gate
            Gate input for selecting the 7.

        select9: gate
            Gate input for selecting the 9 (which is the same
            as the 2).

        select11: gate
            Gate input for selecting the 11 (which is the same
            as the 4).

        select13: gate
            Gate input for selecting the 13 (which is the same
            as the 6).

        selectfill1: gate
            Selects the alternative 9 (i.e.
            the 9 that is not in the scale.

        selectfill2: gate
            Selects the alternative 3 (i.e.
            the 3 that is not in the scale).

        selectfill3: gate
            Selects the alternative 4 or 5. In
            most cases this is the diminished 5.

        selectfill4: gate
            Selects the alternative 13 (i.e.
            the 13 that is not in the scale).

        selectfill5: gate
            Selects the alternative 7 (i.e.
            the 7 that is not in the scale).

        harmonicshift: integer
            This input can reduce harmonic complexity by disabling some of
            the scale or non-scale notes. It is an idea first found in the
            Sinfonion and also provided by the circuit sinfonionlink.

            harmonicshift is staged after the select... inputs
            and further filters out (disables) notes based on their relation
            to the current scale. This means that first the 12 select... inputs
            select a subset of the 12 possible notes. After that harmonicshift
            can reduce this set further (it will never add notes).

            If harmonicshift is not zero, depending on its value some or
            more of the scale notes are disabled, even if they would be allowed by
            select....  Or in other words: the harmonic material is reduced.

            You also can use negative values. These create rather strange sounds
            by removing the simple chord functions instead of the complex
            ones first.

            Here are the possible values:

             0off – all selected notes are allowed
            1disable all fill notes (non-scale notes)
            2disable fills and 11
            3disable fills, 11 and 13
            4disable fills, 11, 13 and 9
            5disable fills, 11, 13, 9 and 7
            6disable fills, 11, 13, 9, 7 and 3
            7disable fills, 11, 13, 9, 7, 3 and 5
            -1disable the root note
            -2disable the root note and the 5
            -3disable root, 3, 5
            -4disable root, 3, 5, 7
            -5disable root, 3, 5, 7, 9
            -6disable root, 3, 5, 7, 9 and 13
            -7disable all scale notes (fill notes untouched)




        noteshift: integer
            Shifts the resulting output note(s) by this
            number of scale notes up or down (if negative). So the output
            note still is part of the scale but may be a note that is none
            of the selected ones. The maximum shift range is limited to
            -24 … +24.

        selectnoteshift: integer
            Shifts the output note by this
            number of selected scale notes up or down (if negative).
            If you use noteshift at the same time, first selectnoteshift is applied, then noteshift. The maximum shift range
            is limited to -24 … +24.

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            This value is being added to the output pitch when not
            in tuning mode. It can be used for musical transposition
            or adding a vibrato.


    Outputs:
        output1: voltperoctave
            1 ... 4 pitch output

        output2: voltperoctave
            1 ... 4 pitch output

        output3: voltperoctave
            1 ... 4 pitch output

        output4: voltperoctave
            1 ... 4 pitch output

    """


    pitch: Optional[str] = None
    spread: Optional[str] = None
    inversion: Optional[str] = None
    trigger: Optional[str] = None
    root: Optional[str] = None
    degree: Optional[str] = None
    select1: Optional[str] = None
    select3: Optional[str] = None
    select5: Optional[str] = None
    select7: Optional[str] = None
    select9: Optional[str] = None
    select11: Optional[str] = None
    select13: Optional[str] = None
    selectfill1: Optional[str] = None
    selectfill2: Optional[str] = None
    selectfill3: Optional[str] = None
    selectfill4: Optional[str] = None
    selectfill5: Optional[str] = None
    harmonicshift: Optional[str] = None
    noteshift: Optional[str] = None
    selectnoteshift: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None


@dataclass
class Clocktool:
    """Circuit clocktool.
      Clock divider / multiplier / shifter

    Inputs:
        clock: trigger
            Patch a steady clock here for this circuit to be of any use

        reset: trigger
            A trigger here resets the internal counters. This is useful if you
            use the clock divider and want to restart the internal counting from
            0, in order to align the clock divider with some external sequencers
            or the like

        divide: integer
            Number to divide the clock through. This will be rounded to the
            nearest integer number. Note: if you want to use an external CV then
            you need to multiply that with some useful number, since otherwise
            you will get a number between 0 and 1 which is not useful
            at all. Remember: 10 V translates to a number of 1.

        multiply: integer
            Number to multiply the clock with. Same considerations hold as for divide.

        dutycycle: bipolar
            Output duty cycle of the clock – which is essentially a square wave –
            in a range from 0.0 to 1.0 or 0% to 100%. If you
            don't patch anything here, the length of the trigger output pulses will
            be 10 ms ('s standard trigger duration).

        gatelength: cv
            This jack is alternative to dutycycle and will override it
            if it is used.	It sets the length of each output pulse to a fixed
            value that is independent of the incoming clock. A value of 0.5
            (a CV of 5 volts) translates into a gate length of 0.5 seconds.

        delay: cv
            This CV allows you to shift the input clock beat around in time.
            A value of 0.1 will delay each beat by 10% of a clock cycle.
            A value of -0.1 is also allowed and shifts the beat 10%
            ahead.

            For an unmodulated delay -0.1 and 0.9 is just the same,
            because the output clock will have the same relation to the input
            clock. But if you modify the delay from 0.0 to 0.9,
            the next tick will be delayed by 90% of one cycle, where is a
            modification from 0.0 to -0.1 will play the next tick
            by 10% earlier.


    Outputs:
        output: gate
            Here comes the modified clock

        inputpitch: cv
            Experimental output that outputs a representation of the input
            clock's pitch on a 1V/octave base, based on the reference of 60 BPM
            (1 Hz). This means that an input clock of 120 BPM will output 1V
            (a value of 0.1), since 120 BPM it is one octave higher than
            60 BPM. If you feed that value to the rate input of an LFO you
            get that running at exactly the same speed (not in the same phase,
            however).

        outputpitch: cv
            Same for the modified output clock

    """


    clock: Optional[str] = None
    reset: Optional[str] = None
    divide: Optional[str] = None
    multiply: Optional[str] = None
    dutycycle: Optional[str] = None
    gatelength: Optional[str] = None
    delay: Optional[str] = None
    output: Optional[str] = None
    inputpitch: Optional[str] = None
    outputpitch: Optional[str] = None


@dataclass
class Compare:
    """Circuit compare.
      Compare two values

    Inputs:
        input: cv
            A value to compare.

        compare: cv
            A reference value to compare the input with.

        ifgreater: cv
            Value to be output if input is greater than compare.
            If you patch nothing here, the value of the input else will be used.

        ifless: cv
            Value to be output if input is less than compare.
            If you patch nothing here, the value of the input else will be used.

        ifequal: cv
            Value to be output if input is equal to compare within the
            precision defined by precision.
            If you patch nothing here, the value of the input else will be used.

        else_: cv
            Specifies the output value in case non of the stated conditions are met.

        precision: cv
            An optional precision to be used by ifequal


    Outputs:
        output: cv
            Here one of ifgreater, ifless or ifequal is output.

    """


    input: Optional[str] = None
    compare: Optional[str] = None
    ifgreater: Optional[str] = None
    ifless: Optional[str] = None
    ifequal: Optional[str] = None
    else_: Optional[str] = None
    precision: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Contour:
    """Circuit contour.
      Contour generator

    Inputs:
        gate: gate
            Patch a gate signal here that triggers the envelope. Gate means
            that the length of the signal is relevant. While the gate is high
            the sustain phase holds on. As soon as gate is going low the release
            phase is being entered.

        trigger: trigger
            This is an alternative method of starting the envelope.
            If you use trigger instead of gate, there are the
            following differences:



              * The duration of the trigger signal is being ignored.

              * There is no decay / sustain phase. Attack and hold are
            immediately followed by release. The inputs sustain and
            decay have no impact anymore.

              * The predelay and attack phases are continued until their
            end even when the trigger signal ends (When using gate
            and the gate signal ends during predelay, the envelope does
            not start. When it ends during attack, decay / sustain are
            being skipped and release starts at the current level of the envelope.
            That way short gates can result in “quieter” envelopes).


        retrigger: gate
            If you patch 0 or off here, a gate or trigger impulse
            will not immediately restart the envelope unless it already has
            reached its release phase.  The default on,
            which means that a trigger will immediately restart the envelope in any
            case.

        startfromzero: gate
            If you set this to 1 or on, a trigger or gate will
            reset the envelope's current level immediately to zero. This is sometimes
            called “digital mode”. In the normal analog mode the envelope
            resumes from where it is. This means that when a trigger occurs right
            in the release phase where the level is still high, will start
            it's attack not from zero but from this hight value.

        abortattack: gate
            This is an on / off setting that decides what happens
            if the input gate goes off while the predelay or attack phase
            is still not finished. Per default that phase will be finalized
            regardless of the gate state.  If abortattack is on, the
            end of the gate will immediately stop the attack phase and move on
            to hold. Note: In this case the value of the envelope will not reach the maximum
            level. If the gate ends during the predelay phase, no
            envelope will be started at all.

            Note: This setting is only functional when the gate input
            is being used for triggering the envelope. If you use trigger,
            the attack phase is always completely executed and this setting
            has no influence.

        loop: gate
            This is an on / off input that switches loop on or off. When
            loop is on, the envelope will immediately start again once it
            has finished. It also starts without triggering. This converts
            contour into a kind of fancy LFO.

            gate / trigger and loop can be combined. Any gate or
            trigger will restart the envelope just as usual – even in loop mode.

        predelay: cv
            The predelay phase inserts a delay between the incoming gate
            and the begin of the envelope. The length of the predelay is
            0.1 seconds per volt, so a value of 1.0 means 1 second

        attack: cv
            Length of the attack phase, i.e. the time from the beginning of
            the gate until the maximum level is reached. See the general
            description for information about the scaling of this input.

        hold: cv
            If this is none-zero, the envelopes lingers a certain amount
            of time at its maximum level after the attack and before the decay
            phase. The input value specifies a number of seconds.
            A value of 0.5 (this is 5 V) will create a hold time of
            0.5 seconds.

        decay: cv
            Time of the decay phase

        sustain: fraction
            Sustain level

        swell: fraction
            If this jack is set to a value greater than 0.0,
            the level of the envelope will go
            up or down again during the sustain phase until it reaches
            swelllevel.

        swelltime: cv
            Time of the swell phase

        swelllevel: cv
            Level the swell phase is approaching. Setting this to the
            same as sustain effectively disables swell.

        release: cv
            Timing of the release phase

        level: cv
            Maximum level and scaling of the envelope. It is basically an
            output attenuator of the envelope. Sudden changes in the level will
            immediately have an (audible) impact on the envelope.

        velocity: fraction
            energy of the attack: The velocity is similar to the level,
            but is effective just during the attack phase. During that phase that
            maximum voltage that is read from the velocity jack and will be used
            as the velocity of the envelope. Further changes during the other phases
            will be ignored. This makes it ideal of using with a sequencer. For example
            you can patch an accent output here and add some offset.
            Sudden changes in this input will not affect the shape of the envelope.

        pitch: voltperoctave
            This is a one volt per octave input affecting all timings of
            the envelope. When you set this to 0 (the default), it is neutral.
            A value of 0.1 (1 Volt) will exactly double the speed of all phases -
            just as one octave up doubles the frequency of an oscillator. This jack
            can be used to easily implement envelopes where the length very naturally
            follows this pitch - just like on a piano, glockenspiel or marimba lower
            notes last longer than higher ones.

        taptempo: trigger
            Tap tempo is an alternative method of specifying a pitch information.
            When you patch a clock to tap tempo, all time parameters in
            the envelope are relative to that clock. If the clock speeds up,
            the envelope gets faster and vice versa. The reference speed is 120 BPM.
            This means that if you patch a 120 BPM clock here, nothing changes.
            Clocks faster than 120 BPM will speed up the envelope. Clocks slower
            than 120 BPM will slow it down.

            Please see page 23 for details on using
            taptempo inputs.

        shape: bipolar
            If you use this jack, it sets the shape for all of the
            relevant phases, which are attack, decay, swell and release. Note:
            this input is only effective for those phases where the dedicated
            input (like attackshape, etc.) is not being used.

        attackshape: bipolar
            Shape of the attack curve. If nothing is patched here, the value
            of shape will be used.
            See the general description for how curve shapes work.

        decayshape: bipolar
            Shape of the curve in the decay phase. If nothing is patched here,
            the value of shape will be used.

        swellshape: bipolar
            Shape of curve during the swell phase. If nothing is patched here,
            the value of shape will be used.

        releaseshape: bipolar
            Shape of the curve in the release phase. If nothing is patched
            here, the value of shape will be used.

        zerocrossing: cv
            This is an experimental feature: If you patch the output of an
            oscillator here, an incoming gate or trigger signal will be
            delayed until the next zero crossing of that signal. That allows
            you to start the envelope exactly when the audio signal is at 0
            and avoid nasty klicks, even if the attack is set to 0. It comes
            at a price, however. The delay between the trigger and the first
            zero crossing might vary a lot from note to note and that could
            make your rhythm untight, especially if the frequency of the oscillator
            is low.


    Outputs:
        output: cv
            Main output of the envelope. Patch this to your filter, VCA or
            wherever you like.

        negated: cv
            The negated output is the same as the output but in negative
            voltage.

        inverted: cv
            The inverted output always outputs positive voltages but
            is inverted relative to the level of the envelope. When the normal
            output outputs 0 V, the inverted output outputs level and
            vice versa

        endofpredelay: trigger
            This output will emit a trigger with a length of 10 ms when the
            predelay phase has ended.

        endofattack: trigger
            This output will emit a trigger with a length of 10 ms when the
            attack phase has ended.

        endofhold: trigger
            This output will emit a trigger with a length of 10 ms when the
            hold phase has ended.

        endofdecay: trigger
            This output will emit a trigger with a length of 10 ms when the
            decay phase has ended.

        endofrelease: trigger
            This output will emit a trigger with a length of 10 ms when the
            release phase has ended.

    """


    gate: Optional[str] = None
    trigger: Optional[str] = None
    retrigger: Optional[str] = None
    startfromzero: Optional[str] = None
    abortattack: Optional[str] = None
    loop: Optional[str] = None
    predelay: Optional[str] = None
    attack: Optional[str] = None
    hold: Optional[str] = None
    decay: Optional[str] = None
    sustain: Optional[str] = None
    swell: Optional[str] = None
    swelltime: Optional[str] = None
    swelllevel: Optional[str] = None
    release: Optional[str] = None
    level: Optional[str] = None
    velocity: Optional[str] = None
    pitch: Optional[str] = None
    taptempo: Optional[str] = None
    shape: Optional[str] = None
    attackshape: Optional[str] = None
    decayshape: Optional[str] = None
    swellshape: Optional[str] = None
    releaseshape: Optional[str] = None
    zerocrossing: Optional[str] = None
    output: Optional[str] = None
    negated: Optional[str] = None
    inverted: Optional[str] = None
    endofpredelay: Optional[str] = None
    endofattack: Optional[str] = None
    endofhold: Optional[str] = None
    endofdecay: Optional[str] = None
    endofrelease: Optional[str] = None


@dataclass
class Copy:
    """Circuit copy.
      Copy a signal, while applying attenuation and offset

    Inputs:
        input: cv
            Connect the signal you want to copy here.


    Outputs:
        output: cv
            The resulting signal will be sent here.

    """


    input: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Crossfader:
    """Circuit crossfader.
      Morph between 8 inputs

    Inputs:
        input1: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input2: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input3: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input4: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input5: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input6: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input7: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        input8: cv
            The input signals that you want to crossfade between. At least
            input1 and input2 need to be patched. Otherwise they
            are treated like 0 V signals.

        fade: fraction
            This value decides which of the two inputs should be mixed and
            to which degree each one should go into the mix. At 0.0 the
            mix consists of 100% of the first inputs, at 1.0 of 100%
            of the last patched input.


    Outputs:
        output: cv
            Output of the mix

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    fade: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Cvlooper:
    """Circuit cvlooper.
      Clocked CV looper

    Inputs:
        cvin: cv
            Input CV that should be looped.

        gatein: gate
            Optional input gate. If you do not patch something here, the gate is
            assumed to be always high.

        clock: trigger
            Input clock. The clock is mandatory and is the base for the definition of
            the loop length. Also the loop switch is quantized in time to the nearest
            clock.

        reset: trigger
            A trigger here resets the playback head immediately to the start of the loop,
            if you are in playback mode.

        length: integer
            Length of the loop in clock ticks. Example: You get a length of 16 ticks
            by patching the number 16 to length. If you want to set the length by means
            of an external CV that would require 160 Volts. So you need to multiply your
            input by some useful number in that case.

        tapespeed: cv
            Relative tape speed, where 1.0 is the normal speed.
            So a value of 0.5
            slows down the speed thus increasing the effective tape length from 8 to
            16 seconds while reducing the sampling rate from 1 ms to 2 ms per sample.
            Changing the tape speed on the fly probably leads to interesting results.

        loopswitch: gate
            Mandatory parameter: While the loop switch is off the CV looper
            simply sends all input CV and gate to their respective outputs. At the same time CV
            and gate are also recorded to the tape. When the loop switch is on,
            the CV and gate are being read from the tape, instead. The input
            CV and gate are now ignored.

        pause: gate
            This is a binary input. If you send a high signal here, the looper
            pauses. This is only works in playback mode. The current CV value
            is hold the entire time. This is not the same as bypass, since
            in bypass mode the original CV will be routed through.

        overlay: gate
            Overlaying changes the behaviour while looping is active. If overlay is
            set to on, while the input gate is active the gate and CV will be
            sent directly from the inputs rather than read from the tape.

        overdub: gate
            Overdubbing also changes the behaviour during the looping: If
            it is active then while the input gate is high the input gate
            and CV will be written
            to the tape – thus changing the loop on the fly.

        bypass: gate
            Setting bypass to on copies the input CV and gate from their
            inputs to their outputs while keeping the loop's content
            untouched. This disabled the looping for the while, but you
            can get back to it later. Note: this is different from turning
            off the loop switch, because then your tape's content
            would be overwritten.


    Outputs:
        cvout: cv
            Output of the bypassed or looped CV

        gateout: gate
            Output of the bypassed or looped gate

    """


    cvin: Optional[str] = None
    gatein: Optional[str] = None
    clock: Optional[str] = None
    reset: Optional[str] = None
    length: Optional[str] = None
    tapespeed: Optional[str] = None
    loopswitch: Optional[str] = None
    pause: Optional[str] = None
    overlay: Optional[str] = None
    overdub: Optional[str] = None
    bypass: Optional[str] = None
    cvout: Optional[str] = None
    gateout: Optional[str] = None


@dataclass
class Dac:
    """Circuit dac.
      DA Converter with 12 bits

    Inputs:
        bit1: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit2: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit3: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit4: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit5: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit6: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit7: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit8: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit9: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit10: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit11: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        bit12: gate
            The 12 bit input bits. bit1 is the MSB – the most significant
            bit. The LSB (least significant bit) is the highest input that
            you actually patch.

        minimum: cv
            This sets the lower bound of the output range, i.e. the
            value that the bit sequence 000000000000 will produce.

        maximum: cv
            This sets the upper bound of the output value, i.e. the
            value that the bit sequence 111111111111 will produce.


    Outputs:
        output: cv
            Output signal.

    """


    bit1: Optional[str] = None
    bit2: Optional[str] = None
    bit3: Optional[str] = None
    bit4: Optional[str] = None
    bit5: Optional[str] = None
    bit6: Optional[str] = None
    bit7: Optional[str] = None
    bit8: Optional[str] = None
    bit9: Optional[str] = None
    bit10: Optional[str] = None
    bit11: Optional[str] = None
    bit12: Optional[str] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Delay:
    """Circuit delay.
      A tape delay for CVs, gates and numbers

    Inputs:
        delay: cv
            The CVs are delayed by this amount of seconds. If you patch clock as well, the delay is specified in clock tick, so then delay = 1 means “delay by one clock tick”.

        cvin: cv
            Continous input CV

        numberin: integer
            Discrete input number in the range 0 ... 255

        gatein1: cv
            Input gates

        gatein2: cv
            Input gates

        gatein3: cv
            Input gates

        gatein4: cv
            Input gates

        gatein5: cv
            Input gates

        gatein6: cv
            Input gates

        gatein7: cv
            Input gates

        gatein8: cv
            Input gates

        clock: trigger
            If you use this clock input, all time inputs are measured in
            clock ticks instead of seconds.

        sample: gate
            If you patch this input, “triggered” mode is enabled. In this mode,
            the virtual tape just records a new CV on each trigger at sample.
            So it just records stepped CVs, no slopes and no CV changes
            between the triggers.

        timewindow: cv
            When in triggered mode, this optional parameter helps tackling
            a problem that many hardware sequencers show: often their
            pitch CV is not at its final destination value at the time their
            gate is being output. Often you see a very short “slew” ramp
            of say 5 ms after the gate. During that time the pitch CV moves
            from its former to the new value.

            Now if you trigger the cvtape circuit with the sequencer's
            gate you will essentially sample the previous pitch CV
            instead of the new one. Or maybe something in between.

            The timewindow parameter configures a short time window
            after the trigger to trigger. During that time period the
            tape will constantly adapt the last sample to a changed input
            CV. When that time is over, the input is finally frozen on the tape.

            The timewindow parameter is in seconds. So when you set timewindow to say 0.005 (which means 5 ms), you give the
            input CV 5 ms time for settling to its final value after a trigger
            to sample before freezing it.

        bypass: gate
            Setting bypass to on copies the input signals directly
            to the outputs, regardless of any other stuff going on.

        save: trigger
            Send a trigger here to save the current contents of the
            tape to a file on the SD card. The filename is tapeXXXX.bin,
            where XXXX is replaced by the number set by filenumber.

        load: trigger
            Send a trigger here to load a previously saved file into the
            tape. Use filenumber so specify which file to load.

        filenumber: integer
            Number of the file to load or save. The range is 0 - 9999.
            If filenumber is 123, the name on the SD card is
            tape0123.bin. These files are shared between all
            recorder and delay circuits.


    Outputs:
        cvout: cv
            Output of the continous input CV

        numberout: integer
            Output of the discrete number

        gateout1: gate
            Output of the gates

        gateout2: gate
            Output of the gates

        gateout3: gate
            Output of the gates

        gateout4: gate
            Output of the gates

        gateout5: gate
            Output of the gates

        gateout6: gate
            Output of the gates

        gateout7: gate
            Output of the gates

        gateout8: gate
            Output of the gates

        overflow: gate
            When the internal memory of the tape is exceeded and
            data got lost, this gate goes to 1 for 0.5 seconds.
            If you are suspecting this situation, you can wire this
            output to an LED and observe the memory status that way.

    """


    delay: Optional[str] = None
    cvin: Optional[str] = None
    numberin: Optional[str] = None
    gatein1: Optional[str] = None
    gatein2: Optional[str] = None
    gatein3: Optional[str] = None
    gatein4: Optional[str] = None
    gatein5: Optional[str] = None
    gatein6: Optional[str] = None
    gatein7: Optional[str] = None
    gatein8: Optional[str] = None
    clock: Optional[str] = None
    sample: Optional[str] = None
    timewindow: Optional[str] = None
    bypass: Optional[str] = None
    save: Optional[str] = None
    load: Optional[str] = None
    filenumber: Optional[str] = None
    cvout: Optional[str] = None
    numberout: Optional[str] = None
    gateout1: Optional[str] = None
    gateout2: Optional[str] = None
    gateout3: Optional[str] = None
    gateout4: Optional[str] = None
    gateout5: Optional[str] = None
    gateout6: Optional[str] = None
    gateout7: Optional[str] = None
    gateout8: Optional[str] = None
    overflow: Optional[str] = None


@dataclass
class Detune:
    """Circuit detune.
      Detune multiple voices in a most disharmonic way

    Inputs:
        input1: cv

        input2: cv

        input3: cv

        input4: cv

        input5: cv

        input6: cv

        input7: cv

        input8: cv

        detune: cv

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.


    Outputs:
        output1: cv

        output2: cv

        output3: cv

        output4: cv

        output5: cv

        output6: cv

        output7: cv

        output8: cv

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    detune: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None


@dataclass
class Droid:
    """Circuit droid.
      General DROID controls

    Inputs:
        ledbrightness: cv
            Let's you dim all of the 24 LEDs of the master and the G8. This
            is mainly for those who think they are too bright. But since this
            parameter can be CV-controlled, you could of course also do funny
            things with it. Beware: if you set this to zero, the LEDs will
            be completely dark. This also includes possible error messages.

        maxslope1: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope2: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope3: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope4: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope5: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope6: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope7: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        maxslope8: cv
            Sets a threshold for a voltage change between two samples until
            the internal logic of the outputs assumes that
            this step is intentional and should not be smoothed out.
            A typical case where you do not want smoothing is the pitch
            output of a sequencer.

            The default value is 0.25. A value of 0.0 turns
            off smoothing altogether since the slightest voltage change
            is considered an intentional jump.

        lpfilter1: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter2: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter3: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter4: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter5: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter6: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter7: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        lpfilter8: fraction
            Configures a digital low pass filter on the output in order
            to smooth out digital noise resulting from the 's main
            loop. This loop is running somewhere between 3 and 6 kHz – depending
            on the number of circuits you use.

            Per default this filter is set to 0.25 – which means a mild
            filtering – thus still allowing fast and snappy envelopes and
            other rapidly changing signals while filtering away most of the
            digital artefacts.

            If you use an output for a slow envelope that is combined with an
            audio path in a way that you hear digital artifacts then increase
            that value. This is e.g. the case if you modulate a VCA that in
            turn modulates a very low pitched audio wave with very few harmonics
            (such as a sine or triangle wave).

            The maximum value of 1.0 leads to a very strong filtering – i.e.
            removing all fast transients. Snappy envelopes will be smoothed out
            heavily. Square wave LFOs will be converted into lower level almost
            sine waves.

        m4faderspeed: fraction
            Set the force / speed of the motor faders. Faster speeds need
            more electrical power and might wear off the faders faster. Too
            slow speeds might lead to poor operation. This value goes from 0.0
            (slowest possible speed) to 1.0 (maximum speed). If you don't use
            this parameter, some reasonable default is used that depends on the
            firmware of the M4 module.

        statusdump: trigger
            A trigger here does the same as a double “click” on the
            master's button: it creates a status dump file on the SD card.
            This trigger allows you automated control with a precise timing.
            Each dump needs a couple of milli seconds to write to the SD
            card. So better do not spam this input with a high frequency
            of triggers.

        m4notchpower: fraction
            Set the force feedback power of the M4 motor fader units when
            they operate with virtual notches. The range is from 0 (minimum
            notch power) to 1 (maximum notch power). Note: 0 does not turn the
            notches off, there is still some minimal feedback. If you don't use
            this parameter, the notch force feedback operates at some default
            power, which is dependent on the M4 firmware version.

        calibrate: trigger
            Immediately enter the calibration procedure, that's contained
            in the maintainance menu (only MASTER). Skips the menu. After
            calibration is done, resets.

        startcontrollerupgrade: trigger
            Immediately starts the firmware upgrade procedure for controllers
            like M4 and E4. After one succesfull upgrade resets the master.

        startx7upgrade: trigger
            Immediately starts the X7 firmware upgrade procedure (which is
            located at position 8 of the maintainance menu). After the upgrade
            of the X7 resets the master.

        clear: trigger
            A trigger here sends a trigger to the clear input of
            all circuits that support this. That brings the state of those
            circuits to their start state. Circuits that have presets do keep
            those presets untouched. Just the current state is affected.

            That trigger is not sent to circuits whose clear input
            is patched.

            Note: Just that part of the state is affected that is saved
            to the SD card. For example the algoquencer does not
            reset to the first step, it just clears it's current pattern.

        clearall: trigger
            A trigger here sends a trigger to the clearall input of
            all circuits that support this. That's like a global factory reset
            for all of your circuits. Everything is set to its starting state,
            including all presets of those circuits.

            That trigger is not sent to circuits whose clearall input
            is patched.

            Note: Just that part of the state is affected that is saved
            to the SD card. For example the algoquencer does not
            reset to the first step, it just clears it's current pattern.


    Outputs:

    """


    ledbrightness: Optional[str] = None
    maxslope1: Optional[str] = None
    maxslope2: Optional[str] = None
    maxslope3: Optional[str] = None
    maxslope4: Optional[str] = None
    maxslope5: Optional[str] = None
    maxslope6: Optional[str] = None
    maxslope7: Optional[str] = None
    maxslope8: Optional[str] = None
    lpfilter1: Optional[str] = None
    lpfilter2: Optional[str] = None
    lpfilter3: Optional[str] = None
    lpfilter4: Optional[str] = None
    lpfilter5: Optional[str] = None
    lpfilter6: Optional[str] = None
    lpfilter7: Optional[str] = None
    lpfilter8: Optional[str] = None
    m4faderspeed: Optional[str] = None
    statusdump: Optional[str] = None
    m4notchpower: Optional[str] = None
    calibrate: Optional[str] = None
    startcontrollerupgrade: Optional[str] = None
    startx7upgrade: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None


@dataclass
class Encoderbank:
    """Circuit encoderbank.
      Create bank of up to 8 virtual input knobs from E4 encoders

    Inputs:
        firstencoder: integer
            The first encoder to use. You can either use it's register name,
            like E8.2 for encoder 2 on controller 8. As an alternative you
            can use a number like 6. That would specify the 6 encoder of
            your setup: the encoder number 2 on your second E4.

            For each of the output jacks you use, one encoder is used,
            following the order of your controllers.

            This value is read just once when the starts.
            Making this parameter dynamic does not work.

        led1: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led2: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led3: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led4: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led5: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led6: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led7: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        led8: fraction
            You can use the rings of LEDs around the encoders as virtual
            LEDs using this parameter. This is similar to using the according
            L registers of the E4, but honors the select input.

        startvalue: cv
            This sets the value the encoder gets when you start this circuit
            for the first time or when you send trigger to clear.

            Note: the range of this value refers to the situation before
            outputscale and outputoffset is applied. So if mode
            is unused or at 0, a startvalue of 0.5 sets the encoder's virtual
            value exactly to the center – regardless of any scaling or
            offsetting that happens afterwards.

        notch: cv
            This parameter helps you to dial in exactly the center of
            the selected range, which is 0.5 in normal mode and 0.0
            in bipolar mode.

            The value of notch specifies the portion of one complete
            360 cycle of the pot during which the center position should
            be assumed. 0.1 is probably a good value.

            Notch does not work if mode selects positive or
            negative infinity.

        outputscale: cv
            The output is multiplied by this value. This is just
            for convenience and may save a copy circuit in some
            situations.

        outputoffset: cv
            After scaling the virtual value with outputscale, this
            value is being added before sending the result to the output.

        mode: integer
            Selects the possible range of the virtual value.

             0Off: the encoder is unsed, its LEDs are off
            1Normal mode: fixed range between 0.0 and 1.0
            2Bipolar mode: fixed range between -1.0 and 1.0
            3Positive infinity: open range between 0.0 and ∞
            4Negative infinity: open range between -∞ and 0.0
            5Bipolar infinity: open range between -∞ and ∞
            6Circular infinity: range is 0.0 … 1.0, but repeats over in both directions


            This setting is ignored if discrete is in use.

            Note: The mode 0 is for situations where encoders are
            overlayed with select and an encoder is unused. Setting mode = 0 can be used to disable this encoder and blank its LEDs.

        smooth: cv
            Unlike a potentiometer, an encoder does not output continous
            values but steps. If you directly wire the output of an encoder
            to a CV input of an audio module, the steps might become audible.

            Therefore the final values of the encoder are smoothed out by
            a simulation of a low pass filter. That's essentially the same as
            in the slew circuit. The smoothing is enabled per default but
            you can change it with this parameter.

            A value of 0.0 turns off smoothing and you get access to
            the tiny steps of the encoder. 1.0 selects a maximum smoothing,
            which has also the effect that fast turns of the encoder are slowed
            down a bit. The default value of 0.5 does just a mild slew limiting.

            If you use discrete, the smoothing is not applied.

        discrete: integer
            Set this to an integer number of 2 or higher to
            enable discrete mode. In this mode the encoder works like
            a rotary switch for selecting one of the numbers 0, 1,
            2 and so on. The number you set for discrete selects the
            number of positions in this “switch”. For example discrete = 4
            produces the values 0, 1, 2 or 3.

            In this mode the inputs notch, mode and smooth
            are ignored.

        snapto: cv
            Use this parameter to define a position where the encoder
            value automatically returns to if it is not turned. This behaves
            a bit like a pitch bend wheel. You can get crazy CV modulations
            if you use a dynamic CV for snapto, such as the output of an LFO.
            The encoder's value will try to follow the LFO but you can still
            turn the encoder and work “against” the LFO.

            This mechanism also works if the encoder is not selected.

        snapforce: cv
            Specifies the speed or “force” with that the encoder moves
            back to the snapto position if that is used. A force of
            0.0 deactivates snapto.

        sensivity: cv
            The sensivity determines how far you need to turn the knob to get
            which amout of value change. Per default one turn of 360 degrees
            changes to the value from 0.0 to 1.0.  A sensitivity of 2,
            doubles the speed of change, 0.5 slows it down to the half.

            If you use mode to enable infinity, there is no total
            range. In this case one turn changes the value by sensivity.

            If you use discrete, one turn of the knob changes the virtual
            switch by eight positions, if sensitivity is at 1.0, and
            accordingly faster or slower if you change that.

        autozoom: fraction
            The “auto zoom” feature allows you to fine adjust values when
            turning the knob slowly and coarse adjust when you turn it fast.
            If autozoom is at the maximum value of 1.0, turning the
            knob just slowly changes the value by super tiny amounts, while
            turning it fast operates way faster than usual. Use any value between 0.0
            and 1.0 for autozoom to select the level of this slowing
            down for slow movements.

            autozoom has no effect if discrete is used.

        color: cv
            Color of the pointer in the LED ring. Here are some
            example color values:

             0.2cyan
            0.4green
            0.6yellow
            0.73orange
            0.8red
            1.0magenta
            1.1violet
            1.2blue





        negativecolor: cv
            If you use this parameter, it defines the color of the
            LEDs in case the current logical value is negative.

        ledfill: integer
            Selects whether the LED ring displays the current value with
            just a single colored dot (ledfill = 0) or by additionally
            illuminating all LEDs between 0 and the current value in half brightness
            (ledfill = 1).

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output1: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output2: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output3: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output4: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output5: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output6: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output7: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        output8: cv
            Output the current value if the virtual encoder value
            (don't use this if you are using sharewithnext).

        button1: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button2: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button3: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button4: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button5: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button6: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button7: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

        button8: gate
            This outputs provides you with the current states of the push buttons
            in the encoders, but only if the circuit is selected. While you could do this with an extra button circuits, using this
            output is more convenient in some situations.

    """


    firstencoder: Optional[str] = None
    led1: Optional[str] = None
    led2: Optional[str] = None
    led3: Optional[str] = None
    led4: Optional[str] = None
    led5: Optional[str] = None
    led6: Optional[str] = None
    led7: Optional[str] = None
    led8: Optional[str] = None
    startvalue: Optional[str] = None
    notch: Optional[str] = None
    outputscale: Optional[str] = None
    outputoffset: Optional[str] = None
    mode: Optional[str] = None
    smooth: Optional[str] = None
    discrete: Optional[str] = None
    snapto: Optional[str] = None
    snapforce: Optional[str] = None
    sensivity: Optional[str] = None
    autozoom: Optional[str] = None
    color: Optional[str] = None
    negativecolor: Optional[str] = None
    ledfill: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None
    button1: Optional[str] = None
    button2: Optional[str] = None
    button3: Optional[str] = None
    button4: Optional[str] = None
    button5: Optional[str] = None
    button6: Optional[str] = None
    button7: Optional[str] = None
    button8: Optional[str] = None


@dataclass
class Encoder:
    """Circuit encoder.
      Provide access to a knob on the E4 controller

    Inputs:
        encoder: integer
            The encoder to use. You can either use it's register name,
            like E8.2 for encoder 2 on controller 8. As an alternative you
            can use a number like 6. That would specify the 6 encoder of
            your setup: the encoder number 2 on your second E4.

            This value is read just once when the starts.
            Making this parameter dynamic does not work.

        override: cv
            Use this parameter to convert the encoder into a mere display.
            The knob is completely ignored and the value from the input
            is used as the value that is displayed in the LED ring.

            The parameter discrete still works, so you can use the
            LED ring for displaying a discrete number such as the current
            step in a sequence.

            Also mode is honored. Values that do not fit into the
            selected range or number of discrete values will be rounded
            to the nearest allowed value.

            override honors select, so if you use select,
            it does nothing to the LEDs while the encoder circuit is not selected.

        sharewithnext: gate
            If set this to 1, the output output will not be
            used but the circuit shares it's output with the next
            encoder circuit and operates on the same virtual value
            as that. Use this if you want to control the
            same value with two different encoder circuits (which might
            be available in different contexts of your user interface).

            If you do this, make sure that both encoder circuits have
            the same settings of mode and discrete.

        movementticks: integer
            Specifies the number of encoder ticks you need to turn to
            get one trigger at movedup or moveddown. One complete
            rotation of the encoder creates 96 such ticks.

        led: fraction
            You can use the ring of LEDs around the encoder as one virtual
            LED using this parameter. This is similar to using the according
            L register of the E4, but honors the select input.

            If you set led to 1, all LEDs will get brighter or
            white, if they would be black otherwise.

        startvalue: cv
            This sets the value the encoder gets when you start this circuit
            for the first time or when you send trigger to clear.

            Note: the range of this value refers to the situation before
            outputscale and outputoffset is applied. So if mode
            is unused or at 0, a startvalue of 0.5 sets the encoder's virtual
            value exactly to the center – regardless of any scaling or
            offsetting that happens afterwards.

        notch: cv
            This parameter helps you to dial in exactly the center of
            the selected range, which is 0.5 in normal mode and 0.0
            in bipolar mode.

            The value of notch specifies the portion of one complete
            360 cycle of the pot during which the center position should
            be assumed. 0.1 is probably a good value.

            Notch does not work if mode selects positive or
            negative infinity.

        outputscale: cv
            The output is multiplied by this value. This is just
            for convenience and may save a copy circuit in some
            situations.

        outputoffset: cv
            After scaling the virtual value with outputscale, this
            value is being added before sending the result to the output.

        mode: integer
            Selects the possible range of the virtual value.

             0Off: the encoder is unsed, its LEDs are off
            1Normal mode: fixed range between 0.0 and 1.0
            2Bipolar mode: fixed range between -1.0 and 1.0
            3Positive infinity: open range between 0.0 and ∞
            4Negative infinity: open range between -∞ and 0.0
            5Bipolar infinity: open range between -∞ and ∞
            6Circular infinity: range is 0.0 … 1.0, but repeats over in both directions


            This setting is ignored if discrete is in use.

            Note: The mode 0 is for situations where encoders are
            overlayed with select and an encoder is unused. Setting mode = 0 can be used to disable this encoder and blank its LEDs.

        smooth: cv
            Unlike a potentiometer, an encoder does not output continous
            values but steps. If you directly wire the output of an encoder
            to a CV input of an audio module, the steps might become audible.

            Therefore the final values of the encoder are smoothed out by
            a simulation of a low pass filter. That's essentially the same as
            in the slew circuit. The smoothing is enabled per default but
            you can change it with this parameter.

            A value of 0.0 turns off smoothing and you get access to
            the tiny steps of the encoder. 1.0 selects a maximum smoothing,
            which has also the effect that fast turns of the encoder are slowed
            down a bit. The default value of 0.5 does just a mild slew limiting.

            If you use discrete, the smoothing is not applied.

        discrete: integer
            Set this to an integer number of 2 or higher to
            enable discrete mode. In this mode the encoder works like
            a rotary switch for selecting one of the numbers 0, 1,
            2 and so on. The number you set for discrete selects the
            number of positions in this “switch”. For example discrete = 4
            produces the values 0, 1, 2 or 3.

            In this mode the inputs notch, mode and smooth
            are ignored.

        snapto: cv
            Use this parameter to define a position where the encoder
            value automatically returns to if it is not turned. This behaves
            a bit like a pitch bend wheel. You can get crazy CV modulations
            if you use a dynamic CV for snapto, such as the output of an LFO.
            The encoder's value will try to follow the LFO but you can still
            turn the encoder and work “against” the LFO.

            This mechanism also works if the encoder is not selected.

        snapforce: cv
            Specifies the speed or “force” with that the encoder moves
            back to the snapto position if that is used. A force of
            0.0 deactivates snapto.

        sensivity: cv
            The sensivity determines how far you need to turn the knob to get
            which amout of value change. Per default one turn of 360 degrees
            changes to the value from 0.0 to 1.0.  A sensitivity of 2,
            doubles the speed of change, 0.5 slows it down to the half.

            If you use mode to enable infinity, there is no total
            range. In this case one turn changes the value by sensivity.

            If you use discrete, one turn of the knob changes the virtual
            switch by eight positions, if sensitivity is at 1.0, and
            accordingly faster or slower if you change that.

        autozoom: fraction
            The “auto zoom” feature allows you to fine adjust values when
            turning the knob slowly and coarse adjust when you turn it fast.
            If autozoom is at the maximum value of 1.0, turning the
            knob just slowly changes the value by super tiny amounts, while
            turning it fast operates way faster than usual. Use any value between 0.0
            and 1.0 for autozoom to select the level of this slowing
            down for slow movements.

            autozoom has no effect if discrete is used.

        color: cv
            Color of the pointer in the LED ring. Here are some
            example color values:

             0.2cyan
            0.4green
            0.6yellow
            0.73orange
            0.8red
            1.0magenta
            1.1violet
            1.2blue





        negativecolor: cv
            If you use this parameter, it defines the color of the
            LEDs in case the current logical value is negative.

        ledfill: integer
            Selects whether the LED ring displays the current value with
            just a single colored dot (ledfill = 0) or by additionally
            illuminating all LEDs between 0 and the current value in half brightness
            (ledfill = 1).

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output: cv
            Outputs the current virtual value of this circuit.
            Don't use this if you are using sharewithnext.

        button: gate
            This output provides you with the current state of the push button
            in the encoder, but only if the circuit is selected. While you could do this with an extra button circuit, using this
            output is more convenient in some situations. While the circuit is
            not selected, the output is set to 0.

        moveddown: trigger
            Outputs a trigger whenever you have turned the encoder left (counter
            clock wise) by a certain amount (which can be altered by movementticks.
            Beware: If you turn too fast, triggers might overlap and merge together.

        movedup: trigger
            Outputs a trigger whenever you have turned the encoder right (
            clock wise) by a certain amount (which can be altered by movementticks).
            Beware: If you turn too fast, triggers might overlap and merge together.

        valuechanged: trigger
            Outputs a trigger whenever the virtual value has changed.

    """


    encoder: Optional[str] = None
    override: Optional[str] = None
    sharewithnext: Optional[str] = None
    movementticks: Optional[str] = None
    led: Optional[str] = None
    startvalue: Optional[str] = None
    notch: Optional[str] = None
    outputscale: Optional[str] = None
    outputoffset: Optional[str] = None
    mode: Optional[str] = None
    smooth: Optional[str] = None
    discrete: Optional[str] = None
    snapto: Optional[str] = None
    snapforce: Optional[str] = None
    sensivity: Optional[str] = None
    autozoom: Optional[str] = None
    color: Optional[str] = None
    negativecolor: Optional[str] = None
    ledfill: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output: Optional[str] = None
    button: Optional[str] = None
    moveddown: Optional[str] = None
    movedup: Optional[str] = None
    valuechanged: Optional[str] = None


@dataclass
class Encoquencer:
    """Circuit encoquencer.
      Performance sequencer using E4 encoders

    Inputs:
        zorder: integer
            This parameter changes to order of the encoders in the sequence.
            The natural order (at the default value of zorder = 0) assignes
            the sequence steps to the encoders in their order of appearance
            in your controllers. The step counter moves downwards the four
            encoders of one E4, then jumps to the first encoder of the next
            E4 and so on. There are four different choices. The choices
            2 and 3 are for situations where you mount the master
            at the right of your controllers.

             0sequence step moves downwards, E4 by E4
            1sequence step moves left to right, row by row
            2Like 0, but start with last E4
            3right to left, row by row


            The name zorder resembles
            the fact that if you draw the order of the encoders with a
            pen on a paper, the setting zorder = 1 looks like three
            times the letter Z.

        nume4s: integer
            Define the number of E4 modules the sequencer should
            occupy if zorder is 1 or 3. If you don't
            used this variable, the number is set to numfaders / 4.
            If you have eight E4 and want to create a sequencer with just
            the first row, set numfaders = 8 and zorder = 1
            and nume4s = 8. For using the first two rows, do the
            same with numfaders = 16. By choosing a specific
            encoder to be the first, with firstfader, you
            can move this rectangle of encoders to a different position
            in your E4 matrix.

        ledpreview: gate
            Set this to 1 if you want the inactive states
            (or possible settings) to be illuminated in the LED ring.

        firstfader: integer
            First M4 fader of the sequencer (starting with 1). If you
            omit this, it starts at the first fader of your first M4.

        numfaders: integer
            Number of faders to use for your sequencer. The typical
            numbers are 4, 8, 16 and 32. 32 is the maximum (eight
            M4 units). If you omit this, all of your M4 faders
            will be used.

        numsteps: integer
            Number of steps your sequence consists of (at maximum).
            The number of steps can be greater than the number of faders.
            In that case use page for paging your faders so that
            you can edit all of the steps. Having the number of steps
            less than the faders, makes no sense – it's just a waste
            of faders. The maximum number of steps is 32.

            If you don't set this parameter, the number of steps
            will be set to the number of faders.

            Note: changing this setting dynamically can provoke various
            surprising behaviours. For example the number of pages
            (see parameter page) might be reduced. Or the end
            marker is forcibly moved around. If you want to change the
            length of the sequence via CV, better use endstep
            or autoreset.

            Another note: Setting numsteps will not restrict
            the number of faders. If you set numsteps = 4 but have
            eight faders available, the circuit will use all these,
            even if faders 5, 6, 7 and 8 will be useless. You need to
            set numfaders = 4 in this situation.

        page: integer
            Use this parameter, if you have less faders than steps.
            The first page is 0, not 1.
            For example if you have 4 faders but 16 steps, you can
            select between the four “pages” of four faders each, by
            settings bar to 0, 1, 2 or 3.
            The output of a buttongroup with one button
            per page is a good match for this parameter.

        clock: trigger
            Patch an input clock here. If you want to use ratcheting,
            that clock needs to be stable and regular, because the sequencer
            needs to interpolate the clock and create evenly distributed
            new beats within two clock ticks. If you don't use ratching,
            you can use any rhythm you like here – may it be shuffled,
            euklidean, the output from another sequencer or whatever you
            like. Each clock tick will advance the sequence to the next
            step (or to the next repition of the current step).

        taptempo: trigger
            If your clock is not steady but might be stopped and restarted,
            you should patch a steady clock here. This avoids problems
            with the computation of the gate length right after starting
            the clock. The tap tempo computation needs a series of at least
            two clock pulses so the gate length of the first step is wrong
            after the clock has stopped for a while.

        reset: trigger
            A trigger here resets the sequencer to its start step. The
            next clock tick (or a tick that is roughly at the same time as
            the reset) will play step 1. Note: If there is a reset without
            a clock tick at the same time, the sequencer will go to “step 0”,
            which is a special state where it waits for the clock to advance
            to the first step. Without that fancy logic, a reset plus clock
            would skip step 1 and start with step 2.

        run: gate
            If you set this input to 0, the sequencer will ignore all
            incoming clock ticks. It stops. The default of 1 is normal
            operation, where it runs. This input is a better way to temporarily
            stop the sequencer than to stop the clock. The reason: for computing
            the gate length and ratchets a steady input clock is needed. If
            you stop the clock, the next gate length and ratches right after
            the next start will have the wrong duration since at least two
            clock ticks are neccessary for computing its speed.

            Note: This input is not a replacement for mute, since a
            muted sequencer leaves the clock running and advances steps.
            It just mutes the gate output.

        composemode: gate
            Enabling “compose mode” makes it easier to find the right note in
            a step, when creating more complex melodies.  When composemode
            is set to 1, the sequencer stops clocking. Instead – every
            time you change the CV of a step, it immediately jumps to that step,
            outputs the changed CV and opens the gate for a short time, so you
            can listen to the changed note.

        mute: gate
            If you set this to 1, the gate output of the sequencer
            is muted (will always be 0). Any changes of the CV output still
            happen.

        cvbase: cv
            Here you set the voltage the sequencer will output if the
            CV fader is at the bottom position. The allowed range is -1
            … 1 (which is the same as the range from -10 V to +10 V,
            if you output the CV directly to an output).

        cvrange: cv
            CV range of the faders. So the resulting CV lies somewhere
            between cvbase and cvbase + cvrange. The CV
            range cannot be negative and is capped at 1. If you need a greater
            range, consider multiplying the output value of the cv
            output of the sequencer.

        invert: gate
            Inverts the CV or pitch output. This is like mirroring the fader
            position. Now if the fader is up, the output is low and vice versa.
            In scale quantized mode, the melody still stays within the scale.

        quantize: integer
            Switches on quantization in two levels. At 0, the faders run
            freely and output a continous CV.

            At 1, the output is quantized to semitones, which is 1/12V
            steps. Also the faders will get artifical notches – one for each
            semitone.  That is, unless your range is too large. The maximum number
            of notches with force feedback is 25, so if your range exceeds two
            octaves (0.2), the notches are turned off.

            At 2, the output is quantized to the scale that root and degree
            define. Furthermore the individual scale notes can be switched on or
            off with the parameters select1, select3
            and so on. Note: the root input does not select the lowest
            note of the CV range. That is still set with cvbase. It is
            just used for selecting the scale.

            0no quantization
            1quantize to semitones (1/12V steps)
            2quantize to the scale set by root and degree



        cvnotches: integer
            Usually the CVs of the steps are ment to be note pitches
            (when quantize is 1 or 2), or just free CVs (quantize = 0).
            There is an alternative mode, however, that allows you to
            assign integer values like 0, 1, 2 and so on to each step.

            To do this set cvnotches to a value of 2 or greater. This
            defines the number of discrete values (and hence notches) for
            each step and put CVs of the sequence into notched mode.
            1 makes no sense, of course, since in this “pitch
            bend mode” the faders would always return to the neutral position.

            In notched mode the cv output does not output a pitch but
            a notch number starting from 0. cvbase, cvrange and
            quantize are ignored.

            The maximum number of notches is 127, but the haptic force
            feedback of the motor faders is disabled starting at 26.

        shiftsteps: integer
            Shifts all your steps by that number to the left (negative
            numbers shift to the right). So if shiftsteps is 1, right
            after a reset, the sequencer will not play step 1, but step 2.
            The shifting wraps around at the end of your sequence, so if
            you have 24 steps and shift is 1, the sequencer will play step 1
            instead of step 24.

            Note: Other things like startstep, endstep, playmode,
            from and autoreset take place after shifting.

        startstep: integer
            Sets the first step to be used.  This means that after a reset or
            when the sequencer comes to the end of the sequence, it will begin
            at this step.

            There is also a way for settings start and end with buttons
            (see below at buttonmode). If you use the interactive
            mode, the startstep and endstep settings will be
            overridden. The are reactived if you clear everything.

            Note: startstep and endstep take place after applying
            shiftsteps.

        endstep: integer
            Sets the last of the steps to be played. The default is to play
            all steps. After playing the end step, the sequencer moves on to
            the start step at the next clock tick.

            If startstep is equal to endstep, the sequence
            just consists of one single step.

            Settings startstep larger then endstep is allowed
            and reverses the playing order.

        form: integer
            This is an advanced feature that allows you to slice your
            steps into two or three parts and create musical song forms
            like AAAB or ABAC. Each of the parts A, B or C are then played
            according to the playmode.

            The form AAAB, for example, creates a 32 step form from
            just 16 steps, by playing the first 8 steps three times and
            then the second 8 steps once.

            The following forms are available:

            0A (forms are basically deactivated)
            1AAAB
            2AABB
            3ABAC
            4AAABAAAC
            5AB
            6AAB


            Notes:


              * The splitting of the steps into parts takes place
            after accounting for startstep and endstep.

              * Forms with A, B and C split the pattern into
            three parts. These parts can only be of equal size if the
            number of steps is dividable by 3, of course.

              * The pattern AB is really not the same as A, e.g when
            direction is set 1 (reverse). In that case each of the
            parts is played backwards, but the parts themselves move
            forwards on your steps.


        direction: gate
            Sets the general direction in which the sequencer moves through
            the steps. 0 means forwards and 1 means backwards.

        pingpong: gate
            If set to 1, the sequencer will change the direction every time
            it reaches the start or end of the sequence.

        pattern: integer
            Selects one of a list of movement patterns. That way, the sequence
            steps are not played in linear order but in a more sophisticated
            movement.  Available pattern are:

             0go step by step to the sequence (normal)→
            1two steps forward, one step backward→ → ←
            2double step forward, one step backward⇒ ←
            3double step forward, double step backward, single step forward⇒ ⇐  →
            4double step forward, single step forward, double step backward, single step forward⇒ → ⇐ →
            5random single step forward or backward↔
            6go forward by a small random number of steps→ × ? 
            7random jump to any allowed (other) note⇕




        repeatshift: integer
            This is a number in the range -24 … +24. If you set this
            to non-zero, each repetition of a step shifts the played note
            by that many notes within the selected scale notes. This only
            has effect on steps where the number of repeats is greater than 1.
            Also it is only is applied when the quantize = 2.

        ratchetshift: integer
            This is a number in the range -24 … +24. If you set this
            to non-zero, each ratchet of a step shifts the played note
            by that many notes within the selected scale notes. This only
            has effect on steps where the number of ratchets is greater than 1.
            Also it is only is applied when the quantize = 2.

            If you combine ratchetshift with repeatshift, both
            shifts are added together. And the ratchet shifting is reset
            for each repetition of the step.

        accumulatorrange: integer
            Using this parameter enables the pitch accumulator. The value sets
            the maximum value the accumulator can get.  The maximum is 16. If
            you set this to 0, the fader mode for pitch randomization still
            is in the special mode where the upper four positions control the
            impact of the accumulator.

            Please consult the manual of motoquencer for details on
            the pitch accumulator.

        autoreset: integer
            If set to non-zero, automatically issues a reset (just like a
            trigger to reset) every N clock ticks.

        metricsaver: gate
            The Metric Saver ™ helps you to reliably come back
            to your original metric and time after playing around with all
            sorts of parameters that change the played number of steps in
            the sequence.  These are: startstep, endstep (also when
            changed interactively), form, direction, pingpong, pattern, autoreset and repeats and skips of individual steps.
            Therefore it counts the actual number of clock cycles since the
            last external reset (or system start). And when all of these
            features are deactivated, it snaps back the clock to the position
            it would have been by now if you never had played around with
            all the funny stuff.

            That way, during a live performance, you can safely play around
            with all this polymetric and otherwise time disrupting stuff and
            as soon as you clean up your mess – voila: you are back on track
            and in sync with the rest of the “band”.

            The metric saver is turned on by default. But you can disable
            it by setting the parameter to 0.

        fadermode: integer
            Switches the current meaning of the motor faders. You probably
            want to connect the output of a buttongroup here.
            Here are the possible modes:

            0pitch / CV
            1randomize CV
            2gate propability
            3repeats (up to 16)
            4gate pattern
            5ratchets (up to 8)
            6gate
            7skip


        buttonmode: integer
            Switches the current meaning of the touch buttons below the faders.
            You probably want to connect the output of a buttongroup
            here. Here are the possible modes:

            0gates
            1start / end
            2gate pattern
            3skip


        holdcv: gate
            This setting determines wether the CV output changes every
            time the sequencer moves to the next step or just when that
            step is active (a gate is being played). The latter is the
            default. But if you set this to 0, the CV values of
            steps without gates will also influence the output CV.

            Note: regardless of this setting, the CV will never change
            inbetween. Any change of the CV faders, the cvbase
            and cvrange and so on will only take effect when the
            next step is played. This also ensures that repeats or ratchets
            are always in the same pitch.

        defaultcv: cv
            Set the CV the steps should be set to on a trigger to
            clear. That value must be within the range set by cvbase
            and cvrange, or it will be truncated to that range.

            If you have set cvnotches, however, the value is expected
            to be an integer in the range 0 ... cvnotches - 1.

        defaultgate: gate
            Here you set to which state (on / off) the gates should be
            set on a trigger to clear.

        clearskips: trigger
            A trigger here removes the “skip” setting from all steps.

        clearrepeats: trigger
            A trigger here resets the number of repeats to 1 for each step.

        clearstartend: trigger
            A trigger here clears the manual settings of the start and
            end step. So the sequence will be played in its full length
            (again) .

        gatelength: cv
            The gate length in input clock cycles. A value of 0.5
            thus means half a clock cycle. A steady input clock is needed for
            this to work. Please note that if the gate length is >= 1.0,
            two succeeding notes will get a steady gate, which
            essentially means legato.

            If you don't use a steady clock, set this parameter to 0. This
            will output a minimal gate length of about 10 ms (basically just
            a trigger).

        keyboardmode: integer
            This input sets how a keyboard, that is hooked to keyboardcv,
            and keyboardgate should be used for directly playing notes.
            You can set it to 0, 1 or 2.

             0ignore the keyboard inputs
            1keyboard and sequencer play together, keyboard has precedence
            2mute sequencer, just play keyboard




        keyboardcv: voltperoctave

            The pitch input of a keyboard. This is used for playing
            along with the keyboardmode or recording with recordmode.

        keyboardgate: gate

            The gate input of a keyboard. A positive gate enabled play
            along (see keyboardmode) and also recording, if recordmode is set accordingly.

        recordmode: integer

            Use this input to record melodies played with a keyboard
            (namely keyboardcv and keyboardgate) into the
            sequencer. There are three possible settings:

             0don't record
            1record, notes longer than one step will automatically tie steps via the gate pattern
            2record, don't tie notes. Ignore the length of the input note




        recordsilence: gate
            When this input is set to 1 while recording, silence will
            be recorded while keyboardgate is off. Otherwise you can
            just add notes to the sequence.

        copy: trigger
            A trigger here copies the current page of the sequence to
            an internal clipboard. The clipboard is not part of any preset and
            is also not saved to the SD card. It can be used later for pasting
            it's data to another preset or another page of a sequence.

        paste: trigger
            A trigger here copies the steps from the clipboard to the
            current page.

        pastefaders: trigger
            This is like paste, but just the values of the faders
            of the current fadermode are copied.

        pastebuttons: trigger
            This is like paste, but just the values of the faders
            of the current buttonmode are copied. Note: the button
            mode “start / end” is not supported by copy and paste.

        linktonext: gate
            This settings allows you to create motoquencer tracks that
            have more than one CV or gate output for each step. If you
            set this to 1, the next motoquencer circuit
            in your patch will by synchronized to this one. This means
            that it always plays the same step number – including all
            fancy operating like shiftsteps, startstep,
            endstep, form, pattern and autoreset.
            All those inputs and also clock and reset
            are ignored by the next motoquencer.

            The same holds for the “repeats” and “skip” setting of the steps.

            fadermode and buttonmode are extended to
            the next motoquencers by adding 10 for each motoquencer to
            follow. So fadermode = 10 will show the CV of next motoquencer
            in the faders. fadermode = 11 the CV randomization of the
            next motoquencer. fadermode = 20 show the CV of the
            third linked motoquencer and so on.

            Don't set fadermode or buttonmode on the linked
            motoquencers. They will be ignored there.

            Note: The linktonext setting cannot by dynamically
            changed. It needs to be fixed 0 or 1. You cannot
            use any button or internal cable or other methods to change
            it while the patch is running.

        luckychance: fraction
            Sets tha chance for a step to be affected by the next
            “lucky” operation (see triggers below).

        luckyscope: integer
            Determines which part of the sequence is affected by
            the “lucky” operations. Depending on this setting the
            following steps are affected:

             0All steps between the current start and end step
            1All steps
            2All steps between start and end on the current page
            3All steps on the current page




        luckyamount: fraction
            Sets the amount of change that a “lucky” operation does to
            a step. The meaning depends on the operation. See the parameters
            below.

        luckycvbase: fraction
            This parameter affects only the operation luckycvs and
            luckyfaders when the fader mode is set to 0.
            It adds a fixed amount of CV to the random result, so that
            lies in the range luckycvbase … (luckycvbase + luckyamount).

        luckyfaders: trigger
            Moves the currently selected faders (according to
            fadermode) to new random positions. luckyamount
            sets the maximum value of the fader, where 1 allows the
            maximum.

        luckybuttons: trigger
            Randomly toggles the currently selected buttons (according
            to buttonmode). luckyamount
            only has an effect when the gate patterns are selected, since
            here, four different values are possible. luckamount
            restricts them if it is lower than 1.

        luckycvs: trigger
            Replaces the affected steps' CVs with a new random CVs. The
            lowest possible CV is cvbase. If luckyamount is 1,
            the highest possible CV is cvbase + cvrange, otherwise
            it is cvbase + luckyamount × cvrange.

        luckycvdrift: trigger
            Modifies the affected steps' CV randomly up or down. They will stay
            in the CV range set by cvbase and cvrange. luckyamount
            controls the amount of change.

        luckyspread: trigger
            First computes the average CV of all steps. Then changes
            the CV values of the affected steps such that their distance to
            the average increases or decreases.  If luckyamount
            is greater than 0.5, the distance is increased. Otherwise it
            is decreased.

        luckyinvert: trigger
            Inverts the CVs of the affected steps within the allowed CV
            range. luckyamount has no influence.

        luckyrandomizecv: trigger
            Sets the “randomize CV” values of the affected steps to
            random values (yes, this is double randomization). The luckyamount
            sets the maximum randomization value that will be set.

        luckygates: trigger
            Sets the gates of the affected steps randomly to on or off. The
            chance for on is determined by luckyamount. So with
            luckyamount = 0 you clear all gates and with luckyamount = 1
            you set all gates.

        luckyskips: trigger
            Sets the “skip this step” setting of the affected steps
            randomly to skip or normal. The chance for skip is determined by luckyamount.

        luckyties: trigger
            Sets the “tie this step to the next” setting of the affected steps
            randomly to tie or normal. This is the same as setting the gate pattern
            to the upper most position. The chance for tie is determined by luckyamount.

        luckygatepattern: trigger
            Randomizes the gate pattern of the selected steps (there are four
            different values: once, all, hold and tie). Use luckyamount
            to reduce that set.

        luckygateprob: trigger
            Sets the “randomize gate” values of the affected steps to
            random values (yes, this is double randomization). The luckyamount
            sets the minimum randomization value that will be set (yes, this
            is inverted). So with luckyamount = 1 you disable randomization
            and make the gates play always. With luckymount = 0 you set
            the gate propability to the lowest possible value (still not 0).

        luckyrepeats: trigger
            Randomly sets the number of repeats of the affected steps to
            something between 1 and 16 (the maximum). The luckyamount determines
            the maximum repetition number, where 1 stands for a maximum of 16
            repetitions.

        luckyratchets: trigger
            Randomly sets the number of ratches of the affected steps to
            something between 1 and 8 (the maximum). The luckyamount determines
            the maximum ratchet number, where 1 stands for a maximum of 8
            ratchets.

        luckyshuffle: trigger
            Randomly swaps all affected affected steps (their playing
            order) together will all their attributes. luckyamount has no
            influence.

        buttoncolor: cv
            Set a user defined color for the gate buttons. This
            color is only used when buttonmode = 0. The main purpose
            of this option is to allow a separate color for the gate
            button in a linked sequencer, that does something else than
            gates.

        luckyreverse: trigger
            Reverses the playin gorder of the affected steps. luckyamount
            has not influence.

        root: integer
            Set the root note here. 0 means C, 1 means
            C♯, 2 means D and so on. If you multiply
            the value of an input like I1 with 120, then you can use a 1V/Oct
            input for selecting the root note via a sequencer, MIDI keyboard
            or the like.
            Also then you are compatible with the ROOT CV input of the Sinfonion.

             0C
            1C♯
            2D
            3D♯
            4E
            5F
            6F♯
            7G
            8G♯
            9A
            10A♯
            11B
            12C




        degree: integer
            Set the musical scale. This is a number from 0 to 107.
            Below are the first 12 and most important scales. You find a list
            of all 108 scales on page 105.

             0lyd – Lydian major scale (it has a ♯ 4)
            1maj – Normal major scale (ionian)
            2X^7 – Mixolydian (dominant seven chords)
            3sus – mixolydian with 3/4 swapped
            4alt – Altered scale
            5hm^5 – Harmonic minor scale from the 5
            6dor – Dorian minor (minor with ♯ 13)
            7min – Natural minor (aeolian)
            8hm – Harmonic minor (♭ 6 but ♯ 7)
            9phr – Phrygian minor scale (with ♭ 9)
            10dim – Diminished scale (whole/half tone)
            11aug – Augmented scale (just whole tones)


            Note: Alltogether there are 108 scales. Please see page 105 for a complete list

        select1: gate
            Gate input for selecting the root note as being an
            allowed interval. When you want to create a playing interface
            for live operation you can patch the output of a toggle button
            (made with the circuit [button]) here.

            Note: When all select and selectfill inputs are 0,
            automatically all seven scale notes are selected, i.e.
            select1 ... select13 will be set to one.

        select3: gate
            Gate input for selecting the 3.

        select5: gate
            Gate input for selecting the 5.

        select7: gate
            Gate input for selecting the 7.

        select9: gate
            Gate input for selecting the 9 (which is the same
            as the 2).

        select11: gate
            Gate input for selecting the 11 (which is the same
            as the 4).

        select13: gate
            Gate input for selecting the 13 (which is the same
            as the 6).

        selectfill1: gate
            Selects the alternative 9 (i.e.
            the 9 that is not in the scale.

        selectfill2: gate
            Selects the alternative 3 (i.e.
            the 3 that is not in the scale).

        selectfill3: gate
            Selects the alternative 4 or 5. In
            most cases this is the diminished 5.

        selectfill4: gate
            Selects the alternative 13 (i.e.
            the 13 that is not in the scale).

        selectfill5: gate
            Selects the alternative 7 (i.e.
            the 7 that is not in the scale).

        harmonicshift: integer
            This input can reduce harmonic complexity by disabling some of
            the scale or non-scale notes. It is an idea first found in the
            Sinfonion and also provided by the circuit sinfonionlink.

            harmonicshift is staged after the select... inputs
            and further filters out (disables) notes based on their relation
            to the current scale. This means that first the 12 select... inputs
            select a subset of the 12 possible notes. After that harmonicshift
            can reduce this set further (it will never add notes).

            If harmonicshift is not zero, depending on its value some or
            more of the scale notes are disabled, even if they would be allowed by
            select....  Or in other words: the harmonic material is reduced.

            You also can use negative values. These create rather strange sounds
            by removing the simple chord functions instead of the complex
            ones first.

            Here are the possible values:

             0off – all selected notes are allowed
            1disable all fill notes (non-scale notes)
            2disable fills and 11
            3disable fills, 11 and 13
            4disable fills, 11, 13 and 9
            5disable fills, 11, 13, 9 and 7
            6disable fills, 11, 13, 9, 7 and 3
            7disable fills, 11, 13, 9, 7, 3 and 5
            -1disable the root note
            -2disable the root note and the 5
            -3disable root, 3, 5
            -4disable root, 3, 5, 7
            -5disable root, 3, 5, 7, 9
            -6disable root, 3, 5, 7, 9 and 13
            -7disable all scale notes (fill notes untouched)




        noteshift: integer
            Shifts the resulting output note(s) by this
            number of scale notes up or down (if negative). So the output
            note still is part of the scale but may be a note that is none
            of the selected ones. The maximum shift range is limited to
            -24 … +24.

        selectnoteshift: integer
            Shifts the output note by this
            number of selected scale notes up or down (if negative).
            If you use noteshift at the same time, first selectnoteshift is applied, then noteshift. The maximum shift range
            is limited to -24 … +24.

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            This value is being added to the output pitch when not
            in tuning mode. It can be used for musical transposition
            or adding a vibrato.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        cv: cv
            The CV output (or pitch output, if you use quantize).

        gate: gate
            The gate output.

        startofsequence: trigger
            Outputs a trigger whenever the sequencer starts playing
            from the beginning. This can be used for synchronizing with other sequencers.
            An external reset will also cause this output to trigger.

        startofpart: trigger
            Outputs a trigger whenever a form part starts again.
            This is only interesting when you use form.

        startstepout: integer
            Outputs the current start step. This is useful in case it has
            been interactively set with the buttons and you need that information
            for another circuit.

        endstepout: integer
            Outputs the current end step. This is useful in case it has
            been interactively set with the buttons and you need that information
            for another circuit.

        currentstep: integer
            Outputs the number of the step that is currently being played
            (starting from 0).

        currentpage: integer
            Outputs the number of the fader page that is currently played,
            i.e. the value you would have to feed into page in order to
            see the currently being played step.

        accumulator: integer
            The current value of the pitch accumulator (an integer number
            in the range 0 … 16.

    """


    zorder: Optional[str] = None
    nume4s: Optional[str] = None
    ledpreview: Optional[str] = None
    firstfader: Optional[str] = None
    numfaders: Optional[str] = None
    numsteps: Optional[str] = None
    page: Optional[str] = None
    clock: Optional[str] = None
    taptempo: Optional[str] = None
    reset: Optional[str] = None
    run: Optional[str] = None
    composemode: Optional[str] = None
    mute: Optional[str] = None
    cvbase: Optional[str] = None
    cvrange: Optional[str] = None
    invert: Optional[str] = None
    quantize: Optional[str] = None
    cvnotches: Optional[str] = None
    shiftsteps: Optional[str] = None
    startstep: Optional[str] = None
    endstep: Optional[str] = None
    form: Optional[str] = None
    direction: Optional[str] = None
    pingpong: Optional[str] = None
    pattern: Optional[str] = None
    repeatshift: Optional[str] = None
    ratchetshift: Optional[str] = None
    accumulatorrange: Optional[str] = None
    autoreset: Optional[str] = None
    metricsaver: Optional[str] = None
    fadermode: Optional[str] = None
    buttonmode: Optional[str] = None
    holdcv: Optional[str] = None
    defaultcv: Optional[str] = None
    defaultgate: Optional[str] = None
    clearskips: Optional[str] = None
    clearrepeats: Optional[str] = None
    clearstartend: Optional[str] = None
    gatelength: Optional[str] = None
    keyboardmode: Optional[str] = None
    keyboardcv: Optional[str] = None
    keyboardgate: Optional[str] = None
    recordmode: Optional[str] = None
    recordsilence: Optional[str] = None
    copy: Optional[str] = None
    paste: Optional[str] = None
    pastefaders: Optional[str] = None
    pastebuttons: Optional[str] = None
    linktonext: Optional[str] = None
    luckychance: Optional[str] = None
    luckyscope: Optional[str] = None
    luckyamount: Optional[str] = None
    luckycvbase: Optional[str] = None
    luckyfaders: Optional[str] = None
    luckybuttons: Optional[str] = None
    luckycvs: Optional[str] = None
    luckycvdrift: Optional[str] = None
    luckyspread: Optional[str] = None
    luckyinvert: Optional[str] = None
    luckyrandomizecv: Optional[str] = None
    luckygates: Optional[str] = None
    luckyskips: Optional[str] = None
    luckyties: Optional[str] = None
    luckygatepattern: Optional[str] = None
    luckygateprob: Optional[str] = None
    luckyrepeats: Optional[str] = None
    luckyratchets: Optional[str] = None
    luckyshuffle: Optional[str] = None
    buttoncolor: Optional[str] = None
    luckyreverse: Optional[str] = None
    root: Optional[str] = None
    degree: Optional[str] = None
    select1: Optional[str] = None
    select3: Optional[str] = None
    select5: Optional[str] = None
    select7: Optional[str] = None
    select9: Optional[str] = None
    select11: Optional[str] = None
    select13: Optional[str] = None
    selectfill1: Optional[str] = None
    selectfill2: Optional[str] = None
    selectfill3: Optional[str] = None
    selectfill4: Optional[str] = None
    selectfill5: Optional[str] = None
    harmonicshift: Optional[str] = None
    noteshift: Optional[str] = None
    selectnoteshift: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    cv: Optional[str] = None
    gate: Optional[str] = None
    startofsequence: Optional[str] = None
    startofpart: Optional[str] = None
    startstepout: Optional[str] = None
    endstepout: Optional[str] = None
    currentstep: Optional[str] = None
    currentpage: Optional[str] = None
    accumulator: Optional[str] = None


@dataclass
class Euklid:
    """Circuit euklid.
      Euclidean rhythm generator

    Inputs:
        clock: gate
            Patch a clock signal here. It does not need to be steady –
            even if this is the most usual application. Note: this input is classified
            as a gate input, since the length of the gate is being
            preserved when forwarded to output and offbeats.

        reset: trigger
            A trigger here resets the pattern to the start

        outputsignal: cv
            Usually on active steps euklid just lets the original
            input clock get through to the output. If this parameter is
            used, it will be sent to the output on active steps instead.
            The easiest application is just setting it to 1.
            The output will then become 1 the whole time while
            the current step is active. This is useful if you want to
            use euklid as modulation CV rather than as trigger.

        length: integer
            The length of a pattern. This is interpreted as an integer number,
            which must be greater than 0. If it is not then 1 is assumed.
            If you CV control the length, use multiplication. The maximum accepted
            length is 64.

        beats: integer
            The number of active beats that should be distributed amongst
            the length steps. If that number is greater than length,
            it is capped to that number.

        offset: integer
            rotates or shifts the pattern by that number of steps. This number
            can be positive or negative.


    Outputs:
        output: gate
            Output of the beats in the current pattern.
            The gate length is directly taken from
            the input clock – just as the voltage.

        offbeats: gate
            Here those impulses will be output where there is no
            beat in the pattern.

    """


    clock: Optional[str] = None
    reset: Optional[str] = None
    outputsignal: Optional[str] = None
    length: Optional[str] = None
    beats: Optional[str] = None
    offset: Optional[str] = None
    output: Optional[str] = None
    offbeats: Optional[str] = None


@dataclass
class Explin:
    """Circuit explin.
      Exponential to linear converter

    Inputs:
        input: cv
            Patch an exponential envelope output or a similar signal here. This
            value must be positive or otherwise it will be set to 0.0.

        startvalue: cv
            The assumed maximum value of the input signal (the start voltage
            from where it decays in an exponential way.

        endvalue: cv
            The value at which it is assumed to be zero (at which the linear
            output will be set to zero. This value must be positive. It is forced
            to be >=  0.001.

        mix: fraction
            Sets the mix between the “dry” and “wet” signal: At 0.0 the
            output is the same as the input. At 1.0 the output is the linear
            curve. At a value in between it is some average. You are even allowed
            to used values > 1.0. A value of 2.0 will overcompensate
            and bend the curve beyond linearity into a curve some modularists would
            call logarithmic.


    Outputs:
        output: cv
            Here comes the resulting linear output

    """


    input: Optional[str] = None
    startvalue: Optional[str] = None
    endvalue: Optional[str] = None
    mix: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Faderbank:
    """Circuit faderbank.
      Create multiple virtual faders in M4 controller

    Inputs:
        firstfader: integer
            First M4 fader of the virtual fader bank (starting with 1).

        notches: integer
            Number of artifical notches. 0 disables the notches.
            1 creates a pitch bend wheel. 2 creates a binary
            switch with the output values 0 and 1. Higher
            number create that number of notches. E.g. 8 creates
            eight notches and output will output one of the
            value 0, 1, ... 8.

            The maximum number of notches is 201. But if you select
            more than 25 notches, the force feedback is turned off as the
            notches would get too small to work.

        startvalue: cv
            This sets the value the faders should get when the circuit
            starts for the first time or when you send a trigger to clear.

        ledcolor: cv
            When you use this input, it will set the color of the
            LED below the faders, when the circuit is selected. If the
            LED is off, this setting has now impact.

        ledvalue1: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue2: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue3: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue4: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue5: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue6: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue7: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue8: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue9: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue10: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue11: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue12: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue13: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue14: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue15: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        ledvalue16: cv
            When you use this input, it will override the brightness
            of the LEDs below the faders, but just when this circuit
            is selected.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output1: cv
            The current values of the virtual motor faders are output
            here.

        output2: cv
            The current values of the virtual motor faders are output
            here.

        output3: cv
            The current values of the virtual motor faders are output
            here.

        output4: cv
            The current values of the virtual motor faders are output
            here.

        output5: cv
            The current values of the virtual motor faders are output
            here.

        output6: cv
            The current values of the virtual motor faders are output
            here.

        output7: cv
            The current values of the virtual motor faders are output
            here.

        output8: cv
            The current values of the virtual motor faders are output
            here.

        output9: cv
            The current values of the virtual motor faders are output
            here.

        output10: cv
            The current values of the virtual motor faders are output
            here.

        output11: cv
            The current values of the virtual motor faders are output
            here.

        output12: cv
            The current values of the virtual motor faders are output
            here.

        output13: cv
            The current values of the virtual motor faders are output
            here.

        output14: cv
            The current values of the virtual motor faders are output
            here.

        output15: cv
            The current values of the virtual motor faders are output
            here.

        output16: cv
            The current values of the virtual motor faders are output
            here.

        button1: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button2: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button3: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button4: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button5: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button6: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button7: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button8: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button9: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button10: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button11: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button12: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button13: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button14: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button15: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

        button16: gate
            Outputs the current value of the touch buttons of the
            faders to these output, when this circuit is selected. When
            the circuit is not selected, 0 is output.

    """


    firstfader: Optional[str] = None
    notches: Optional[str] = None
    startvalue: Optional[str] = None
    ledcolor: Optional[str] = None
    ledvalue1: Optional[str] = None
    ledvalue2: Optional[str] = None
    ledvalue3: Optional[str] = None
    ledvalue4: Optional[str] = None
    ledvalue5: Optional[str] = None
    ledvalue6: Optional[str] = None
    ledvalue7: Optional[str] = None
    ledvalue8: Optional[str] = None
    ledvalue9: Optional[str] = None
    ledvalue10: Optional[str] = None
    ledvalue11: Optional[str] = None
    ledvalue12: Optional[str] = None
    ledvalue13: Optional[str] = None
    ledvalue14: Optional[str] = None
    ledvalue15: Optional[str] = None
    ledvalue16: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None
    output9: Optional[str] = None
    output10: Optional[str] = None
    output11: Optional[str] = None
    output12: Optional[str] = None
    output13: Optional[str] = None
    output14: Optional[str] = None
    output15: Optional[str] = None
    output16: Optional[str] = None
    button1: Optional[str] = None
    button2: Optional[str] = None
    button3: Optional[str] = None
    button4: Optional[str] = None
    button5: Optional[str] = None
    button6: Optional[str] = None
    button7: Optional[str] = None
    button8: Optional[str] = None
    button9: Optional[str] = None
    button10: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    button13: Optional[str] = None
    button14: Optional[str] = None
    button15: Optional[str] = None
    button16: Optional[str] = None


@dataclass
class Fadermatrix:
    """Circuit fadermatrix.
      Matrix of up to 4x4 virtual motor faders

    Inputs:
        firstfader: integer
            First M4 fader of the virtual fader matrix (starting with 1).

        rowcolumn: integer
            Currently selected row or column as follows:

             0Control output11, output12, output13 and output14
            1Control output21, output22, output23 and output24
            2Control output31, output32, output33 and output34
            3Control output41, output42, output43 and output44
            4Control output11, output21, output31 and output41
            5Control output12, output22, output32 and output42
            6Control output13, output23, output33 and output43
            7Control output14, output24, output34 and output44

            2mm

        notches1: integer
            Number of artifical notches in the respective column. For example
            notches2 controls the notches of output12, output22,
            output32 and output42.

             0disables the notches
            1creates a pitch bend wheel
            2creates a binary switch
            3creates a switch with four positions
            8creates eight notches
            25creates 25 notches


            Enabling notches also changes the output value. When you have two or
            more notches, the output values become discrete. For example with four notches
            the output will be 0, 1, 2 or 3.

            Note: The maximum number of notches is 201. But if you select
            more than 25 notches, the force feedback is turned off as the
            notches would get too small to work.

        notches2: integer
            Number of artifical notches in the respective column. For example
            notches2 controls the notches of output12, output22,
            output32 and output42.

             0disables the notches
            1creates a pitch bend wheel
            2creates a binary switch
            3creates a switch with four positions
            8creates eight notches
            25creates 25 notches


            Enabling notches also changes the output value. When you have two or
            more notches, the output values become discrete. For example with four notches
            the output will be 0, 1, 2 or 3.

            Note: The maximum number of notches is 201. But if you select
            more than 25 notches, the force feedback is turned off as the
            notches would get too small to work.

        notches3: integer
            Number of artifical notches in the respective column. For example
            notches2 controls the notches of output12, output22,
            output32 and output42.

             0disables the notches
            1creates a pitch bend wheel
            2creates a binary switch
            3creates a switch with four positions
            8creates eight notches
            25creates 25 notches


            Enabling notches also changes the output value. When you have two or
            more notches, the output values become discrete. For example with four notches
            the output will be 0, 1, 2 or 3.

            Note: The maximum number of notches is 201. But if you select
            more than 25 notches, the force feedback is turned off as the
            notches would get too small to work.

        notches4: integer
            Number of artifical notches in the respective column. For example
            notches2 controls the notches of output12, output22,
            output32 and output42.

             0disables the notches
            1creates a pitch bend wheel
            2creates a binary switch
            3creates a switch with four positions
            8creates eight notches
            25creates 25 notches


            Enabling notches also changes the output value. When you have two or
            more notches, the output values become discrete. For example with four notches
            the output will be 0, 1, 2 or 3.

            Note: The maximum number of notches is 201. But if you select
            more than 25 notches, the force feedback is turned off as the
            notches would get too small to work.

        startvalue1: cv
            These inputs allow to set a defined start value for each column. When
            the starts first and there is either no saved state or state saving
            is disabled via dontsave = 1, these start values are used. Also a trigger
            to clear loads the start avlues. There
            is one start value for each column. All rows share the same start value
            for a column.

        startvalue2: cv
            These inputs allow to set a defined start value for each column. When
            the starts first and there is either no saved state or state saving
            is disabled via dontsave = 1, these start values are used. Also a trigger
            to clear loads the start avlues. There
            is one start value for each column. All rows share the same start value
            for a column.

        startvalue3: cv
            These inputs allow to set a defined start value for each column. When
            the starts first and there is either no saved state or state saving
            is disabled via dontsave = 1, these start values are used. Also a trigger
            to clear loads the start avlues. There
            is one start value for each column. All rows share the same start value
            for a column.

        startvalue4: cv
            These inputs allow to set a defined start value for each column. When
            the starts first and there is either no saved state or state saving
            is disabled via dontsave = 1, these start values are used. Also a trigger
            to clear loads the start avlues. There
            is one start value for each column. All rows share the same start value
            for a column.

        ledvalue11: cv
            With these inputs you can address the LEDs below the virtual faders of output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs will only affect the LED if the according output
            is selected.

        ledvalue12: cv
            With these inputs you can address the LEDs below the virtual faders of output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs will only affect the LED if the according output
            is selected.

        ledvalue13: cv
            With these inputs you can address the LEDs below the virtual faders of output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs will only affect the LED if the according output
            is selected.

        ledvalue14: cv
            With these inputs you can address the LEDs below the virtual faders of output11 ... output14. As opposed to using direction (e.g. L1.1), these inputs will only affect the LED if the according output
            is selected.

        ledvalue21: cv
            With these inputs you can address the LEDs below the virtual faders of output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue22: cv
            With these inputs you can address the LEDs below the virtual faders of output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue23: cv
            With these inputs you can address the LEDs below the virtual faders of output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue24: cv
            With these inputs you can address the LEDs below the virtual faders of output21 ... output24. As opposed to using direction (e.g. L1.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue31: cv
            With these inputs you can address the LEDs below the virtual faders of output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue32: cv
            With these inputs you can address the LEDs below the virtual faders of output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue33: cv
            With these inputs you can address the LEDs below the virtual faders of output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue34: cv
            With these inputs you can address the LEDs below the virtual faders of output31 ... output34. As opposed to using direction (e.g. L3.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue41: cv
            With these inputs you can address the LEDs below the virtual faders of output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue42: cv
            With these inputs you can address the LEDs below the virtual faders of output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue43: cv
            With these inputs you can address the LEDs below the virtual faders of output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs will only affect the LED if the according output
            is selected.

        ledvalue44: cv
            With these inputs you can address the LEDs below the virtual faders of output41 ... output44. As opposed to using direction (e.g. L4.2), these inputs will only affect the LED if the according output
            is selected.

        ledcolor1: cv
            Sets the color of the LEDs below the faders if ledvalueXY is
            used. There are just four inputs since every column of outputs has
            the same LED color (in order to identify them). The color works as
            with the R registers for the LEDs on the master module.

        ledcolor2: cv
            Sets the color of the LEDs below the faders if ledvalueXY is
            used. There are just four inputs since every column of outputs has
            the same LED color (in order to identify them). The color works as
            with the R registers for the LEDs on the master module.

        ledcolor3: cv
            Sets the color of the LEDs below the faders if ledvalueXY is
            used. There are just four inputs since every column of outputs has
            the same LED color (in order to identify them). The color works as
            with the R registers for the LEDs on the master module.

        ledcolor4: cv
            Sets the color of the LEDs below the faders if ledvalueXY is
            used. There are just four inputs since every column of outputs has
            the same LED color (in order to identify them). The color works as
            with the R registers for the LEDs on the master module.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output11: cv
            Outputs for the CV values of the first row of parmeter.

        output12: cv
            Outputs for the CV values of the first row of parmeter.

        output13: cv
            Outputs for the CV values of the first row of parmeter.

        output14: cv
            Outputs for the CV values of the first row of parmeter.

        output21: cv
            Outputs for the CV values of the second row of parmeter.

        output22: cv
            Outputs for the CV values of the second row of parmeter.

        output23: cv
            Outputs for the CV values of the second row of parmeter.

        output24: cv
            Outputs for the CV values of the second row of parmeter.

        output31: cv
            Outputs for the CV values of the third row of parmeter.

        output32: cv
            Outputs for the CV values of the third row of parmeter.

        output33: cv
            Outputs for the CV values of the third row of parmeter.

        output34: cv
            Outputs for the CV values of the third row of parmeter.

        output41: cv
            Outputs for the CV values of the fourth row of parmeter.

        output42: cv
            Outputs for the CV values of the fourth row of parmeter.

        output43: cv
            Outputs for the CV values of the fourth row of parmeter.

        output44: cv
            Outputs for the CV values of the fourth row of parmeter.

        button11: gate
            Give access to the state of the touch button below the faders
            when the respective output in the first row is selected.

        button12: gate
            Give access to the state of the touch button below the faders
            when the respective output in the first row is selected.

        button13: gate
            Give access to the state of the touch button below the faders
            when the respective output in the first row is selected.

        button14: gate
            Give access to the state of the touch button below the faders
            when the respective output in the first row is selected.

        button21: gate
            Give access to the state of the touch button below the faders
            when the respective output in the second row is selected.

        button22: gate
            Give access to the state of the touch button below the faders
            when the respective output in the second row is selected.

        button23: gate
            Give access to the state of the touch button below the faders
            when the respective output in the second row is selected.

        button24: gate
            Give access to the state of the touch button below the faders
            when the respective output in the second row is selected.

        button31: gate
            Give access to the state of the touch button below the faders
            when the respective output in the third row is selected.

        button32: gate
            Give access to the state of the touch button below the faders
            when the respective output in the third row is selected.

        button33: gate
            Give access to the state of the touch button below the faders
            when the respective output in the third row is selected.

        button34: gate
            Give access to the state of the touch button below the faders
            when the respective output in the third row is selected.

        button41: gate
            Give access to the state of the touch button below the faders
            when the respective output in the fourth row is selected.

        button42: gate
            Give access to the state of the touch button below the faders
            when the respective output in the fourth row is selected.

        button43: gate
            Give access to the state of the touch button below the faders
            when the respective output in the fourth row is selected.

        button44: gate
            Give access to the state of the touch button below the faders
            when the respective output in the fourth row is selected.

    """


    firstfader: Optional[str] = None
    rowcolumn: Optional[str] = None
    notches1: Optional[str] = None
    notches2: Optional[str] = None
    notches3: Optional[str] = None
    notches4: Optional[str] = None
    startvalue1: Optional[str] = None
    startvalue2: Optional[str] = None
    startvalue3: Optional[str] = None
    startvalue4: Optional[str] = None
    ledvalue11: Optional[str] = None
    ledvalue12: Optional[str] = None
    ledvalue13: Optional[str] = None
    ledvalue14: Optional[str] = None
    ledvalue21: Optional[str] = None
    ledvalue22: Optional[str] = None
    ledvalue23: Optional[str] = None
    ledvalue24: Optional[str] = None
    ledvalue31: Optional[str] = None
    ledvalue32: Optional[str] = None
    ledvalue33: Optional[str] = None
    ledvalue34: Optional[str] = None
    ledvalue41: Optional[str] = None
    ledvalue42: Optional[str] = None
    ledvalue43: Optional[str] = None
    ledvalue44: Optional[str] = None
    ledcolor1: Optional[str] = None
    ledcolor2: Optional[str] = None
    ledcolor3: Optional[str] = None
    ledcolor4: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output11: Optional[str] = None
    output12: Optional[str] = None
    output13: Optional[str] = None
    output14: Optional[str] = None
    output21: Optional[str] = None
    output22: Optional[str] = None
    output23: Optional[str] = None
    output24: Optional[str] = None
    output31: Optional[str] = None
    output32: Optional[str] = None
    output33: Optional[str] = None
    output34: Optional[str] = None
    output41: Optional[str] = None
    output42: Optional[str] = None
    output43: Optional[str] = None
    output44: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    button13: Optional[str] = None
    button14: Optional[str] = None
    button21: Optional[str] = None
    button22: Optional[str] = None
    button23: Optional[str] = None
    button24: Optional[str] = None
    button31: Optional[str] = None
    button32: Optional[str] = None
    button33: Optional[str] = None
    button34: Optional[str] = None
    button41: Optional[str] = None
    button42: Optional[str] = None
    button43: Optional[str] = None
    button44: Optional[str] = None


@dataclass
class Firefacecontrol:
    """Circuit firefacecontrol.
      Control a RME Fireface interface (experimental)

    Inputs:
        trs: integer

        outputlevel1: fraction

        outputlevel2: fraction

        outputlevel3: fraction

        outputlevel4: fraction

        outputlevel5: fraction

        outputlevel6: fraction

        outputlevel7: fraction

        outputlevel8: fraction

        outputlevel9: fraction

        outputlevel10: fraction

        outputlevel11: fraction

        outputlevel12: fraction

        outputlevel13: fraction

        outputlevel14: fraction

        outputlevel15: fraction

        outputlevel16: fraction

        mainoutput: integer

        phonesoutput1: integer

        phonesoutput2: integer

        outputmix1in1: fraction

        outputmix1in2: fraction

        outputmix1in3: fraction

        outputmix1in4: fraction

        outputmix1in5: fraction

        outputmix1in6: fraction

        outputmix1in7: fraction

        outputmix1in8: fraction

        outputmix1in9: fraction

        outputmix1in10: fraction

        outputmix1in11: fraction

        outputmix1in12: fraction

        outputmix1in13: fraction

        outputmix1in14: fraction

        outputmix1in15: fraction

        outputmix1in16: fraction

        outputmix2in1: fraction

        outputmix2in2: fraction

        outputmix2in3: fraction

        outputmix2in4: fraction

        outputmix2in5: fraction

        outputmix2in6: fraction

        outputmix2in7: fraction

        outputmix2in8: fraction

        outputmix2in9: fraction

        outputmix2in10: fraction

        outputmix2in11: fraction

        outputmix2in12: fraction

        outputmix2in13: fraction

        outputmix2in14: fraction

        outputmix2in15: fraction

        outputmix2in16: fraction

        outputmix3in1: fraction

        outputmix3in2: fraction

        outputmix3in3: fraction

        outputmix3in4: fraction

        outputmix3in5: fraction

        outputmix3in6: fraction

        outputmix3in7: fraction

        outputmix3in8: fraction

        outputmix3in9: fraction

        outputmix3in10: fraction

        outputmix3in11: fraction

        outputmix3in12: fraction

        outputmix3in13: fraction

        outputmix3in14: fraction

        outputmix3in15: fraction

        outputmix3in16: fraction

        outputmix4in1: fraction

        outputmix4in2: fraction

        outputmix4in3: fraction

        outputmix4in4: fraction

        outputmix4in5: fraction

        outputmix4in6: fraction

        outputmix4in7: fraction

        outputmix4in8: fraction

        outputmix4in9: fraction

        outputmix4in10: fraction

        outputmix4in11: fraction

        outputmix4in12: fraction

        outputmix4in13: fraction

        outputmix4in14: fraction

        outputmix4in15: fraction

        outputmix4in16: fraction

        outputmix5in1: fraction

        outputmix5in2: fraction

        outputmix5in3: fraction

        outputmix5in4: fraction

        outputmix5in5: fraction

        outputmix5in6: fraction

        outputmix5in7: fraction

        outputmix5in8: fraction

        outputmix5in9: fraction

        outputmix5in10: fraction

        outputmix5in11: fraction

        outputmix5in12: fraction

        outputmix5in13: fraction

        outputmix5in14: fraction

        outputmix5in15: fraction

        outputmix5in16: fraction

        outputmix6in1: fraction

        outputmix6in2: fraction

        outputmix6in3: fraction

        outputmix6in4: fraction

        outputmix6in5: fraction

        outputmix6in6: fraction

        outputmix6in7: fraction

        outputmix6in8: fraction

        outputmix6in9: fraction

        outputmix6in10: fraction

        outputmix6in11: fraction

        outputmix6in12: fraction

        outputmix6in13: fraction

        outputmix6in14: fraction

        outputmix6in15: fraction

        outputmix6in16: fraction

        outputmix7in1: fraction

        outputmix7in2: fraction

        outputmix7in3: fraction

        outputmix7in4: fraction

        outputmix7in5: fraction

        outputmix7in6: fraction

        outputmix7in7: fraction

        outputmix7in8: fraction

        outputmix7in9: fraction

        outputmix7in10: fraction

        outputmix7in11: fraction

        outputmix7in12: fraction

        outputmix7in13: fraction

        outputmix7in14: fraction

        outputmix7in15: fraction

        outputmix7in16: fraction

        outputmix8in1: fraction

        outputmix8in2: fraction

        outputmix8in3: fraction

        outputmix8in4: fraction

        outputmix8in5: fraction

        outputmix8in6: fraction

        outputmix8in7: fraction

        outputmix8in8: fraction

        outputmix8in9: fraction

        outputmix8in10: fraction

        outputmix8in11: fraction

        outputmix8in12: fraction

        outputmix8in13: fraction

        outputmix8in14: fraction

        outputmix8in15: fraction

        outputmix8in16: fraction

        outputmix9in1: fraction

        outputmix9in2: fraction

        outputmix9in3: fraction

        outputmix9in4: fraction

        outputmix9in5: fraction

        outputmix9in6: fraction

        outputmix9in7: fraction

        outputmix9in8: fraction

        outputmix9in9: fraction

        outputmix9in10: fraction

        outputmix9in11: fraction

        outputmix9in12: fraction

        outputmix9in13: fraction

        outputmix9in14: fraction

        outputmix9in15: fraction

        outputmix9in16: fraction

        outputmix10in1: fraction

        outputmix10in2: fraction

        outputmix10in3: fraction

        outputmix10in4: fraction

        outputmix10in5: fraction

        outputmix10in6: fraction

        outputmix10in7: fraction

        outputmix10in8: fraction

        outputmix10in9: fraction

        outputmix10in10: fraction

        outputmix10in11: fraction

        outputmix10in12: fraction

        outputmix10in13: fraction

        outputmix10in14: fraction

        outputmix10in15: fraction

        outputmix10in16: fraction

        outputmix11in1: fraction

        outputmix11in2: fraction

        outputmix11in3: fraction

        outputmix11in4: fraction

        outputmix11in5: fraction

        outputmix11in6: fraction

        outputmix11in7: fraction

        outputmix11in8: fraction

        outputmix11in9: fraction

        outputmix11in10: fraction

        outputmix11in11: fraction

        outputmix11in12: fraction

        outputmix11in13: fraction

        outputmix11in14: fraction

        outputmix11in15: fraction

        outputmix11in16: fraction

        outputmix12in1: fraction

        outputmix12in2: fraction

        outputmix12in3: fraction

        outputmix12in4: fraction

        outputmix12in5: fraction

        outputmix12in6: fraction

        outputmix12in7: fraction

        outputmix12in8: fraction

        outputmix12in9: fraction

        outputmix12in10: fraction

        outputmix12in11: fraction

        outputmix12in12: fraction

        outputmix12in13: fraction

        outputmix12in14: fraction

        outputmix12in15: fraction

        outputmix12in16: fraction

        outputmix13in1: fraction

        outputmix13in2: fraction

        outputmix13in3: fraction

        outputmix13in4: fraction

        outputmix13in5: fraction

        outputmix13in6: fraction

        outputmix13in7: fraction

        outputmix13in8: fraction

        outputmix13in9: fraction

        outputmix13in10: fraction

        outputmix13in11: fraction

        outputmix13in12: fraction

        outputmix13in13: fraction

        outputmix13in14: fraction

        outputmix13in15: fraction

        outputmix13in16: fraction

        outputmix14in1: fraction

        outputmix14in2: fraction

        outputmix14in3: fraction

        outputmix14in4: fraction

        outputmix14in5: fraction

        outputmix14in6: fraction

        outputmix14in7: fraction

        outputmix14in8: fraction

        outputmix14in9: fraction

        outputmix14in10: fraction

        outputmix14in11: fraction

        outputmix14in12: fraction

        outputmix14in13: fraction

        outputmix14in14: fraction

        outputmix14in15: fraction

        outputmix14in16: fraction

        outputmix15in1: fraction

        outputmix15in2: fraction

        outputmix15in3: fraction

        outputmix15in4: fraction

        outputmix15in5: fraction

        outputmix15in6: fraction

        outputmix15in7: fraction

        outputmix15in8: fraction

        outputmix15in9: fraction

        outputmix15in10: fraction

        outputmix15in11: fraction

        outputmix15in12: fraction

        outputmix15in13: fraction

        outputmix15in14: fraction

        outputmix15in15: fraction

        outputmix15in16: fraction

        outputmix16in1: fraction

        outputmix16in2: fraction

        outputmix16in3: fraction

        outputmix16in4: fraction

        outputmix16in5: fraction

        outputmix16in6: fraction

        outputmix16in7: fraction

        outputmix16in8: fraction

        outputmix16in9: fraction

        outputmix16in10: fraction

        outputmix16in11: fraction

        outputmix16in12: fraction

        outputmix16in13: fraction

        outputmix16in14: fraction

        outputmix16in15: fraction

        outputmix16in16: fraction

        postfader1: gate

        postfader2: gate

        postfader3: gate

        postfader4: gate

        postfader5: gate

        postfader6: gate

        postfader7: gate

        postfader8: gate

        postfader9: gate

        postfader10: gate

        postfader11: gate

        postfader12: gate

        postfader13: gate

        postfader14: gate

        postfader15: gate

        postfader16: gate

        pan1: fraction

        pan2: fraction

        pan3: fraction

        pan4: fraction

        pan5: fraction

        pan6: fraction

        pan7: fraction

        pan8: fraction

        pan9: fraction

        pan10: fraction

        pan11: fraction

        pan12: fraction

        pan13: fraction

        pan14: fraction

        pan15: fraction

        pan16: fraction

        unmute1: fraction

        unmute2: fraction

        unmute3: fraction

        unmute4: fraction

        unmute5: fraction

        unmute6: fraction

        unmute7: fraction

        unmute8: fraction

        unmute9: fraction

        unmute10: fraction

        unmute11: fraction

        unmute12: fraction

        unmute13: fraction

        unmute14: fraction

        unmute15: fraction

        unmute16: fraction

        update: trigger

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:

    """


    trs: Optional[str] = None
    outputlevel1: Optional[str] = None
    outputlevel2: Optional[str] = None
    outputlevel3: Optional[str] = None
    outputlevel4: Optional[str] = None
    outputlevel5: Optional[str] = None
    outputlevel6: Optional[str] = None
    outputlevel7: Optional[str] = None
    outputlevel8: Optional[str] = None
    outputlevel9: Optional[str] = None
    outputlevel10: Optional[str] = None
    outputlevel11: Optional[str] = None
    outputlevel12: Optional[str] = None
    outputlevel13: Optional[str] = None
    outputlevel14: Optional[str] = None
    outputlevel15: Optional[str] = None
    outputlevel16: Optional[str] = None
    mainoutput: Optional[str] = None
    phonesoutput1: Optional[str] = None
    phonesoutput2: Optional[str] = None
    outputmix1in1: Optional[str] = None
    outputmix1in2: Optional[str] = None
    outputmix1in3: Optional[str] = None
    outputmix1in4: Optional[str] = None
    outputmix1in5: Optional[str] = None
    outputmix1in6: Optional[str] = None
    outputmix1in7: Optional[str] = None
    outputmix1in8: Optional[str] = None
    outputmix1in9: Optional[str] = None
    outputmix1in10: Optional[str] = None
    outputmix1in11: Optional[str] = None
    outputmix1in12: Optional[str] = None
    outputmix1in13: Optional[str] = None
    outputmix1in14: Optional[str] = None
    outputmix1in15: Optional[str] = None
    outputmix1in16: Optional[str] = None
    outputmix2in1: Optional[str] = None
    outputmix2in2: Optional[str] = None
    outputmix2in3: Optional[str] = None
    outputmix2in4: Optional[str] = None
    outputmix2in5: Optional[str] = None
    outputmix2in6: Optional[str] = None
    outputmix2in7: Optional[str] = None
    outputmix2in8: Optional[str] = None
    outputmix2in9: Optional[str] = None
    outputmix2in10: Optional[str] = None
    outputmix2in11: Optional[str] = None
    outputmix2in12: Optional[str] = None
    outputmix2in13: Optional[str] = None
    outputmix2in14: Optional[str] = None
    outputmix2in15: Optional[str] = None
    outputmix2in16: Optional[str] = None
    outputmix3in1: Optional[str] = None
    outputmix3in2: Optional[str] = None
    outputmix3in3: Optional[str] = None
    outputmix3in4: Optional[str] = None
    outputmix3in5: Optional[str] = None
    outputmix3in6: Optional[str] = None
    outputmix3in7: Optional[str] = None
    outputmix3in8: Optional[str] = None
    outputmix3in9: Optional[str] = None
    outputmix3in10: Optional[str] = None
    outputmix3in11: Optional[str] = None
    outputmix3in12: Optional[str] = None
    outputmix3in13: Optional[str] = None
    outputmix3in14: Optional[str] = None
    outputmix3in15: Optional[str] = None
    outputmix3in16: Optional[str] = None
    outputmix4in1: Optional[str] = None
    outputmix4in2: Optional[str] = None
    outputmix4in3: Optional[str] = None
    outputmix4in4: Optional[str] = None
    outputmix4in5: Optional[str] = None
    outputmix4in6: Optional[str] = None
    outputmix4in7: Optional[str] = None
    outputmix4in8: Optional[str] = None
    outputmix4in9: Optional[str] = None
    outputmix4in10: Optional[str] = None
    outputmix4in11: Optional[str] = None
    outputmix4in12: Optional[str] = None
    outputmix4in13: Optional[str] = None
    outputmix4in14: Optional[str] = None
    outputmix4in15: Optional[str] = None
    outputmix4in16: Optional[str] = None
    outputmix5in1: Optional[str] = None
    outputmix5in2: Optional[str] = None
    outputmix5in3: Optional[str] = None
    outputmix5in4: Optional[str] = None
    outputmix5in5: Optional[str] = None
    outputmix5in6: Optional[str] = None
    outputmix5in7: Optional[str] = None
    outputmix5in8: Optional[str] = None
    outputmix5in9: Optional[str] = None
    outputmix5in10: Optional[str] = None
    outputmix5in11: Optional[str] = None
    outputmix5in12: Optional[str] = None
    outputmix5in13: Optional[str] = None
    outputmix5in14: Optional[str] = None
    outputmix5in15: Optional[str] = None
    outputmix5in16: Optional[str] = None
    outputmix6in1: Optional[str] = None
    outputmix6in2: Optional[str] = None
    outputmix6in3: Optional[str] = None
    outputmix6in4: Optional[str] = None
    outputmix6in5: Optional[str] = None
    outputmix6in6: Optional[str] = None
    outputmix6in7: Optional[str] = None
    outputmix6in8: Optional[str] = None
    outputmix6in9: Optional[str] = None
    outputmix6in10: Optional[str] = None
    outputmix6in11: Optional[str] = None
    outputmix6in12: Optional[str] = None
    outputmix6in13: Optional[str] = None
    outputmix6in14: Optional[str] = None
    outputmix6in15: Optional[str] = None
    outputmix6in16: Optional[str] = None
    outputmix7in1: Optional[str] = None
    outputmix7in2: Optional[str] = None
    outputmix7in3: Optional[str] = None
    outputmix7in4: Optional[str] = None
    outputmix7in5: Optional[str] = None
    outputmix7in6: Optional[str] = None
    outputmix7in7: Optional[str] = None
    outputmix7in8: Optional[str] = None
    outputmix7in9: Optional[str] = None
    outputmix7in10: Optional[str] = None
    outputmix7in11: Optional[str] = None
    outputmix7in12: Optional[str] = None
    outputmix7in13: Optional[str] = None
    outputmix7in14: Optional[str] = None
    outputmix7in15: Optional[str] = None
    outputmix7in16: Optional[str] = None
    outputmix8in1: Optional[str] = None
    outputmix8in2: Optional[str] = None
    outputmix8in3: Optional[str] = None
    outputmix8in4: Optional[str] = None
    outputmix8in5: Optional[str] = None
    outputmix8in6: Optional[str] = None
    outputmix8in7: Optional[str] = None
    outputmix8in8: Optional[str] = None
    outputmix8in9: Optional[str] = None
    outputmix8in10: Optional[str] = None
    outputmix8in11: Optional[str] = None
    outputmix8in12: Optional[str] = None
    outputmix8in13: Optional[str] = None
    outputmix8in14: Optional[str] = None
    outputmix8in15: Optional[str] = None
    outputmix8in16: Optional[str] = None
    outputmix9in1: Optional[str] = None
    outputmix9in2: Optional[str] = None
    outputmix9in3: Optional[str] = None
    outputmix9in4: Optional[str] = None
    outputmix9in5: Optional[str] = None
    outputmix9in6: Optional[str] = None
    outputmix9in7: Optional[str] = None
    outputmix9in8: Optional[str] = None
    outputmix9in9: Optional[str] = None
    outputmix9in10: Optional[str] = None
    outputmix9in11: Optional[str] = None
    outputmix9in12: Optional[str] = None
    outputmix9in13: Optional[str] = None
    outputmix9in14: Optional[str] = None
    outputmix9in15: Optional[str] = None
    outputmix9in16: Optional[str] = None
    outputmix10in1: Optional[str] = None
    outputmix10in2: Optional[str] = None
    outputmix10in3: Optional[str] = None
    outputmix10in4: Optional[str] = None
    outputmix10in5: Optional[str] = None
    outputmix10in6: Optional[str] = None
    outputmix10in7: Optional[str] = None
    outputmix10in8: Optional[str] = None
    outputmix10in9: Optional[str] = None
    outputmix10in10: Optional[str] = None
    outputmix10in11: Optional[str] = None
    outputmix10in12: Optional[str] = None
    outputmix10in13: Optional[str] = None
    outputmix10in14: Optional[str] = None
    outputmix10in15: Optional[str] = None
    outputmix10in16: Optional[str] = None
    outputmix11in1: Optional[str] = None
    outputmix11in2: Optional[str] = None
    outputmix11in3: Optional[str] = None
    outputmix11in4: Optional[str] = None
    outputmix11in5: Optional[str] = None
    outputmix11in6: Optional[str] = None
    outputmix11in7: Optional[str] = None
    outputmix11in8: Optional[str] = None
    outputmix11in9: Optional[str] = None
    outputmix11in10: Optional[str] = None
    outputmix11in11: Optional[str] = None
    outputmix11in12: Optional[str] = None
    outputmix11in13: Optional[str] = None
    outputmix11in14: Optional[str] = None
    outputmix11in15: Optional[str] = None
    outputmix11in16: Optional[str] = None
    outputmix12in1: Optional[str] = None
    outputmix12in2: Optional[str] = None
    outputmix12in3: Optional[str] = None
    outputmix12in4: Optional[str] = None
    outputmix12in5: Optional[str] = None
    outputmix12in6: Optional[str] = None
    outputmix12in7: Optional[str] = None
    outputmix12in8: Optional[str] = None
    outputmix12in9: Optional[str] = None
    outputmix12in10: Optional[str] = None
    outputmix12in11: Optional[str] = None
    outputmix12in12: Optional[str] = None
    outputmix12in13: Optional[str] = None
    outputmix12in14: Optional[str] = None
    outputmix12in15: Optional[str] = None
    outputmix12in16: Optional[str] = None
    outputmix13in1: Optional[str] = None
    outputmix13in2: Optional[str] = None
    outputmix13in3: Optional[str] = None
    outputmix13in4: Optional[str] = None
    outputmix13in5: Optional[str] = None
    outputmix13in6: Optional[str] = None
    outputmix13in7: Optional[str] = None
    outputmix13in8: Optional[str] = None
    outputmix13in9: Optional[str] = None
    outputmix13in10: Optional[str] = None
    outputmix13in11: Optional[str] = None
    outputmix13in12: Optional[str] = None
    outputmix13in13: Optional[str] = None
    outputmix13in14: Optional[str] = None
    outputmix13in15: Optional[str] = None
    outputmix13in16: Optional[str] = None
    outputmix14in1: Optional[str] = None
    outputmix14in2: Optional[str] = None
    outputmix14in3: Optional[str] = None
    outputmix14in4: Optional[str] = None
    outputmix14in5: Optional[str] = None
    outputmix14in6: Optional[str] = None
    outputmix14in7: Optional[str] = None
    outputmix14in8: Optional[str] = None
    outputmix14in9: Optional[str] = None
    outputmix14in10: Optional[str] = None
    outputmix14in11: Optional[str] = None
    outputmix14in12: Optional[str] = None
    outputmix14in13: Optional[str] = None
    outputmix14in14: Optional[str] = None
    outputmix14in15: Optional[str] = None
    outputmix14in16: Optional[str] = None
    outputmix15in1: Optional[str] = None
    outputmix15in2: Optional[str] = None
    outputmix15in3: Optional[str] = None
    outputmix15in4: Optional[str] = None
    outputmix15in5: Optional[str] = None
    outputmix15in6: Optional[str] = None
    outputmix15in7: Optional[str] = None
    outputmix15in8: Optional[str] = None
    outputmix15in9: Optional[str] = None
    outputmix15in10: Optional[str] = None
    outputmix15in11: Optional[str] = None
    outputmix15in12: Optional[str] = None
    outputmix15in13: Optional[str] = None
    outputmix15in14: Optional[str] = None
    outputmix15in15: Optional[str] = None
    outputmix15in16: Optional[str] = None
    outputmix16in1: Optional[str] = None
    outputmix16in2: Optional[str] = None
    outputmix16in3: Optional[str] = None
    outputmix16in4: Optional[str] = None
    outputmix16in5: Optional[str] = None
    outputmix16in6: Optional[str] = None
    outputmix16in7: Optional[str] = None
    outputmix16in8: Optional[str] = None
    outputmix16in9: Optional[str] = None
    outputmix16in10: Optional[str] = None
    outputmix16in11: Optional[str] = None
    outputmix16in12: Optional[str] = None
    outputmix16in13: Optional[str] = None
    outputmix16in14: Optional[str] = None
    outputmix16in15: Optional[str] = None
    outputmix16in16: Optional[str] = None
    postfader1: Optional[str] = None
    postfader2: Optional[str] = None
    postfader3: Optional[str] = None
    postfader4: Optional[str] = None
    postfader5: Optional[str] = None
    postfader6: Optional[str] = None
    postfader7: Optional[str] = None
    postfader8: Optional[str] = None
    postfader9: Optional[str] = None
    postfader10: Optional[str] = None
    postfader11: Optional[str] = None
    postfader12: Optional[str] = None
    postfader13: Optional[str] = None
    postfader14: Optional[str] = None
    postfader15: Optional[str] = None
    postfader16: Optional[str] = None
    pan1: Optional[str] = None
    pan2: Optional[str] = None
    pan3: Optional[str] = None
    pan4: Optional[str] = None
    pan5: Optional[str] = None
    pan6: Optional[str] = None
    pan7: Optional[str] = None
    pan8: Optional[str] = None
    pan9: Optional[str] = None
    pan10: Optional[str] = None
    pan11: Optional[str] = None
    pan12: Optional[str] = None
    pan13: Optional[str] = None
    pan14: Optional[str] = None
    pan15: Optional[str] = None
    pan16: Optional[str] = None
    unmute1: Optional[str] = None
    unmute2: Optional[str] = None
    unmute3: Optional[str] = None
    unmute4: Optional[str] = None
    unmute5: Optional[str] = None
    unmute6: Optional[str] = None
    unmute7: Optional[str] = None
    unmute8: Optional[str] = None
    unmute9: Optional[str] = None
    unmute10: Optional[str] = None
    unmute11: Optional[str] = None
    unmute12: Optional[str] = None
    unmute13: Optional[str] = None
    unmute14: Optional[str] = None
    unmute15: Optional[str] = None
    unmute16: Optional[str] = None
    update: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None


@dataclass
class Flipflop:
    """Circuit flipflop.
      Simple flip flop

    Inputs:
        toggle: trigger
            A trigger here inverts the state of the flip flop. It changes
            0 to 1 and 1 to 0.

        set: trigger
            Sets the flip flop to 1.

        reset: trigger
            Sets the flip flop to 0.

        clear: trigger
            Sets the flip flop to the value defined by startvalue.

        startvalue: gate
            The flip flop starts its live with this value. Also clear
            will set the flip flop to this value.

        load: trigger
            Loads the value into the flip flop that's defined with loadvalue.

        loadvalue: gate
            Value to set the flip flop to, when load is triggered.


    Outputs:
        output: gate
            Outputs the current value of the flip flop: either 0 or 1.

    """


    toggle: Optional[str] = None
    set: Optional[str] = None
    reset: Optional[str] = None
    clear: Optional[str] = None
    startvalue: Optional[str] = None
    load: Optional[str] = None
    loadvalue: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Fold:
    """Circuit fold.
      CV folder – keep (pitch) CV within certain bounds

    Inputs:
        input: cv
            Input CV to be folded.

        foldby: cv
            Amount to be added or substracted from the input CV if
            it is not within the allowed range. This CV must be positive.
            If it is negative or zero, no folding will be done.

        minimum: cv
            Lower bound of the allowed range. If unpatched, no lower
            bound will be applied.

        maximum: cv
            Upper bound of the allowed range. If unpatched, no upper
            bound will be applied.


    Outputs:
        output: cv
            Folded output voltage

    """


    input: Optional[str] = None
    foldby: Optional[str] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Fourstatebutton:
    """Circuit fourstatebutton.
      Button switching through 4 states (OBSOLETE)

    Inputs:
        button: trigger
            The button.

        reset: trigger
            A positive trigger here will reset the button to the first state.

        value1: cv
            The values that output should get when the four
            various states are active.

        value2: cv
            The values that output should get when the four
            various states are active.

        value3: cv
            The values that output should get when the four
            various states are active.

        value4: cv
            The values that output should get when the four
            various states are active.

        startvalue: integer
            By setting this to 0, 1, 2 or 3 you
            set the initial state of the button when the is powered up to
            state 1, 2, 3 or 4. It also disabled the automatic saving of the button's
            state in the 's internal flash memory.


    Outputs:
        output: cv
            Depending on the current state of the button here the
            value of input1, input2, input3 or input4
            will be copied.

        led: fraction
            The LED in the button

    """


    button: Optional[str] = None
    reset: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    value3: Optional[str] = None
    value4: Optional[str] = None
    startvalue: Optional[str] = None
    output: Optional[str] = None
    led: Optional[str] = None


@dataclass
class Gatetool:
    """Circuit gatetool.
      Operate on triggers and gates, modify gatelength

    Inputs:
        inputgate: gate
            Input gate. Use this if the length of the input gate is relevant.

        inputtrigger: trigger
            Input trigger. Use this if the length of the input gate should be
            ignored.

        inputedge: gate
            Input edge: Use this if every low/high or high/low transition should
            count as a trigger.

        gatelength: cv
            Sets the length of the gate of outputgate in seconds. If you
            use taptempo the length is in fractions of a clock tick, instead.

        gatestretch: cv
            Makes the output gate longer than the input gate by the given percentage.
            This parameter is ignored if gatelength is used.

        mingatelength: cv
            Defines a minimum length of the output gate in seconds or
            clock ticks.

        maxgatelength: cv
            Defines a maximum length of the output gate in seconds or
            clock ticks.

        taptempo: trigger
            If you patch a reference clock here, gatelength, mingatelength
            and maxgatelength are fractions of one clock tick, not seconds
            anymore.
            Please see page 23 for details on using
            taptempo inputs.


    Outputs:
        outputgate: gate
            Outputs a gate with controllable length for every gate, trigger or
            edge event.

        outputtrigger: trigger
            Outputs a 10 ms trigger for every gate, trigger or edge event.

        outputedge: gate
            Toggle between 0 and 1 at every gate, trigger or edge event.

    """


    inputgate: Optional[str] = None
    inputtrigger: Optional[str] = None
    inputedge: Optional[str] = None
    gatelength: Optional[str] = None
    gatestretch: Optional[str] = None
    mingatelength: Optional[str] = None
    maxgatelength: Optional[str] = None
    taptempo: Optional[str] = None
    outputgate: Optional[str] = None
    outputtrigger: Optional[str] = None
    outputedge: Optional[str] = None


@dataclass
class Lfo:
    """Circuit lfo.
      Low frequency oscillator (LFO)

    Inputs:
        rate: cv
            Frequency control: The default frequency of the LFO is 1 Hz
            (one cycle per second). Each volt doubles
            the frequency. So an input of 1 V (a number of 0.1) speeds up
            the LFO to 2 Hz, 2 V (0.2) create 4 Hz and
            so on. On the other hand negative voltages reduce the speed, so
            -1 V (-0.1) will give 0.5 Hz and so on.

        taptempo: trigger
            Feed a reference clock here and the LFO will run at the speed of
            that clock – albeit optionally modified by rate and hz.
            Please see page 23 for details on using
            taptempo inputs.

        hz: cv
            Set the frequency in Hz directly by setting a number here. Note:
            you cannot use hz at that same time as taptempo. But
            both can be combined with rate.

        level: cv
            The maximum positive output level of the LFO. The default of 1.0
            means a swing between 0 V and 10 V – unless you enable bipolar,
            in which case it moves from -10 V to 10 V.

        randomize: fraction
            Randomization is an experimental new feature that combines random
            voltages with an LFO. If you turn this parameter up, then for each
            hill of the LFO's waveform output a new random attenuation is being chosen
            and multiplied with the current level. The result is an output,
            where each cycle of the waveform has a different level.

        offset: cv
            The output of the LFO is shifted by that voltage right before
            the output. This is the same as adding or mixing a
            fixed voltage to the output. Not very fancy, but practical if
            you want to output a modulation voltage within a certain range.

        bipolar: gate
            If this switch is set to on, then the LFO will output a full
            swing from -level to +level. When set to off it will swing
            between 0V and +level.

        phase: fraction
            Shift the LFOs phase by this value. A value of 0.0 leaves the LFO
            run in its normal phase. 0.5 will shift bei 180^∘.
            And 1.0 will shift by a complete phase of 360^∘, which
            is the same as 0.0.

        pulsewidth: bipolar
            This sets the pulse width of the square LFO and only affects the
            output square. It ranges from 0.0 to 1.0. Please note that
            a pulse width of exactly 0.0 or 1.0 will make the output stick
            to the respective lower or upper level.

        skew: bipolar
            Modifies the symmetry of the triangle output by shifting the
            “peak” of the triangle left and right. The default of 0.5
            creates a symmetric waveform. Smaller values speed up the rising
            part of the triangle and create more and more a ramp like waveform
            until a skew of 0.0 creates an exact ramp – just the same as
            the ramp output. A skew of 1.0 create a sawtooth waveform.

        sync: trigger
            A positive trigger edge at this input will reset the LFO. It will
            force to restart the waveform at its “beginning”. By using the
            input syncphase you can change that behaviour.

        syncphase: fraction
            This input changes the behaviour of the sync input. I changes
            the phase the waveform restarts at when it receives a sync trigger.
            E.g. by setting this to 0.5 a sync trigger will restart the waveform
            right at its middle. This is an interesting feature that cannot be
            found in analog LFOs since it would be very hard to build in actual
            circuits.

        waveform: cv
            If you use output – rather than the individual waveform outputs like
            square, saw and so on – this input selects the Wave form. An integer
            number from 0 to 6 selects one of the seven available waveforms. Any number
            in between selects a mixture of the two neighboring waveforms. That way you can smoothly
            morph through all the available waveforms. The codes for the waveforms are:

             0square
            1sawtooth
            2triangle
            3ramp
            4paraboloid
            5sine
            6cosine



    Outputs:
        output: cv
            Main output of the LFO.

        square: cv
            A square waveform – modified by pulsewidth.

        sawtooth: cv
            Outputs a sawtooth waveform – i.e. a rising ramp

        triangle: cv
            Outputs a triangle waveform – modified by skew.

        ramp: cv
            Outputs a falling ramp – like a sawtooth that is mirrored. Note:
            if the LFO is set to bipolar then this is the negation of sawtooth.
            If it is set to unipolar then this is not the case. The waveform
            will be positive then!

        paraboloid: cv
            An experimental waveform that looks very similar to a sine
            wave but is derived from a triangle by computing the square
            of each waypoint's distance to level.

        sine: cv
            A sine waveform.

        cosine: cv
            A sine waveform shifted by 90^∘. This output is for your
            convenience and avoids needing two LFO circuits in cases where you
            want to make quadrature applications. Please note that 180^∘
            and 270^∘ can easily be achieved by negating the outputs sine
            and cosine at a later stage.

    """


    rate: Optional[str] = None
    taptempo: Optional[str] = None
    hz: Optional[str] = None
    level: Optional[str] = None
    randomize: Optional[str] = None
    offset: Optional[str] = None
    bipolar: Optional[str] = None
    phase: Optional[str] = None
    pulsewidth: Optional[str] = None
    skew: Optional[str] = None
    sync: Optional[str] = None
    syncphase: Optional[str] = None
    waveform: Optional[str] = None
    output: Optional[str] = None
    square: Optional[str] = None
    sawtooth: Optional[str] = None
    triangle: Optional[str] = None
    ramp: Optional[str] = None
    paraboloid: Optional[str] = None
    sine: Optional[str] = None
    cosine: Optional[str] = None


@dataclass
class Logic:
    """Circuit logic.
      Logic operations utility

    Inputs:
        input1: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input2: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input3: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input4: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input5: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input6: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input7: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        input8: gate
            1 ... 8 input. Note: this input is declared as a gate input, but
            in fact you can use it as a CV input in combination with various or random values set
            for the threshold.

        threshold: cv
            Input values at, or above this threshold value, are considered high or on.
            The default is 0.1 which corresponds to an input voltage of 1 V. You can get
            interesting results when both the inputs are variable CVs (like from LFOs) and this
            threshold is being modulated as well.

        lowvalue: cv
            Output value that is output for logic low, false or off.

        highvalue: cv
            Output value that is output for a logic high, true or on.

        countvalue: cv
            Value added to the count output for each input with a high level


    Outputs:
        and_: cv
            A logic AND operation on all patched inputs:
            This output is set to highvalue if all inputs are high (i.e. at least
            threshold), else lowvalue

        or_: cv
            A logic OR operation on all patched inputs:
            This output is set to highvalue if at least one of the inputs is high

        xor: cv
            Exclusive OR: This is high, if the number of high inputs is odd! This means
            that any change in one of the inputs will also change the output.

        nand: cv
            Like AND but the outcome is negated.

        nor: cv
            Like OR but the outcome is negated.

        negated: cv
            Logical negate of input1 (which can abbreviated as input). Note:
            The inputs input2 ... input7 are ignored here. Another note:
            If you use input1 anyway, negated always outputs exactly the
            same as nand and nor. It's just more convenient to write and easier
            to understand. Hence a dedicated output for a logic negate.

        count: integer
            Adds countvalue to this output for each input that is high.

        countlow: cv
            Adds countvalue to this output for each input that is low.

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    threshold: Optional[str] = None
    lowvalue: Optional[str] = None
    highvalue: Optional[str] = None
    countvalue: Optional[str] = None
    and_: Optional[str] = None
    or_: Optional[str] = None
    xor: Optional[str] = None
    nand: Optional[str] = None
    nor: Optional[str] = None
    negated: Optional[str] = None
    count: Optional[str] = None
    countlow: Optional[str] = None


@dataclass
class Math:
    """Circuit math.
      Math utility circuit

    Inputs:
        input1: cv
            The two inputs

        input2: cv
            The two inputs


    Outputs:
        sum: cv
            input1 +  input2

        difference: cv
            input1 -  input2

        product: cv
            input1× input2

        quotient: cv
            input1 /  input2. If input2 is zero, a very
            large number will be returned, while the correct sign is being
            kept. This is mathematically not correct but more useful than any
            other possible result.

        modulo: cv
            input1 modulo input2. This needs some explanation: With
            this operation you can “fold” the value from input1 into the
            range 0 ... input2. For example if input2 is 1 V, the
            output will convert 1.234 V to 0.234 V, -2.1 V to 0.9 V and 0.5 V
            to 0.5 V. If input2 is zero or negative, the output will be zero.

        power: cv
            input1 to the power of input2. Please note that the
            power has several cases where it is not defined when either
            the base or the exponent is zero or less than zero. In order to
            be as useful for your music making as possible the math circuit behaves
            in the following way:



              * If input1 < 0, input2 is rounded to the nearest integer.

              * If input1 = 0 and input2 < 0, a very large number is output.



        average: cv
            The average of input1 and input2

        maximum: cv
            The maximum of input1 and input2

        minimum: cv
            The minimum of input1 and input2

        negation: cv
            -  input1

        reciprocal: cv
            1 /  input1. If input1 is zero, a very large number
            is being output, while the sign is being kept.

        amount: cv
            The absolute value of input1
            (i.e. -   input1 if input1 < 0, else input1)

        sine: cv
            The sine of input1 in a way, the input range of 0.0 … 1.0
            goes exactly through one wave cycle. Or more mathematically expressed:
            sin(2π× input1).

        cosine: cv
            The cosine of input1 in a way, the input range of 0.0 … 1.0
            goes exactly through one wave cycle. Or more mathematically expressed:
            cos(2π× input1).

        square: cv
            input1^2

        root: cv
            √( input1). Please note that you cannot compute the square
            root of a negative number. In order to output something useful anyway,
            the result will be - √(-  input1), if input1 < 0.

        logarithm: cv
            The natural logarithm of input1: ln _ input1. The
            logarithm is only defined for positive numbers. mathcircuit
            behaves like this:



              * If input1 = 0, a negative very large number is output.

              * If input2 < 0, - ln _-  input1 is output.


        round: cv
            The integer number nearest to input1

        floor: cv
            The largest integer number that is not greater than input1

        ceil: cv
            The smallest integer number that is not less than input1

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    sum: Optional[str] = None
    difference: Optional[str] = None
    product: Optional[str] = None
    quotient: Optional[str] = None
    modulo: Optional[str] = None
    power: Optional[str] = None
    average: Optional[str] = None
    maximum: Optional[str] = None
    minimum: Optional[str] = None
    negation: Optional[str] = None
    reciprocal: Optional[str] = None
    amount: Optional[str] = None
    sine: Optional[str] = None
    cosine: Optional[str] = None
    square: Optional[str] = None
    root: Optional[str] = None
    logarithm: Optional[str] = None
    round: Optional[str] = None
    floor: Optional[str] = None
    ceil: Optional[str] = None


@dataclass
class Matrixmixer:
    """Circuit matrixmixer.
      Matrix mixer for CVs

    Inputs:
        input1: cv
            The up to four CV inputs that you want to mix

        input2: cv
            The up to four CV inputs that you want to mix

        input3: cv
            The up to four CV inputs that you want to mix

        input4: cv
            The up to four CV inputs that you want to mix

        auxin1: cv
            These auxiliary inputs will be mixed directly into the four
            outputs output1 … output4 and are used for
            cascading several matrix mixers into one with more than four
            inputs.

        auxin2: cv
            These auxiliary inputs will be mixed directly into the four
            outputs output1 … output4 and are used for
            cascading several matrix mixers into one with more than four
            inputs.

        auxin3: cv
            These auxiliary inputs will be mixed directly into the four
            outputs output1 … output4 and are used for
            cascading several matrix mixers into one with more than four
            inputs.

        auxin4: cv
            These auxiliary inputs will be mixed directly into the four
            outputs output1 … output4 and are used for
            cascading several matrix mixers into one with more than four
            inputs.

        mixmax: fraction
            If this is 0.0, normal mixing is done (the
            enabled inputs CVs will be added). At a value of 1.0
            instead each outputs is the maximum of the enabled inputs.
            Any number in between will create a weighted average between
            these two values.

        startvalue: integer
            This input selects in which state the matrix begins
            life. Also a trigger to clear will create that starting state.
            The following three configurations can be selected with startvalue:

             0All buttons are cleared.
            1The buttons on the diagonal are active.
            2All buttons are set.


            When set to 1, input1 is sent to output1, input2
            to output2 and so on.

        button11: gate
            These four buttons decide, to which of the four outputs input1
            is being mixed.

        button12: gate
            These four buttons decide, to which of the four outputs input1
            is being mixed.

        button13: gate
            These four buttons decide, to which of the four outputs input1
            is being mixed.

        button14: gate
            These four buttons decide, to which of the four outputs input1
            is being mixed.

        button21: gate
            These four buttons decide, to which of the four outputs input2
            is being mixed.

        button22: gate
            These four buttons decide, to which of the four outputs input2
            is being mixed.

        button23: gate
            These four buttons decide, to which of the four outputs input2
            is being mixed.

        button24: gate
            These four buttons decide, to which of the four outputs input2
            is being mixed.

        button31: gate
            These four buttons decide, to which of the four outputs input3
            is being mixed.

        button32: gate
            These four buttons decide, to which of the four outputs input3
            is being mixed.

        button33: gate
            These four buttons decide, to which of the four outputs input3
            is being mixed.

        button34: gate
            These four buttons decide, to which of the four outputs input3
            is being mixed.

        button41: gate
            These four buttons decide, to which of the four outputs input4
            is being mixed.

        button42: gate
            These four buttons decide, to which of the four outputs input4
            is being mixed.

        button43: gate
            These four buttons decide, to which of the four outputs input4
            is being mixed.

        button44: gate
            These four buttons decide, to which of the four outputs input4
            is being mixed.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output1: cv
            The four outputs

        output2: cv
            The four outputs

        output3: cv
            The four outputs

        output4: cv
            The four outputs

        led11: fraction
            The LEDs in the buttons button11 …button14

        led12: fraction
            The LEDs in the buttons button11 …button14

        led13: fraction
            The LEDs in the buttons button11 …button14

        led14: fraction
            The LEDs in the buttons button11 …button14

        led21: fraction
            The LEDs in the buttons button21 …button24

        led22: fraction
            The LEDs in the buttons button21 …button24

        led23: fraction
            The LEDs in the buttons button21 …button24

        led24: fraction
            The LEDs in the buttons button21 …button24

        led31: fraction
            The LEDs in the buttons button31 …button34

        led32: fraction
            The LEDs in the buttons button31 …button34

        led33: fraction
            The LEDs in the buttons button31 …button34

        led34: fraction
            The LEDs in the buttons button31 …button34

        led41: fraction
            The LEDs in the buttons button41 …button44

        led42: fraction
            The LEDs in the buttons button41 …button44

        led43: fraction
            The LEDs in the buttons button41 …button44

        led44: fraction
            The LEDs in the buttons button41 …button44

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    auxin1: Optional[str] = None
    auxin2: Optional[str] = None
    auxin3: Optional[str] = None
    auxin4: Optional[str] = None
    mixmax: Optional[str] = None
    startvalue: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    button13: Optional[str] = None
    button14: Optional[str] = None
    button21: Optional[str] = None
    button22: Optional[str] = None
    button23: Optional[str] = None
    button24: Optional[str] = None
    button31: Optional[str] = None
    button32: Optional[str] = None
    button33: Optional[str] = None
    button34: Optional[str] = None
    button41: Optional[str] = None
    button42: Optional[str] = None
    button43: Optional[str] = None
    button44: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    led11: Optional[str] = None
    led12: Optional[str] = None
    led13: Optional[str] = None
    led14: Optional[str] = None
    led21: Optional[str] = None
    led22: Optional[str] = None
    led23: Optional[str] = None
    led24: Optional[str] = None
    led31: Optional[str] = None
    led32: Optional[str] = None
    led33: Optional[str] = None
    led34: Optional[str] = None
    led41: Optional[str] = None
    led42: Optional[str] = None
    led43: Optional[str] = None
    led44: Optional[str] = None


@dataclass
class Midifileplayer:
    """Circuit midifileplayer.
      MIDI file player

    Inputs:
        file: integer
            Number of the MIDI file to play. 7 will select midi7.mid.

        track: integer
            Number of the track in the file to play, starting at 1. Empty
            tracks do not count. Any number smaller than 1 will be interpreted
            as one. If the number is too big, the last track in the file
            is played.

        clock: trigger
            Patch an external clock here and the MIDI file will be played
            according to that clock. In order to be modular-friendly, this
            is not a MIDI clock but one counting the sixteenth, which
            is typically the step resolution of analog sequencers. This clock
            is then internally multiplied in order to create the necessary
            resolution. Note: The input speed has no effect when using
            an external clock.

        reset: trigger
            A trigger here sets the play back position to the start.

        loop: gate
            When loop mode is active (set to 1), the track will start
            over again immediately when it has reached its end. This is the
            default. Otherwise playback stops at the end of the track.

        end: integer
            If you set this value, it defines the playing end of the track. This
            is set in quarters as counted from the start. Setting the end beyond the
            end of the track will insert some pause.

        speed: cv
            Change the relative speed of the playback with this setting. At 1
            the speed is unchanged. 1.5 makes the speed 50% faster,
            0.5 plays at half speed. At 0 the playing is completely
            frozen. Note: speed is being ignored when using the input
            clock.

        channel: integer
            Only execute / play commands from a certain MIDI channel.
            There are 16 MIDI channels. It ranges from 1
            to 16.

        tuningmode: gate
            If set to 1, all pitch outputs will go to the CV
            selected for tuningpitch (which defaults to 2 V),
            and all
            gate outputs will play gates at 120 BPM. This helps getting
            all attached voices tuned when working with many voices.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            Transposes all output pitches by this value by adding
            the value. So in order to transpose one octave
            down, set this input to -1V or -0.1. Changes in the
            transposition are immediately reflected, even for currently
            already active notes.

        holdvelocity: gate
            If this is set to 1, the velocity output for a voice
            will not be affected by note off events. It's just altered
            at the beginning of new notes.
            The velocity is kept after the note ends.
            This way during the release phase of an envelope triggered
            by the gate, the original velocity still lasts on. In most cases
            the note off velocity is set to 0, which would
            immediately cut off the release phase when the velocity is patched
            into a VCA.

        pitchbendrange: voltperoctave
            Sets the value to the desired maximum that pitchbend
            should output, and likewise it's negative counterpart at its minimum
            value. At the middle position it always outputs 0. This defaults
            to 2/12 V, which corresponds to one whole tone. Note:
            setting this to a negative value is allowed and will invert
            pitch bend.

        bendpitch: gate
            When set to 1 (which is the default), the pitch bend
            will directly be applied to all output pitches. Alternatively
            you can set it to 0 and use the output pitchbend,
            for using it elsewhere.

        roundrobin: gate
            Normally when looking for a free output for playing the
            next note, this circuit will start from output1
            in its search. This way, if there are not more notes than outputs
            at any time, the notes played first will always be played
            at the lowest numbered outputs. This leads to a deterministic
            behaviour when it comes to playing things like chords. The
            same voice will always be used for the first note in the stream
            of MIDI events.

            When you switch roundrobin to 1, this changes.
            Now the outputs are scanned in a round-robin
            fashion, like in a rotating switch. That way every output has
            the same chance to get a new note. Here it can even make sense
            to define multiple voices even if the track is
            monophonic. When you use envelopes with longer release times,
            you can transform such a melody into chords with simultaneous
            notes.

            Note: When all outputs are currently used by a note, roundrobin
            has no influence. Here voiceallocation selects which of the
            notes will be dropped.

        voiceallocation: integer
            When the MIDI stream, at any given time, needs to play more notes
            than you have voices assigned, normally the “oldest” notes
            would be cancelled. This behaviour can be configured here by
            setting voiceallocation to one of the following values:

            0The oldest note will be cancelled (default)
            1The new note will not be played and simply be omitted
            2The lowest note will be cancelled
            3The highest note will be cancelled




        notegap: cv
            When your MIDI devices plays a note so “long” that it lasts
            exactly until the next note begins – or if due to a lack of
            used pitch outputs one currently played note has to be replaced
            with a new one, the gate output will have no time to go
            low for a sufficient time between the two notes. In effect it
            won't trigger any envelope for the new note but will play “legato”.

            If you don't like this, you can use notegap. This input specifies
            a number of milliseconds that the gate will be forced down
            before the new note begins. This has the drawback of introducing some
            latency, of course! So I suggest that you start with notegap =
            1 and then check out if your envelope is fast enough to trigger.
            If not, increase the value.

            If you are using 's own contour circuit or trigger something
            else internally in your patch, you can use notegap = 0.1. That is
            sufficient and introduces barely any latency.
            A value of 0.0 keeps the default of the legato mode.

            Note: the notegap parameter does not affect the trigger
            outputs.

        ccnumber1: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber2: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber3: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber4: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        lowestnote: integer
            With this input you can restrict the notes being played by setting
            a lower bound. In MIDI the notes range from 0 (C-2) to 127 (G9).
            By setting lowestnote to 24 (C0), all notes below this note are simply
            ignored. This allows for example for a keyboard split by using
            a second circuit with a highestnote of 23. Note gates
            are not being affected by this bound.

        highestnote: integer
            Sets an upper limit to the note being played, similar to
            lowestnote. The “Notegates” are not being affected by this bound.

        note1: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note2: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note3: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note4: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note5: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note6: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note7: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note8: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note9: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note10: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note11: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note12: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note13: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note14: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note15: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note16: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.


    Outputs:
        clockout: trigger
            Outputs a steady clock of 1 tick per 16 note.

        midiclock: trigger
            Outputs a steady MIDI clock, i.e. 24 ticks per quarter note
            of the tune. This is 6 times faster than clock.

        endoftrack: trigger
            Outputs a trigger when the end of the track is reached.

        error: cv
            This output will be set to a value other than zero in case
            of an error while loading and parsing the MIDI file. This is
            intended for wiring it to one of the R registers. Here
            different errors will be displayed as different colors. Here
            is the list of all possible values of error:

            0black – Everything is fine.
            -1white – The SD card or MIDI file is missing.
            1magenta – The file is corrupted, garbled or no MIDI file.
            0.75orange – The file does not contain any non-empty track.
            0.25cyan – the track is too long (max 6000 bytes are allowed).




        pitch1: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch2: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch3: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch4: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch5: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch6: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch7: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch8: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        velocity1: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity2: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity3: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity4: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity5: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity6: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity7: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity8: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        pressure1: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure2: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure3: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure4: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure5: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure6: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure7: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure8: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        gate1: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate2: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate3: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate4: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate5: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate6: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate7: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate8: gate
            Gate outputs for the up to eight simultaneous note outputs.

        trigger1: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger2: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger3: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger4: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger5: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger6: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger7: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger8: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        cc1: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc2: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc3: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc4: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cctrigger1: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger2: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger3: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger4: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        notegate1: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate2: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate3: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate4: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate5: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate6: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate7: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate8: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate9: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate10: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate11: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate12: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate13: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate14: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate15: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate16: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        pitchbend: cv
            Outputs the current pitch bend value as a bipolar voltage.
            The range can be set with pitchbendrange.

        programchange: trigger
            Sends a trigger whenever a MIDI program change message
            arrives. Just before sending the trigger sets program to
            the new program number (something from 0 to 127). Note: This
            trigger is also being output when the program change messages
            sends the same program number as previously, i.e. if there
            is no actual change.

        program: integer
            The number of the last program change. This starts at 0.

        bank: integer
            Outputs the number of the currently selected bank – from
            0 to 16384. MIDI defines the MSB of the bank to be changed
            with CC#0 and the LSB with CC#32. That means if you just
            use CC#0, you will only be able to select the banks 0, 128,
            256, and so on. As long as no bank select CC has been received,
            bank will output 0.

        modwheel: fraction
            Output the current state of the mod wheel level – within
            the range from 0.0 to 1.0. The mod wheel is changed
            by MIDI control change 1.

        volume: fraction
            Outputs the current global volume as set by MIDI control change 7.

        portamento: gate
            This output gives you access to the current state of
            the “portamento pedal” (MIDI CC 65). You can use it to
            enable an external slew circuit for creating portamento
            effects.

        soft: gate
            This output gives you access to the current state of
            the “soft pedal” (MIDI CC 67). It is 1 while the pedal
            is hold and 0 otherwise.

    """


    file: Optional[str] = None
    track: Optional[str] = None
    clock: Optional[str] = None
    reset: Optional[str] = None
    loop: Optional[str] = None
    end: Optional[str] = None
    speed: Optional[str] = None
    channel: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    holdvelocity: Optional[str] = None
    pitchbendrange: Optional[str] = None
    bendpitch: Optional[str] = None
    roundrobin: Optional[str] = None
    voiceallocation: Optional[str] = None
    notegap: Optional[str] = None
    ccnumber1: Optional[str] = None
    ccnumber2: Optional[str] = None
    ccnumber3: Optional[str] = None
    ccnumber4: Optional[str] = None
    lowestnote: Optional[str] = None
    highestnote: Optional[str] = None
    note1: Optional[str] = None
    note2: Optional[str] = None
    note3: Optional[str] = None
    note4: Optional[str] = None
    note5: Optional[str] = None
    note6: Optional[str] = None
    note7: Optional[str] = None
    note8: Optional[str] = None
    note9: Optional[str] = None
    note10: Optional[str] = None
    note11: Optional[str] = None
    note12: Optional[str] = None
    note13: Optional[str] = None
    note14: Optional[str] = None
    note15: Optional[str] = None
    note16: Optional[str] = None
    clockout: Optional[str] = None
    midiclock: Optional[str] = None
    endoftrack: Optional[str] = None
    error: Optional[str] = None
    pitch1: Optional[str] = None
    pitch2: Optional[str] = None
    pitch3: Optional[str] = None
    pitch4: Optional[str] = None
    pitch5: Optional[str] = None
    pitch6: Optional[str] = None
    pitch7: Optional[str] = None
    pitch8: Optional[str] = None
    velocity1: Optional[str] = None
    velocity2: Optional[str] = None
    velocity3: Optional[str] = None
    velocity4: Optional[str] = None
    velocity5: Optional[str] = None
    velocity6: Optional[str] = None
    velocity7: Optional[str] = None
    velocity8: Optional[str] = None
    pressure1: Optional[str] = None
    pressure2: Optional[str] = None
    pressure3: Optional[str] = None
    pressure4: Optional[str] = None
    pressure5: Optional[str] = None
    pressure6: Optional[str] = None
    pressure7: Optional[str] = None
    pressure8: Optional[str] = None
    gate1: Optional[str] = None
    gate2: Optional[str] = None
    gate3: Optional[str] = None
    gate4: Optional[str] = None
    gate5: Optional[str] = None
    gate6: Optional[str] = None
    gate7: Optional[str] = None
    gate8: Optional[str] = None
    trigger1: Optional[str] = None
    trigger2: Optional[str] = None
    trigger3: Optional[str] = None
    trigger4: Optional[str] = None
    trigger5: Optional[str] = None
    trigger6: Optional[str] = None
    trigger7: Optional[str] = None
    trigger8: Optional[str] = None
    cc1: Optional[str] = None
    cc2: Optional[str] = None
    cc3: Optional[str] = None
    cc4: Optional[str] = None
    cctrigger1: Optional[str] = None
    cctrigger2: Optional[str] = None
    cctrigger3: Optional[str] = None
    cctrigger4: Optional[str] = None
    notegate1: Optional[str] = None
    notegate2: Optional[str] = None
    notegate3: Optional[str] = None
    notegate4: Optional[str] = None
    notegate5: Optional[str] = None
    notegate6: Optional[str] = None
    notegate7: Optional[str] = None
    notegate8: Optional[str] = None
    notegate9: Optional[str] = None
    notegate10: Optional[str] = None
    notegate11: Optional[str] = None
    notegate12: Optional[str] = None
    notegate13: Optional[str] = None
    notegate14: Optional[str] = None
    notegate15: Optional[str] = None
    notegate16: Optional[str] = None
    pitchbend: Optional[str] = None
    programchange: Optional[str] = None
    program: Optional[str] = None
    bank: Optional[str] = None
    modwheel: Optional[str] = None
    volume: Optional[str] = None
    portamento: Optional[str] = None
    soft: Optional[str] = None


@dataclass
class Midiin:
    """Circuit midiin.
      MIDI to CV converter

    Inputs:
        trs: integer
            Selects a TRS port to use (3.5 mm jack).
            trs = 0 disables TRS, trs = 10
            enables auto detection. See the manual of midiin for details on port
            selection.

        usb: integer
            Selects a USB port to use.
            usb = 0 disables USB, usb = 10
            enables auto detection. See the manual of midiin for details on port
            selection.

        initialrunning: integer
            This parameter sets which “running” state is assumed when your
            starts. The idea behind this parameter is, that at this point
            of time you cannot know the real running state of the MIDI stream,
            since e.g. the might have started after the sequencer at the
            sending end of the line.

            You have three ways to set this: start in stopped state, start
            in running state and an inbetween “automatic” mode. In the
            auto mode, you start in stopped state but automatically switch
            to running as soon as a note on event is received. At that moment
            a MIDI START event is simulated.

            0Start stopped state
            1Start in running state
            2Automatic: start in stopped state, switch to running on first “note on”


            Note: as this parameter is just read once the absolute system start,
            you cannot assign a dynamic CV input or control here.

        systemreset: trigger
            A trigger here resets the whole MIDI state of this circuit.
            It does the same as a MIDI RESET message: It stops all
            playing note, resets the controllers, the states of the
            pedals and so on.

        channel: integer
            Only execute / play commands from a certain MIDI channel.
            There are 16 MIDI channels. It ranges from 1
            to 16.

        tuningmode: gate
            If set to 1, all pitch outputs will go to the CV
            selected for tuningpitch (which defaults to 2 V),
            and all
            gate outputs will play gates at 120 BPM. This helps getting
            all attached voices tuned when working with many voices.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            Transposes all output pitches by this value by adding
            the value. So in order to transpose one octave
            down, set this input to -1V or -0.1. Changes in the
            transposition are immediately reflected, even for currently
            already active notes.

        holdvelocity: gate
            If this is set to 1, the velocity output for a voice
            will not be affected by note off events. It's just altered
            at the beginning of new notes.
            The velocity is kept after the note ends.
            This way during the release phase of an envelope triggered
            by the gate, the original velocity still lasts on. In most cases
            the note off velocity is set to 0, which would
            immediately cut off the release phase when the velocity is patched
            into a VCA.

        pitchbendrange: voltperoctave
            Sets the value to the desired maximum that pitchbend
            should output, and likewise it's negative counterpart at its minimum
            value. At the middle position it always outputs 0. This defaults
            to 2/12 V, which corresponds to one whole tone. Note:
            setting this to a negative value is allowed and will invert
            pitch bend.

        bendpitch: gate
            When set to 1 (which is the default), the pitch bend
            will directly be applied to all output pitches. Alternatively
            you can set it to 0 and use the output pitchbend,
            for using it elsewhere.

        roundrobin: gate
            Normally when looking for a free output for playing the
            next note, this circuit will start from output1
            in its search. This way, if there are not more notes than outputs
            at any time, the notes played first will always be played
            at the lowest numbered outputs. This leads to a deterministic
            behaviour when it comes to playing things like chords. The
            same voice will always be used for the first note in the stream
            of MIDI events.

            When you switch roundrobin to 1, this changes.
            Now the outputs are scanned in a round-robin
            fashion, like in a rotating switch. That way every output has
            the same chance to get a new note. Here it can even make sense
            to define multiple voices even if the track is
            monophonic. When you use envelopes with longer release times,
            you can transform such a melody into chords with simultaneous
            notes.

            Note: When all outputs are currently used by a note, roundrobin
            has no influence. Here voiceallocation selects which of the
            notes will be dropped.

        voiceallocation: integer
            When the MIDI stream, at any given time, needs to play more notes
            than you have voices assigned, normally the “oldest” notes
            would be cancelled. This behaviour can be configured here by
            setting voiceallocation to one of the following values:

            0The oldest note will be cancelled (default)
            1The new note will not be played and simply be omitted
            2The lowest note will be cancelled
            3The highest note will be cancelled




        notegap: cv
            When your MIDI devices plays a note so “long” that it lasts
            exactly until the next note begins – or if due to a lack of
            used pitch outputs one currently played note has to be replaced
            with a new one, the gate output will have no time to go
            low for a sufficient time between the two notes. In effect it
            won't trigger any envelope for the new note but will play “legato”.

            If you don't like this, you can use notegap. This input specifies
            a number of milliseconds that the gate will be forced down
            before the new note begins. This has the drawback of introducing some
            latency, of course! So I suggest that you start with notegap =
            1 and then check out if your envelope is fast enough to trigger.
            If not, increase the value.

            If you are using 's own contour circuit or trigger something
            else internally in your patch, you can use notegap = 0.1. That is
            sufficient and introduces barely any latency.
            A value of 0.0 keeps the default of the legato mode.

            Note: the notegap parameter does not affect the trigger
            outputs.

        ccnumber1: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber2: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber3: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        ccnumber4: integer
            You can listen to up to four CCs (control changes). For example
            if you are interested in the current value of CC#17, set
            ccnumber1 = 17 and use the output cc1 for getting the value
            of CC 17.

        lowestnote: integer
            With this input you can restrict the notes being played by setting
            a lower bound. In MIDI the notes range from 0 (C-2) to 127 (G9).
            By setting lowestnote to 24 (C0), all notes below this note are simply
            ignored. This allows for example for a keyboard split by using
            a second circuit with a highestnote of 23. Note gates
            are not being affected by this bound.

        highestnote: integer
            Sets an upper limit to the note being played, similar to
            lowestnote. The “Notegates” are not being affected by this bound.

        note1: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note2: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note3: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note4: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note5: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note6: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note7: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note8: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note9: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note10: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note11: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note12: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note13: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note14: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note15: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.

        note16: integer
            Selects up to 16 individual notes for which you can get a
            dedicated gate signal. Per default these values are set to
            0 for note1 (meaning C-2), 1 for note2
            (meaning C♯-2) and so on. For each of these notes
            you get a corresponding gate output (see notegate1, notegate2, etc.).
            These gates are high as long as the selected notes are being hold.
            One application is to use just one midifileplayer or midiin
            circuit for sequencing up to 16 drum voices. Another application is
            to use a MIDI keyboard or controller as a button expander – just
            like a P2B8 or B32.


    Outputs:
        clock: trigger
            If the MIDI sender sends a MIDI clock, you get a 16
            note clock output here. This is the same as the clock16 jack
            and just a convenient abbreviation.

        clock8: trigger
            Gets an 8 clock here (like clock divided by 2)

        clock8t: trigger
            Gets a 8 triplets clock here. This is faster than
            clock8 but slower than clock.

        clock16: trigger
            The same as clock: a clock running at 16 notes.

        clock4: trigger
            A clock at the speed of quarter notes.

        midiclock: trigger
            Here you get the original MIDI clock. This is 6 times
            faster than clock and 24 times faster than clock4. This
            is because the MIDI clock is specified to run at 24 PPQ, i.e.
            24 pulses per quarter note.

        start: trigger
            This jack sends a trigger when a MIDI START message arrives.

        continue_: trigger
            This jack sends a trigger when a MIDI CONTINUE message arrives.

        stop: trigger
            This jack sends a trigger when a MIDI STOP message arrives.

        running: gate
            This jack remembers the current running state according to
            previous START and STOP messages.

        active: gate
            If the sending device supports active sensing, this output
            is high as long as a device is connected. Otherwise its high if
            at least one MIDI message has been received.

        pitch1: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch2: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch3: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch4: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch5: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch6: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch7: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        pitch8: voltperoctave
            Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play
            several notes at the same time – you can assign up to eight outputs
            here. The notes will be distributed to the defined outputs
            according to the settings roundrobin and voiceallocation.

        velocity1: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity2: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity3: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity4: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity5: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity6: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity7: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        velocity8: fraction
            For each voice there is an optional velocity output, which
            translates the MIDI velocity into values from 0 to 1.

        pressure1: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure2: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure3: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure4: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure5: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure6: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure7: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        pressure8: fraction
            MIDI provides two different messages for sending "after-touch"
            information, i.e. information about how strong a key is pressed
            down after the initial hit. Some keyboards just have one pressure
            sensor in total and send the current maximum pressure information
            of all keys in one message (“channel pressure”). Others have
            one pressure sensor per key and send “polyphonic key pressure”
            messages. This circuit maps both to a pressure output
            per note that is being played. So if your keyboard (or sequencer
            or DAW or whatever) sends polyphonic key pressure events and
            you use multiple pitchX outputs, wire the individual
            pressureX outputs to wherever you like. Otherwise
            you can simply use pressure1 for all notes (which can
            be abbreviated with pressure), since it is the same for
            all note outputs anyway. pressure outputs a value from
            0 to 1.

        gate1: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate2: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate3: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate4: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate5: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate6: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate7: gate
            Gate outputs for the up to eight simultaneous note outputs.

        gate8: gate
            Gate outputs for the up to eight simultaneous note outputs.

        trigger1: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger2: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger3: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger4: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger5: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger6: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger7: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        trigger8: trigger
            Trigger outputs for the up to eight simultaneous note outputs. The
            difference to the gate outputs is, that these just send a short
            trigger of 5 ms at the start of the note. This can be interesting
            in situations where the notes have no gaps in between so
            that gate will never go low.

        cc1: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc2: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc3: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cc4: fraction
            Outputs the current value of the four CC number that are defined
            with the inputs ccnumber1 ... ccnumber4. CCs have a
            range from 0 to 127, but this is converted in the range 0.0 .. 1.0
            here, in order to make it easier to use that as a CV. If you need
            the raw number, multiply the output with 127. Note: as long as no CC
            message with the selected number happened, this output will be set
            to 0.

        cctrigger1: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger2: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger3: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        cctrigger4: trigger
            These outputs send a trigger whenever a CC event matching the
            corresponding ccnumber is processed. Some devices uses triggers
            in such a way – as events rather then indicating the change of a
            continous value. So if you set ccnumber2 = 17, the output
            cctrigger2 sends a trigger whenever CC#17 is received.

        notegate1: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate2: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate3: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate4: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate5: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate6: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate7: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate8: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate9: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate10: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate11: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate12: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate13: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate14: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate15: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        notegate16: gate
            Outputs a high gate whenever the corresponding note (which is
            selected by note1 through note16) is currently being played.

        pitchbend: cv
            Outputs the current pitch bend value as a bipolar voltage.
            The range can be set with pitchbendrange.

        programchange: trigger
            Sends a trigger whenever a MIDI program change message
            arrives. Just before sending the trigger sets program to
            the new program number (something from 0 to 127). Note: This
            trigger is also being output when the program change messages
            sends the same program number as previously, i.e. if there
            is no actual change.

        program: integer
            The number of the last program change. This starts at 0.

        bank: integer
            Outputs the number of the currently selected bank – from
            0 to 16384. MIDI defines the MSB of the bank to be changed
            with CC#0 and the LSB with CC#32. That means if you just
            use CC#0, you will only be able to select the banks 0, 128,
            256, and so on. As long as no bank select CC has been received,
            bank will output 0.

        modwheel: fraction
            Output the current state of the mod wheel level – within
            the range from 0.0 to 1.0. The mod wheel is changed
            by MIDI control change 1.

        volume: fraction
            Outputs the current global volume as set by MIDI control change 7.

        portamento: gate
            This output gives you access to the current state of
            the “portamento pedal” (MIDI CC 65). You can use it to
            enable an external slew circuit for creating portamento
            effects.

        soft: gate
            This output gives you access to the current state of
            the “soft pedal” (MIDI CC 67). It is 1 while the pedal
            is hold and 0 otherwise.

    """


    trs: Optional[str] = None
    usb: Optional[str] = None
    initialrunning: Optional[str] = None
    systemreset: Optional[str] = None
    channel: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    holdvelocity: Optional[str] = None
    pitchbendrange: Optional[str] = None
    bendpitch: Optional[str] = None
    roundrobin: Optional[str] = None
    voiceallocation: Optional[str] = None
    notegap: Optional[str] = None
    ccnumber1: Optional[str] = None
    ccnumber2: Optional[str] = None
    ccnumber3: Optional[str] = None
    ccnumber4: Optional[str] = None
    lowestnote: Optional[str] = None
    highestnote: Optional[str] = None
    note1: Optional[str] = None
    note2: Optional[str] = None
    note3: Optional[str] = None
    note4: Optional[str] = None
    note5: Optional[str] = None
    note6: Optional[str] = None
    note7: Optional[str] = None
    note8: Optional[str] = None
    note9: Optional[str] = None
    note10: Optional[str] = None
    note11: Optional[str] = None
    note12: Optional[str] = None
    note13: Optional[str] = None
    note14: Optional[str] = None
    note15: Optional[str] = None
    note16: Optional[str] = None
    clock: Optional[str] = None
    clock8: Optional[str] = None
    clock8t: Optional[str] = None
    clock16: Optional[str] = None
    clock4: Optional[str] = None
    midiclock: Optional[str] = None
    start: Optional[str] = None
    continue_: Optional[str] = None
    stop: Optional[str] = None
    running: Optional[str] = None
    active: Optional[str] = None
    pitch1: Optional[str] = None
    pitch2: Optional[str] = None
    pitch3: Optional[str] = None
    pitch4: Optional[str] = None
    pitch5: Optional[str] = None
    pitch6: Optional[str] = None
    pitch7: Optional[str] = None
    pitch8: Optional[str] = None
    velocity1: Optional[str] = None
    velocity2: Optional[str] = None
    velocity3: Optional[str] = None
    velocity4: Optional[str] = None
    velocity5: Optional[str] = None
    velocity6: Optional[str] = None
    velocity7: Optional[str] = None
    velocity8: Optional[str] = None
    pressure1: Optional[str] = None
    pressure2: Optional[str] = None
    pressure3: Optional[str] = None
    pressure4: Optional[str] = None
    pressure5: Optional[str] = None
    pressure6: Optional[str] = None
    pressure7: Optional[str] = None
    pressure8: Optional[str] = None
    gate1: Optional[str] = None
    gate2: Optional[str] = None
    gate3: Optional[str] = None
    gate4: Optional[str] = None
    gate5: Optional[str] = None
    gate6: Optional[str] = None
    gate7: Optional[str] = None
    gate8: Optional[str] = None
    trigger1: Optional[str] = None
    trigger2: Optional[str] = None
    trigger3: Optional[str] = None
    trigger4: Optional[str] = None
    trigger5: Optional[str] = None
    trigger6: Optional[str] = None
    trigger7: Optional[str] = None
    trigger8: Optional[str] = None
    cc1: Optional[str] = None
    cc2: Optional[str] = None
    cc3: Optional[str] = None
    cc4: Optional[str] = None
    cctrigger1: Optional[str] = None
    cctrigger2: Optional[str] = None
    cctrigger3: Optional[str] = None
    cctrigger4: Optional[str] = None
    notegate1: Optional[str] = None
    notegate2: Optional[str] = None
    notegate3: Optional[str] = None
    notegate4: Optional[str] = None
    notegate5: Optional[str] = None
    notegate6: Optional[str] = None
    notegate7: Optional[str] = None
    notegate8: Optional[str] = None
    notegate9: Optional[str] = None
    notegate10: Optional[str] = None
    notegate11: Optional[str] = None
    notegate12: Optional[str] = None
    notegate13: Optional[str] = None
    notegate14: Optional[str] = None
    notegate15: Optional[str] = None
    notegate16: Optional[str] = None
    pitchbend: Optional[str] = None
    programchange: Optional[str] = None
    program: Optional[str] = None
    bank: Optional[str] = None
    modwheel: Optional[str] = None
    volume: Optional[str] = None
    portamento: Optional[str] = None
    soft: Optional[str] = None


@dataclass
class Midiout:
    """Circuit midiout.
      CV to MIDI converter

    Inputs:
        channel: integer
            Selects the MIDI channel to send the events on. Default is to send on
            channel 1. There are 16 channels. Make sure that the receiving device
            listens to this (or to all) channels.

        usb: gate
            Set usb = 1 if you want to send the MIDI output to the USB-C port.
            You can set trs = 1, as well, for sending the data to both outputs.
            If you don't use usb nor trs, the output will be sent to the
            TRS output only.

        trs: gate
            This controls wether the MIDI data is sent via the TRS output of the X7.
            If you just want the TRS output, you don't need this, because that is
            the default. If you want the output both on USB and TRS, you need to
            set usb = 1 and trs = 1 at the same time.

        pitch1: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch2: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch3: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch4: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch5: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch6: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch7: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        pitch8: voltperoctave
            Pitch of the notes to be played in modular style (1 V/octave).
            The range is from -2 V (MIDI note 0, usually C-2) to 8.583 V
            (MIDI note 127, usually G9). You can use up to eight pitch inputs
            for playing up to eight notes in parallel. pitch1 can
            be abbreviated with just pitch.

        gate1: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate2: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate3: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate4: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate5: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate6: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate7: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        gate8: gate
            A positive edge into the gate jacks trigger note on messages
            (starts the note at the pitch set by the corresponding pitch input).
            A negative edge ends the currently played note.

        velocity1: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity2: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity3: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity4: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity5: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity6: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity7: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        velocity8: fraction
            The velocities for the up to eight notes. The velocity value is
            just picked up at the start of the note (at the positive edge of
            the corresponding gate inputs. It ranges from 0.0 to 1.0.
            A value of 0.0 is practically the same as “note off”. The
            default velocity is 1.0.

        noteoffvelocity1: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity2: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity3: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity4: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity5: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity6: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity7: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        noteoffvelocity8: fraction
            MIDI also sends a velocity at the end of a note. The idea
            is to model the speed with which a key is being released.
            This is rarely used. If you don't use these jacks, the
            velocity for “note off” events is the same as that for “note on”
            events.

        pressure1: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure2: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure3: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure4: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure5: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure6: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure7: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        pressure8: fraction
            Sends key pressure events for individually played notes via
            the MIDI event “polyphonic key pressure” (this is not a CC!).
            These values are not processed at the time of note on/off events but
            all the time and can also change while a note is already being
            played. This corresponds to “aftertouch” key pressure on keyboards
            that have a pressure sensor per key.

            If nothing is patched here, no pressure events are sent.

        channelpressure: fraction
            Whenever this CV changes, sends a MIDI channel pressure event,
            also known as “aftertouch”. This corresponds to keyboards that
            just have one global pressure sensor and not one per key.

            If nothing is patched here, no channel pressure events are sent.

        pitchstabilization: gate
            Enables or disables pitch stabilization. It is on per default
            and can be disabled by setting this jack to 0. Pitch stabilization
            fixes timing issues where the input pitch needs some time for
            reaching the target pitch after a gate.

        triggerdelay: cv
            Introduces a delay between in the incoming gate signal (just the
            positive edge) and the “note on” event. This can tackle the
            problem when your pitch input (sequencer etc.) needs some time
            after the gate in order to reach and stabilize the target pitch.
            The delay is specified in milliseconds, so a typical useful value would
            be 5 (5 ms). This is an alternative to the automatic
            pitchstabilization. Note: triggerdelay disables
            pitchstabilization, as long as that is not set to 1
            explicitly. If both are used at the same time, the triggerdelay
            happens before the pitch stabilization. So it is a minimum
            delay.

        lowestnote: integer
            With this input you can restrict the notes being played by setting
            a lower bound. In MIDI the notes range from 0 (C-2) to 127 (G9).
            By setting lowestnote to 24 (C0), all notes below this note are simply
            ignored. This allows for example for a keyboard split by using
            a second circuit with a highestnote of 23. Note gates
            are not being affected by this bound.

        highestnote: integer
            Sets an upper limit to the note being played, similar to
            lowestnote. Note gates are not being affected by this bound.

        notegate1: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate2: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate3: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate4: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate5: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate6: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate7: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate8: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate9: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate10: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate11: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate12: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate13: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate14: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate15: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        notegate16: gate
            You can define up to 16 notes that can be directly controlled
            with a dedicated gate. This is convenient for playing drum sounds
            directly from triggers and also for using DROID controllers as
            MIDI controllers. A trigger or gate to notegate1 will directly
            play the note whose pitch is set by note1.

        note1: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note2: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note3: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note4: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note5: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note6: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note7: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note8: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note9: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note10: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note11: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note12: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note13: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note14: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note15: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        note16: integer
            MIDI notes to played via notegate. The range is from
            0 to 127.  Per default the notes are set to the MIDI notes 0, 1, 2
            ... 15.

        notegatevelocity1: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity2: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity3: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity4: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity5: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity6: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity7: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity8: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity9: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity10: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity11: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity12: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity13: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity14: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity15: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        notegatevelocity16: fraction
            Here you can set the velocities use by the notegates.
            In order to keep it simple, this velocity is used for note on
            and note off events (nobody cares about the note off
            velocity anyway). If you do not use these jacks, the note
            gates will always use the maximum velocity.

        modwheel: fraction
            Sets the current value of the modulation wheel. Any change
            here sends a midi CC#1 with a new value for the modulation wheel.
            The input range is 0.0 ... 1.0 and will be converted into the
            MIDI range of 0 ... 127. Note: in future we might support
            CC#33, which is the LSB value of CC#1 and increases the resolution
            from 128 to 16384 different values, at the cost – however – of
            two additional bytes being sent.

        volume: fraction
            Sets the volume of the target device. This is done by sending the
            MIDI CC#7 (VOLUME MSB) and MIDI CC#39 (VOLUME LSB). Using these
            two CCs enables a 14 bit high resolution 16384 levels (not just 127).
            Some devices to not react to CC#39 and simply ignore the LSB (least
            significant byte). The volume CV ranges from 0.0 (silent) to 1.0
            (the default).

        pitchbend: cv
            Bends the pitches of all currently played notes up
            and down by a range that is configured or elsewhere defined
            by the device that plays our stuff. The range of this CV is
            -1.0 ... 1.0 for covering the maximum pitch bend range. Most
            times that range is two semitones up and down. This
            CV does not behave in a 1V/oct way!

        pitchtracking: integer
            Pitch tracking is an advanced feature that allows you to track
            continuous changes in the incoming pitch CV while the note
            is already playing. It does this by listening to the input CV
            and converting any change into a MIDI “pitch bend” change.

            This feature has two limitations:
            First, there is just one global pitch bend value per channel, not
            one per note. So this feature only works in a monophonic situation.
            Only the value of pitch1 is being tracked.
            When you play more than one note per channel, funny things might
            probably happen.
            Also The maximum range is limited by the pitch bend range of
            your target device. That is usually preset to 2 semitones up and
            down. If you can increase it, please also adapt pitchbandrange
            so this circuit knows about it.

            Pitch tracking has two levels: pitchbandrange = 1 will
            alter the pitch of the current note within the maximum range
            of pitch bend and will clip any further changes.
            pitchbendrange = 2, in contrast, plays a new note if the
            current range is exceeded. Depending on your sound settings
            this “dent” might be audible or not.

             0pitch tracking is off
            1just use MIDI pitch bend
            2use new note on larger changes


            Note: When you use pitch tracking at the same time as
            pitchbend, both pitch alterations will add up.

        pitchbendrange: voltperoctave
            Defines the range of the effect of pitch bend at the target
            device on a 1V/oct base. Note: You cannot change that actual
            range here. You just can make sure that this circuit has the correct
            assumption of that range.

            If your target device has a configuration for extending the range,
            and you have set that for example to 1 octave, set pitchbendrange to 1 V.
            This allows pitchtracking to correctly adapt in-note pitch
            changes. Note: This has no effect on the pitchbend CV.

        ccnumber1: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber2: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber3: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber4: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber5: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber6: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber7: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        ccnumber8: integer
            Specifies up to eight different CC numbers that can be continuously
            updated via the corresponding cc1 through cc8 inputs.
            The value needs to be an integer number from 0 to 127.

        cc1: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc2: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc3: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc4: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc5: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc6: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc7: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cc8: fraction
            The current value of the CCs that are specified with ccnumber1
            through ccnumber8. The range is always from 0.0 to 1.0 (which is
            mapped to the number 0 to 127 on the MIDI wire).

            If you don't patch anything here, no CC events will be sent, of course.

        cctrigger1: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger2: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger3: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger4: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger5: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger6: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger7: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        cctrigger8: trigger
            Usually midiout will send out a new CC event every time the
            input value of a CC has changed (with some rate limit in order not to
            to flood the MIDI stream).

            When you use these inputs, an alternative method is enabled. Now
            CC events are created whenever a trigger arrives here. No more
            updates will be sent automatically.

            This is useful for target devices that use CCs just as messages,
            i.e. as one time events and not for updating a continous value.

        updateccs: trigger
            A trigger here sends an update for all CCs that you have in
            use (used ccX inputs).  Normally an update is just sent once
            initially and then when the input CV at one of the cc inputs
            changes its value. With the trigger you can force updates. This
            might be neccessary if the receiving device has lost memory of the
            current states of the CCs (e.g. due to a power cycle).

            Note: Unlike the cctriggerX inputs, this trigger does
            not change the way the CC inputs work. It is just a
            hint for that forces one additonal update.

        delayinitialccs: cv
            When the Droid starts it needs a short time until the X7
            is operating and your PC / DAW is able to receive the MIDI events
            via USB. Initial CC updates during that short time period might
            get lost and you are missing the correct CC states (which are
            updated later only on changes).

            In order to avoid that, the Droid wait a short time after
            starting before it sends the first CC events. That delay can
            be tuned here. It is a time in seconds.

        bank: integer
            Selects the current “bank”.
            Some MIDI devices have more than 128 programs (i.e., patches,
            instruments, preset, etc). A MIDI Program Change message supports
            switching between only 128 programs. So, “Bank Select”
            (sometimes also called bank switch) is sometimes used to allow switching
            between groups of 128 programs. Bank select uses the MIDI CCs #0 (MSB)
            and #32 (LSB) together to form a number of 16384 different banks. The
            input value thus ranges from 1 to 16384.
            Most devices, however, restrict themselves to just 128 banks and just
            use the MSB (CC#0). If that is the case, you need to set
            bank to 128 for bank 2, 256 for bank 3 and so on. This
            can be done by simply multiplying the actual bank number with 128.

        program: integer
            Select the current “program”. This is a number from 1 to 128.

        programchange: trigger
            A trigger here will send out a “program change” MIDI message even
            if the value of bank or program has not changed.

        start: trigger
            If you send a trigger here, the MIDI message START will be emitted.
            Don't use this jack if you also use running. Note: START/STOP
            messages are not bound to a specific channel.

        stop: trigger
            If you send a trigger here, the MIDI message STOP will be emitted.
            Don't use this jack if you also use running. Note: START/STOP
            messages are not bound to a specific channel.

        running: gate
            This is an alternative to the jacks start and stop. It combines
            both into one “running” state. When this gate input goes high,
            a START message is sent, when it goes low a STOP message. So you can
            work with a state rather than with state changes. Note: START/STOP
            messages are not bound to a specific channel.

        systemreset: trigger
            A trigger here will send the MIDI real-time message “RESET”,
            that is supposed to bring the device into some start state.

        allnotesoff: trigger
            A trigger here will send the MIDI CC#123 “ALL NOTES OFF”, which
            is essentially the same as releasing all currently held keys.

        allsoundoff: trigger
            A trigger here will send the MIDI CC#120 “ALL SOUND OFF”, which
            is supposed to make the device silent as soon as possible.

        damper: gate
            This gate input simulates a hold or damper pedal. This is done
            via the CC#64. If the gate goes to high, a value of 127 is being
            sent, when it goes back to low, a value of 0. When the damper pedal
            is pressed, the device is supposed to hold all currently played
            notes and not react to any subsequent “NOTE OFF” of those
            notes as long as the pedal is held. When the pedal is released,
            all notes that had been held be the pedal should be released.

        portamento: gate
            Controls the portamento pedal. The receiver is meant to activate
            some kind of glide effect as long as this gate is high.

        sostenuto: gate
            This enables the sustain pedal. This is similar to but not exactly
            the same as the damper pedal as it just holds notes that are pressed
            while the pedal goes down.

        soft: gate
            Controls the soft pedal. The receiving synth voice is meant to
            play notes softer while this pedal is hold down.

        legato: gate
            Controls the legato pedal, which ties subsequent notes together.

        clock: trigger
            If you feed a steady clock here, a MIDI clock signal will be
            derived from this and sent through the output wire. The MIDI beat
            clock or simply MIDI clock is defined to send pulses at 24 PPQN:
            24 pulses per quarter note. One quarter note has four 16s, so
            the MIDI clock is running at 6 pulses per 16 note, and in the modular
            environment it is very common to work with 16 pulses as a master
            clock. So this clock jack is meant to retrieve a modular master clock,
            multiplies this by 6 and creates a MIDI clock from it.

        midiclock: trigger
            This is an alternative to clock: don't use both at the same
            time. Here you can directly send the MIDI clock in 24 PPQN.

        activesensing: gate
            This is a switch that disables or enables active sensing. This
            is a MIDI feature where a MIDI sender emits one message of the type
            “active sensing” every 300 ms. The receiver can use this in order
            to detect if the connection is still active and also immediately
            reset (und turn all sound off) if it is not. Active sensing
            is enabled per default. You can disable it here by setting activesensing = 0.

            Note: If you have more than one midiout circuit sending
            to the same port, you should activate activesensing just for
            one of them in order to avoid useless duplicate MIDI events.

        updaterate: cv
            Specifies the maximum rate at which continuous controllers like
            the CCs, volume, pitchbend and channelpressure are updated. This
            limitation is necessary in order not to flood the MIDI interface
            with too many updates because of just minimal changes. This
            rate is specified in update per second and the default is 50.
            A zero or negative value will completely stop all updates.

            Note: depending on how many events are happening on your channel,
            fewer updates might be possible. MIDI over a classical cable is limited
            to 3125 bytes per second. Events typically need 1, 2 or 3 bytes each.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:

    """


    channel: Optional[str] = None
    usb: Optional[str] = None
    trs: Optional[str] = None
    pitch1: Optional[str] = None
    pitch2: Optional[str] = None
    pitch3: Optional[str] = None
    pitch4: Optional[str] = None
    pitch5: Optional[str] = None
    pitch6: Optional[str] = None
    pitch7: Optional[str] = None
    pitch8: Optional[str] = None
    gate1: Optional[str] = None
    gate2: Optional[str] = None
    gate3: Optional[str] = None
    gate4: Optional[str] = None
    gate5: Optional[str] = None
    gate6: Optional[str] = None
    gate7: Optional[str] = None
    gate8: Optional[str] = None
    velocity1: Optional[str] = None
    velocity2: Optional[str] = None
    velocity3: Optional[str] = None
    velocity4: Optional[str] = None
    velocity5: Optional[str] = None
    velocity6: Optional[str] = None
    velocity7: Optional[str] = None
    velocity8: Optional[str] = None
    noteoffvelocity1: Optional[str] = None
    noteoffvelocity2: Optional[str] = None
    noteoffvelocity3: Optional[str] = None
    noteoffvelocity4: Optional[str] = None
    noteoffvelocity5: Optional[str] = None
    noteoffvelocity6: Optional[str] = None
    noteoffvelocity7: Optional[str] = None
    noteoffvelocity8: Optional[str] = None
    pressure1: Optional[str] = None
    pressure2: Optional[str] = None
    pressure3: Optional[str] = None
    pressure4: Optional[str] = None
    pressure5: Optional[str] = None
    pressure6: Optional[str] = None
    pressure7: Optional[str] = None
    pressure8: Optional[str] = None
    channelpressure: Optional[str] = None
    pitchstabilization: Optional[str] = None
    triggerdelay: Optional[str] = None
    lowestnote: Optional[str] = None
    highestnote: Optional[str] = None
    notegate1: Optional[str] = None
    notegate2: Optional[str] = None
    notegate3: Optional[str] = None
    notegate4: Optional[str] = None
    notegate5: Optional[str] = None
    notegate6: Optional[str] = None
    notegate7: Optional[str] = None
    notegate8: Optional[str] = None
    notegate9: Optional[str] = None
    notegate10: Optional[str] = None
    notegate11: Optional[str] = None
    notegate12: Optional[str] = None
    notegate13: Optional[str] = None
    notegate14: Optional[str] = None
    notegate15: Optional[str] = None
    notegate16: Optional[str] = None
    note1: Optional[str] = None
    note2: Optional[str] = None
    note3: Optional[str] = None
    note4: Optional[str] = None
    note5: Optional[str] = None
    note6: Optional[str] = None
    note7: Optional[str] = None
    note8: Optional[str] = None
    note9: Optional[str] = None
    note10: Optional[str] = None
    note11: Optional[str] = None
    note12: Optional[str] = None
    note13: Optional[str] = None
    note14: Optional[str] = None
    note15: Optional[str] = None
    note16: Optional[str] = None
    notegatevelocity1: Optional[str] = None
    notegatevelocity2: Optional[str] = None
    notegatevelocity3: Optional[str] = None
    notegatevelocity4: Optional[str] = None
    notegatevelocity5: Optional[str] = None
    notegatevelocity6: Optional[str] = None
    notegatevelocity7: Optional[str] = None
    notegatevelocity8: Optional[str] = None
    notegatevelocity9: Optional[str] = None
    notegatevelocity10: Optional[str] = None
    notegatevelocity11: Optional[str] = None
    notegatevelocity12: Optional[str] = None
    notegatevelocity13: Optional[str] = None
    notegatevelocity14: Optional[str] = None
    notegatevelocity15: Optional[str] = None
    notegatevelocity16: Optional[str] = None
    modwheel: Optional[str] = None
    volume: Optional[str] = None
    pitchbend: Optional[str] = None
    pitchtracking: Optional[str] = None
    pitchbendrange: Optional[str] = None
    ccnumber1: Optional[str] = None
    ccnumber2: Optional[str] = None
    ccnumber3: Optional[str] = None
    ccnumber4: Optional[str] = None
    ccnumber5: Optional[str] = None
    ccnumber6: Optional[str] = None
    ccnumber7: Optional[str] = None
    ccnumber8: Optional[str] = None
    cc1: Optional[str] = None
    cc2: Optional[str] = None
    cc3: Optional[str] = None
    cc4: Optional[str] = None
    cc5: Optional[str] = None
    cc6: Optional[str] = None
    cc7: Optional[str] = None
    cc8: Optional[str] = None
    cctrigger1: Optional[str] = None
    cctrigger2: Optional[str] = None
    cctrigger3: Optional[str] = None
    cctrigger4: Optional[str] = None
    cctrigger5: Optional[str] = None
    cctrigger6: Optional[str] = None
    cctrigger7: Optional[str] = None
    cctrigger8: Optional[str] = None
    updateccs: Optional[str] = None
    delayinitialccs: Optional[str] = None
    bank: Optional[str] = None
    program: Optional[str] = None
    programchange: Optional[str] = None
    start: Optional[str] = None
    stop: Optional[str] = None
    running: Optional[str] = None
    systemreset: Optional[str] = None
    allnotesoff: Optional[str] = None
    allsoundoff: Optional[str] = None
    damper: Optional[str] = None
    portamento: Optional[str] = None
    sostenuto: Optional[str] = None
    soft: Optional[str] = None
    legato: Optional[str] = None
    clock: Optional[str] = None
    midiclock: Optional[str] = None
    activesensing: Optional[str] = None
    updaterate: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None


@dataclass
class Midithrough:
    """Circuit midithrough.
      Forward MIDI events from input to one or more outputs

    Inputs:
        fromtrs: integer
            Selects a TRS port to use as input (3.5 mm jack).
            fromtrs = 0 disables TRS, fromtrs = 10
            enables auto detection. See the manual of midiin for details on port
            selection.

        fromusb: integer
            Selects a USB port to use as input.
            fromusb = 0 disables USB, fromusb = 10
            enables auto detection. See the manual of midiin for details on port
            selection.

        totrs: integer
            Selects which TRS MIDI port to output to. See the manual of midiout
            for details on port selection.

        tousb: integer
            Selects which USB MIDI port to output to. See the manual of midiout
            for details on port selection.


    Outputs:

    """


    fromtrs: Optional[str] = None
    fromusb: Optional[str] = None
    totrs: Optional[str] = None
    tousb: Optional[str] = None


@dataclass
class Minifonion:
    """Circuit minifonion.
      Musical quantizer

    Inputs:
        input: voltperoctave
            Patch the unquantized input voltage here

        trigger: trigger
            This jack is optional. If you patch it, the Minifonion will
            work in triggered mode. Here the output pitch is always frozen until the
            next trigger happens.

        bypass: gate
            If you set this gate input to 1 then quantization is bypassed
            and the input voltage is directly copied to the output.

        root: integer
            Set the root note here. 0 means C, 1 means
            C♯, 2 means D and so on. If you multiply
            the value of an input like I1 with 120, then you can use a 1V/Oct
            input for selecting the root note via a sequencer, MIDI keyboard
            or the like.
            Also then you are compatible with the ROOT CV input of the Sinfonion.

             0C
            1C♯
            2D
            3D♯
            4E
            5F
            6F♯
            7G
            8G♯
            9A
            10A♯
            11B
            12C




        degree: integer
            Set the musical scale. This is a number from 0 to 107.
            Below are the first 12 and most important scales. You find a list
            of all 108 scales on page 105.

             0lyd – Lydian major scale (it has a ♯ 4)
            1maj – Normal major scale (ionian)
            2X^7 – Mixolydian (dominant seven chords)
            3sus – mixolydian with 3/4 swapped
            4alt – Altered scale
            5hm^5 – Harmonic minor scale from the 5
            6dor – Dorian minor (minor with ♯ 13)
            7min – Natural minor (aeolian)
            8hm – Harmonic minor (♭ 6 but ♯ 7)
            9phr – Phrygian minor scale (with ♭ 9)
            10dim – Diminished scale (whole/half tone)
            11aug – Augmented scale (just whole tones)


            Note: Alltogether there are 108 scales. Please see page 105 for a complete list

        select1: gate
            Gate input for selecting the root note as being an
            allowed interval. When you want to create a playing interface
            for live operation you can patch the output of a toggle button
            (made with the circuit [button]) here.

            Note: When all select and selectfill inputs are 0,
            automatically all seven scale notes are selected, i.e.
            select1 ... select13 will be set to one.

        select3: gate
            Gate input for selecting the 3.

        select5: gate
            Gate input for selecting the 5.

        select7: gate
            Gate input for selecting the 7.

        select9: gate
            Gate input for selecting the 9 (which is the same
            as the 2).

        select11: gate
            Gate input for selecting the 11 (which is the same
            as the 4).

        select13: gate
            Gate input for selecting the 13 (which is the same
            as the 6).

        selectfill1: gate
            Selects the alternative 9 (i.e.
            the 9 that is not in the scale.

        selectfill2: gate
            Selects the alternative 3 (i.e.
            the 3 that is not in the scale).

        selectfill3: gate
            Selects the alternative 4 or 5. In
            most cases this is the diminished 5.

        selectfill4: gate
            Selects the alternative 13 (i.e.
            the 13 that is not in the scale).

        selectfill5: gate
            Selects the alternative 7 (i.e.
            the 7 that is not in the scale).

        harmonicshift: integer
            This input can reduce harmonic complexity by disabling some of
            the scale or non-scale notes. It is an idea first found in the
            Sinfonion and also provided by the circuit sinfonionlink.

            harmonicshift is staged after the select... inputs
            and further filters out (disables) notes based on their relation
            to the current scale. This means that first the 12 select... inputs
            select a subset of the 12 possible notes. After that harmonicshift
            can reduce this set further (it will never add notes).

            If harmonicshift is not zero, depending on its value some or
            more of the scale notes are disabled, even if they would be allowed by
            select....  Or in other words: the harmonic material is reduced.

            You also can use negative values. These create rather strange sounds
            by removing the simple chord functions instead of the complex
            ones first.

            Here are the possible values:

             0off – all selected notes are allowed
            1disable all fill notes (non-scale notes)
            2disable fills and 11
            3disable fills, 11 and 13
            4disable fills, 11, 13 and 9
            5disable fills, 11, 13, 9 and 7
            6disable fills, 11, 13, 9, 7 and 3
            7disable fills, 11, 13, 9, 7, 3 and 5
            -1disable the root note
            -2disable the root note and the 5
            -3disable root, 3, 5
            -4disable root, 3, 5, 7
            -5disable root, 3, 5, 7, 9
            -6disable root, 3, 5, 7, 9 and 13
            -7disable all scale notes (fill notes untouched)




        noteshift: integer
            Shifts the resulting output note(s) by this
            number of scale notes up or down (if negative). So the output
            note still is part of the scale but may be a note that is none
            of the selected ones. The maximum shift range is limited to
            -24 … +24.

        selectnoteshift: integer
            Shifts the output note by this
            number of selected scale notes up or down (if negative).
            If you use noteshift at the same time, first selectnoteshift is applied, then noteshift. The maximum shift range
            is limited to -24 … +24.

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            This value is being added to the output pitch when not
            in tuning mode. It can be used for musical transposition
            or adding a vibrato.


    Outputs:
        output: voltperoctave
            Here comes your quantized output voltage

        notechange: trigger
            Whenever the quantization changes to a new note a trigger
            with the duration 10 ms is output here. No trigger is
            output in bypass mode.

    """


    input: Optional[str] = None
    trigger: Optional[str] = None
    bypass: Optional[str] = None
    root: Optional[str] = None
    degree: Optional[str] = None
    select1: Optional[str] = None
    select3: Optional[str] = None
    select5: Optional[str] = None
    select7: Optional[str] = None
    select9: Optional[str] = None
    select11: Optional[str] = None
    select13: Optional[str] = None
    selectfill1: Optional[str] = None
    selectfill2: Optional[str] = None
    selectfill3: Optional[str] = None
    selectfill4: Optional[str] = None
    selectfill5: Optional[str] = None
    harmonicshift: Optional[str] = None
    noteshift: Optional[str] = None
    selectnoteshift: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    output: Optional[str] = None
    notechange: Optional[str] = None


@dataclass
class Mixer:
    """Circuit mixer.
      CV mixer

    Inputs:
        input1: cv
            1 ... 8 mixing input

        input2: cv
            1 ... 8 mixing input

        input3: cv
            1 ... 8 mixing input

        input4: cv
            1 ... 8 mixing input

        input5: cv
            1 ... 8 mixing input

        input6: cv
            1 ... 8 mixing input

        input7: cv
            1 ... 8 mixing input

        input8: cv
            1 ... 8 mixing input


    Outputs:
        output: cv
            Sum of all patched inputs

        maximum: cv
            Maximum of all patched inputs of this circuit. This can e.g. be used for mixing together the
            envelopes from several sequencer tracks without making them “louder”
            or distorting them when two sequencers play a note at the same time.

        minimum: cv
            Minimum of all patched inputs of this circuit.

        average: cv
            Average of all patched inputs of this circuit.

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    output: Optional[str] = None
    maximum: Optional[str] = None
    minimum: Optional[str] = None
    average: Optional[str] = None


@dataclass
class Motoquencer:
    """Circuit motoquencer.
      Motor fader sequencer

    Inputs:
        firstfader: integer
            First M4 fader of the sequencer (starting with 1). If you
            omit this, it starts at the first fader of your first M4.

        numfaders: integer
            Number of faders to use for your sequencer. The typical
            numbers are 4, 8, 16 and 32. 32 is the maximum (eight
            M4 units). If you omit this, all of your M4 faders
            will be used.

        numsteps: integer
            Number of steps your sequence consists of (at maximum).
            The number of steps can be greater than the number of faders.
            In that case use page for paging your faders so that
            you can edit all of the steps. Having the number of steps
            less than the faders, makes no sense – it's just a waste
            of faders. The maximum number of steps is 32.

            If you don't set this parameter, the number of steps
            will be set to the number of faders.

            Note: changing this setting dynamically can provoke various
            surprising behaviours. For example the number of pages
            (see parameter page) might be reduced. Or the end
            marker is forcibly moved around. If you want to change the
            length of the sequence via CV, better use endstep
            or autoreset.

            Another note: Setting numsteps will not restrict
            the number of faders. If you set numsteps = 4 but have
            eight faders available, the circuit will use all these,
            even if faders 5, 6, 7 and 8 will be useless. You need to
            set numfaders = 4 in this situation.

        page: integer
            Use this parameter, if you have less faders than steps.
            The first page is 0, not 1.
            For example if you have 4 faders but 16 steps, you can
            select between the four “pages” of four faders each, by
            settings bar to 0, 1, 2 or 3.
            The output of a buttongroup with one button
            per page is a good match for this parameter.

        clock: trigger
            Patch an input clock here. If you want to use ratcheting,
            that clock needs to be stable and regular, because the sequencer
            needs to interpolate the clock and create evenly distributed
            new beats within two clock ticks. If you don't use ratching,
            you can use any rhythm you like here – may it be shuffled,
            euklidean, the output from another sequencer or whatever you
            like. Each clock tick will advance the sequence to the next
            step (or to the next repition of the current step).

        taptempo: trigger
            If your clock is not steady but might be stopped and restarted,
            you should patch a steady clock here. This avoids problems
            with the computation of the gate length right after starting
            the clock. The tap tempo computation needs a series of at least
            two clock pulses so the gate length of the first step is wrong
            after the clock has stopped for a while.

        reset: trigger
            A trigger here resets the sequencer to its start step. The
            next clock tick (or a tick that is roughly at the same time as
            the reset) will play step 1. Note: If there is a reset without
            a clock tick at the same time, the sequencer will go to “step 0”,
            which is a special state where it waits for the clock to advance
            to the first step. Without that fancy logic, a reset plus clock
            would skip step 1 and start with step 2.

        run: gate
            If you set this input to 0, the sequencer will ignore all
            incoming clock ticks. It stops. The default of 1 is normal
            operation, where it runs. This input is a better way to temporarily
            stop the sequencer than to stop the clock. The reason: for computing
            the gate length and ratchets a steady input clock is needed. If
            you stop the clock, the next gate length and ratches right after
            the next start will have the wrong duration since at least two
            clock ticks are neccessary for computing its speed.

            Note: This input is not a replacement for mute, since a
            muted sequencer leaves the clock running and advances steps.
            It just mutes the gate output.

        composemode: gate
            Enabling “compose mode” makes it easier to find the right note in
            a step, when creating more complex melodies.  When composemode
            is set to 1, the sequencer stops clocking. Instead – every
            time you change the CV of a step, it immediately jumps to that step,
            outputs the changed CV and opens the gate for a short time, so you
            can listen to the changed note.

        mute: gate
            If you set this to 1, the gate output of the sequencer
            is muted (will always be 0). Any changes of the CV output still
            happen.

        cvbase: cv
            Here you set the voltage the sequencer will output if the
            CV fader is at the bottom position. The allowed range is -1
            … 1 (which is the same as the range from -10 V to +10 V,
            if you output the CV directly to an output).

        cvrange: cv
            CV range of the faders. So the resulting CV lies somewhere
            between cvbase and cvbase + cvrange. The CV
            range cannot be negative and is capped at 1. If you need a greater
            range, consider multiplying the output value of the cv
            output of the sequencer.

        invert: gate
            Inverts the CV or pitch output. This is like mirroring the fader
            position. Now if the fader is up, the output is low and vice versa.
            In scale quantized mode, the melody still stays within the scale.

        quantize: integer
            Switches on quantization in two levels. At 0, the faders run
            freely and output a continous CV.

            At 1, the output is quantized to semitones, which is 1/12V
            steps. Also the faders will get artifical notches – one for each
            semitone.  That is, unless your range is too large. The maximum number
            of notches with force feedback is 25, so if your range exceeds two
            octaves (0.2), the notches are turned off.

            At 2, the output is quantized to the scale that root and degree
            define. Furthermore the individual scale notes can be switched on or
            off with the parameters select1, select3
            and so on. Note: the root input does not select the lowest
            note of the CV range. That is still set with cvbase. It is
            just used for selecting the scale.

            0no quantization
            1quantize to semitones (1/12V steps)
            2quantize to the scale set by root and degree



        cvnotches: integer
            Usually the CVs of the steps are ment to be note pitches
            (when quantize is 1 or 2), or just free CVs (quantize = 0).
            There is an alternative mode, however, that allows you to
            assign integer values like 0, 1, 2 and so on to each step.

            To do this set cvnotches to a value of 2 or greater. This
            defines the number of discrete values (and hence notches) for
            each step and put CVs of the sequence into notched mode.
            1 makes no sense, of course, since in this “pitch
            bend mode” the faders would always return to the neutral position.

            In notched mode the cv output does not output a pitch but
            a notch number starting from 0. cvbase, cvrange and
            quantize are ignored.

            The maximum number of notches is 127, but the haptic force
            feedback of the motor faders is disabled starting at 26.

        shiftsteps: integer
            Shifts all your steps by that number to the left (negative
            numbers shift to the right). So if shiftsteps is 1, right
            after a reset, the sequencer will not play step 1, but step 2.
            The shifting wraps around at the end of your sequence, so if
            you have 24 steps and shift is 1, the sequencer will play step 1
            instead of step 24.

            Note: Other things like startstep, endstep, playmode,
            from and autoreset take place after shifting.

        startstep: integer
            Sets the first step to be used.  This means that after a reset or
            when the sequencer comes to the end of the sequence, it will begin
            at this step.

            There is also a way for settings start and end with buttons
            (see below at buttonmode). If you use the interactive
            mode, the startstep and endstep settings will be
            overridden. The are reactived if you clear everything.

            Note: startstep and endstep take place after applying
            shiftsteps.

        endstep: integer
            Sets the last of the steps to be played. The default is to play
            all steps. After playing the end step, the sequencer moves on to
            the start step at the next clock tick.

            If startstep is equal to endstep, the sequence
            just consists of one single step.

            Settings startstep larger then endstep is allowed
            and reverses the playing order.

        form: integer
            This is an advanced feature that allows you to slice your
            steps into two or three parts and create musical song forms
            like AAAB or ABAC. Each of the parts A, B or C are then played
            according to the playmode.

            The form AAAB, for example, creates a 32 step form from
            just 16 steps, by playing the first 8 steps three times and
            then the second 8 steps once.

            The following forms are available:

            0A (forms are basically deactivated)
            1AAAB
            2AABB
            3ABAC
            4AAABAAAC
            5AB
            6AAB


            Notes:


              * The splitting of the steps into parts takes place
            after accounting for startstep and endstep.

              * Forms with A, B and C split the pattern into
            three parts. These parts can only be of equal size if the
            number of steps is dividable by 3, of course.

              * The pattern AB is really not the same as A, e.g when
            direction is set 1 (reverse). In that case each of the
            parts is played backwards, but the parts themselves move
            forwards on your steps.


        direction: gate
            Sets the general direction in which the sequencer moves through
            the steps. 0 means forwards and 1 means backwards.

        pingpong: gate
            If set to 1, the sequencer will change the direction every time
            it reaches the start or end of the sequence.

        pattern: integer
            Selects one of a list of movement patterns. That way, the sequence
            steps are not played in linear order but in a more sophisticated
            movement.  Available pattern are:

             0go step by step to the sequence (normal)→
            1two steps forward, one step backward→ → ←
            2double step forward, one step backward⇒ ←
            3double step forward, double step backward, single step forward⇒ ⇐  →
            4double step forward, single step forward, double step backward, single step forward⇒ → ⇐ →
            5random single step forward or backward↔
            6go forward by a small random number of steps→ × ? 
            7random jump to any allowed (other) note⇕




        repeatshift: integer
            This is a number in the range -24 … +24. If you set this
            to non-zero, each repetition of a step shifts the played note
            by that many notes within the selected scale notes. This only
            has effect on steps where the number of repeats is greater than 1.
            Also it is only is applied when the quantize = 2.

        ratchetshift: integer
            This is a number in the range -24 … +24. If you set this
            to non-zero, each ratchet of a step shifts the played note
            by that many notes within the selected scale notes. This only
            has effect on steps where the number of ratchets is greater than 1.
            Also it is only is applied when the quantize = 2.

            If you combine ratchetshift with repeatshift, both
            shifts are added together. And the ratchet shifting is reset
            for each repetition of the step.

        accumulatorrange: integer
            Using this parameter enables the pitch accumulator. The value sets
            the maximum value the accumulator can get.  The maximum is 16. If
            you set this to 0, the fader mode for pitch randomization still
            is in the special mode where the upper four positions control the
            impact of the accumulator.

            Please consult the manual of motoquencer for details on
            the pitch accumulator.

        autoreset: integer
            If set to non-zero, automatically issues a reset (just like a
            trigger to reset) every N clock ticks.

        metricsaver: gate
            The Metric Saver ™ helps you to reliably come back
            to your original metric and time after playing around with all
            sorts of parameters that change the played number of steps in
            the sequence.  These are: startstep, endstep (also when
            changed interactively), form, direction, pingpong, pattern, autoreset and repeats and skips of individual steps.
            Therefore it counts the actual number of clock cycles since the
            last external reset (or system start). And when all of these
            features are deactivated, it snaps back the clock to the position
            it would have been by now if you never had played around with
            all the funny stuff.

            That way, during a live performance, you can safely play around
            with all this polymetric and otherwise time disrupting stuff and
            as soon as you clean up your mess – voila: you are back on track
            and in sync with the rest of the “band”.

            The metric saver is turned on by default. But you can disable
            it by setting the parameter to 0.

        fadermode: integer
            Switches the current meaning of the motor faders. You probably
            want to connect the output of a buttongroup here.
            Here are the possible modes:

            0pitch / CV
            1randomize CV
            2gate propability
            3repeats (up to 16)
            4gate pattern
            5ratchets (up to 8)
            6gate
            7skip


        buttonmode: integer
            Switches the current meaning of the touch buttons below the faders.
            You probably want to connect the output of a buttongroup
            here. Here are the possible modes:

            0gates
            1start / end
            2gate pattern
            3skip


        holdcv: gate
            This setting determines wether the CV output changes every
            time the sequencer moves to the next step or just when that
            step is active (a gate is being played). The latter is the
            default. But if you set this to 0, the CV values of
            steps without gates will also influence the output CV.

            Note: regardless of this setting, the CV will never change
            inbetween. Any change of the CV faders, the cvbase
            and cvrange and so on will only take effect when the
            next step is played. This also ensures that repeats or ratchets
            are always in the same pitch.

        defaultcv: cv
            Set the CV the steps should be set to on a trigger to
            clear. That value must be within the range set by cvbase
            and cvrange, or it will be truncated to that range.

            If you have set cvnotches, however, the value is expected
            to be an integer in the range 0 ... cvnotches - 1.

        defaultgate: gate
            Here you set to which state (on / off) the gates should be
            set on a trigger to clear.

        clearskips: trigger
            A trigger here removes the “skip” setting from all steps.

        clearrepeats: trigger
            A trigger here resets the number of repeats to 1 for each step.

        clearstartend: trigger
            A trigger here clears the manual settings of the start and
            end step. So the sequence will be played in its full length
            (again) .

        gatelength: cv
            The gate length in input clock cycles. A value of 0.5
            thus means half a clock cycle. A steady input clock is needed for
            this to work. Please note that if the gate length is >= 1.0,
            two succeeding notes will get a steady gate, which
            essentially means legato.

            If you don't use a steady clock, set this parameter to 0. This
            will output a minimal gate length of about 10 ms (basically just
            a trigger).

        keyboardmode: integer
            This input sets how a keyboard, that is hooked to keyboardcv,
            and keyboardgate should be used for directly playing notes.
            You can set it to 0, 1 or 2.

             0ignore the keyboard inputs
            1keyboard and sequencer play together, keyboard has precedence
            2mute sequencer, just play keyboard




        keyboardcv: voltperoctave

            The pitch input of a keyboard. This is used for playing
            along with the keyboardmode or recording with recordmode.

        keyboardgate: gate

            The gate input of a keyboard. A positive gate enabled play
            along (see keyboardmode) and also recording, if recordmode is set accordingly.

        recordmode: integer

            Use this input to record melodies played with a keyboard
            (namely keyboardcv and keyboardgate) into the
            sequencer. There are three possible settings:

             0don't record
            1record, notes longer than one step will automatically tie steps via the gate pattern
            2record, don't tie notes. Ignore the length of the input note




        recordsilence: gate
            When this input is set to 1 while recording, silence will
            be recorded while keyboardgate is off. Otherwise you can
            just add notes to the sequence.

        copy: trigger
            A trigger here copies the current page of the sequence to
            an internal clipboard. The clipboard is not part of any preset and
            is also not saved to the SD card. It can be used later for pasting
            it's data to another preset or another page of a sequence.

        paste: trigger
            A trigger here copies the steps from the clipboard to the
            current page.

        pastefaders: trigger
            This is like paste, but just the values of the faders
            of the current fadermode are copied.

        pastebuttons: trigger
            This is like paste, but just the values of the faders
            of the current buttonmode are copied. Note: the button
            mode “start / end” is not supported by copy and paste.

        linktonext: gate
            This settings allows you to create motoquencer tracks that
            have more than one CV or gate output for each step. If you
            set this to 1, the next motoquencer circuit
            in your patch will by synchronized to this one. This means
            that it always plays the same step number – including all
            fancy operating like shiftsteps, startstep,
            endstep, form, pattern and autoreset.
            All those inputs and also clock and reset
            are ignored by the next motoquencer.

            The same holds for the “repeats” and “skip” setting of the steps.

            fadermode and buttonmode are extended to
            the next motoquencers by adding 10 for each motoquencer to
            follow. So fadermode = 10 will show the CV of next motoquencer
            in the faders. fadermode = 11 the CV randomization of the
            next motoquencer. fadermode = 20 show the CV of the
            third linked motoquencer and so on.

            Don't set fadermode or buttonmode on the linked
            motoquencers. They will be ignored there.

            Note: The linktonext setting cannot by dynamically
            changed. It needs to be fixed 0 or 1. You cannot
            use any button or internal cable or other methods to change
            it while the patch is running.

        luckychance: fraction
            Sets tha chance for a step to be affected by the next
            “lucky” operation (see triggers below).

        luckyscope: integer
            Determines which part of the sequence is affected by
            the “lucky” operations. Depending on this setting the
            following steps are affected:

             0All steps between the current start and end step
            1All steps
            2All steps between start and end on the current page
            3All steps on the current page




        luckyamount: fraction
            Sets the amount of change that a “lucky” operation does to
            a step. The meaning depends on the operation. See the parameters
            below.

        luckycvbase: fraction
            This parameter affects only the operation luckycvs and
            luckyfaders when the fader mode is set to 0.
            It adds a fixed amount of CV to the random result, so that
            lies in the range luckycvbase … (luckycvbase + luckyamount).

        luckyfaders: trigger
            Moves the currently selected faders (according to
            fadermode) to new random positions. luckyamount
            sets the maximum value of the fader, where 1 allows the
            maximum.

        luckybuttons: trigger
            Randomly toggles the currently selected buttons (according
            to buttonmode). luckyamount
            only has an effect when the gate patterns are selected, since
            here, four different values are possible. luckamount
            restricts them if it is lower than 1.

        luckycvs: trigger
            Replaces the affected steps' CVs with a new random CVs. The
            lowest possible CV is cvbase. If luckyamount is 1,
            the highest possible CV is cvbase + cvrange, otherwise
            it is cvbase + luckyamount × cvrange.

        luckycvdrift: trigger
            Modifies the affected steps' CV randomly up or down. They will stay
            in the CV range set by cvbase and cvrange. luckyamount
            controls the amount of change.

        luckyspread: trigger
            First computes the average CV of all steps. Then changes
            the CV values of the affected steps such that their distance to
            the average increases or decreases.  If luckyamount
            is greater than 0.5, the distance is increased. Otherwise it
            is decreased.

        luckyinvert: trigger
            Inverts the CVs of the affected steps within the allowed CV
            range. luckyamount has no influence.

        luckyrandomizecv: trigger
            Sets the “randomize CV” values of the affected steps to
            random values (yes, this is double randomization). The luckyamount
            sets the maximum randomization value that will be set.

        luckygates: trigger
            Sets the gates of the affected steps randomly to on or off. The
            chance for on is determined by luckyamount. So with
            luckyamount = 0 you clear all gates and with luckyamount = 1
            you set all gates.

        luckyskips: trigger
            Sets the “skip this step” setting of the affected steps
            randomly to skip or normal. The chance for skip is determined by luckyamount.

        luckyties: trigger
            Sets the “tie this step to the next” setting of the affected steps
            randomly to tie or normal. This is the same as setting the gate pattern
            to the upper most position. The chance for tie is determined by luckyamount.

        luckygatepattern: trigger
            Randomizes the gate pattern of the selected steps (there are four
            different values: once, all, hold and tie). Use luckyamount
            to reduce that set.

        luckygateprob: trigger
            Sets the “randomize gate” values of the affected steps to
            random values (yes, this is double randomization). The luckyamount
            sets the minimum randomization value that will be set (yes, this
            is inverted). So with luckyamount = 1 you disable randomization
            and make the gates play always. With luckymount = 0 you set
            the gate propability to the lowest possible value (still not 0).

        luckyrepeats: trigger
            Randomly sets the number of repeats of the affected steps to
            something between 1 and 16 (the maximum). The luckyamount determines
            the maximum repetition number, where 1 stands for a maximum of 16
            repetitions.

        luckyratchets: trigger
            Randomly sets the number of ratches of the affected steps to
            something between 1 and 8 (the maximum). The luckyamount determines
            the maximum ratchet number, where 1 stands for a maximum of 8
            ratchets.

        luckyshuffle: trigger
            Randomly swaps all affected affected steps (their playing
            order) together will all their attributes. luckyamount has no
            influence.

        buttoncolor: cv
            Set a user defined color for the gate buttons. This
            color is only used when buttonmode = 0. The main purpose
            of this option is to allow a separate color for the gate
            button in a linked sequencer, that does something else than
            gates.

        luckyreverse: trigger
            Reverses the playin gorder of the affected steps. luckyamount
            has not influence.

        root: integer
            Set the root note here. 0 means C, 1 means
            C♯, 2 means D and so on. If you multiply
            the value of an input like I1 with 120, then you can use a 1V/Oct
            input for selecting the root note via a sequencer, MIDI keyboard
            or the like.
            Also then you are compatible with the ROOT CV input of the Sinfonion.

             0C
            1C♯
            2D
            3D♯
            4E
            5F
            6F♯
            7G
            8G♯
            9A
            10A♯
            11B
            12C




        degree: integer
            Set the musical scale. This is a number from 0 to 107.
            Below are the first 12 and most important scales. You find a list
            of all 108 scales on page 105.

             0lyd – Lydian major scale (it has a ♯ 4)
            1maj – Normal major scale (ionian)
            2X^7 – Mixolydian (dominant seven chords)
            3sus – mixolydian with 3/4 swapped
            4alt – Altered scale
            5hm^5 – Harmonic minor scale from the 5
            6dor – Dorian minor (minor with ♯ 13)
            7min – Natural minor (aeolian)
            8hm – Harmonic minor (♭ 6 but ♯ 7)
            9phr – Phrygian minor scale (with ♭ 9)
            10dim – Diminished scale (whole/half tone)
            11aug – Augmented scale (just whole tones)


            Note: Alltogether there are 108 scales. Please see page 105 for a complete list

        select1: gate
            Gate input for selecting the root note as being an
            allowed interval. When you want to create a playing interface
            for live operation you can patch the output of a toggle button
            (made with the circuit [button]) here.

            Note: When all select and selectfill inputs are 0,
            automatically all seven scale notes are selected, i.e.
            select1 ... select13 will be set to one.

        select3: gate
            Gate input for selecting the 3.

        select5: gate
            Gate input for selecting the 5.

        select7: gate
            Gate input for selecting the 7.

        select9: gate
            Gate input for selecting the 9 (which is the same
            as the 2).

        select11: gate
            Gate input for selecting the 11 (which is the same
            as the 4).

        select13: gate
            Gate input for selecting the 13 (which is the same
            as the 6).

        selectfill1: gate
            Selects the alternative 9 (i.e.
            the 9 that is not in the scale.

        selectfill2: gate
            Selects the alternative 3 (i.e.
            the 3 that is not in the scale).

        selectfill3: gate
            Selects the alternative 4 or 5. In
            most cases this is the diminished 5.

        selectfill4: gate
            Selects the alternative 13 (i.e.
            the 13 that is not in the scale).

        selectfill5: gate
            Selects the alternative 7 (i.e.
            the 7 that is not in the scale).

        harmonicshift: integer
            This input can reduce harmonic complexity by disabling some of
            the scale or non-scale notes. It is an idea first found in the
            Sinfonion and also provided by the circuit sinfonionlink.

            harmonicshift is staged after the select... inputs
            and further filters out (disables) notes based on their relation
            to the current scale. This means that first the 12 select... inputs
            select a subset of the 12 possible notes. After that harmonicshift
            can reduce this set further (it will never add notes).

            If harmonicshift is not zero, depending on its value some or
            more of the scale notes are disabled, even if they would be allowed by
            select....  Or in other words: the harmonic material is reduced.

            You also can use negative values. These create rather strange sounds
            by removing the simple chord functions instead of the complex
            ones first.

            Here are the possible values:

             0off – all selected notes are allowed
            1disable all fill notes (non-scale notes)
            2disable fills and 11
            3disable fills, 11 and 13
            4disable fills, 11, 13 and 9
            5disable fills, 11, 13, 9 and 7
            6disable fills, 11, 13, 9, 7 and 3
            7disable fills, 11, 13, 9, 7, 3 and 5
            -1disable the root note
            -2disable the root note and the 5
            -3disable root, 3, 5
            -4disable root, 3, 5, 7
            -5disable root, 3, 5, 7, 9
            -6disable root, 3, 5, 7, 9 and 13
            -7disable all scale notes (fill notes untouched)




        noteshift: integer
            Shifts the resulting output note(s) by this
            number of scale notes up or down (if negative). So the output
            note still is part of the scale but may be a note that is none
            of the selected ones. The maximum shift range is limited to
            -24 … +24.

        selectnoteshift: integer
            Shifts the output note by this
            number of selected scale notes up or down (if negative).
            If you use noteshift at the same time, first selectnoteshift is applied, then noteshift. The maximum shift range
            is limited to -24 … +24.

        tuningmode: gate
            While this is 1, the circuit will output the value set
            by tuningpitch instead of the actual pitch. This is ment
            to be a help for tuning your VCOs.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        transpose: voltperoctave
            This value is being added to the output pitch when not
            in tuning mode. It can be used for musical transposition
            or adding a vibrato.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        cv: cv
            The CV output (or pitch output, if you use quantize).

        gate: gate
            The gate output.

        startofsequence: trigger
            Outputs a trigger whenever the sequencer starts playing
            from the beginning. This can be used for synchronizing with other sequencers.
            An external reset will also cause this output to trigger.

        startofpart: trigger
            Outputs a trigger whenever a form part starts again.
            This is only interesting when you use form.

        startstepout: integer
            Outputs the current start step. This is useful in case it has
            been interactively set with the buttons and you need that information
            for another circuit.

        endstepout: integer
            Outputs the current end step. This is useful in case it has
            been interactively set with the buttons and you need that information
            for another circuit.

        currentstep: integer
            Outputs the number of the step that is currently being played
            (starting from 0).

        currentpage: integer
            Outputs the number of the fader page that is currently played,
            i.e. the value you would have to feed into page in order to
            see the currently being played step.

        accumulator: integer
            The current value of the pitch accumulator (an integer number
            in the range 0 … 16.

    """


    firstfader: Optional[str] = None
    numfaders: Optional[str] = None
    numsteps: Optional[str] = None
    page: Optional[str] = None
    clock: Optional[str] = None
    taptempo: Optional[str] = None
    reset: Optional[str] = None
    run: Optional[str] = None
    composemode: Optional[str] = None
    mute: Optional[str] = None
    cvbase: Optional[str] = None
    cvrange: Optional[str] = None
    invert: Optional[str] = None
    quantize: Optional[str] = None
    cvnotches: Optional[str] = None
    shiftsteps: Optional[str] = None
    startstep: Optional[str] = None
    endstep: Optional[str] = None
    form: Optional[str] = None
    direction: Optional[str] = None
    pingpong: Optional[str] = None
    pattern: Optional[str] = None
    repeatshift: Optional[str] = None
    ratchetshift: Optional[str] = None
    accumulatorrange: Optional[str] = None
    autoreset: Optional[str] = None
    metricsaver: Optional[str] = None
    fadermode: Optional[str] = None
    buttonmode: Optional[str] = None
    holdcv: Optional[str] = None
    defaultcv: Optional[str] = None
    defaultgate: Optional[str] = None
    clearskips: Optional[str] = None
    clearrepeats: Optional[str] = None
    clearstartend: Optional[str] = None
    gatelength: Optional[str] = None
    keyboardmode: Optional[str] = None
    keyboardcv: Optional[str] = None
    keyboardgate: Optional[str] = None
    recordmode: Optional[str] = None
    recordsilence: Optional[str] = None
    copy: Optional[str] = None
    paste: Optional[str] = None
    pastefaders: Optional[str] = None
    pastebuttons: Optional[str] = None
    linktonext: Optional[str] = None
    luckychance: Optional[str] = None
    luckyscope: Optional[str] = None
    luckyamount: Optional[str] = None
    luckycvbase: Optional[str] = None
    luckyfaders: Optional[str] = None
    luckybuttons: Optional[str] = None
    luckycvs: Optional[str] = None
    luckycvdrift: Optional[str] = None
    luckyspread: Optional[str] = None
    luckyinvert: Optional[str] = None
    luckyrandomizecv: Optional[str] = None
    luckygates: Optional[str] = None
    luckyskips: Optional[str] = None
    luckyties: Optional[str] = None
    luckygatepattern: Optional[str] = None
    luckygateprob: Optional[str] = None
    luckyrepeats: Optional[str] = None
    luckyratchets: Optional[str] = None
    luckyshuffle: Optional[str] = None
    buttoncolor: Optional[str] = None
    luckyreverse: Optional[str] = None
    root: Optional[str] = None
    degree: Optional[str] = None
    select1: Optional[str] = None
    select3: Optional[str] = None
    select5: Optional[str] = None
    select7: Optional[str] = None
    select9: Optional[str] = None
    select11: Optional[str] = None
    select13: Optional[str] = None
    selectfill1: Optional[str] = None
    selectfill2: Optional[str] = None
    selectfill3: Optional[str] = None
    selectfill4: Optional[str] = None
    selectfill5: Optional[str] = None
    harmonicshift: Optional[str] = None
    noteshift: Optional[str] = None
    selectnoteshift: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    transpose: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    cv: Optional[str] = None
    gate: Optional[str] = None
    startofsequence: Optional[str] = None
    startofpart: Optional[str] = None
    startstepout: Optional[str] = None
    endstepout: Optional[str] = None
    currentstep: Optional[str] = None
    currentpage: Optional[str] = None
    accumulator: Optional[str] = None


@dataclass
class Motorfader:
    """Circuit motorfader.
      Create virtual fader in M4 controller

    Inputs:
        fader: integer
            The number of the motor fader to use, starting with 1
            for the first fader in the first M4. 5 selects the first
            fader in the second M4 and so on.

        startvalue: cv
            This sets the value the fader gets when you start this circuit
            this first time or when a trigger to clear happens.

        notches: integer
            Number of artifical notches. 0 disables the notches.
            1 creates a pitch bend wheel. 2 creates a binary
            switch with the output values 0 and 1. Higher
            number create that number of notches. E.g. 8 creates
            eight notches and output will output one of the
            value 0, 1, ... 8. The maximum allowed number
            is 25.

        ledvalue: cv
            When you use this input, it will override the brightness
            of the LED below the fader, but just when this circuit
            is selected.

        ledcolor: cv
            When you use this input, it will set the color of the
            LED below the fader, when the circuit is selected. If the
            LED is off, this setting has now impact.

        sharewithnext: gate
            If set to 1, the output output will not be
            used but the circuit shares it's output with the next
            motorfader circuit.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output: cv
            Output the current value if the virtual motor fader
            (don't use this if you are using sharewithnext).

        button: gate
            This output provides you with the current state of the touch button
            below the fader, but only if the circuit is selected. While you could do this with an extra button circuit, using this
            output is more convenient in some situations. While the circuit is
            not selected, the output is set to 0.

    """


    fader: Optional[str] = None
    startvalue: Optional[str] = None
    notches: Optional[str] = None
    ledvalue: Optional[str] = None
    ledcolor: Optional[str] = None
    sharewithnext: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output: Optional[str] = None
    button: Optional[str] = None


@dataclass
class Multicompare:
    """Circuit multicompare.
      Compare in input with up to eight possible values

    Inputs:
        input: cv
            A value to compare.

        compare1: cv
            Up to eight reference values to compare the input with.

        compare2: cv
            Up to eight reference values to compare the input with.

        compare3: cv
            Up to eight reference values to compare the input with.

        compare4: cv
            Up to eight reference values to compare the input with.

        compare5: cv
            Up to eight reference values to compare the input with.

        compare6: cv
            Up to eight reference values to compare the input with.

        compare7: cv
            Up to eight reference values to compare the input with.

        compare8: cv
            Up to eight reference values to compare the input with.

        ifequal1: cv
            The output values if the according comparison value is found at
            the input.

        ifequal2: cv
            The output values if the according comparison value is found at
            the input.

        ifequal3: cv
            The output values if the according comparison value is found at
            the input.

        ifequal4: cv
            The output values if the according comparison value is found at
            the input.

        ifequal5: cv
            The output values if the according comparison value is found at
            the input.

        ifequal6: cv
            The output values if the according comparison value is found at
            the input.

        ifequal7: cv
            The output values if the according comparison value is found at
            the input.

        ifequal8: cv
            The output values if the according comparison value is found at
            the input.

        else_: cv
            Specifies the output value in case non of comparison values is
            found at the input.


    Outputs:
        output: cv
            The vaue of the matching ifequal or else input.

    """


    input: Optional[str] = None
    compare1: Optional[str] = None
    compare2: Optional[str] = None
    compare3: Optional[str] = None
    compare4: Optional[str] = None
    compare5: Optional[str] = None
    compare6: Optional[str] = None
    compare7: Optional[str] = None
    compare8: Optional[str] = None
    ifequal1: Optional[str] = None
    ifequal2: Optional[str] = None
    ifequal3: Optional[str] = None
    ifequal4: Optional[str] = None
    ifequal5: Optional[str] = None
    ifequal6: Optional[str] = None
    ifequal7: Optional[str] = None
    ifequal8: Optional[str] = None
    else_: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Notchedpot:
    """Circuit notchedpot.
      Helper circuit for pots (OBSOLETE)

    Inputs:
        pot: fraction
            Wire your pot here, e.g. P1.1

        notch: cv
            Optionally set the notch size, if you do not like the default of 0.1.
            The maximum allowed value is 0.5. Greater values will be reduced to that.


    Outputs:
        output: fraction
            Your pot output comes here. It still goes from 0.0 to 1.0.

        bipolar: cv
            Optional output with a range from -1.0 to 1.0, where the center notch
            is at 0.0.

        absbipolar: cv
            A variation of bipolar that always outputs a positive value,
            i.e. the pot will go 1 ... 0.5 ... 0 ... 0.5 ... 1

        lefthalf: cv
            This output allows you to split the pot into two hemispheres. Here
            you get 1.0 ... 0.0 while the pot is in the left half. In the middle
            and right of it you always get 0.

        righthalf: cv
            This is the same but for the right half. It outputs 0 while
            the pot is in the left half and 0.0 ... 1.0 from the middle to the
            fully right position.

        lefthalfinv: cv
            This outputs 1.0 - lefthalf, i.e. the value range
            0.0 ... 1.0 ... 1.0 when the pot moves left → mid
            → right.

        righthalfinv: cv
            This outputs 1.0 - righthalf, i.e. the value range
            1.0 ... 1.0 ... 0.0 when the pot moves left → mid
            → right.

    """


    pot: Optional[str] = None
    notch: Optional[str] = None
    output: Optional[str] = None
    bipolar: Optional[str] = None
    absbipolar: Optional[str] = None
    lefthalf: Optional[str] = None
    righthalf: Optional[str] = None
    lefthalfinv: Optional[str] = None
    righthalfinv: Optional[str] = None


@dataclass
class Notebuttons:
    """Circuit notebuttons.
      Note Selection Buttons

    Inputs:
        button1: trigger
            Wire 12 buttons to these 12 inputs.

        button2: trigger
            Wire 12 buttons to these 12 inputs.

        button3: trigger
            Wire 12 buttons to these 12 inputs.

        button4: trigger
            Wire 12 buttons to these 12 inputs.

        button5: trigger
            Wire 12 buttons to these 12 inputs.

        button6: trigger
            Wire 12 buttons to these 12 inputs.

        button7: trigger
            Wire 12 buttons to these 12 inputs.

        button8: trigger
            Wire 12 buttons to these 12 inputs.

        button9: trigger
            Wire 12 buttons to these 12 inputs.

        button10: trigger
            Wire 12 buttons to these 12 inputs.

        button11: trigger
            Wire 12 buttons to these 12 inputs.

        button12: trigger
            Wire 12 buttons to these 12 inputs.

        clock: trigger
            When you use this jack, all button presses are quantized in
            time to the next clock pulse arriving here. That makes it easier
            to switch the note exactly in time.

        startnote: integer
            Specify the note that should be selected when the Droid
            starts and no state is loaded, or when a trigger to clear
            or clearall happened.
            This is an integer number from 0 to 11.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        led1: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led2: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led3: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led4: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led5: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led6: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led7: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led8: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led9: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led10: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led11: gate
            Wire the LEDs in the buttons to these 12 outputs.

        led12: gate
            Wire the LEDs in the buttons to these 12 outputs.

        output: integer
            Here you get a number from 0 to 11, according to the currently
            selected button.

        semitone: voltperoctave
            Here you get the same as output, but divided by 120. When
            you patch this output to a CV output of the , like O1,
            it will output the note as a semitone on a 1 V per octave scheme.

        gate: gate
            This output is 1 as long as one of the buttons is held.
            You can use that together with the semitone output to use
            the notebuttons as a CV/gate keyboard with 12 keys.

    """


    button1: Optional[str] = None
    button2: Optional[str] = None
    button3: Optional[str] = None
    button4: Optional[str] = None
    button5: Optional[str] = None
    button6: Optional[str] = None
    button7: Optional[str] = None
    button8: Optional[str] = None
    button9: Optional[str] = None
    button10: Optional[str] = None
    button11: Optional[str] = None
    button12: Optional[str] = None
    clock: Optional[str] = None
    startnote: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    led1: Optional[str] = None
    led2: Optional[str] = None
    led3: Optional[str] = None
    led4: Optional[str] = None
    led5: Optional[str] = None
    led6: Optional[str] = None
    led7: Optional[str] = None
    led8: Optional[str] = None
    led9: Optional[str] = None
    led10: Optional[str] = None
    led11: Optional[str] = None
    led12: Optional[str] = None
    output: Optional[str] = None
    semitone: Optional[str] = None
    gate: Optional[str] = None


@dataclass
class Nudge:
    """Circuit nudge.
      Modify a value in steps using two buttons

    Inputs:
        buttonup: trigger
            Button for nudging the value up by one step

        buttondown: trigger
            Button for nudging the value down by one step

        amount: cv
            Amount to modify the value by on each press. This must be a value > 0

        startvalue: cv
            The value this circuit starts with or is being reset to if you use
            the clear input.

        minimum: cv
            The minimum possible value. If you do not wire this,
            the value can go down infinitely.

        maximum: cv
            the maximum possible value. If you do not wire this,
            the value can go up infinitely.

        wrap: gate
            Set this to 1 in order to have the value wrap around
            if the minimum or the maximum has been exceeded. Note: wrap
            does only work if you set minimum and maximum.

        offset: cv
            This value is being added to the output.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        ledup: stepped
            Wire this to the LED in the button for nuding up. It will indicate the current value.

        leddown: stepped
            Wire this to the LED in the button for nuding down. It will indicate the current value.

        output: cv
            The output of the current value plus value if offset.

    """


    buttonup: Optional[str] = None
    buttondown: Optional[str] = None
    amount: Optional[str] = None
    startvalue: Optional[str] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    wrap: Optional[str] = None
    offset: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    ledup: Optional[str] = None
    leddown: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Octave:
    """Circuit octave.
      Multi-VCO octave animator

    Inputs:
        input: voltperoctave
            The general pitch information on a 1 V / octave base to be used
            for the three VCOs.

        spread: stepped
            The amount of octave spread between output1 and output3.
            At a value of 1.0 the spread is four octaves.

        detune: fraction
            The amount of linear detune of VCO 2 and 3. This is not
            on a 1 V / octave base but corresponds to an absolute frequency
            difference in Hertz. The exact frequency difference cannot be
            set here, since that depends on how you have tuned your VCOs.
            But the rule is the following: If input is a 0 V and detune is 1.0,
            the detune is by four semitones. And for
            an input of 1 V (one octave higher) it is just two semitones,
            because that results in the same frequency difference. For
            2 V (two octaves up) it ist just one semitone and for 3 V
            half a semitone (and so on). Best thing is to simply try out
            and listen!

        fifths: gate
            Set this to 1 or on if you want to include
            perfect fifths as intermediate steps.


    Outputs:
        output1: voltperoctave
            Outputs for the 1 V / octave of the three VCOs. output1
            is an exact copy of input so you could omit that and rather patch
            VCO 1 to the original pitch CV.

        output2: voltperoctave
            Outputs for the 1 V / octave of the three VCOs. output1
            is an exact copy of input so you could omit that and rather patch
            VCO 1 to the original pitch CV.

        output3: voltperoctave
            Outputs for the 1 V / octave of the three VCOs. output1
            is an exact copy of input so you could omit that and rather patch
            VCO 1 to the original pitch CV.

    """


    input: Optional[str] = None
    spread: Optional[str] = None
    detune: Optional[str] = None
    fifths: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None


@dataclass
class Once:
    """Circuit once.
      Output one trigger after the Droid has started

    Inputs:
        delay: cv
            Set a delay in seconds after the Droid's start before the trigger
            triggers. Note: the default value is 10 ms, not zero. This allows
            all attached controllers to have sent at least one update before
            and the real pot values etc. are available at the circuits.

        onlycoldstart: gate
            If you set this input to 1, once just sends a trigger after
            a cold start, only. A cold start means that the Droid has been powered
            up. Pressing the button for loading a new patch and does a warm
            start.


    Outputs:
        trigger: trigger
            The trigger is output here.

    """


    delay: Optional[str] = None
    onlycoldstart: Optional[str] = None
    trigger: Optional[str] = None


@dataclass
class Outputcalibrator:
    """Circuit outputcalibrator.
      Tune the calibration of your CV outputs

    Inputs:
        output: integer
            Select the output to calibrate. This is a number from
            1 to 8.

        referencepoint: integer
            For each output, two voltages need to be adjusted: 0 V
            and 5 V. Select either 0 for 0 V or 1 for 5 V.

        nudgeup: trigger
            Increase the currently selected output voltage by one minimal
            step, to match the reference voltage.

        nudgedown: trigger
            Decrease the currently selected output voltage by one minimal
            step, to match the reference voltage.

        save: trigger
            A trigger here saves the changed calibration values to
            the internal flash of the master and the the SD card.

        cancel: trigger
            A trigger here restores the previous calibration values from the
            internal flash.

        loaddefaults: trigger
            A trigger here loads the default calibration values, which are
            not very precise, but a good starting point if you got totally lost.


    Outputs:
        dirty: gate
            Outputs 1 if the current calibration has been changed and
            needs to be saved.

        calibration: cv
            Shows the difference between the current calibration of the
            selected output and reference voltage and its default calibration
            value.

        uncalibrated: fraction
            Shows you the percentage of uncalibrated outputs. If
            all eight outputs are calibrated (differ from the default
            calibration value) this outputs 0.

    """


    output: Optional[str] = None
    referencepoint: Optional[str] = None
    nudgeup: Optional[str] = None
    nudgedown: Optional[str] = None
    save: Optional[str] = None
    cancel: Optional[str] = None
    loaddefaults: Optional[str] = None
    dirty: Optional[str] = None
    calibration: Optional[str] = None
    uncalibrated: Optional[str] = None


@dataclass
class Polytool:
    """Circuit polytool.
      Change number of voices in polyphonic setups

    Inputs:
        pitchinput1: any
            The pitches of up to 16 input voices.

        pitchinput2: any
            The pitches of up to 16 input voices.

        pitchinput3: any
            The pitches of up to 16 input voices.

        pitchinput4: any
            The pitches of up to 16 input voices.

        pitchinput5: any
            The pitches of up to 16 input voices.

        pitchinput6: any
            The pitches of up to 16 input voices.

        pitchinput7: any
            The pitches of up to 16 input voices.

        pitchinput8: any
            The pitches of up to 16 input voices.

        pitchinput9: any
            The pitches of up to 16 input voices.

        pitchinput10: any
            The pitches of up to 16 input voices.

        pitchinput11: any
            The pitches of up to 16 input voices.

        pitchinput12: any
            The pitches of up to 16 input voices.

        pitchinput13: any
            The pitches of up to 16 input voices.

        pitchinput14: any
            The pitches of up to 16 input voices.

        pitchinput15: any
            The pitches of up to 16 input voices.

        pitchinput16: any
            The pitches of up to 16 input voices.

        gateinput1: gate
            The gates of up to 16 input voices.

        gateinput2: gate
            The gates of up to 16 input voices.

        gateinput3: gate
            The gates of up to 16 input voices.

        gateinput4: gate
            The gates of up to 16 input voices.

        gateinput5: gate
            The gates of up to 16 input voices.

        gateinput6: gate
            The gates of up to 16 input voices.

        gateinput7: gate
            The gates of up to 16 input voices.

        gateinput8: gate
            The gates of up to 16 input voices.

        gateinput9: gate
            The gates of up to 16 input voices.

        gateinput10: gate
            The gates of up to 16 input voices.

        gateinput11: gate
            The gates of up to 16 input voices.

        gateinput12: gate
            The gates of up to 16 input voices.

        gateinput13: gate
            The gates of up to 16 input voices.

        gateinput14: gate
            The gates of up to 16 input voices.

        gateinput15: gate
            The gates of up to 16 input voices.

        gateinput16: gate
            The gates of up to 16 input voices.

        roundrobin: gate
            Normally when looking for a free output for playing the
            next note, this circuit will start from pitchoutput1
            in its search. This way, if there are not more notes than outputs
            at any time, the notes played first will always be played
            at the lowest numbered outputs. This leads to a deterministic
            behaviour when it comes to playing things like chords. The
            same voice will always be used for the first note in the stream
            of MIDI events.

            When you switch roundrobin to 1, this changes.
            Now the outputs are scanned in a round-robin
            fashion, like in a rotating switch. That way every output has
            the same chance to get a new note. Here it can even make sense
            to define multiple voices even if the track is
            monophonic. When you use envelopes with longer release times,
            you can transform such a melody into chords with simultaneous
            notes.

            Note: When all outputs are currently used by a note, roundrobin
            has no influence. Here voiceallocation selects which of the
            notes will be dropped.

        voiceallocation: integer
            When from the pitch inputs, at any given time, more voice are active
            than you have outputs assigned, normally the “oldest” notes
            would be cancelled. This behaviour can be configured here by
            setting voiceallocation to one of the following values:

             0The oldest note will be cancelled (default)
            1The new note will not be played and simply be omitted
            2The lowest note will be cancelled
            3The highest note will be cancelled





    Outputs:
        pitchoutput1: any
            The pitches of up to 16 output voices.

        pitchoutput2: any
            The pitches of up to 16 output voices.

        pitchoutput3: any
            The pitches of up to 16 output voices.

        pitchoutput4: any
            The pitches of up to 16 output voices.

        pitchoutput5: any
            The pitches of up to 16 output voices.

        pitchoutput6: any
            The pitches of up to 16 output voices.

        pitchoutput7: any
            The pitches of up to 16 output voices.

        pitchoutput8: any
            The pitches of up to 16 output voices.

        pitchoutput9: any
            The pitches of up to 16 output voices.

        pitchoutput10: any
            The pitches of up to 16 output voices.

        pitchoutput11: any
            The pitches of up to 16 output voices.

        pitchoutput12: any
            The pitches of up to 16 output voices.

        pitchoutput13: any
            The pitches of up to 16 output voices.

        pitchoutput14: any
            The pitches of up to 16 output voices.

        pitchoutput15: any
            The pitches of up to 16 output voices.

        pitchoutput16: any
            The pitches of up to 16 output voices.

        gateoutput1: gate
            The gates of up to 16 output voices.

        gateoutput2: gate
            The gates of up to 16 output voices.

        gateoutput3: gate
            The gates of up to 16 output voices.

        gateoutput4: gate
            The gates of up to 16 output voices.

        gateoutput5: gate
            The gates of up to 16 output voices.

        gateoutput6: gate
            The gates of up to 16 output voices.

        gateoutput7: gate
            The gates of up to 16 output voices.

        gateoutput8: gate
            The gates of up to 16 output voices.

        gateoutput9: gate
            The gates of up to 16 output voices.

        gateoutput10: gate
            The gates of up to 16 output voices.

        gateoutput11: gate
            The gates of up to 16 output voices.

        gateoutput12: gate
            The gates of up to 16 output voices.

        gateoutput13: gate
            The gates of up to 16 output voices.

        gateoutput14: gate
            The gates of up to 16 output voices.

        gateoutput15: gate
            The gates of up to 16 output voices.

        gateoutput16: gate
            The gates of up to 16 output voices.

    """


    pitchinput1: Optional[str] = None
    pitchinput2: Optional[str] = None
    pitchinput3: Optional[str] = None
    pitchinput4: Optional[str] = None
    pitchinput5: Optional[str] = None
    pitchinput6: Optional[str] = None
    pitchinput7: Optional[str] = None
    pitchinput8: Optional[str] = None
    pitchinput9: Optional[str] = None
    pitchinput10: Optional[str] = None
    pitchinput11: Optional[str] = None
    pitchinput12: Optional[str] = None
    pitchinput13: Optional[str] = None
    pitchinput14: Optional[str] = None
    pitchinput15: Optional[str] = None
    pitchinput16: Optional[str] = None
    gateinput1: Optional[str] = None
    gateinput2: Optional[str] = None
    gateinput3: Optional[str] = None
    gateinput4: Optional[str] = None
    gateinput5: Optional[str] = None
    gateinput6: Optional[str] = None
    gateinput7: Optional[str] = None
    gateinput8: Optional[str] = None
    gateinput9: Optional[str] = None
    gateinput10: Optional[str] = None
    gateinput11: Optional[str] = None
    gateinput12: Optional[str] = None
    gateinput13: Optional[str] = None
    gateinput14: Optional[str] = None
    gateinput15: Optional[str] = None
    gateinput16: Optional[str] = None
    roundrobin: Optional[str] = None
    voiceallocation: Optional[str] = None
    pitchoutput1: Optional[str] = None
    pitchoutput2: Optional[str] = None
    pitchoutput3: Optional[str] = None
    pitchoutput4: Optional[str] = None
    pitchoutput5: Optional[str] = None
    pitchoutput6: Optional[str] = None
    pitchoutput7: Optional[str] = None
    pitchoutput8: Optional[str] = None
    pitchoutput9: Optional[str] = None
    pitchoutput10: Optional[str] = None
    pitchoutput11: Optional[str] = None
    pitchoutput12: Optional[str] = None
    pitchoutput13: Optional[str] = None
    pitchoutput14: Optional[str] = None
    pitchoutput15: Optional[str] = None
    pitchoutput16: Optional[str] = None
    gateoutput1: Optional[str] = None
    gateoutput2: Optional[str] = None
    gateoutput3: Optional[str] = None
    gateoutput4: Optional[str] = None
    gateoutput5: Optional[str] = None
    gateoutput6: Optional[str] = None
    gateoutput7: Optional[str] = None
    gateoutput8: Optional[str] = None
    gateoutput9: Optional[str] = None
    gateoutput10: Optional[str] = None
    gateoutput11: Optional[str] = None
    gateoutput12: Optional[str] = None
    gateoutput13: Optional[str] = None
    gateoutput14: Optional[str] = None
    gateoutput15: Optional[str] = None
    gateoutput16: Optional[str] = None


@dataclass
class Pot:
    """Circuit pot.
      Helper circuit for pots

    Inputs:
        pot: fraction
            Wire your pot here, e.g. P1.1

        outputscale: cv
            The final output is multiplied with this value. It's a convenient
            method for scaling up and down the pot range.

        notch: cv
            By setting this parameter to a positive number you create an
            artificial “notch” of that size. We suggest using 0.1 (or
            10%.  The maximum allowed value is 0.5. Greater values
            will be reduced to that.  Note: Using this in combination with outputscale also moves the notching point.  E.g. with outputscale = 2
            the notch will be at 1.0.

        discrete: integer
            Setting this value to 1 or larger switches the pot over
            to select a discrete integer number, rather than a continous
            value. For example discrete = 5 makes the pot output
            one of the exact values 0, 1, 2, 3
            or 4. This is ideal for selecting presets and similar.
            If you enable ledgauge (highly recommended), it shows
            you the value by using the LEDs of the master in an adapted
            way.

            The maximum allowed number is 16.

            When using discrete, the startvalue input is
            interpreted as a discrete number. So for example if you
            have discrete = 5, you can use startvalue = 3
            to set the selected value to the number 3 after a
            trigger to clear.
            A potential outputscale is applied afterwards.

            Notes: The options notch and slope do not work
            in discrete mode. outputscale is still applied, though.
            All outputs other than output are dead
            and output 0.0. discrete = 1 does not really make sense,
            since there is just one value to select from and the output
            will always be 0.0.

        slope: cv
            Changes the resolution of the pot in lower or higher ranges.
            Set slope to 2 or more, if you want small values near 0.0
            to be “zoomed in”. Set slope to 0.5 or 0.3 if you want
            to zoom in value nears 1.0.

        ledgauge: cv
            The “LED gauge” uses the 16 LEDs of the MASTER in order
            to indicate the current value of the pot (not available on the
            MASTER18). This is especially useful for “virtual” pots –
            i.e. those pots that you get when you use select in order to
            layer several different functions onto one pot.  In that situation
            the position of the physical pot can be different than that of the
            virtual one, so the gauge shows you the effective virtual value.

            Furthermore, by illuminating the inner four LEDs, the gauge shows
            when the pot hits exactly 0.5. This can only happen if you
            use the notch parameter. Otherwise its practically impossible
            to hit exactly.

            If you have a MASTER18, the gauge is displayed in the upper 16
            LEDs of your first B32, if you have one.

            The LED gauge is automatically activated if you use select.
            If you don't like the LED gauge, you can turn it
            off with ledgauge = off. Otherwise ledgauge set's the color
            of the indicator in the same way as the R-registers do and at the
            same time enables the gauge even if you don't use select.

            Here are some color examples that you can use for the value of ledgauge:

             0.2cyan
            0.4green
            0.6yellow
            0.73orange
            0.8red
            1.0magenta
            1.1violet
            1.2blue


            The colors repeat over in a kind of wheel at 1.2, so e.g. 1.4
            creates the same color as 0.2.

        startvalue: fraction
            This parameter defines the value your pot will get when there is
            a trigger to clear. This is the value before outputscale
            is applied.

            If you use discrete, the parameter does not expect a fraction but
            a discrete number in the range of the discrete values (0, 1,
            2, etc.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.

        preset: integer
            This is the preset number to save or to load. Note: the first
            preset has the number 0, not 1! For the whole story
            on presets please refer to page 21.

        loadpreset: trigger
            A trigger here loads a preset. As a speciality you can
            use the trigger for selecting a preset at the same time.

        savepreset: trigger
            A trigger here saves a preset.

        clear: trigger
            A trigger here loads the default start state into the circuit.
            The presets are not affected, unless you use direct preset switching
            with the preset input and without triggers. And that case
            the current preset is also cleared.

        clearall: trigger
            A trigger here loads the default start state into the circuit
            and into all of its presets.

        dontsave: gate
            If you set this to 1, the state of the circuit will
            not saved to the SD card and not loaded from the SD card
            when the Droid starts.


    Outputs:
        output: fraction
            Your pot output comes here.

        bipolar: cv
            Optional output with a range from -1.0 to 1.0, where the center notch
            is at 0.0 (or from -outputscale to +outputscale if that is used).

        absbipolar: cv
            A variation of bipolar that always outputs a positive value,
            i.e. the pot will go 1 ... 0.5 ... 0 ... 0.5 ... 1 (if outputscale
            is not used).

        lefthalf: cv
            This output allows you to split the pot into two hemispheres. Here
            you get outputscale ... 0.0 while the pot is in the left half. In the middle
            and right of it you always get 0.

        righthalf: cv
            This is the same but for the right half. It outputs 0 while
            the pot is in the left half and 0.0 ... outputscale from the middle to the
            fully right position.

        lefthalfinv: cv
            This outputs 1.0 - lefthalf, i.e. the value range
            0.0 ... 1.0 ... 1.0 when the pot moves left → mid
            → right (and the scaled by outputscale).

        righthalfinv: cv
            This outputs 1.0 - righthalf, i.e. the value range
            1.0 ... 1.0 ... 0.0 when the pot moves left → mid
            → right (and the scaled by outputscale).

        onchange: trigger
            This output emits a trigger whenever the pot is turned in
            either direction.

    """


    pot: Optional[str] = None
    outputscale: Optional[str] = None
    notch: Optional[str] = None
    discrete: Optional[str] = None
    slope: Optional[str] = None
    ledgauge: Optional[str] = None
    startvalue: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    preset: Optional[str] = None
    loadpreset: Optional[str] = None
    savepreset: Optional[str] = None
    clear: Optional[str] = None
    clearall: Optional[str] = None
    dontsave: Optional[str] = None
    output: Optional[str] = None
    bipolar: Optional[str] = None
    absbipolar: Optional[str] = None
    lefthalf: Optional[str] = None
    righthalf: Optional[str] = None
    lefthalfinv: Optional[str] = None
    righthalfinv: Optional[str] = None
    onchange: Optional[str] = None


@dataclass
class Quantizer:
    """Circuit quantizer.
      Non-musical quantizer

    Inputs:
        input: cv
            Patch the unquantized input voltage here

        trigger: trigger
            This jack is optional. If you patch it, the quantizer will
            work in triggered mode. Here the output pitch is always frozen until the
            next trigger happens.

        steps: integer
            Number of steps that one Volt should be divided in. The default
            is 12 and will quantize the input voltage to semitones.
            The number of steps is related to a value of 1 V which means 0.1.
            It is allowed to use a fractional number here. E.g. the value
            1.2 will quantize to 12 steps per 10 V (which means 12 steps
            per 1.0, which can make sense. A value of 0 (or lower)
            will basically mean an infinite number of steps and thus
            practically disable quantization.

        bypass: gate
            If you set this gate input to 1 then quantization is bypassed
            and the input voltage is directly copied to the output.

        direction: integer
            This parameter selects which value is chosen if the input value
            lies between two allowed quantized values (which is almost always
            the case). The default is to choose the nearest value.

            0quantized down
            1quantize to nearest allowed value
            2quantize up



    Outputs:
        output: stepped
            Here comes your quantized output voltage

        changed: trigger
            Whenever the quantization changes to a new output value a trigger
            with the duration 10 ms is output here. No trigger is output in bypass
            mode.

    """


    input: Optional[str] = None
    trigger: Optional[str] = None
    steps: Optional[str] = None
    bypass: Optional[str] = None
    direction: Optional[str] = None
    output: Optional[str] = None
    changed: Optional[str] = None


@dataclass
class Queue:
    """Circuit queue.
      Clocked CV shift register

    Inputs:
        input: cv
            This CV will be pushed into the first cell of the shift register
            whenever a clock occurs.

        clock: trigger
            Each clock signal at this jack will move the CV content
            from every cell of the shift register to the next cell. The CV
            in the last cell will be dropped.

        outputpos1: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos2: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos3: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos4: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos5: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos6: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos7: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.

        outputpos8: integer
            Specifies the position of each of the eight outputs – i.e. which
            cell of the shift register it should output. Allowed are values
            from 1 up to 64. These jacks defaults to 1, 2, ... 8, so
            if you do not wire them the eight outputs reflect the first eight
            positions of the shift register.


    Outputs:
        output1: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output2: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output3: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output4: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output5: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output6: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output7: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

        output8: cv
            Eight outputs for eight different positions of the register. If
            you do not wire outputpos1 ... outputpos8, these outputs
            show the content of the 1, 2, ... 8 cell.

    """


    input: Optional[str] = None
    clock: Optional[str] = None
    outputpos1: Optional[str] = None
    outputpos2: Optional[str] = None
    outputpos3: Optional[str] = None
    outputpos4: Optional[str] = None
    outputpos5: Optional[str] = None
    outputpos6: Optional[str] = None
    outputpos7: Optional[str] = None
    outputpos8: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None


@dataclass
class Random:
    """Circuit random.
      Random number generator

    Inputs:
        clock: trigger
            Optional triggger: if this input is used then the output holds
            the current random number until the next clock impulse (sample & hold)

        minimum: cv
            Minimum possible random number

        maximum: cv
            Maximum possible random number

        steps: integer
            Number of different voltage levels. If this is set to 0 (default),
            any voltage can appear, there is no limit. If this is 1, then there is no
            random any more since there is only one allowed step (which is the average
            between minimum and maximum. At 2 the only two possible
            output values are minimum and maximum. At 3 the possible
            levels are minimum, minimum +  maximum/2
            and maximum and so on...


    Outputs:
        output: cv
            Output of the random number / voltage

    """


    clock: Optional[str] = None
    minimum: Optional[str] = None
    maximum: Optional[str] = None
    steps: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Recorder:
    """Circuit recorder.
      Record and playback CVs und gates

    Inputs:
        playbutton: trigger
            A trigger here starts or restarts the playback.

        recordbutton: trigger
            A trigger here starts or stops the recording.

        stopbutton: trigger
            A trigger here stops and ongoing playback or recording.

        loop: gate
            Set this to 1 to enable loop mode. In loop mode the playback
            is restarted immediately when it's finished.

        pause: gate
            While this is 1, playback or recording is halted (the tape
            stops moving for the while).

        mode: integer
            Using this input is an alternative to using the three button
            inputs. If you patch mode, the three buttons (and LED outputs)
            are ignored. Instead you set the mode with this input:

             0Idle / stopped
            1Playback
            2Recording


            Since you set the mode from “outside”, the recorder cannot switch
            it by itself. So if the mode is set to 1 (playback) and the
            playback is finished, it stays in playback mode and continues outputting
            the last sample.

        playbackspeed: cv
            Sets the speed of the tape during playback. 1 is normal speed,
            0.5 half speed, 2 double speed, and so on. Negative speeds
            are allowed an move the tape backwards. The speed 0 stops the
            tape.

        scrub: gate
            If 1 enables scrubbing. Now the outputs reflect the tape
            position that is set with scrubposition.

        scrubposition: fraction
            Position of the tape to play when scrubbing is enabled.

        trimstart: fraction
            Omits a fraction of the recording at the beginning during
            playback and scrubbing. 0.1 omits the first 10%.

        trimend: fraction
            Omits a fraction of the recording at the end during
            playback and scrubbing. 0.8 omits the last 20% (not
            80%!).

        cvin: cv
            Continous input CV

        numberin: integer
            Discrete input number in the range 0 ... 255

        gatein1: cv
            Input gates

        gatein2: cv
            Input gates

        gatein3: cv
            Input gates

        gatein4: cv
            Input gates

        gatein5: cv
            Input gates

        gatein6: cv
            Input gates

        gatein7: cv
            Input gates

        gatein8: cv
            Input gates

        clock: trigger
            If you use this clock input, all time inputs are measured in
            clock ticks instead of seconds.

        sample: gate
            If you patch this input, “triggered” mode is enabled. In this mode,
            the virtual tape just records a new CV on each trigger at sample.
            So it just records stepped CVs, no slopes and no CV changes
            between the triggers.

        timewindow: cv
            When in triggered mode, this optional parameter helps tackling
            a problem that many hardware sequencers show: often their
            pitch CV is not at its final destination value at the time their
            gate is being output. Often you see a very short “slew” ramp
            of say 5 ms after the gate. During that time the pitch CV moves
            from its former to the new value.

            Now if you trigger the cvtape circuit with the sequencer's
            gate you will essentially sample the previous pitch CV
            instead of the new one. Or maybe something in between.

            The timewindow parameter configures a short time window
            after the trigger to trigger. During that time period the
            tape will constantly adapt the last sample to a changed input
            CV. When that time is over, the input is finally frozen on the tape.

            The timewindow parameter is in seconds. So when you set timewindow to say 0.005 (which means 5 ms), you give the
            input CV 5 ms time for settling to its final value after a trigger
            to sample before freezing it.

        bypass: gate
            Setting bypass to on copies the input signals directly
            to the outputs, regardless of any other stuff going on.

        save: trigger
            Send a trigger here to save the current contents of the
            tape to a file on the SD card. The filename is tapeXXXX.bin,
            where XXXX is replaced by the number set by filenumber.

        load: trigger
            Send a trigger here to load a previously saved file into the
            tape. Use filenumber so specify which file to load.

        filenumber: integer
            Number of the file to load or save. The range is 0 - 9999.
            If filenumber is 123, the name on the SD card is
            tape0123.bin. These files are shared between all
            recorder and delay circuits.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:
        recordled: gate
            Is 1 during recordings.

        playled: gate
            Is 1 during playback or scrubbing.

        stopled: gate
            Is 1 when no playback, recording or scrubbing is going on.

        cvout: cv
            Output of the continous input CV

        numberout: integer
            Output of the discrete number

        gateout1: gate
            Output of the gates

        gateout2: gate
            Output of the gates

        gateout3: gate
            Output of the gates

        gateout4: gate
            Output of the gates

        gateout5: gate
            Output of the gates

        gateout6: gate
            Output of the gates

        gateout7: gate
            Output of the gates

        gateout8: gate
            Output of the gates

        overflow: gate
            When the internal memory of the tape is exceeded and
            data got lost, this gate goes to 1 for 0.5 seconds.
            If you are suspecting this situation, you can wire this
            output to an LED and observe the memory status that way.

    """


    playbutton: Optional[str] = None
    recordbutton: Optional[str] = None
    stopbutton: Optional[str] = None
    loop: Optional[str] = None
    pause: Optional[str] = None
    mode: Optional[str] = None
    playbackspeed: Optional[str] = None
    scrub: Optional[str] = None
    scrubposition: Optional[str] = None
    trimstart: Optional[str] = None
    trimend: Optional[str] = None
    cvin: Optional[str] = None
    numberin: Optional[str] = None
    gatein1: Optional[str] = None
    gatein2: Optional[str] = None
    gatein3: Optional[str] = None
    gatein4: Optional[str] = None
    gatein5: Optional[str] = None
    gatein6: Optional[str] = None
    gatein7: Optional[str] = None
    gatein8: Optional[str] = None
    clock: Optional[str] = None
    sample: Optional[str] = None
    timewindow: Optional[str] = None
    bypass: Optional[str] = None
    save: Optional[str] = None
    load: Optional[str] = None
    filenumber: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    recordled: Optional[str] = None
    playled: Optional[str] = None
    stopled: Optional[str] = None
    cvout: Optional[str] = None
    numberout: Optional[str] = None
    gateout1: Optional[str] = None
    gateout2: Optional[str] = None
    gateout3: Optional[str] = None
    gateout4: Optional[str] = None
    gateout5: Optional[str] = None
    gateout6: Optional[str] = None
    gateout7: Optional[str] = None
    gateout8: Optional[str] = None
    overflow: Optional[str] = None


@dataclass
class Sample:
    """Circuit sample.
      Sample & Hold Circuit

    Inputs:
        input: cv
            Input signal to be sampled

        sample: trigger
            A positive trigger here will read the current value from
            input and store it internally.

        gate: gate
            This is an alternative way of making the circuit take a sample
            from the input. Here it is sampling all the time while the gate
            is high. In that way it is a bit like bypass. But as soon
            as the gate goes low again, the output sticks to the last sample
            value just before that.

        timewindow: cv
            This optional parameter helps tackling a problem that
            many (non-analog) sequencers show: often their pitch CV
            is not at its final destination value at the time their
            gate is being output. Often you see a very short “slew”
            ramp of say 5 ms after the gate. During that time the pitch
            CV moves from its former to the new value.

            Now if you trigger the sample circuit with the sequencer's
            gate you will essentially sample the previous pitch
            CV instead of the new one. Or maybe something in between.

            Now the timewindow parameter introduces a short time window after
            the sample trigger. During that time period the sample & hold
            circuit will constantly adapt to a changed input CV (is essentially
            in bypass mode). When that time is over, the input is finally frozen.

            The timewindow parameter is in seconds. So when you set timewindow to say 0.005 (which means 5 ms), you give the
            input CV 5 ms time for settling to its final value after a trigger
            to sample before freezing it.

        bypass: gate
            While this gate input is high, the circuit is bypassed and
            input is copied to output.


    Outputs:
        output: cv
            The most recently sampled value is sent here.

    """


    input: Optional[str] = None
    sample: Optional[str] = None
    gate: Optional[str] = None
    timewindow: Optional[str] = None
    bypass: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Select:
    """Circuit select.
      Copy a signal if selected

    Inputs:
        input: cv
            Connect the signal you want to copy.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:
        output: cv
            The input will be copied here, but just when the circuit is
            selected via select.

    """


    input: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Sequencer:
    """Circuit sequencer.
      Simple eight step sequencer

    Inputs:
        clock: trigger
            Each trigger into this jack advances the sequence
            by one step.

        reset: trigger
            A trigger here resets the sequence to the first step

        stages: integer
            Number of inputs of pitch.., gate.., slew.., cv and
            repeats that should be used. If you set stages to a number higher
            than the number of used inputs, all inputs will be used.
            If you omit this parameter, all used inputs will be used.

        steps: integer
            With this input you can force the sequencer to begin from start
            after a certain number of clock cycles. If you omit the parameter
            or if it is set to 0, the sequencer will play all stages with all
            repeats until it resets to the beginning.

        transpose: cv
            This voltage is added to the pitch output.

        outputscaling: cv
            The output pitch is multiplied by this parameter.

        gatelength: fraction
            The length of the output gates. If it is unpatched, the original
            input clock is fed through 1:1 (with its own duty cycle). When used, it
            is a ratio from 0.0 to 1.0 and relative to the cycle of the
            input clock. Setting the gatelength to 1.0 merges two adjacent
            gates together since there is not time left for a low gate before
            the next step begins.

        pitch1: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch2: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch3: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch4: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch5: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch6: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch7: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        pitch8: cv
            These are the pitches of the various steps. You can put fixed numbers
            here but also of course pots or variable inputs. Note: The number of
            used input jacks defines the length of the sequence,
            unless you override that with stages.

        cv1: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv2: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv3: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv4: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv5: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv6: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv7: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        cv8: cv
            Each step has an optional CV assigned. You can use that CV for
            modulating something or even outputting a second pitch information.

        gate1: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate2: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate3: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate4: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate5: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate6: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate7: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        gate8: gate
            The gate inputs should be 0 (off) or 1 (on).
            For stages with a 0-gate no output gate is produced and the pitch
            information is kept at the previous state. Unpatched gates are
            considered to be on!

        slew1: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew2: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew3: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew4: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew5: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew6: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew7: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        slew8: cv
            Enables slew limiting for that stage. The input is not binary but
            you can set the amount of slew here – individually for each step.
            0.0 switches the slew off, higher values create slower slews.

        repeat1: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat2: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat3: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat4: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat5: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat6: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat7: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        repeat8: cv
            Set this to a positive integer number like 1, 2, and so on.
            It sets the number of times this stage should be repeated until the
            next stage will be approached.
            It is currently not allowed to have 0 repeats – although this would
            make sense in a future version.

        chaintonext: gate
            If you set this input to 1, the next sequencer circuit's pitch
            and other step inputs will be added to this sequencer. See the general circuit
            notes for details.


    Outputs:
        pitchoutput: cv
            The pitch output. It is unquantized.

        cvoutput: cv
            The optional CV output, in case you use the cv1 ... cv8 inputs.

        gateoutput: gate
            The gate output.

    """


    clock: Optional[str] = None
    reset: Optional[str] = None
    stages: Optional[str] = None
    steps: Optional[str] = None
    transpose: Optional[str] = None
    outputscaling: Optional[str] = None
    gatelength: Optional[str] = None
    pitch1: Optional[str] = None
    pitch2: Optional[str] = None
    pitch3: Optional[str] = None
    pitch4: Optional[str] = None
    pitch5: Optional[str] = None
    pitch6: Optional[str] = None
    pitch7: Optional[str] = None
    pitch8: Optional[str] = None
    cv1: Optional[str] = None
    cv2: Optional[str] = None
    cv3: Optional[str] = None
    cv4: Optional[str] = None
    cv5: Optional[str] = None
    cv6: Optional[str] = None
    cv7: Optional[str] = None
    cv8: Optional[str] = None
    gate1: Optional[str] = None
    gate2: Optional[str] = None
    gate3: Optional[str] = None
    gate4: Optional[str] = None
    gate5: Optional[str] = None
    gate6: Optional[str] = None
    gate7: Optional[str] = None
    gate8: Optional[str] = None
    slew1: Optional[str] = None
    slew2: Optional[str] = None
    slew3: Optional[str] = None
    slew4: Optional[str] = None
    slew5: Optional[str] = None
    slew6: Optional[str] = None
    slew7: Optional[str] = None
    slew8: Optional[str] = None
    repeat1: Optional[str] = None
    repeat2: Optional[str] = None
    repeat3: Optional[str] = None
    repeat4: Optional[str] = None
    repeat5: Optional[str] = None
    repeat6: Optional[str] = None
    repeat7: Optional[str] = None
    repeat8: Optional[str] = None
    chaintonext: Optional[str] = None
    pitchoutput: Optional[str] = None
    cvoutput: Optional[str] = None
    gateoutput: Optional[str] = None


@dataclass
class Sinfonionlink:
    """Circuit sinfonionlink.
      Sync harmonic state from Sinfonion

    Inputs:


    Outputs:
        root: integer
            The current root note as an integer number. C = 0, C♯ =
            1, D = 2 and so on.

        degree: integer
            The current scale (the Sinfonion uses the word degree for this).
            This is an integer number. If find a list of all available
            scales on page 105.

        transpose: voltperoctave
            The current global transposition of the Sinfonion. This
            is in 1V/Oct, so you can add it to your pitch whereever
            you output one.

        chaoticdetune: cv
            The current value of the chaotic detune. You can feed this into
            the detune input of the circuit detune.

        harmonicshift: integer
            Harmonic shift is a feature of the Sinfonion that allows to reduce
            harmonic complexity via CV (or the builtin pots POT1 or POT2). The
            idea is that the more you rise the CV, the less complex scale
            notes are allowed.

            This output gives you access to the current setting of harmonic
            shift of the Sinfonion. It is an integer number between -7 and 7.
            You can directly feed it into the harmonicshift input of
            circuits like minifonion, chord, arpeggio
            or motoquencer. Harmonic shift is explained in detail
            in the manual chapter of minifonion.

        linkstate: gate
            Outputs 1 if the link to the Sinfonion is up and active, otherwise 0.

        clock: trigger
            Gives you a copy of the Sinfonion's clock input

        reset: trigger
            Outputs a trigger whenever in Song mode the Sinfonion forwards
            to the first bar of the song.

        step: trigger
            Outputs a trigger for every step of a song.

        beat: trigger
            Outputs a trigger for every beat (subdivision of a step).

    """


    root: Optional[str] = None
    degree: Optional[str] = None
    transpose: Optional[str] = None
    chaoticdetune: Optional[str] = None
    harmonicshift: Optional[str] = None
    linkstate: Optional[str] = None
    clock: Optional[str] = None
    reset: Optional[str] = None
    step: Optional[str] = None
    beat: Optional[str] = None


@dataclass
class Slew:
    """Circuit slew.
      Slew limiter

    Inputs:
        input: cv
            Wire the CV that you wish to slew limit here.

        slew: cv
            This controls the slew rate. A value of 0.0 disables slew
            limiting. The output immediately follows the input without any
            delay. A value of for example 2.0 in linear mode means that
            2.0 seconds are needed for a change of 1 V (which is a value of
            0.1 or one octave if used as pitch).
            In the other two modes the slew time is tuned to sound similar.
            Negative values of this parameter are treated as 0.0.

        slewup: cv
            This allows a special handling when the voltage moves upwards.
            The slew limiting for upwards is slew multiplied with slewup.
            Since slew defaults to 1.0 you can just use slewup
            and slewdown if you want to control both directions separately.

        slewdown: cv
            Sets the slew rate for downwards movement.

        gate: gate
            If this jack is patched, the slew limiting is only active
            while this gate is high. Otherwise it's like setting the slew
            parameter to zero.


    Outputs:
        exponential: cv
            Output for the resulting CV with the exponential (classical) slew
            algorithm applied

        linear: cv
            Output for linear slew limiting

        scurve: cv
            Output with the slew limitation according to the S-curve algorithm.

    """


    input: Optional[str] = None
    slew: Optional[str] = None
    slewup: Optional[str] = None
    slewdown: Optional[str] = None
    gate: Optional[str] = None
    exponential: Optional[str] = None
    linear: Optional[str] = None
    scurve: Optional[str] = None


@dataclass
class Spring:
    """Circuit spring.
      Physical spring simulation

    Inputs:
        mass: cv
            The mass of the object on the spring. The heavier it is, the farther the spring
            will move up and down.

        gravity: cv
            The gravity of the simulated planet the spring is mounted at. If you
            set the gravity to zero, the mass will move exactly around the zero
            position from positive to negative and back. But you need to shove
            it or set a start position other than 0, in order to get it started.

        springforce: cv
            The force of the string per m it is stretched. In an ideal spring
            the force is proportional to the current elongation.

        flowresistance: cv
            Setting this to a value > 0 will dampen the oscillation in a way,
            that higher velocities will be damped more then slower ones. This means
            that impact of the friction will get less and less as time goes by and
            the movement slows down.

        friction: cv
            Setting this to a value > 0 will also dampen the oscillation, but in
            a way that is independent of the current speed of the mass.

        speed: cv
            This parameter speeds up or slows down the perceived time. It works
            on a 1V/Oct base. Every positive 1V (or 0.1) doubles the speed.
            So if you set speed to 2V or 0.2 it will speed
            up the movement by a factor of 4. An input of -1V will slow down the
            movement to the half.

        shove: gate
            While this gate input is logical 1, an extra force of 1 N is applied to
            the mass pointing downwards. You can change that force with shoveforce.

        shoveforce: cv
            This is the force being applied to the mass while shove is active

        reset: trigger
            Resets the whole system to its start position.

        startvelocity: cv
            Sets the velocity the mass has which starts of a reset is triggered

        startposition: cv
            Sets the position the spring has which starts of a reset is triggered


    Outputs:
        velocity: cv
            Outputs the current velocity of the mass

        position: cv
            Output the current length of the string. If the string goes
            upwards (which is possible with certain modulations), this can
            be negative.

    """


    mass: Optional[str] = None
    gravity: Optional[str] = None
    springforce: Optional[str] = None
    flowresistance: Optional[str] = None
    friction: Optional[str] = None
    speed: Optional[str] = None
    shove: Optional[str] = None
    shoveforce: Optional[str] = None
    reset: Optional[str] = None
    startvelocity: Optional[str] = None
    startposition: Optional[str] = None
    velocity: Optional[str] = None
    position: Optional[str] = None


@dataclass
class Superjust:
    """Circuit superjust.
      Perfect intonation of up to eight voices

    Inputs:
        input1: voltperoctave
            1 ... 8 pitch input

        input2: voltperoctave
            1 ... 8 pitch input

        input3: voltperoctave
            1 ... 8 pitch input

        input4: voltperoctave
            1 ... 8 pitch input

        input5: voltperoctave
            1 ... 8 pitch input

        input6: voltperoctave
            1 ... 8 pitch input

        input7: voltperoctave
            1 ... 8 pitch input

        input8: voltperoctave
            1 ... 8 pitch input

        tuningmode: gate
            While this is 1, all outputs output the value set
            by tuningpitch. This is for tuning all outputs. Since
            perfect tuning is crucial for perfect intonation, this is
            quite useful.

        tuningpitch: voltperoctave
            This pitch CV will be output while the tuning mode
            is active.

        bypass: gate
            While this is 1, all inputs are passed through
            to the outputs without changes.

        transpose: voltperoctave
            This value is being added to all outputs, but not
            in tuning or bypass mode. It can e.g. be used for
            making a vibrato on a chord.


    Outputs:
        output1: voltperoctave
            1 ... 8 pitch output

        output2: voltperoctave
            1 ... 8 pitch output

        output3: voltperoctave
            1 ... 8 pitch output

        output4: voltperoctave
            1 ... 8 pitch output

        output5: voltperoctave
            1 ... 8 pitch output

        output6: voltperoctave
            1 ... 8 pitch output

        output7: voltperoctave
            1 ... 8 pitch output

        output8: voltperoctave
            1 ... 8 pitch output

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    tuningmode: Optional[str] = None
    tuningpitch: Optional[str] = None
    bypass: Optional[str] = None
    transpose: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None


@dataclass
class Switch:
    """Circuit switch.
      Adressable/clockable switch

    Inputs:
        input1: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input2: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input3: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input4: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input5: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input6: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input7: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input8: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input9: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input10: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input11: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input12: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input13: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input14: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input15: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        input16: cv
            1 ... 16 input. Use these inputs in order and don't leave
            gaps.

        forward: trigger
            If a trigger or gate is received here, the switch adds one
            to the current internal switch offset. So every output moves to the
            next input and every input moves to the previous output.

        backward: trigger
            Similar then forward, but switches backwards

        reset: trigger
            Resets the switch to its initial position. Assuming offset is at 0,
            input1 is connected to output1, input2 to output2 etc.

            If reset and a trigger at forward / backward happen at the
            same time (within
            5 ms), the reset will win and the switch is being reset to offset
            0. This avoids problems with unprecise timing of external sequencers.

        offset: integer
            This allows CV addressable switching. The number read here is being used
            a shifting offset and is always added to the internal offset.
            For example if you send 5 here, it is like
            you have triggered forward five times after the last reset. Please
            note, then 5 would mean 50 Volts, not 5 Volts. So if you patch an
            external CV like I1 here, you probably want to multiply with some
            useful number.


    Outputs:
        output1: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output2: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output3: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output4: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output5: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output6: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output7: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output8: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output9: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output10: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output11: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output12: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output13: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output14: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output15: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

        output16: cv
            1 ... 16 output. Use these outputs in order and don't
            leave gaps.

    """


    input1: Optional[str] = None
    input2: Optional[str] = None
    input3: Optional[str] = None
    input4: Optional[str] = None
    input5: Optional[str] = None
    input6: Optional[str] = None
    input7: Optional[str] = None
    input8: Optional[str] = None
    input9: Optional[str] = None
    input10: Optional[str] = None
    input11: Optional[str] = None
    input12: Optional[str] = None
    input13: Optional[str] = None
    input14: Optional[str] = None
    input15: Optional[str] = None
    input16: Optional[str] = None
    forward: Optional[str] = None
    backward: Optional[str] = None
    reset: Optional[str] = None
    offset: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None
    output9: Optional[str] = None
    output10: Optional[str] = None
    output11: Optional[str] = None
    output12: Optional[str] = None
    output13: Optional[str] = None
    output14: Optional[str] = None
    output15: Optional[str] = None
    output16: Optional[str] = None


@dataclass
class Switchedpot:
    """Circuit switchedpot.
      Overlay pot with multiple functions (OBSOLETE)

    Inputs:
        pot: fraction
            The pot that you want to overlay, e.g. P1.1

        bipolar: gate
            If this input is set to 1, the usual pot range of 0 ... 1 will be
            mapped to -1 ... +1, which converts this to a bipolar potentiometer.
            This is done by multiplying the output with 2.0 and substracting
            1.0 afterwards.

        switch1: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch2: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch3: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch4: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch5: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch6: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch7: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).

        switch8: gate
            These inputs select which of the virtual pots should be changed
            when the physical pot is being turned. These should be set to 0
            or 1 (or off and on).


    Outputs:
        output1: fraction
            The output of the up to eight virtual pots.

        output2: fraction
            The output of the up to eight virtual pots.

        output3: fraction
            The output of the up to eight virtual pots.

        output4: fraction
            The output of the up to eight virtual pots.

        output5: fraction
            The output of the up to eight virtual pots.

        output6: fraction
            The output of the up to eight virtual pots.

        output7: fraction
            The output of the up to eight virtual pots.

        output8: fraction
            The output of the up to eight virtual pots.

    """


    pot: Optional[str] = None
    bipolar: Optional[str] = None
    switch1: Optional[str] = None
    switch2: Optional[str] = None
    switch3: Optional[str] = None
    switch4: Optional[str] = None
    switch5: Optional[str] = None
    switch6: Optional[str] = None
    switch7: Optional[str] = None
    switch8: Optional[str] = None
    output1: Optional[str] = None
    output2: Optional[str] = None
    output3: Optional[str] = None
    output4: Optional[str] = None
    output5: Optional[str] = None
    output6: Optional[str] = None
    output7: Optional[str] = None
    output8: Optional[str] = None


@dataclass
class Timing:
    """Circuit timing.
      Shuffle/swing and complex timing generator

    Inputs:
        clock: trigger
            Patch a steady clock here for this circuit to be of any use

        reset: trigger
            A trigger here resets the internal step counter and restart at
            step 1.

        timing1: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing2: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing3: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing4: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing5: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing6: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing7: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.

        timing8: cv
            Specifies a relative timing for each step in relation to the input clock.
            A timing of 0.3 will shift the respective beat 30% of a clock cycle behind,
            while -0.3 will make it 30% early.

            The timing values are clipped into the range -0.9999 …0.9999.


    Outputs:
        output: trigger
            Here comes the modified output clock

    """


    clock: Optional[str] = None
    reset: Optional[str] = None
    timing1: Optional[str] = None
    timing2: Optional[str] = None
    timing3: Optional[str] = None
    timing4: Optional[str] = None
    timing5: Optional[str] = None
    timing6: Optional[str] = None
    timing7: Optional[str] = None
    timing8: Optional[str] = None
    output: Optional[str] = None


@dataclass
class Togglebutton:
    """Circuit togglebutton.
      Create on/off buttons (OBSOLETE)

    Inputs:
        button: trigger
            The actual push button. Usually you want to wire this to B1.1,
            B1.2 and so on: to one of the push buttons of your
            controllers. Each time that
            input goes from low to high the state of the push button will toggle.

        reset: trigger
            A positive trigger edge here will reset the
            button into the state “not pressed” – regardless of
            its current state

        onvalue: cv
            Value sent to output when the push button is on. Setting this to a
            different value than the default value saves you attenuating its value
            later on when you use it as a CV.

        offvalue: cv
            Value sent to output when the push button is off.

        doubleclickmode: gate
            This input can enable a double click mode when set to 1.
            In that mode the button only toggles it's constant state if you double
            press it in a short time. Otherwise it behaves like a momentary button,
            that inverts the persisted state (which you toggle with the double click).

        startvalue: gate
            State of the push button when you switch on your system. Setting this
            to on or off will force the button into that state. Using this
            jack disables the persistence of the state! In switched mode this will
            be used for the other button layers as well.


    Outputs:
        led: gate
            When the button's state is on a value of 1.0 will be sent to that
            output – regardless of the values in onvalue
            and offvalue. Usually you will wire this jack to the
            LED within the button, e.g. to L1.1, L1.2
            and so on

        output: cv
            This jack will output either onvalue or offvalue
            depending on the
            state of the 1 ... 4 button.
            If you have not wired those inputs then this is
            the same as the led output.

        inverted: cv
            The same as output1, but sends onvalue when the
            button is off and offvalue when the button is on.
            Note: there is no inverted version of output2 ... output4.

        negated: gate
            Similar to inverted, but always sends 1 when the button
            is off and 0 when the button is on – independent of the values
            of onvalue and offvalue.

    """


    button: Optional[str] = None
    reset: Optional[str] = None
    onvalue: Optional[str] = None
    offvalue: Optional[str] = None
    doubleclickmode: Optional[str] = None
    startvalue: Optional[str] = None
    led: Optional[str] = None
    output: Optional[str] = None
    inverted: Optional[str] = None
    negated: Optional[str] = None


@dataclass
class Transient:
    """Circuit transient.
      Transient generator

    Inputs:
        start: cv
            Start value of the transient

        end: cv
            Target value of the transient

        duration: cv
            Duration: if the clock input is used, it is in clock ticks.
            Otherwise it is in seconds. A negative duration will be treated as
            zero. And a zero duration will make the output always be at end level.

        loop: gate
            If this is set to 1, the transient will start over
            again as soon as it reaches the end.

        pingpong: gate
            If this set to 1, the transient will start moving
            backwards towards the start when it has reached end. It will swing
            back and forth, in fact looping infinitely.

        freeze: gate
            while this is set to 1, the transient it frozen at its
            current position.

        reset: trigger
            A trigger here will immediately set the transient back to
            its start value.

        clock: trigger
            If you patch a clock here, the duration will be set in terms
            of clock ticks, not of seconds. This needs to be a steady clock
            in order to get predictable results.


    Outputs:
        output: cv
            Here comes the current value of the transient.

        phase: cv
            This output reflects the current phase of the transient. It behaves
            as if start would be 0 and end would be 1.

        endoftransient: gate
            When loop and pingpong is off, this output goes to 1 when
            the transient has reached the end – and stays there.
            In loop mode just a short trigger is sent.
            In pingpong mode that trigger is not sent when the transient has
            reach the end-value, but when it is back at start
            (i.e. after one full cycle).

    """


    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None
    loop: Optional[str] = None
    pingpong: Optional[str] = None
    freeze: Optional[str] = None
    reset: Optional[str] = None
    clock: Optional[str] = None
    output: Optional[str] = None
    phase: Optional[str] = None
    endoftransient: Optional[str] = None


@dataclass
class Triggerdelay:
    """Circuit triggerdelay.
      Trigger Delay with multi tap and optional clocking

    Inputs:
        input: gate
            Patch triggers or gates to be delayed here.

        delay: cv
            Amount of time the incoming triggers are being delayed. When clock is
            patched, this is in relation to one clock cycle, so a delay of
            4 will delay the input pattern by exactly 4 beats. Fractions are
            allowed also. If clock is not patched, this parameter
            is in seconds. So for example in order to delay by 100 ms
            you need a delay of 0.1.

        gatelength: cv
            Unless you patch this jack the length of the output gates is
            exactly the length of the input gates. By use of this parameter you
            override that length and set a fixed length in seconds – or
            if clock is being used – in clock cycles.

        repeats: integer
            Number of times the delayed trigger is being repeated. Each
            further repetition is with the same delay.

        mute: gate
            A high gate signal suppresses any further output gates. However, the current
            gate is finished normally.

        clock: trigger
            When you patch this input, the trigger delay runs in clocked
            mode. In this mode delay is relative to one clock cycle. I.e. a delay
            if 0.5 will delay the trigger by half a clock cycle. The same holds
            for gatelength. That is measured in clock cycles, too.


    Outputs:
        output: gate
            Outputs the delayed triggers/gates, while keeping the gate length –
            unless you have changed that

        overflow: gate
            Whenever there are more input triggers than this circuit can keep
            memory of, this output outputs a gate of 0.5 sec length. You can
            wire this to an LED in order to know when this happens.

    """


    input: Optional[str] = None
    delay: Optional[str] = None
    gatelength: Optional[str] = None
    repeats: Optional[str] = None
    mute: Optional[str] = None
    clock: Optional[str] = None
    output: Optional[str] = None
    overflow: Optional[str] = None


@dataclass
class Unusedfaders:
    """Circuit unusedfaders.
      Declare unused motor faders

    Inputs:
        firstfader: integer
            The number of the first unused motor fader motor.

        numfaders: integer
            The number of unused faders

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:

    """


    firstfader: Optional[str] = None
    numfaders: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None


@dataclass
class Vcotuner:
    """Circuit vcotuner.
      measure frequency and tuning of a VCO

    Inputs:
        tuningnote: integer
            You can either tune to a specific note, like C or A or
            whatever you like. In this case set tuningnote to
            a number from 0 to 11, where 0 is C, 1 is C#, 2 is D and
            so on. Or you set it to -1 (which is the default) to
            tune to the nearest semitone.

        concertpitch: cv
            Set the frequency of the concert pitch here, which is the
            frequency of A1. Most commonly this is 440 Hz, so 440 is the
            default value of this parameter.

        basepitch: voltperoctave
            This output sets the reference for the pitch output.
            It is the voltage for the note C0. With analog synths it is
            common – but not neccessary – that the C notes correspond
            to integer voltage numbers.

        smooth: fraction
            When measuring the input frequency, a slight smoothing
            is applied (like a low pass filter). It evens out some possible
            jitter that you might have. You can adjust this filter here.
            Per default smoothing is just subtle. Beware: smooth = 1
            smoothes strong, so the frequency measurement needs some time
            to get accurate.

        precision: cv
            This parameter defines the precision for the input frequency
            to be in tune. It is set in cents, where 100 cent correspond
            to one semitone. If you set the precision too low, it is very
            hard to tune correctly. If you set it too high, your tuning is
            not very precise.

        select: gate
            The select input allows you to overlay buttons and
            LEDs with
            multiple functions. If you use this input, the circuit will
            process the buttons and LEDs just as if select has a positive
            gate signal (usually you will select this to 1).
            Otherwise it won't touch them so they can be used by
            another circuit. Note: even if the circuit is currently
            not selected, it will nevertheless work and process all its
            other inputs and its  outputs (those that do not deal with
            buttons or LEDs) in a normal way.

        selectat: integer
            This input makes the select input more flexible. Here
            you specify at which value select should select this circuit.
            E.g. if selectat is 0, the circuit will be active if
            select is exactly 0 instead of a positive gate signal.
            In some cases this is more conventient.


    Outputs:
        hz: cv
            Outputs the current input frequency. If you no signal is
            found, the output is 0.

        ledflat: fraction
            Patch this to a LED to show if and how much the input frequency
            is flat (too low). This value ranges from 0.2 to 1.0 if
            the input frequency is flat and goes straight to 0 otherwise.
            If you use select, this output only works while the circuit
            is selected.

        ledsharp: fraction
            Patch this to a LED to show if and how much the input frequency
            is sharp (too high). This value ranges from 0.2 to 1.0 if
            the input frequency is sharp and goes straight to 0 otherwise.
            If you use select, this output only works while the circuit
            is selected.

        ledintune: gate
            Outputs 1 if the input frequency is “in tune”. Here the
            precision input is applied.
            If you use select, this output only works while the circuit
            is selected.

        intune: gate
            Outputs 1 if the input frequency is “in tune”. Here the
            precision input is applied. This output also while while
            the circuit is not selected. You can use it in situations where
            you want to process this information by some other circuit rather
            than just displaying it.

        tuning: bipolar
            Outputs the current tuning deviation of the input measured
            in 1V/octave.

        cents: bipolar
            Outputs the current tuning deviation in cents, where
            100 cents correspond to one semitone.

        pitch: voltperoctave
            Outputs the current pitch of the input frequency in terms
            of 1V/octave. Here the basepitch is applied. You can
            patch this output to the pitch input of a second VCO to have
            that follow the pitch of the measured VCO.

        referencepitch: voltperoctave
            Here you get the pitch of the reference tone the tuner currently
            “locked in” into. It is either the nearest semitone or the
            note selected by tuningnote in the nearest octave.

        vcofound: gate
            This output is 1 whenever a valid input signal
            is found on the tuning input I1.

    """


    tuningnote: Optional[str] = None
    concertpitch: Optional[str] = None
    basepitch: Optional[str] = None
    smooth: Optional[str] = None
    precision: Optional[str] = None
    select: Optional[str] = None
    selectat: Optional[str] = None
    hz: Optional[str] = None
    ledflat: Optional[str] = None
    ledsharp: Optional[str] = None
    ledintune: Optional[str] = None
    intune: Optional[str] = None
    tuning: Optional[str] = None
    cents: Optional[str] = None
    pitch: Optional[str] = None
    referencepitch: Optional[str] = None
    vcofound: Optional[str] = None