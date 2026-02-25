from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if "hello" in incoming_msg:
        msg.body("Hi 👋 Welcome!")
    elif "menu" in incoming_msg:
        msg.body("1. About us\n2. Contact\n3. Prices")
    elif "help" in incoming_msg:
        msg.body("Send 'menu' to see options.")
    else:
        msg.body("Sorry, I didn't understand that.")

    return str(response)

if __name__ == "__main__":
    app.run()
