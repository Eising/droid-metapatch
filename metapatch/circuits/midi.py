"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Firefacecontrol(DroidCircuit):
    """ Control a RME Fireface interface (experimental)

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

    _ramsize: int = 1088

    trs: str | None = Field(
        default=None,
        serialization_alias="trs",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": ""},
    )
    outputlevel1: str | None = Field(
        default=None,
        serialization_alias="outputlevel1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ol1"},
    )
    outputlevel2: str | None = Field(
        default=None,
        serialization_alias="outputlevel2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ol2"},
    )
    outputlevel3: str | None = Field(
        default=None,
        serialization_alias="outputlevel3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ol3"},
    )
    outputlevel4: str | None = Field(
        default=None,
        serialization_alias="outputlevel4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "ol4"},
    )
    outputlevel5: str | None = Field(
        default=None,
        serialization_alias="outputlevel5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol5"},
    )
    outputlevel6: str | None = Field(
        default=None,
        serialization_alias="outputlevel6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol6"},
    )
    outputlevel7: str | None = Field(
        default=None,
        serialization_alias="outputlevel7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol7"},
    )
    outputlevel8: str | None = Field(
        default=None,
        serialization_alias="outputlevel8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol8"},
    )
    outputlevel9: str | None = Field(
        default=None,
        serialization_alias="outputlevel9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol9"},
    )
    outputlevel10: str | None = Field(
        default=None,
        serialization_alias="outputlevel10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol10"},
    )
    outputlevel11: str | None = Field(
        default=None,
        serialization_alias="outputlevel11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol11"},
    )
    outputlevel12: str | None = Field(
        default=None,
        serialization_alias="outputlevel12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol12"},
    )
    outputlevel13: str | None = Field(
        default=None,
        serialization_alias="outputlevel13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol13"},
    )
    outputlevel14: str | None = Field(
        default=None,
        serialization_alias="outputlevel14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol14"},
    )
    outputlevel15: str | None = Field(
        default=None,
        serialization_alias="outputlevel15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol15"},
    )
    outputlevel16: str | None = Field(
        default=None,
        serialization_alias="outputlevel16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ol16"},
    )
    mainoutput: str | None = Field(
        default=None,
        serialization_alias="mainoutput",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "mo"},
    )
    phonesoutput1: str | None = Field(
        default=None,
        serialization_alias="phonesoutput1",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "po1"},
    )
    phonesoutput2: str | None = Field(
        default=None,
        serialization_alias="phonesoutput2",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "po2"},
    )
    outputmix1in1: str | None = Field(
        default=None,
        serialization_alias="outputmix1in1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o1i1"},
    )
    outputmix1in2: str | None = Field(
        default=None,
        serialization_alias="outputmix1in2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o1i2"},
    )
    outputmix1in3: str | None = Field(
        default=None,
        serialization_alias="outputmix1in3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o1i3"},
    )
    outputmix1in4: str | None = Field(
        default=None,
        serialization_alias="outputmix1in4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o1i4"},
    )
    outputmix1in5: str | None = Field(
        default=None,
        serialization_alias="outputmix1in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i5"},
    )
    outputmix1in6: str | None = Field(
        default=None,
        serialization_alias="outputmix1in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i6"},
    )
    outputmix1in7: str | None = Field(
        default=None,
        serialization_alias="outputmix1in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i7"},
    )
    outputmix1in8: str | None = Field(
        default=None,
        serialization_alias="outputmix1in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i8"},
    )
    outputmix1in9: str | None = Field(
        default=None,
        serialization_alias="outputmix1in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i9"},
    )
    outputmix1in10: str | None = Field(
        default=None,
        serialization_alias="outputmix1in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i10"},
    )
    outputmix1in11: str | None = Field(
        default=None,
        serialization_alias="outputmix1in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i11"},
    )
    outputmix1in12: str | None = Field(
        default=None,
        serialization_alias="outputmix1in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i12"},
    )
    outputmix1in13: str | None = Field(
        default=None,
        serialization_alias="outputmix1in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i13"},
    )
    outputmix1in14: str | None = Field(
        default=None,
        serialization_alias="outputmix1in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i14"},
    )
    outputmix1in15: str | None = Field(
        default=None,
        serialization_alias="outputmix1in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i15"},
    )
    outputmix1in16: str | None = Field(
        default=None,
        serialization_alias="outputmix1in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o1i16"},
    )
    outputmix2in1: str | None = Field(
        default=None,
        serialization_alias="outputmix2in1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o2i1"},
    )
    outputmix2in2: str | None = Field(
        default=None,
        serialization_alias="outputmix2in2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o2i2"},
    )
    outputmix2in3: str | None = Field(
        default=None,
        serialization_alias="outputmix2in3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o2i3"},
    )
    outputmix2in4: str | None = Field(
        default=None,
        serialization_alias="outputmix2in4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o2i4"},
    )
    outputmix2in5: str | None = Field(
        default=None,
        serialization_alias="outputmix2in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i5"},
    )
    outputmix2in6: str | None = Field(
        default=None,
        serialization_alias="outputmix2in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i6"},
    )
    outputmix2in7: str | None = Field(
        default=None,
        serialization_alias="outputmix2in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i7"},
    )
    outputmix2in8: str | None = Field(
        default=None,
        serialization_alias="outputmix2in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i8"},
    )
    outputmix2in9: str | None = Field(
        default=None,
        serialization_alias="outputmix2in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i9"},
    )
    outputmix2in10: str | None = Field(
        default=None,
        serialization_alias="outputmix2in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i10"},
    )
    outputmix2in11: str | None = Field(
        default=None,
        serialization_alias="outputmix2in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i11"},
    )
    outputmix2in12: str | None = Field(
        default=None,
        serialization_alias="outputmix2in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i12"},
    )
    outputmix2in13: str | None = Field(
        default=None,
        serialization_alias="outputmix2in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i13"},
    )
    outputmix2in14: str | None = Field(
        default=None,
        serialization_alias="outputmix2in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i14"},
    )
    outputmix2in15: str | None = Field(
        default=None,
        serialization_alias="outputmix2in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i15"},
    )
    outputmix2in16: str | None = Field(
        default=None,
        serialization_alias="outputmix2in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o2i16"},
    )
    outputmix3in1: str | None = Field(
        default=None,
        serialization_alias="outputmix3in1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o3i1"},
    )
    outputmix3in2: str | None = Field(
        default=None,
        serialization_alias="outputmix3in2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o3i2"},
    )
    outputmix3in3: str | None = Field(
        default=None,
        serialization_alias="outputmix3in3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o3i3"},
    )
    outputmix3in4: str | None = Field(
        default=None,
        serialization_alias="outputmix3in4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o3i4"},
    )
    outputmix3in5: str | None = Field(
        default=None,
        serialization_alias="outputmix3in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i5"},
    )
    outputmix3in6: str | None = Field(
        default=None,
        serialization_alias="outputmix3in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i6"},
    )
    outputmix3in7: str | None = Field(
        default=None,
        serialization_alias="outputmix3in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i7"},
    )
    outputmix3in8: str | None = Field(
        default=None,
        serialization_alias="outputmix3in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i8"},
    )
    outputmix3in9: str | None = Field(
        default=None,
        serialization_alias="outputmix3in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i9"},
    )
    outputmix3in10: str | None = Field(
        default=None,
        serialization_alias="outputmix3in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i10"},
    )
    outputmix3in11: str | None = Field(
        default=None,
        serialization_alias="outputmix3in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i11"},
    )
    outputmix3in12: str | None = Field(
        default=None,
        serialization_alias="outputmix3in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i12"},
    )
    outputmix3in13: str | None = Field(
        default=None,
        serialization_alias="outputmix3in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i13"},
    )
    outputmix3in14: str | None = Field(
        default=None,
        serialization_alias="outputmix3in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i14"},
    )
    outputmix3in15: str | None = Field(
        default=None,
        serialization_alias="outputmix3in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i15"},
    )
    outputmix3in16: str | None = Field(
        default=None,
        serialization_alias="outputmix3in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o3i16"},
    )
    outputmix4in1: str | None = Field(
        default=None,
        serialization_alias="outputmix4in1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o4i1"},
    )
    outputmix4in2: str | None = Field(
        default=None,
        serialization_alias="outputmix4in2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o4i2"},
    )
    outputmix4in3: str | None = Field(
        default=None,
        serialization_alias="outputmix4in3",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o4i3"},
    )
    outputmix4in4: str | None = Field(
        default=None,
        serialization_alias="outputmix4in4",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "o4i4"},
    )
    outputmix4in5: str | None = Field(
        default=None,
        serialization_alias="outputmix4in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i5"},
    )
    outputmix4in6: str | None = Field(
        default=None,
        serialization_alias="outputmix4in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i6"},
    )
    outputmix4in7: str | None = Field(
        default=None,
        serialization_alias="outputmix4in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i7"},
    )
    outputmix4in8: str | None = Field(
        default=None,
        serialization_alias="outputmix4in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i8"},
    )
    outputmix4in9: str | None = Field(
        default=None,
        serialization_alias="outputmix4in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i9"},
    )
    outputmix4in10: str | None = Field(
        default=None,
        serialization_alias="outputmix4in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i10"},
    )
    outputmix4in11: str | None = Field(
        default=None,
        serialization_alias="outputmix4in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i11"},
    )
    outputmix4in12: str | None = Field(
        default=None,
        serialization_alias="outputmix4in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i12"},
    )
    outputmix4in13: str | None = Field(
        default=None,
        serialization_alias="outputmix4in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i13"},
    )
    outputmix4in14: str | None = Field(
        default=None,
        serialization_alias="outputmix4in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i14"},
    )
    outputmix4in15: str | None = Field(
        default=None,
        serialization_alias="outputmix4in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i15"},
    )
    outputmix4in16: str | None = Field(
        default=None,
        serialization_alias="outputmix4in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o4i16"},
    )
    outputmix5in1: str | None = Field(
        default=None,
        serialization_alias="outputmix5in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i1"},
    )
    outputmix5in2: str | None = Field(
        default=None,
        serialization_alias="outputmix5in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i2"},
    )
    outputmix5in3: str | None = Field(
        default=None,
        serialization_alias="outputmix5in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i3"},
    )
    outputmix5in4: str | None = Field(
        default=None,
        serialization_alias="outputmix5in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i4"},
    )
    outputmix5in5: str | None = Field(
        default=None,
        serialization_alias="outputmix5in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i5"},
    )
    outputmix5in6: str | None = Field(
        default=None,
        serialization_alias="outputmix5in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i6"},
    )
    outputmix5in7: str | None = Field(
        default=None,
        serialization_alias="outputmix5in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i7"},
    )
    outputmix5in8: str | None = Field(
        default=None,
        serialization_alias="outputmix5in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i8"},
    )
    outputmix5in9: str | None = Field(
        default=None,
        serialization_alias="outputmix5in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i9"},
    )
    outputmix5in10: str | None = Field(
        default=None,
        serialization_alias="outputmix5in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i10"},
    )
    outputmix5in11: str | None = Field(
        default=None,
        serialization_alias="outputmix5in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i11"},
    )
    outputmix5in12: str | None = Field(
        default=None,
        serialization_alias="outputmix5in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i12"},
    )
    outputmix5in13: str | None = Field(
        default=None,
        serialization_alias="outputmix5in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i13"},
    )
    outputmix5in14: str | None = Field(
        default=None,
        serialization_alias="outputmix5in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i14"},
    )
    outputmix5in15: str | None = Field(
        default=None,
        serialization_alias="outputmix5in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i15"},
    )
    outputmix5in16: str | None = Field(
        default=None,
        serialization_alias="outputmix5in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o5i16"},
    )
    outputmix6in1: str | None = Field(
        default=None,
        serialization_alias="outputmix6in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i1"},
    )
    outputmix6in2: str | None = Field(
        default=None,
        serialization_alias="outputmix6in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i2"},
    )
    outputmix6in3: str | None = Field(
        default=None,
        serialization_alias="outputmix6in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i3"},
    )
    outputmix6in4: str | None = Field(
        default=None,
        serialization_alias="outputmix6in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i4"},
    )
    outputmix6in5: str | None = Field(
        default=None,
        serialization_alias="outputmix6in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i5"},
    )
    outputmix6in6: str | None = Field(
        default=None,
        serialization_alias="outputmix6in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i6"},
    )
    outputmix6in7: str | None = Field(
        default=None,
        serialization_alias="outputmix6in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i7"},
    )
    outputmix6in8: str | None = Field(
        default=None,
        serialization_alias="outputmix6in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i8"},
    )
    outputmix6in9: str | None = Field(
        default=None,
        serialization_alias="outputmix6in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i9"},
    )
    outputmix6in10: str | None = Field(
        default=None,
        serialization_alias="outputmix6in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i10"},
    )
    outputmix6in11: str | None = Field(
        default=None,
        serialization_alias="outputmix6in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i11"},
    )
    outputmix6in12: str | None = Field(
        default=None,
        serialization_alias="outputmix6in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i12"},
    )
    outputmix6in13: str | None = Field(
        default=None,
        serialization_alias="outputmix6in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i13"},
    )
    outputmix6in14: str | None = Field(
        default=None,
        serialization_alias="outputmix6in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i14"},
    )
    outputmix6in15: str | None = Field(
        default=None,
        serialization_alias="outputmix6in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i15"},
    )
    outputmix6in16: str | None = Field(
        default=None,
        serialization_alias="outputmix6in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o6i16"},
    )
    outputmix7in1: str | None = Field(
        default=None,
        serialization_alias="outputmix7in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i1"},
    )
    outputmix7in2: str | None = Field(
        default=None,
        serialization_alias="outputmix7in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i2"},
    )
    outputmix7in3: str | None = Field(
        default=None,
        serialization_alias="outputmix7in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i3"},
    )
    outputmix7in4: str | None = Field(
        default=None,
        serialization_alias="outputmix7in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i4"},
    )
    outputmix7in5: str | None = Field(
        default=None,
        serialization_alias="outputmix7in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i5"},
    )
    outputmix7in6: str | None = Field(
        default=None,
        serialization_alias="outputmix7in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i6"},
    )
    outputmix7in7: str | None = Field(
        default=None,
        serialization_alias="outputmix7in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i7"},
    )
    outputmix7in8: str | None = Field(
        default=None,
        serialization_alias="outputmix7in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i8"},
    )
    outputmix7in9: str | None = Field(
        default=None,
        serialization_alias="outputmix7in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i9"},
    )
    outputmix7in10: str | None = Field(
        default=None,
        serialization_alias="outputmix7in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i10"},
    )
    outputmix7in11: str | None = Field(
        default=None,
        serialization_alias="outputmix7in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i11"},
    )
    outputmix7in12: str | None = Field(
        default=None,
        serialization_alias="outputmix7in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i12"},
    )
    outputmix7in13: str | None = Field(
        default=None,
        serialization_alias="outputmix7in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i13"},
    )
    outputmix7in14: str | None = Field(
        default=None,
        serialization_alias="outputmix7in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i14"},
    )
    outputmix7in15: str | None = Field(
        default=None,
        serialization_alias="outputmix7in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i15"},
    )
    outputmix7in16: str | None = Field(
        default=None,
        serialization_alias="outputmix7in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o7i16"},
    )
    outputmix8in1: str | None = Field(
        default=None,
        serialization_alias="outputmix8in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i1"},
    )
    outputmix8in2: str | None = Field(
        default=None,
        serialization_alias="outputmix8in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i2"},
    )
    outputmix8in3: str | None = Field(
        default=None,
        serialization_alias="outputmix8in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i3"},
    )
    outputmix8in4: str | None = Field(
        default=None,
        serialization_alias="outputmix8in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i4"},
    )
    outputmix8in5: str | None = Field(
        default=None,
        serialization_alias="outputmix8in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i5"},
    )
    outputmix8in6: str | None = Field(
        default=None,
        serialization_alias="outputmix8in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i6"},
    )
    outputmix8in7: str | None = Field(
        default=None,
        serialization_alias="outputmix8in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i7"},
    )
    outputmix8in8: str | None = Field(
        default=None,
        serialization_alias="outputmix8in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i8"},
    )
    outputmix8in9: str | None = Field(
        default=None,
        serialization_alias="outputmix8in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i9"},
    )
    outputmix8in10: str | None = Field(
        default=None,
        serialization_alias="outputmix8in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i10"},
    )
    outputmix8in11: str | None = Field(
        default=None,
        serialization_alias="outputmix8in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i11"},
    )
    outputmix8in12: str | None = Field(
        default=None,
        serialization_alias="outputmix8in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i12"},
    )
    outputmix8in13: str | None = Field(
        default=None,
        serialization_alias="outputmix8in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i13"},
    )
    outputmix8in14: str | None = Field(
        default=None,
        serialization_alias="outputmix8in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i14"},
    )
    outputmix8in15: str | None = Field(
        default=None,
        serialization_alias="outputmix8in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i15"},
    )
    outputmix8in16: str | None = Field(
        default=None,
        serialization_alias="outputmix8in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o8i16"},
    )
    outputmix9in1: str | None = Field(
        default=None,
        serialization_alias="outputmix9in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i1"},
    )
    outputmix9in2: str | None = Field(
        default=None,
        serialization_alias="outputmix9in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i2"},
    )
    outputmix9in3: str | None = Field(
        default=None,
        serialization_alias="outputmix9in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i3"},
    )
    outputmix9in4: str | None = Field(
        default=None,
        serialization_alias="outputmix9in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i4"},
    )
    outputmix9in5: str | None = Field(
        default=None,
        serialization_alias="outputmix9in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i5"},
    )
    outputmix9in6: str | None = Field(
        default=None,
        serialization_alias="outputmix9in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i6"},
    )
    outputmix9in7: str | None = Field(
        default=None,
        serialization_alias="outputmix9in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i7"},
    )
    outputmix9in8: str | None = Field(
        default=None,
        serialization_alias="outputmix9in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i8"},
    )
    outputmix9in9: str | None = Field(
        default=None,
        serialization_alias="outputmix9in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i9"},
    )
    outputmix9in10: str | None = Field(
        default=None,
        serialization_alias="outputmix9in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i10"},
    )
    outputmix9in11: str | None = Field(
        default=None,
        serialization_alias="outputmix9in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i11"},
    )
    outputmix9in12: str | None = Field(
        default=None,
        serialization_alias="outputmix9in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i12"},
    )
    outputmix9in13: str | None = Field(
        default=None,
        serialization_alias="outputmix9in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i13"},
    )
    outputmix9in14: str | None = Field(
        default=None,
        serialization_alias="outputmix9in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i14"},
    )
    outputmix9in15: str | None = Field(
        default=None,
        serialization_alias="outputmix9in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i15"},
    )
    outputmix9in16: str | None = Field(
        default=None,
        serialization_alias="outputmix9in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o9i16"},
    )
    outputmix10in1: str | None = Field(
        default=None,
        serialization_alias="outputmix10in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i1"},
    )
    outputmix10in2: str | None = Field(
        default=None,
        serialization_alias="outputmix10in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i2"},
    )
    outputmix10in3: str | None = Field(
        default=None,
        serialization_alias="outputmix10in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i3"},
    )
    outputmix10in4: str | None = Field(
        default=None,
        serialization_alias="outputmix10in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i4"},
    )
    outputmix10in5: str | None = Field(
        default=None,
        serialization_alias="outputmix10in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i5"},
    )
    outputmix10in6: str | None = Field(
        default=None,
        serialization_alias="outputmix10in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i6"},
    )
    outputmix10in7: str | None = Field(
        default=None,
        serialization_alias="outputmix10in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i7"},
    )
    outputmix10in8: str | None = Field(
        default=None,
        serialization_alias="outputmix10in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i8"},
    )
    outputmix10in9: str | None = Field(
        default=None,
        serialization_alias="outputmix10in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i9"},
    )
    outputmix10in10: str | None = Field(
        default=None,
        serialization_alias="outputmix10in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i10"},
    )
    outputmix10in11: str | None = Field(
        default=None,
        serialization_alias="outputmix10in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i11"},
    )
    outputmix10in12: str | None = Field(
        default=None,
        serialization_alias="outputmix10in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i12"},
    )
    outputmix10in13: str | None = Field(
        default=None,
        serialization_alias="outputmix10in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i13"},
    )
    outputmix10in14: str | None = Field(
        default=None,
        serialization_alias="outputmix10in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i14"},
    )
    outputmix10in15: str | None = Field(
        default=None,
        serialization_alias="outputmix10in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i15"},
    )
    outputmix10in16: str | None = Field(
        default=None,
        serialization_alias="outputmix10in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o10i16"},
    )
    outputmix11in1: str | None = Field(
        default=None,
        serialization_alias="outputmix11in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i1"},
    )
    outputmix11in2: str | None = Field(
        default=None,
        serialization_alias="outputmix11in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i2"},
    )
    outputmix11in3: str | None = Field(
        default=None,
        serialization_alias="outputmix11in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i3"},
    )
    outputmix11in4: str | None = Field(
        default=None,
        serialization_alias="outputmix11in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i4"},
    )
    outputmix11in5: str | None = Field(
        default=None,
        serialization_alias="outputmix11in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i5"},
    )
    outputmix11in6: str | None = Field(
        default=None,
        serialization_alias="outputmix11in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i6"},
    )
    outputmix11in7: str | None = Field(
        default=None,
        serialization_alias="outputmix11in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i7"},
    )
    outputmix11in8: str | None = Field(
        default=None,
        serialization_alias="outputmix11in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i8"},
    )
    outputmix11in9: str | None = Field(
        default=None,
        serialization_alias="outputmix11in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i9"},
    )
    outputmix11in10: str | None = Field(
        default=None,
        serialization_alias="outputmix11in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i10"},
    )
    outputmix11in11: str | None = Field(
        default=None,
        serialization_alias="outputmix11in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i11"},
    )
    outputmix11in12: str | None = Field(
        default=None,
        serialization_alias="outputmix11in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i12"},
    )
    outputmix11in13: str | None = Field(
        default=None,
        serialization_alias="outputmix11in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i13"},
    )
    outputmix11in14: str | None = Field(
        default=None,
        serialization_alias="outputmix11in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i14"},
    )
    outputmix11in15: str | None = Field(
        default=None,
        serialization_alias="outputmix11in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i15"},
    )
    outputmix11in16: str | None = Field(
        default=None,
        serialization_alias="outputmix11in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o11i16"},
    )
    outputmix12in1: str | None = Field(
        default=None,
        serialization_alias="outputmix12in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i1"},
    )
    outputmix12in2: str | None = Field(
        default=None,
        serialization_alias="outputmix12in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i2"},
    )
    outputmix12in3: str | None = Field(
        default=None,
        serialization_alias="outputmix12in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i3"},
    )
    outputmix12in4: str | None = Field(
        default=None,
        serialization_alias="outputmix12in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i4"},
    )
    outputmix12in5: str | None = Field(
        default=None,
        serialization_alias="outputmix12in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i5"},
    )
    outputmix12in6: str | None = Field(
        default=None,
        serialization_alias="outputmix12in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i6"},
    )
    outputmix12in7: str | None = Field(
        default=None,
        serialization_alias="outputmix12in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i7"},
    )
    outputmix12in8: str | None = Field(
        default=None,
        serialization_alias="outputmix12in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i8"},
    )
    outputmix12in9: str | None = Field(
        default=None,
        serialization_alias="outputmix12in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i9"},
    )
    outputmix12in10: str | None = Field(
        default=None,
        serialization_alias="outputmix12in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i10"},
    )
    outputmix12in11: str | None = Field(
        default=None,
        serialization_alias="outputmix12in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i11"},
    )
    outputmix12in12: str | None = Field(
        default=None,
        serialization_alias="outputmix12in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i12"},
    )
    outputmix12in13: str | None = Field(
        default=None,
        serialization_alias="outputmix12in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i13"},
    )
    outputmix12in14: str | None = Field(
        default=None,
        serialization_alias="outputmix12in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i14"},
    )
    outputmix12in15: str | None = Field(
        default=None,
        serialization_alias="outputmix12in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i15"},
    )
    outputmix12in16: str | None = Field(
        default=None,
        serialization_alias="outputmix12in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o12i16"},
    )
    outputmix13in1: str | None = Field(
        default=None,
        serialization_alias="outputmix13in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i1"},
    )
    outputmix13in2: str | None = Field(
        default=None,
        serialization_alias="outputmix13in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i2"},
    )
    outputmix13in3: str | None = Field(
        default=None,
        serialization_alias="outputmix13in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i3"},
    )
    outputmix13in4: str | None = Field(
        default=None,
        serialization_alias="outputmix13in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i4"},
    )
    outputmix13in5: str | None = Field(
        default=None,
        serialization_alias="outputmix13in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i5"},
    )
    outputmix13in6: str | None = Field(
        default=None,
        serialization_alias="outputmix13in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i6"},
    )
    outputmix13in7: str | None = Field(
        default=None,
        serialization_alias="outputmix13in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i7"},
    )
    outputmix13in8: str | None = Field(
        default=None,
        serialization_alias="outputmix13in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i8"},
    )
    outputmix13in9: str | None = Field(
        default=None,
        serialization_alias="outputmix13in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i9"},
    )
    outputmix13in10: str | None = Field(
        default=None,
        serialization_alias="outputmix13in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i10"},
    )
    outputmix13in11: str | None = Field(
        default=None,
        serialization_alias="outputmix13in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i11"},
    )
    outputmix13in12: str | None = Field(
        default=None,
        serialization_alias="outputmix13in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i12"},
    )
    outputmix13in13: str | None = Field(
        default=None,
        serialization_alias="outputmix13in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i13"},
    )
    outputmix13in14: str | None = Field(
        default=None,
        serialization_alias="outputmix13in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i14"},
    )
    outputmix13in15: str | None = Field(
        default=None,
        serialization_alias="outputmix13in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i15"},
    )
    outputmix13in16: str | None = Field(
        default=None,
        serialization_alias="outputmix13in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o13i16"},
    )
    outputmix14in1: str | None = Field(
        default=None,
        serialization_alias="outputmix14in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i1"},
    )
    outputmix14in2: str | None = Field(
        default=None,
        serialization_alias="outputmix14in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i2"},
    )
    outputmix14in3: str | None = Field(
        default=None,
        serialization_alias="outputmix14in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i3"},
    )
    outputmix14in4: str | None = Field(
        default=None,
        serialization_alias="outputmix14in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i4"},
    )
    outputmix14in5: str | None = Field(
        default=None,
        serialization_alias="outputmix14in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i5"},
    )
    outputmix14in6: str | None = Field(
        default=None,
        serialization_alias="outputmix14in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i6"},
    )
    outputmix14in7: str | None = Field(
        default=None,
        serialization_alias="outputmix14in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i7"},
    )
    outputmix14in8: str | None = Field(
        default=None,
        serialization_alias="outputmix14in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i8"},
    )
    outputmix14in9: str | None = Field(
        default=None,
        serialization_alias="outputmix14in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i9"},
    )
    outputmix14in10: str | None = Field(
        default=None,
        serialization_alias="outputmix14in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i10"},
    )
    outputmix14in11: str | None = Field(
        default=None,
        serialization_alias="outputmix14in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i11"},
    )
    outputmix14in12: str | None = Field(
        default=None,
        serialization_alias="outputmix14in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i12"},
    )
    outputmix14in13: str | None = Field(
        default=None,
        serialization_alias="outputmix14in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i13"},
    )
    outputmix14in14: str | None = Field(
        default=None,
        serialization_alias="outputmix14in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i14"},
    )
    outputmix14in15: str | None = Field(
        default=None,
        serialization_alias="outputmix14in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i15"},
    )
    outputmix14in16: str | None = Field(
        default=None,
        serialization_alias="outputmix14in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o14i16"},
    )
    outputmix15in1: str | None = Field(
        default=None,
        serialization_alias="outputmix15in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i1"},
    )
    outputmix15in2: str | None = Field(
        default=None,
        serialization_alias="outputmix15in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i2"},
    )
    outputmix15in3: str | None = Field(
        default=None,
        serialization_alias="outputmix15in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i3"},
    )
    outputmix15in4: str | None = Field(
        default=None,
        serialization_alias="outputmix15in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i4"},
    )
    outputmix15in5: str | None = Field(
        default=None,
        serialization_alias="outputmix15in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i5"},
    )
    outputmix15in6: str | None = Field(
        default=None,
        serialization_alias="outputmix15in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i6"},
    )
    outputmix15in7: str | None = Field(
        default=None,
        serialization_alias="outputmix15in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i7"},
    )
    outputmix15in8: str | None = Field(
        default=None,
        serialization_alias="outputmix15in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i8"},
    )
    outputmix15in9: str | None = Field(
        default=None,
        serialization_alias="outputmix15in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i9"},
    )
    outputmix15in10: str | None = Field(
        default=None,
        serialization_alias="outputmix15in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i10"},
    )
    outputmix15in11: str | None = Field(
        default=None,
        serialization_alias="outputmix15in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i11"},
    )
    outputmix15in12: str | None = Field(
        default=None,
        serialization_alias="outputmix15in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i12"},
    )
    outputmix15in13: str | None = Field(
        default=None,
        serialization_alias="outputmix15in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i13"},
    )
    outputmix15in14: str | None = Field(
        default=None,
        serialization_alias="outputmix15in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i14"},
    )
    outputmix15in15: str | None = Field(
        default=None,
        serialization_alias="outputmix15in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i15"},
    )
    outputmix15in16: str | None = Field(
        default=None,
        serialization_alias="outputmix15in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o15i16"},
    )
    outputmix16in1: str | None = Field(
        default=None,
        serialization_alias="outputmix16in1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i1"},
    )
    outputmix16in2: str | None = Field(
        default=None,
        serialization_alias="outputmix16in2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i2"},
    )
    outputmix16in3: str | None = Field(
        default=None,
        serialization_alias="outputmix16in3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i3"},
    )
    outputmix16in4: str | None = Field(
        default=None,
        serialization_alias="outputmix16in4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i4"},
    )
    outputmix16in5: str | None = Field(
        default=None,
        serialization_alias="outputmix16in5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i5"},
    )
    outputmix16in6: str | None = Field(
        default=None,
        serialization_alias="outputmix16in6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i6"},
    )
    outputmix16in7: str | None = Field(
        default=None,
        serialization_alias="outputmix16in7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i7"},
    )
    outputmix16in8: str | None = Field(
        default=None,
        serialization_alias="outputmix16in8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i8"},
    )
    outputmix16in9: str | None = Field(
        default=None,
        serialization_alias="outputmix16in9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i9"},
    )
    outputmix16in10: str | None = Field(
        default=None,
        serialization_alias="outputmix16in10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i10"},
    )
    outputmix16in11: str | None = Field(
        default=None,
        serialization_alias="outputmix16in11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i11"},
    )
    outputmix16in12: str | None = Field(
        default=None,
        serialization_alias="outputmix16in12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i12"},
    )
    outputmix16in13: str | None = Field(
        default=None,
        serialization_alias="outputmix16in13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i13"},
    )
    outputmix16in14: str | None = Field(
        default=None,
        serialization_alias="outputmix16in14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i14"},
    )
    outputmix16in15: str | None = Field(
        default=None,
        serialization_alias="outputmix16in15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i15"},
    )
    outputmix16in16: str | None = Field(
        default=None,
        serialization_alias="outputmix16in16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "o16i16"},
    )
    postfader1: str | None = Field(
        default=None,
        serialization_alias="postfader1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf1"},
    )
    postfader2: str | None = Field(
        default=None,
        serialization_alias="postfader2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf2"},
    )
    postfader3: str | None = Field(
        default=None,
        serialization_alias="postfader3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf3"},
    )
    postfader4: str | None = Field(
        default=None,
        serialization_alias="postfader4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf4"},
    )
    postfader5: str | None = Field(
        default=None,
        serialization_alias="postfader5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf5"},
    )
    postfader6: str | None = Field(
        default=None,
        serialization_alias="postfader6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf6"},
    )
    postfader7: str | None = Field(
        default=None,
        serialization_alias="postfader7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf7"},
    )
    postfader8: str | None = Field(
        default=None,
        serialization_alias="postfader8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf8"},
    )
    postfader9: str | None = Field(
        default=None,
        serialization_alias="postfader9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf9"},
    )
    postfader10: str | None = Field(
        default=None,
        serialization_alias="postfader10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf10"},
    )
    postfader11: str | None = Field(
        default=None,
        serialization_alias="postfader11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf11"},
    )
    postfader12: str | None = Field(
        default=None,
        serialization_alias="postfader12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf12"},
    )
    postfader13: str | None = Field(
        default=None,
        serialization_alias="postfader13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf13"},
    )
    postfader14: str | None = Field(
        default=None,
        serialization_alias="postfader14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf14"},
    )
    postfader15: str | None = Field(
        default=None,
        serialization_alias="postfader15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf15"},
    )
    postfader16: str | None = Field(
        default=None,
        serialization_alias="postfader16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "pf16"},
    )
    pan1: str | None = Field(
        default=None,
        serialization_alias="pan1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p1"},
    )
    pan2: str | None = Field(
        default=None,
        serialization_alias="pan2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p2"},
    )
    pan3: str | None = Field(
        default=None,
        serialization_alias="pan3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p3"},
    )
    pan4: str | None = Field(
        default=None,
        serialization_alias="pan4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p4"},
    )
    pan5: str | None = Field(
        default=None,
        serialization_alias="pan5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p5"},
    )
    pan6: str | None = Field(
        default=None,
        serialization_alias="pan6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p6"},
    )
    pan7: str | None = Field(
        default=None,
        serialization_alias="pan7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p7"},
    )
    pan8: str | None = Field(
        default=None,
        serialization_alias="pan8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p8"},
    )
    pan9: str | None = Field(
        default=None,
        serialization_alias="pan9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p9"},
    )
    pan10: str | None = Field(
        default=None,
        serialization_alias="pan10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p10"},
    )
    pan11: str | None = Field(
        default=None,
        serialization_alias="pan11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p11"},
    )
    pan12: str | None = Field(
        default=None,
        serialization_alias="pan12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p12"},
    )
    pan13: str | None = Field(
        default=None,
        serialization_alias="pan13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p13"},
    )
    pan14: str | None = Field(
        default=None,
        serialization_alias="pan14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p14"},
    )
    pan15: str | None = Field(
        default=None,
        serialization_alias="pan15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p15"},
    )
    pan16: str | None = Field(
        default=None,
        serialization_alias="pan16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "p16"},
    )
    unmute1: str | None = Field(
        default=None,
        serialization_alias="unmute1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u1"},
    )
    unmute2: str | None = Field(
        default=None,
        serialization_alias="unmute2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u2"},
    )
    unmute3: str | None = Field(
        default=None,
        serialization_alias="unmute3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u3"},
    )
    unmute4: str | None = Field(
        default=None,
        serialization_alias="unmute4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u4"},
    )
    unmute5: str | None = Field(
        default=None,
        serialization_alias="unmute5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u5"},
    )
    unmute6: str | None = Field(
        default=None,
        serialization_alias="unmute6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u6"},
    )
    unmute7: str | None = Field(
        default=None,
        serialization_alias="unmute7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u7"},
    )
    unmute8: str | None = Field(
        default=None,
        serialization_alias="unmute8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u8"},
    )
    unmute9: str | None = Field(
        default=None,
        serialization_alias="unmute9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u9"},
    )
    unmute10: str | None = Field(
        default=None,
        serialization_alias="unmute10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u10"},
    )
    unmute11: str | None = Field(
        default=None,
        serialization_alias="unmute11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u11"},
    )
    unmute12: str | None = Field(
        default=None,
        serialization_alias="unmute12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u12"},
    )
    unmute13: str | None = Field(
        default=None,
        serialization_alias="unmute13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u13"},
    )
    unmute14: str | None = Field(
        default=None,
        serialization_alias="unmute14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u14"},
    )
    unmute15: str | None = Field(
        default=None,
        serialization_alias="unmute15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u15"},
    )
    unmute16: str | None = Field(
        default=None,
        serialization_alias="unmute16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "u16"},
    )
    update: str | None = Field(
        default=None,
        serialization_alias="update",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ud"},
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


class Midifileplayer(DroidCircuit):
    """ MIDI file player

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

    _ramsize: int = 6384

    file: str | None = Field(
        default=None,
        serialization_alias="file",
        json_schema_extra={"essential": 2, "type": "integer", "shortname": "f"},
    )
    track: str | None = Field(
        default=None,
        serialization_alias="track",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "tc"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
    )
    reset: str | None = Field(
        default=None,
        serialization_alias="reset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "r"},
    )
    loop: str | None = Field(
        default=None,
        serialization_alias="loop",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lo"},
    )
    end: str | None = Field(
        default=None,
        serialization_alias="end",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "e"},
    )
    speed: str | None = Field(
        default=None,
        serialization_alias="speed",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "sp"},
    )
    channel: str | None = Field(
        default=None,
        serialization_alias="channel",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ch"},
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
    holdvelocity: str | None = Field(
        default=None,
        serialization_alias="holdvelocity",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "hv"},
    )
    pitchbendrange: str | None = Field(
        default=None,
        serialization_alias="pitchbendrange",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "pbr"},
    )
    bendpitch: str | None = Field(
        default=None,
        serialization_alias="bendpitch",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bp"},
    )
    roundrobin: str | None = Field(
        default=None,
        serialization_alias="roundrobin",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "rr"},
    )
    voiceallocation: str | None = Field(
        default=None,
        serialization_alias="voiceallocation",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "va"},
    )
    notegap: str | None = Field(
        default=None,
        serialization_alias="notegap",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ngp"},
    )
    ccnumber1: str | None = Field(
        default=None,
        serialization_alias="ccnumber1",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn1"},
    )
    ccnumber2: str | None = Field(
        default=None,
        serialization_alias="ccnumber2",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn2"},
    )
    ccnumber3: str | None = Field(
        default=None,
        serialization_alias="ccnumber3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn3"},
    )
    ccnumber4: str | None = Field(
        default=None,
        serialization_alias="ccnumber4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn4"},
    )
    lowestnote: str | None = Field(
        default=None,
        serialization_alias="lowestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ln"},
    )
    highestnote: str | None = Field(
        default=None,
        serialization_alias="highestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "hn"},
    )
    note1: str | None = Field(
        default=None,
        serialization_alias="note1",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n1"},
    )
    note2: str | None = Field(
        default=None,
        serialization_alias="note2",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n2"},
    )
    note3: str | None = Field(
        default=None,
        serialization_alias="note3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n3"},
    )
    note4: str | None = Field(
        default=None,
        serialization_alias="note4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n4"},
    )
    note5: str | None = Field(
        default=None,
        serialization_alias="note5",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n5"},
    )
    note6: str | None = Field(
        default=None,
        serialization_alias="note6",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n6"},
    )
    note7: str | None = Field(
        default=None,
        serialization_alias="note7",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n7"},
    )
    note8: str | None = Field(
        default=None,
        serialization_alias="note8",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n8"},
    )
    note9: str | None = Field(
        default=None,
        serialization_alias="note9",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n9"},
    )
    note10: str | None = Field(
        default=None,
        serialization_alias="note10",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n10"},
    )
    note11: str | None = Field(
        default=None,
        serialization_alias="note11",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n11"},
    )
    note12: str | None = Field(
        default=None,
        serialization_alias="note12",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n12"},
    )
    note13: str | None = Field(
        default=None,
        serialization_alias="note13",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n13"},
    )
    note14: str | None = Field(
        default=None,
        serialization_alias="note14",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n14"},
    )
    note15: str | None = Field(
        default=None,
        serialization_alias="note15",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n15"},
    )
    note16: str | None = Field(
        default=None,
        serialization_alias="note16",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n16"},
    )
    clockout: str | None = Field(
        default=None,
        serialization_alias="clockout",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "co"},
    )
    midiclock: str | None = Field(
        default=None,
        serialization_alias="midiclock",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "mc"},
    )
    endoftrack: str | None = Field(
        default=None,
        serialization_alias="endoftrack",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "et"},
    )
    error: str | None = Field(
        default=None,
        serialization_alias="error",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "er"},
    )
    pitch1: str | None = Field(
        default=None,
        serialization_alias="pitch1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "p1"},
    )
    pitch2: str | None = Field(
        default=None,
        serialization_alias="pitch2",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p2"},
    )
    pitch3: str | None = Field(
        default=None,
        serialization_alias="pitch3",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p3"},
    )
    pitch4: str | None = Field(
        default=None,
        serialization_alias="pitch4",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p4"},
    )
    pitch5: str | None = Field(
        default=None,
        serialization_alias="pitch5",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p5"},
    )
    pitch6: str | None = Field(
        default=None,
        serialization_alias="pitch6",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p6"},
    )
    pitch7: str | None = Field(
        default=None,
        serialization_alias="pitch7",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p7"},
    )
    pitch8: str | None = Field(
        default=None,
        serialization_alias="pitch8",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p8"},
    )
    velocity1: str | None = Field(
        default=None,
        serialization_alias="velocity1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v1"},
    )
    velocity2: str | None = Field(
        default=None,
        serialization_alias="velocity2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v2"},
    )
    velocity3: str | None = Field(
        default=None,
        serialization_alias="velocity3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v3"},
    )
    velocity4: str | None = Field(
        default=None,
        serialization_alias="velocity4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v4"},
    )
    velocity5: str | None = Field(
        default=None,
        serialization_alias="velocity5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v5"},
    )
    velocity6: str | None = Field(
        default=None,
        serialization_alias="velocity6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v6"},
    )
    velocity7: str | None = Field(
        default=None,
        serialization_alias="velocity7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v7"},
    )
    velocity8: str | None = Field(
        default=None,
        serialization_alias="velocity8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v8"},
    )
    pressure1: str | None = Field(
        default=None,
        serialization_alias="pressure1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr1"},
    )
    pressure2: str | None = Field(
        default=None,
        serialization_alias="pressure2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr2"},
    )
    pressure3: str | None = Field(
        default=None,
        serialization_alias="pressure3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr3"},
    )
    pressure4: str | None = Field(
        default=None,
        serialization_alias="pressure4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr4"},
    )
    pressure5: str | None = Field(
        default=None,
        serialization_alias="pressure5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr5"},
    )
    pressure6: str | None = Field(
        default=None,
        serialization_alias="pressure6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr6"},
    )
    pressure7: str | None = Field(
        default=None,
        serialization_alias="pressure7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr7"},
    )
    pressure8: str | None = Field(
        default=None,
        serialization_alias="pressure8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr8"},
    )
    gate1: str | None = Field(
        default=None,
        serialization_alias="gate1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g1"},
    )
    gate2: str | None = Field(
        default=None,
        serialization_alias="gate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g2"},
    )
    gate3: str | None = Field(
        default=None,
        serialization_alias="gate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g3"},
    )
    gate4: str | None = Field(
        default=None,
        serialization_alias="gate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g4"},
    )
    gate5: str | None = Field(
        default=None,
        serialization_alias="gate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g5"},
    )
    gate6: str | None = Field(
        default=None,
        serialization_alias="gate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g6"},
    )
    gate7: str | None = Field(
        default=None,
        serialization_alias="gate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g7"},
    )
    gate8: str | None = Field(
        default=None,
        serialization_alias="gate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g8"},
    )
    trigger1: str | None = Field(
        default=None,
        serialization_alias="trigger1",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t1"},
    )
    trigger2: str | None = Field(
        default=None,
        serialization_alias="trigger2",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t2"},
    )
    trigger3: str | None = Field(
        default=None,
        serialization_alias="trigger3",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t3"},
    )
    trigger4: str | None = Field(
        default=None,
        serialization_alias="trigger4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t4"},
    )
    trigger5: str | None = Field(
        default=None,
        serialization_alias="trigger5",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t5"},
    )
    trigger6: str | None = Field(
        default=None,
        serialization_alias="trigger6",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t6"},
    )
    trigger7: str | None = Field(
        default=None,
        serialization_alias="trigger7",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t7"},
    )
    trigger8: str | None = Field(
        default=None,
        serialization_alias="trigger8",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t8"},
    )
    cc1: str | None = Field(
        default=None,
        serialization_alias="cc1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "1"},
    )
    cc2: str | None = Field(
        default=None,
        serialization_alias="cc2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "2"},
    )
    cc3: str | None = Field(
        default=None,
        serialization_alias="cc3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "3"},
    )
    cc4: str | None = Field(
        default=None,
        serialization_alias="cc4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "4"},
    )
    cctrigger1: str | None = Field(
        default=None,
        serialization_alias="cctrigger1",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct1"},
    )
    cctrigger2: str | None = Field(
        default=None,
        serialization_alias="cctrigger2",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct2"},
    )
    cctrigger3: str | None = Field(
        default=None,
        serialization_alias="cctrigger3",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct3"},
    )
    cctrigger4: str | None = Field(
        default=None,
        serialization_alias="cctrigger4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct4"},
    )
    notegate1: str | None = Field(
        default=None,
        serialization_alias="notegate1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng1"},
    )
    notegate2: str | None = Field(
        default=None,
        serialization_alias="notegate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng2"},
    )
    notegate3: str | None = Field(
        default=None,
        serialization_alias="notegate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng3"},
    )
    notegate4: str | None = Field(
        default=None,
        serialization_alias="notegate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng4"},
    )
    notegate5: str | None = Field(
        default=None,
        serialization_alias="notegate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng5"},
    )
    notegate6: str | None = Field(
        default=None,
        serialization_alias="notegate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng6"},
    )
    notegate7: str | None = Field(
        default=None,
        serialization_alias="notegate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng7"},
    )
    notegate8: str | None = Field(
        default=None,
        serialization_alias="notegate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng8"},
    )
    notegate9: str | None = Field(
        default=None,
        serialization_alias="notegate9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng9"},
    )
    notegate10: str | None = Field(
        default=None,
        serialization_alias="notegate10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng10"},
    )
    notegate11: str | None = Field(
        default=None,
        serialization_alias="notegate11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng11"},
    )
    notegate12: str | None = Field(
        default=None,
        serialization_alias="notegate12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng12"},
    )
    notegate13: str | None = Field(
        default=None,
        serialization_alias="notegate13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng13"},
    )
    notegate14: str | None = Field(
        default=None,
        serialization_alias="notegate14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng14"},
    )
    notegate15: str | None = Field(
        default=None,
        serialization_alias="notegate15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng15"},
    )
    notegate16: str | None = Field(
        default=None,
        serialization_alias="notegate16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng16"},
    )
    pitchbend: str | None = Field(
        default=None,
        serialization_alias="pitchbend",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pb"},
    )
    programchange: str | None = Field(
        default=None,
        serialization_alias="programchange",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pc"},
    )
    program: str | None = Field(
        default=None,
        serialization_alias="program",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pm"},
    )
    bank: str | None = Field(
        default=None,
        serialization_alias="bank",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ba"},
    )
    modwheel: str | None = Field(
        default=None,
        serialization_alias="modwheel",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "w"},
    )
    volume: str | None = Field(
        default=None,
        serialization_alias="volume",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "vo"},
    )
    portamento: str | None = Field(
        default=None,
        serialization_alias="portamento",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "po"},
    )
    soft: str | None = Field(
        default=None,
        serialization_alias="soft",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "so"},
    )


