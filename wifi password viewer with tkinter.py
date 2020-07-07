from tkinter import *
import tkinter as tk
import subprocess
wifi = tk.Tk()
wifi.title("Wifi Password Viewer")
wifi.geometry("700x600+16+61")
wifi.configure(background='black')

def comut():
    system=tk.Label(text="...System Scann Completed...",fg='green',bg='black',font='1')
    system.pack()
    system2=tk.Label(text="--------------------------------------------------------------------------------",fg='red',bg='black',font='10')
    system2.pack()
    veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
    for i in sistemler:
        sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
        try:
            şifre = tk.Label(text="User: {:<10} || Pass: {:<} \n ".format(i, sonuç[0]),fg='green',bg='black',font="10")
            şifre.pack()
        except IndexError:
            bilgi = tk.Label(text=" |{:<30}=>  Pass: {:<}|".format(i, ""))
            şifre.pack()
sa =tk.Label(text="""  Welcome to Wifi Password Viewer   """,bg="black",fg="red",font="10")
sa.pack()

buton=tk.Button(text="Scann System",bg="red",command=comut,font='30')
buton.pack(padx=110, pady=10)

def quit():
    wifi.destroy()  
çıkış=tk.Button(text="Exit",command=quit,bg="red",font="30")
çıkış.pack()

ad=tk.Label(text="**This app coded by Emyounoone**",fg='blue',bg='black')
ad.pack(side='bottom')

wifi.mainloop()
