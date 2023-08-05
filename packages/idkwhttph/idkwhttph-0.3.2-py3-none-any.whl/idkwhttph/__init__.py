__version__ = "0.3.2"
# Imports
import bcrypt
from getkey import getkey, keys
from replit import clear
from replit import db
from time import sleep
import json
import shutil
import os
import sys
from replit.database import AsyncDatabase


  
'''
This module generates ANSI character codes to printing colors to terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code
'''

  
  
CSI = '\033['
OSC = '\033]'
BEL = '\a'


def code_to_chars(code):
    return CSI + str(code) + 'm'

def set_title(title):
    return OSC + '2;' + title + BEL

def clear_screen(mode=2):
    return CSI + str(mode) + 'J'

def clear_line(mode=2):
    return CSI + str(mode) + 'K'


class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'
    def DOWN(self, n=1):
        return CSI + str(n) + 'B'
    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'
    def BACK(self, n=1):
        return CSI + str(n) + 'D'
    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'


class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107


class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()
F = AnsiFore()
B   = AnsiBack()
S  = AnsiStyle()
C = AnsiCursor()

if os.name == 'nt':
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide(stream=sys.stdout):
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        stream.write("\033[?25l")
        stream.flush()

def show(stream=sys.stdout):
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        stream.write("\033[?25h")
        stream.flush()
        
class HiddenCursor(object):
    def __init__(self, stream=sys.stdout):
        self._stream = stream
    def __enter__(self):
        hide(stream=self._stream)
    def __exit__(self, type, value, traceback):
        show(stream=self._stream)



def printInMiddle(text, columns=shutil.get_terminal_size().columns):
    # Get the current width of the console
    console_width = columns

    # Calculate the padding for the left side
    padding = (console_width - len(text)) // 2 + 5

    # Print the padded text
    print(" " * padding + text)


def write(string: str, speed: int = 0.05) -> None:
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(speed)


backup_file_path = "backup.json"


def create_backup(data_base):
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file, indent=2)


def load_backup(data_base):
    if os.path.exists(backup_file_path):
        with open(backup_file_path, "r") as file:
            backup_data = json.load(file)
            data_base.update(backup_data)


def save_backup(data_base):
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file)


def sync_backup(data_base):
    with open(backup_file_path, "r") as file:
        backup_data = json.load(file)

    data_base.update(backup_data)

    create_backup(data_base)





def print_layer():
    console_width = shutil.get_terminal_size().columns
    for i in range(console_width):
        print("-", end="")
    print()
    # Print a newline at the end


def options(prompt, menu, title, bold, PIM: bool) -> None:
    
    global bold_yes
    if bold:
        bold_yes = S.BRIGHT
    elif bold == False:
        bold_yes = S.NORMAL
    else:
        return 0
    selection = 0
    key = None

    while True:
        try:
            while key != keys.ENTER:
                clear()
                if title == False:
                    pass
                else:
                    if PIM == True:
                        printInMiddle(f"{bold_yes}{title}")
                        print_layer()
                    elif PIM == False:
                        print(f"{bold_yes}{title}")
                        print_layer()
                    else:
                        return
                if prompt == False:
                    pass
                else:
                    print(f"{bold_yes}{prompt}")
                for i in range(len(menu)):
                    opt = menu[i]
                    if i == selection:
                        print(f"{bold_yes}> {opt}")

                    else:
                        print(f"{bold_yes}  {opt}")

                key = getkey()
                if key == keys.W or key == keys.UP:
                    clear()
                    selection = (selection - 1) % len(menu)
                    if selection == -1:
                        selection = (selection + len(menu) + 1) % len(menu)
                elif key == keys.S or key == keys.DOWN:
                    clear()
                    selection = (selection + 1) % len(menu)
                    if selection > len(menu):
                        selection = (selection - len(menu) - 1) % len(menu)
            return selection

        except:
            clear()


def crash():
    exec(
        type((lambda: 0).__code__)(
            0, 0, 0, 0, 0, 0, b"\x053", (), (), (), "", "", 0, b""
        )
    )
    clear()





backup_file_path = "backup.json"





def load_json_data():
    with open("backup.json", "r") as file:
        data = json.load(file)
    return data


JLI = False
# Fake password
username = [""]
list_1 = [""]
default = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "n",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "_",
    "-",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "B",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "N",
    "M",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
Restrictions = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "n",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "_",
    "-",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "B",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "N",
    "M",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

options = ["Username: ", "PassWord: ", "Show Password", "Hide password", "Submit!"]


def enter_to_continue():
    print(f"{S.BRIGHT}|{F.BLUE}Enter{F.WHITE}|To Continue")
    input()


# Real password
list_2 = [""]
list_3 = list_1


