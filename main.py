import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame

from x_o import UiForm


class MyGame(QtWidgets.QWidget):

    def __init__(self):
        super(MyGame, self).__init__()
        self.board = None
        self._counter = 0
        self.ui = UiForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('media/icons/sf.ico'))
        self.setWindowTitle('Game Tic-Tac-Toe ("Skill Factory" B5.6)')

        self.ui.label.setFrameShape(QFrame.Shape.StyledPanel)
        label_font = QtGui.QFont()
        label_font.setFamily('Calibri, Tahoma, Arial, Helvetica')
        label_font.setPointSizeF(14)
        self.ui.label.setFont(label_font)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self._counter = 0
        for r in range(1, 10):
            exec(f'self.ui.pBtn_{str(r)}.setEnabled(True)')
            exec(f'self.ui.pBtn_{str(r)}.setStyleSheet("color: black;")')
        self.ui.label.setStyleSheet('color: black;')
        self.redraw()

    def redraw(self):
        self.draw_board(self.board)
        self.label_message()
        self.check_winner()

    def label_message(self):
        if not self._counter % 2:
            self.ui.label.setText('Сейчас ход "Крестиков"')
        else:
            self.ui.label.setText('Сейчас ход "Ноликов"')

    def draw_board(self, board):
        for btn_i in range(1, 10):
            exec(f'self.ui.pBtn_{str(btn_i)}'
                 f'.setText(board[{str(btn_i - 1)}])')

    for btn_no in range(1, 10):
        exec(
            f'def btn_{str(btn_no)}(self):\n'
            f'    if not self._counter % 2:\n'
            f'        self.board[{str(btn_no - 1)}] = "X"\n'
            f'    else:\n'
            f'        self.board[{str(btn_no - 1)}] = "O"\n'
            f'    self.ui.pBtn_{str(btn_no)}.setEnabled(False)\n'
            f'    self._counter += 1\n'
            f'    self.redraw()'
        )

    def btn_10(self):
        self.reset_game()

    def line_light(self, cells):
        for bt_n in range(3):
            exec(f'self.ui.pBtn_{str(cells[bt_n] + 1)}'
                 f'.setStyleSheet("color: red;")')
        for en in range(1, 10):
            exec(f'self.ui.pBtn_{str(en)}.setEnabled(False)')

    def check_winner(self):
        line_to_win = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        )
        x_list = [bool(cell == 'X') for cell in self.board]
        o_list = [bool(cell == 'O') for cell in self.board]
        for line in line_to_win:
            if all([x_list[line[idx_x]] for idx_x in range(3)]):
                self.ui.label.setStyleSheet('color: red;')
                self.ui.label.setText('Победили "Крестики"')
                self.line_light(cells=line)
                break
            elif all([o_list[line[idx_o]] for idx_o in range(3)]):
                self.ui.label.setStyleSheet('color: red;')
                self.ui.label.setText('Победили "Нолики"')
                self.line_light(cells=line)
                break
            if self._counter == 9:
                self.ui.label.setStyleSheet('color: blue;')
                self.ui.label.setText('Ничья')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game = MyGame()
    game.show()

    game.reset_game()
    game.draw_board(game.board)
    game.label_message()
    for i in range(1, 11):
        exec(f'game.ui.pBtn_{str(i)}.clicked.connect(game.btn_{str(i)})')

    sys.exit(app.exec())
