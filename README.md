# Introduction

The DROID metapatch library aims to create an easier and more pythonic way of creating DROID patch generators. DROID patch generators are a recent feature added to the the DROID Forge application that allows you to define python scripts that generate full-fledges patches.

DROID is a series of eurorack controllers and CV processors made by [Der Mann mit der Maschine](https://shop.dermannmitdermaschine.de/).


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


# Getting started

A few examples have been distributed with the source code of this library that you may look at to see full implementations.


## Using droid-metapatch to convert an existing patch to a patch generator

To get started really quickly, there&rsquo;s a helpful CLI script bundled with this library.

```
$ droid-metapatch --help
usage: droid-metapatch [-h] [--boilerplate] [infile] [outfile]

Metapatch helper script.

positional arguments:
  infile         Input file. Defaults to stdin.
  outfile        Output file. Defaults to stdout.

options:
  -h, --help     show this help message and exit
  --boilerplate  Generate a full example patch generator.

If called without any arguments, you may input one or more droid circuits, and get the corresponding
python code back.
```

If you run it without any arguments, you can paste one or more circuits, and get just the python code back that you can use within an ongoing patchgenerator project.

However, if you provide a full patch as input, and use the `--boilerplate` option, it will output a full patch generator you can continue.


### Example

Here I&rsquo;m using one of the bundled patches from the blue4 DROID release:

```
$ droid-metapatch ~/p/droid/releases/droid-blue-4/patches/motoquencer_minimal.ini --boilerplate

import metapatch

class PatchGenerator(metapatch.PatchGenerator):
    """Patch Generator boilerplate.

    Change this to something more meaningful.
    Also remember to add parameters and presets.
    """
    title = "Title of your patch generator"  # CHANGEME
    description = "Description of your patch generator"  # CHANGEME

    def generate(self) -> None:
        """Patch generator function.

        Modify this function to create your patch generator.
        """
        self.add_controller("p2b8", 1)
        self.add_controller("m4", 2)

        self.add_section("LFO and Sequencer")

        self.add_circuit(
            "lfo",
            {
                "hz": "20 * P1.1",
                "square": "_CLOCK",
            },
            "Master clock"
        )

        self.add_circuit(
            "motoquencer",
            {
                "clock": "_CLOCK",
                "cv": "O1",
                "gate": "O5",
            },
            "This motoquencer has as many steps as you have M4 faders"
        )
if __name__ == "__main__":
    PatchGenerator.run()

```

If you specify an additional filename, the output will be written to that file instead of your terminal.


### Continuing

After this, you need to continue on your own. You should add presets and input parameters, and make the patch generator do something with those input parameters.

See the next section for more details.


## Defining your patch generator class

To start, you must define a python `class` that is a subclass of `metapatch.PatchGenerator`.

Inside this class, you must at least define a `title` and a `description`, as well as a method called `generate`.

This method should contain all the logic needed to create your patch. To actually define the patch, the class instance provides functions that allow you to add circuits, controllers and even sections.

```python
import metapatch


class MyPatchGenerator(metapatch.PatchGenerator):
    """My Patch Generator."""

    title = "My patch generator."
    description = "This is an example patch generator."

    def generate(self) -> None:
        """Generate a patch."""

```


## Capturing parameters

The patch generator framework supports three types of options:

-   Boolean (on/off)
-   A range of numbers
-   Choosing string values from a drop-down list (enumerations)

These are quite essential to make your patch generator dynamic, and can be defined in the class with the `option` function.

```python
class MyPatchGenerator(metapatch.PatchGenerator):
    """My Patch Generator."""

    title = "My patch generator."
    description = "This is an example patch generator."
    # Parameters
    midi_channel: int = metapatch.option("MIDI channel to use", minimum=1, maximum=16)
    clock_source: str = metapatch.option(
        "Clock source, internal or external",
        choices=[
            ("internal", "Generate a clock with a DROID circuit"),
            ("external", "Receive clock via CV"),
            ("midi", "Receive a clock via MIDI")
        ]
    )
    copy_clock: bool = metapatch.option("Copy clock to an output")

    def generate(self) -> None:
        """Generate a patch."""
        if self.clock_source == "external":
            # Do something here



```

In this example, we see all three option types. To make your text editor be able to help you, we use `type hints` on our parameters.

We can now access those parameters from inside our `generate()` function like shown before.

You can also specify default values for parameters, by adding `default=defaultvalue`. If no default value is specified, we use the following logic:

-   The first provided choice for enumerations
-   True for booleans
-   The lowest number for number ranges.


## Capturing presets

I&rsquo;ve defined presets as a defined set of parameters with a title.

You define your presets in much the same way as your parameters:

```python
class MyPatchGenerator(metapatch.PatchGenerator):
    """My Patch Generator."""

    title = "My patch generator."
    description = "This is an example patch generator."
    # Parameters
    midi_channel: int = metapatch.option("MIDI channel to use", minimum=1, maximum=16)
    clock_source: str = metapatch.option(
        "Clock source, internal or external",
        choices=[
            ("internal", "Generate a clock with a DROID circuit"),
            ("external", "Receive clock via CV"),
            ("midi", "Receive a clock via MIDI")
        ]
    )
    copy_clock: bool = metapatch.option("Copy clock to an output")

    default = metapatch.preset(
        "The default preset",
        {
            "midi_channel": 11,
            "clock_source": "internal",
            "copy_clock": False,
        }
    )


```

Any value provided to the `preset()` function dictionary will be passed to the patch generator if that particular preset is loaded.


## Writing patches

The following actions are currently supported:

-   Adding controllers
-   Adding circuits
-   Adding sections
-   Adding labels to jacks, buttons and pots


### Adding controllers

```python
    def add_controller(self, type: str, position: int) -> None:
        """Add a controller at a given position.

        Args:
            type: Type of controller, e.g. B32
            position: controller position, e.g. 1
        """
```

Controllers must be added with a position parameter. So if you want to add a `P2B8` module in the first position, you can can write as follows:

```python
self.add_controller("P2B8", 1)
```


### Adding circuits

```python
    def add_circuit(
        self,
        name: str,
        params: Mapping[str, str],
        comment: Optional[str] = None,
    ) -> None:
        """Add a circuit.

        Args:
            name: Circuit name, e.g. copy for a [copy] circuit
            params: Dictionary of circuit parameters.
            comment: Optional comment for the circuit.
        """
```

To add a simple `copy` circuit:

```python
self.add_circuit("copy", {"input": "I1", "output": "O1"}, "This circuit copies from I1 to O1")
```

The comment is optional.


### Splitting your patch into sections

Sections are a great way to split up a patch into smaller chunks that may be easier to read.

You can define sections as you write your patch:

```python
class MyPatch(metapatch.PatchGenerator):

    title = "Example"
    description = "Example"

    voices: int = metapatch.option("Number of voices", minimum=1, maximum=4)
    def generate(self) -> None:
        """Generate patch."""
        # Section with a comment
        self.add_section("Master Clock", "This section contains the master clock configuration.")
        # Add your circuits to this section.
        self.add_circuit("lfo", {...})

        # Iterate over voices that were defined
        for voicenum in range(1, self.voices + 1):
            self.add_section(f"Voice {voicenum}")
            # Add circuits here.
```


### Adding labels to jacks, buttons and pots

You can add labels to jacks, buttons and pots with the `add_label` function:

```python
    def add_label(
        self, item: str, short_label: str, long_label: Optional[str] = None
    ) -> None:
        """Add a label.

        Args:
            item: string of the thing you want to label, e.g. O1 or G1.2
            short_label: The short label
            long_label: Optional longer label
        """
```

The item is the item you want to label, and can be anything that supports a label. The short label is mandatory, but the long one can be optional.

For example:

```python
        def generate(self) -> None:
            """Generate patch."""
            self.add_controller("P2B8", 1)
            self.add_controller("P2B8", 2)
            self.add_controller("P2B8", 3)
            self.add_controller("E4", 4)
            self.add_label("I1", "Input 1", "This is input 1")
            self.add_label("O1", "Output 1")
            self.add_label("G2.7", "Gate 7", "Gate jack number 7")
            self.add_label("E4.3", "Encoder", "Encoder 3 on module 4")
```

This will generate the following:

```
#  I1: [Input 1] This is input 1

# OUTPUTS:
#  O1: [Output 1]

# GATES ON MODULE 2:
#  G2.7: [Gate 7] Gate jack number 7

# CONTROLLER 4:
#  E4.3: [Encoder] Encoder 3 on module 4

[P2B8]
[P2B8]
[P2B8]
[E4]


```


## Finishing your patch

Once you are done writing your code, you just need to make sure that the patch generator is loaded when executing the module.

This can be done by simply calling `run()` on your class.

```python
class MyPatch(metapatch.PatchGenerator):

    title = "Example"
    description = "Example"

    def generate(self) -> None:
        """Patch generator function."""
        # Patch generator logic here


MyPatch.run()
```

This automatically sets up processing of command line arguments, correct argument passing and so on.


# Getting help

If you have any problems with the library, let me know on the DROID discord server. I&rsquo;m known as eising on that server.

Please note that any support will be on a best effort basis, if I have the time an energy.

If you have found a bug, please create an issue here on github.
