"""DROID circuits. These circuits are auto-generated from circuits.json."""

from dataclasses import dataclass, field
from typing import Optional

from metapatch.circuits.base import DroidCircuit
from metapatch.circuits import circuit_types as ctype


__droid_version__ = "blue-6"


@dataclass
class Firefacecontrol(DroidCircuit):
    """Control a RME Fireface interface (experimental).

    Args:
        trs (integer):

        outputlevel1 (fraction):

        outputlevel2 (fraction):

        outputlevel3 (fraction):

        outputlevel4 (fraction):

        outputlevel5 (fraction):

        outputlevel6 (fraction):

        outputlevel7 (fraction):

        outputlevel8 (fraction):

        outputlevel9 (fraction):

        outputlevel10 (fraction):

        outputlevel11 (fraction):

        outputlevel12 (fraction):

        outputlevel13 (fraction):

        outputlevel14 (fraction):

        outputlevel15 (fraction):

        outputlevel16 (fraction):

        mainoutput (integer):

        phonesoutput1 (integer):

        phonesoutput2 (integer):

        outputmix1in1 (fraction):

        outputmix1in2 (fraction):

        outputmix1in3 (fraction):

        outputmix1in4 (fraction):

        outputmix1in5 (fraction):

        outputmix1in6 (fraction):

        outputmix1in7 (fraction):

        outputmix1in8 (fraction):

        outputmix1in9 (fraction):

        outputmix1in10 (fraction):

        outputmix1in11 (fraction):

        outputmix1in12 (fraction):

        outputmix1in13 (fraction):

        outputmix1in14 (fraction):

        outputmix1in15 (fraction):

        outputmix1in16 (fraction):

        outputmix2in1 (fraction):

        outputmix2in2 (fraction):

        outputmix2in3 (fraction):

        outputmix2in4 (fraction):

        outputmix2in5 (fraction):

        outputmix2in6 (fraction):

        outputmix2in7 (fraction):

        outputmix2in8 (fraction):

        outputmix2in9 (fraction):

        outputmix2in10 (fraction):

        outputmix2in11 (fraction):

        outputmix2in12 (fraction):

        outputmix2in13 (fraction):

        outputmix2in14 (fraction):

        outputmix2in15 (fraction):

        outputmix2in16 (fraction):

        outputmix3in1 (fraction):

        outputmix3in2 (fraction):

        outputmix3in3 (fraction):

        outputmix3in4 (fraction):

        outputmix3in5 (fraction):

        outputmix3in6 (fraction):

        outputmix3in7 (fraction):

        outputmix3in8 (fraction):

        outputmix3in9 (fraction):

        outputmix3in10 (fraction):

        outputmix3in11 (fraction):

        outputmix3in12 (fraction):

        outputmix3in13 (fraction):

        outputmix3in14 (fraction):

        outputmix3in15 (fraction):

        outputmix3in16 (fraction):

        outputmix4in1 (fraction):

        outputmix4in2 (fraction):

        outputmix4in3 (fraction):

        outputmix4in4 (fraction):

        outputmix4in5 (fraction):

        outputmix4in6 (fraction):

        outputmix4in7 (fraction):

        outputmix4in8 (fraction):

        outputmix4in9 (fraction):

        outputmix4in10 (fraction):

        outputmix4in11 (fraction):

        outputmix4in12 (fraction):

        outputmix4in13 (fraction):

        outputmix4in14 (fraction):

        outputmix4in15 (fraction):

        outputmix4in16 (fraction):

        outputmix5in1 (fraction):

        outputmix5in2 (fraction):

        outputmix5in3 (fraction):

        outputmix5in4 (fraction):

        outputmix5in5 (fraction):

        outputmix5in6 (fraction):

        outputmix5in7 (fraction):

        outputmix5in8 (fraction):

        outputmix5in9 (fraction):

        outputmix5in10 (fraction):

        outputmix5in11 (fraction):

        outputmix5in12 (fraction):

        outputmix5in13 (fraction):

        outputmix5in14 (fraction):

        outputmix5in15 (fraction):

        outputmix5in16 (fraction):

        outputmix6in1 (fraction):

        outputmix6in2 (fraction):

        outputmix6in3 (fraction):

        outputmix6in4 (fraction):

        outputmix6in5 (fraction):

        outputmix6in6 (fraction):

        outputmix6in7 (fraction):

        outputmix6in8 (fraction):

        outputmix6in9 (fraction):

        outputmix6in10 (fraction):

        outputmix6in11 (fraction):

        outputmix6in12 (fraction):

        outputmix6in13 (fraction):

        outputmix6in14 (fraction):

        outputmix6in15 (fraction):

        outputmix6in16 (fraction):

        outputmix7in1 (fraction):

        outputmix7in2 (fraction):

        outputmix7in3 (fraction):

        outputmix7in4 (fraction):

        outputmix7in5 (fraction):

        outputmix7in6 (fraction):

        outputmix7in7 (fraction):

        outputmix7in8 (fraction):

        outputmix7in9 (fraction):

        outputmix7in10 (fraction):

        outputmix7in11 (fraction):

        outputmix7in12 (fraction):

        outputmix7in13 (fraction):

        outputmix7in14 (fraction):

        outputmix7in15 (fraction):

        outputmix7in16 (fraction):

        outputmix8in1 (fraction):

        outputmix8in2 (fraction):

        outputmix8in3 (fraction):

        outputmix8in4 (fraction):

        outputmix8in5 (fraction):

        outputmix8in6 (fraction):

        outputmix8in7 (fraction):

        outputmix8in8 (fraction):

        outputmix8in9 (fraction):

        outputmix8in10 (fraction):

        outputmix8in11 (fraction):

        outputmix8in12 (fraction):

        outputmix8in13 (fraction):

        outputmix8in14 (fraction):

        outputmix8in15 (fraction):

        outputmix8in16 (fraction):

        outputmix9in1 (fraction):

        outputmix9in2 (fraction):

        outputmix9in3 (fraction):

        outputmix9in4 (fraction):

        outputmix9in5 (fraction):

        outputmix9in6 (fraction):

        outputmix9in7 (fraction):

        outputmix9in8 (fraction):

        outputmix9in9 (fraction):

        outputmix9in10 (fraction):

        outputmix9in11 (fraction):

        outputmix9in12 (fraction):

        outputmix9in13 (fraction):

        outputmix9in14 (fraction):

        outputmix9in15 (fraction):

        outputmix9in16 (fraction):

        outputmix10in1 (fraction):

        outputmix10in2 (fraction):

        outputmix10in3 (fraction):

        outputmix10in4 (fraction):

        outputmix10in5 (fraction):

        outputmix10in6 (fraction):

        outputmix10in7 (fraction):

        outputmix10in8 (fraction):

        outputmix10in9 (fraction):

        outputmix10in10 (fraction):

        outputmix10in11 (fraction):

        outputmix10in12 (fraction):

        outputmix10in13 (fraction):

        outputmix10in14 (fraction):

        outputmix10in15 (fraction):

        outputmix10in16 (fraction):

        outputmix11in1 (fraction):

        outputmix11in2 (fraction):

        outputmix11in3 (fraction):

        outputmix11in4 (fraction):

        outputmix11in5 (fraction):

        outputmix11in6 (fraction):

        outputmix11in7 (fraction):

        outputmix11in8 (fraction):

        outputmix11in9 (fraction):

        outputmix11in10 (fraction):

        outputmix11in11 (fraction):

        outputmix11in12 (fraction):

        outputmix11in13 (fraction):

        outputmix11in14 (fraction):

        outputmix11in15 (fraction):

        outputmix11in16 (fraction):

        outputmix12in1 (fraction):

        outputmix12in2 (fraction):

        outputmix12in3 (fraction):

        outputmix12in4 (fraction):

        outputmix12in5 (fraction):

        outputmix12in6 (fraction):

        outputmix12in7 (fraction):

        outputmix12in8 (fraction):

        outputmix12in9 (fraction):

        outputmix12in10 (fraction):

        outputmix12in11 (fraction):

        outputmix12in12 (fraction):

        outputmix12in13 (fraction):

        outputmix12in14 (fraction):

        outputmix12in15 (fraction):

        outputmix12in16 (fraction):

        outputmix13in1 (fraction):

        outputmix13in2 (fraction):

        outputmix13in3 (fraction):

        outputmix13in4 (fraction):

        outputmix13in5 (fraction):

        outputmix13in6 (fraction):

        outputmix13in7 (fraction):

        outputmix13in8 (fraction):

        outputmix13in9 (fraction):

        outputmix13in10 (fraction):

        outputmix13in11 (fraction):

        outputmix13in12 (fraction):

        outputmix13in13 (fraction):

        outputmix13in14 (fraction):

        outputmix13in15 (fraction):

        outputmix13in16 (fraction):

        outputmix14in1 (fraction):

        outputmix14in2 (fraction):

        outputmix14in3 (fraction):

        outputmix14in4 (fraction):

        outputmix14in5 (fraction):

        outputmix14in6 (fraction):

        outputmix14in7 (fraction):

        outputmix14in8 (fraction):

        outputmix14in9 (fraction):

        outputmix14in10 (fraction):

        outputmix14in11 (fraction):

        outputmix14in12 (fraction):

        outputmix14in13 (fraction):

        outputmix14in14 (fraction):

        outputmix14in15 (fraction):

        outputmix14in16 (fraction):

        outputmix15in1 (fraction):

        outputmix15in2 (fraction):

        outputmix15in3 (fraction):

        outputmix15in4 (fraction):

        outputmix15in5 (fraction):

        outputmix15in6 (fraction):

        outputmix15in7 (fraction):

        outputmix15in8 (fraction):

        outputmix15in9 (fraction):

        outputmix15in10 (fraction):

        outputmix15in11 (fraction):

        outputmix15in12 (fraction):

        outputmix15in13 (fraction):

        outputmix15in14 (fraction):

        outputmix15in15 (fraction):

        outputmix15in16 (fraction):

        outputmix16in1 (fraction):

        outputmix16in2 (fraction):

        outputmix16in3 (fraction):

        outputmix16in4 (fraction):

        outputmix16in5 (fraction):

        outputmix16in6 (fraction):

        outputmix16in7 (fraction):

        outputmix16in8 (fraction):

        outputmix16in9 (fraction):

        outputmix16in10 (fraction):

        outputmix16in11 (fraction):

        outputmix16in12 (fraction):

        outputmix16in13 (fraction):

        outputmix16in14 (fraction):

        outputmix16in15 (fraction):

        outputmix16in16 (fraction):

        postfader1 (gate):

        postfader2 (gate):

        postfader3 (gate):

        postfader4 (gate):

        postfader5 (gate):

        postfader6 (gate):

        postfader7 (gate):

        postfader8 (gate):

        postfader9 (gate):

        postfader10 (gate):

        postfader11 (gate):

        postfader12 (gate):

        postfader13 (gate):

        postfader14 (gate):

        postfader15 (gate):

        postfader16 (gate):

        pan1 (fraction):

        pan2 (fraction):

        pan3 (fraction):

        pan4 (fraction):

        pan5 (fraction):

        pan6 (fraction):

        pan7 (fraction):

        pan8 (fraction):

        pan9 (fraction):

        pan10 (fraction):

        pan11 (fraction):

        pan12 (fraction):

        pan13 (fraction):

        pan14 (fraction):

        pan15 (fraction):

        pan16 (fraction):

        unmute1 (fraction):

        unmute2 (fraction):

        unmute3 (fraction):

        unmute4 (fraction):

        unmute5 (fraction):

        unmute6 (fraction):

        unmute7 (fraction):

        unmute8 (fraction):

        unmute9 (fraction):

        unmute10 (fraction):

        unmute11 (fraction):

        unmute12 (fraction):

        unmute13 (fraction):

        unmute14 (fraction):

        unmute15 (fraction):

        unmute16 (fraction):

        update (trigger):

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
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 1088
    trs: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    outputlevel1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputlevel16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    mainoutput: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    phonesoutput1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    phonesoutput2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    outputmix1in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix1in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix2in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix3in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix4in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix5in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix6in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix7in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix8in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix9in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix10in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix11in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix12in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix13in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix14in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix15in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    outputmix16in16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    postfader1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader13: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader14: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader15: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    postfader16: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pan1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pan16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    unmute16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    update: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    select: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    selectat: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )



@dataclass
class Midifileplayer(DroidCircuit):
    """MIDI file player.

    Args:
        file (integer):
          Number of the MIDI file to play. 7 will select midi7.mid.
        track (integer):
          Number of the track in the file to play, starting at 1. Empty tracks do not
          count. Any number smaller than 1 will be interpreted as one. If the number is
          too big, the last track in the file is played.
        clock (trigger):
          Patch an external clock here and the MIDI file will be played according to
          that clock. In order to be modular-friendly, this is not a MIDI clock but one
          counting the sixteenth, which is typically the step resolution of analog
          sequencers. This clock is then internally multiplied in order to create the
          necessary resolution. Note: The input speed has no effect when using an
          external clock.
        reset (trigger):
          A trigger here sets the play back position to the start.
        loop (gate):
          When loop mode is active (set to 1), the track will start over again
          immediately when it has reached its end. This is the default. Otherwise
          playback stops at the end of the track.
        end (integer):
          If you set this value, it defines the playing end of the track. This is set in
          quarters as counted from the start. Setting the end beyond the end of the
          track will insert some pause.
        speed (cv):
          Change the relative speed of the playback with this setting. At 1 the speed is
          unchanged. 1.5 makes the speed 50% faster, 0.5 plays at half speed. At 0 the
          playing is completely frozen. Note: speed is being ignored when using the
          input clock.
        channel (integer):
          Only execute / play commands from a certain MIDI channel. There are 16 MIDI
          channels. It ranges from 1 to 16.
        tuningmode (gate):
          If set to 1, all pitch outputs will go to the CV selected for tuningpitch
          (which defaults to 2 V), and all gate outputs will play gates at 120 BPM. This
          helps getting all attached voices tuned when working with many voices.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        transpose (voltperoctave):
          Transposes all output pitches by this value by adding the value. So in order
          to transpose one octave down, set this input to -1V or -0.1. Changes in the
          transposition are immediately reflected, even for currently already active
          notes.
        holdvelocity (gate):
          If this is set to 1, the velocity output for a voice will not be affected by
          note off events. It's just altered at the beginning of new notes. The velocity
          is kept after the note ends. This way during the release phase of an envelope
          triggered by the gate, the original velocity still lasts on. In most cases the
          note off velocity is set to 0, which would immediately cut off the release
          phase when the velocity is patched into a VCA.
        pitchbendrange (voltperoctave):
          Sets the value to the desired maximum that pitchbend should output, and
          likewise it's negative counterpart at its minimum value. At the middle
          position it always outputs 0. This defaults to 2/12 V, which corresponds to
          one whole tone. Note: setting this to a negative value is allowed and will
          invert pitch bend.
        bendpitch (gate):
          When set to 1 (which is the default), the pitch bend will directly be applied
          to all output pitches. Alternatively you can set it to 0 and use the output
          pitchbend, for using it elsewhere.
        roundrobin (gate):
          Normally when looking for a free output for playing the next note, this
          circuit will start from output1 in its search. This way, if there are not more
          notes than outputs at any time, the notes played first will always be played
          at the lowest numbered outputs. This leads to a deterministic behaviour when
          it comes to playing things like chords. The same voice will always be used for
          the first note in the stream of MIDI events.  When you switch roundrobin to 1,
          this changes. Now the outputs are scanned in a round-robin fashion, like in a
          rotating switch. That way every output has the same chance to get a new note.
          Here it can even make sense to define multiple voices even if the track is
          monophonic. When you use envelopes with longer release times, you can
          transform such a melody into chords with simultaneous notes.  Note: When all
          outputs are currently used by a note, roundrobin has no influence. Here
          voiceallocation selects which of the notes will be dropped.
        voiceallocation (integer):
          When the MIDI stream, at any given time, needs to play more notes than you
          have voices assigned, normally the “oldest” notes would be cancelled. This
          behaviour can be configured here by setting voiceallocation to one of the
          following values:  0The oldest note will be cancelled (default) 1The new note
          will not be played and simply be omitted 2The lowest note will be cancelled
          3The highest note will be cancelled
        notegap (cv):
          When your MIDI devices plays a note so “long” that it lasts exactly until the
          next note begins – or if due to a lack of used pitch outputs one currently
          played note has to be replaced with a new one, the gate output will have no
          time to go low for a sufficient time between the two notes. In effect it won't
          trigger any envelope for the new note but will play “legato”.  If you don't
          like this, you can use notegap. This input specifies a number of milliseconds
          that the gate will be forced down before the new note begins. This has the
          drawback of introducing some latency, of course! So I suggest that you start
          with notegap = 1 and then check out if your envelope is fast enough to
          trigger. If not, increase the value.  If you are using 's own contour circuit
          or trigger something else internally in your patch, you can use notegap = 0.1.
          That is sufficient and introduces barely any latency. A value of 0.0 keeps the
          default of the legato mode.  Note: the notegap parameter does not affect the
          trigger outputs.
        ccnumber1 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber2 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber3 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber4 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        lowestnote (integer):
          With this input you can restrict the notes being played by setting a lower
          bound. In MIDI the notes range from 0 (C-2) to 127 (G9). By setting lowestnote
          to 24 (C0), all notes below this note are simply ignored. This allows for
          example for a keyboard split by using a second circuit with a highestnote of
          23. Note gates are not being affected by this bound.
        highestnote (integer):
          Sets an upper limit to the note being played, similar to lowestnote. The
          “Notegates” are not being affected by this bound.
        note1 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note2 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note3 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note4 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note5 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note6 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note7 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note8 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note9 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note10 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note11 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note12 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note13 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note14 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note15 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note16 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        clockout (trigger):
          Outputs a steady clock of 1 tick per 16 note.
        midiclock (trigger):
          Outputs a steady MIDI clock, i.e. 24 ticks per quarter note of the tune. This
          is 6 times faster than clock.
        endoftrack (trigger):
          Outputs a trigger when the end of the track is reached.
        error (cv):
          This output will be set to a value other than zero in case of an error while
          loading and parsing the MIDI file. This is intended for wiring it to one of
          the R registers. Here different errors will be displayed as different colors.
          Here is the list of all possible values of error:  0black – Everything is
          fine. -1white – The SD card or MIDI file is missing. 1magenta – The file is
          corrupted, garbled or no MIDI file. 0.75orange – The file does not contain any
          non-empty track. 0.25cyan – the track is too long (max 6000 bytes are
          allowed).
        pitch1 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch2 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch3 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch4 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch5 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch6 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch7 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch8 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        velocity1 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity2 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity3 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity4 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity5 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity6 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity7 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity8 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        pressure1 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure2 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure3 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure4 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure5 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure6 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure7 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure8 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        gate1 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate2 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate3 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate4 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate5 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate6 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate7 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate8 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        trigger1 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger2 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger3 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger4 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger5 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger6 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger7 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger8 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        cc1 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc2 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc3 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc4 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cctrigger1 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger2 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger3 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger4 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        notegate1 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate2 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate3 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate4 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate5 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate6 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate7 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate8 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate9 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate10 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate11 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate12 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate13 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate14 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate15 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate16 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        pitchbend (cv):
          Outputs the current pitch bend value as a bipolar voltage. The range can be
          set with pitchbendrange.
        programchange (trigger):
          Sends a trigger whenever a MIDI program change message arrives. Just before
          sending the trigger sets program to the new program number (something from 0
          to 127). Note: This trigger is also being output when the program change
          messages sends the same program number as previously, i.e. if there is no
          actual change.
        program (integer):
          The number of the last program change. This starts at 0.
        bank (integer):
          Outputs the number of the currently selected bank – from 0 to 16384. MIDI
          defines the MSB of the bank to be changed with CC#0 and the LSB with CC#32.
          That means if you just use CC#0, you will only be able to select the banks 0,
          128, 256, and so on. As long as no bank select CC has been received, bank will
          output 0.
        modwheel (fraction):
          Output the current state of the mod wheel level – within the range from 0.0 to
          1.0. The mod wheel is changed by MIDI control change 1.
        volume (fraction):
          Outputs the current global volume as set by MIDI control change 7.
        portamento (gate):
          This output gives you access to the current state of the “portamento pedal”
          (MIDI CC 65). You can use it to enable an external slew circuit for creating
          portamento effects.
        soft (gate):
          This output gives you access to the current state of the “soft pedal” (MIDI CC
          67). It is 1 while the pedal is hold and 0 otherwise.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 6384
    file: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    track: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    clock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    reset: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    loop: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    end: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    speed: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    channel: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    tuningmode: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    tuningpitch: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    transpose: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    holdvelocity: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitchbendrange: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    bendpitch: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    roundrobin: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    voiceallocation: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    notegap: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ccnumber1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    lowestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    highestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note5: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note6: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note7: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note8: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note9: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note10: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note11: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note12: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note13: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note14: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note15: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note16: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    clockout: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    midiclock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    endoftrack: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    error: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    pitch1: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch2: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch3: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch4: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch5: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch6: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch7: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch8: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    velocity1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    gate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    trigger1: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger2: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger3: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger5: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger6: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger7: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger8: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cc1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cctrigger1: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger2: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger3: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    notegate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate13: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate14: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate15: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate16: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitchbend: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    programchange: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    program: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    bank: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    modwheel: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    volume: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    portamento: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    soft: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )



