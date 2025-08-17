"""DROID circuits. These circuits are auto-generated from circuits.json."""

from pydantic import AliasChoices, Field
from metapatch.circuits.base import DroidCircuit


__droid_version__ = "blue-6"


class Adc(DroidCircuit):
    """ AD Converter with 12 bits

    Args:
        input (cv):
          Input signal to convert to binary representation.
        minimum (cv):
          The lowest assumed input value. This value and all lower values will be
          converted to the bit sequence 000000000000.
        maximum (cv):
          The highest assumed input value. This value and all higher values will be
          converted to the bit sequence 111111111111.
        bit1 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit2 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit3 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit4 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit5 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit6 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit7 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit8 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit9 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit10 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit11 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        bit12 (gate):
          The 12 bit outputs. bit1 is the MSB – the most significant bit. The LSB (least
          significant bit) is the highest output that you actually patch. If you do not
          need the full resolution of 12 bits, simply just use the first couple of
          outputs.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    minimum: str | None = Field(
        default=None,
        serialization_alias="minimum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "m"},
    )
    maximum: str | None = Field(
        default=None,
        serialization_alias="maximum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "x"},
    )
    bit1: str | None = Field(
        default=None,
        serialization_alias="bit1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b1"},
    )
    bit2: str | None = Field(
        default=None,
        serialization_alias="bit2",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b2"},
    )
    bit3: str | None = Field(
        default=None,
        serialization_alias="bit3",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b3"},
    )
    bit4: str | None = Field(
        default=None,
        serialization_alias="bit4",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b4"},
    )
    bit5: str | None = Field(
        default=None,
        serialization_alias="bit5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b5"},
    )
    bit6: str | None = Field(
        default=None,
        serialization_alias="bit6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b6"},
    )
    bit7: str | None = Field(
        default=None,
        serialization_alias="bit7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b7"},
    )
    bit8: str | None = Field(
        default=None,
        serialization_alias="bit8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b8"},
    )
    bit9: str | None = Field(
        default=None,
        serialization_alias="bit9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b9"},
    )
    bit10: str | None = Field(
        default=None,
        serialization_alias="bit10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b10"},
    )
    bit11: str | None = Field(
        default=None,
        serialization_alias="bit11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b11"},
    )
    bit12: str | None = Field(
        default=None,
        serialization_alias="bit12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b12"},
    )


class Compare(DroidCircuit):
    """ Compare two values

    Args:
        input (cv):
          A value to compare.
        compare (cv):
          A reference value to compare the input with.
        ifgreater (cv):
          Value to be output if input is greater than compare. If you patch nothing
          here, the value of the input else will be used.
        ifless (cv):
          Value to be output if input is less than compare. If you patch nothing here,
          the value of the input else will be used.
        ifequal (cv):
          Value to be output if input is equal to compare within the precision defined
          by precision. If you patch nothing here, the value of the input else will be
          used.
        else (cv):
          Specifies the output value in case non of the stated conditions are met.
        precision (cv):
          An optional precision to be used by ifequal
        output (cv):
          Here one of ifgreater, ifless or ifequal is output.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    compare: str | None = Field(
        default=None,
        serialization_alias="compare",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "c"},
    )
    ifgreater: str | None = Field(
        default=None,
        serialization_alias="ifgreater",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "g"},
    )
    ifless: str | None = Field(
        default=None,
        serialization_alias="ifless",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "l"},
    )
    ifequal: str | None = Field(
        default=None,
        serialization_alias="ifequal",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "q"},
    )
    else_: str | None = Field(
        default=None,
        serialization_alias="else",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "e"},
    )
    precision: str | None = Field(
        default=None,
        serialization_alias="precision",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pc"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Copy(DroidCircuit):
    """ Copy a signal, while applying attenuation and offset

    Args:
        input (cv):
          Connect the signal you want to copy here.
        output (cv):
          The resulting signal will be sent here.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 24

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Dac(DroidCircuit):
    """ DA Converter with 12 bits

    Args:
        bit1 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit2 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit3 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit4 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit5 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit6 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit7 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit8 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit9 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit10 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit11 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        bit12 (gate):
          The 12 bit input bits. bit1 is the MSB – the most significant bit. The LSB
          (least significant bit) is the highest input that you actually patch.
        minimum (cv):
          This sets the lower bound of the output range, i.e. the value that the bit
          sequence 000000000000 will produce.
        maximum (cv):
          This sets the upper bound of the output value, i.e. the value that the bit
          sequence 111111111111 will produce.
        output (cv):
          Output signal.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    bit1: str | None = Field(
        default=None,
        serialization_alias="bit1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b1"},
    )
    bit2: str | None = Field(
        default=None,
        serialization_alias="bit2",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b2"},
    )
    bit3: str | None = Field(
        default=None,
        serialization_alias="bit3",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b3"},
    )
    bit4: str | None = Field(
        default=None,
        serialization_alias="bit4",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "b4"},
    )
    bit5: str | None = Field(
        default=None,
        serialization_alias="bit5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b5"},
    )
    bit6: str | None = Field(
        default=None,
        serialization_alias="bit6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b6"},
    )
    bit7: str | None = Field(
        default=None,
        serialization_alias="bit7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b7"},
    )
    bit8: str | None = Field(
        default=None,
        serialization_alias="bit8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b8"},
    )
    bit9: str | None = Field(
        default=None,
        serialization_alias="bit9",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b9"},
    )
    bit10: str | None = Field(
        default=None,
        serialization_alias="bit10",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b10"},
    )
    bit11: str | None = Field(
        default=None,
        serialization_alias="bit11",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b11"},
    )
    bit12: str | None = Field(
        default=None,
        serialization_alias="bit12",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "b12"},
    )
    minimum: str | None = Field(
        default=None,
        serialization_alias="minimum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "m"},
    )
    maximum: str | None = Field(
        default=None,
        serialization_alias="maximum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "x"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Explin(DroidCircuit):
    """ Exponential to linear converter

    Args:
        input (cv):
          Patch an exponential envelope output or a similar signal here. This value must
          be positive or otherwise it will be set to 0.0.
        startvalue (cv):
          The assumed maximum value of the input signal (the start voltage from where it
          decays in an exponential way.
        endvalue (cv):
          The value at which it is assumed to be zero (at which the linear output will
          be set to zero. This value must be positive. It is forced to be >=  0.001.
        mix (fraction):
          Sets the mix between the “dry” and “wet” signal: At 0.0 the output is the same
          as the input. At 1.0 the output is the linear curve. At a value in between it
          is some average. You are even allowed to used values > 1.0. A value of 2.0
          will overcompensate and bend the curve beyond linearity into a curve some
          modularists would call logarithmic.
        output (cv):
          Here comes the resulting linear output
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    startvalue: str | None = Field(
        default=None,
        serialization_alias="startvalue",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "sv"},
    )
    endvalue: str | None = Field(
        default=None,
        serialization_alias="endvalue",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "ev"},
    )
    mix: str | None = Field(
        default=None,
        serialization_alias="mix",
        json_schema_extra={"essential": 0, "type": "fraction", "shortname": "m"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Ifequal(DroidCircuit):
    """ Check if two values are equal

    Args:
        input1 (cv):
          A value.
        input2 (cv):
          Another value
        ifequal (cv):
          Value to be output if input1 is exactly equal to input2.
        else (cv):
          Value to output otherwise.
        output (cv):
          Here comes the result.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 32

    input1: str | None = Field(
        default=None,
        serialization_alias="input1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i1"},
    )
    input2: str | None = Field(
        default=None,
        serialization_alias="input2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i2"},
    )
    ifequal: str | None = Field(
        default=None,
        serialization_alias="ifequal",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "q"},
    )
    else_: str | None = Field(
        default=None,
        serialization_alias="else",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "e"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Logic(DroidCircuit):
    """ Logic operations utility

    Args:
        input1 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input2 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input3 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input4 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input5 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input6 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input7 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        input8 (gate):
          1 ... 8 input. Note: this input is declared as a gate input, but in fact you
          can use it as a CV input in combination with various or random values set for
          the threshold.
        threshold (cv):
          Input values at, or above this threshold value, are considered high or on. The
          default is 0.1 which corresponds to an input voltage of 1 V. You can get
          interesting results when both the inputs are variable CVs (like from LFOs) and
          this threshold is being modulated as well.
        lowvalue (cv):
          Output value that is output for logic low, false or off.
        highvalue (cv):
          Output value that is output for a logic high, true or on.
        countvalue (cv):
          Value added to the count output for each input with a high level
        and (cv):
          A logic AND operation on all patched inputs: This output is set to highvalue
          if all inputs are high (i.e. at least threshold), else lowvalue
        or (cv):
          A logic OR operation on all patched inputs: This output is set to highvalue if
          at least one of the inputs is high
        xor (cv):
          Exclusive OR: This is high, if the number of high inputs is odd! This means
          that any change in one of the inputs will also change the output.
        nand (cv):
          Like AND but the outcome is negated.
        nor (cv):
          Like OR but the outcome is negated.
        negated (cv):
          Logical negate of input1 (which can abbreviated as input). Note: The inputs
          input2 ... input7 are ignored here. Another note: If you use input1 anyway,
          negated always outputs exactly the same as nand and nor. It's just more
          convenient to write and easier to understand. Hence a dedicated output for a
          logic negate.
        count (integer):
          Adds countvalue to this output for each input that is high.
        countlow (cv):
          Adds countvalue to this output for each input that is low.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    input1: str | None = Field(
        default=None,
        serialization_alias="input1",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "i1"},
    )
    input2: str | None = Field(
        default=None,
        serialization_alias="input2",
        json_schema_extra={"essential": 2, "type": "gate", "shortname": "i2"},
    )
    input3: str | None = Field(
        default=None,
        serialization_alias="input3",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i3"},
    )
    input4: str | None = Field(
        default=None,
        serialization_alias="input4",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i4"},
    )
    input5: str | None = Field(
        default=None,
        serialization_alias="input5",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i5"},
    )
    input6: str | None = Field(
        default=None,
        serialization_alias="input6",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i6"},
    )
    input7: str | None = Field(
        default=None,
        serialization_alias="input7",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i7"},
    )
    input8: str | None = Field(
        default=None,
        serialization_alias="input8",
        json_schema_extra={"essential": 0, "type": "gate", "shortname": "i8"},
    )
    threshold: str | None = Field(
        default=None,
        serialization_alias="threshold",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "t"},
    )
    lowvalue: str | None = Field(
        default=None,
        serialization_alias="lowvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l"},
    )
    highvalue: str | None = Field(
        default=None,
        serialization_alias="highvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "h"},
    )
    countvalue: str | None = Field(
        default=None,
        serialization_alias="countvalue",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "cv"},
    )
    and_: str | None = Field(
        default=None,
        serialization_alias="and",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "a"},
    )
    or_: str | None = Field(
        default=None,
        serialization_alias="or",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "o"},
    )
    xor: str | None = Field(
        default=None,
        serialization_alias="xor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "x"},
    )
    nand: str | None = Field(
        default=None,
        serialization_alias="nand",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "na"},
    )
    nor: str | None = Field(
        default=None,
        serialization_alias="nor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "no"},
    )
    negated: str | None = Field(
        default=None,
        serialization_alias="negated",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "n"},
    )
    count: str | None = Field(
        default=None,
        serialization_alias="count",
        json_schema_extra={"essential": 1, "type": "integer", "shortname": "c"},
    )
    countlow: str | None = Field(
        default=None,
        serialization_alias="countlow",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "cl"},
    )


class Math(DroidCircuit):
    """ Math utility circuit

    Args:
        input1 (cv):
          The two inputs
        input2 (cv):
          The two inputs
        sum (cv):
          input1 +  input2
        difference (cv):
          input1 -  input2
        product (cv):
          input1× input2
        quotient (cv):
          input1 /  input2. If input2 is zero, a very large number will be returned,
          while the correct sign is being kept. This is mathematically not correct but
          more useful than any other possible result.
        modulo (cv):
          input1 modulo input2. This needs some explanation: With this operation you can
          “fold” the value from input1 into the range 0 ... input2. For example if
          input2 is 1 V, the output will convert 1.234 V to 0.234 V, -2.1 V to 0.9 V and
          0.5 V to 0.5 V. If input2 is zero or negative, the output will be zero.
        power (cv):
          input1 to the power of input2. Please note that the power has several cases
          where it is not defined when either the base or the exponent is zero or less
          than zero. In order to be as useful for your music making as possible the math
          circuit behaves in the following way:
          * If input1 < 0, input2 is rounded to the nearest integer.
          * If input1 = 0 and input2 < 0, a very large number is output.

        average (cv):
          The average of input1 and input2
        maximum (cv):
          The maximum of input1 and input2
        minimum (cv):
          The minimum of input1 and input2
        negation (cv):
          -  input1
        reciprocal (cv):
          1 /  input1. If input1 is zero, a very large number is being output, while the
          sign is being kept.
        amount (cv):
          The absolute value of input1 (i.e. -   input1 if input1 < 0, else input1)
        sine (cv):
          The sine of input1 in a way, the input range of 0.0 … 1.0 goes exactly through
          one wave cycle. Or more mathematically expressed: sin(2π× input1).
        cosine (cv):
          The cosine of input1 in a way, the input range of 0.0 … 1.0 goes exactly
          through one wave cycle. Or more mathematically expressed: cos(2π× input1).
        square (cv):
          input1^2
        root (cv):
          √( input1). Please note that you cannot compute the square root of a negative
          number. In order to output something useful anyway, the result will be - √(-
          input1), if input1 < 0.
        logarithm (cv):
          The natural logarithm of input1: ln _ input1. The logarithm is only defined
          for positive numbers. mathcircuit behaves like this:
          * If input1 = 0, a negative very large number is output.
          * If input2 < 0, - ln _-
          input1 is output.

        round (cv):
          The integer number nearest to input1
        floor (cv):
          The largest integer number that is not greater than input1
        ceil (cv):
          The smallest integer number that is not less than input1
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 64

    input1: str | None = Field(
        default=None,
        serialization_alias="input1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i1"},
    )
    input2: str | None = Field(
        default=None,
        serialization_alias="input2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i2"},
    )
    sum: str | None = Field(
        default=None,
        serialization_alias="sum",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "s"},
    )
    difference: str | None = Field(
        default=None,
        serialization_alias="difference",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "d"},
    )
    product: str | None = Field(
        default=None,
        serialization_alias="product",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "p"},
    )
    quotient: str | None = Field(
        default=None,
        serialization_alias="quotient",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "qu"},
    )
    modulo: str | None = Field(
        default=None,
        serialization_alias="modulo",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "md"},
    )
    power: str | None = Field(
        default=None,
        serialization_alias="power",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "pw"},
    )
    average: str | None = Field(
        default=None,
        serialization_alias="average",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "a"},
    )
    maximum: str | None = Field(
        default=None,
        serialization_alias="maximum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "x"},
    )
    minimum: str | None = Field(
        default=None,
        serialization_alias="minimum",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "m"},
    )
    negation: str | None = Field(
        default=None,
        serialization_alias="negation",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "n"},
    )
    reciprocal: str | None = Field(
        default=None,
        serialization_alias="reciprocal",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rc"},
    )
    amount: str | None = Field(
        default=None,
        serialization_alias="amount",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "am"},
    )
    sine: str | None = Field(
        default=None,
        serialization_alias="sine",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "si"},
    )
    cosine: str | None = Field(
        default=None,
        serialization_alias="cosine",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "cs"},
    )
    square: str | None = Field(
        default=None,
        serialization_alias="square",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "q"},
    )
    root: str | None = Field(
        default=None,
        serialization_alias="root",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "ro"},
    )
    logarithm: str | None = Field(
        default=None,
        serialization_alias="logarithm",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "l"},
    )
    round: str | None = Field(
        default=None,
        serialization_alias="round",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "rd"},
    )
    floor: str | None = Field(
        default=None,
        serialization_alias="floor",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "f"},
    )
    ceil: str | None = Field(
        default=None,
        serialization_alias="ceil",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c"},
    )


