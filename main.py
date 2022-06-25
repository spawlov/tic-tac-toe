import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame

from x_o import Ui_Form


class MyGame(QtWidgets.QWidget):

    def __init__(self):
        super(MyGame, self).__init__()
        self.board = []
        self._counter = 0
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('media/icons/sf.ico'))
        self.setWindowTitle('Game Tic-Tac-Toe (for "Skill Factory")')

        self.ui.label.setFrameShape(QFrame.Shape.StyledPanel)
        self.ui.label.setStyleSheet('QLabel{color: red;}')
        myFont = QtGui.QFont()
        myFont.setFamily('Calibri, Tahoma, Arial, Helvetica')
        myFont.setPointSizeF(14)
        self.ui.label.setFont(myFont)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self._counter = 0
        self.ui.pBtn_1.setEnabled(True)
        self.ui.pBtn_2.setEnabled(True)
        self.ui.pBtn_3.setEnabled(True)
        self.ui.pBtn_4.setEnabled(True)
        self.ui.pBtn_5.setEnabled(True)
        self.ui.pBtn_6.setEnabled(True)
        self.ui.pBtn_7.setEnabled(True)
        self.ui.pBtn_8.setEnabled(True)
        self.ui.pBtn_9.setEnabled(True)
        self.ui.label.setStyleSheet('QLabel{color: black;}')
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
        self.ui.pBtn_1.setText(board[0])
        self.ui.pBtn_2.setText(board[1])
        self.ui.pBtn_3.setText(board[2])
        self.ui.pBtn_4.setText(board[3])
        self.ui.pBtn_5.setText(board[4])
        self.ui.pBtn_6.setText(board[5])
        self.ui.pBtn_7.setText(board[6])
        self.ui.pBtn_8.setText(board[7])
        self.ui.pBtn_9.setText(board[8])

    def btn_1(self):
        if not self._counter % 2:
            self.board[0] = 'X'
            self._counter += 1
        else:
            self.board[0] = 'O'
            self._counter += 1
        self.ui.pBtn_1.setEnabled(False)
        self.redraw()

    def btn_2(self):
        if not self._counter % 2:
            self.board[1] = 'X'
            self._counter += 1
        else:
            self.board[1] = 'O'
            self._counter += 1
        self.ui.pBtn_2.setEnabled(False)
        self.redraw()

    def btn_3(self):
        if not self._counter % 2:
            self.board[2] = 'X'
            self._counter += 1
        else:
            self.board[2] = 'O'
            self._counter += 1
        self.ui.pBtn_3.setEnabled(False)
        self.redraw()

    def btn_4(self):
        if not self._counter % 2:
            self.board[3] = 'X'
            self._counter += 1
        else:
            self.board[3] = 'O'
            self._counter += 1
        self.ui.pBtn_4.setEnabled(False)
        self.redraw()

    def btn_5(self):
        if not self._counter % 2:
            self.board[4] = 'X'
            self._counter += 1
        else:
            self.board[4] = 'O'
            self._counter += 1
        self.ui.pBtn_5.setEnabled(False)
        self.redraw()

    def btn_6(self):
        if not self._counter % 2:
            self.board[5] = 'X'
            self._counter += 1
        else:
            self.board[5] = 'O'
            self._counter += 1
        self.ui.pBtn_6.setEnabled(False)
        self.redraw()

    def btn_7(self):
        if not self._counter % 2:
            self.board[6] = 'X'
            self._counter += 1
        else:
            self.board[6] = 'O'
            self._counter += 1
        self.ui.pBtn_7.setEnabled(False)
        self.redraw()

    def btn_8(self):
        if not self._counter % 2:
            self.board[7] = 'X'
            self._counter += 1
        else:
            self.board[7] = 'O'
            self._counter += 1
        self.ui.pBtn_8.setEnabled(False)
        self.redraw()

    def btn_9(self):
        if not self._counter % 2:
            self.board[8] = 'X'
            self._counter += 1
        else:
            self.board[8] = 'O'
            self._counter += 1
        self.ui.pBtn_9.setEnabled(False)
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
            if (self.board[line[0]] ==
                self.board[line[1]] ==
                self.board[line[2]] == 'X') \
                    or \
                    (self.board[line[0]] ==
                     self.board[line[1]] ==
                     self.board[line[2]] == 'O'):
                self.ui.label.setStyleSheet('QLabel{color: red;}')
                self.ui.label.setText(
                    f'Победили "'
                    f'{"Крестики" if self.board[line[0]] == "X" else "Нолики"}'
                    f'"')
                self.ui.pBtn_1.setEnabled(False)
                self.ui.pBtn_2.setEnabled(False)
                self.ui.pBtn_3.setEnabled(False)
                self.ui.pBtn_4.setEnabled(False)
                self.ui.pBtn_5.setEnabled(False)
                self.ui.pBtn_6.setEnabled(False)
                self.ui.pBtn_7.setEnabled(False)
                self.ui.pBtn_8.setEnabled(False)
                self.ui.pBtn_9.setEnabled(False)
            elif self._counter == 9:
                self.ui.label.setStyleSheet('QLabel{color: blue;}')
                self.ui.label.setText('Ничья')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    game = MyGame()
    game.show()

    game.reset_game()

    game.draw_board(game.board)
    game.label_message()

    game.ui.pBtn_1.clicked.connect(game.btn_1)
    game.ui.pBtn_2.clicked.connect(game.btn_2)
    game.ui.pBtn_3.clicked.connect(game.btn_3)
    game.ui.pBtn_4.clicked.connect(game.btn_4)
    game.ui.pBtn_5.clicked.connect(game.btn_5)
    game.ui.pBtn_6.clicked.connect(game.btn_6)
    game.ui.pBtn_7.clicked.connect(game.btn_7)
    game.ui.pBtn_8.clicked.connect(game.btn_8)
    game.ui.pBtn_9.clicked.connect(game.btn_9)

    game.ui.pBtn_10.clicked.connect(game.btn_10)

    sys.exit(app.exec())
