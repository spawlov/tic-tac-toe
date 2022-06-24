import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon

from x_o import Ui_Form


class MyGame(QtWidgets.QWidget):

    def __init__(self):
        super(MyGame, self).__init__()
        self._board = []
        self._counter = 0
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('media/icons/sf.ico'))
        self.setWindowTitle('Game Tic-Tac-Toe (for "Skill Factory")')

        self.reset_game()

        self.draw_board(self._board)
        self.label_message()

        self.ui.pBtn_1.clicked.connect(self.btn_1)
        self.ui.pBtn_2.clicked.connect(self.btn_2)
        self.ui.pBtn_3.clicked.connect(self.btn_3)
        self.ui.pBtn_4.clicked.connect(self.btn_4)
        self.ui.pBtn_5.clicked.connect(self.btn_5)
        self.ui.pBtn_6.clicked.connect(self.btn_6)
        self.ui.pBtn_7.clicked.connect(self.btn_7)
        self.ui.pBtn_8.clicked.connect(self.btn_8)
        self.ui.pBtn_9.clicked.connect(self.btn_9)

        self.ui.pBtn_10.clicked.connect(self.btn_10)

    def reset_game(self):
        self._board = [' ' for _ in range(9)]
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
        self.redraw()

    def redraw(self):
        self.draw_board(self._board)
        self.label_message()
        self.check_winner()

    def label_message(self):
        if not self._counter % 2:
            self.ui.label.setText('Сейчас ход "X"')
        else:
            self.ui.label.setText('Сейчас ход "O"')

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
            self._board[0] = 'X'
            self._counter += 1
        else:
            self._board[0] = 'O'
            self._counter += 1
        self.ui.pBtn_1.setEnabled(False)
        self.redraw()

    def btn_2(self):
        if not self._counter % 2:
            self._board[1] = 'X'
            self._counter += 1
        else:
            self._board[1] = 'O'
            self._counter += 1
        self.ui.pBtn_2.setEnabled(False)
        self.redraw()

    def btn_3(self):
        if not self._counter % 2:
            self._board[2] = 'X'
            self._counter += 1
        else:
            self._board[2] = 'O'
            self._counter += 1
        self.ui.pBtn_3.setEnabled(False)
        self.redraw()

    def btn_4(self):
        if not self._counter % 2:
            self._board[3] = 'X'
            self._counter += 1
        else:
            self._board[3] = 'O'
            self._counter += 1
        self.ui.pBtn_4.setEnabled(False)
        self.redraw()

    def btn_5(self):
        if not self._counter % 2:
            self._board[4] = 'X'
            self._counter += 1
        else:
            self._board[4] = 'O'
            self._counter += 1
        self.ui.pBtn_5.setEnabled(False)
        self.redraw()

    def btn_6(self):
        if not self._counter % 2:
            self._board[5] = 'X'
            self._counter += 1
        else:
            self._board[5] = 'O'
            self._counter += 1
        self.ui.pBtn_6.setEnabled(False)
        self.redraw()

    def btn_7(self):
        if not self._counter % 2:
            self._board[6] = 'X'
            self._counter += 1
        else:
            self._board[6] = 'O'
            self._counter += 1
        self.ui.pBtn_7.setEnabled(False)
        self.redraw()

    def btn_8(self):
        if not self._counter % 2:
            self._board[7] = 'X'
            self._counter += 1
        else:
            self._board[7] = 'O'
            self._counter += 1
        self.ui.pBtn_8.setEnabled(False)
        self.redraw()

    def btn_9(self):
        if not self._counter % 2:
            self._board[8] = 'X'
            self._counter += 1
        else:
            self._board[8] = 'O'
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
            if (self._board[line[0]] ==
                self._board[line[1]] ==
                self._board[line[2]] == 'X') \
                    or \
                    (self._board[line[0]] ==
                     self._board[line[1]] ==
                     self._board[line[2]] == 'O'):
                self.ui.label.setText(f'ПОБЕДА: "'
                                      f'{str(self._board[line[0]])}'
                                      f'" !!!')
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
                self.ui.label.setText('Ничья')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    game = MyGame()
    game.show()

    sys.exit(app.exec())
