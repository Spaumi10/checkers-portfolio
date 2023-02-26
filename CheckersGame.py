# Author: Michael Spaulding
# GitHub username: Spaumi10
# Date: 02/25/2023
# Description:


class Checkers:
    """
    Represents a checkers game, including board and gameplay.
    """

    BLACK_CHECKERS = 12
    WHITE_CHECKERS = 12

    def __init__(self):
        self._board = Board()

    def create_player(self, player_name, piece_color):
        """Returns a player object with name and piece color."""
        # TODO check on whether the parameter name should be piece_color or checker_color. Seems to be conflict between what is mentioned here and for the Player class constructor.
        return Player(player_name, piece_color)

    def play_game(
        self, player_name, starting_square_location, destination_square_location
    ):
        """
        Moves the player's piece from the starting location to the destination
        location.
        """

    def get_checker_details(self, square_location):
        """Returns the checker details present at the square_location."""
        row = square_location[0]
        column = square_location[1]
        try:
            if self._board.get_board()[row][column]:
                return self._board.get_board()[row][column]
            else:
                return None
        except IndexError:
            raise InvalidSquare

    def print_board(self):
        """
        Prints the current checker board, with placement of current pieces,
        None for empty spaces.
        """
        print(self._board.get_board())

    def game_winner(self):
        """
        Returns the name of the winning player, or if game not over, returns
        that fact.
        """


class Player:
    """
    Represents a checkers player.
    """

    def __init__(self, player_name, checker_color):
        self._player_name = player_name
        self._checker_color = checker_color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces_count = 0

    def get_king_count(self):
        """Returns the number of king pieces that the player has."""
        return self._king_count

    def get_triple_king_count(self):
        """Returns the number of triple king pieces that the player has."""
        return self._triple_king_count

    def get_captured_pieces_count(self):
        """Returns the number of opponent peces that the player has captured."""
        return self._captured_pieces_count


class Board:
    """Creates game board with starting pieces in place."""

    def __init__(self):
        self._board = []
        # TODO Shorten code for creating a board w/ pieces.
        # Creates board and places starting pieces.
        for i in range(8):
            temp_list = []
            for i in range(8):
                # White piece placement
                # Places white pieces on 1st and 3rd row from top.
                if len(self._board) % 2 == 0 and len(self._board) < 3:
                    if len(temp_list) % 2 == 1:
                        temp_list.append(Piece("White"))
                    else:
                        temp_list.append(None)
                # Places white pieces on 2nd row from top.
                elif len(self._board) % 2 == 1 and len(self._board) < 3:
                    if len(temp_list) % 2 == 0:
                        temp_list.append(Piece("White"))
                    else:
                        temp_list.append(None)

                # Black piece placement
                # Places black pieces on 6th and 8th row from top.
                elif len(self._board) % 2 == 0 and len(self._board) > 4:
                    if len(temp_list) % 2 == 1:
                        temp_list.append(Piece("Black"))
                    else:
                        temp_list.append(None)
                # Places black pieces on 7th row from top.
                elif len(self._board) % 2 == 1 and len(self._board) > 4:
                    if len(temp_list) % 2 == 0:
                        temp_list.append(Piece("Black"))
                    else:
                        temp_list.append(None)

                # Fills in empty spaces
                else:
                    temp_list.append(None)

            self._board.append(temp_list)

    def get_board(self):
        """Returns board."""
        return self._board


class Piece:
    """Represents a checkers piece"""

    def __init__(self, piece_color, piece_type=""):
        self._piece_color = piece_color
        self._piece_type = piece_type

    def check_moves(self, starting_square_location, destination_square_location):
        """Checks if move available for piece type."""
        # King piece moves
        if self._piece_type == "king":
            pass

        # Triple king piece moves
        elif self._piece_type == "triple_king":
            pass

        # Regular piece moves
        else:
            pass

    def get_piece_color(self):
        """Returns piece's color."""
        return self._piece_color

    def set_piece_type(self, piece_type):
        """Sets piece to piece_type."""
        self._piece_type = piece_type

    def __str__(self) -> str:
        return self._piece_color

    def __repr__(self) -> str:
        return self._piece_color

    # def get_kinged(self):
    #     """"""

    # def get_triple_kinged(self):
    #     """"""


# Exceptions
class OutofTurn(Exception):
    """"""

    pass


class InvalidSquare(Exception):
    """"""

    pass


class InvalidPlayer(Exception):
    """"""

    pass


game = Checkers()

for row in game._board.get_board():
    print(row)

Player1 = game.create_player("Adam", "White")

Player2 = game.create_player("Lucy", "Black")


# game.play_game("Lucy", (5, 6), (4, 7))

# game.play_game("Adam", (2,1), (3,0))

print(game.get_checker_details((3, 1)))

# Player1.get_captured_pieces_count()
