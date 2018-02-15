from unittest import TestCase

from game import Puissance4

class GameTest(TestCase):
    def test_init(self):
        # Instanciate a 10 x 10 grid
        game = Puissance4(grid_size=10)

    def test_play(self):

        player_1 = 1
        player_2 = 2
        game = Puissance4(4)

        ok_flag = game.play(player_1, column=0)
        self.assertEqual(True,ok_flag)

        ok_flag = game.play(player_2,0)
        self.assertEqual(True,ok_flag)

        ok_flag = game.play(player_1,0)
        self.assertEqual(True,ok_flag)

        ok_flag = game.play(player_2,0)
        self.assertEqual(True,ok_flag)

        ok_flag = game.play(player_1,0)
        self.assertEqual(False,ok_flag)


    def test_print_grid(self):
        player_1 = 1
        player_2 = 2
        game = Puissance4(4)

        ok_flag = game.play(player_1, column=2)
        ok_flag = game.play(player_2,0)
        ok_flag = game.play(player_1,0)
        ok_flag = game.play(player_2,0)

        text_grid = game.print_grid()

        expected_grid = "|    |\n|o   |\n|x   |\n|o x |"
        self.assertEqual(text_grid, expected_grid)


    def test_get_winner(self):
        player_1 = 1
        player_2 = 2
        # Vertical winner
        game = Puissance4(10)

        ok_flag = game.play(player_1, column=2)
        ok_flag = game.play(player_2,0)
        ok_flag = game.play(player_1,2)
        ok_flag = game.play(player_2,0)

        print(game.print_grid())

        player_won = game.get_winner()
        #If nobody won, return zero as winner
        self.assertEqual(player_won,0)

        ok_flag = game.play(player_1,1)
        ok_flag = game.play(player_2,0)
        ok_flag = game.play(player_2,0)

        print(game.print_grid())

        player_won = game.get_winner()

        self.assertEqual(player_won,player_2,
                "Game did not recognize vertical winner")

        # Horizonal winner
        game = Puissance4(4)

        ok_flag = game.play(player_1, column=0)
        ok_flag = game.play(player_2,0)
        ok_flag = game.play(player_1,1)
        ok_flag = game.play(player_2,1)
        ok_flag = game.play(player_1,2)
        ok_flag = game.play(player_2,2)
        ok_flag = game.play(player_1,3)

        self.assertEqual(game.get_winner(),player_1,
                "Game did not recognize horizontal winner")

        # Diagonal winner
        game = Puissance4(4)

        ok_flag = game.play(player_1, column=0)
        ok_flag = game.play(player_2,1)
        ok_flag = game.play(player_1,1)
        ok_flag = game.play(player_2,2)
        ok_flag = game.play(player_1,3)
        ok_flag = game.play(player_2,2)
        ok_flag = game.play(player_1,2)
        ok_flag = game.play(player_2,3)
        ok_flag = game.play(player_1,3)
        ok_flag = game.play(player_1,3)

        print(game.print_grid())

        self.assertEqual(game.get_winner(),player_1,
                "Game did not recognize diagonal winner")

        # Horizonal winner
        game = Puissance4(10)

        ok_flag = game.play(player_1, column=1)
        ok_flag = game.play(player_2,1)
        ok_flag = game.play(player_1,2)
        ok_flag = game.play(player_2,2)
        ok_flag = game.play(player_1,3)
        ok_flag = game.play(player_2,3)
        ok_flag = game.play(player_1,4)

	print()
	print(game.print_grid())

        #import ipdb
        #ipdb.set_trace()

	winner = game.get_winner()
        self.assertEqual(winner,player_1)

    def test_template(self):
        self.assertEqual(
            ['hello', 'world'],
            ['hello', 'world'],
        )
