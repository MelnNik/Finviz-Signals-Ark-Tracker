"""
import urllib.request
import json

FOR FURTHER DJANGO APP

listing = report[report.index.duplicated()]

indexes = list(dict.fromkeys(report.index.tolist()))

print(indexes)
print(listing)

for index in indexes:
    url = f'https://api.polygon.io/v1/meta/symbols/{index}/news?perpage=10&page=1&apiKey=dv0fVWsBEP83mlaLWcnPlQrQxNkAHcov'
    response = urllib.request.urlopen(
        url)
    decoded_data = json.loads(response.read().decode("utf-8"))
    time.sleep(1)
    for i in range(10):
        print(decoded_data[i]['summary'])


def sentiment(stock, api):
    # LOADING TRADERVIEW
    url = 'https://www.tradingview.com/screener/'

    # LOADING FLAIR
    flair_sentiment = flair.models.TextClassifier.load('en-sentiment')

    # NEWSAPI API call
    newsapi = NewsApiClient(api_key='a55c6ba73d7a4d05982624aabebdc375')

    # GET THE ARTICLES
    response = newsapi.get_everything(qintitle=stock)

    # SPECIFY API CALL INSIDE THE FUNCTION
    news = api.polygon.news(stock)

    # OPEN NEWS.TXT TO WRITE NEWS
    file = open('news.txt', 'w')

    # VERIFY SENTIMENT VARIABLE IS 0
    sentiment = 0
    print(response)
    # ITERATES THROUGH EVERY NEWS ARTICLE FROM NEWS API
    for line in response['articles']:
        words = str(line['title'])
        file.write(words)
        # RUNS FLAIR SENTIMENT ANALYSIS
        sentence = Sentence(str(words))
        flair_sentiment.predict(sentence)
        total_sentiment = sentence.labels
        print(str(words))

        # Checks to see if the sentiment is negative and subtracts by how negative flair thinks it is
        if total_sentiment[0].value == 'NEGATIVE':
            total_sentiment[0].to_dict()['confidence']
            # Flair favors negative outcomes
            sentiment -= total_sentiment[0].to_dict()['confidence']

        # Checks to see if the sentiment is positive and adds how positive flair thinks it is
        elif total_sentiment[0].value == 'POSITIVE':
            total_sentiment[0].to_dict()['confidence']
            sentiment += total_sentiment[0].to_dict()['confidence']

    # ITERATES THROUGH EVERY NEWS ARTICLE FROM POLYGON.IO
    for source in news:
        words = source.summary
        try:
            file.write(words)
        except:
            print('FAILSAFE ACTIVATED')
        file.write('\n')

        # Runs Flair sentiment analysis
        sentence = Sentence(str(words))
        try:
            flair_sentiment.predict(sentence)
        except:
            print("\n")
        total_sentiment = sentence.labels
        print(str(words))

        # Checks to see if the sentiment is negative and subtracts by how negative flair thinks it is
        if total_sentiment[0].value == 'NEGATIVE':
            total_sentiment[0].to_dict()['confidence']
            # Flair favors negative outcomes
            sentiment -= total_sentiment[0].to_dict()['confidence']

        # Checks to see if the sentiment is positive and adds how positive flair thinks it is
        if total_sentiment[0].value == 'POSITIVE':
            total_sentiment[0].to_dict()['confidence']
            sentiment += total_sentiment[0].to_dict()['confidence']

    file.close()
    print('Total sentiment', sentiment)


sentiment('BLNK', api)
"""