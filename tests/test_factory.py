"""Test factory functions."""

from metapatch.factory.patch_parser import tokenize

def test_minified_tokenizer() -> None:
    """Test the tokenizer's ability to test a minified patch."""
    testpatch = """[buttongroup]
s=_TRACK_1*_NO_CONTROL
b1=B2.1
b2=B2.2
b3=B2.3
b4=B2.4
b5=B2.5
b6=B2.6
v1=0
v2=10
v3=3
v4=4
v5=5
v6=1
l1=L2.1
l2=L2.2
l3=L2.3
l4=L2.4
l5=L2.5
l6=L2.6
o=_T1_FADERMODE
sc=_T1_FADERMODE_UPDATED"""
    testpatch += "\n"
    tokens = list(tokenize(testpatch))
    lines = {token.line for token in tokens}
    assert len(lines) == 22
    params = [token for token in tokens if token.type == "PARAM"]
    values = [token for token in tokens if token.type == "VALUE"]
    assert len(params) == len(values)
    param_names = [p.value for p in params]
    value_names = [p.value for p in values]
    expected = "[buttongroup]\n"
    for param, value in zip(param_names, value_names):
        expected += f"{param}={value}\n"

    assert expected == testpatch
