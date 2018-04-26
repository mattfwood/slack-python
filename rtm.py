import time
import pprint
import pdb
from slackclient import SlackClient
import commands

slack_token = "xoxb-323196240915-8yexA1X0Gm2YX81hC3r5id3L"
sc = SlackClient(slack_token)

if sc.rtm_connect():
    while sc.server.connected is True:
        events = sc.rtm_read()
        if events:
            event = events[0]
            # set type to false if key doesn't exist
            type = event.get('type', False)
            if type == 'message':
              channel = event['channel']
              message = event['text']
              response_message = commands.reply(message)
              sc.rtm_send_message(channel, response_message)
              print message
        time.sleep(1)

else:
    print('Connection Failed')
