import sys
from PyQt5 import uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

from card import Card

class Pyramid_UI(QMainWindow):
    def __init__(self):
        super(Pyramid_UI, self).__init__()
        self.pyramidUI()

    def pyramidUI(self):
        self.ui_pyramid = uic.loadUi('game.ui')

        self.ui_pyramid.setWindowFlags(Qt.WindowTitleHint)

        self.ui_pyramid.action_New_Game.triggered.connect(self.newGame)
        self.ui_pyramid.action_New_Game.setShortcut('Ctrl+N')
        self.ui_pyramid.action_Exit.triggered.connect(self.exitGame)
        self.ui_pyramid.action_Exit.setShortcut('Ctrl+Q')

        self.cards = Card()

        self.ui_pyramid.next_card.clicked.connect(self.move_card)

        self.cards_table = [self.ui_pyramid.card_t1, self.ui_pyramid.card_t2, self.ui_pyramid.card_t3, self.ui_pyramid.card_t4,
                            self.ui_pyramid.card_t5, self.ui_pyramid.card_t6, self.ui_pyramid.card_t7, self.ui_pyramid.card_t8, 
                            self.ui_pyramid.card_t9, self.ui_pyramid.card_t10, self.ui_pyramid.card_t11, self.ui_pyramid.card_t12, 
                            self.ui_pyramid.card_t13, self.ui_pyramid.card_t14, self.ui_pyramid.card_t15, self.ui_pyramid.card_t16, 
                            self.ui_pyramid.card_t17, self.ui_pyramid.card_t18, self.ui_pyramid.card_t19, self.ui_pyramid.card_t20,
                            self.ui_pyramid.card_t21, self.ui_pyramid.card_t22, self.ui_pyramid.card_t23, self.ui_pyramid.card_t24, 
                            self.ui_pyramid.card_t25, self.ui_pyramid.card_t26, self.ui_pyramid.card_t27, self.ui_pyramid.card_t28]
        self.cards_tabel_range = []

        self.cards_deck = [self.ui_pyramid.card_d1, self.ui_pyramid.card_d2, self.ui_pyramid.card_d3, self.ui_pyramid.card_d4,
                           self.ui_pyramid.card_d5, self.ui_pyramid.card_d6, self.ui_pyramid.card_d7, self.ui_pyramid.card_d8,
                           self.ui_pyramid.card_d9, self.ui_pyramid.card_d10, self.ui_pyramid.card_d11, self.ui_pyramid.card_d12,
                           self.ui_pyramid.card_d13, self.ui_pyramid.card_d14, self.ui_pyramid.card_d15, self.ui_pyramid.card_d16,
                           self.ui_pyramid.card_d17, self.ui_pyramid.card_d18, self.ui_pyramid.card_d19, self.ui_pyramid.card_d20,
                           self.ui_pyramid.card_d21, self.ui_pyramid.card_d22, self.ui_pyramid.card_d23, self.ui_pyramid.card_d24]
        self.cards_deck_range = []

        self.remove_pairs = []
        self.move_deck_increment = 0
        self.nubrer_hands = 0

        for i in range(len(self.cards_table)):
            temp = self.cards.__next__()
            self.cards_tabel_range.append(temp)
            pixmap = QIcon()
            if i >= 0 and i <= 27:
                pixmap.addPixmap(QPixmap(str(temp) + '.jpg'))
                self.cards_table[i].setIcon(pixmap)
            self.cards_table[i].setIconSize(QSize(100, 150))
            self.cards_table[i].clicked.connect(self.remove_pair_card)

        for i in range(len(self.cards_deck)):
            temp = self.cards.__next__()
            self.cards_deck_range.append(temp)
            pixmap = QIcon()
            pixmap.addPixmap(QPixmap(str(temp) + '.jpg'))
            self.cards_deck[i].setIcon(pixmap)
            self.cards_deck[i].setIconSize(QSize(100, 150))
            self.cards_deck[i].clicked.connect(self.remove_pair_card)

        self.ui_pyramid.show()

    def move_card(self):
        if self.nubrer_hands >= 0 and self.nubrer_hands <= 3:
            if self.move_deck_increment == len(self.cards_deck):
                if self.nubrer_hands != 2:
                    for i in range(len(self.cards_deck)):
                        self.cards_deck[i].move(305, 510)
                        self.cards_deck[i].setHidden(False)
                self.move_deck_increment = 0
                self.nubrer_hands += 1

            elif self.nubrer_hands == 3:
                self.overGame()

            else:
                self.cards_deck[self.move_deck_increment].move(495, 510)
                if self.move_deck_increment > 0:
                    self.cards_deck[self.move_deck_increment-1].setHidden(True)
                self.move_deck_increment += 1

    def choose_card(self, sender):
        list_for_card = []
        for i in range(len(self.cards_deck)):
            if self.cards_deck[i] == sender:
                temp = str(self.cards_deck_range[i])
                temp = temp[::-1]
                temp = temp[:3]
                temp = temp[1:]
                temp = temp[::-1]
                temp = int(temp)
                if temp == 13:
                    self.del_card_deck(i+1)
                else:
                    list_for_card.append(2)
                    list_for_card.append(i+1)
                    list_for_card.append(temp)
                    self.remove_pairs.append(list_for_card)
                break


        for i in range(len(self.cards_table)):
            if self.cards_table[i] == sender:
                temp = str(self.cards_tabel_range[i])
                temp = temp[::-1]
                temp = temp[:3]
                temp = temp[1:]
                temp = temp[::-1]
                temp = int(temp)
                if temp == 13:
                    self.del_card_table(i+1)
                else:
                    list_for_card.append(1)
                    list_for_card.append(i+1)
                    list_for_card.append(temp)
                    self.remove_pairs.append(list_for_card)
                break

    def remove_pair_card(self):
        sender = self.sender()
        self.choose_card(sender)
        if len(self.remove_pairs) == 2:
            if self.remove_pairs[0][0] == 1 and self.remove_pairs[1][0] == 1:
                if (self.remove_pairs[0][2] + self.remove_pairs[1][2]) == 13:
                    self.del_card_table(self.remove_pairs[0][1])
                    self.del_card_table(self.remove_pairs[1][1])

            elif self.remove_pairs[0][0] == 2 and self.remove_pairs[1][0] == 2:
                if (self.remove_pairs[0][2] + self.remove_pairs[1][2]) == 13:
                    self.del_card_deck(self.remove_pairs[0][1])
                    self.del_card_deck(self.remove_pairs[1][1])

            else:
                if (self.remove_pairs[0][2] + self.remove_pairs[1][2]) == 13:
                    if self.remove_pairs[0][0] == 1:
                        self.del_card_table(self.remove_pairs[0][1])

                    if self.remove_pairs[1][0] == 1:
                        self.del_card_table(self.remove_pairs[1][1])

                    if self.remove_pairs[0][0] == 2:
                        self.del_card_deck(self.remove_pairs[0][1])

                    if self.remove_pairs[1][0] == 2:
                        self.del_card_deck(self.remove_pairs[1][1])
            self.remove_pairs = []

            card_del = 0
            for i in self.cards_table:
                if i == ' ':
                    card_del += 1
            if card_del == 28:
                self.winGame()

    def del_card_table(self, position):
        self.cards_table[position - 1].setHidden(True)
        self.cards_table.pop(position - 1)
        self.cards_table.insert(position - 1, ' ')
        line = 0
        summ = 0
        for i in range(7):
            summ += line
            if position > summ:
                line += 1
        summ = 0
        for i in range(line + 1):
            summ += i

        if position == summ and position != 1:
            if self.cards_table[position - 2] == ' ':
                self.cards_table[(position - line) - 1].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[(position - line) - 1]) + '.jpg'))
                self.cards_table[(position - line) - 1].setIcon(pixmap)
                self.cards_table[(position - line) - 1].setIconSize(QSize(100, 150))

        elif position == ((summ - line) + 1) and position != 1:
            if self.cards_table[position] == ' ':
                self.cards_table[position - line].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[position - line]) + '.jpg'))
                self.cards_table[position - line].setIcon(pixmap)
                self.cards_table[position - line].setIconSize(QSize(100, 150))

        elif position == 1:
            pass

        else:
            if self.cards_table[position] == ' ' and self.cards_table[position-2] == ' ':
                self.cards_table[((position - line) - 1)].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[((position - line) - 1)]) + '.jpg'))
                self.cards_table[((position - line) - 1)].setIcon(pixmap)
                self.cards_table[((position - line) - 1)].setIconSize(QSize(100, 150))

                self.cards_table[position - line].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[position - line]) + '.jpg'))
                self.cards_table[position - line].setIcon(pixmap)
                self.cards_table[position - line].setIconSize(QSize(100, 150))

            elif self.cards_table[position] == ' ' and self.cards_table[position-2] != ' ':
                self.cards_table[position - line].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[position - line]) + '.jpg'))
                self.cards_table[position - line].setIcon(pixmap)
                self.cards_table[position - line].setIconSize(QSize(100, 150))

            elif self.cards_table[position] != ' ' and self.cards_table[position-2] == ' ':
                self.cards_table[((position - line) - 1)].setEnabled(True)
                pixmap = QIcon()
                pixmap.addPixmap(QPixmap(str(self.cards_tabel_range[((position - line) - 1)]) + '.jpg'))
                self.cards_table[((position - line) - 1)].setIcon(pixmap)
                self.cards_table[((position - line) - 1)].setIconSize(QSize(100, 150))


    def del_card_deck(self, position):
        self.cards_deck[position-1].setHidden(True)
        self.cards_deck.pop(position-1)
        self.cards_deck_range.pop(position-1)

        if self.nubrer_hands == 3:
            if len(self.cards_deck) != 1:
                self.cards_deck[len(self.cards_deck) - 2].setHidden(False)

        elif self.move_deck_increment == position and self.nubrer_hands != 3:
            self.cards_deck[self.move_deck_increment-2].setHidden(False)
            self.move_deck_increment -= 1

    def newGame(self):
        new_g = QMessageBox.question(self, 'Message', "Start a New Game?",
                                        QMessageBox.Yes | QMessageBox.No)
        if new_g == QMessageBox.Yes:
            self.pyramidUI()
        elif new_g == QMessageBox.No:
            self.close()

    def winGame(self):
        win_g = QMessageBox.question(self, 'Information', "Congratulations!!! \n You Finished The Game!!!",
                                        QMessageBox.Retry | QMessageBox.Close)
        if win_g == QMessageBox.Retry:
            self.pyramidUI()
        elif win_g == QMessageBox.Close:
            self.ui_pyramid.close()

    def overGame(self):
        over_g = QMessageBox.question(self, 'Information', "You Lost The Game!!!",
                                        QMessageBox.Retry | QMessageBox.Close)
        if over_g == QMessageBox.Retry:
            self.pyramidUI()
        elif over_g == QMessageBox.Close:
            self.ui_pyramid.close()

    def exitGame(self):
        exit_a = QMessageBox.question(self, 'Message', "Quit of The Game?",
                                        QMessageBox.Yes | QMessageBox.No)
        if exit_a == QMessageBox.Yes:
            self.ui_pyramid.close()
        elif exit_a == QMessageBox.No:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pyramid_UI()
    sys.exit(app.exec_())