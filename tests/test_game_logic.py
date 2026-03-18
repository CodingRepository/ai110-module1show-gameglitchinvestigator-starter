from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_with_string_secret():
    # Test the bug where secret is sometimes a string
    outcome, message = check_guess(10, "20")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
    
    outcome, message = check_guess(3, "20")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

    outcome, message = check_guess(30, "20")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_parse_guess_strips_whitespace():
    # Regression test for bug where whitespace would prevent parsing.
    ok, value, err = parse_guess("  42  \n")
    assert ok is True
    assert value == 42
    assert err is None
