def pot_odds(pot, call_amount):
    final_pot = pot + call_amount

    return call_amount / final_pot
def expected_value(equity, pot, call_amount):
    final_pot = pot + call_amount

    win_value = equity * final_pot
    cost = call_amount

    return win_value - cost
def choose_action(equity, pot, call_amount):

    required_equity = pot_odds(
        pot,
        call_amount
    )

    if equity > required_equity:
        return "CALL"

    return "FOLD"
