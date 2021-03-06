import chess

from flask import Blueprint, request

from .svg import parse_args, render_svg

bp = Blueprint('san', __name__, url_prefix='/san')

def is_supported(path: str):
  moves = path.split('/')

  try:
    board = chess.Board()
    apply_moves(board, moves)
  except ValueError:
    return False

  return True


@bp.route('/')
def root():
  board = chess.Board()

  args = parse_args(request.args)
  return render_svg(board, **args)


@bp.route('/<path:path>')
def board_with_moves(path: str):
  moves = path.split('/')

  board = chess.Board()
  apply_moves(board, moves)

  args = parse_args(request.args)
  return render_svg(board, **args)


def apply_moves(board, moves):
  for move in moves:
      board.push_san(move)
