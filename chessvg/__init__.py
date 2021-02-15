import chess

from flask import Flask, abort, redirect, render_template, request, send_file, url_for

from . import fen, san
from .svg import parse_args, render_svg


app = Flask(__name__)
modules = [fen, san]
for module in modules:
  app.register_blueprint(module.bp)


@app.route('/')
def root():
  board = chess.Board()
  
  args = parse_args(request.args)
  return render_svg(board, **args)


@app.route('/<path:path>')
def root_handler(path: str):
  print(path)
  for module in modules:
    if module.is_supported(path):
      return redirect(module.bp.url_prefix + '/' + path)

  abort(404)
