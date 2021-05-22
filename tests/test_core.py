from pyper import Echo, Prompt


def test_echo_is_a_value_object():
    assert Echo(message="same coat") == Echo(message="same coat")


def test_prompt_is_a_value_object():
    assert Prompt(message="same coat") == Prompt(message="same coat")


def test_echo_is_not_a_prompt():
    assert Echo(message="same coat") != Prompt(message="same coat")



