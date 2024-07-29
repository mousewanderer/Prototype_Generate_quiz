import randfacts
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords


#Priority list 1. with double " " 2. With numbers. 3. randomly decided Nouns 

def ranfacts():
    return randfacts.get_fact(only_unsafe=False)

def extract_nouns_and_numbers(facts):
    # Tokenize the fact into words
    tokens = word_tokenize(facts)
    # POS tagging to identify parts of speech
    tagged = pos_tag(tokens)
    
    # Define stopwords
    stop_words = set(stopwords.words('english'))
    
    # Extract nouns and numbers, ignoring stopwords
    extracted = [word for word, pos in tagged if (pos in ['NN', 'NNS', 'NNP', 'NNPS'] or word.isdigit()) and word.lower() not in stop_words]
    
    return extracted

def extract_answer(facts):
    # Extract nouns and numbers
    words = extract_nouns_and_numbers(facts)
    
    # Select a random word or number from the list
    if words:
        return random.choice(words)
    return ""

def Create_answer(facts):
    # Check for text between double quotes
    start_quote = facts.find('"')
    if start_quote != -1:
        end_quote = facts.find('"', start_quote + 1)
        if end_quote != -1:
            result = facts[start_quote + 1:end_quote]
            if result.isdigit():
                return result
            else:
                return result
    
    # Check for numbers in the string
    digits = ''.join(filter(str.isdigit, facts))
    if digits:
        return digits
    
    # Default to extracting nouns or numbers if no quotes or numbers are found
    return extract_answer(facts)

def create_question(fact, answer):
    if answer:
        question = fact.replace(answer, "___", 1)
        return question
    return False

questions = []
answers = []
def generate_quiz(num_questions=10):
    
    while len(questions) < num_questions:
        factual = ranfacts()
        solution = Create_answer(facts=factual)
        question = create_question(fact=factual, answer=solution)
        
        if question:
            questions.append(question)
            answers.append(solution)  # Store the correct answer

    return questions, answers

# Generate quiz with 10 questions
quiz_questions, quiz_answers = generate_quiz(10)


          
