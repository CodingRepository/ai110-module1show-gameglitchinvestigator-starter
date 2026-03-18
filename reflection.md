# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
Despite the game saying normal difficulty has 8 attempts, you start with one less on first run. The hints are backwards: Guessing lower than secret number shows "go lower." The game also doesn't seem to update correctly, as submitting guesses doesn't append to the number to history and the attempts counter doesn't change; it only updates on subsequent presses. I feel like changing the game is also supposed to start a new game, as the secret number doesn't change which is an issue since normal difficulty has range 1-100 while hard has 1-50.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Using Copilot, I was able to refactor and correct the bugs surrounding secret number (e.g. type comparison, wrong hints). The AI made a good, simple suggestion on its second try, converting the str secret on even numbered attempts to int to always ensure an int comparison. However, it gave a very convoluted solution on its initial prompt that essentially chose to convert the user's guess to a str. The specific implementation (which I don't completely remember) did correctly compare as ints, but it was just unnecessary and hard to read.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I reviewed the suggested code changes and used intuition, pytests, and game runs to verify the problem was indeed fixed. For example, the pytest "test_check_guess_with_string_secret" would check whether the function was properly comparing int to int. I used tests like int 3 against str "20" to see whether check_guess would properly assert 3 was lower than 20. Had the bug not been fixed, it would've compared lexicographically, making the test fail. AI helped me to understand each of the function logic when I did not understand it, and I would generate a pytest then review to make sure it was actually testing the issue at hand.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
The secret number kept changing in the original app due to the secret number being shifted between an int and str every odd and even attempt number respectively. Streamlit reruns the entire script every time an interaction occurs. The session state and its connected variables are only for that one browser tab that opens when the program is run. The change that gave the game a stable secret number was forcing int comparisons between the secret and guess.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I never really used the AI features in VS Code, but now I see how powerful and convenient it is to have on hand. One thing I'd do differently going forward when working with AI is being very specific with the tasks I want to outline, otherwise the AI can make very unnecessary changes and change things you don't want touched. This project changed the way I think about AI generated code as it really put an emphasis on thorough review of the implementations generated and rigorous testing of that code to make sure everything truly runs properly.