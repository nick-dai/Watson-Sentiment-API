#!/usr/bin/python
import requests
from Credentials import username, password

sentiment = {
    'text': 'Natural Language Understanding is a collection of APIs that offer text analysis through natural language processing. This set of APIs can analyze text to help you understand its concepts, entities, keywords, sentiment, and more.',
    'features': {
        'sentiment': {
            'document': 'true'
        }
    }
}

sentiment_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-03-16'

r = requests.post(sentiment_url, auth=(username, password), json=sentiment)
print(r.text)
