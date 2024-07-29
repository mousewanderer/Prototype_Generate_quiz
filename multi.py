import random
from random_word import RandomWords
import nltk
from nltk.corpus import wordnet
import factsgen

r = RandomWords()

def changenum1(insert):
    """Generate a random number slightly different from the given number."""
    return int(insert) + random.randint(-5, 5)

def changenum2(insert):
    """Generate a random float number slightly different from the given float number."""
    return float(insert) + random.uniform(-5, 5)

def get_antonyms(word):
    """Fetch antonyms for a given word."""
    antonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.update(lemma.antonyms())
    return {antonym.name() for antonym in antonyms}

def bias1(a):
    """Generate a wrong answer based on the type of answer (noun or number)."""
    if a.isalpha():  # If the answer is a word
        antonyms = get_antonyms(a)
        if antonyms:
            antonyms_list = list(antonyms)
            if len(antonyms_list) >= 2:
                wrong_answers = random.sample(antonyms_list, 2)
                wrong_answers.append(r.get_random_word())  # Add an unrelated word
                random.shuffle(wrong_answers)
                return wrong_answers
        return [r.get_random_word()]  # Default to random word if no antonyms found

    elif a.isdigit():  # If the answer is a number
        return [str(changenum1(a)), str(changenum1(a)), str(changenum1(a))]

    elif any(char.isdigit() for char in a):  # If the answer is a float
        return [str(changenum2(a)), str(changenum2(a)), str(changenum2(a))]

    return [r.get_random_word()]  # Fallback

def generate_wrong_answers(correct_answers):
    """Generate three lists of wrong answers."""
    wrong1 = []
    wrong2 = []
    wrong3 = []

    for answer in correct_answers:
        wrongs = bias1(answer)
        if len(wrongs) >= 3:
            wrong1.append(wrongs[0])
            wrong2.append(wrongs[1])
            wrong3.append(wrongs[2])
        else:
            wrong1.append(wrongs[0])
            wrong2.append(r.get_random_word())
            wrong3.append(r.get_random_word())

    return wrong1, wrong2, wrong3

# Example usage with answers from factsgen
correct_answers = factsgen.answers  # Assuming this is a list of correct answers
wrong1, wrong2, wrong3 = generate_wrong_answers(correct_answers)




    