class Midiin(DroidCircuit):
    """ MIDI to CV converter

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
        continue (trigger):
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

    _ramsize: int = 560

    trs: str | None = Field(
        default=None,
        serialization_alias="trs",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": ""},
    )
    usb: str | None = Field(
        default=None,
        serialization_alias="usb",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": ""},
    )
    initialrunning: str | None = Field(
        default=None,
        serialization_alias="initialrunning",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ir"},
    )
    systemreset: str | None = Field(
        default=None,
        serialization_alias="systemreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sr"},
    )
    channel: str | None = Field(
        default=None,
        serialization_alias="channel",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "ch"},
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
    holdvelocity: str | None = Field(
        default=None,
        serialization_alias="holdvelocity",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "hv"},
    )
    pitchbendrange: str | None = Field(
        default=None,
        serialization_alias="pitchbendrange",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "pbr"},
    )
    bendpitch: str | None = Field(
        default=None,
        serialization_alias="bendpitch",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "bp"},
    )
    roundrobin: str | None = Field(
        default=None,
        serialization_alias="roundrobin",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "rr"},
    )
    voiceallocation: str | None = Field(
        default=None,
        serialization_alias="voiceallocation",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "va"},
    )
    notegap: str | None = Field(
        default=None,
        serialization_alias="notegap",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ngp"},
    )
    ccnumber1: str | None = Field(
        default=None,
        serialization_alias="ccnumber1",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn1"},
    )
    ccnumber2: str | None = Field(
        default=None,
        serialization_alias="ccnumber2",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn2"},
    )
    ccnumber3: str | None = Field(
        default=None,
        serialization_alias="ccnumber3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn3"},
    )
    ccnumber4: str | None = Field(
        default=None,
        serialization_alias="ccnumber4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn4"},
    )
    lowestnote: str | None = Field(
        default=None,
        serialization_alias="lowestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ln"},
    )
    highestnote: str | None = Field(
        default=None,
        serialization_alias="highestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "hn"},
    )
    note1: str | None = Field(
        default=None,
        serialization_alias="note1",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n1"},
    )
    note2: str | None = Field(
        default=None,
        serialization_alias="note2",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n2"},
    )
    note3: str | None = Field(
        default=None,
        serialization_alias="note3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n3"},
    )
    note4: str | None = Field(
        default=None,
        serialization_alias="note4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n4"},
    )
    note5: str | None = Field(
        default=None,
        serialization_alias="note5",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n5"},
    )
    note6: str | None = Field(
        default=None,
        serialization_alias="note6",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n6"},
    )
    note7: str | None = Field(
        default=None,
        serialization_alias="note7",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n7"},
    )
    note8: str | None = Field(
        default=None,
        serialization_alias="note8",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n8"},
    )
    note9: str | None = Field(
        default=None,
        serialization_alias="note9",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n9"},
    )
    note10: str | None = Field(
        default=None,
        serialization_alias="note10",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n10"},
    )
    note11: str | None = Field(
        default=None,
        serialization_alias="note11",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n11"},
    )
    note12: str | None = Field(
        default=None,
        serialization_alias="note12",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n12"},
    )
    note13: str | None = Field(
        default=None,
        serialization_alias="note13",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n13"},
    )
    note14: str | None = Field(
        default=None,
        serialization_alias="note14",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n14"},
    )
    note15: str | None = Field(
        default=None,
        serialization_alias="note15",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n15"},
    )
    note16: str | None = Field(
        default=None,
        serialization_alias="note16",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n16"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
    )
    clock8: str | None = Field(
        default=None,
        serialization_alias="clock8",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c8"},
    )
    clock8t: str | None = Field(
        default=None,
        serialization_alias="clock8t",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c8t"},
    )
    clock16: str | None = Field(
        default=None,
        serialization_alias="clock16",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c16"},
    )
    clock4: str | None = Field(
        default=None,
        serialization_alias="clock4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "c4"},
    )
    midiclock: str | None = Field(
        default=None,
        serialization_alias="midiclock",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "mc"},
    )
    start: str | None = Field(
        default=None,
        serialization_alias="start",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "st"},
    )
    continue_: str | None = Field(
        default=None,
        serialization_alias="continue",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "co"},
    )
    stop: str | None = Field(
        default=None,
        serialization_alias="stop",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "sp"},
    )
    running: str | None = Field(
        default=None,
        serialization_alias="running",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "ru"},
    )
    active: str | None = Field(
        default=None,
        serialization_alias="active",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "a"},
    )
    pitch1: str | None = Field(
        default=None,
        serialization_alias="pitch1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "p1"},
    )
    pitch2: str | None = Field(
        default=None,
        serialization_alias="pitch2",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p2"},
    )
    pitch3: str | None = Field(
        default=None,
        serialization_alias="pitch3",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p3"},
    )
    pitch4: str | None = Field(
        default=None,
        serialization_alias="pitch4",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p4"},
    )
    pitch5: str | None = Field(
        default=None,
        serialization_alias="pitch5",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p5"},
    )
    pitch6: str | None = Field(
        default=None,
        serialization_alias="pitch6",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p6"},
    )
    pitch7: str | None = Field(
        default=None,
        serialization_alias="pitch7",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p7"},
    )
    pitch8: str | None = Field(
        default=None,
        serialization_alias="pitch8",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p8"},
    )
    velocity1: str | None = Field(
        default=None,
        serialization_alias="velocity1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v1"},
    )
    velocity2: str | None = Field(
        default=None,
        serialization_alias="velocity2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v2"},
    )
    velocity3: str | None = Field(
        default=None,
        serialization_alias="velocity3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v3"},
    )
    velocity4: str | None = Field(
        default=None,
        serialization_alias="velocity4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v4"},
    )
    velocity5: str | None = Field(
        default=None,
        serialization_alias="velocity5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v5"},
    )
    velocity6: str | None = Field(
        default=None,
        serialization_alias="velocity6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v6"},
    )
    velocity7: str | None = Field(
        default=None,
        serialization_alias="velocity7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v7"},
    )
    velocity8: str | None = Field(
        default=None,
        serialization_alias="velocity8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v8"},
    )
    pressure1: str | None = Field(
        default=None,
        serialization_alias="pressure1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr1"},
    )
    pressure2: str | None = Field(
        default=None,
        serialization_alias="pressure2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr2"},
    )
    pressure3: str | None = Field(
        default=None,
        serialization_alias="pressure3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr3"},
    )
    pressure4: str | None = Field(
        default=None,
        serialization_alias="pressure4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr4"},
    )
    pressure5: str | None = Field(
        default=None,
        serialization_alias="pressure5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr5"},
    )
    pressure6: str | None = Field(
        default=None,
        serialization_alias="pressure6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr6"},
    )
    pressure7: str | None = Field(
        default=None,
        serialization_alias="pressure7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr7"},
    )
    pressure8: str | None = Field(
        default=None,
        serialization_alias="pressure8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr8"},
    )
    gate1: str | None = Field(
        default=None,
        serialization_alias="gate1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g1"},
    )
    gate2: str | None = Field(
        default=None,
        serialization_alias="gate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g2"},
    )
    gate3: str | None = Field(
        default=None,
        serialization_alias="gate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g3"},
    )
    gate4: str | None = Field(
        default=None,
        serialization_alias="gate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g4"},
    )
    gate5: str | None = Field(
        default=None,
        serialization_alias="gate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g5"},
    )
    gate6: str | None = Field(
        default=None,
        serialization_alias="gate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g6"},
    )
    gate7: str | None = Field(
        default=None,
        serialization_alias="gate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g7"},
    )
    gate8: str | None = Field(
        default=None,
        serialization_alias="gate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g8"},
    )
    trigger1: str | None = Field(
        default=None,
        serialization_alias="trigger1",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t1"},
    )
    trigger2: str | None = Field(
        default=None,
        serialization_alias="trigger2",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t2"},
    )
    trigger3: str | None = Field(
        default=None,
        serialization_alias="trigger3",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t3"},
    )
    trigger4: str | None = Field(
        default=None,
        serialization_alias="trigger4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t4"},
    )
    trigger5: str | None = Field(
        default=None,
        serialization_alias="trigger5",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t5"},
    )
    trigger6: str | None = Field(
        default=None,
        serialization_alias="trigger6",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t6"},
    )
    trigger7: str | None = Field(
        default=None,
        serialization_alias="trigger7",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t7"},
    )
    trigger8: str | None = Field(
        default=None,
        serialization_alias="trigger8",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "t8"},
    )
    cc1: str | None = Field(
        default=None,
        serialization_alias="cc1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "1"},
    )
    cc2: str | None = Field(
        default=None,
        serialization_alias="cc2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "2"},
    )
    cc3: str | None = Field(
        default=None,
        serialization_alias="cc3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "3"},
    )
    cc4: str | None = Field(
        default=None,
        serialization_alias="cc4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "4"},
    )
    cctrigger1: str | None = Field(
        default=None,
        serialization_alias="cctrigger1",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct1"},
    )
    cctrigger2: str | None = Field(
        default=None,
        serialization_alias="cctrigger2",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct2"},
    )
    cctrigger3: str | None = Field(
        default=None,
        serialization_alias="cctrigger3",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct3"},
    )
    cctrigger4: str | None = Field(
        default=None,
        serialization_alias="cctrigger4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct4"},
    )
    notegate1: str | None = Field(
        default=None,
        serialization_alias="notegate1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng1"},
    )
    notegate2: str | None = Field(
        default=None,
        serialization_alias="notegate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng2"},
    )
    notegate3: str | None = Field(
        default=None,
        serialization_alias="notegate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng3"},
    )
    notegate4: str | None = Field(
        default=None,
        serialization_alias="notegate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng4"},
    )
    notegate5: str | None = Field(
        default=None,
        serialization_alias="notegate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng5"},
    )
    notegate6: str | None = Field(
        default=None,
        serialization_alias="notegate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng6"},
    )
    notegate7: str | None = Field(
        default=None,
        serialization_alias="notegate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng7"},
    )
    notegate8: str | None = Field(
        default=None,
        serialization_alias="notegate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng8"},
    )
    notegate9: str | None = Field(
        default=None,
        serialization_alias="notegate9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng9"},
    )
    notegate10: str | None = Field(
        default=None,
        serialization_alias="notegate10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng10"},
    )
    notegate11: str | None = Field(
        default=None,
        serialization_alias="notegate11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng11"},
    )
    notegate12: str | None = Field(
        default=None,
        serialization_alias="notegate12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng12"},
    )
    notegate13: str | None = Field(
        default=None,
        serialization_alias="notegate13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng13"},
    )
    notegate14: str | None = Field(
        default=None,
        serialization_alias="notegate14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng14"},
    )
    notegate15: str | None = Field(
        default=None,
        serialization_alias="notegate15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng15"},
    )
    notegate16: str | None = Field(
        default=None,
        serialization_alias="notegate16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng16"},
    )
    pitchbend: str | None = Field(
        default=None,
        serialization_alias="pitchbend",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pb"},
    )
    programchange: str | None = Field(
        default=None,
        serialization_alias="programchange",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pc"},
    )
    program: str | None = Field(
        default=None,
        serialization_alias="program",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pm"},
    )
    bank: str | None = Field(
        default=None,
        serialization_alias="bank",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ba"},
    )
    modwheel: str | None = Field(
        default=None,
        serialization_alias="modwheel",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "w"},
    )
    volume: str | None = Field(
        default=None,
        serialization_alias="volume",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "vo"},
    )
    portamento: str | None = Field(
        default=None,
        serialization_alias="portamento",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "po"},
    )
    soft: str | None = Field(
        default=None,
        serialization_alias="soft",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "so"},
    )


class Midiout(DroidCircuit):
    """ CV to MIDI converter

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

    _ramsize: int = 664

    channel: str | None = Field(
        default=None,
        serialization_alias="channel",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ch"},
    )
    usb: str | None = Field(
        default=None,
        serialization_alias="usb",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": ""},
    )
    trs: str | None = Field(
        default=None,
        serialization_alias="trs",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": ""},
    )
    pitch1: str | None = Field(
        default=None,
        serialization_alias="pitch1",
        json_schema_extra={"essential": 2, "type": "voltperoctave", "shortname": "p1"},
    )
    pitch2: str | None = Field(
        default=None,
        serialization_alias="pitch2",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p2"},
    )
    pitch3: str | None = Field(
        default=None,
        serialization_alias="pitch3",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p3"},
    )
    pitch4: str | None = Field(
        default=None,
        serialization_alias="pitch4",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p4"},
    )
    pitch5: str | None = Field(
        default=None,
        serialization_alias="pitch5",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p5"},
    )
    pitch6: str | None = Field(
        default=None,
        serialization_alias="pitch6",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p6"},
    )
    pitch7: str | None = Field(
        default=None,
        serialization_alias="pitch7",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p7"},
    )
    pitch8: str | None = Field(
        default=None,
        serialization_alias="pitch8",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "p8"},
    )
    gate1: str | None = Field(
        default=None,
        serialization_alias="gate1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "g1"},
    )
    gate2: str | None = Field(
        default=None,
        serialization_alias="gate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g2"},
    )
    gate3: str | None = Field(
        default=None,
        serialization_alias="gate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g3"},
    )
    gate4: str | None = Field(
        default=None,
        serialization_alias="gate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g4"},
    )
    gate5: str | None = Field(
        default=None,
        serialization_alias="gate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g5"},
    )
    gate6: str | None = Field(
        default=None,
        serialization_alias="gate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g6"},
    )
    gate7: str | None = Field(
        default=None,
        serialization_alias="gate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g7"},
    )
    gate8: str | None = Field(
        default=None,
        serialization_alias="gate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "g8"},
    )
    velocity1: str | None = Field(
        default=None,
        serialization_alias="velocity1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "v1"},
    )
    velocity2: str | None = Field(
        default=None,
        serialization_alias="velocity2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v2"},
    )
    velocity3: str | None = Field(
        default=None,
        serialization_alias="velocity3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v3"},
    )
    velocity4: str | None = Field(
        default=None,
        serialization_alias="velocity4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v4"},
    )
    velocity5: str | None = Field(
        default=None,
        serialization_alias="velocity5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v5"},
    )
    velocity6: str | None = Field(
        default=None,
        serialization_alias="velocity6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v6"},
    )
    velocity7: str | None = Field(
        default=None,
        serialization_alias="velocity7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v7"},
    )
    velocity8: str | None = Field(
        default=None,
        serialization_alias="velocity8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "v8"},
    )
    noteoffvelocity1: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv1"},
    )
    noteoffvelocity2: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv2"},
    )
    noteoffvelocity3: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv3"},
    )
    noteoffvelocity4: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv4"},
    )
    noteoffvelocity5: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv5"},
    )
    noteoffvelocity6: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv6"},
    )
    noteoffvelocity7: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv7"},
    )
    noteoffvelocity8: str | None = Field(
        default=None,
        serialization_alias="noteoffvelocity8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "nv8"},
    )
    pressure1: str | None = Field(
        default=None,
        serialization_alias="pressure1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr1"},
    )
    pressure2: str | None = Field(
        default=None,
        serialization_alias="pressure2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr2"},
    )
    pressure3: str | None = Field(
        default=None,
        serialization_alias="pressure3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr3"},
    )
    pressure4: str | None = Field(
        default=None,
        serialization_alias="pressure4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr4"},
    )
    pressure5: str | None = Field(
        default=None,
        serialization_alias="pressure5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr5"},
    )
    pressure6: str | None = Field(
        default=None,
        serialization_alias="pressure6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr6"},
    )
    pressure7: str | None = Field(
        default=None,
        serialization_alias="pressure7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr7"},
    )
    pressure8: str | None = Field(
        default=None,
        serialization_alias="pressure8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "pr8"},
    )
    channelpressure: str | None = Field(
        default=None,
        serialization_alias="channelpressure",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "cp"},
    )
    pitchstabilization: str | None = Field(
        default=None,
        serialization_alias="pitchstabilization",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ps"},
    )
    triggerdelay: str | None = Field(
        default=None,
        serialization_alias="triggerdelay",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "td"},
    )
    lowestnote: str | None = Field(
        default=None,
        serialization_alias="lowestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ln"},
    )
    highestnote: str | None = Field(
        default=None,
        serialization_alias="highestnote",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "hn"},
    )
    notegate1: str | None = Field(
        default=None,
        serialization_alias="notegate1",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng1"},
    )
    notegate2: str | None = Field(
        default=None,
        serialization_alias="notegate2",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng2"},
    )
    notegate3: str | None = Field(
        default=None,
        serialization_alias="notegate3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng3"},
    )
    notegate4: str | None = Field(
        default=None,
        serialization_alias="notegate4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng4"},
    )
    notegate5: str | None = Field(
        default=None,
        serialization_alias="notegate5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng5"},
    )
    notegate6: str | None = Field(
        default=None,
        serialization_alias="notegate6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng6"},
    )
    notegate7: str | None = Field(
        default=None,
        serialization_alias="notegate7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng7"},
    )
    notegate8: str | None = Field(
        default=None,
        serialization_alias="notegate8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng8"},
    )
    notegate9: str | None = Field(
        default=None,
        serialization_alias="notegate9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng9"},
    )
    notegate10: str | None = Field(
        default=None,
        serialization_alias="notegate10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng10"},
    )
    notegate11: str | None = Field(
        default=None,
        serialization_alias="notegate11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng11"},
    )
    notegate12: str | None = Field(
        default=None,
        serialization_alias="notegate12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng12"},
    )
    notegate13: str | None = Field(
        default=None,
        serialization_alias="notegate13",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng13"},
    )
    notegate14: str | None = Field(
        default=None,
        serialization_alias="notegate14",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng14"},
    )
    notegate15: str | None = Field(
        default=None,
        serialization_alias="notegate15",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng15"},
    )
    notegate16: str | None = Field(
        default=None,
        serialization_alias="notegate16",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "ng16"},
    )
    note1: str | None = Field(
        default=None,
        serialization_alias="note1",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n1"},
    )
    note2: str | None = Field(
        default=None,
        serialization_alias="note2",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n2"},
    )
    note3: str | None = Field(
        default=None,
        serialization_alias="note3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n3"},
    )
    note4: str | None = Field(
        default=None,
        serialization_alias="note4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n4"},
    )
    note5: str | None = Field(
        default=None,
        serialization_alias="note5",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n5"},
    )
    note6: str | None = Field(
        default=None,
        serialization_alias="note6",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n6"},
    )
    note7: str | None = Field(
        default=None,
        serialization_alias="note7",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n7"},
    )
    note8: str | None = Field(
        default=None,
        serialization_alias="note8",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n8"},
    )
    note9: str | None = Field(
        default=None,
        serialization_alias="note9",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n9"},
    )
    note10: str | None = Field(
        default=None,
        serialization_alias="note10",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n10"},
    )
    note11: str | None = Field(
        default=None,
        serialization_alias="note11",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n11"},
    )
    note12: str | None = Field(
        default=None,
        serialization_alias="note12",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n12"},
    )
    note13: str | None = Field(
        default=None,
        serialization_alias="note13",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n13"},
    )
    note14: str | None = Field(
        default=None,
        serialization_alias="note14",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n14"},
    )
    note15: str | None = Field(
        default=None,
        serialization_alias="note15",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n15"},
    )
    note16: str | None = Field(
        default=None,
        serialization_alias="note16",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "n16"},
    )
    notegatevelocity1: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity1",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv1"},
    )
    notegatevelocity2: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity2",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv2"},
    )
    notegatevelocity3: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv3"},
    )
    notegatevelocity4: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv4"},
    )
    notegatevelocity5: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv5"},
    )
    notegatevelocity6: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv6"},
    )
    notegatevelocity7: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv7"},
    )
    notegatevelocity8: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv8"},
    )
    notegatevelocity9: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity9",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv9"},
    )
    notegatevelocity10: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity10",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv10"},
    )
    notegatevelocity11: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity11",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv11"},
    )
    notegatevelocity12: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity12",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv12"},
    )
    notegatevelocity13: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity13",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv13"},
    )
    notegatevelocity14: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity14",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv14"},
    )
    notegatevelocity15: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity15",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv15"},
    )
    notegatevelocity16: str | None = Field(
        default=None,
        serialization_alias="notegatevelocity16",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "ngv16"},
    )
    modwheel: str | None = Field(
        default=None,
        serialization_alias="modwheel",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "w"},
    )
    volume: str | None = Field(
        default=None,
        serialization_alias="volume",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "vo"},
    )
    pitchbend: str | None = Field(
        default=None,
        serialization_alias="pitchbend",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pb"},
    )
    pitchtracking: str | None = Field(
        default=None,
        serialization_alias="pitchtracking",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pt"},
    )
    pitchbendrange: str | None = Field(
        default=None,
        serialization_alias="pitchbendrange",
        json_schema_extra={"essential": 0, "type": "voltperoctave", "shortname": "pbr"},
    )
    ccnumber1: str | None = Field(
        default=None,
        serialization_alias="ccnumber1",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn1"},
    )
    ccnumber2: str | None = Field(
        default=None,
        serialization_alias="ccnumber2",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "cn2"},
    )
    ccnumber3: str | None = Field(
        default=None,
        serialization_alias="ccnumber3",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn3"},
    )
    ccnumber4: str | None = Field(
        default=None,
        serialization_alias="ccnumber4",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn4"},
    )
    ccnumber5: str | None = Field(
        default=None,
        serialization_alias="ccnumber5",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn5"},
    )
    ccnumber6: str | None = Field(
        default=None,
        serialization_alias="ccnumber6",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn6"},
    )
    ccnumber7: str | None = Field(
        default=None,
        serialization_alias="ccnumber7",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn7"},
    )
    ccnumber8: str | None = Field(
        default=None,
        serialization_alias="ccnumber8",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "cn8"},
    )
    cc1: str | None = Field(
        default=None,
        serialization_alias="cc1",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "1"},
    )
    cc2: str | None = Field(
        default=None,
        serialization_alias="cc2",
        json_schema_extra={"essential": 1, "type": "fraction", "shortname": "2"},
    )
    cc3: str | None = Field(
        default=None,
        serialization_alias="cc3",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "3"},
    )
    cc4: str | None = Field(
        default=None,
        serialization_alias="cc4",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "4"},
    )
    cc5: str | None = Field(
        default=None,
        serialization_alias="cc5",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "5"},
    )
    cc6: str | None = Field(
        default=None,
        serialization_alias="cc6",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "6"},
    )
    cc7: str | None = Field(
        default=None,
        serialization_alias="cc7",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "7"},
    )
    cc8: str | None = Field(
        default=None,
        serialization_alias="cc8",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "8"},
    )
    cctrigger1: str | None = Field(
        default=None,
        serialization_alias="cctrigger1",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct1"},
    )
    cctrigger2: str | None = Field(
        default=None,
        serialization_alias="cctrigger2",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct2"},
    )
    cctrigger3: str | None = Field(
        default=None,
        serialization_alias="cctrigger3",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct3"},
    )
    cctrigger4: str | None = Field(
        default=None,
        serialization_alias="cctrigger4",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct4"},
    )
    cctrigger5: str | None = Field(
        default=None,
        serialization_alias="cctrigger5",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct5"},
    )
    cctrigger6: str | None = Field(
        default=None,
        serialization_alias="cctrigger6",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct6"},
    )
    cctrigger7: str | None = Field(
        default=None,
        serialization_alias="cctrigger7",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct7"},
    )
    cctrigger8: str | None = Field(
        default=None,
        serialization_alias="cctrigger8",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ct8"},
    )
    updateccs: str | None = Field(
        default=None,
        serialization_alias="updateccs",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "uc"},
    )
    delayinitialccs: str | None = Field(
        default=None,
        serialization_alias="delayinitialccs",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "dc"},
    )
    bank: str | None = Field(
        default=None,
        serialization_alias="bank",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ba"},
    )
    program: str | None = Field(
        default=None,
        serialization_alias="program",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "pm"},
    )
    programchange: str | None = Field(
        default=None,
        serialization_alias="programchange",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "pc"},
    )
    start: str | None = Field(
        default=None,
        serialization_alias="start",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "st"},
    )
    stop: str | None = Field(
        default=None,
        serialization_alias="stop",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sp"},
    )
    running: str | None = Field(
        default=None,
        serialization_alias="running",
        json_schema_extra={"essential": 1, "type": "gate", "shortname": "ru"},
    )
    systemreset: str | None = Field(
        default=None,
        serialization_alias="systemreset",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "sr"},
    )
    allnotesoff: str | None = Field(
        default=None,
        serialization_alias="allnotesoff",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "ao"},
    )
    allsoundoff: str | None = Field(
        default=None,
        serialization_alias="allsoundoff",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "aso"},
    )
    damper: str | None = Field(
        default=None,
        serialization_alias="damper",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "dp"},
    )
    portamento: str | None = Field(
        default=None,
        serialization_alias="portamento",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "po"},
    )
    sostenuto: str | None = Field(
        default=None,
        serialization_alias="sostenuto",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "su"},
    )
    soft: str | None = Field(
        default=None,
        serialization_alias="soft",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "so"},
    )
    legato: str | None = Field(
        default=None,
        serialization_alias="legato",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "lg"},
    )
    clock: str | None = Field(
        default=None,
        serialization_alias="clock",
        json_schema_extra={"essential": 1, "type": "trigger", "shortname": "c"},
    )
    midiclock: str | None = Field(
        default=None,
        serialization_alias="midiclock",
        json_schema_extra={"essential": 0, "type": "trigger", "shortname": "mc"},
    )
    activesensing: str | None = Field(
        default=None,
        serialization_alias="activesensing",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "as"},
    )
    updaterate: str | None = Field(
        default=None,
        serialization_alias="updaterate",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ur"},
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


class Midithrough(DroidCircuit):
    """ Forward MIDI events from input to one or more outputs

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

    _ramsize: int = 240

    fromtrs: str | None = Field(
        default=None,
        serialization_alias="fromtrs",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "ft"},
    )
    fromusb: str | None = Field(
        default=None,
        serialization_alias="fromusb",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "fu"},
    )
    totrs: str | None = Field(
        default=None,
        serialization_alias="totrs",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "tt"},
    )
    tousb: str | None = Field(
        default=None,
        serialization_alias="tousb",
        json_schema_extra={"essential": 0, "type": "integer", "shortname": "tu"},
    )

