# Write your solution here
import json
class Player:

    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f"{self.name:<21}{self.team}{self.goals:>4} +{self.assists:>3} = {self.goals+self.assists:>3}"

    
class Players:

    def __init__(self):
        self.players = {}

    def player_search(self, name: str):
        try:
            print(self.players[name])
        except KeyError:
            print("no such player")

    def team_list(self):
        teams = [player.team for key, player in self.players.items()]
        for team in sorted(set(teams)):
            print(team)

    def country_list(self):
        countries = [player.nationality for key, player in self.players.items()]
        for country in sorted(set(countries)):
            print(country)

    def dict_to_list(self, dictionary: dict):
        return [player for key, player in self.players.items()]

    def points_in_team(self, team: str):
        players = list(filter(lambda player: player.team == team, self.dict_to_list(self.players)))
        for player in sorted(players, key=lambda player: (player.goals + player.assists), reverse=True):
            print(player)

    def points_by_country(self, country: str):
        players = list(filter(lambda player: player.nationality == country, self.dict_to_list(self.players)))
        for player in sorted(players, key=lambda player: (player.goals + player.assists), reverse=True):
            print(player)

    def most_points(self, amount: int):
        players = sorted(self.dict_to_list(self.players), key=lambda player: ((player.goals + player.assists), player.goals), reverse=True)
        for i in range(amount):
            print(players[i])

    def most_goals(self, amount: int):
        players = sorted(self.dict_to_list(self.players), key=lambda player: player.games)
        players = sorted(players, key=lambda player: player.goals, reverse=True)
        for i in range(amount):
            print(players[i])


class FileHandler():

    def __init__(self, filename: str):
        self.__filename = filename

    def load_file(self):
        players = {}
        with open(self.__filename) as file:
            data = file.read()
        players = json.loads(data)
        return players
    

class StatisticsApp:

    def __init__(self):
        self.__players = Players()

    def read_file(self, filename: str):
        self.__filehandler = FileHandler(filename)
        players = self.__filehandler.load_file()
        for player in players:
            self.__players.players[player["name"]] = Player(player["name"], player["nationality"], int(player["assists"]), int(player["goals"]), int(player["penalties"]), player["team"], int(player["games"]))

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def searh_player(self):
        name = input("name: ")
        self.__players.player_search(name)

    def list_teams(self):
        self.__players.team_list()

    def list_countries(self):
        self.__players.country_list()

    def team_points(self):
        team = input("team: ")
        self.__players.points_in_team(team)

    def country_points(self):
        country = input("country: ")
        self.__players.points_by_country(country)

    def most_points(self):
        amount = int(input("how many: "))
        self.__players.most_points(amount)

    def most_goals(self):
        amount = int(input("how many: "))
        self.__players.most_goals(amount)

    def execute(self):
        filename = input("file name: ")
        self.read_file(filename)
        print(f"read the data of {len(self.__players.players)} players")
        print("")
        self.help()
        print("")

        while True:
            command = input("command: ")
            if(command == "0"):
                break
            elif(command == "1"):
                self.searh_player()
            elif(command == "2"):
                self.list_teams()
            elif(command == "3"):
                self.list_countries()
            elif(command == "4"):
                self.team_points()
            elif(command == "5"):
                self.country_points()
            elif(command == "6"):
                self.most_points()
            elif(command == "7"):
                self.most_goals()
            else:
                self.help()

application = StatisticsApp()
application.execute()

### Example solution
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()