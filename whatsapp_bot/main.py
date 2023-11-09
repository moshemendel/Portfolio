from twilio.rest import Client

account_sid = 'AC37db6360c72add3457267120247fe738'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+972549084308'
)

print(message.sid)