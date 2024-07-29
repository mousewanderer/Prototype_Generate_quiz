import randfacts
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

# Download the necessary resources for nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def get_random_fact():
    return randfacts.get_fact(only_unsafe=False)

def extract_nouns_and_numbers(fact):
    # Tokenize the fact into words
    tokens = word_tokenize(fact)
    # POS tagging to identify parts of speech
    tagged = pos_tag(tokens)
    
    # Define stopwords
    stop_words = set(stopwords.words('english'))
    
    # Extract nouns and numbers, ignoring stopwords
    extracted = [word for word, pos in tagged if (pos in ['NN', 'NNS', 'NNP', 'NNPS'] or word.isdigit()) and word.lower() not in stop_words]
    
    return extracted

def extract_answer(fact):
    # Extract nouns and numbers
    words = extract_nouns_and_numbers(fact)
    
    # Select a random word or number from the list
    if words:
        answer = random.choice(words)
        return answer
    return ""

def create_question(fact, answer):
    if answer:
        question = fact.replace(answer, "___", 1)
        return question
    return False

def generate_quiz(num_questions=10):
    questions = []
    answers = []
    
    while len(questions) < num_questions:
        fact = get_random_fact()
        answer = extract_answer(fact)
        question = create_question(fact, answer)
        
        if question:
            questions.append(question)
            answers.append(answer)
    
    return questions, answers

# Generate quiz with 10 questions
quiz_questions, quiz_answers = generate_quiz(10)

# Print the questions and answers for verification
for i, (q, a) in enumerate(zip(quiz_questions, quiz_answers), start=1):
    print(f"Q{i}: {q}")
    print(f"A{i}: {a}")
