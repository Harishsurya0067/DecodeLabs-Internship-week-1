# Rule-Based AI Chatbot
# DecodeLabs Internship - Project 1
# Developer: [Your Name]

# ============================================================
# KNOWLEDGE BASE - Dictionary (O(1) lookup, professional approach)
# ============================================================

responses = {
    "hello":        "Hello! I am DecoBot. How can I assist you today?",
    "hi":           "Hi there! Welcome to DecodeLabs AI. How may I help you?",
    "hey":          "Hey! Good to see you. What can I do for you?",
    "how are you":  "I am fully operational and running at 100 percent efficiency!",
    "what is ai":   "Artificial Intelligence is the simulation of human intelligence by machines using logic, learning, and decision-making.",
    "what can you do": "I can answer your questions, greet you, and demonstrate rule-based AI logic.",
    "who made you": "I was built by an AI Engineer Intern at DecodeLabs using Python and rule-based logic.",
    "what is your name": "My name is DecoBot, your rule-based AI assistant.",
    "bye":          "Goodbye! It was great talking to you. Keep building!",
    "thanks":       "You are welcome! Is there anything else I can help you with?",
    "thank you":    "Happy to help! Let me know if you need anything else.",
    "help":         "You can ask me about AI, greet me, or type 'exit' to quit.",
    "what is python": "Python is a high-level, beginner-friendly programming language widely used in AI and data science.",
    "what is decodelabs": "DecodeLabs is an industrial training organization that helps interns build real-world AI and development projects.",
}

# ============================================================
# PHASE 1 - INPUT SANITIZATION FUNCTION
# ============================================================

def sanitize(raw_input):
    return raw_input.lower().strip()

# ============================================================
# PHASE 2 - RESPONSE ENGINE FUNCTION
# ============================================================

def get_response(clean_input):
    return responses.get(clean_input, "I do not understand that yet. Try asking something else or type 'help'.")

# ============================================================
# PHASE 3 - MAIN LOOP (The Heartbeat)
# ============================================================

def run_chatbot():
    print("=" * 50)
    print("      DecoBot - Rule-Based AI Chatbot")
    print("      DecodeLabs Internship | Project 1")
    print("=" * 50)
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 50)

    while True:

        # Get raw input from user
        raw_input = input("You: ")

        # Sanitize the input
        clean_input = sanitize(raw_input)

        # Exit strategy - clean break command
        if clean_input in ("exit", "quit"):
            print("DecoBot: Goodbye! Session terminated. Keep coding!")
            break

        # Get response from knowledge base
        reply = get_response(clean_input)

        # Output the response
        print("DecoBot:", reply)
        print()

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_chatbot()