from utils import translate_tier_to_number
from config import parties_table_name
from http import HTTPStatus
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(parties_table_name)

def lambda_handler(event, context):
    """
    Receives from the body:
    party_name: str,
    member_name: str
    tierlist: dict
    """

    body = json.loads(event["body"])
    party = body["party_name"]
    member = body["member_name"]
    raw_tier_list = body["tierlist"]

    tier_list = {}
    for character, tier in raw_tier_list.items():
        number = translate_tier_to_number(tier)
        if number is None:
            return {
                "statusCode": HTTPStatus.NOT_FOUND,
                "body": f"TIER NOT FOUND: {tier}"
            }
        
        tier_list[character] = number
    
    keys = { "party_name": party }
    response = table.get_item(Key=keys)

    if 'Item' not in response:
        return {
            "statusCode": HTTPStatus.NOT_FOUND,
            "body": "Party not found."
        }

    update_expression = """
    SET
    members.#member = :new_tier_list
    """

    expression_names = {
        "#member": member
    }

    expression_values = {
       ":new_tier_list": tier_list
    }

    response = table.update_item(
        Key={"party_name": party},
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_names,
        ExpressionAttributeValues=expression_values,
        ReturnValues='ALL_NEW'
    )

    updated = response.get("Attributes", {})
    if len(updated) == 0:
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": "Tier-list was not registered."
        }

    return {
        "statusCode": HTTPStatus.OK,
        "body": "Tier-list registered successfully."
    }