from threading import Timer
import random


class Game:
    top_score: int = 86
    __fraction = 0

    @staticmethod
    def show_help():
        print("这是游戏的帮助信息")

    def show_top_score(self):
        print("历史最高分为%d" % self.top_score)

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print("%s开始游戏了..." % self.player_name)
        t = Timer(5.0, self.tim())
        t.start()

    def tim(self):
        self.__fraction = random.randint(1, 100)
        print("最终得分%d" % self.__fraction)
        if self.top_score < self.__fraction:
            self.top_score = self.__fraction


game = Game("岂可修")
game.show_help()
game.show_top_score()
game.start_game()
