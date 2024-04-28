"""DROID circuits. These circuits are auto-generated from circuits.json."""

from dataclasses import dataclass
from typing import Optional

from metapatch.circuits.base import DroidCircuit

@dataclass
class Case(DroidCircuit):
    """Circuit case.

    Switch choosing from inputs via conditions

    Args:
        case1 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case2 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case3 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case4 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case5 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case6 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case7 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case8 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case9 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case10 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case11 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case12 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case13 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case14 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case15 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        case16 (cv):
          1 ... 16 case input. The first one that is non-zero defines which input value
          to use.

        value1 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value2 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value3 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value4 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value5 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value6 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value7 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value8 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value9 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value10 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value11 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value12 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value13 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value14 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value15 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        value16 (cv):
          1 ... 16 value input. One of these is copied to the output, depending on which
          of the case inputs is none-zero.

        else_ (trigger):
          In case none of the case inputs is non-zero, this value is copied to the
          output.

        output (cv):
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
class Crossfader(DroidCircuit):
    """Circuit crossfader.

    Morph between 8 inputs

    Args:
        input1 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input2 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input3 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input4 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input5 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input6 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input7 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        input8 (cv):
          The input signals that you want to crossfade between. At least input1 and
          input2 need to be patched. Otherwise they are treated like 0 V signals.

        fade (fraction):
          This value decides which of the two inputs should be mixed and to which degree
          each one should go into the mix. At 0.0 the mix consists of 100% of the first
          inputs, at 1.0 of 100% of the last patched input.

        output (cv):
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
class Cvlooper(DroidCircuit):
    """Circuit cvlooper.

    Clocked CV looper

    Args:
        cvin (cv):
          Input CV that should be looped.

        gatein (gate):
          Optional input gate. If you do not patch something here, the gate is assumed
          to be always high.

        clock (trigger):
          Input clock. The clock is mandatory and is the base for the definition of the
          loop length. Also the loop switch is quantized in time to the nearest clock.

        reset (trigger):
          A trigger here resets the playback head immediately to the start of the loop,
          if you are in playback mode.

        length (integer):
          Length of the loop in clock ticks. Example: You get a length of 16 ticks by
          patching the number 16 to length. If you want to set the length by means of an
          external CV that would require 160 Volts. So you need to multiply your input
          by some useful number in that case.

        tapespeed (cv):
          Relative tape speed, where 1.0 is the normal speed. So a value of 0.5 slows
          down the speed thus increasing the effective tape length from 8 to 16 seconds
          while reducing the sampling rate from 1 ms to 2 ms per sample. Changing the
          tape speed on the fly probably leads to interesting results.

        loopswitch (gate):
          Mandatory parameter: While the loop switch is off the CV looper simply sends
          all input CV and gate to their respective outputs. At the same time CV and
          gate are also recorded to the tape. When the loop switch is on, the CV and
          gate are being read from the tape, instead. The input CV and gate are now
          ignored.

        pause (gate):
          This is a binary input. If you send a high signal here, the looper pauses.
          This is only works in playback mode. The current CV value is hold the entire
          time. This is not the same as bypass, since in bypass mode the original CV
          will be routed through.

        overlay (gate):
          Overlaying changes the behaviour while looping is active. If overlay is set to
          on, while the input gate is active the gate and CV will be sent directly from
          the inputs rather than read from the tape.

        overdub (gate):
          Overdubbing also changes the behaviour during the looping: If it is active
          then while the input gate is high the input gate and CV will be written to the
          tape – thus changing the loop on the fly.

        bypass (gate):
          Setting bypass to on copies the input CV and gate from their inputs to their
          outputs while keeping the loop's content untouched. This disabled the looping
          for the while, but you can get back to it later. Note: this is different from
          turning off the loop switch, because then your tape's content would be
          overwritten.

        cvout (cv):
          Output of the bypassed or looped CV

        gateout (gate):
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
class Delay(DroidCircuit):
    """Circuit delay.

    A tape delay for CVs, gates and numbers

    Args:
        delay (cv):
          The CVs are delayed by this amount of seconds. If you patch clock as well, the
          delay is specified in clock tick, so then delay = 1 means “delay by one clock
          tick”.

        cvin (cv):
          Continous input CV

        numberin (integer):
          Discrete input number in the range 0 ... 255

        gatein1 (cv):
          Input gates

        gatein2 (cv):
          Input gates

        gatein3 (cv):
          Input gates

        gatein4 (cv):
          Input gates

        gatein5 (cv):
          Input gates

        gatein6 (cv):
          Input gates

        gatein7 (cv):
          Input gates

        gatein8 (cv):
          Input gates

        clock (trigger):
          If you use this clock input, all time inputs are measured in clock ticks
          instead of seconds.

        sample (gate):
          If you patch this input, “triggered” mode is enabled. In this mode, the
          virtual tape just records a new CV on each trigger at sample. So it just
          records stepped CVs, no slopes and no CV changes between the triggers.

        timewindow (cv):
          When in triggered mode, this optional parameter helps tackling a problem that
          many hardware sequencers show: often their pitch CV is not at its final
          destination value at the time their gate is being output. Often you see a very
          short “slew” ramp of say 5 ms after the gate. During that time the pitch CV
          moves from its former to the new value.  Now if you trigger the cvtape circuit
          with the sequencer's gate you will essentially sample the previous pitch CV
          instead of the new one. Or maybe something in between.  The timewindow
          parameter configures a short time window after the trigger to trigger. During
          that time period the tape will constantly adapt the last sample to a changed
          input CV. When that time is over, the input is finally frozen on the tape.
          The timewindow parameter is in seconds. So when you set timewindow to say
          0.005 (which means 5 ms), you give the input CV 5 ms time for settling to its
          final value after a trigger to sample before freezing it.

        bypass (gate):
          Setting bypass to on copies the input signals directly to the outputs,
          regardless of any other stuff going on.

        save (trigger):
          Send a trigger here to save the current contents of the tape to a file on the
          SD card. The filename is tapeXXXX.bin, where XXXX is replaced by the number
          set by filenumber.

        load (trigger):
          Send a trigger here to load a previously saved file into the tape. Use
          filenumber so specify which file to load.

        filenumber (integer):
          Number of the file to load or save. The range is 0 - 9999. If filenumber is
          123, the name on the SD card is tape0123.bin. These files are shared between
          all recorder and delay circuits.

        cvout (cv):
          Output of the continous input CV

        numberout (integer):
          Output of the discrete number

        gateout1 (gate):
          Output of the gates

        gateout2 (gate):
          Output of the gates

        gateout3 (gate):
          Output of the gates

        gateout4 (gate):
          Output of the gates

        gateout5 (gate):
          Output of the gates

        gateout6 (gate):
          Output of the gates

        gateout7 (gate):
          Output of the gates

        gateout8 (gate):
          Output of the gates

        overflow (gate):
          When the internal memory of the tape is exceeded and data got lost, this gate
          goes to 1 for 0.5 seconds. If you are suspecting this situation, you can wire
          this output to an LED and observe the memory status that way.

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
class Matrixmixer(DroidCircuit):
    """Circuit matrixmixer.

    Matrix mixer for CVs

    Args:
        input1 (cv):
          The up to four CV inputs that you want to mix

        input2 (cv):
          The up to four CV inputs that you want to mix

        input3 (cv):
          The up to four CV inputs that you want to mix

        input4 (cv):
          The up to four CV inputs that you want to mix

        auxin1 (cv):
          These auxiliary inputs will be mixed directly into the four outputs output1 …
          output4 and are used for cascading several matrix mixers into one with more
          than four inputs.

        auxin2 (cv):
          These auxiliary inputs will be mixed directly into the four outputs output1 …
          output4 and are used for cascading several matrix mixers into one with more
          than four inputs.

        auxin3 (cv):
          These auxiliary inputs will be mixed directly into the four outputs output1 …
          output4 and are used for cascading several matrix mixers into one with more
          than four inputs.

        auxin4 (cv):
          These auxiliary inputs will be mixed directly into the four outputs output1 …
          output4 and are used for cascading several matrix mixers into one with more
          than four inputs.

        mixmax (fraction):
          If this is 0.0, normal mixing is done (the enabled inputs CVs will be added).
          At a value of 1.0 instead each outputs is the maximum of the enabled inputs.
          Any number in between will create a weighted average between these two values.

        startvalue (integer):
          This input selects in which state the matrix begins life. Also a trigger to
          clear will create that starting state. The following three configurations can
          be selected with startvalue:   0All buttons are cleared. 1The buttons on the
          diagonal are active. 2All buttons are set.   When set to 1, input1 is sent to
          output1, input2 to output2 and so on.

        button11 (gate):
          These four buttons decide, to which of the four outputs input1 is being mixed.

        button12 (gate):
          These four buttons decide, to which of the four outputs input1 is being mixed.

        button13 (gate):
          These four buttons decide, to which of the four outputs input1 is being mixed.

        button14 (gate):
          These four buttons decide, to which of the four outputs input1 is being mixed.

        button21 (gate):
          These four buttons decide, to which of the four outputs input2 is being mixed.

        button22 (gate):
          These four buttons decide, to which of the four outputs input2 is being mixed.

        button23 (gate):
          These four buttons decide, to which of the four outputs input2 is being mixed.

        button24 (gate):
          These four buttons decide, to which of the four outputs input2 is being mixed.

        button31 (gate):
          These four buttons decide, to which of the four outputs input3 is being mixed.

        button32 (gate):
          These four buttons decide, to which of the four outputs input3 is being mixed.

        button33 (gate):
          These four buttons decide, to which of the four outputs input3 is being mixed.

        button34 (gate):
          These four buttons decide, to which of the four outputs input3 is being mixed.

        button41 (gate):
          These four buttons decide, to which of the four outputs input4 is being mixed.

        button42 (gate):
          These four buttons decide, to which of the four outputs input4 is being mixed.

        button43 (gate):
          These four buttons decide, to which of the four outputs input4 is being mixed.

        button44 (gate):
          These four buttons decide, to which of the four outputs input4 is being mixed.

        select (gate):
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
          The four outputs

        output2 (cv):
          The four outputs

        output3 (cv):
          The four outputs

        output4 (cv):
          The four outputs

        led11 (fraction):
          The LEDs in the buttons button11 …button14

        led12 (fraction):
          The LEDs in the buttons button11 …button14

        led13 (fraction):
          The LEDs in the buttons button11 …button14

        led14 (fraction):
          The LEDs in the buttons button11 …button14

        led21 (fraction):
          The LEDs in the buttons button21 …button24

        led22 (fraction):
          The LEDs in the buttons button21 …button24

        led23 (fraction):
          The LEDs in the buttons button21 …button24

        led24 (fraction):
          The LEDs in the buttons button21 …button24

        led31 (fraction):
          The LEDs in the buttons button31 …button34

        led32 (fraction):
          The LEDs in the buttons button31 …button34

        led33 (fraction):
          The LEDs in the buttons button31 …button34

        led34 (fraction):
          The LEDs in the buttons button31 …button34

        led41 (fraction):
          The LEDs in the buttons button41 …button44

        led42 (fraction):
          The LEDs in the buttons button41 …button44

        led43 (fraction):
          The LEDs in the buttons button41 …button44

        led44 (fraction):
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
class Mixer(DroidCircuit):
    """Circuit mixer.

    CV mixer

    Args:
        input1 (cv):
          1 ... 8 mixing input

        input2 (cv):
          1 ... 8 mixing input

        input3 (cv):
          1 ... 8 mixing input

        input4 (cv):
          1 ... 8 mixing input

        input5 (cv):
          1 ... 8 mixing input

        input6 (cv):
          1 ... 8 mixing input

        input7 (cv):
          1 ... 8 mixing input

        input8 (cv):
          1 ... 8 mixing input

        output (cv):
          Sum of all patched inputs

        maximum (cv):
          Maximum of all patched inputs of this circuit. This can e.g. be used for
          mixing together the envelopes from several sequencer tracks without making
          them “louder” or distorting them when two sequencers play a note at the same
          time.

        minimum (cv):
          Minimum of all patched inputs of this circuit.

        average (cv):
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
class Quantizer(DroidCircuit):
    """Circuit quantizer.

    Non-musical quantizer

    Args:
        input (cv):
          Patch the unquantized input voltage here

        trigger (trigger):
          This jack is optional. If you patch it, the quantizer will work in triggered
          mode. Here the output pitch is always frozen until the next trigger happens.

        steps (integer):
          Number of steps that one Volt should be divided in. The default is 12 and will
          quantize the input voltage to semitones. The number of steps is related to a
          value of 1 V which means 0.1. It is allowed to use a fractional number here.
          E.g. the value 1.2 will quantize to 12 steps per 10 V (which means 12 steps
          per 1.0, which can make sense. A value of 0 (or lower) will basically mean an
          infinite number of steps and thus practically disable quantization.

        bypass (gate):
          If you set this gate input to 1 then quantization is bypassed and the input
          voltage is directly copied to the output.

        direction (integer):
          This parameter selects which value is chosen if the input value lies between
          two allowed quantized values (which is almost always the case). The default is
          to choose the nearest value.  0quantized down 1quantize to nearest allowed
          value 2quantize up

        output (stepped):
          Here comes your quantized output voltage

        changed (trigger):
          Whenever the quantization changes to a new output value a trigger with the
          duration 10 ms is output here. No trigger is output in bypass mode.

    """


    input: Optional[str] = None
    trigger: Optional[str] = None
    steps: Optional[str] = None
    bypass: Optional[str] = None
    direction: Optional[str] = None
    output: Optional[str] = None
    changed: Optional[str] = None

