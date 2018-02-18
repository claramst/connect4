from flask import render_template
from flask import request, redirect
from app import app
import app.game.board as bd


@app.route('/')
@app.route('/index')
def index():
    board = bd.get_board()
    message = bd.get_message()
    flat = board.flatten(order='C')
    board_as_string = '[' + ','.join([str(i) for i in flat]) + ']'
    return render_template('index.html', text=board_as_string   , message=message, title='Home')


@app.route('/move', methods=['GET', 'POST'])
def move():
    column = request.form['option']
    bd.next_human_move_and_computer(int(column))
    return redirect('/')


@app.route('/start', methods=['GET', 'POST'])
def start():
    bd.start_new_game()
    return redirect('/')
