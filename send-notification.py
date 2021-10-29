import json
import boto3
import sys

ses = boto3.client('sesv2')

def main():
    title = sys.argv[1]
    url = sys.argv[2]
    additional_message = sys.argv[3]
    contacts = ses.list_contacts(
        ContactListName='BlogContactList',
        Filter={
            'FilteredStatus': 'OPT_IN'
        }
    )
    successes = []
    failures = []
    for contact in contacts['Contacts']:
        email_address = contact['EmailAddress']
        response = ses.send_email(
            FromEmailAddress='notification@mariacmorrissey.com',
            Destination={
                'ToAddresses': [
                    email_address
                ]
            },
            ReplyToAddresses=[
                'mariamorrissey24@gmail.com'    
            ],
            FeedbackForwardingEmailAddress='mariamorrissey24@gmail.com',
            Content={
                'Template': {
                    'TemplateName': 'PostNotificationTemplate',
                    'TemplateData': f"{{ \"title\":\"{title}\", \"url\":\"{url}\", \"additional_message\":\"{additional_message}\" }}"
                }
            },
            ListManagementOptions={
                'ContactListName': 'BlogContactList',
                'TopicName': 'BlogPosts'
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            successes.append(email_address)
        else:
            failures.append(email_address)
        
    return {
        'successes': successes,
        'failures': failures
    }

if __name__ == '__main__':
    print(main())