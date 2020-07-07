
print("--------")
print("""Welcome to Wifi Password Viewer.exe

                        -This App Coded by Emyounooone-
""")

import time
time.sleep(1)
while True:

    import subprocess

    print("System Analyzing Please Wait..")
    import time

    time.sleep(2)

    print("Wifi Passwords for saved in this PC: ")

    veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
    for i in sistemler:
        sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
        try:
            print(" \\{:<30}| Password:  {:<}".format(i, sonuç[0]))
        except IndexError:
            print(" \\{:<30}| Password:  {:<}".format(i, ""))

    exe = int(input("\n \n \nPress 1 to System Analysis Again \nPress 2 to Exit Wifi Password Viewer System "))
    if (exe == 1):
        print("")
        import time

        time.sleep(1)
        


    elif (exe == 2):
        print("")
        import time

        time.sleep(2)
        break
        quit()

    else:
        print("Please Try Again")

















