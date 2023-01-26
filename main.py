from random import *
import string
import json
from pyautogui import hotkey
from time import sleep
from pyperclip import copy

main_list = [[string.ascii_uppercase], [string.ascii_lowercase], [string.digits], [string.punctuation]]
letters_upper = [string.ascii_uppercase]
letters_lower = [string.ascii_lowercase]
digits = [string.digits]
symbols = [r'!#$%&\()*+,-./:;<=>?@\\^_~']
logo = r"""
Made by : Fahad Salman, Abdualaziz

  _____                                    _   __  __                                   
 |  __ \                                  | | |  \/  |                                  
 | |__) |_ _ ___ _____      _____  _ __ __| | | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                         __/ |          
                                                                        |___/           
"""


# This function is used to generate a password from a list of digits, letters, and punctuation and randomize it so that
# it much secure ,
def pass_gen():
    global password_len, website, email, data, default_email
    hotkey('ctrl', 'l')
    while True:
        try:
            password_len = int(input("What is the length of the Password you want (the length should be more than 9):"))
            if password_len < 9:
                print("this integer is less than 9")
                continue
            with open("default_em.json", 'r') as file:
                email_json = json.load(file)
                default_email = email_json["default_email"]["email"]
            if "@" in default_email:
                want_use_default = input("Do you want to use you default email ? (yes/no): ")
                if want_use_default == "yes":
                    email = default_email
                elif want_use_default == "no":
                    email = input("what is the email that you want to save with this password ?: ")
            else:
                email = input("what is the email that you want to save with this password ?: ")
            website = input("what website is this password for? : ")

            break
        except ValueError:
            print("this is not an integer, try again")

    # making the password with choice method
    password = ""
    for i in range(password_len):
        password += choice(main_list[randint(0, 3)][0])
    copy(password)
    print("the password has been copied to you clipboard, you can paste it now !")
    j_pass = {
        website:
            {
                "email": email,
                "password": password
            }
    }

    with open("pwd.json", "r") as file:
        try:
            data = json.load(file)
            data.update(j_pass)
            err = False
        except json.decoder.JSONDecodeError:
            err = True

    with open("pwd.json", "w") as file:
        if err == True:
            json.dump(j_pass, file, indent=4)
        else:
            json.dump(data, file, indent=4)


while True:
    hotkey('ctrl', 'l')
    empty = ""
    counter = 0
    print(logo)
    main = input("0-Generate Password\n"
                 "1-View my Passwords\n"
                 "2-Set a Default Email\n"
                 "3-Important Notes\n"
                 "4-Exit\n")

    if main == "0":
        pass_gen()
    elif main == "1":
        hotkey('ctrl', 'l')
        with open("pwd.json", "r") as file:
            try:
                passwords = json.load(file)
            except json.decoder.JSONDecodeError:
                passwords = None
            if type(passwords) == "str":
                continue
            elif passwords == None or passwords == {}:
                print("Passwords:\nNone\n----------------------------------------------")
                counter += 1
                back = input("0-back\n")
                if back == "0":
                    continue
            else:
                print("Passwords:")
                for key in passwords.keys():
                    print(
                        f'{counter}-website: {key} | email: {passwords[key]["email"]} | password: {passwords[key]["password"]}')
                    counter += 1
                counter = 0
                print("----------------------------------------------")
                back = input("0-back\n"
                             "1-delete one by its index\n"
                             "2-delete all passwords\n")
                if back == "0":
                    continue
                elif back == "1":
                    hotkey('ctrl', 'l')
                    for key in passwords.keys():
                        print(
                            f'{counter}-website: {key} | email: {passwords[key]["email"]} | password: {passwords[key]["password"]}')
                        counter += 1
                    delete_one = input(
                        "-------------------------------------------------------------\nchoose one by its website name to delete:\n")
                    for key in passwords.keys():
                        if delete_one == key:
                            with open("pwd.json", 'r') as f:
                                p_data = json.load(f)
                                del p_data[key]
                            with open("pwd.json", 'w') as f:
                                json.dump(p_data, f, indent=4)
                    counter = 0
                elif back == "2":

                    with open("pwd.json", 'r') as f:
                        p_data = json.load(f)
                        p_data.clear()
                    with open("pwd.json", "w") as file:
                        json.dump(p_data, file, indent=4)
                else:
                    print("this is not a valid number\n you will be redirected to the main menu.")
                    sleep(2)
                    continue



    elif main == "2":
        hotkey('ctrl', 'l')
        default_email = input("what Default Email you want to set ?:\n"
                              "(press enter if you want to rest it to be nothing)\n")
        default_email_json = {
            "default_email": {
                "email": default_email
            }
        }
        with open("default_em.json", "w") as file:
            json.dump(default_email_json, file, indent=4)
    elif main == "3":
        hotkey('ctrl', 'l')
        print("firts note:\n"
              "if you want to save 2 websites with the same name you should add numbers\n"
              "to the second and a different number for the third one and so on, because if you didn't do that when\n"
              " you try delete one password you the program will delete all passwords with the same website name.\n"
              "-------------------------------------------------------------------------------------")
        if input("0-back\n") == "0":
            continue

    elif main == "4":
        hotkey('ctrl', 'l')
        break
    else:
        print("this is not a valid number\n you will be redirected to the main menu.")
        sleep(2)
        continue
