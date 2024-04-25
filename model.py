class Player:
    def __init__(self, name):
        self._won = 0
        self._tied = 0
        self._lost = 0
        self.name = name

    def win(self):
        self._won = self._won + 1

    def tie(self):
        self._tied = self._tied + 1

    def lose(self):
        self._lost = self._lost + 1

    def total_matches(self):
        return self._won + self._tied + self._lost

    def points(self):
        return self._won * 3 + self._tied

    def __repr__(self):
        return f"{self.name} w:{self._won} t:{self._tied} l:{self._lost} p: {self.points()} mp:{self.total_matches()}"


class Match:
    def __init__(self, date, home_team, away_team, result, goal_diff):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.goal_diff = goal_diff

    def to_dict(self):
        return dict(date=self.date,
                    home_team=self.home_team,
                    away_team=self.away_team,
                    result=self.result)
