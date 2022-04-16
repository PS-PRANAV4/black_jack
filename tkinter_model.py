
import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter





def load_image(card_image):
    extension = 'png'
    suits = ["heart", "spade", "club", "diamond"]
    face_card = ["king", "jack", "queen"]
    for suit in suits:
        for card in range(1, 11):
            name = "E:\pranav ps\my project\TkInter_model\cards\{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_image.append((card, image))

        for card in face_card:
            name = "E:\pranav ps\my project\TkInter_model\cards\{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_image.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def deal_dealer():


    global dealer_ace
    global dealer_scorev

    card_value = deal_card(dealer_cardFrame)[0]
    # print(card_value)
    if card_value == 1 and not dealer_ace:
        card_value = 11
        dealer_ace = True
    dealer_scorev += card_value
    print(dealer_scorev)
    if card_value > 21 and  dealer_ace:
        card_value -= 10
        dealer_ace = False
    dealer_score.set(dealer_scorev)
    if dealer_scorev > 21:
        result_text.set("player wins")


def deal_player():
    global player_ace
    global player_scorev

    card_value = deal_card(player_card_frame)[0]
    # print(card_value)
    if card_value == 1 and not player_ace:
        card_value = 11
        player_ace = True
    player_scorev += card_value
    print(player_scorev)
    if card_value > 21 and not player_ace:
        card_value -= 10
        player_ace = False
    player_score.set(player_scorev)
    if player_scorev > 21:
        result_text.set("dealer wins")



# declaring the main window
mainWindow = tkinter.Tk()
# setting up the main_window first title of the window and then geometry
mainWindow.title("black jack")
mainWindow.geometry("680x480")
mainWindow.configure(background="blue")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)
dealer_score = tkinter.IntVar()
tkinter.Label(cardFrame, text="dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealer_score, background="green", fg="white").grid(row=1, column=0)
dealer_cardFrame = tkinter.Frame(cardFrame, background="green")
dealer_cardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)
player_score = tkinter.IntVar()
tkinter.Label(cardFrame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=player_score, background="green", fg="white").grid(row=3, column=0)
player_card_frame = tkinter.Frame(cardFrame, background="green")
player_card_frame.grid(row=8, column=5, columnspan=5, sticky="w")
button_frame = tkinter.Frame(mainWindow)
player_ace = False
player_scorev = 0
dealer_ace = False
dealer_scorev = 0
# card_value = 0


button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
player_button = tkinter.Button(button_frame, text="player", command=deal_player)
player_button.grid(row=0, column=0)
dealer_button = tkinter.Button(button_frame, text="dealer", command=deal_dealer)
dealer_button.grid(row=0, column=1)
cards = []
load_image(cards)
print(cards)
deck = list(cards)
random.shuffle(deck)
dealer_hand = []
player_hand = []
mainWindow.mainloop()
