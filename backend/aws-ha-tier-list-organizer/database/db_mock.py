# This mock consists of:
# a unique party id
# Each party id has tierlists of different members of the party (each member has a unique name too)


db = {
    "party_1_id": {
        "party_name": "Party 1",
        "members": {
            "member_1_id": {
                "member_name": "raulsao",
                "tier_list": {
                    "Hecarim": 4,
                    "Aatrox": 4,
                    "Morgana": 2,
                    "Neeko": 0
                }
            },
            "member_2_id": {
                "member_name": "Caio",
                "tier_list": {
                    "Hecarim": 3,
                    "Aatrox": 4,
                    "Morgana": 3,
                    "Neeko": 1
                }
            },
            "member_3_id": {
                "member_name": "Wolf",
                "tier_list": {
                    "Hecarim": 3,
                    "Aatrox": 4,
                    "Morgana": 2,
                    "Neeko": 0
                }
            },
            "member_4_id": {
                "member_name": "André",
                "tier_list": {
                    "Volibear": 4,
                    "Morgana": 4,
                    "Lux": 4,
                    "Yumi": 4
                }
            }
        }
    },
    "party_2_id": {
        "party_name": "Party 2",
        "members": {
            "member_1_id": {
                "member_name": "vini",
                "tier_list": {}
            },
            "member_2_id": {
                "member_name": "Clara",
                "tier_list": {}
            },
            "member_3_id": {
                "member_name": "Du",
                "tier_list": {}
            }
        }
    },
}