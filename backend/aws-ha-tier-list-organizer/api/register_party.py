from config import parties_table_name
from http import HTTPStatus
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(parties_table_name)

def lambda_handler(event, context):
    """
    Receives from the body:
    party_name
    If the party name is unique, inserts it into the DB.
    """

    body = json.loads(event["body"])
    party_name = body["party_name"]
    
    keys = { "party_name": party_name }
    response = table.get_item(Key=keys)

    if 'Item' in response:
        return {
            "statusCode": HTTPStatus.FORBIDDEN,
            "body": "Party name already in use."
        }

    new_party = {
        "party_name": party_name,
        "members": {}
    }

    response = table.put_item(Item=new_party)

    return {
        "statusCode": HTTPStatus.OK,
        "body": "Party registered successfully."
    }