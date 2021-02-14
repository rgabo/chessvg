import io

from flask import send_file

import chess.svg


def parse_args(args):
    result = {}
    
    orientation = args.get('orientation', 'white')
    flip = args.get('flip', None) is not None
    flipped = args.get('flipped', None) is not None
    
    result['flipped'] = flip or flipped or orientation == 'black'

    arrows = args.get('arrows', None)
    if arrows:
      arrows = arrows.split(',')
      result['arrows'] = map(lambda arrow: chess.svg.Arrow.from_pgn(arrow), arrows)
      
    return result


def send_svg(svg: str):
    fp = io.BytesIO(svg.encode('utf-8'))
    return send_file(fp, mimetype='image/svg+xml')
  

def render_svg(board: chess.Board, **kwargs):
    svg = chess.svg.board(board, **kwargs)

    return send_svg(svg)