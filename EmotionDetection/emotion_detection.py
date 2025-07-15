from transformers import pipeline
import requests
import json
"""
def emotion_detector(text_to_analyse):
    classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)
    result = classifier(text_to_analyse)
    return result
"""

def emotion_detector(text_to_analyse):
    # Load the pipeline
    classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)

    # Get the prediction results
    results = classifier(text_to_analyse)[0]  # [0] because pipeline returns a list of predictions

    # Convert to dictionary: {'emotion': score, ...}
    emotions = {item['label'].lower(): item['score'] for item in results}

    # Extract the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return in your required format
    return {
        'anger': emotions.get('anger', 0.0),
        'disgust': emotions.get('disgust', 0.0),
        'fear': emotions.get('fear', 0.0),
        'joy': emotions.get('joy', 0.0),
        'sadness': emotions.get('sadness', 0.0),
        'dominant_emotion': dominant_emotion
    }
