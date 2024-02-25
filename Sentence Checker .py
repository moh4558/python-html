import nltk
nltk.download('punkt')
nltk.data.path.append('/path/to/downloaded/data')
from nltk.tokenize import sent_tokenize
from textblob import TextBlob  

def check_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged)
    return result

def print_noun_phrases(tree):
    for subtree in tree.subtrees(filter=lambda x: x.label() == 'NP'):
        np_words = [word for word, tag in subtree.leaves()]
        np_phrase = ' '.join(np_words)
        print(f"Detected Noun Phrase: {np_phrase}")

def analyze_sentiment(sentence):
    analysis = TextBlob(sentence)
    polarity = analysis.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Neutral" if polarity == 0 else "Negative"
    print(f"Sentiment Analysis: {sentiment} (Polarity: {polarity:.2f})")

def recognize_entities(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    print("Recognized Entities:")
    print(entities)

def main():
    print("Welcome to the Advanced Text Analyzer!")

    while True:
        try:
            print("\nOptions:")
            print("1. Analyze a sentence")
            print("2. Analyze multiple sentences")
            print("3. Exit")

            choice = input("Select an option (1, 2, or 3): ").strip()

            if choice == '1':
                text = input("Enter a sentence for analysis: ").strip()
                if not text:
                    print("Please enter a valid sentence.")
                    continue

                # Tokenize and check the sentence
                sentences = sent_tokenize(text)
                for sentence in sentences:
                    print("\nOriginal Sentence:", sentence)
                    result = check_sentence(sentence)
                    print_noun_phrases(result)
                    analyze_sentiment(sentence)
                    recognize_entities(sentence)

            elif choice == '2':
                text = input("Enter multiple sentences for analysis (separated by '. '): ").strip()
                if not text:
                    print("Please enter valid sentences.")
                    continue

                # Tokenize and check multiple sentences
                sentences = sent_tokenize(text)
                for sentence in sentences:
                    print("\nOriginal Sentence:", sentence)
                    result = check_sentence(sentence)
                    print_noun_phrases(result)
                    analyze_sentiment(sentence)
                    recognize_entities(sentence)

            elif choice == '3':
                print("Exiting the program. Thank you for using the Advanced Text Analyzer!")
                break

            else:
                print("Invalid choice. Please enter '1' to analyze a sentence, '2' to analyze multiple sentences, or '3' to exit.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Download NLTK data
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')

    # Run the main function
    main()
