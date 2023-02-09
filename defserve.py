import time
import sqlite3
from colorama import Fore, Style
from sqlitedict import SqliteDict

#setting up the colors
red = Fore.RED

lred = Fore.LIGHTRED_EX

black = Fore.BLACK

lblack = Fore.LIGHTBLACK_EX

white = Fore.WHITE

lwhite = Fore.LIGHTWHITE_EX

green = Fore.GREEN

lgreen = Fore.LIGHTGREEN_EX

cyan = Fore.CYAN

lcyan = Fore.LIGHTCYAN_EX

magenta = Fore.MAGENTA

lmagenta = Fore.LIGHTMAGENTA_EX

yellow = Fore.YELLOW

lyellow = Fore.LIGHTYELLOW_EX

blue = Fore.BLUE

lblue = Fore.LIGHTBLUE_EX

reset = Fore.RESET

bright = Style.BRIGHT

reset_style = Style.RESET_ALL

diary = {}

instruction = f"""0:search\n1:Display Your passwords 📃\n2:Adds password ➕\n3:Removes Password ➖\n4:Exit❌ \n0:search """

class MyClass():
    def __init__(self, param):
        self.param = param
 
def save(key, value, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value # Using dict[key] to store
            mydict.commit() # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)
 
def load(key, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key] # No need to use commit(), since we are only loading data!
        return value
    except Exception as ex:
        print("Error during loading data:", ex)

while True:

  print(instruction)

  c1 = int(input(f"{green}Enter your choice :{blue}"))
  if c1 == 0:
    m= input("Enter the website:")
    if m in diary:
      print(diary[m])
    else:
      print("No such website found❌")
  if c1 == 1:

    ("you choose", c1)

    if diary == {}:

      print(

        f"{yellow}you don't have any password saved ,BUT YOU CAN ADD SOME PASSWORD🔐 "

      )



    for i in diary:

      print(f"{i}:{diary[i]}")

  if c1 == 2:

    ("you choose", c1)

    a = input(f"{red}Enter website:{cyan}")

    b = input(f"{red}Enter the password:{cyan}")

    diary[a] = MyClass(b)
    save("MyClass_key",diary)

    print("processing ⚙")

    time.sleep(3)

    print(f"{green}PASSWORD ADDED SUCCESSFULLY ✅")

  if c1 == 3:

    ("you choose", c1)

    ab = input(f"{red}Enter the website:{cyan}")

    diary.pop(ab)

    print("processing ⚙")
    save("MyClass_key",diary)

    time.sleep(3)

    print(f"{green}PASSWORD REMOVED SUCCESSFULLY ✅")

  if c1 == 4:

    break

  else:

    print()
