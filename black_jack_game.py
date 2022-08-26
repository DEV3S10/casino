from deckk import deck
from bot import bot_count, curr
from plyaer import Player


class Game(Player):
    def blackjack(self):

        count = 0
        curr = deck.pop()
        count += curr
        curr = deck.pop()
        count += curr

        chiso = input("Do you want do stavku!: y/n \n")
        if chiso == "y":
            if Player.cash > 100:
                print(f"Your count {count}")
                while True:
                    choice = input("Would you like get cards? y/n \n")
                    if choice == "y":
                        print(f"Vam popalas carta {curr}")
                        count += curr
                        print(f"Your count {count}")
                        if count > 21:
                            print("You are lose!")
                            Player.cash -= 100
                            print(f"your cash {Player.cash}")
                            return Game.blackjack(self)
                        elif count == 21:
                            print("You are win!")
                            Player.cash += 100
                            print(f"your cash {Player.cash}")
                            return Game.blackjack(self)
                        else:
                            print(f"You have {count}")
                            print(f"Bot have {bot_count}")
                            if bot_count > count:
                                print("You are lose!")
                                Player.cash -= 100
                                print(f"your cash {Player.cash}")
                                return Game.blackjack(self)
                            elif bot_count == count:
                                return Game.blackjack(self)

                            else:
                                print("You are win!")
                                Player.cash += 100
                                print(f"your cash {Player.cash}")
                                return Game.blackjack(self)
                    else:
                        print(f"You have {count}")
                        print(f"Bot have {bot_count}")
                        if bot_count > count:
                            print("You are lose!")
                            Player.cash -= 100
                            print(f"your cash {Player.cash}")
                            return Game.blackjack(self)
                        elif bot_count == count:
                            return Game.blackjack(self)

                        else:
                            print("You are win!")
                            Player.cash += 100
                            print(f"your cash {Player.cash}")
                            return Game.blackjack(self)

            else:
                print("Ne dostatochno sredstv!!!")
        else:
            return "You have ", Player.cash


c = Game
print(c.blackjack(c))

