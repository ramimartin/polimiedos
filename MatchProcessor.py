import csv
from model import Player, Match
from unidecode import unidecode


class MatchProcessor:
    def __init__(self, file):
        self.players = {}
        self.matches = []
        self.__processCSV(file)

    def __processCSV(self, file):
        with open(file) as csv_f:
            r = csv.reader(csv_f)
            for row in r:
                match = Match(row[0], row[1].split(';'), row[2].split(';'), row[3], int(row[4]))
                self.matches.append(match)
                if match.result == 'H':
                    self.__victory(match.home_team, match.away_team, match.goal_diff)
                elif match.result == 'A':
                    self.__victory(match.away_team, match.home_team, match.goal_diff)
                elif match.result == 'T':
                    self.__tie(match.home_team, match.away_team)

    def __victory(self, a_team, another_team, goal_diff):
        for p in a_team:
            player = self.players.get(p)
            if player is None:
                player = Player(p)
                self.players.update({p: player})
            player.win(goal_diff)
        for p in another_team:
            player = self.players.get(p)
            if player is None:
                player = Player(p)
                self.players.update({p: player})
            player.lose(goal_diff)

    def __tie(self, a_team, another_team):
        for p in (a_team + another_team):
            player = self.players.get(p)
            if player is None:
                player = Player(p)
                self.players.update({p: player})
            player.tie()

    def get_position_table(self):
        return sorted(list(self.players.values()), key=lambda x: (-x.points(), -x.prom(), unidecode(x.name)))
