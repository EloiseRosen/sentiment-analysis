from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
from pprint import pprint

json_data=open('sample_text.json').read()
data = json.loads(json_data)
sentences = data['sample_text']

SIA = SentimentIntensityAnalyzer()
positive_text = []
negative_text = []

for sentence in sentences:
    # compound score, ranges from -1 (the most negative) to 1 (the most positive)
    score = SIA.polarity_scores(sentence)["compound"]
    if score > 0:
        positive_text.append(sentence)
    if score < 0:
        negative_text.append(sentence)
    # print(sentence)
    # print(str(score))