# FIX: Refactored logic from app.py. Function itself unchanged.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

# FIX: Refactored logic from app.py. Fixed bug in which leading/trailing whitespace could prevent parsing.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Refactored logic from app.py into logic_utils.py using Copilot.
# Fixed str vs int bug using type conversion and changed hints to be correct. Imported logic_utils into app.py.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess = int(guess)
    secret = int(secret)
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

# FIX: Refactored from app.py and fixes faulty point calculation bugs involving attempt number 
# (removed %2 condition and made points decrease with each attempt).
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
