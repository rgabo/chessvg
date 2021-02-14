import chess

from flask import Flask, render_template, request, send_file, url_for

from . import fen, san
from .svg import parse_args, render_svg


app = Flask(__name__)
app.register_blueprint(fen.bp)
app.register_blueprint(san.bp)

@app.route('/')
def root():
  board = chess.Board()
  
  args = parse_args(request.args)
  return render_svg(board, **args)
