''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer


#Initiate the flask app : TODO
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
#This code receives the text from the HTML interface and 
#runs sentiment analysis over it using sentiment_analysis()
#function. The output returned shows the label and its confidence 
#score for the provided text.

    # TODO
def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    return response.text

@app.route("/")
def render_index_page():
#This function initiates the rendering of the main application page over the Flask channel

    return render_template('index.html')
    
    
if __name__ == "__main__":
#This functions executes the flask app and deploys it on localhost:5000
    app.run(debug=True)
