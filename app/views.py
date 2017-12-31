from flask import render_template
from flask import request, redirect
from app import app
from app.game.board import Board


@app.route('/')
@app.route('/index')
def index():
    board = Board()
    board.fill_example()
    text = board.as_pandas().to_html(header=False, index=False)
    return render_template('index.html', text=text, title='Home')


@app.route('/move', methods=['GET', 'POST'])
def move():
    cell = request.form['option']
    print(cell)
    return redirect('/')

