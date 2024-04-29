"""Functions to layers test.

This demonstrates how a function can be made into multiple layers using the
tranformation actions.
"""

from typing import List

import metapatch
import metapatch.circuits
from metapatch import DroidCircuit


class TestMetaPatch(metapatch.PatchGenerator):
    """Test metapatch."""

    title = "Test"
    description = "A test patch."

    voices = metapatch.option("Number of voices", minimum=1, maximum=4)

    def sequencer(self) -> List[DroidCircuit]:
        """Sequencer."""
        voice = [
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
                led1="L2.1",
                led2="L2.2",
                led3="L2.3",
                led4="L2.4",
                led5="L2.5",
                led6="L2.6",
                led7="L2.7",
                led8="L2.8",
                gate="_GATE",
                pitch="_PITCH_U",
                activity="_ACTIVITY",
            ),
            metapatch.circuits.Pot(pot="P3.1", notch="0.1", output="_ACTIVITY"),
            metapatch.circuits.Minifonion(
                input="_PITCH_U",
                root="_ROOT",
                degree="_DEGREE",
                select1="1",
                select3="1",
                select5="1",
                select7="1",
                select9="1",
                select11="1",
                select13="1",
                tuningmode="_TUNINGMODE",
                tuningpitch="3V",
                output="O1",
            ),
            metapatch.circuits.Button(
                button="B1.1", led="L1.1", onvalue="0", offvalue="1", output="_MUTED"
            ),
            metapatch.circuits.Copy(input="_GATE * _MUTED", output="G1.1"),
        ]
        return voice

    def generate(self) -> None:
        """Generate patch."""
        self.add_controller("P2B8", 1)
        self.add_controller("B32", 2)
        self.add_controller("P4B2", 3)
        for voice in range(1, self.voices + 1):
            self.add_circuits(
                self.sequencer(),
                f"Voice {voice}",
                ignore=["_ROOT", "_DEGREE", "_CLOCK", "_RESET", "_TUNINGMODE"],
                prepend=f"_VOICE_{voice}",
                output=f"O{voice}",
                gate=f"G1.{voice}",
                replace=[
                    ("P3.1", f"P3.{voice}"),
                    ("B1.1", f"B1.{voice}"),
                    ("L1.1", f"L1.{voice}"),
                ],
            )


if __name__ == "__main__":
    TestMetaPatch.run()
