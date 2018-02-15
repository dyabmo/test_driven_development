from enum import Enum


class Directions(Enum):
    Horizontal = (0, 1)
    Vertical = (1, 0)
    Diagonal_right = (1, 1)
    Diagonal_left = (1, -1)


class Puissance4(object):

    def __init__(self, grid_size):
        self._grid = []
        for _ in range(grid_size):
            self._grid.append([0] * grid_size)

    def play(self, player_id, column):
        ok_flag = False
        for row in self._grid:
            if row[column] == 0:
                row[column] = player_id
                ok_flag = True
                break
        return ok_flag

    def print_grid(self):
        text_grid = ""
        for row in reversed(self._grid):
            text_grid += "|"
            text_grid += "".join(
                self._coin_to_string(coin) for coin in row
            )
            text_grid += "|\n"
        return text_grid[:-1]

    def get_winner(self):
        for x in range(len(self._grid)):
            for y in range(len(self._grid[0])):
                if self._grid[x][y] == 0:
                    continue
                is_winner = 0
                for direction in Directions:
                    is_winner |= self._check_direction(direction, x, y)
                if is_winner:
                    return self._grid[x][y]

        return 0

    def _check_direction(self, direction, x, y):
        this_coin = self._grid[x][y]
        x_step, y_step = direction.value
        for i in range(1, 4):
            try:
                new_coin = self._grid[x + x_step * i][y + y_step * i]
            except IndexError:
                return False
            if this_coin != new_coin:
                return False
        return True

    def _coin_to_string(self, coin):
        if coin == 0:
            return " "
        elif coin == 1:
            return "x"
        elif coin == 2:
            return "o"
        raise ValueError("No coin mapping for coin %s" % coin)
