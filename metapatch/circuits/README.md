# DROID Circuits

In this module you will find all the DROID circuits including descriptions of their parameters.

All of this is auto-generated based on the circuits.json file that is bundled with each DROID release.

## Using circuits in your patch generator.
You can use these in your patch generators directly, and with a modern editor, you should get relevant help for each circuit and parameter.

Note that some circuit parameters collide with reserved keyword names in Python. In those cases, an `_` has been added. See for example `metapatch.circuits.Case.else_`.
Outside of the name itself, it behaves the same.

I have tried my best to clean up the embedded formating in the parameter description, but I may have missed something.
Kindly let me know by creating an issue in the github repository.

To work with the circuits, two functions are included in the `metapatch.PatchGenerator` class: `metapatch.PatchGenerator.add` to add a single circuit, and `metapatch.PatchGenerator.add_circuits` that support adding multiple circuits, and even applying transformations to them.

For example:

``` python

class PatchGenerator(metapatch.PatchGenerator):
    
    def generate(self) -> None:
        """Generate patch."""
        clock = [
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
        # Add the list of circuits in the clock variable to a 
        # section called "Master Clock"
        self.add_circuits(clock, "Master Clock")

```
