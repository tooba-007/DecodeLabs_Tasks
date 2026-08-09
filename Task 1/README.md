# Task 1 – Rule-Based AI Chatbot
**DecodeLabs AI Industrial Training Kit**

## What this project does
A simple **rule-based chatbot** that responds to predefined user messages
using a dictionary lookup. It runs in a continuous loop, understands
greetings, a couple of questions, and an exit command.

## Key Requirements (matches the project spec)
- ✅ Continuous input loop (`while True`)
- ✅ Sanitization — input is lowercased and stripped of extra spaces
- ✅ Knowledge base — a dictionary with 6 predefined intents
- ✅ Fallback — a default response for anything not understood
- ✅ Exit strategy — typing `exit` cleanly breaks the loop

## How it works
Instead of a long, hard-to-maintain `if-elif-elif...` ladder, this bot
uses a **dictionary + `.get()`**, which is faster and cleaner:

```python
responses = {
    "hello": "Hi there! How can I help you today?",
    "bye": "Goodbye! Shutting down the logic engine."
}
reply = responses.get(user_input, "I do not understand that command.")
```

`.get()` looks up the user's message as a key; if it's not found, it
instantly falls back to the default message — no long chain of checks
needed.

## How to run
```bash
python project1.py
```
Then type things like `hello`, `help`, `what is your name`, or `bye`.
Type `exit` anytime to stop the bot.

## Example conversation
```
Bot: Hello! I am your Rule-Based Assistant. Type 'exit' to stop.
You: hello
Bot: Hi there! How can I help you today?
You: what is your name
Bot: I am Project 1, your Rule-Based Assistant.
You: exit
Bot: Shutting down. Goodbye!
```

## Ideas to extend it
- Add more intents (weather, jokes, date/time)
- Handle simple typos or partial matches
- Give the bot a custom personality/name
