from deck import Deck
from hand_evaluator import evaluate_hand


def monte_carlo_equity(
    player_hand,
    community_cards,
    simulations=10000
):
    wins = 0
    ties = 0
    losses = 0

    for _ in range(simulations):

        deck = Deck()

        known_cards = player_hand + community_cards

        deck.cards = [
            card for card in deck.cards
            if card not in known_cards
        ]

        deck.shuffle()

        opponent_hand = deck.deal_hand(2)

        remaining_community = 5 - len(community_cards)

        future_cards = deck.deal_hand(remaining_community)

        final_community = community_cards + future_cards

        player_score = evaluate_hand(
            player_hand + final_community
        )

        opponent_score = evaluate_hand(
            opponent_hand + final_community
        )

        if player_score > opponent_score:
            wins += 1

        elif player_score == opponent_score:
            ties += 1

        else:
            losses += 1

    win_probability = wins / simulations
    tie_probability = ties / simulations
    loss_probability = losses / simulations

    equity = (wins + 0.5 * ties) / simulations

    return {
        "win_probability": win_probability,
        "tie_probability": tie_probability,
        "loss_probability": loss_probability,
        "equity": equity
    }
