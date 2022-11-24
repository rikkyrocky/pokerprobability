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

def flop_straight(hand_info):
    possible_straights = []
    for i in range(1, 10):
        straight_count = 0
        num_needed = []
        for a in range(5):
            num = i + a
            if num in hand_info["numbers"]:
                straight_count += 1
            else:
                num_needed.append(num)
        if straight_count == 5:
            possible_straights.append([i, None])
        elif straight_count >= 3:
            possible_straights.append([i,num_needed])
    return possible_straights
#print(dictify(['d1','s6'], ['h3','c4','c5']))


def flop_flush(hand_info):
    possible_flush = []
    suit_count = {}
    for suit in hand_info["suits"]:
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1
    for suit in suit_count:
        if suit_count[suit] == 5:
            possible_flush.append([suit, None])
        elif suit_count[suit] >= 3:
            possible_flush.append([suit, 5-suit_count[suit]])
    return possible_flush

def diagnostic(pocket, community):
    hand_info = dictify(pocket, community)
    print(hand_info)
    print("flush", flop_flush(hand_info))
    print("straight", flop_straight(hand_info))

def flop_straight_flush(hand_info):
    if flop_flush(hand_info) and flop_straight(hand_info):
        print("both")

print(diagnostic(['c1','h12'], ['s1','s11','s7']))

'''def is_pattern(pocket,community,status):
    patterns = []
    hand_info = dictify(pocket, community)
    if status == "opening":
        return true, 0, 0
    elif status == "flop":






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
    hands = {"Royal Flush":,}'''
