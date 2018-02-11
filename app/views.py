from flask import render_template
from flask import request, redirect
from app import app
import app.game.board as bd
import app.game.utilities as util
import pandas as pd



@app.route('/')
@app.route('/index')
def index():
    board = bd.get_board()
    message = bd.get_message()
    df = pd.DataFrame(board)
    text = df.to_html(header=False, index=False)
    return render_template('index.html', text=text, message=message, title='Home')


@app.route('/move', methods=['GET', 'POST'])
def move():
    column = request.form['option']
    bd.next_human_move_and_computer(int(column))
    return redirect('/')


@app.route('/start', methods=['GET', 'POST'])
def start():
    bd.start_new_game()
    return redirect('/')
