"""
Natural Language Processing Application

A starter NLP workflow that analyzes text, detects simple sentiment,
and extracts basic entities from sample input.
"""


def analyze_sentiment(text):
    positive_words = ["good", "great", "excellent", "happy", "love"]
    negative_words = ["bad", "poor", "sad", "angry", "hate"]

    text_lower = text.lower()

    positive_score = sum(word in text_lower for word in positive_words)
    negative_score = sum(word in text_lower for word in negative_words)

    if positive_score > negative_score:
        return "Positive"
    elif negative_score > positive_score:
        return "Negative"
    return "Neutral"


def extract_entities(text):
    entities = []

    known_entities = ["OpenAI", "LangChain", "Python", "GitHub"]

    for entity in known_entities:
        if entity.lower() in text.lower():
            entities.append(entity)

    return entities


def main():
    sample_text = "I love building AI automation projects with Python, LangChain, OpenAI, and GitHub."

    sentiment = analyze_sentiment(sample_text)
    entities = extract_entities(sample_text)

    print("Natural Language Processing Application")
    print("---------------------------------------")
    print("Input Text:", sample_text)
    print("Sentiment:", sentiment)
    print("Entities:", entities)


if __name__ == "__main__":
    main()