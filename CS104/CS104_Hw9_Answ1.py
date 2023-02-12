class Team():
    def __init__(self, color, match, wins, loses, draws):
        self.color = color
        self.match = match
        self.wins = wins
        self.loses = loses
        self.draws = draws

    def report(self):
        print("Team: {} Team, Matches: {}, Wins: {}, Loses:{}, Draws:{}".format(self.color, self.match, self.wins,
                                                                                self.loses,
                                                                                self.draws))


team_a = Team("Red", 6, 2, 2, 2)
team_b = Team("Blue", 5, 3, 2, 0)
team_a.report()
team_b.report()
