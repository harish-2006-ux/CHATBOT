# ai_engine.py
# Shadow Recall: session memory (lightweight)

MAX_MEMORY = 5
memory = []  # stores tuples: (user, bot)

def remember(user, bot):
    memory.append((user, bot))
    if len(memory) > MAX_MEMORY:
        memory.pop(0)

def get_context():
    if not memory:
        return ""
    context_lines = []
    for u, b in memory[-MAX_MEMORY:]:
        context_lines.append(f"User: {u}")
        context_lines.append(f"Interpreter: {b}")
    return " | ".join(context_lines)

def interpret_query(message):
    msg = message.lower().strip()
    context = get_context()

    if msg in ["hi", "hello", "hey"]:
        reply = "You are acknowledged. Issue a command."

    elif "who are you" in msg:
        reply = "I am the Shadow Interpreter. I analyze. I respond."

    elif "status" in msg:
        reply = "System stable. Shadow authority active."

    elif "analyze" in msg:
        reply = "Analysis mode engaged. Provide data."

    elif "remember" in msg:
        reply = "Shadow Recall active. Recent commands retained."

    else:
        # Use context lightly
        if context:
            reply = "Context recognized. Clarify the next directive."
        else:
            reply = "Insufficient clarity. Reissue command."

    remember(message, reply)
    return reply