@dataclass
class Queue(DroidCircuit):
    """Circuit queue.

    Clocked CV shift register

    Args:
        input (cv):
          This CV will be pushed into the first cell of the shift register whenever a
          clock occurs.

        clock (trigger):
          Each clock signal at this jack will move the CV content from every cell of the
          shift register to the next cell. The CV in the last cell will be dropped.

        outputpos1 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos2 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos3 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos4 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos5 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos6 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos7 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        outputpos8 (integer):
          Specifies the position of each of the eight outputs – i.e. which cell of the
          shift register it should output. Allowed are values from 1 up to 64. These
          jacks defaults to 1, 2, ... 8, so if you do not wire them the eight outputs
          reflect the first eight positions of the shift register.

        output1 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output2 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output3 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output4 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output5 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output6 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output7 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

        output8 (cv):
          Eight outputs for eight different positions of the register. If you do not
          wire outputpos1 ... outputpos8, these outputs show the content of the 1, 2,
          ... 8 cell.

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
class Recorder(DroidCircuit):
    """Circuit recorder.

    Record and playback CVs und gates

    Args:
        playbutton (trigger):
          A trigger here starts or restarts the playback.

        recordbutton (trigger):
          A trigger here starts or stops the recording.

        stopbutton (trigger):
          A trigger here stops and ongoing playback or recording.

        loop (gate):
          Set this to 1 to enable loop mode. In loop mode the playback is restarted
          immediately when it's finished.

        pause (gate):
          While this is 1, playback or recording is halted (the tape stops moving for
          the while).

        mode (integer):
          Using this input is an alternative to using the three button inputs. If you
          patch mode, the three buttons (and LED outputs) are ignored. Instead you set
          the mode with this input:   0Idle / stopped 1Playback 2Recording   Since you
          set the mode from “outside”, the recorder cannot switch it by itself. So if
          the mode is set to 1 (playback) and the playback is finished, it stays in
          playback mode and continues outputting the last sample.

        playbackspeed (cv):
          Sets the speed of the tape during playback. 1 is normal speed, 0.5 half speed,
          2 double speed, and so on. Negative speeds are allowed an move the tape
          backwards. The speed 0 stops the tape.

        scrub (gate):
          If 1 enables scrubbing. Now the outputs reflect the tape position that is set
          with scrubposition.

        scrubposition (fraction):
          Position of the tape to play when scrubbing is enabled.

        trimstart (fraction):
          Omits a fraction of the recording at the beginning during playback and
          scrubbing. 0.1 omits the first 10%.

        trimend (fraction):
          Omits a fraction of the recording at the end during playback and scrubbing.
          0.8 omits the last 20% (not 80%!).

        cvin (cv):
          Continous input CV

        numberin (integer):
          Discrete input number in the range 0 ... 255

        gatein1 (cv):
          Input gates

        gatein2 (cv):
          Input gates

        gatein3 (cv):
          Input gates

        gatein4 (cv):
          Input gates

        gatein5 (cv):
          Input gates

        gatein6 (cv):
          Input gates

        gatein7 (cv):
          Input gates

        gatein8 (cv):
          Input gates

        clock (trigger):
          If you use this clock input, all time inputs are measured in clock ticks
          instead of seconds.

        sample (gate):
          If you patch this input, “triggered” mode is enabled. In this mode, the
          virtual tape just records a new CV on each trigger at sample. So it just
          records stepped CVs, no slopes and no CV changes between the triggers.

        timewindow (cv):
          When in triggered mode, this optional parameter helps tackling a problem that
          many hardware sequencers show: often their pitch CV is not at its final
          destination value at the time their gate is being output. Often you see a very
          short “slew” ramp of say 5 ms after the gate. During that time the pitch CV
          moves from its former to the new value.  Now if you trigger the cvtape circuit
          with the sequencer's gate you will essentially sample the previous pitch CV
          instead of the new one. Or maybe something in between.  The timewindow
          parameter configures a short time window after the trigger to trigger. During
          that time period the tape will constantly adapt the last sample to a changed
          input CV. When that time is over, the input is finally frozen on the tape.
          The timewindow parameter is in seconds. So when you set timewindow to say
          0.005 (which means 5 ms), you give the input CV 5 ms time for settling to its
          final value after a trigger to sample before freezing it.

        bypass (gate):
          Setting bypass to on copies the input signals directly to the outputs,
          regardless of any other stuff going on.

        save (trigger):
          Send a trigger here to save the current contents of the tape to a file on the
          SD card. The filename is tapeXXXX.bin, where XXXX is replaced by the number
          set by filenumber.

        load (trigger):
          Send a trigger here to load a previously saved file into the tape. Use
          filenumber so specify which file to load.

        filenumber (integer):
          Number of the file to load or save. The range is 0 - 9999. If filenumber is
          123, the name on the SD card is tape0123.bin. These files are shared between
          all recorder and delay circuits.

        select (gate):
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

        recordled (gate):
          Is 1 during recordings.

        playled (gate):
          Is 1 during playback or scrubbing.

        stopled (gate):
          Is 1 when no playback, recording or scrubbing is going on.

        cvout (cv):
          Output of the continous input CV

        numberout (integer):
          Output of the discrete number

        gateout1 (gate):
          Output of the gates

        gateout2 (gate):
          Output of the gates

        gateout3 (gate):
          Output of the gates

        gateout4 (gate):
          Output of the gates

        gateout5 (gate):
          Output of the gates

        gateout6 (gate):
          Output of the gates

        gateout7 (gate):
          Output of the gates

        gateout8 (gate):
          Output of the gates

        overflow (gate):
          When the internal memory of the tape is exceeded and data got lost, this gate
          goes to 1 for 0.5 seconds. If you are suspecting this situation, you can wire
          this output to an LED and observe the memory status that way.

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
class Sample(DroidCircuit):
    """Circuit sample.

    Sample & Hold Circuit

    Args:
        input (cv):
          Input signal to be sampled

        sample (trigger):
          A positive trigger here will read the current value from input and store it
          internally.

        gate (gate):
          This is an alternative way of making the circuit take a sample from the input.
          Here it is sampling all the time while the gate is high. In that way it is a
          bit like bypass. But as soon as the gate goes low again, the output sticks to
          the last sample value just before that.

        timewindow (cv):
          This optional parameter helps tackling a problem that many (non-analog)
          sequencers show: often their pitch CV is not at its final destination value at
          the time their gate is being output. Often you see a very short “slew” ramp of
          say 5 ms after the gate. During that time the pitch CV moves from its former
          to the new value.  Now if you trigger the sample circuit with the sequencer's
          gate you will essentially sample the previous pitch CV instead of the new one.
          Or maybe something in between.  Now the timewindow parameter introduces a
          short time window after the sample trigger. During that time period the sample
          & hold circuit will constantly adapt to a changed input CV (is essentially in
          bypass mode). When that time is over, the input is finally frozen.  The
          timewindow parameter is in seconds. So when you set timewindow to say 0.005
          (which means 5 ms), you give the input CV 5 ms time for settling to its final
          value after a trigger to sample before freezing it.

        bypass (gate):
          While this gate input is high, the circuit is bypassed and input is copied to
          output.

        output (cv):
          The most recently sampled value is sent here.

    """


    input: Optional[str] = None
    sample: Optional[str] = None
    gate: Optional[str] = None
    timewindow: Optional[str] = None
    bypass: Optional[str] = None
    output: Optional[str] = None

