class OpponentModel:

    def __init__(self):
        self.hands = 0
        self.raises = 0
        self.calls = 0
        self.folds = 0

    def record_action(self, action):

        self.hands += 1

        if action == "raise":
            self.raises += 1

        elif action == "call":
            self.calls += 1

        elif action == "fold":
            self.folds += 1

    def raise_probability(self):

        if self.hands == 0:
            return 0

        return self.raises / self.hands

    def fold_probability(self):

        if self.hands == 0:
            return 0

        return self.folds / self.hands
