import pdb
from flask import Flask
from flask import request
from slackclient import SlackClient
import json

app = Flask(__name__)

slack_token = "xoxb-323196240915-8yexA1X0Gm2YX81hC3r5id3L"
sc = SlackClient(slack_token)

@app.route("/", methods=['GET'])
def hello():
  channels = sc.api_call("channels.list")
  return json.dumps(channels)

@app.route('/', methods=['POST'])
def message():
  print(request.data)
  payload = json.loads(request.data)
  sc.api_call(
    "chat.postMessage",
    channel="C9H8G8ATC",
    text=payload["message"]
  )
  return "Success"
