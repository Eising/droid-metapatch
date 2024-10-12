"""DROID circuits module.

These circuits are auto-generated from circuits.json for droid firmware version
'blue-6'.


.. include:: README.md
"""

__docformat__ = "google"


from .logic import (
    Adc,
    Compare,
    Copy,
    Dac,
    Explin,
    Ifequal,
    Logic,
    Math,
    Multicompare,
    Select,
)
from .sequencing import (
    Algoquencer,
    Arpeggio,
    Encoquencer,
    Euklid,
    Motoquencer,
    Polytool,
    Sequencer,
)
from .clock import (
    Bernoulli,
    Burst,
    Clocktool,
    Flipflop,
    Gatetool,
    Once,
    Timing,
    Triggerdelay,
)
from .ui import (
    Button,
    Buttongroup,
    Encoderbank,
    Encoder,
    Faderbank,
    Fadermatrix,
    Motorfader,
    Notebuttons,
    Nudge,
    Pot,
    Unusedfaders,
)
from .pitch import (
    Calibrator,
    Chord,
    Detune,
    Fold,
    Minifonion,
    Octave,
    Sinfonionlink,
    Superjust,
    Vcotuner,
)
from .cv import (
    Case,
    Crossfader,
    Cvlooper,
    Delay,
    Matrixmixer,
    Mixer,
    Quantizer,
    Queue,
    Recorder,
    Sample,
    Slew,
    Switch,
)
from .modulation import (
    Contour,
    Lfo,
    Random,
    Spring,
    Transient,
)
from .other import (
    Droid,
    Outputcalibrator,
)
from .midi import (
    Firefacecontrol,
    Midifileplayer,
    Midiin,
    Midiout,
    Midithrough,
)
from .deprecated import (
    Fourstatebutton,
    Notchedpot,
    Switchedpot,
    Togglebutton,
)


__all__ = (
    "Adc",
    "Compare",
    "Copy",
    "Dac",
    "Explin",
    "Ifequal",
    "Logic",
    "Math",
    "Multicompare",
    "Select",
    "Algoquencer",
    "Arpeggio",
    "Encoquencer",
    "Euklid",
    "Motoquencer",
    "Polytool",
    "Sequencer",
    "Bernoulli",
    "Burst",
    "Clocktool",
    "Flipflop",
    "Gatetool",
    "Once",
    "Timing",
    "Triggerdelay",
    "Button",
    "Buttongroup",
    "Encoderbank",
    "Encoder",
    "Faderbank",
    "Fadermatrix",
    "Motorfader",
    "Notebuttons",
    "Nudge",
    "Pot",
    "Unusedfaders",
    "Calibrator",
    "Chord",
    "Detune",
    "Fold",
    "Minifonion",
    "Octave",
    "Sinfonionlink",
    "Superjust",
    "Vcotuner",
    "Case",
    "Crossfader",
    "Cvlooper",
    "Delay",
    "Matrixmixer",
    "Mixer",
    "Quantizer",
    "Queue",
    "Recorder",
    "Sample",
    "Slew",
    "Switch",
    "Contour",
    "Lfo",
    "Random",
    "Spring",
    "Transient",
    "Droid",
    "Outputcalibrator",
    "Firefacecontrol",
    "Midifileplayer",
    "Midiin",
    "Midiout",
    "Midithrough",
    "Fourstatebutton",
    "Notchedpot",
    "Switchedpot",
    "Togglebutton",
)