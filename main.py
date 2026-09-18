from deck import Deck
from simulator import monte_carlo_equity
from strategy import choose_action


def main():

    deck = Deck()
    deck.shuffle()

    bot_hand = deck.deal_hand(2)
    opponent_hand = deck.deal_hand(2)

    flop = deck.deal_hand(3)

    print("Bot hand:")

    for card in bot_hand:
        print(card)

    print("\nFlop:")

    for card in flop:
        print(card)

    result = monte_carlo_equity(
        bot_hand,
        flop,
        simulations=10000
    )

    print("\nSimulation results:")
    print("Win probability:",
          result["win_probability"])

    print("Tie probability:",
          result["tie_probability"])

    print("Loss probability:",
          result["loss_probability"])

    print("Equity:",
          result["equity"])


if __name__ == "__main__":
    main()
