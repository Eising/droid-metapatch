"""DROID circuits. These circuits are auto-generated from circuits.json."""

from dataclasses import dataclass, field
from typing import Optional

from metapatch.circuits.base import DroidCircuit
from metapatch.circuits import circuit_types as ctype


__droid_version__ = "blue-6"


@dataclass
class Adc(DroidCircuit):
    """AD Converter with 12 bits.

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

    __ramsize__ = 56
    input: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    minimum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    maximum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    bit1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )



@dataclass
class Compare(DroidCircuit):
    """Compare two values.

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
        else_ (cv):
          Specifies the output value in case non of the stated conditions are met.
        precision (cv):
          An optional precision to be used by ifequal
        output (cv):
          Here one of ifgreater, ifless or ifequal is output.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 32
    input: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifgreater: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifless: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    else_: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    precision: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Copy(DroidCircuit):
    """Copy a signal, while applying attenuation and offset.

    Args:
        input (cv):
          Connect the signal you want to copy here.
        output (cv):
          The resulting signal will be sent here.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 24
    input: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Dac(DroidCircuit):
    """DA Converter with 12 bits.

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

    __ramsize__ = 56
    bit1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit9: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit10: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit11: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    bit12: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    minimum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    maximum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Explin(DroidCircuit):
    """Exponential to linear converter.

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

    __ramsize__ = 32
    input: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    startvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    endvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    mix: Optional[str] = field(
            default=None,
            metadata=ctype.type_fraction(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Ifequal(DroidCircuit):
    """Check if two values are equal.

    Args:
        input1 (cv):
          A value.
        input2 (cv):
          Another value
        ifequal (cv):
          Value to be output if input1 is exactly equal to input2.
        else_ (cv):
          Value to output otherwise.
        output (cv):
          Here comes the result.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 32
    input1: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    input2: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    else_: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Logic(DroidCircuit):
    """Logic operations utility.

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
        and_ (cv):
          A logic AND operation on all patched inputs: This output is set to highvalue
          if all inputs are high (i.e. at least threshold), else lowvalue
        or_ (cv):
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

    __ramsize__ = 56
    input1: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input2: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input3: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input4: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input5: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input6: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input7: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    input8: Optional[str] = field(
            default=None,
            metadata=ctype.type_gate(ramsize=0)
    )
    threshold: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    lowvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    highvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    countvalue: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    and_: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    or_: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    xor: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    nand: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    nor: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    negated: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    count: Optional[str] = field(
            default=None,
            metadata=ctype.type_integer(ramsize=0)
    )
    countlow: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Math(DroidCircuit):
    """Math utility circuit.

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

    __ramsize__ = 64
    input1: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    input2: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    sum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    difference: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    product: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    quotient: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    modulo: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    power: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    average: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    maximum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    minimum: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    negation: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    reciprocal: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    amount: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    sine: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    cosine: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    square: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    root: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    logarithm: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    round: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    floor: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ceil: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Multicompare(DroidCircuit):
    """Compare in input with up to eight possible values.

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
        else_ (cv):
          Specifies the output value in case non of comparison values is found at the
          input.
        output (cv):
          The vaue of the matching ifequal or else input.
        comment: Add a comment in the droid ini file.

    """

    __ramsize__ = 56
    input: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare1: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare2: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare3: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare4: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare5: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare6: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare7: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    compare8: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal1: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal2: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal3: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal4: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal5: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal6: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal7: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    ifequal8: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    else_: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



@dataclass
class Select(DroidCircuit):
    """Copy a signal if selected.

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

    __ramsize__ = 24
    input: Optional[str] = field(
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
    output: Optional[str] = field(
            default=None,
            metadata=ctype.type_cv(ramsize=0)
    )



