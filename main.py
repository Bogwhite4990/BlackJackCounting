import webbrowser
from tkinter import *

FONT_TEXT = ("Cooper", 10, "bold")
BACKGROUND_COLOR = "#5299BF"
FONT_NUMBER_SUM = ("Cooper", 20, "bold")
FONT_COUNT = ("Constantia", 10, "bold")
FONT_NUMBER_MOVEMENT = ("Cooper", 12, "bold")
FONT_CHANCE_NUMBER = ("Arial", 25, "bold")


# Website link
def open_web_browser():
    webbrowser.open("www.adrian-bogdan.com")


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        # Add icon here
        self.iconbitmap("cards/bj_img.ico")
        self.geometry("800x850")
        self.title("Black Jack Count/Predict")
        self.config(background="#5299BF")
        self.count = IntVar()
        self.count_number = 0
        self.card_number_player = 0
        self.card_number_player2 = 0
        self.card_number_dealer = 0
        self.deck_number_counting = IntVar()

        # Label for the move - change everytime
        self.label_movement = Label(text="WAIT FOR THE MOVEMENT", font=FONT_NUMBER_MOVEMENT,
                                    background=BACKGROUND_COLOR)
        self.label_movement.place(x=460, y=749)

        # Info for first part
        self.label_info_send = Label(text="Do not use this if you use the script below", font=("Arial", 8),
                                     background=BACKGROUND_COLOR)
        self.label_info_send.place(x=10, y=258)

        # Cards text on the screen
        self.text_entry = Label(text="CARDS:", background=BACKGROUND_COLOR, font=FONT_TEXT)
        self.text_entry.place(x=100, y=200)

        # Cards entry on the screen
        self.entry_cards = Entry(textvariable=self.count)
        self.entry_cards.place(x=180, y=200)

        # Label for alert <<<
        self.alert_label = Label(text="↓ DO NOT LEAVE THIS BLANK  ↓", font=("Arial", 8, "bold"), background="red")
        self.alert_label.place(x=150, y=170)

        def count_cards():
            if 2 <= self.count.get() < 7:
                self.count_number += 1
                self.counter_label_variable_total_sum.config(text=self.count_number)
                self.entry_cards.delete(0, END)
                self.entry_cards.insert(0, "")
            elif 7 <= self.count.get() <= 9:
                self.count_number += 0
                self.counter_label_variable_total_sum.config(text=self.count_number)
                self.entry_cards.delete(0, END)
                self.entry_cards.insert(0, "")
            elif 10 <= self.count.get() <= 11:
                self.count_number -= 1
                self.counter_label_variable_total_sum.config(text=self.count_number)
                self.entry_cards.delete(0, END)
                self.entry_cards.insert(0, "")
            else:
                self.count_number += 0
                self.counter_label_variable_total_sum.config(text=self.count_number)

            # Change color for text
            check_color()

        def check_color():
            if self.count_number == 0:
                self.counter_label_variable_total_sum.config(fg="black")
            elif self.count_number > 0:
                self.counter_label_variable_total_sum.config(fg="#7CFC00")
            elif self.count_number < 0:
                self.counter_label_variable_total_sum.config(fg="red")

        # Button submit
        self.submit_button = Button(text="SEND", command=count_cards)
        self.submit_button.place(x=180, y=230)

        # Counter
        self.counter_label = Label(text="Count: ", font=FONT_COUNT, background=BACKGROUND_COLOR)
        self.counter_label.place(x=100, y=300)

        self.counter_label_variable_total_sum = Label(text=self.count_number, font=FONT_NUMBER_SUM,
                                                      background=BACKGROUND_COLOR)
        self.counter_label_variable_total_sum.place(x=200, y=293)

        # Commands buttons for each
        def button_1():
            check_color()
            self.count_number += 1
            self.counter_label_variable_total_sum.config(text=self.count_number)

        def button_2():
            check_color()
            self.count_number += 0
            self.counter_label_variable_total_sum.config(text=self.count_number)

        def button_3():
            check_color()
            self.count_number -= 1
            self.counter_label_variable_total_sum.config(text=self.count_number)

        # Buttons for easy entry
        # ---------------1
        self.button_number_1 = Button(text=" 2 ", command=button_1, width=4, height=2)
        self.button_number_1.place(x=100, y=360)
        # ---------------2
        self.button_number_2 = Button(text=" 3 ", command=button_1, width=4, height=2)
        self.button_number_2.place(x=140, y=360)
        # ---------------3
        self.button_number_3 = Button(text=" 4 ", command=button_1, width=4, height=2)
        self.button_number_3.place(x=180, y=360)
        # ---------------4
        self.button_number_4 = Button(text=" 5 ", command=button_1, width=4, height=2)
        self.button_number_4.place(x=100, y=405)
        # ---------------5
        self.button_number_5 = Button(text=" 6 ", command=button_1, width=4, height=2)
        self.button_number_5.place(x=140, y=405)
        # ---------------6
        self.button_number_6 = Button(text=" 7 ", command=button_2, width=4, height=2)
        self.button_number_6.place(x=180, y=405)
        # ---------------7
        self.button_number_7 = Button(text=" 8 ", command=button_2, width=4, height=2)
        self.button_number_7.place(x=100, y=450)
        # ---------------8
        self.button_number_8 = Button(text=" 9 ", command=button_2, width=4, height=2)
        self.button_number_8.place(x=140, y=450)
        # ---------------9
        self.button_number_9 = Button(text="10", command=button_3, width=4, height=2)
        self.button_number_9.place(x=180, y=450)
        # ---------------10
        self.button_number_10 = Button(text="11", command=button_3, width=4, height=2)
        self.button_number_10.place(x=140, y=495)

        # Create line
        self.button_line = Button()
        self.button_line.place(x=0, y=140, height=0, width=800)

        self.button_line1 = Button()
        self.button_line1.place(x=0, y=280, height=0, width=380)

        self.button_line2 = Button()
        self.button_line2.place(x=380, y=140, height=680, width=0)

        self.button_line3 = Button()
        self.button_line3.place(x=0, y=820, height=0, width=800)

        self.button_line4 = Button()
        self.button_line4.place(x=0, y=600, height=0, width=380)

        # Dealer cards
        self.label_dealer_text = Label(text="Dealer card:", font=FONT_TEXT, background=BACKGROUND_COLOR)
        self.label_dealer_text.place(x=400, y=170)

        # --------- Dealer cards buttons to add them in the count + functions
        def dealer_button2():
            self.image_2_club = PhotoImage(file="cards/2_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 2

        def dealer_button3():
            self.image_2_club = PhotoImage(file="cards/3_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 3

        def dealer_button4():
            self.image_2_club = PhotoImage(file="cards/4_of_clubs.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 4

        def dealer_button5():
            self.image_2_club = PhotoImage(file="cards/5_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 5

        def dealer_button6():
            self.image_2_club = PhotoImage(file="cards/6_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 6

        def dealer_button7():
            self.image_2_club = PhotoImage(file="cards/7_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 7

        def dealer_button8():
            self.image_2_club = PhotoImage(file="cards/8_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 8

        def dealer_button9():
            self.image_2_club = PhotoImage(file="cards/9_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 9

        def dealer_button10():
            self.image_2_club = PhotoImage(file="cards/10_of_spades.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 10

        def dealer_button11():
            self.image_2_club = PhotoImage(file="cards/ace_of_spades2.png")
            self.card_front_place.config(image=self.image_2_club)
            self.card_number_dealer = 11

        self.dealer_button_2 = Button(text=" 2 ", command=dealer_button2)
        self.dealer_button_2.place(x=400, y=200, width=40, height=40)

        self.dealer_button_3 = Button(text=" 3 ", command=dealer_button3)
        self.dealer_button_3.place(x=450, y=200, width=40, height=40)

        self.dealer_button_4 = Button(text=" 4 ", command=dealer_button4)
        self.dealer_button_4.place(x=500, y=200, width=40, height=40)

        self.dealer_button_5 = Button(text=" 5 ", command=dealer_button5)
        self.dealer_button_5.place(x=550, y=200, width=40, height=40)

        self.dealer_button_6 = Button(text=" 6 ", command=dealer_button6)
        self.dealer_button_6.place(x=400, y=250, width=40, height=40)

        self.dealer_button_7 = Button(text=" 7 ", command=dealer_button7)
        self.dealer_button_7.place(x=450, y=250, width=40, height=40)

        self.dealer_button_8 = Button(text=" 8 ", command=dealer_button8)
        self.dealer_button_8.place(x=500, y=250, width=40, height=40)

        self.dealer_button_9 = Button(text=" 9 ", command=dealer_button9)
        self.dealer_button_9.place(x=550, y=250, width=40, height=40)

        self.dealer_button_10 = Button(text="10", command=dealer_button10)
        self.dealer_button_10.place(x=450, y=300, width=40, height=40)

        self.dealer_button_11 = Button(text="11", command=dealer_button11)
        self.dealer_button_11.place(x=500, y=300, width=40, height=40)

        # BACK OF THE CARDS FOR THE DEALER
        self.dealer_card_back_image = PhotoImage(file="cards/cards_back.png")
        self.card_back_place = Label(image=self.dealer_card_back_image)
        self.card_back_place.place(x=620, y=200)

        # FRONT CARD FOR THE DEALER
        self.dealer_card_front_image = PhotoImage(file="cards/cards_back.png")
        self.card_front_place = Label(image=self.dealer_card_back_image)
        self.card_front_place.place(x=700, y=200)

        # Player cards

        self.first_player_hand = Label(text="First card", font=FONT_TEXT, bg=BACKGROUND_COLOR, fg="purple")
        self.first_player_hand.place(x=530, y=400)

        self.first_player_hand = Label(text="Second card", font=FONT_TEXT, bg=BACKGROUND_COLOR, fg="purple")
        self.first_player_hand.place(x=510, y=580)

        self.label_dealer_text = Label(text="Player cards:", font=FONT_TEXT, background=BACKGROUND_COLOR)
        self.label_dealer_text.place(x=400, y=400)

        # --------- Player cards buttons to add them in the count + functions
        def player_button2():
            self.image_2_club2 = PhotoImage(file="cards/2_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club2)
            self.card_number_player = 2

        def player_button3():
            self.image_2_club3 = PhotoImage(file="cards/3_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club3)
            self.card_number_player = 3

        def player_button4():
            self.image_2_club4 = PhotoImage(file="cards/4_of_clubs.png")
            self.card_back_place_player.config(image=self.image_2_club4)
            self.card_number_player = 4

        def player_button5():
            self.image_2_club5 = PhotoImage(file="cards/5_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club5)
            self.card_number_player = 5

        def player_button6():
            self.image_2_club6 = PhotoImage(file="cards/6_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club6)
            self.card_number_player = 6

        def player_button7():
            self.image_2_club7 = PhotoImage(file="cards/7_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club7)
            self.card_number_player = 7

        def player_button8():
            self.image_2_club8 = PhotoImage(file="cards/8_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club8)
            self.card_number_player = 8

        def player_button9():
            self.image_2_club9 = PhotoImage(file="cards/9_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club9)
            self.card_number_player = 9

        def player_button10():
            self.image_2_club10 = PhotoImage(file="cards/10_of_spades.png")
            self.card_back_place_player.config(image=self.image_2_club10)
            self.card_number_player = 10

        def player_button11():
            self.image_2_club11 = PhotoImage(file="cards/ace_of_spades2.png")
            self.card_back_place_player.config(image=self.image_2_club11)
            self.card_number_player = 11

        self.player_button_2 = Button(text=" 2 ", command=player_button2)
        self.player_button_2.place(x=400, y=430, width=40, height=40)

        self.player_button_3 = Button(text=" 3 ", command=player_button3)
        self.player_button_3.place(x=450, y=430, width=40, height=40)

        self.player_button_4 = Button(text=" 4 ", command=player_button4)
        self.player_button_4.place(x=500, y=430, width=40, height=40)

        self.player_button_5 = Button(text=" 5 ", command=player_button5)
        self.player_button_5.place(x=550, y=430, width=40, height=40)

        self.player_button_6 = Button(text=" 6 ", command=player_button6)
        self.player_button_6.place(x=400, y=480, width=40, height=40)

        self.player_button_7 = Button(text=" 7 ", command=player_button7)
        self.player_button_7.place(x=450, y=480, width=40, height=40)

        self.player_button_8 = Button(text=" 8 ", command=player_button8)
        self.player_button_8.place(x=500, y=480, width=40, height=40)

        self.player_button_9 = Button(text=" 9 ", command=player_button9)
        self.player_button_9.place(x=550, y=480, width=40, height=40)

        self.player_button_10 = Button(text="10", command=player_button10)
        self.player_button_10.place(x=450, y=530, width=40, height=40)

        self.player_button_11 = Button(text="11", command=player_button11)
        self.player_button_11.place(x=500, y=530, width=40, height=40)

        # ----------- Player back cards image
        self.player_back_card_image = PhotoImage(file="cards/cards_back.png")
        self.card_back_place_player = Label(image=self.player_back_card_image)
        self.card_back_place_player.place(x=620, y=430)

        self.player_back_card_image1 = PhotoImage(file="cards/cards_back.png")
        self.card_back_place_player1 = Label(image=self.player_back_card_image)
        self.card_back_place_player1.place(x=700, y=430)

        # Player second cards button functions

        def player_button2_func():
            self.image_2_player_club2 = PhotoImage(file="cards/2_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club2)
            self.card_number_player2 = 2

        def player_button3_func():
            self.image_2_player_club3 = PhotoImage(file="cards/3_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club3)
            self.card_number_player2 = 3

        def player_button4_func():
            self.image_2_player_club4 = PhotoImage(file="cards/4_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club4)
            self.card_number_player2 = 4

        def player_button5_func():
            self.image_2_player_club5 = PhotoImage(file="cards/5_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club5)
            self.card_number_player2 = 5

        def player_button6_func():
            self.image_2_player_club6 = PhotoImage(file="cards/6_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club6)
            self.card_number_player2 = 6

        def player_button7_func():
            self.image_2_player_club7 = PhotoImage(file="cards/7_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club7)
            self.card_number_player2 = 7

        def player_button8_func():
            self.image_2_player_club8 = PhotoImage(file="cards/8_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club8)
            self.card_number_player2 = 8

        def player_button9_func():
            self.image_2_player_club9 = PhotoImage(file="cards/9_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club9)
            self.card_number_player2 = 9

        def player_button10_func():
            self.image_2_player_club10 = PhotoImage(file="cards/10_of_spades.png")
            self.card_back_place_player1.config(image=self.image_2_player_club10)
            self.card_number_player2 = 10

        def player_button11_func():
            self.image_2_player_club11 = PhotoImage(file="cards/ace_of_spades2.png")
            self.card_back_place_player1.config(image=self.image_2_player_club11)
            self.card_number_player2 = 11

        # Player second hand buttons
        self.player_button_2_hand2 = Button(text=" 2 ", command=player_button2_func)
        self.player_button_2_hand2.place(x=400, y=610, width=40, height=40)

        self.player_button_3_hand2 = Button(text=" 3 ", command=player_button3_func)
        self.player_button_3_hand2.place(x=450, y=610, width=40, height=40)

        self.player_button_4_hand2 = Button(text=" 4 ", command=player_button4_func)
        self.player_button_4_hand2.place(x=500, y=610, width=40, height=40)

        self.player_button_5_hand2 = Button(text=" 5 ", command=player_button5_func)
        self.player_button_5_hand2.place(x=550, y=610, width=40, height=40)

        self.player_button_6_hand2 = Button(text=" 6 ", command=player_button6_func)
        self.player_button_6_hand2.place(x=600, y=610, width=40, height=40)

        self.player_button_7_hand2 = Button(text=" 7 ", command=player_button7_func)
        self.player_button_7_hand2.place(x=650, y=610, width=40, height=40)

        self.player_button_8_hand2 = Button(text=" 8 ", command=player_button8_func)
        self.player_button_8_hand2.place(x=700, y=610, width=40, height=40)

        self.player_button_9_hand2 = Button(text=" 9 ", command=player_button9_func)
        self.player_button_9_hand2.place(x=750, y=610, width=40, height=40)

        self.player_button_10_hand2 = Button(text="10", command=player_button10_func)
        self.player_button_10_hand2.place(x=550, y=660, width=40, height=40)

        self.player_button_11_hand2 = Button(text="11", command=player_button11_func)
        self.player_button_11_hand2.place(x=600, y=660, width=40, height=40)

        # Win Prediction
        def send_command_info():
            DEALER_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            player_card_count = self.card_number_player + self.card_number_player2
            # Derivative number method
            if player_card_count == 16 and self.card_number_dealer == 11 and self.count_number > 3:
                self.label_movement.config(text="Take insurance")
            elif player_card_count == 16 and self.card_number_dealer == 10 and self.count_number > 5:
                self.label_movement.config(text="STAND")
            elif player_card_count == 16 and self.card_number_dealer == 10 and self.count_number > 0:
                self.label_movement.config(text="STAND")
            elif player_card_count == 15 and self.card_number_dealer == 10 and self.count_number > 4:
                self.label_movement.config(text="STAND")
            elif player_card_count == 13 and self.card_number_dealer == 2 and self.count_number == -1:
                self.label_movement.config(text="STAND")
            elif player_card_count == 13 and self.card_number_dealer == 3 and self.count_number == -2:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer == 2 and self.count_number > 4:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer == 3 and self.count_number > 2:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer == 4 and self.count_number > 0:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer == 5 and self.count_number == -1:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer == 6 and self.count_number < -1:
                self.label_movement.config(text="STAND")
            elif player_card_count == 11 and self.card_number_dealer == 11 and self.count_number == 1:
                self.label_movement.config(text="DOUBLE DOWN")
            elif player_card_count == 10 and self.card_number_dealer == 10 and self.count_number > 4:
                self.label_movement.config(text="DOUBLE DOWN")
            elif player_card_count == 10 and self.card_number_dealer == 11 and self.count_number > 4:
                self.label_movement.config(text="DOUBLE DOWN")
            elif player_card_count == 9 and self.card_number_dealer == 2 and self.count_number == 1:
                self.label_movement.config(text="DOUBLE DOWN")
            elif player_card_count == 9 and self.card_number_dealer == 7 and self.count_number > 4:
                self.label_movement.config(text="DOUBLE DOWN")
            elif self.card_number_player == 10 and self.card_number_player2 == 10 and self.card_number_dealer == 5 and self.count_number > 5:
                self.label_movement.config(text="SPLIT THE HAND")
            elif self.card_number_player == 10 and self.card_number_player2 == 10 and self.card_number_dealer == 6 and self.count_number > 5:
                self.label_movement.config(text="SPLIT THE HAND")

            elif self.card_number_player == self.card_number_player2:
                if player_card_count == 22 and self.card_number_dealer in DEALER_CARDS:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 20 and self.card_number_dealer in DEALER_CARDS:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 18 and self.card_number_dealer in DEALER_CARDS[0:5]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 18 and self.card_number_dealer in DEALER_CARDS[5:6]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 18 and self.card_number_dealer in DEALER_CARDS[6:9]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 18 and self.card_number_dealer in DEALER_CARDS[9:-1]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 16 and self.card_number_dealer in DEALER_CARDS:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 14 and self.card_number_dealer in DEALER_CARDS[0:6]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 14 and self.card_number_dealer in DEALER_CARDS[7:-1]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 12 and self.card_number_dealer in DEALER_CARDS[0:1]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 12 and self.card_number_dealer in DEALER_CARDS[1:5]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 12 and self.card_number_dealer in DEALER_CARDS[6:-1]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 10 and self.card_number_dealer in DEALER_CARDS:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 8 and self.card_number_dealer in DEALER_CARDS[0:3]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 8 and self.card_number_dealer in DEALER_CARDS[3:6]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 8 and self.card_number_dealer in DEALER_CARDS[6:-1]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 6 and self.card_number_dealer == 2:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 6 and self.card_number_dealer == 3:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 6 and self.card_number_dealer in DEALER_CARDS[2:6]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 6 and self.card_number_dealer in DEALER_CARDS[6:-1]:
                    self.label_movement.config(text="DO NOT SPLIT")
                elif player_card_count == 4 and self.card_number_dealer == 2:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 4 and self.card_number_dealer == 3:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 4 and self.card_number_dealer in DEALER_CARDS[2:6]:
                    self.label_movement.config(text="SPLIT THE PAIR")
                elif player_card_count == 4 and self.card_number_dealer in DEALER_CARDS[6:-1]:
                    self.label_movement.config(text="DO NOT SPLIT")
            elif self.card_number_player == 11 or self.card_number_player2 == 11:
                if self.card_number_player == 9 or self.card_number_player2 == 9 and self.card_number_dealer in DEALER_CARDS:
                    self.label_movement.config(text="STAND")
                elif self.card_number_player == 8 or self.card_number_player2 == 8 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  0:4]:
                    self.label_movement.config(text="STAND")
                elif self.card_number_player == 8 or self.card_number_player2 == 8 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  4:5]:
                    self.label_movement.config(text="DOUBLE ELSE STAND")
                elif self.card_number_player == 8 or self.card_number_player2 == 8 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="STAND")
                elif self.card_number_player == 7 or self.card_number_player2 == 7 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  0:5]:
                    self.label_movement.config(text="DOUBLE ELSE STAND")
                elif self.card_number_player == 7 or self.card_number_player2 == 7 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:7]:
                    self.label_movement.config(text="STAND")
                elif self.card_number_player == 7 or self.card_number_player2 == 7 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  7:-1]:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 6 or self.card_number_player2 == 6 and self.card_number_dealer in \
                        DEALER_CARDS[0]:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 6 or self.card_number_player2 == 6 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  1:5]:
                    self.label_movement.config(text="DOUBLE ELSE HIT")
                elif self.card_number_player == 6 or self.card_number_player2 == 6 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="HIT")
                # A5
                elif self.card_number_player == 5 or self.card_number_player2 == 5 and self.card_number_dealer == 2:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 5 or self.card_number_player2 == 5 and self.card_number_dealer == 3:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 5 or self.card_number_player2 == 5 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  2:5]:
                    self.label_movement.config(text="DOUBLE ELSE HIT")
                elif self.card_number_player == 5 or self.card_number_player2 == 5 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="HIT")
                # A4
                elif self.card_number_player == 4 or self.card_number_player2 == 4 and self.card_number_dealer in \
                        DEALER_CARDS[0]:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 4 or self.card_number_player2 == 4 and self.card_number_dealer in \
                        DEALER_CARDS[1]:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 4 or self.card_number_player2 == 4 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  2:5]:
                    self.label_movement.config(text="DOUBLE ELSE HIT")
                elif self.card_number_player == 4 or self.card_number_player2 == 4 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="HIT")
                # A3
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer == 2:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer == 3:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer == 4:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  3:5]:
                    self.label_movement.config(text="DOUBLE ELSE HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="HIT")
                # A2
                elif self.card_number_player == 2 or self.card_number_player2 == 2 and self.card_number_dealer == 2:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 2 or self.card_number_player2 == 2 and self.card_number_dealer == 3:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 2 or self.card_number_player2 == 2 and self.card_number_dealer == 4:
                    self.label_movement.config(text="HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  3:5]:
                    self.label_movement.config(text="DOUBLE ELSE HIT")
                elif self.card_number_player == 3 or self.card_number_player2 == 3 and self.card_number_dealer in DEALER_CARDS[
                                                                                                                  5:-1]:
                    self.label_movement.config(text="HIT")

            # Second instruction

            elif player_card_count == 17 and self.card_number_dealer in DEALER_CARDS:
                self.label_movement.config(text="STAND")
            elif player_card_count == 16 and self.card_number_dealer in DEALER_CARDS[0:5]:
                self.label_movement.config(text="STAND")
            elif player_card_count == 16 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 15
            elif player_card_count == 15 and self.card_number_dealer in DEALER_CARDS[0:5]:
                self.label_movement.config(text="STAND")
            elif player_card_count == 16 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 14
            elif player_card_count == 14 and self.card_number_dealer in DEALER_CARDS[0:5]:
                self.label_movement.config(text="STAND")
            elif player_card_count == 14 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 13
            elif player_card_count == 13 and self.card_number_dealer in DEALER_CARDS[0:5]:
                self.label_movement.config(text="STAND")
            elif player_card_count == 13 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 12
            elif player_card_count == 12 and self.card_number_dealer == 2:
                self.label_movement.config(text="HIT")
            elif player_card_count == 12 and self.card_number_dealer == 3:
                self.label_movement.config(text="HIT")
            elif player_card_count == 12 and self.card_number_dealer in DEALER_CARDS[2:5]:
                self.label_movement.config(text="STAND")
            elif player_card_count == 12 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 11
            elif player_card_count == 11 and self.card_number_dealer in DEALER_CARDS:
                self.label_movement.config(text="DOUBLE ELSE HIT")
            # 10
            elif player_card_count == 10 and self.card_number_dealer in DEALER_CARDS[0:8]:
                self.label_movement.config(text="DOUBLE ELSE HIT")
            elif player_card_count == 10 and self.card_number_dealer in DEALER_CARDS[8:-1]:
                self.label_movement.config(text="HIT")
            # 9
            elif player_card_count == 9 and self.card_number_dealer == 2:
                self.label_movement.config(text="HIT")
            elif player_card_count == 9 and self.card_number_dealer in DEALER_CARDS[1:5]:
                self.label_movement.config(text="DOUBLE ELSE HIT")
            elif player_card_count == 9 and self.card_number_dealer in DEALER_CARDS[5:-1]:
                self.label_movement.config(text="HIT")
            # 8
            elif player_card_count == 8 and self.card_number_dealer in DEALER_CARDS:
                self.label_movement.config(text="HIT")
            else:
                self.label_movement.config(text="HIT")

            if player_card_count == 21:
                self.label_movement.config(text="BJ WIN")

            # Derivative BJ cards and new

        # Send button
        self.send_info_button = Button(text="SEND", command=send_command_info)
        self.send_info_button.place(x=700, y=750)

        # HIT STAND DOUBLE

        self.what_to_do_label = Label(text="MOVE:", font=FONT_TEXT, bg=BACKGROUND_COLOR)
        self.what_to_do_label.place(x=400, y=750)

        # Percent for winning
        self.winning_label_text = Label(text="Chance of winning")
        self.winning_label_text.place(x=130, y=620)

        self.deck_name_label_text = Label(text="Decks:", font=FONT_TEXT, background=BACKGROUND_COLOR)
        self.deck_name_label_text.place(x=50, y=670)

        self.entry_deck_number = Entry(textvariable=self.deck_number_counting)
        self.entry_deck_number.place(x=100, y=670)

        def calculate_chance():
            total = self.count_number / self.deck_number_counting.get()
            print(self.count_number)
            print(self.deck_number_counting.get())
            if total > 0.6:
                self.display_calculate_chance.config(text=round(total, 2), fg="green")
            else:
                self.display_calculate_chance.config(text=round(total, 2), fg="red")

        self.calculate_button = Button(text="Calculate", command=calculate_chance)
        self.calculate_button.place(x=150, y=700)

        # ---------- label for function and display

        self.display_calculate_chance = Label(text="00", font=FONT_CHANCE_NUMBER, background=BACKGROUND_COLOR)
        self.display_calculate_chance.place(x=150, y=750)

        self.prc_display = Label(text="%", font=FONT_CHANCE_NUMBER, background=BACKGROUND_COLOR)
        self.prc_display.place(x=230, y=750)

        # LOGO

        self.logo_image = PhotoImage(file="cards/bj_img.png")
        self.logo_label = Label(image=self.logo_image, background=BACKGROUND_COLOR)
        self.logo_label.place(x=290, y=2)

        # Copyright
        self.label_copyright = Button(text="2023 Copyright v1.0", background=BACKGROUND_COLOR, command=open_web_browser)
        self.label_copyright.place(x=675, y=825)


if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
