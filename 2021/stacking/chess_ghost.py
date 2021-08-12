import chess, chess.pgn as pgn

game = pgn.Game()
game.headers["Event"] = "Example"
# print(game)
# print(game.board().legal_moves)

print('='*25)
# print(game.board())
print('='*25)

b = game.board()

real_game = game.add_variation(chess.Move.from_uci("e2e4"))
# print(game.board().legal_moves == b)
# print(game.board().legal_moves + b)
print(game.board() == b)
print(real_game.board() == b)

fake_game = game.add_variation(chess.Move.from_uci("e2e4"))
# print(game.board().legal_moves == b)
print(game.board() == b)
print(fake_game.board() == b)
# if game.board()==b & fake_game.board()==real_game.board():

print(real_game.board()==fake_game.board())
print(real_game.board().legal_moves==fake_game.board().legal_moves)
print(real_game.board().legal_moves)
print(fake_game.board().legal_moves)
print(game.board().legal_moves)
print()
print('='*25)
print('='*25)