@dataclass
class Slew(DroidCircuit):
    """Circuit slew.

    Slew limiter

    Args:
        input (cv):
          Wire the CV that you wish to slew limit here.

        slew (cv):
          This controls the slew rate. A value of 0.0 disables slew limiting. The output
          immediately follows the input without any delay. A value of for example 2.0 in
          linear mode means that 2.0 seconds are needed for a change of 1 V (which is a
          value of 0.1 or one octave if used as pitch). In the other two modes the slew
          time is tuned to sound similar. Negative values of this parameter are treated
          as 0.0.

        slewup (cv):
          This allows a special handling when the voltage moves upwards. The slew
          limiting for upwards is slew multiplied with slewup. Since slew defaults to
          1.0 you can just use slewup and slewdown if you want to control both
          directions separately.

        slewdown (cv):
          Sets the slew rate for downwards movement.

        gate (gate):
          If this jack is patched, the slew limiting is only active while this gate is
          high. Otherwise it's like setting the slew parameter to zero.

        exponential (cv):
          Output for the resulting CV with the exponential (classical) slew algorithm
          applied

        linear (cv):
          Output for linear slew limiting

        scurve (cv):
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
class Switch(DroidCircuit):
    """Circuit switch.

    Adressable/clockable switch

    Args:
        input1 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input2 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input3 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input4 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input5 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input6 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input7 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input8 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input9 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input10 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input11 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input12 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input13 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input14 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input15 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        input16 (cv):
          1 ... 16 input. Use these inputs in order and don't leave gaps.

        forward (trigger):
          If a trigger or gate is received here, the switch adds one to the current
          internal switch offset. So every output moves to the next input and every
          input moves to the previous output.

        backward (trigger):
          Similar then forward, but switches backwards

        reset (trigger):
          Resets the switch to its initial position. Assuming offset is at 0, input1 is
          connected to output1, input2 to output2 etc.  If reset and a trigger at
          forward / backward happen at the same time (within 5 ms), the reset will win
          and the switch is being reset to offset 0. This avoids problems with unprecise
          timing of external sequencers.

        offset (integer):
          This allows CV addressable switching. The number read here is being used a
          shifting offset and is always added to the internal offset. For example if you
          send 5 here, it is like you have triggered forward five times after the last
          reset. Please note, then 5 would mean 50 Volts, not 5 Volts. So if you patch
          an external CV like I1 here, you probably want to multiply with some useful
          number.

        output1 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output2 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output3 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output4 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output5 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output6 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output7 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output8 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output9 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output10 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output11 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output12 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output13 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output14 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output15 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

        output16 (cv):
          1 ... 16 output. Use these outputs in order and don't leave gaps.

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
