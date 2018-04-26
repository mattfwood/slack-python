from slackclient import SlackClient

slack_token = "xoxb-323196240915-8yexA1X0Gm2YX81hC3r5id3L"
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="C9H8G8ATC",
  text="Hello from Python! :tada:"
)
