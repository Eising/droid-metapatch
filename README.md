# Introduction

The DROID metapatch library aims to create an easier and more pythonic way of creating DROID patch generators. DROID patch generators are a recent feature added to the the DROID Forge application that allows you to define python scripts that generate full-fledges patches.

DROID is a series of eurorack controllers and CV processors made by [Der Mann mit der Maschine](https://shop.dermannmitdermaschine.de/).


# Comparison to the bundled `pg.py` script

This library is quite a bit more advanced than the bundled `pg.py` script. It&rsquo;s not meant to be more difficult though, but instead it should remove some of the complicated elements of writing patch generators. For example:

-   It automatically collects the input parameters
-   It ensures that correct output types for Forge to pick up, such as the JSON synopsis out, the parameter types and presets.
-   It has a complete library of all the DROID circuits, so if you have a modern editor, you get auto-completion of DROID circuits, and a context-specific help from the DROID manual.
-   You can convert DROID patches into partial patch generators through a script, so it should be super fast to get started.


# Installation


## Installing the library

Before you can write a patch generator, please install this library to your system python environment. Forge does not support virtual environments, so you must install this library somewhere where your default python library can find it.

This library is available from pypi, use `pip install droid-metapatch` to install it.


## Installation on MacOS

DROID Forge uses the version of python that is bundled with MacOS. If you have installed python via homebrew or any other way, you may have multiple different python versions available.

There are several ways to solve this:


### Install the library with the system Python

To ensure install this library to the one bundled with MacOS, run the following command:

```
$ /usr/bin/python3 -m pip install droid-metapatch
```

Note that this may result in a situation where the Forge has this library available, but your editor or shell does not. In that case, you can run the `pip install droid-metapatch` also. You will then have two copies installed, one for each environment.


### Installing the metapatch library by hand

You could also clone or download this repository, and place the `metapatch` folder into your Generators folder (located in your home directory under the `DROID Patches` folder.)

This should work, but note that the `droid-metapatch` CLI utility will not be available then.


# How to use the metapatch library



## Getting started

The DROID metapatch library is intended to get you started making your own patch generator with as little overhead as possible.

To further make this possible, it comes with a handy command line tool to help you get started really quickly, and convert existing patches into patch generators.

You can also just write one from scratch. It&rsquo;s not very hard once you grasp the concepts.

In this section, we will first try to convert a patch into a patch generator, and then look at some patterns for writing smart scripts.


## Converting a DROID patch into a generator

You can use the `droid-metapatch` script to kickstart a patch generator. From there, you can add parameters, and customize your script to be dynamic.

First we need a DROID patch, so here is a simple patch with an `algoquencer`.

It could look like this:

```
[p4b2]
[b32]

# -------------------------------------------------
# clock
# -------------------------------------------------

[lfo]
    hz = -8 * P1.4 + 8
    square = _CLOCK_UNMUTED

[button]
    button = B1.1
    onvalue = 1
    offvalue = 0
    led = L1.1
    output = _RUNNING

[button]
    button = B1.1
    states = 1
    output = _RESET

[copy]
    input = _CLOCK_UNMUTED * _RUNNING
    output = _CLOCK

# -------------------------------------------------
# Algoquencer
# -------------------------------------------------

[algoquencer]
    clock = _CLOCK
    reset = _RESET
    button1 = B2.1
    button2 = B2.2
    button3 = B2.3
    button4 = B2.4
    button5 = B2.5
    button6 = B2.6
    button7 = B2.7
    button8 = B2.8
    button9 = B2.9
    button10 = B2.10
    button11 = B2.11
    button12 = B2.12
    button13 = B2.13
    button14 = B2.14
    button15 = B2.15
    button16 = B2.16
    activity = P1.1
    pitch = _PITCH_UNQUANTIZED
    gate = G1.1
    mutebutton = B2.25
    lengthbutton = B2.17
    muteled = L2.25
    led1 = L2.1
    led2 = L2.2
    led3 = L2.3
    led4 = L2.4
    led5 = L2.5
    led6 = L2.6
    led7 = L2.7
    led8 = L2.8
    led9 = L2.9
    led10 = L2.10
    led11 = L2.11
    led12 = L2.12
    led13 = L2.13
    led14 = L2.14
    led15 = L2.15
    led16 = L2.16

[minifonion]
    input = _PITCH_UNQUANTIZED
    root = 0
    degree = 7
    select1 = 1
    select3 = 1
    select5 = 1
    select7 = 1
    select9 = 1
    select11 = 1
    select13 = 1
    output = O1
```

If you put this into a file, and run in with `$ droid-metapatch boilerplate <filename>`, the output will look like this:

```python
"""Patch generator auto-generated by the droid-metapatch utility."""
from typing import List
import metapatch

class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Draft Patch Generator"
    description = "A short description"

    def clock(self) -> List[metapatch.DroidCircuit]:
        """Generate contents of section 'clock'."""
        return [
            metapatch.circuits.Lfo(
                hz="-8 * P1.4 + 8",
                square="_CLOCK_UNMUTED",
            ),
            metapatch.circuits.Button(
                button="B1.1",
                onvalue="1",
                offvalue="0",
                led="L1.1",
                output="_RUNNING",
            ),
            metapatch.circuits.Button(
                button="B1.1",
                states="1",
                output="_RESET",
            ),
            metapatch.circuits.Copy(
                input="_CLOCK_UNMUTED * _RUNNING",
                output="_CLOCK",
            ),
        ]


    def algoquencer(self) -> List[metapatch.DroidCircuit]:
        """Generate contents of section 'Algoquencer'."""
        return [
            metapatch.circuits.Algoquencer(
                clock="_CLOCK",
                reset="_RESET",
                button1="B2.1",
                button2="B2.2",
                button3="B2.3",
                button4="B2.4",
                button5="B2.5",
                button6="B2.6",
                button7="B2.7",
                button8="B2.8",
                button9="B2.9",
                button10="B2.10",
                button11="B2.11",
                button12="B2.12",
                button13="B2.13",
                button14="B2.14",
                button15="B2.15",
                button16="B2.16",
                activity="P1.1",
                pitch="_PITCH_UNQUANTIZED",
                gate="G1.1",
                mutebutton="B2.25",
                lengthbutton="B2.17",
                muteled="L2.25",
                led1="L2.1",
                led2="L2.2",
                led3="L2.3",
                led4="L2.4",
                led5="L2.5",
                led6="L2.6",
                led7="L2.7",
                led8="L2.8",
                led9="L2.9",
                led10="L2.10",
                led11="L2.11",
                led12="L2.12",
                led13="L2.13",
                led14="L2.14",
                led15="L2.15",
                led16="L2.16",
            ),
            metapatch.circuits.Minifonion(
                input="_PITCH_UNQUANTIZED",
                root="0",
                degree="7",
                select1="1",
                select3="1",
                select5="1",
                select7="1",
                select9="1",
                select11="1",
                select13="1",
                output="O1",
            ),
        ]



    def generate(self) -> None:
        """"Patch generator function.

        This function is the entrypoint function when generating the patch.
        """
        self.add_controller("p4b2", 1)
        self.add_controller("b32", 2)
        self.add_circuits(
            self.clock(),
            "clock",
        )

        self.add_circuits(
            self.algoquencer(),
            "Algoquencer",
        )

if __name__ == "__main__":
    PatchGenerator.run()


```

Here you can see how each of the sections of your patch are now made into their own python functions. These functions return a list of circuits identical to those in your patch.

This is a great starting point.

Let&rsquo;s start by changing the title and the description under the `class` definition.

```python
class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Simple Algoquencer"
    description = "A patch generator for simple algoquencers."

```

Now you can work on making this patch *dynamic*.


### Adding input parameters

Three types of input parameters are supported:

-   Boolean which are represented in Forge with a checkbox. It&rsquo;s a true/false, or on/off variable.
-   Number ranges that go from a minimum number to a maximum number.
-   An *enumeration*, or a defined set of text values you can select in a drop-down box.

We can add these by defining them as *class variables* in our patch generator class.

We might for example want to take our algoquencer and generate between 1 and 4 voices from it, so we can add a variable called `voices`.

In our class definition, we can write:

```python
class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Simple Algoquencer"
    description = "A patch generator for simple algoquencers."

    voices: int = metapatch.option("Number of voices", minimum=1, maximum=4)

```

The type notation `:int` makes it easier for your editor to validate your code, and the important part is the `metapatch.option` assignment.

The first argument (&ldquo;Number of voices&rdquo;) is the description of the parameter, the next part determines the type of parameter.

For numbers, we specify `minumum` and `maximum`.

Let&rsquo;s add a parameter to determine how many steps to use. This will be a string enumeration.

```python
class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Simple Algoquencer"
    description = "A patch generator for simple algoquencers."

    voices: int = metapatch.option("Number of voices", minimum=1, maximum=4)
    steps: str = metapatch.option("Number of steps", choices=[("16", "16 steps"), ("8", "8 steps")])

```

Here we specify our enumeration as a *list of tuples*. The first value of the tuple is the value in your code when read it, and the second is the description seen in the Forge wizard.

Let&rsquo;s add a boolean to determine whether to use an internal clock or an external one.

```python
class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Simple Algoquencer"
    description = "A patch generator for simple algoquencers."

    voices: int = metapatch.option("Number of voices", minimum=1, maximum=4)
    steps: str = metapatch.option("Number of steps", choices=[("16", "16 steps"), ("8", "8 steps")])
    external_clock: bool = metapatch.option("Use an external clock input instead of the internal one.")

```

Now we have three nice variables we can use to transform our patch with.


### Making our voices

The boilerplate version of our patch gave us one python function per section in the patch. This should make it possible for us to put those parameters into those functions.

Let&rsquo;s modify our algoquencer function.

```python
    def algoquencer(self, output: str, gate: str, mutebutton: str, select: str) -> List[metapatch.DroidCircuit]:
        """Generate contents of section 'Algoquencer'."""
        muteled = "L" + mutebutton[1:]
        algoquencer = metapatch.circuits.Algoquencer(
            select=select,
            clock="_CLOCK",
            reset="_RESET",
            button1="B2.1",
            button2="B2.2",
            button3="B2.3",
            button4="B2.4",
            button5="B2.5",
            button6="B2.6",
            button7="B2.7",
            button8="B2.8",
            button9="B2.9",
            button10="B2.10",
            button11="B2.11",
            button12="B2.12",
            button13="B2.13",
            button14="B2.14",
            button15="B2.15",
            button16="B2.16",
            activity="P1.1",
            pitch=f"{select}_PITCH_UNQUANTIZED",
            gate=gate,
            mutebutton=mutebutton,
            lengthbutton="B2.17",
            muteled=muteled,
            led1="L2.1",
            led2="L2.2",
            led3="L2.3",
            led4="L2.4",
            led5="L2.5",
            led6="L2.6",
            led7="L2.7",
            led8="L2.8",
            led9="L2.9",
            led10="L2.10",
            led11="L2.11",
            led12="L2.12",
            led13="L2.13",
            led14="L2.14",
            led15="L2.15",
            led16="L2.16",
        )
        quantizer = metapatch.circuits.Minifonion(
            input=f"{select}_PITCH_UNQUANTIZED",
            root="0",
            degree="7",
            select1="1",
            select3="1",
            select5="1",
            select7="1",
            select9="1",
            select11="1",
            select13="1",
            output=select,
        )
        return [algoquencer, quantizer]

```

Now we can call this function with different arguments depending on the voice allocation.

We do this in our `generate()` function.

```python
    def generate(self) -> None:
        """"Patch generator function.

        This function is the entrypoint function when generating the patch.
        """
        self.add_controller("p4b2", 1)
        self.add_controller("b32", 2)
        self.add_circuits(
            self.clock(),
            "clock",
        )

        for voice in range(1, self.voices + 1):
            output = f"O{voice}"
            gate = f"G1.{voice}"
            mutebutton = f"B2.{16 + voice}"
            select = f"_VOICE_{voice}"
            self.add_circuits(
                self.algoquencer(output, gate, mutebutton, select),
                f"Voice {voice} Algoquencer",
            )


```

Notice how the string after the function call was also updated? This is to give each voice their own section.

Let&rsquo;s quickly update the clock function also.

```python
    def clock(self) -> List[metapatch.DroidCircuit]:
        """Generate contents of section 'clock'."""
        if self.external_clock:
            return [
                metapatch.circuits.Copy(input="I1", output="_CLOCK"),
                metapatch.circuits.Copy(input="I2", output="_RESET"),
            ]

        # if external clock is false, the following is returned:
        return [
            metapatch.circuits.Lfo(
                hz="-8 * P1.4 + 8",
                square="_CLOCK_UNMUTED",
            ),
            metapatch.circuits.Button(
                button="B1.1",
                onvalue="1",
                offvalue="0",
                led="L1.1",
                output="_RUNNING",
            ),
            metapatch.circuits.Button(
                button="B1.1",
                states="1",
                output="_RESET",
            ),
            metapatch.circuits.Copy(
                input="_CLOCK_UNMUTED * _RUNNING",
                output="_CLOCK",
            ),
        ]

```

We don&rsquo;t need to add an input variable for something as simple as this, and we can much easier just check the external<sub>clock</sub> variable inside this function.


### Modifying circuits

Remember how we added a parameter to choose the length of our buttons?

Let&rsquo;s make our algoquencer function handle this too.

```python
    def algoquencer(self, output: str, gate: str, mutebutton: str, select: str) -> List[metapatch.DroidCircuit]:
        """Generate contents of section 'Algoquencer'."""
        muteled = "L" + mutebutton[1:]
        algoquencer = metapatch.circuits.Algoquencer(
            select=select,
            clock="_CLOCK",
            reset="_RESET",
            button1="B2.1",
            button2="B2.2",
            button3="B2.3",
            button4="B2.4",
            button5="B2.5",
            button6="B2.6",
            button7="B2.7",
            button8="B2.8",
            activity="P1.1",
            pitch=f"{select}_PITCH_UNQUANTIZED",
            gate=gate,
            mutebutton=mutebutton,
            lengthbutton="B2.17",
            muteled=muteled,
            led1="L2.1",
            led2="L2.2",
            led3="L2.3",
            led4="L2.4",
            led5="L2.5",
            led6="L2.6",
            led7="L2.7",
            led8="L2.8",
        )
        if self.steps == "16":
            algoquencer.button9 = "B2.9"
            algoquencer.button10 = "B2.10"
            algoquencer.button11 = "B2.11"
            algoquencer.button12 = "B3.12"
            algoquencer.button13 = "B2.13"
            algoquencer.button14 = "B3.14"
            algoquencer.button15 = "B2.15"
            algoquencer.button16 = "B2.16"
            algoquencer.led9 = "L2.9"
            algoquencer.led10 = "L2.10"
            algoquencer.led11 = "L2.11"
            algoquencer.led12 = "L3.12"
            algoquencer.led13 = "L2.13"
            algoquencer.led14 = "L3.14"
            algoquencer.led15 = "L2.15"
            algoquencer.led16 = "L2.16"

        quantizer = metapatch.circuits.Minifonion(
            input=f"{select}_PITCH_UNQUANTIZED",
            root="0",
            degree="7",
            select1="1",
            select3="1",
            select5="1",
            select7="1",
            select9="1",
            select11="1",
            select13="1",
            output=output,
        )
        return [algoquencer, quantizer]


```

The various Droid circuits are implemented as so called `dataclasses`, and their values can either be set at initialization, or afterwards.

Note that some names of parameters clash with python&rsquo;s internal keywords, for example the many of the parameters in the `compare` circuit have this problem. The parameter names have gotten an underscore added here, so that `else` becomes `else_`.


### Adding presets

The metapatch framework automatically adds a default preset, since a patch generator must have at least one of these to be valid. You can however add your own. These are added in much the same way as the parameters.

```python
class PatchGenerator(metapatch.PatchGenerator):
    """"Auto-generated patch generator.

    Change this to something more meaningful.
        Also remember to add parameters and presets.
    """

    title = "Simple Algoquencer"
    description = "A patch generator for simple algoquencers."

    voices: int = metapatch.option("Number of voices", minimum=1, maximum=4)
    steps: str = metapatch.option("Number of steps", choices=[("16", "16 steps"), ("8", "8 steps")])
    external_clock: bool = metapatch.option("Use an external clock input instead of the internal one.")
    my_preset = metapatch.preset("My Favorite Preset", {"voices": 4, "steps": "16", "external_clock": False})

```

Here the preset is defined with a description, and a dictionary of our parameters and the values assigned by the preset.


### Wrapping up

There&rsquo;s much more to explore from here but this is the basics.

If you run your script from the command line, it will generate a patch. If you type `--help`, you will get the following:

```
usage: DROID patch generator "Simple Algoquencer" [-h] [--synopsis] [-p P] [param=value ... ...]

A patch generator for simple algoquencers.

positional arguments:
  param=value ...   Patch generator parameters.

options:
  -h, --help        show this help message and exit
  --synopsis, -s    Output possible parameters as JSON
  -p P, --preset P  Use settings from preset P

Available Presets:
my_preset    My Favorite Preset

parameters (defaults are marked with *):

  Number of voices
      voices=1..4           Number of voices

  Number of steps
    * steps=16              16 steps
      steps=8               8 steps

  Use an external clock input instead of the internal one.
    * external_clock=True   Use an external clock input instead of the internal one.
      external_clock=False  Don't use an external clock input instead of the internal one.
```

You can also check the synopsis. Here I&rsquo;ve used the `jq` program to format it nicely.

`$ python examples/getting_started -s | jq`

```json
{
  "title": "Simple Algoquencer",
  "description": "A patch generator for simple algoquencers.",
  "sections": [
    {
      "title": "Options",
      "options": [
        {
          "name": "voices",
          "title": "Number of voices",
          "number": [
            1,
            4
          ]
        },
        {
          "name": "steps",
          "title": "Number of steps",
          "enum": [
            [
              "16",
              "16 steps"
            ],
            [
              "8",
              "8 steps"
            ]
          ]
        },
        {
          "name": "external_clock",
          "title": "Use an external clock input instead of the internal one."
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "my_preset",
      "title": "My Favorite Preset",
      "parameters": {
        "voices": 4,
        "steps": "16",
        "external_clock": false
      }
    }
  ]
}

```


# Getting help

If you have any problems with the library, let me know on the DROID discord server. I&rsquo;m known as eising on that server.

Please note that any support will be on a best effort basis, if I have the time an energy.

If you have found a bug, please create an issue on [Github](https://github.com/Eising/droid-metapatch).


# License

I have chosen to use the same license as the DROID Forge, namely GPL version 3.

The source code is distributed with a copy of this license.
