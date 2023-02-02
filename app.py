from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'frase' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'

        msg.body(quote)
        responded = True

    if 'gato' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True

    if not responded:
        msg.body('Disculpe, solo conocemos de frases famosas y gatos !')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)
