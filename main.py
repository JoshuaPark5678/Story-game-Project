import time


#printing red
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
# ask the player for name  
def start(x):
  askName = str(input("\033[1;34;1m" + x + "what is your name?  \n:"))
  askNameConfirm = str(input("Is your name "+ askName.capitalize() + "?\n     y or n\n:"))
  if askNameConfirm == "y" or askNameConfirm == "Y":
    global name
    name = askName.capitalize()
    print("Okay " + name + " lets start your story.")
    gameStart()
  elif askNameConfirm == "n" or askNameConfirm == "N":
    start("")
  else: 
    prRed("|type a valid answer|")

def gameStart():
  time.sleep(3)
  clear = "\n" * 100
  print(clear)
  print("\033[1;32;1m" + "You woke up in a dark room. You are on a bed. You feel a little dizzy and tired")
  time.sleep(2)
  print("...")
  time.sleep(2)
  print("...")
  time.sleep(2)
  print("...\n")
  print("You wonder why you are here the first place but you dont seem to remember.")
  wakingUp = str(input("Will you get up from bed " + name + "?\n     y or n\n:"))
  if wakingUp == "y" or wakingUp == "Y":
    print("You lift your sore legs off the bed. It seems like you were on that bed for a long time...\n")
    time.sleep(2)
    print("Your eyes aren't adjusted to the dark yet so you can't see anything.\n")
    time.sleep(2)
    print("You walk foward about 5 steps and hit a wall.\n")
    time.sleep(2)
    print("Your mind has cleared up a bit and you notice that there is a door leaking out dim light\n")
    time.sleep(1)
    goToDoor = input("will you go to the door?\n     y or n\n:")
    if goToDoor == "y" or goToDoor == "Y":
      door()
    elif goToDoor == "n" or goToDoor == "N":
      print("You stand there still...")
      time.sleep(2)
      print("Your vision had been adjusted to the dark... You see a desk on the corner of the room")
      goToDoorOrDesk = input("Where will you go?\n   (1) Door  (2) Desk")
      if goToDoorOrDesk == 1:
        door()
      elif goToDoorOrDesk == 2:
        desk()
      else:
        prRed("|type a valid answer|")
  else:
    print("Your vision had been adjusted to the dark... you see a door a desk in the room")
    doorOrDesk = input("Where will you go?\n    (y) Door  (n) Desk\n:")
    if doorOrDesk == "y":
      door()
    elif doorOrDesk == "n":
      desk()
    else:
      prRed("|type a valid answer|")
        
def door():
  door = input("Your in front of the door.\n  (1) Try opening the door  (2) Look under the door (3) Keep exploring\n:")
  if door == "1":
    print("The door is locked")
    door()

  elif door == "2":
    print("You look under the door and see a long hallway with multiple doors on each side")
    door()

  elif door == "3":
    print("Your vision had been adjusted to the dark... You see a desk on the corner of the room")
    desk()
  else:
    prRed("|type a valid answer|")

  
def desk():
  desk = input("There are three drawers on the desk.\nwhat drawer will you open\n   (1)  (2)  (3)\n:")
  if desk == "1":
    print("Books and paper piled up but nothing important...")
    books = input("Will you search the books?\n    y or n\n:")
  
    if books == "y":
      print("It's dark but you still lift and open the book\n\nThe book is completly empty...")
      desk()
    elif books == "not":
      desk()
    else:
      prRed("|type a valid answer|")
  elif desk == "2":
    print("Empty")
  elif desk == "3":
    print("A green key")
    inventory = []
    inventory.append("Green key")
    print("Inventory:"+inventory)





start("Hello, ")