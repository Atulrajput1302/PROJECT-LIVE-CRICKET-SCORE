#Sending WhatsApp messages

from twilio.rest import Client

whatsapp_message = 'Hello! This is a TEST MESSAGE'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#1
a_sid = "ACbfe4b9167845fa577c1288af9541f3c0"

#2
auth_token = "18e3b0adc8c6b80077bfea596304196c"

#3
client = Client(a_sid, auth_token)

#4
messages = client.messages.create(body=whatsapp_message, from_="whatsapp:+14155238886", to="whatsapp:+91 9939867080")
