import string

train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]

# Level 1
def count_moods(data):
    happy = sad = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy += 1
        else:
            sad += 1
    return happy, sad

# Level 2 (N = 5)
happy_words = ["won", "surprise", "excited", "tasty", "selected"]
sad_words = ["lost", "failed", "upset", "cancelled", "missed"]

def clean(sentence):
    return sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()

def guess_mood(sentence):
    words = clean(sentence)
    h = sum(w in happy_words for w in words)
    s = sum(w in sad_words for w in words)
    if h > s:
        return "Happy"
    if s > h:
        return "Sad"
    return "Happy"  # tie: train_data has more Happy (8) than Sad (7)

# Bonus
def learn_scores(data):
    scores = {}
    for sentence, mood in data:
        for w in set(clean(sentence)):
            scores[w] = scores.get(w, 0) + (1 if mood == "Happy" else -1)
    return scores

def guess_mood_learned(sentence, scores):
    total = sum(scores.get(w, 0) for w in clean(sentence))
    return "Happy" if total > 0 else "Sad"

if __name__ == "__main__":
    print(count_moods(train_data))  # (8, 7)
    correct = 0
    for s, real in practice_data:
        g = guess_mood(s)
        print(s, "->", g)
        correct += g == real
    print("Accuracy:", correct / len(practice_data) * 100, "%")

    scores = learn_scores(train_data)
    c2 = sum(guess_mood_learned(s, scores) == r for s, r in practice_data)
    print("Learned accuracy:", c2 / len(practice_data) * 100, "%")