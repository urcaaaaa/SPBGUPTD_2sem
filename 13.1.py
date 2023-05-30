from tkinter import *
import requests

root = Tk()

def get_weather():
    city = cityField.get()

    key = '5fe5fe8c2778cd24eff16d8c6ecf3d0c'
    url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {'APPID': key, 'q': city, 'units': 'imperial'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'Weather in {str(weather["name"])}: {weather["main"]["temp"]}°F'

root['bg'] = '#fafafa'
root.title('Weather App')
root.geometry('300x250')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text=' Get Weather ', command=get_weather)
btn.pack()

info = Label(frame_bottom, text=' Weather in City ', bg='#ffb700', font=40)
info.pack()

root.mainloop()
