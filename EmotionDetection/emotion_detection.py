import requests
import json

def emotion_detector(text_to_analyse):
    #Define the URL for the emotion predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    #Set the headers with the required model ID for the API
    header = { "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock" }

    #POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        #Parse the response from the API
        formatted_response = json.loads(response.text)
        #JSON that contains emotions results
        emotions_score = formatted_response['emotionPredictions'][0]["emotion"]
        #Get the key with the dominant emotion
        dominant_key = max(emotions_score, key=emotions_score.get)
        #Add the dominant emotion key
        emotions_score['dominant_emotion'] = dominant_key

    elif response.status_code == 400:
        emotions_score = { 'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None }
    
    return emotions_score