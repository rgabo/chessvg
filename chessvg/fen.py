import chess

from flask import Blueprint, request

from .san import apply_moves
from .svg import parse_args, render_svg

bp = Blueprint('fen', __name__, url_prefix='/fen')
      

@bp.route('/<path:path>')
def fen_with_moves(path: str):
  parts = path.split('/')
  fen = '/'.join(parts[:8])

  moves = parts[8:]
  if moves and moves[0] == 'b':
    fen = fen + ' b'
    moves.pop(0)
  
  board = chess.Board(fen)

  if moves:
    apply_moves(board, moves)

  args = parse_args(request.args)
  return render_svg(board, **args)