# Poker Strategy & Monte Carlo Simulation

A Python project that simulates Texas Hold'em poker and uses Monte Carlo simulation to estimate the probability of winning a hand.

## What the Project Does

The program:

- Creates and shuffles a standard 52-card deck
- Deals hole cards and community cards
- Evaluates poker hands and determines the strongest possible 5-card combination
- Simulates thousands of possible opponent hands and future community cards
- Estimates win, tie and loss probabilities
- Calculates overall hand equity
- Uses pot odds and expected value to explore poker decision-making

## Monte Carlo Simulation

At any point in a poker hand, some information is unknown. For example, after the flop, the opponent's cards, turn and river are unknown.

The simulation repeatedly generates possible outcomes and evaluates the resulting hands.

For each simulation:

1. Generate a possible opponent hand
2. Generate the remaining community cards
3. Evaluate the player's hand
4. Evaluate the opponent's hand
5. Record the outcome

After many simulations, the program estimates:

- Win probability
- Tie probability
- Loss probability
- Hand equity

Equity is calculated as:

\[
Equity = P(Win) + \frac{1}{2}P(Tie)
\]

## Example

For a given hand and flop, the program produces output such as:

```text
Bot hand:
Q♥
K♦

Flop:
5♣
6♦
8♦

Simulation results:
Win probability: 0.4024
Tie probability: 0.0314
Loss probability: 0.5662
Equity: 0.4181
