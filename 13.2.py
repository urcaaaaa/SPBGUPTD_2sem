from tkinter import *
from PIL import Image, ImageTk
import requests

root = Tk()

deck_id = "new"

def get_card():
    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'

    response = requests.get(url)
    data = response.json()

    if 'cards' in data:
        code = data['cards'][0]['code']
        image_url = data['cards'][0]['image']
        value = data['cards'][0]['value']
        suit = data['cards'][0]['suit']

        info['text'] = f'Card: {value} of {suit}\nCode: {code}'
        image['image'] = ImageTk.PhotoImage(Image.open(requests.get(image_url, stream=True).raw).convert("RGB"))
    else:
        info['text'] = 'Error: Failed to retrieve card data'

    remaining = data['remaining']
    if remaining == 0:

        create_new_deck()

def create_new_deck():
    global deck_id
    url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
    response = requests.get(url)
    data = response.json()
    deck_id = data['deck_id']

root['bg'] = '#fafafa'
root.title('Deck of Cards App')
root.geometry('300x400')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.6)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.8, relwidth=0.7, relheight=0.1)

btn = Button(frame_top, text='Draw Card', command=get_card)
btn.pack()

info = Label(frame_top, text='Card: \nCode: ', bg='#ffb700', font=40)
info.pack()

image = Label(frame_bottom)
image.pack()

create_new_deck()

root.mainloop()
