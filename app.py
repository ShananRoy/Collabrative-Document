from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)
fake= Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID="ACf675ca19550fd63315c485b8a9357225"
    TWILIO_SYNC_SERVICE_SID="IS9e506ba52a9b5673bdb2c240e341565e"
    TWILIO_API_KEY="SKfc590db01de8547339a3eb2502d4482f"
    TWILIO_API_SECRET="HUH75YLX5SE9uZlPvgHkiURmKthMAT5S"

    username= request.args.get('username', fake.user_name())

    token= AccessToken(TWILIO_ACCOUNT_SID,TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)

    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

if __name__ == "__main__":
    app.run()

