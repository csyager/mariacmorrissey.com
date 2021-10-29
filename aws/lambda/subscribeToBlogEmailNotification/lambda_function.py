import json
import boto3

ses = boto3.client('sesv2')

def lambda_handler(event, context):
    email_address=event["email"]
    try:
        response = ses.create_contact(
            ContactListName="BlogContactList",
            EmailAddress=email_address,
            TopicPreferences=[{
                "TopicName": "BlogPosts",
                "SubscriptionStatus": "OPT_IN"
            }]
        )
    except ses.exceptions.AlreadyExistsException as e:
        response = ses.update_contact(
            ContactListName='BlogContactList',
            EmailAddress=email_address,
            TopicPreferences=[
                {
                    'TopicName': 'BlogPosts',
                    'SubscriptionStatus': 'OPT_IN'
                },
            ]
        )
        
    response_status = response['ResponseMetadata']['HTTPStatusCode']
    if response_status == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully added email to contact list')
        }
    else:
        return {
            'statusCode': response_status,
            'body': json.dumps('Email not added to contact list')
            
        }
