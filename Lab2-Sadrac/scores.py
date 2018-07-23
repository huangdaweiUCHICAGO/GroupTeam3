class Score(object):
    name = 'player'
    score = 0

    def _init_(self, score, name):
        self.name = name
        self.score = score

    # returns the name associated with score
    def get_name(self):
        return self.name

    # returns score of player
    def get_score(self):
        return self.score
