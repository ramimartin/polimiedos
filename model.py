from datetime import datetime


class Player:
    def __init__(self, name):
        self._won = 0
        self._tied = 0
        self._lost = 0
        self.name = name
        self.total_goal_diff  = 0
        self.results = []

    def win(self, goal_diff):
        self._won = self._won + 1
        self.total_goal_diff += goal_diff
        self.results.append('W')

    def tie(self):
        self._tied = self._tied + 1
        self.results.append('T')

    def lose(self, goal_diff):
        self._lost = self._lost + 1
        self.total_goal_diff -= goal_diff
        self.results.append('L')

    def total_matches(self):
        return self._won + self._tied + self._lost

    def points(self):
        return self._won * 3 + self._tied

    def prom(self):
        return self.points()/self.total_matches()
    
    def last_results(self):
        return self.results[-5:]

    def __repr__(self):
        return f"{self.name} w:{self._won} t:{self._tied} l:{self._lost} p: {self.points()} mp:{self.total_matches()}"


class Match:
    def __init__(self, date, home_team, away_team, result, goal_diff):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.goal_diff = goal_diff

    def to_dict(self):
        return dict(date=self.date,
                    home_team=self.home_team,
                    away_team=self.away_team,
                    result=self.result)
