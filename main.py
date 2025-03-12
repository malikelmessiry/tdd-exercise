VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    if len(hand) >= 2 and len(hand) < 6:
        for card in hand:
            if card not in VALID_CARDS:
                return "Invalid"   
                break 
            elif card == "Jack" or card == "Queen" or card == "King":
                card = 10
            elif card == "Ace" and score <= 10:
                card = 11
            elif card == "Ace" and score > 10:
                card = 1
            score += card
            print(score)
            if score > 21 and hand.count("Ace") > 1:
                score -= 10
            elif score > 21:
                return "Bust"
    else:
        return "Invalid"
    return score

print(blackjack_score(["Ace", "Ace", 10]))