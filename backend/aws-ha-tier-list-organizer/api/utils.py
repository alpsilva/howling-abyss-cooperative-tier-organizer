
TIERS = ["D", "C", "B", "A", "S"]

TIER_TO_NUMBER = {}
NUMBER_TO_TIER = {}
for index, tier in enumerate(TIERS):
    TIER_TO_NUMBER[tier] = index
    NUMBER_TO_TIER[index] = tier

def translate_tier_to_number(tier: str):
    """
    Translates the tier to it's assigned number.
    If the tier does not exist, return None.
    """
    if tier not in TIER_TO_NUMBER:
        return None
    return TIER_TO_NUMBER[tier]

def translate_number_to_tier(number: int):
    """
    Translates the assigned number to it's tier.
    If the number does not exist, return None.
    """
    if number not in NUMBER_TO_TIER:
        return None
    return NUMBER_TO_TIER[number]