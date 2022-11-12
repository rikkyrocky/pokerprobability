import random

# pocket and community are lists of cards in the following format [d1,s6,h13,c3]

def dictify(pocket, community):
    hand_info = {}
    hand = pocket
    for i in range(len(community)):
        hand.append(community[i])
    hand_dict = []
    suits = []
    numbers = []
    for card in hand:
        suits.append(card[0])
        numbers.append(int(card[1:]))
        hand_dict.append([card[0],int(card[1:])])
    hand_info["hand"] = hand_dict
    hand_info["suits"] = suits
    hand_info["numbers"] = numbers
    return hand_info

def is_royal_flush(pocket,community,status):
    hand_info = dictify(pocket, community)
    if status == "opening":
        return true, 0
    elif status == "flop":
        if hand_info['suits']



#players is a dictionary with each player's hand, flop is a list of the cards that have been dealt
def poker_equity(players,community):

    if len(community) == 3:
        status = "flop"
    elif len(community) == 0:
        status = "opening"
    elif len(community) == 4:
        status = "turn"
    else:
        status = "board"
    hands = {"Royal Flush":,}
