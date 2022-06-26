import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame

from x_o import UiForm


class MyGame(QtWidgets.QWidget):

    def __init__(self):
        super(MyGame, self).__init__()
        self.board = []
        self._counter = 0
        self.ui = UiForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('media/icons/sf.ico'))
        self.setWindowTitle('Game Tic-Tac-Toe (for "Skill Factory")')

        self.ui.label.setFrameShape(QFrame.Shape.StyledPanel)
        myFont = QtGui.QFont()
        myFont.setFamily('Calibri, Tahoma, Arial, Helvetica')
        myFont.setPointSizeF(14)
        self.ui.label.setFont(myFont)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self._counter = 0
        for r in range(1, 10):
            exec('self.ui.pBtn_' + str(r) + '.setEnabled(True)')
            exec('self.ui.pBtn_' + str(r) + '.setStyleSheet("color: black;")')
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
            exec('self.ui.pBtn_' + str(btn_i) +
                 '.setText(board[' + str(btn_i - 1) + '])')

    def btn_1(self):
        if not self._counter % 2:
            self.board[0] = 'X'
        else:
            self.board[0] = 'O'
        self.ui.pBtn_1.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_2(self):
        if not self._counter % 2:
            self.board[1] = 'X'
        else:
            self.board[1] = 'O'
        self.ui.pBtn_2.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_3(self):
        if not self._counter % 2:
            self.board[2] = 'X'
        else:
            self.board[2] = 'O'
        self.ui.pBtn_3.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_4(self):
        if not self._counter % 2:
            self.board[3] = 'X'
        else:
            self.board[3] = 'O'
        self.ui.pBtn_4.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_5(self):
        if not self._counter % 2:
            self.board[4] = 'X'
        else:
            self.board[4] = 'O'
        self.ui.pBtn_5.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_6(self):
        if not self._counter % 2:
            self.board[5] = 'X'
        else:
            self.board[5] = 'O'
        self.ui.pBtn_6.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_7(self):
        if not self._counter % 2:
            self.board[6] = 'X'
        else:
            self.board[6] = 'O'
        self.ui.pBtn_7.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_8(self):
        if not self._counter % 2:
            self.board[7] = 'X'
        else:
            self.board[7] = 'O'
        self.ui.pBtn_8.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_9(self):
        if not self._counter % 2:
            self.board[8] = 'X'
        else:
            self.board[8] = 'O'
        self.ui.pBtn_9.setEnabled(False)
        self._counter += 1
        self.redraw()

    def btn_10(self):
        self.reset_game()

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
        for line in line_to_win:
            print(line)
            if (self.board[line[0]] ==
                self.board[line[1]] ==
                self.board[line[2]] == 'X') \
                    or \
                    (self.board[line[0]] ==
                     self.board[line[1]] ==
                     self.board[line[2]] == 'O'):
                self.ui.label.setStyleSheet('color: red;')
                self.ui.label.setText(
                    f'Победили "'
                    f'{"Крестики" if self.board[line[0]] == "X" else "Нолики"}'
                    f'"')
                exec('self.ui.pBtn_' + str(line[0] + 1) +
                     '.setStyleSheet("color: red;")')
                exec('self.ui.pBtn_' + str(line[1] + 1) +
                     '.setStyleSheet("color: red;")')
                exec('self.ui.pBtn_' + str(line[2] + 1) +
                     '.setStyleSheet("color: red;")')
                for en in range(1, 10):
                    exec('self.ui.pBtn_' + str(en) + '.setEnabled(False)')
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
        exec('game.ui.pBtn_'+str(i)+'.clicked.connect(game.btn_'+str(i)+')')

    sys.exit(app.exec())
