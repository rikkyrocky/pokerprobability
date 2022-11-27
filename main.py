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
    if len(hand_info['hand']) == 2:
        num1 = hand_info['hand'][0][1]
        num2 = hand_info['hand'][1][1]
        if num1 > num2:
            n1large =True
            diff = num1 - num2
        else:
            n1large = False
            diff = num2 - num1
        if diff <= 4:
            for i in range(1, 10):
                num_needed = []
                start = i
                if (num1 in range(start, start+5)) and (num2 in range(start, start+5)):
                    for number in range(start, start+5):
                        num_needed.append(number)
                    num_needed.remove(num1)
                    num_needed.remove(num2)
                    possible_straights.append([start, num_needed])
    else:
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
                possible_straights.append([i, num_needed])
    return possible_straights
# print(dictify(['d1','s6'], ['h3','c4','c5']))


def flop_flush(hand_info):
    possible_flush = []
    suit_count = {}
    if len(hand_info['hand']) == 2:
        if hand_info['hand'][0][0] == hand_info['hand'][1][0]:
            possible_flush.append([hand_info['hand'][0][0], 3])
    else:
        for suit in hand_info["suits"]:
            if suit in suit_count:
                suit_count[suit] += 1
            else:
                suit_count[suit] = 1
        for suit in suit_count:
            if suit_count[suit] >= 5:
                possible_flush.append([suit, None])
            elif suit_count[suit] >= 3:
                possible_flush.append([suit, 5-suit_count[suit]])
    return possible_flush


def diagnostic(pocket, community):
    hand_info = dictify(pocket, community)
    print(hand_info)
    print("flush", flop_flush(hand_info))
    print("straight", flop_straight(hand_info))
    print("straight flush", flop_straight_flush(hand_info))
    print("of a kind", of_a_kind(hand_info))
    print(fh2p(hand_info))

def flop_straight_flush(hand_info):
    possible_straight_flush = []
    SUITS = ['d','s','h','c']
    if flop_flush(hand_info) and flop_straight(hand_info) and len(hand_info['hand']) == 2:
        if hand_info['hand'][0][0] == hand_info['hand'][1][0]:
            for straight in flop_straight(hand_info):
                cards_needed = []
                for i in straight[1]:
                    cards_needed.append([hand_info['hand'][0][0], i])
                possible_straight_flush.append([straight[0],cards_needed])
    elif flop_flush(hand_info) and flop_straight(hand_info):
        straight_index = -1
        straight_cards = flop_straight(hand_info)
        for straight in straight_cards:
            #print("straight", straight)
            cards_needed = []
            sf_card = []
            straight_index += 1
            start = straight[0]
            for card_number in range(start, start+5):
                '''if straight_cards[straight_index][1] == None:
                    for card in hand_info["hand"]:
                        if card[1] == card_number:
                            sf_card.append(card)
                elif not (card_number in straight_cards[straight_index][1]):
                    for card in hand_info["hand"]:
                        if card[1] == card_number:
                            sf_card.append(card)'''
                for card in hand_info["hand"]:
                    if card[1] == card_number:
                        sf_card.append(card)
            #print(sf_card)
            suit1 = ''
            for suit in SUITS:
                suit_cards = []
                for card in sf_card:
                    if suit == card[0]:
                        suit_cards.append(card)
                #print(suit_cards, "SC")
                if len(suit_cards) >= 3:
                    suit1=suit
                    #print(suit1)
                    break
            nums = []
            if suit1:
                for card in suit_cards:
                    nums.append(card[1])
                for i in range(start, start+5):
                        if not (i in nums):
                            #print(i, nums)
                            cards_needed.append([suit1, i])
                if not cards_needed:
                    straight_flush = [start, None]
                else:
                    straight_flush = [start, cards_needed]
                possible_straight_flush.append(straight_flush)
    return possible_straight_flush

def of_a_kind(hand_info):
    pair_triple = []
    card_count = {}
    for num in hand_info["numbers"]:
        if num in card_count:
            card_count[num] += 1
        else:
            card_count[num] = 1
    for number in card_count:
        if card_count[number] == 2:
            pair_triple.append(["pair", number])
        elif card_count[number] == 3:
            pair_triple.append(["triple", number])
        elif card_count[number] == 4:
            pair_triple.append(["quad", number])
    return pair_triple

def fh2p(hand_info):
    fh2p = []
    pnum = []
    hands = []
    pair = 0
    if len(of_a_kind(hand_info)) > 1:
        for pattern, number in of_a_kind(hand_info):
            hands.append(pattern)
            if pattern == "pair":
                pair += 1
                pnum.append(number)
            if pattern == "triple":
                tnum = number
        if pair > 1:
            if len(pnum) > 2:
                pnum.remove(min(pnum))
            fh2p.append(["2p",pnum])
        if "pair" in hands and "triple" in hands:
            fh2p.append(["fh", [tnum,max(pnum)]])
    return fh2p




print(diagnostic(['h3','h5'], ['h4','d3','c5','d4']))


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
