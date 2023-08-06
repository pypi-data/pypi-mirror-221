from flask import Flask, request, jsonify
from tonb import TONBApiClient


app = Flask(__name__)

client = TONBApiClient(
    "https://merchant-app-api2.tonb.io", "YOUR_API_KEY", "YOUR_MERCHANT_ID"
)


@app.route("/webhook", methods=["POST"])
def handle_webhook():
    try:
        # Use the handler to validate and parse the webhook data
        data = client.handle_request(request)
        # If the data is valid, you can continue processing it
        print(data)
        # This could involve updating your database, triggering other actions, etc.
        return jsonify({"message": "Webhook received and validated successfully."}), 200
    except ValueError:
        # If the data is not valid, respond with an error status
        return jsonify({"message": "Invalid webhook data."}), 400


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