class Multicompare(DroidCircuit):
    """ Compare in input with up to eight possible values

    Args:
        input (cv):
          A value to compare.
        compare1 (cv):
          Up to eight reference values to compare the input with.
        compare2 (cv):
          Up to eight reference values to compare the input with.
        compare3 (cv):
          Up to eight reference values to compare the input with.
        compare4 (cv):
          Up to eight reference values to compare the input with.
        compare5 (cv):
          Up to eight reference values to compare the input with.
        compare6 (cv):
          Up to eight reference values to compare the input with.
        compare7 (cv):
          Up to eight reference values to compare the input with.
        compare8 (cv):
          Up to eight reference values to compare the input with.
        ifequal1 (cv):
          The output values if the according comparison value is found at the input.
        ifequal2 (cv):
          The output values if the according comparison value is found at the input.
        ifequal3 (cv):
          The output values if the according comparison value is found at the input.
        ifequal4 (cv):
          The output values if the according comparison value is found at the input.
        ifequal5 (cv):
          The output values if the according comparison value is found at the input.
        ifequal6 (cv):
          The output values if the according comparison value is found at the input.
        ifequal7 (cv):
          The output values if the according comparison value is found at the input.
        ifequal8 (cv):
          The output values if the according comparison value is found at the input.
        else (cv):
          Specifies the output value in case non of comparison values is found at the
          input.
        output (cv):
          The vaue of the matching ifequal or else input.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 56

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
    )
    compare1: str | None = Field(
        default=None,
        serialization_alias="compare1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "c1"},
    )
    compare2: str | None = Field(
        default=None,
        serialization_alias="compare2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "c2"},
    )
    compare3: str | None = Field(
        default=None,
        serialization_alias="compare3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "c3"},
    )
    compare4: str | None = Field(
        default=None,
        serialization_alias="compare4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "c4"},
    )
    compare5: str | None = Field(
        default=None,
        serialization_alias="compare5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c5"},
    )
    compare6: str | None = Field(
        default=None,
        serialization_alias="compare6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c6"},
    )
    compare7: str | None = Field(
        default=None,
        serialization_alias="compare7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c7"},
    )
    compare8: str | None = Field(
        default=None,
        serialization_alias="compare8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "c8"},
    )
    ifequal1: str | None = Field(
        default=None,
        serialization_alias="ifequal1",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "if1"},
    )
    ifequal2: str | None = Field(
        default=None,
        serialization_alias="ifequal2",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "if2"},
    )
    ifequal3: str | None = Field(
        default=None,
        serialization_alias="ifequal3",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "if3"},
    )
    ifequal4: str | None = Field(
        default=None,
        serialization_alias="ifequal4",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "if4"},
    )
    ifequal5: str | None = Field(
        default=None,
        serialization_alias="ifequal5",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "if5"},
    )
    ifequal6: str | None = Field(
        default=None,
        serialization_alias="ifequal6",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "if6"},
    )
    ifequal7: str | None = Field(
        default=None,
        serialization_alias="ifequal7",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "if7"},
    )
    ifequal8: str | None = Field(
        default=None,
        serialization_alias="ifequal8",
        json_schema_extra={"essential": 0, "type": "cv", "shortname": "if8"},
    )
    else_: str | None = Field(
        default=None,
        serialization_alias="else",
        json_schema_extra={"essential": 1, "type": "cv", "shortname": "e"},
    )
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )


class Select(DroidCircuit):
    """ Copy a signal if selected

    Args:
        input (cv):
          Connect the signal you want to copy.
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
        output (cv):
          The input will be copied here, but just when the circuit is selected via
          select.
        comment: Add a comment in the droid ini file.
    """

    _ramsize: int = 24

    input: str | None = Field(
        default=None,
        serialization_alias="input",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "i"},
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
    output: str | None = Field(
        default=None,
        serialization_alias="output",
        json_schema_extra={"essential": 2, "type": "cv", "shortname": "o"},
    )

