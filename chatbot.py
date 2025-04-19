import random
import nltk
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Custom Q&A pairs (updated)
custom_qna = {
    "what is your name": "I'm ChatterBot, your virtual buddy!",
    "how are you": "I'm doing great! Just excited to talk to you.",
    "who created you": "I was built by a creative developer with Python skills!",
    "what can you do": "I can chat with you, keep you company, and answer basic questions. Ask me anything!",
    "what do you like": "I love talking to curious people like you!",
    "do you sleep": "Nope, I'm always awake for a good conversation.",
    "are you real": "I'm real in the digital world!"
}

# Intent-based replies
responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "responses": ["Hey there!", "Hi! How can I help you today?", "Hello, friend!", "Yo! What's up?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "Take care!", "Bye! Have a nice day."]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },
    "fun": {
        "keywords": ["joke", "funny", "laugh"],
        "responses": ["Why don’t scientists trust atoms? Because they make up everything!",
                      "I'm a bot, but my code is hilarious!"]
    },
    "default": {
        "responses": ["I'm not sure I understand.", "Tell me more!", "Interesting... go on."]
    }
}

def tokenize(text):
    words = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(w) for w in words]

def get_intent(user_input):
    tokens = tokenize(user_input)
    for intent, data in responses.items():
        if intent == "default":
            continue
        for keyword in data["keywords"]:
            if keyword in tokens:
                return intent
    return "default"

def get_response(user_input):
    # First, try direct match in custom Q&A
    lower_input = user_input.lower().strip()
    if lower_input in custom_qna:
        return custom_qna[lower_input]

    # Fallback to intent-based reply
    intent = get_intent(user_input)
    return random.choice(responses[intent]["responses"])

# Chatbot loop with logging
print("🤖 Bot: Hello! Ask me something or type 'bye' to quit.")

with open("chat_log.txt", "a") as log_file:
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            print("🤖 Bot: Bye! Take care.")
            log_file.write("You: " + user_input + "\n")
            log_file.write("Bot: Bye! Take care.\n")
            break
        reply = get_response(user_input)
        print("🤖 Bot:", reply)
        log_file.write("You: " + user_input + "\n")
        log_file.write("Bot: " + reply + "\n")