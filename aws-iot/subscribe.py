import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)

ENDPOINT = 'a27z9is7zojvpl-ats.iot.us-east-1.amazonaws.com'
ROOT_CA_PATH = './aws-iot/certificates/AmazonRootCA1.pem'
PRIVATE_KEY_PATH = './aws-iot/certificates/5152df46d4789f28fb04d198519a7c4ea9bc1d2e40ba218e158e8a041332b23d-private.pem.key'
CERTIFICATE_PATH = './aws-iot/certificates/5152df46d4789f28fb04d198519a7c4ea9bc1d2e40ba218e158e8a041332b23d-certificate.pem.crt'


myMQTTClient = AWSIoTMQTTClient("LaxTrackr")
myMQTTClient.configureEndpoint(ENDPOINT, 8883)
myMQTTClient.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERTIFICATE_PATH)

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("general/outbound", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("general/outbound")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")