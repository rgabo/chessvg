import chess

from flask import Blueprint, request

from .san import apply_moves
from .svg import parse_args, render_svg

bp = Blueprint('fen', __name__, url_prefix='/fen')


def is_supported(path: str):
  try:
    fen, _ = parse_fen(path)
    board = chess.Board(fen)
  except ValueError:
    return False
  
  return True


@bp.route('/<path:path>')
def fen_with_moves(path: str):
  fen, moves = parse_fen(path)
  board = chess.Board(fen)

  if moves:
    apply_moves(board, moves)

  args = parse_args(request.args)
  return render_svg(board, **args)


def parse_fen(path: str):
  parts = path.split('/')
  fen = '/'.join(parts[:8])

  moves = parts[8:]
  if moves and moves[0] == 'b':
    fen = fen + ' b'
    moves.pop(0)

  return fen, moves