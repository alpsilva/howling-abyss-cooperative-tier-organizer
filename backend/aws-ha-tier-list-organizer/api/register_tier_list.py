import json
from utils import translate_tier_to_number
from database import db_mock
from http import HTTPStatus

def lambda_handler(event, context):
    """
    Receives from the body:
    party_id: str,
    member_id: str
    tierlist: dict
    """

    db = db_mock.db
    
    body = json.loads(event["body"])
    party = body["party_id"]
    member = body["member_id"]
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
    
    db[party]["members"][member]["tier_list"] = tier_list

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(db[party]["members"][member]["tier_list"])
    }