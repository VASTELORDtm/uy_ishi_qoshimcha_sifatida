class Game_info:
    def __init__(self, game_name, game_lvl, game_max_score, game_Top_Global_Rank, game_Top_Region_Rank):
        self.game_name = game_name  
        self.game_lvl = game_lvl
        self.game_max_score = game_max_score
        self.game_Top_Global_Rank = game_Top_Global_Rank
        self.game_Top_Region_Rank = game_Top_Region_Rank

    def __str__(self):
        return f"| {self.game_name:<12} | {str(self.game_lvl):>4} | {str(self.game_max_score):>10} | {str(self.game_Top_Global_Rank):^15} | {str(self.game_Top_Region_Rank):^15} |"

class Player_info(Game_info):
    def __init__(self, player_name, game_name, game_lvl, game_max_score, game_Top_Global_Rank, game_Top_Region_Rank):
        super().__init__(game_name, game_lvl, game_max_score, game_Top_Global_Rank, game_Top_Region_Rank)
        self.player_name = player_name
        self.player_score = 0

    def __str__(self):
        return f"| {self.player_name:<15} {super().__str__()[2:]}"

player1 = Player_info("VASTELORD", "Blood Strike", 999, 100000000, 1, 1)
player2 = Player_info("LOYAL", "Blood Strike", 800, 6411574, 7, 2)
player3 = Player_info("Gerald", "Blood Strike", 746, 6544684, 56, 17)
player4 = Player_info("Stephen", "Blood Strike", 644, 154646, 99, 25)
player5 = Player_info("Jhony Kage", "Blood Strike", 514, 465644, "No Rank", 49)

# Print header
print("\n" + "="*85)
print("|     PLAYER      |    GAME    | LVL |  MAX SCORE | GLOBAL RANKING | REGION RANKING |")
print("="*85)

players = [player1, player2, player3, player4, player5]
for player in players:
    print(player)
print("="*85)