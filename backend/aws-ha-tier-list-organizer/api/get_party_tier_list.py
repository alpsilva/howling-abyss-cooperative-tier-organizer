from utils import average_character_tier, TIERS
from config import parties_table_name
from http import HTTPStatus
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(parties_table_name)

def lambda_handler(event, context):
    """
    Receives from the body:
    party_id: str
    Returns all the characters grouped by their averaged tier
    """

    path_params = event.get("pathParameters", {})
    party_name = path_params.get("party_name", None)

    if party_name is None:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "party_name id not specified."
        }

    keys = { "party_name": party_name }
    response = table.get_item(Key=keys)

    party = response.get("Item", None)
    if party is None:
        return {
            "statusCode": HTTPStatus.NOT_FOUND,
            "body": "Party not found."
        }

    members = party.get("members", {})

    tier_lists = []
    for member_tier_list in members.values():
        tier_lists.append(member_tier_list)

    avg_character_tier = average_character_tier(tier_lists)

    output = { tier: [] for tier in TIERS }
    for character, avg_tier in avg_character_tier.items():
        output[avg_tier].append(character)
    
    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(output)
    }