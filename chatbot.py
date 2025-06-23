import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Define greeting and farewell patterns
patterns = {
    r'\b(hi|hello|hey)\b': [
        "Hello! How can I assist you today?",
        "Hi there! Ready to help.",
    ],
    r'how are you': [
        "I'm doing great, thanks for asking!",
        "All systems operational!",
    ],
    r'\b(bye|exit|quit)\b': [
        "Goodbye! Have a wonderful day.",
        "See you later!",
    ]
}

# Define simple question-answer knowledge base
knowledge_base = {
    "your name": "I'm ChatBot, your AI assistant.",
    "what is your name": "I'm ChatBot, your AI assistant.",
    "who are you": "I'm ChatBot, created to help you!",
    "who created you": "A developer who loves Python built me.",
    "what is python": "Python is a popular programming language known for its simplicity.",
    "what is ai": "AI stands for Artificial Intelligence—machines that simulate human thinking.",
    "what is machine learning": "Machine Learning is a subset of AI where machines learn from data.",
    "what is your purpose": "I'm here to chat with you and answer basic questions.",
    "what is the capital of bangladesh": "The capital of Bangladesh is Dhaka.",
    "how old are you": "I don't have an age, but I'm always up-to-date!",
}

# Evaluate arithmetic expressions safely
def evaluate_expression(expr):
    if re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expr):
        try:
            result = eval(expr)
            return f"The result is {result}"
        except Exception:
            return "Sorry, I couldn't evaluate the expression."
    return None

# Extract potential arithmetic expression
def extract_arithmetic_expression(text):
    match = re.search(r'([\d\.\s\+\-\*\/\(\)]+)', text)
    return match.group(1).strip() if match else None

# Preprocess input: tokenize, remove stopwords, etc.
def preprocess_input(text):
    tokens = word_tokenize(text.lower())
    return ' '.join([word for word in tokens if word.isalnum() and word not in stopwords.words('english')])

# Match known patterns and responses
def match_pattern(user_input):
    # Check for math expressions
    expr = extract_arithmetic_expression(user_input)
    if expr:
        result = evaluate_expression(expr)
        if result:
            return result

    # Match simple patterns
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input.lower()):
            return random.choice(responses)

    # Clean and check against knowledge base
    cleaned_input = preprocess_input(user_input)
    for key, value in knowledge_base.items():
        if key in cleaned_input:
            return value
