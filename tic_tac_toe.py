"""
Tic-tac-toe
"""

#
# Game Messages
#

GAME_BANNER = """
~~~~~~~~~~~~~~~~~~~~~~~~
      TIC-TAC-TOE:
    *Three in a Row*

     Est. 1300 B.C.
~~~~~~~~~~~~~~~~~~~~~~~~
"""

PLAYER1 = 'X'
PLAYER2 = 'O'
PLAYERS = (PLAYER1, PLAYER2)

GAME_INSTRUCTIONS = """\
Instructions:
  1. Decide who will be {} and who will be {}. {} always goes first.
  2. When it's your turn, enter the move you want to make. If you get three in
     a row, you win!
  3. Enter 'quit' or 'q' at any time to quit the game.
""".format(PLAYER1, PLAYER2, PLAYER1)

GAME_BOARD = """
   {} | {} | {}
  -----------
   {} | {} | {}
  -----------
   {} | {} | {}
"""

GAME_TEXT = {
  'banner':       GAME_BANNER,
  'instructions': GAME_INSTRUCTIONS,
  'board':        GAME_BOARD,
  'ready?':       'Are you ready to play tic-tac-toe? (y/n) ',
  'y_or_n':       'Please enter y or n.',
  'start':        'LET THE GAME BEGIN!',
  'prompt_move':  'Player {}, enter your move (1-9): ',
  'invalid_move': 'You must enter a number between 1 and 9.',
  'space_taken':  'That space is taken!',
  'winner':       'Player {} wins!',
  'draw':         'The game is a draw. No one wins!',
  'goodbye':      'Goodbye.'
}


#
# Game
#

def tic_tac_toe(game_text, game_board, players):
  game_over = False
  winner = None
  number_of_moves = 0

  reset_game_board(game_board)
  display_game_board(game_text, game_board)

  # Game loop
  while not game_over:
    player = players[number_of_moves % 2]
    player_move = get_player_move(game_text, game_board, player)
    update_game_board(game_board, player, player_move)
    display_game_board(game_text, game_board)
    number_of_moves = number_of_moves + 1

    if there_is_a_winner(game_board):
      # Current player won
      game_over = True
      winner = player
    elif number_of_moves == len(game_board):
      # No one won
      game_over = True
      winner = None

  display_winner(game_text, winner)


#
# Game Logic
#

def ready_to_play(game_text):
  while True:
    ready = input(game_text['ready?']).lower()
    if ready in ('y', 'n'):
      return ready == 'y'
    elif ready in ('quit', 'q'):
      say_goodbye(game_text)
    else:
      print(game_text['y_or_n'])

def get_player_move(game_text, game_board, player):
  while True:
    try:
      user_input = input(game_text['prompt_move'].format(player))
      if user_input == 'quit' or user_input == 'q':
        say_goodbye(game_text)
      if not user_input.isdigit():
        raise ValueError(game_text['invalid_move'])
      player_move = int(user_input) - 1
      if not (player_move >= 0 and player_move < len(game_board)):
        raise ValueError(game_text['invalid_move'])
      if not space_is_free(game_board, player_move):
        raise ValueError(game_text['space_taken'])
    except ValueError as e:
      print(e)
    else:
      return player_move

def there_is_a_winner(game_board):
  triplets = (
    get_rows(game_board) +
    get_columns(game_board) +
    get_diagonals(game_board)
  )
  for triplet in triplets:
    if triplet[0] == triplet[1] == triplet[2]:
      return True
  return False


#
# Game Board
#

def create_game_board():
  return [' '] * 9

def reset_game_board(game_board):
  for index, value in enumerate(game_board):
    game_board[index] = index + 1

def update_game_board(game_board, player_symbol, player_move):
  game_board[player_move] = player_symbol

def get_rows(game_board):
  return [
    tuple(game_board[0:3]),
    tuple(game_board[3:6]),
    tuple(game_board[6:9])
  ]

def get_columns(game_board):
  return [
    (game_board[0], game_board[3], game_board[6]),
    (game_board[1], game_board[4], game_board[7]),
    (game_board[2], game_board[5], game_board[8])
  ]

def get_diagonals(game_board):
  return [
    (game_board[0], game_board[4], game_board[8]),
    (game_board[2], game_board[4], game_board[6])
  ]

def space_is_free(game_board, player_move):
  symbol = game_board[player_move]
  return isinstance(symbol, int)


#
# Game Display
#

def display_banner(game_text):
  print(game_text['banner'])

def display_game_instructions(game_text):
  print(game_text['instructions'])

def display_game_start(game_text):
  print('\n' + game_text['start'])

def display_game_board(game_text, game_board):
  print(game_text['board'].format(*game_board))

def display_winner(game_text, winner):
  if winner:
    print(game_text['winner'].format(winner))
  else:
    print(game_text['draw'])

def say_goodbye(game_text):
  print(game_text['goodbye'])
  quit()


#
# 1. Show banner and instructions.
# 2. Ask user if he/she wants to play.
# 3. Play tic-tac-toe! Or say goodbye.
#

if __name__ == '__main__':
  display_banner(GAME_TEXT)
  display_game_instructions(GAME_TEXT)

  ready = ready_to_play(GAME_TEXT)

  if ready:
    display_game_start(GAME_TEXT)
    game_board = create_game_board()
    tic_tac_toe(GAME_TEXT, game_board, PLAYERS)
  else:
    say_goodbye(GAME_TEXT)