def Sign_In() -> None:
    global list_1, list_2, list_3, username, menu, show_hide, alert, JLI, matches
    username = [""]
    list_1 = [""]
    list_2 = [""]
    list_3 = list_1
    alert = False
    show_hide = False
    if show_hide:
        menu = ["Username: ", "PassWord: ", "Hide Password", "Submit!"]
    if show_hide == False:
        menu = ["Username: ", "PassWord: ", "Show Password", "Submit!"]
    opt_2 = ""
    Hello = False
    opt = ""

    if JLI == True:
        selection = 4
        JLI = False
    else:
        selection = 0
    key = ""
    while True:
        try:
            if show_hide:
                menu = [
                    "Username: ",
                    "PassWord: ",
                    "Hide Password",
                    "Submit!",
                    "Already Have an Account?",
                ]
            if show_hide == False:
                menu = [
                    "Username: ",
                    "PassWord: ",
                    "Show Password",
                    "Submit!",
                    "Already Have an Account?",
                ]

            if key == keys.ENTER:
                if opt == "PassWord: ":
                    break
            clear()
            print(f"{S.RESET_ALL}------------------------------------")
            print("             Sign In!")
            print("")
            print("Please use the arrow keys to move Up or Down")
            print("")
            for i in range(len(menu)):
                opt = menu[i]
                if i == selection:
                    if opt == "PassWord: ":
                        opt_2 = "".join(list_2)
                        if Hello:
                            print(f"> {opt}{opt_2}")
                        else:
                            opt_2 = "".join(list_1)
                            print(f"> {opt}{opt_2}")

                    elif opt == "Username: ":
                        if Hello:
                            print(f'> {opt}{"".join(username)}')
                        else:
                            print(f'> {opt}{"".join(username)}')
                    else:
                        print(f"> {opt}")

                else:
                    if opt == "PassWord: ":
                        if Hello:
                            print(f'  {opt}{"".join(list_2)}')
                        else:
                            print(f'  {opt}{"".join(list_1)}')

                    elif opt == "Username: ":
                        if Hello:
                            print(f'  {opt}{"".join(username)}')
                        else:
                            print(f'  {opt}{"".join(username)}')
                    else:
                        print(f"  {opt}")

            key = getkey()

            string = key

            if key == keys.UP:
                selection = (selection - 1) % len(menu)
                if selection == -1:
                    selection = (selection + len(menu) + 1) % len(menu)
            elif key == keys.DOWN:
                selection = (selection + 1) % len(menu)
                if selection > len(menu):
                    selection = (selection - len(menu) - 1) % len(menu)
            if key == keys.UP or key == keys.DOWN:
                pass
            else:
                if selection == 0 or selection == 1:
                    if key == keys.ENTER:
                        alert = True
                    else:
                        pass

                if alert == True:
                    alert = False

                elif alert == False:
                    clear()
                    if key == keys.ENTER and selection == 4:
                        clear()
                        print("Redirecting you to login!")
                        sleep(3)
                        clear()
                        sleep(0.5)
                        Log_In()
                    else:
                        if key == keys.ENTER and selection == 3:
                            if "".join(username) == "" or "".join(list_2) == "":
                                print("You have not entered a username or password")
                                enter_to_continue()
                                clear()
                            elif len(list_2) <= 8:
                                print("Your password must be atleast 8 characters")
                                enter_to_continue()
                                clear()

                            else:
                                clear()
                                print("Signed in!")
                                enter_to_continue()
                                clear()
                                show()

                                matches = db.prefix("Name")
                                matches = list(matches)
                                matches = len(matches)

                                db["Name" + str(matches)] = "".join(username)
                                db["password" + str(matches)] = "".join(list_2)
                                break
                        elif (
                            key == keys.ENTER
                            and selection == 2
                            and menu[2] == "Show Password"
                        ):
                            list_3 = list_2
                            Hello = True
                            show_hide = True
                        elif (
                            key == keys.ENTER
                            and selection == 2
                            and menu[2] == "Hide Password"
                        ):
                            list_3 = list_1
                            Hello = False
                            show_hide = False
                        if selection == 1:
                            if key == keys.BACKSPACE:
                                temp_var = list_1.pop(-1)
                                temp_var = list_2.pop(-1)
                            else:
                                list_1 += "*"
                                list_2 += string
                        if selection == 0:
                            if key == keys.BACKSPACE:
                                try:
                                    username.pop(-1)
                                except:
                                    clear()
                            else:
                                if string not in Restrictions:
                                    pass
                                else:
                                    if string == keys.ENTER:
                                        pass
                                    else:
                                        username += string
                        clear()
        except:
            clear()

