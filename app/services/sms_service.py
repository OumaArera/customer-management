import africastalking
from flask import current_app

def send_sms(to, message):
    africastalking.initialize(
        username=current_app.config['AFRICASTALKING_USERNAME'],
        api_key=current_app.config['AFRICASTALKING_API_KEY']
    )
    sms = africastalking.SMS
    try:
        response = sms.send(message, [to])
        return response
    except Exception as e:
        return str(e)
