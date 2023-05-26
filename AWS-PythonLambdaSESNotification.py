import boto3

def lambda_handler(event, context):
    # Create an SES client
    ses_client = boto3.client('ses')
    
    # Configure the email parameter variables to be used in the rest of the Lambda Function
    sender = # enter verified email in SES1
    recipient = # enter verified email in SES2
    subject = 'Email Notification from Lambda'
    body_text = 'Please work on the first try!'
    body_html = '<html><body><h1>Email Notification from Lambda</h1><p>Please work on the first try!</p></body></html>'
    
    # Send the email
    response = ses_client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body_text
                },
                'Html': {
                    'Data': body_html
                }
            }
        }
    )
    
    # Print the message ID if the email was sent successfully
    print('Email sent successfully. Message ID: ' + response['MessageId'])