def verify_password(password: list) -> bool:
  clear()
  print('Verifying password.. This may take awhile')
  print('Reason: we are generating 2^30 rounds of salt ( 1.073B rounds ) to verify your password.')
  
  password_bytes = password.encode('utf-8')
  salt = bcrypt.gensalt(30)
  salt_str = salt.decode('utf-8')
  
  x = password_bytes + salt
  data = load_json_data()
  matches = len(data)
  sleep(2)
  
  for i in range(matches):
    y = data["password" + str(i)].encode('utf-8')+salt
    if (
          "".join(username) == data["Name" + str(i)]
          and x == y
    ):
      sleep(2)
      return True
  print('Incorrect password!')
  enter_to_continue()
  clear()
  return False

def Log_In():
    hide()
    global list_1, list_2, list_3, username, menu, show_hide, alert, JLI
    alert = False
    show_hide = False
    username = [""]
    list_1 = [""]
    list_2 = [""]
    list_3 = list_1
    if show_hide:
        menu = ["Username: ", "PassWord: ", "Hide Password", "Submit!"]
    if show_hide == False:
        menu = ["Username: ", "PassWord: ", "Show Password", "Submit!"]
    opt_2 = ""
    Hello = False
    opt = ""
    selection = 4
    key = ""
    while True:
        try:
            if show_hide:
                menu = [
                    "Username: ",
                    "PassWord: ",
                    "Hide Password",
                    "Log In!",
                    "Don't have an account?",
                ]
            if show_hide == False:
                menu = [
                    "Username: ",
                    "PassWord: ",
                    "Show Password",
                    "Log In!",
                    "Don't have an account?",
                ]

            if key == keys.ENTER:
                if opt == "PassWord: ":
                    break
            clear()
            print(f"{S.RESET_ALL}------------------------------------")
            print("             Log In!")
            print("")
            print("Please use the arrow keys to move Up or Down")
            print("")
            for i in range(len(menu)):
                opt = menu[i]
                if i == selection:
                    if opt == "PassWord: ":
                        opt_2 = "".join(list_2)
                        if Hello:
                            print(f"> {opt}{opt_2}")
                        else:
                            opt_2 = "".join(list_1)
                            print(f"> {opt}{opt_2}")

                    elif opt == "Username: ":
                        if Hello:
                            print(f'> {opt}{"".join(username)}')
                        else:
                            print(f'> {opt}{"".join(username)}')
                    else:
                        print(f"> {opt}")

                else:
                    if opt == "PassWord: ":
                        if Hello:
                            print(f'  {opt}{"".join(list_2)}')
                        else:
                            print(f'  {opt}{"".join(list_1)}')

                    elif opt == "Username: ":
                        if Hello:
                            print(f'  {opt}{"".join(username)}')
                        else:
                            print(f'  {opt}{"".join(username)}')
                    else:
                        print(f"  {opt}")

            key = getkey()
            string = key

            if key == keys.UP:
                selection = (selection - 1) % len(menu)
                if selection == -1:
                    selection = (selection + len(menu) + 1) % len(menu)
            elif key == keys.DOWN:
                selection = (selection + 1) % len(menu)
                if selection > len(menu):
                    selection = (selection - len(menu) - 1) % len(menu)
            if key == keys.UP or key == keys.DOWN:
                pass
            else:
                if selection == 0 or selection == 1:
                    if key == keys.ENTER:
                        alert = True
                    else:
                        pass

                if alert == True:
                    alert = False

                elif alert == False:
                    clear()
                    if key == keys.ENTER and selection == 4:
                        JLI = True
                        Sign_In()
                    else:
                        if key == keys.ENTER and selection == 3:
                            if "".join(username) == "" or "".join(list_2) == "":
                                print("You have not entered a username or password")
                                enter_to_continue()
                                clear()
                                break

                            else:
                                
                                if verify_password(''.join(list_2)):
                                  clear()
                                  print("Logged in!")
                                  enter_to_continue()
                                  clear()
                                  show()

                                  return True
                                else:
                                    print("Invalid username or password!")
                                    enter_to_continue()
                                    clear()
                        elif (
                            key == keys.ENTER
                            and selection == 2
                            and menu[2] == "Show Password"
                        ):
                            list_3 = list_2
                            Hello = True
                            show_hide = True
                        elif (
                            key == keys.ENTER
                            and selection == 2
                            and menu[2] == "Hide Password"
                        ):
                            list_3 = list_1
                            Hello = False
                            show_hide = False
                        if selection == 1:
                            if key == keys.BACKSPACE:
                                temp_var = list_1.pop(-1)
                                temp_var = list_2.pop(-1)
                            else:
                                list_1 += "*"
                                list_2 += string
                        if selection == 0:
                            if key == keys.BACKSPACE:
                                try:
                                    username.pop(-1)
                                except:
                                    clear()
                            else:
                                if string not in Restrictions:
                                    pass
                                else:
                                    if string == keys.ENTER:
                                        pass
                                    else:
                                        username += string
                        clear()
        except:
            clear()