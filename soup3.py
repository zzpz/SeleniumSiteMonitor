import boto3
from dotenv import load_dotenv, dotenv_values

# load environment variables from .env file
load_dotenv()
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


# print the response


def sendMSG(msg):
    # create an SNS client
    sns = boto3.client("sns")
    topic_arn = config["TOPIC_ARN"]
    # publish a message to the topic
    response = sns.publish(
        TopicArn=topic_arn, Message=(msg if msg else "It's Happening")
    )
    print(response)
