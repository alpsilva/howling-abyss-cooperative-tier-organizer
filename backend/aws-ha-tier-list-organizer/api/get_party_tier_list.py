from utils import average_character_tier, TIERS
from database import db_mock
from http import HTTPStatus
import json

def lambda_handler(event, context):
    """
    Receives from the body:
    party_id: str
    Returns all the characters grouped by their averaged tier
    """

    db = db_mock.db
    
    path_params = event.get("pathParameters", {})
    party = path_params.get("party_id", None)

    if party is None:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "party id not specified."
        }

    members = db[party]["members"]

    tier_lists = []
    for member_info in members.values():
        tier_lists.append(member_info["tier_list"])

    avg_character_tier = average_character_tier(tier_lists)

    response = { tier: [] for tier in TIERS }
    for character, avg_tier in avg_character_tier.items():
        response[avg_tier].append(character)
    
    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(response)
    }