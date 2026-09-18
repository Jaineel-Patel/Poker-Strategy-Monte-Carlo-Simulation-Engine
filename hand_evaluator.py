from itertools import combinations


RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def evaluate_five(cards):
    ranks = sorted(
        [RANK_VALUES[card.rank] for card in cards],
        reverse=True
    )

    suits = [card.suit for card in cards]

    counts = {}

    for rank in ranks:
        counts[rank] = counts.get(rank, 0) + 1

    count_values = sorted(counts.values(), reverse=True)

    # Flush
    is_flush = len(set(suits)) == 1

    # Straight
    unique_ranks = sorted(set(ranks), reverse=True)

    is_straight = False
    straight_high = None

    if len(unique_ranks) == 5:
        if unique_ranks[0] - unique_ranks[4] == 4:
            is_straight = True
            straight_high = unique_ranks[0]

        # A-2-3-4-5
        elif unique_ranks == [14, 5, 4, 3, 2]:
            is_straight = True
            straight_high = 5

    # Straight flush
    if is_straight and is_flush:
        return (8, straight_high)

    # Four of a kind
    if 4 in count_values:
        four = max(rank for rank, count in counts.items() if count == 4)
        kicker = max(rank for rank, count in counts.items() if count != 4)

        return (7, four, kicker)

    # Full house
    if 3 in count_values and 2 in count_values:
        three = max(rank for rank, count in counts.items() if count == 3)
        pair = max(rank for rank, count in counts.items() if count == 2)

        return (6, three, pair)

    # Flush
    if is_flush:
        return (5, *ranks)

    # Straight
    if is_straight:
        return (4, straight_high)

    # Three of a kind
    if 3 in count_values:
        three = max(rank for rank, count in counts.items() if count == 3)

        kickers = sorted(
            [rank for rank, count in counts.items() if count == 1],
            reverse=True
        )

        return (3, three, *kickers)

    # Two pair
    pairs = sorted(
        [rank for rank, count in counts.items() if count == 2],
        reverse=True
    )

    if len(pairs) == 2:
        kicker = max(
            rank for rank, count in counts.items()
            if count == 1
        )

        return (2, pairs[0], pairs[1], kicker)

    # One pair
    if len(pairs) == 1:
        pair = pairs[0]

        kickers = sorted(
            [rank for rank, count in counts.items() if count == 1],
            reverse=True
        )

        return (1, pair, *kickers)

    # High card
    return (0, *ranks)


def evaluate_hand(cards):
    if len(cards) != 7:
        raise ValueError("Texas Hold'em hand must contain 7 cards")

    best_score = None

    for five_cards in combinations(cards, 5):
        score = evaluate_five(five_cards)

        if best_score is None or score > best_score:
            best_score = score

    return best_score
