import csv
from unidecode import unidecode

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


def get_results(file):
    players = {}
    with open(file) as csv_f:
        r = csv.reader(csv_f)
        for row in r:
            date = row[0]
            players_home_team = row[1].split(';')
            players_away_team = row[2].split(';')
            result = row[3]
            if result == 'H':
                victory(players_home_team, players_away_team, players)
            elif result == 'A':
                victory(players_away_team, players_home_team, players)
            elif result == 'T':
                tie(players_home_team, players_away_team, players)
    return sorted(list(players.values()), key =lambda x:(-x.points(), unidecode(x.name)))


def victory(a_team, another_team, players):
    for p in a_team:
        player = players.get(p)
        if player is None:
            player = Player(p)
            players.update({p: player})
        player.win()
    for p in another_team:
        player = players.get(p)
        if player is None:
            player = Player(p)
            players.update({p: player})
        player.lose()


def tie(a_team, another_team, players):
    for p in (a_team + another_team):
        player = players.get(p)
        if player is None:
            player = Player(p)
            players.update({p: player})
        player.tie()
