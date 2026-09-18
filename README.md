# Poker Strategy & Monte Carlo Simulation Engine

I'm building a Texas Hold'em poker simulation in Python to explore how probability and decision-making can be applied to a game with incomplete information.

The main goal of the project is to build a poker bot that can estimate the probability of winning a hand and use those estimates to make decisions.

## What I'm Building

The project will be developed in several stages:

- Build a complete 52-card deck and poker game mechanics
- Evaluate poker hands and determine the winner
- Use Monte Carlo simulation to estimate hand equity
- Calculate pot odds and expected value
- Build a basic betting strategy
- Model opponent behaviour
- Compare different strategies through large-scale simulations

## Current Progress

### Completed
- Card class
- Deck class
- Card shuffling
- Dealing individual cards
- Dealing multiple cards

### In Progress
- Poker hand evaluation
- Monte Carlo simulation
- Decision-making strategy
- Opponent modelling

## How the Simulation Will Work

For example, suppose the bot has:

**A♠ K♠**

and the flop is:

**Q♠ 7♦ 2♠**

The bot knows its own cards and the community cards, but does not know the opponent's cards or the turn and river.

The Monte Carlo engine will simulate many possible combinations of:

1. Opponent cards
2. Turn card
3. River card

It will then evaluate the resulting hands and estimate:

- Probability of winning
- Probability of tying
- Probability of losing
- Overall hand equity

The bot can then use these estimates when making decisions.

## Project Structure

```text
poker_bot/
│
├── deck.py
├── hand_evaluator.py
├── simulator.py
├── strategy.py
├── opponent_model.py
├── main.py
│
└── README.md
