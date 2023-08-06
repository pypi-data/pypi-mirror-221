
import os
from sendgrid.helpers.mail import Email, Personalization
from sendgrid import SendGridAPIClient
import urllib.parse

from datetime import datetime
from adafri.v1.user import User

VALIDATION_FIELD = '_emailValidationSendDate'
STATUS_FIELD = 'status'

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY');
REGISTRATION_TEMPLATE_ID = os.environ.get('REGISTRATION_TEMPLATE_ID')
PAYMENT_TEMPLATE_ID = os.environ.get('PAYMENT_TEMPLATE_ID')
EMAIL_VERIFICATION_TEMPLATE_ID = os.environ.get('EMAIL_VERIFICATION_TEMPLATE_ID')

def compareTimes(date_string: str):
    date_format = "%Y-%m-%d, %H:%M:%S"
    date = datetime.strptime(date_string, date_format);
    now = datetime.now();
    difference = now - date;
    days, seconds = difference.days, difference.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if minutes >= 5:
        return {"status": "ok", "difference": minutes};
    return {"status": "error", "difference": minutes};


def setTimeSended(user: User):
    date_format = "%Y-%m-%d, %H:%M:%S"
    now = datetime.now()
    date_obj = datetime.strftime(now, date_format)
    update_value = {};
    update_value[VALIDATION_FIELD] = date_obj
    update = user.document_reference().set(update_value, merge=True)
    if update['status']=='ok':
        return date_obj
    else:
        return None

def getTimeSended(user: User):
    statement = {};
    if user is None:
        statement[STATUS_FIELD]='error'
        statement[VALIDATION_FIELD]=None
        return statement
    user = user.to_json()
    if VALIDATION_FIELD in user:
        statement[STATUS_FIELD]='ok'
        statement[VALIDATION_FIELD]=user[VALIDATION_FIELD]
        return statement
    else:
        statement[STATUS_FIELD]='ok'
        statement[VALIDATION_FIELD]='now'
        return statement
    

class Mail:
    def __init__(self, from_text=None, destination=None, subject=None, custom_data=None, link=None):
        self.from_text = from_text;
        self.destination = destination;
        self.subject = subject;
        self.custom_data = custom_data;
        self.link = link;
    
    def sendgrid_client(self, _api_key=None):
        api_key = _api_key;
        if api_key is None:
            api_key = SENDGRID_API_KEY;
        return SendGridAPIClient(api_key);
    
    def sendMailRegistration(self, domain, _api_key=None, _template_id=None, bccs=[]):
        if domain is None:
            result = {'status_code': 400, 'message': 'Invalid domain' }
        result = None
        template_id = _template_id;
        if template_id is None:
            template_id = REGISTRATION_TEMPLATE_ID
        message = Mail(
            from_email=self.from_text+'@'+domain,
            to_emails=[self.destination],
            )
        try:
            message.template_id = template_id
            personalization = Personalization()
            for bcc in bccs:
                personalization.add_bcc(Email(bcc))
            message.add_personalization(personalization)
            response = self.sendgrid_client(_api_key=_api_key).send(message)
            if response.status_code==200 or response.status_code==202:
                result = {'status_code': response.status_code, 'message': 'Email sent successfully.' }
                print(result)
            else:
                result = {'status_code': response.status_code, 'message': 'An error occurated' }
        except Exception as e:
            print(e)
            result = {'status_code': 400, 'message': str(e) }
        
        return result
    
    def sendMailPaymentSuccess(self, domain, _api_key=None, _template_id=None, bccs=[]):
        if domain is None:
            result = {'status_code': 400, 'message': 'Invalid domain' }
        result = None
        message = Mail(
            )
        try:
            template_id = _template_id;
            if template_id is None:
                template_id = PAYMENT_TEMPLATE_ID
            message.from_email = self.from_text+'@'+domain
            message.template_id = template_id
            personalization = Personalization()
            personalization.dynamic_template_data = self.custom_data
            personalization.add_to(Email(self.destination))
            personalization.subject = self.subject
            for bcc in bccs:
                personalization.add_bcc(Email(bcc))
            message.add_personalization(personalization)
        
            response = self.sendgrid_client(_api_key).send(message) 
            if response.status_code==200 or response.status_code==202:
                result = {'status_code': response.status_code, 'message': 'Email sent successfully.' }
                print(result)
            else:
                result = {'status_code': response.status_code, 'message': 'An error occurated' }
        except Exception as e:
            print(e)
            result = {'status_code': 400, 'message': str(e) }
        
        return result
    
    def sendMailEmailVerfication(self, domain, _api_key=None, _template_id=None, bccs=[]):
        if domain is None:
            result = {'status_code': 400, 'message': 'Invalid domain' }
        result = None
        message = Mail()
        user_model = User().query([{"key": "email", "value": self.destination, "comp": "=="}], True);
        print(user_model)
        if user_model is not None and user_model.uid is None:
            return {'status_code': 400, 'message': 'User not exist' };
        uid = user_model.uid;
        try:
            template_id = _template_id;
            if template_id is None:
                template_id = os.environ.get('EMAIL_VERIFICATION_TEMPLATE_ID')
            time_sended = getTimeSended(uid);
            if time_sended['status']=='error':
                return {'status_code': 400, 'message': "User not exist"};
            print("Time sended: ", time_sended)
            if time_sended[VALIDATION_FIELD]!='now':
                compare = compareTimes(time_sended[VALIDATION_FIELD]);
                if compare['status'] == 'error':
                    return {'status_code': 400, 'message': f"Please wait {5 - compare['difference']} minutes and retry"};
            custom_data = {'link': urllib.parse.unquote(self.link)}
            message.from_email = self.from_text+'@'+domain
            message.template_id = template_id
            personalization = Personalization()
            personalization.dynamic_template_data = custom_data
            personalization.add_to(Email(self.destination))
            personalization.subject = self.subject
            for bcc in bccs:
                personalization.add_bcc(Email(bcc))
            message.add_personalization(personalization)
            response = self.sendgrid_client(_api_key).send(message) 
            print(response)
            if response.status_code==200 or response.status_code==202:
                update = setTimeSended(user_model);
                print("Update user: ", update)
                result = {'status_code': response.status_code, 'message': 'Email sent successfully.' }
                print(result)
            else:
                result = {'status_code': response.status_code, 'message': 'An error occurated' }
        except Exception as e:
            print(e)
            result = {'status_code': 400, 'message': str(e) }
        
        return result