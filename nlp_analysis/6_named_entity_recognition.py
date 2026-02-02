import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    text = "Apple was founded by Steve Jobs in California"
    print(extract_entities(text))