@dataclass
class Midiin(DroidCircuit):
    """MIDI to CV converter.

    Args:
        trs (integer):
          Selects a TRS port to use (3.5 mm jack). trs = 0 disables TRS, trs = 10
          enables auto detection. See the manual of midiin for details on port
          selection.
        usb (integer):
          Selects a USB port to use. usb = 0 disables USB, usb = 10 enables auto
          detection. See the manual of midiin for details on port selection.
        initialrunning (integer):
          This parameter sets which “running” state is assumed when your starts. The
          idea behind this parameter is, that at this point of time you cannot know the
          real running state of the MIDI stream, since e.g. the might have started after
          the sequencer at the sending end of the line.  You have three ways to set
          this: start in stopped state, start in running state and an inbetween
          “automatic” mode. In the auto mode, you start in stopped state but
          automatically switch to running as soon as a note on event is received. At
          that moment a MIDI START event is simulated.  0Start stopped state 1Start in
          running state 2Automatic: start in stopped state, switch to running on first
          “note on”   Note: as this parameter is just read once the absolute system
          start, you cannot assign a dynamic CV input or control here.
        systemreset (trigger):
          A trigger here resets the whole MIDI state of this circuit. It does the same
          as a MIDI RESET message: It stops all playing note, resets the controllers,
          the states of the pedals and so on.
        channel (integer):
          Only execute / play commands from a certain MIDI channel. There are 16 MIDI
          channels. It ranges from 1 to 16.
        tuningmode (gate):
          If set to 1, all pitch outputs will go to the CV selected for tuningpitch
          (which defaults to 2 V), and all gate outputs will play gates at 120 BPM. This
          helps getting all attached voices tuned when working with many voices.
        tuningpitch (voltperoctave):
          This pitch CV will be output while the tuning mode is active.
        transpose (voltperoctave):
          Transposes all output pitches by this value by adding the value. So in order
          to transpose one octave down, set this input to -1V or -0.1. Changes in the
          transposition are immediately reflected, even for currently already active
          notes.
        holdvelocity (gate):
          If this is set to 1, the velocity output for a voice will not be affected by
          note off events. It's just altered at the beginning of new notes. The velocity
          is kept after the note ends. This way during the release phase of an envelope
          triggered by the gate, the original velocity still lasts on. In most cases the
          note off velocity is set to 0, which would immediately cut off the release
          phase when the velocity is patched into a VCA.
        pitchbendrange (voltperoctave):
          Sets the value to the desired maximum that pitchbend should output, and
          likewise it's negative counterpart at its minimum value. At the middle
          position it always outputs 0. This defaults to 2/12 V, which corresponds to
          one whole tone. Note: setting this to a negative value is allowed and will
          invert pitch bend.
        bendpitch (gate):
          When set to 1 (which is the default), the pitch bend will directly be applied
          to all output pitches. Alternatively you can set it to 0 and use the output
          pitchbend, for using it elsewhere.
        roundrobin (gate):
          Normally when looking for a free output for playing the next note, this
          circuit will start from output1 in its search. This way, if there are not more
          notes than outputs at any time, the notes played first will always be played
          at the lowest numbered outputs. This leads to a deterministic behaviour when
          it comes to playing things like chords. The same voice will always be used for
          the first note in the stream of MIDI events.  When you switch roundrobin to 1,
          this changes. Now the outputs are scanned in a round-robin fashion, like in a
          rotating switch. That way every output has the same chance to get a new note.
          Here it can even make sense to define multiple voices even if the track is
          monophonic. When you use envelopes with longer release times, you can
          transform such a melody into chords with simultaneous notes.  Note: When all
          outputs are currently used by a note, roundrobin has no influence. Here
          voiceallocation selects which of the notes will be dropped.
        voiceallocation (integer):
          When the MIDI stream, at any given time, needs to play more notes than you
          have voices assigned, normally the “oldest” notes would be cancelled. This
          behaviour can be configured here by setting voiceallocation to one of the
          following values:  0The oldest note will be cancelled (default) 1The new note
          will not be played and simply be omitted 2The lowest note will be cancelled
          3The highest note will be cancelled
        notegap (cv):
          When your MIDI devices plays a note so “long” that it lasts exactly until the
          next note begins – or if due to a lack of used pitch outputs one currently
          played note has to be replaced with a new one, the gate output will have no
          time to go low for a sufficient time between the two notes. In effect it won't
          trigger any envelope for the new note but will play “legato”.  If you don't
          like this, you can use notegap. This input specifies a number of milliseconds
          that the gate will be forced down before the new note begins. This has the
          drawback of introducing some latency, of course! So I suggest that you start
          with notegap = 1 and then check out if your envelope is fast enough to
          trigger. If not, increase the value.  If you are using 's own contour circuit
          or trigger something else internally in your patch, you can use notegap = 0.1.
          That is sufficient and introduces barely any latency. A value of 0.0 keeps the
          default of the legato mode.  Note: the notegap parameter does not affect the
          trigger outputs.
        ccnumber1 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber2 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber3 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        ccnumber4 (integer):
          You can listen to up to four CCs (control changes). For example if you are
          interested in the current value of CC#17, set ccnumber1 = 17 and use the
          output cc1 for getting the value of CC 17.
        lowestnote (integer):
          With this input you can restrict the notes being played by setting a lower
          bound. In MIDI the notes range from 0 (C-2) to 127 (G9). By setting lowestnote
          to 24 (C0), all notes below this note are simply ignored. This allows for
          example for a keyboard split by using a second circuit with a highestnote of
          23. Note gates are not being affected by this bound.
        highestnote (integer):
          Sets an upper limit to the note being played, similar to lowestnote. The
          “Notegates” are not being affected by this bound.
        note1 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note2 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note3 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note4 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note5 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note6 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note7 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note8 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note9 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note10 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note11 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note12 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note13 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note14 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note15 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        note16 (integer):
          Selects up to 16 individual notes for which you can get a dedicated gate
          signal. Per default these values are set to 0 for note1 (meaning C-2), 1 for
          note2 (meaning C♯-2) and so on. For each of these notes you get a
          corresponding gate output (see notegate1, notegate2, etc.). These gates are
          high as long as the selected notes are being hold. One application is to use
          just one midifileplayer or midiin circuit for sequencing up to 16 drum voices.
          Another application is to use a MIDI keyboard or controller as a button
          expander – just like a P2B8 or B32.
        clock (trigger):
          If the MIDI sender sends a MIDI clock, you get a 16 note clock output here.
          This is the same as the clock16 jack and just a convenient abbreviation.
        clock8 (trigger):
          Gets an 8 clock here (like clock divided by 2)
        clock8t (trigger):
          Gets a 8 triplets clock here. This is faster than clock8 but slower than
          clock.
        clock16 (trigger):
          The same as clock: a clock running at 16 notes.
        clock4 (trigger):
          A clock at the speed of quarter notes.
        midiclock (trigger):
          Here you get the original MIDI clock. This is 6 times faster than clock and 24
          times faster than clock4. This is because the MIDI clock is specified to run
          at 24 PPQ, i.e. 24 pulses per quarter note.
        start (trigger):
          This jack sends a trigger when a MIDI START message arrives.
        continue_ (trigger):
          This jack sends a trigger when a MIDI CONTINUE message arrives.
        stop (trigger):
          This jack sends a trigger when a MIDI STOP message arrives.
        running (gate):
          This jack remembers the current running state according to previous START and
          STOP messages.
        active (gate):
          If the sending device supports active sensing, this output is high as long as
          a device is connected. Otherwise its high if at least one MIDI message has
          been received.
        pitch1 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch2 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch3 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch4 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch5 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch6 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch7 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        pitch8 (voltperoctave):
          Pitch outputs. Since MIDI tracks can be polyphonic – i.e. play several notes
          at the same time – you can assign up to eight outputs here. The notes will be
          distributed to the defined outputs according to the settings roundrobin and
          voiceallocation.
        velocity1 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity2 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity3 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity4 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity5 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity6 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity7 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        velocity8 (fraction):
          For each voice there is an optional velocity output, which translates the MIDI
          velocity into values from 0 to 1.
        pressure1 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure2 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure3 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure4 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure5 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure6 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure7 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        pressure8 (fraction):
          MIDI provides two different messages for sending "after-touch" information,
          i.e. information about how strong a key is pressed down after the initial hit.
          Some keyboards just have one pressure sensor in total and send the current
          maximum pressure information of all keys in one message (“channel pressure”).
          Others have one pressure sensor per key and send “polyphonic key pressure”
          messages. This circuit maps both to a pressure output per note that is being
          played. So if your keyboard (or sequencer or DAW or whatever) sends polyphonic
          key pressure events and you use multiple pitchX outputs, wire the individual
          pressureX outputs to wherever you like. Otherwise you can simply use pressure1
          for all notes (which can be abbreviated with pressure), since it is the same
          for all note outputs anyway. pressure outputs a value from 0 to 1.
        gate1 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate2 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate3 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate4 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate5 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate6 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate7 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        gate8 (gate):
          Gate outputs for the up to eight simultaneous note outputs.
        trigger1 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger2 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger3 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger4 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger5 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger6 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger7 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        trigger8 (trigger):
          Trigger outputs for the up to eight simultaneous note outputs. The difference
          to the gate outputs is, that these just send a short trigger of 5 ms at the
          start of the note. This can be interesting in situations where the notes have
          no gaps in between so that gate will never go low.
        cc1 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc2 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc3 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cc4 (fraction):
          Outputs the current value of the four CC number that are defined with the
          inputs ccnumber1 ... ccnumber4. CCs have a range from 0 to 127, but this is
          converted in the range 0.0 .. 1.0 here, in order to make it easier to use that
          as a CV. If you need the raw number, multiply the output with 127. Note: as
          long as no CC message with the selected number happened, this output will be
          set to 0.
        cctrigger1 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger2 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger3 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        cctrigger4 (trigger):
          These outputs send a trigger whenever a CC event matching the corresponding
          ccnumber is processed. Some devices uses triggers in such a way – as events
          rather then indicating the change of a continous value. So if you set
          ccnumber2 = 17, the output cctrigger2 sends a trigger whenever CC#17 is
          received.
        notegate1 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate2 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate3 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate4 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate5 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate6 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate7 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate8 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate9 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate10 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate11 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate12 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate13 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate14 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate15 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        notegate16 (gate):
          Outputs a high gate whenever the corresponding note (which is selected by
          note1 through note16) is currently being played.
        pitchbend (cv):
          Outputs the current pitch bend value as a bipolar voltage. The range can be
          set with pitchbendrange.
        programchange (trigger):
          Sends a trigger whenever a MIDI program change message arrives. Just before
          sending the trigger sets program to the new program number (something from 0
          to 127). Note: This trigger is also being output when the program change
          messages sends the same program number as previously, i.e. if there is no
          actual change.
        program (integer):
          The number of the last program change. This starts at 0.
        bank (integer):
          Outputs the number of the currently selected bank – from 0 to 16384. MIDI
          defines the MSB of the bank to be changed with CC#0 and the LSB with CC#32.
          That means if you just use CC#0, you will only be able to select the banks 0,
          128, 256, and so on. As long as no bank select CC has been received, bank will
          output 0.
        modwheel (fraction):
          Output the current state of the mod wheel level – within the range from 0.0 to
          1.0. The mod wheel is changed by MIDI control change 1.
        volume (fraction):
          Outputs the current global volume as set by MIDI control change 7.
        portamento (gate):
          This output gives you access to the current state of the “portamento pedal”
          (MIDI CC 65). You can use it to enable an external slew circuit for creating
          portamento effects.
        soft (gate):
          This output gives you access to the current state of the “soft pedal” (MIDI CC
          67). It is 1 while the pedal is hold and 0 otherwise.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 560
    trs: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    usb: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    initialrunning: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    systemreset: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    channel: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    tuningmode: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    tuningpitch: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    transpose: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    holdvelocity: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitchbendrange: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    bendpitch: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    roundrobin: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    voiceallocation: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    notegap: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ccnumber1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    lowestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    highestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note5: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note6: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note7: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note8: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note9: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note10: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note11: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note12: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note13: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note14: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note15: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note16: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    clock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    clock8: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    clock8t: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    clock16: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    clock4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    midiclock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    start: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    continue_: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    stop: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    running: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    active: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitch1: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch2: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch3: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch4: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch5: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch6: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch7: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch8: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    velocity1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    gate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    trigger1: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger2: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger3: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger5: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger6: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger7: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    trigger8: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cc1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cctrigger1: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger2: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger3: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    notegate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate13: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate14: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate15: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate16: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitchbend: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    programchange: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    program: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    bank: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    modwheel: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    volume: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    portamento: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    soft: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )



@dataclass
class Midiout(DroidCircuit):
    """CV to MIDI converter.

    Args:
        channel (integer):
          Selects the MIDI channel to send the events on. Default is to send on channel
          1. There are 16 channels. Make sure that the receiving device listens to this
          (or to all) channels.
        usb (gate):
          Set usb = 1 if you want to send the MIDI output to the USB-C port. You can set
          trs = 1, as well, for sending the data to both outputs. If you don't use usb
          nor trs, the output will be sent to the TRS output only.
        trs (gate):
          This controls wether the MIDI data is sent via the TRS output of the X7. If
          you just want the TRS output, you don't need this, because that is the
          default. If you want the output both on USB and TRS, you need to set usb = 1
          and trs = 1 at the same time.
        pitch1 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch2 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch3 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch4 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch5 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch6 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch7 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        pitch8 (voltperoctave):
          Pitch of the notes to be played in modular style (1 V/octave). The range is
          from -2 V (MIDI note 0, usually C-2) to 8.583 V (MIDI note 127, usually G9).
          You can use up to eight pitch inputs for playing up to eight notes in
          parallel. pitch1 can be abbreviated with just pitch.
        gate1 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate2 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate3 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate4 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate5 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate6 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate7 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        gate8 (gate):
          A positive edge into the gate jacks trigger note on messages (starts the note
          at the pitch set by the corresponding pitch input). A negative edge ends the
          currently played note.
        velocity1 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity2 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity3 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity4 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity5 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity6 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity7 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        velocity8 (fraction):
          The velocities for the up to eight notes. The velocity value is just picked up
          at the start of the note (at the positive edge of the corresponding gate
          inputs. It ranges from 0.0 to 1.0. A value of 0.0 is practically the same as
          “note off”. The default velocity is 1.0.
        noteoffvelocity1 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity2 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity3 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity4 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity5 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity6 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity7 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        noteoffvelocity8 (fraction):
          MIDI also sends a velocity at the end of a note. The idea is to model the
          speed with which a key is being released. This is rarely used. If you don't
          use these jacks, the velocity for “note off” events is the same as that for
          “note on” events.
        pressure1 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure2 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure3 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure4 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure5 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure6 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure7 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        pressure8 (fraction):
          Sends key pressure events for individually played notes via the MIDI event
          “polyphonic key pressure” (this is not a CC!). These values are not processed
          at the time of note on/off events but all the time and can also change while a
          note is already being played. This corresponds to “aftertouch” key pressure on
          keyboards that have a pressure sensor per key.  If nothing is patched here, no
          pressure events are sent.
        channelpressure (fraction):
          Whenever this CV changes, sends a MIDI channel pressure event, also known as
          “aftertouch”. This corresponds to keyboards that just have one global pressure
          sensor and not one per key.  If nothing is patched here, no channel pressure
          events are sent.
        pitchstabilization (gate):
          Enables or disables pitch stabilization. It is on per default and can be
          disabled by setting this jack to 0. Pitch stabilization fixes timing issues
          where the input pitch needs some time for reaching the target pitch after a
          gate.
        triggerdelay (cv):
          Introduces a delay between in the incoming gate signal (just the positive
          edge) and the “note on” event. This can tackle the problem when your pitch
          input (sequencer etc.) needs some time after the gate in order to reach and
          stabilize the target pitch. The delay is specified in milliseconds, so a
          typical useful value would be 5 (5 ms). This is an alternative to the
          automatic pitchstabilization. Note: triggerdelay disables pitchstabilization,
          as long as that is not set to 1 explicitly. If both are used at the same time,
          the triggerdelay happens before the pitch stabilization. So it is a minimum
          delay.
        lowestnote (integer):
          With this input you can restrict the notes being played by setting a lower
          bound. In MIDI the notes range from 0 (C-2) to 127 (G9). By setting lowestnote
          to 24 (C0), all notes below this note are simply ignored. This allows for
          example for a keyboard split by using a second circuit with a highestnote of
          23. Note gates are not being affected by this bound.
        highestnote (integer):
          Sets an upper limit to the note being played, similar to lowestnote. Note
          gates are not being affected by this bound.
        notegate1 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate2 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate3 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate4 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate5 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate6 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate7 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate8 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate9 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate10 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate11 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate12 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate13 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate14 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate15 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        notegate16 (gate):
          You can define up to 16 notes that can be directly controlled with a dedicated
          gate. This is convenient for playing drum sounds directly from triggers and
          also for using DROID controllers as MIDI controllers. A trigger or gate to
          notegate1 will directly play the note whose pitch is set by note1.
        note1 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note2 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note3 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note4 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note5 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note6 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note7 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note8 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note9 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note10 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note11 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note12 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note13 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note14 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note15 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        note16 (integer):
          MIDI notes to played via notegate. The range is from 0 to 127.  Per default
          the notes are set to the MIDI notes 0, 1, 2 ... 15.
        notegatevelocity1 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity2 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity3 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity4 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity5 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity6 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity7 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity8 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity9 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity10 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity11 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity12 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity13 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity14 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity15 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        notegatevelocity16 (fraction):
          Here you can set the velocities use by the notegates. In order to keep it
          simple, this velocity is used for note on and note off events (nobody cares
          about the note off velocity anyway). If you do not use these jacks, the note
          gates will always use the maximum velocity.
        modwheel (fraction):
          Sets the current value of the modulation wheel. Any change here sends a midi
          CC#1 with a new value for the modulation wheel. The input range is 0.0 ... 1.0
          and will be converted into the MIDI range of 0 ... 127. Note: in future we
          might support CC#33, which is the LSB value of CC#1 and increases the
          resolution from 128 to 16384 different values, at the cost – however – of two
          additional bytes being sent.
        volume (fraction):
          Sets the volume of the target device. This is done by sending the MIDI CC#7
          (VOLUME MSB) and MIDI CC#39 (VOLUME LSB). Using these two CCs enables a 14 bit
          high resolution 16384 levels (not just 127). Some devices to not react to
          CC#39 and simply ignore the LSB (least significant byte). The volume CV ranges
          from 0.0 (silent) to 1.0 (the default).
        pitchbend (cv):
          Bends the pitches of all currently played notes up and down by a range that is
          configured or elsewhere defined by the device that plays our stuff. The range
          of this CV is -1.0 ... 1.0 for covering the maximum pitch bend range. Most
          times that range is two semitones up and down. This CV does not behave in a
          1V/oct way!
        pitchtracking (integer):
          Pitch tracking is an advanced feature that allows you to track continuous
          changes in the incoming pitch CV while the note is already playing. It does
          this by listening to the input CV and converting any change into a MIDI “pitch
          bend” change.  This feature has two limitations: First, there is just one
          global pitch bend value per channel, not one per note. So this feature only
          works in a monophonic situation. Only the value of pitch1 is being tracked.
          When you play more than one note per channel, funny things might probably
          happen. Also The maximum range is limited by the pitch bend range of your
          target device. That is usually preset to 2 semitones up and down. If you can
          increase it, please also adapt pitchbandrange so this circuit knows about it.
          Pitch tracking has two levels: pitchbandrange = 1 will alter the pitch of the
          current note within the maximum range of pitch bend and will clip any further
          changes. pitchbendrange = 2, in contrast, plays a new note if the current
          range is exceeded. Depending on your sound settings this “dent” might be
          audible or not.   0pitch tracking is off 1just use MIDI pitch bend 2use new
          note on larger changes   Note: When you use pitch tracking at the same time as
          pitchbend, both pitch alterations will add up.
        pitchbendrange (voltperoctave):
          Defines the range of the effect of pitch bend at the target device on a 1V/oct
          base. Note: You cannot change that actual range here. You just can make sure
          that this circuit has the correct assumption of that range.  If your target
          device has a configuration for extending the range, and you have set that for
          example to 1 octave, set pitchbendrange to 1 V. This allows pitchtracking to
          correctly adapt in-note pitch changes. Note: This has no effect on the
          pitchbend CV.
        ccnumber1 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber2 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber3 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber4 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber5 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber6 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber7 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        ccnumber8 (integer):
          Specifies up to eight different CC numbers that can be continuously updated
          via the corresponding cc1 through cc8 inputs. The value needs to be an integer
          number from 0 to 127.
        cc1 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc2 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc3 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc4 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc5 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc6 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc7 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cc8 (fraction):
          The current value of the CCs that are specified with ccnumber1 through
          ccnumber8. The range is always from 0.0 to 1.0 (which is mapped to the number
          0 to 127 on the MIDI wire).  If you don't patch anything here, no CC events
          will be sent, of course.
        cctrigger1 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger2 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger3 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger4 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger5 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger6 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger7 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        cctrigger8 (trigger):
          Usually midiout will send out a new CC event every time the input value of a
          CC has changed (with some rate limit in order not to to flood the MIDI
          stream).  When you use these inputs, an alternative method is enabled. Now CC
          events are created whenever a trigger arrives here. No more updates will be
          sent automatically.  This is useful for target devices that use CCs just as
          messages, i.e. as one time events and not for updating a continous value.
        updateccs (trigger):
          A trigger here sends an update for all CCs that you have in use (used ccX
          inputs).  Normally an update is just sent once initially and then when the
          input CV at one of the cc inputs changes its value. With the trigger you can
          force updates. This might be neccessary if the receiving device has lost
          memory of the current states of the CCs (e.g. due to a power cycle).  Note:
          Unlike the cctriggerX inputs, this trigger does not change the way the CC
          inputs work. It is just a hint for that forces one additonal update.
        delayinitialccs (cv):
          When the Droid starts it needs a short time until the X7 is operating and your
          PC / DAW is able to receive the MIDI events via USB. Initial CC updates during
          that short time period might get lost and you are missing the correct CC
          states (which are updated later only on changes).  In order to avoid that, the
          Droid wait a short time after starting before it sends the first CC events.
          That delay can be tuned here. It is a time in seconds.
        bank (integer):
          Selects the current “bank”. Some MIDI devices have more than 128 programs
          (i.e., patches, instruments, preset, etc). A MIDI Program Change message
          supports switching between only 128 programs. So, “Bank Select” (sometimes
          also called bank switch) is sometimes used to allow switching between groups
          of 128 programs. Bank select uses the MIDI CCs #0 (MSB) and #32 (LSB) together
          to form a number of 16384 different banks. The input value thus ranges from 1
          to 16384. Most devices, however, restrict themselves to just 128 banks and
          just use the MSB (CC#0). If that is the case, you need to set bank to 128 for
          bank 2, 256 for bank 3 and so on. This can be done by simply multiplying the
          actual bank number with 128.
        program (integer):
          Select the current “program”. This is a number from 1 to 128.
        programchange (trigger):
          A trigger here will send out a “program change” MIDI message even if the value
          of bank or program has not changed.
        start (trigger):
          If you send a trigger here, the MIDI message START will be emitted. Don't use
          this jack if you also use running. Note: START/STOP messages are not bound to
          a specific channel.
        stop (trigger):
          If you send a trigger here, the MIDI message STOP will be emitted. Don't use
          this jack if you also use running. Note: START/STOP messages are not bound to
          a specific channel.
        running (gate):
          This is an alternative to the jacks start and stop. It combines both into one
          “running” state. When this gate input goes high, a START message is sent, when
          it goes low a STOP message. So you can work with a state rather than with
          state changes. Note: START/STOP messages are not bound to a specific channel.
        systemreset (trigger):
          A trigger here will send the MIDI real-time message “RESET”, that is supposed
          to bring the device into some start state.
        allnotesoff (trigger):
          A trigger here will send the MIDI CC#123 “ALL NOTES OFF”, which is essentially
          the same as releasing all currently held keys.
        allsoundoff (trigger):
          A trigger here will send the MIDI CC#120 “ALL SOUND OFF”, which is supposed to
          make the device silent as soon as possible.
        damper (gate):
          This gate input simulates a hold or damper pedal. This is done via the CC#64.
          If the gate goes to high, a value of 127 is being sent, when it goes back to
          low, a value of 0. When the damper pedal is pressed, the device is supposed to
          hold all currently played notes and not react to any subsequent “NOTE OFF” of
          those notes as long as the pedal is held. When the pedal is released, all
          notes that had been held be the pedal should be released.
        portamento (gate):
          Controls the portamento pedal. The receiver is meant to activate some kind of
          glide effect as long as this gate is high.
        sostenuto (gate):
          This enables the sustain pedal. This is similar to but not exactly the same as
          the damper pedal as it just holds notes that are pressed while the pedal goes
          down.
        soft (gate):
          Controls the soft pedal. The receiving synth voice is meant to play notes
          softer while this pedal is hold down.
        legato (gate):
          Controls the legato pedal, which ties subsequent notes together.
        clock (trigger):
          If you feed a steady clock here, a MIDI clock signal will be derived from this
          and sent through the output wire. The MIDI beat clock or simply MIDI clock is
          defined to send pulses at 24 PPQN: 24 pulses per quarter note. One quarter
          note has four 16s, so the MIDI clock is running at 6 pulses per 16 note, and
          in the modular environment it is very common to work with 16 pulses as a
          master clock. So this clock jack is meant to retrieve a modular master clock,
          multiplies this by 6 and creates a MIDI clock from it.
        midiclock (trigger):
          This is an alternative to clock: don't use both at the same time. Here you can
          directly send the MIDI clock in 24 PPQN.
        activesensing (gate):
          This is a switch that disables or enables active sensing. This is a MIDI
          feature where a MIDI sender emits one message of the type “active sensing”
          every 300 ms. The receiver can use this in order to detect if the connection
          is still active and also immediately reset (und turn all sound off) if it is
          not. Active sensing is enabled per default. You can disable it here by setting
          activesensing = 0.  Note: If you have more than one midiout circuit sending to
          the same port, you should activate activesensing just for one of them in order
          to avoid useless duplicate MIDI events.
        updaterate (cv):
          Specifies the maximum rate at which continuous controllers like the CCs,
          volume, pitchbend and channelpressure are updated. This limitation is
          necessary in order not to flood the MIDI interface with too many updates
          because of just minimal changes. This rate is specified in update per second
          and the default is 50. A zero or negative value will completely stop all
          updates.  Note: depending on how many events are happening on your channel,
          fewer updates might be possible. MIDI over a classical cable is limited to
          3125 bytes per second. Events typically need 1, 2 or 3 bytes each.
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
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 664
    channel: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    usb: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    trs: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    pitch1: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch2: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch3: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch4: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch5: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch6: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch7: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    pitch8: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    gate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    gate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    velocity1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    velocity8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    noteoffvelocity8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pressure8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    channelpressure: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pitchstabilization: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    triggerdelay: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    lowestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    highestnote: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    notegate1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate13: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate14: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate15: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    notegate16: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    note1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note5: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note6: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note7: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note8: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note9: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note10: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note11: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note12: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note13: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note14: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note15: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    note16: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    notegatevelocity1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity9: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity10: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity11: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity12: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity13: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity14: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity15: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    notegatevelocity16: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    modwheel: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    volume: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    pitchbend: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    pitchtracking: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    pitchbendrange: Optional[str] = field(
            default=None,
            metadata=ctype.type_voltperoctave(ramsize=0)
    )
    ccnumber1: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber2: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber3: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber4: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber5: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber6: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber7: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    ccnumber8: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    cc1: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc2: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc3: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc4: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc5: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc6: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc7: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cc8: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    cctrigger1: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger2: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger3: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger4: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger5: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger6: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger7: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    cctrigger8: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    updateccs: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    delayinitialccs: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    bank: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    program: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    programchange: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    start: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    stop: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    running: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    systemreset: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    allnotesoff: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    allsoundoff: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    damper: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    portamento: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    sostenuto: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    soft: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    legato: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    clock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    midiclock: Optional[str] = field(
            default=None,
            metadata=ctype.type_trigger(ramsize=0)
    )
    activesensing: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    updaterate: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    select: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    selectat: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )



@dataclass
class Midithrough(DroidCircuit):
    """Forward MIDI events from input to one or more outputs.

    Args:
        fromtrs (integer):
          Selects a TRS port to use as input (3.5 mm jack). fromtrs = 0 disables TRS,
          fromtrs = 10 enables auto detection. See the manual of midiin for details on
          port selection.
        fromusb (integer):
          Selects a USB port to use as input. fromusb = 0 disables USB, fromusb = 10
          enables auto detection. See the manual of midiin for details on port
          selection.
        totrs (integer):
          Selects which TRS MIDI port to output to. See the manual of midiout for
          details on port selection.
        tousb (integer):
          Selects which USB MIDI port to output to. See the manual of midiout for
          details on port selection.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 240
    fromtrs: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    fromusb: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    totrs: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    tousb: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )



