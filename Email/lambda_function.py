import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the correct region name
REGION = "eu-north-1"  # Correct region for Stockholm
client = boto3.client('ses', region_name=REGION)

def lambda_handler(event, context):
    logging.info(event)  # Log the event for debugging purposes

    try:
        # Extract email information from the event
        source_email = event["from"]
        to_email = event["to"]
        message = event["message"]
        title = event["title"]

        # Send email using SES
        response = client.send_email(
            Source=source_email,  # Use the source email passed in the event
            Destination={
                'ToAddresses': to_email  # Use the recipient emails passed in the event
            },
            Message={
                'Subject': {
                    'Data': title,
                },
                'Body': {
                    'Text': {
                        'Data': message
                    },
                    'Html': {
                        'Data': f'<b>{message}</b>'  # Correct the HTML formatting
                    }
                }
            }
        )

        logging.info(f"Email sent successfully: {response}")

    except Exception as e:
        logging.error(f"Error sending email: {e}")

