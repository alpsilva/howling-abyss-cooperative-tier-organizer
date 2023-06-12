
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

def avg(l: list):
    """ Receives a list of numbers and returns the avg. """
    result = 0
    if len(l) > 0:
        result = sum(l) / len(l)
    return result

def average_character_tier(tier_lists: list):
    """
    Receives a list of dicts, containing members tier lists.
    Returns a single tier list with the average tier of each character.
    """
    average_tier_list = {}

    for tier_list in tier_lists:
        for character, tier in tier_list.items():
            if character not in average_tier_list:
                average_tier_list[character] = []
            average_tier_list[character].append(tier)
    
    return {
        character: translate_number_to_tier(round(avg(tiers)))
        for character, tiers
        in average_tier_list.items()
    }

    