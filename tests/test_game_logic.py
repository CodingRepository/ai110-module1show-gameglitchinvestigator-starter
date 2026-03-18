from logic_utils import check_guess, parse_guess, update_score

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

def test_update_score_win_early():
    # Test winning on first attempt gives high points
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*1

def test_update_score_win_later():
    # Test winning later gives fewer points
    score = update_score(0, "Win", 5)
    assert score == 50  # 100 - 10*5

def test_update_score_win_min_points():
    # Test minimum points for very late wins
    score = update_score(0, "Win", 20)
    assert score == 10  # min(100 - 10*20, 10)

def test_update_score_too_high():
    # Test penalty for guessing too high
    score = update_score(100, "Too High", 1)
    assert score == 95  # 100 - 5

def test_update_score_too_low():
    # Test penalty for guessing too low
    score = update_score(100, "Too Low", 2)
    assert score == 95  # 100 - 5

def test_update_score_no_change():
    # Test unknown outcome doesn't change score
    score = update_score(50, "Unknown", 1)
    assert score == 50
