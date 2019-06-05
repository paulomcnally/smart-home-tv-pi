from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from listener import Listener
import os

pnConfig = PNConfiguration()
pnConfig.subscribe_key = os.environ['SUB_KEY']
pnConfig.publish_key = os.environ['PUB_KEY']
pnConfig.ssl = False

pubNub = PubNub(pnConfig)

my_listener = Listener()

pubNub.add_listener(my_listener)

pubNub.subscribe().channels('tv').execute()
