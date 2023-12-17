

#!pip install --user nltk
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import Tuple

# Download the VADER lexicon for sentiment analysis
# nltk.download('vader_lexicon')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

def classify_yes_no_answers(text: str):
    text = text.lower().strip()
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    # Check for negation in context
    negations = {"not", "n't", "never", "no", "none", "cannot", "can't"}
    positives = {"yes", "sure", "definitely", "absolutely", "of course", "indeed"}
    if any(token in negations for token, _ in tagged_tokens):
        return True, "no"
    elif any(token in positives for token, _ in tagged_tokens):
        return True, "yes"

    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score > 0.2:
        return True, "yes"
    elif sentiment_score < -0.2:
        return True, "no"
    else:
        return False, "other"
