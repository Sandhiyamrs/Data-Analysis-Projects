"""
Simple emotion detection using pretrained transformer (distilbert) from HuggingFace. 
Requires: transformers
"""
from transformers import pipeline

def run_emotion_detector(texts):
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
    return classifier(texts)

if __name__ == "__main__":
    texts = ["I am happy", "I'm so sad and depressed", "This is exciting!"]
    print(run_emotion_detector(texts))
