# Steve Wills
# 9/27/24
# Adventure Game
# see doc in github repo for documentation

def main():
    game = gameDB()
    keepGoing = True
    node = "start"
    while keepGoing == True:
        if node == "quit":
            keepGoing = False
        else:
            node = playGame(game, node)

def gameDB():
    game = {
      "start": ["You are in a skyscraper, its on fire… Do you jump to your death or run down the stairs. ", "Jump", "jump", "Take the stairs", "stairs"], 
      "jump": ["You are dead… splat!", "Start over", "start", "Quit", "quit"], 
      "stairs": ["As you run down the stairs, you hear people yelling for help. Help them or keep running?", "Help", "help", "Keep Running", "run"], 
      "help": ["Take one for the team, eh?! They made it, you didn’t. ", "Start over", "start", "Quit", "quit"], 
      "run": ["You can't save them, but you can save yourself! But now, you are blocked by fire… you see a door. Open it or Kick it in?!", "Open it", "open", "Kick it", "kick"], 
      "open": ["That was easier than expected! You see more stairs and an open window. Its probably too high to jump… Run or Jump?", "Run", "run2", "Jump", "jump2"], 
      "kick": ["You broke your foot! You won't be able to get out on your own… you died… ", "Start over", "start", "Quit", "quit"], 
      "run2": ["you finally see a door. It's locked. But it has a small window. Break the window and open the door? Or Keep going? ", "break window", "window", "Keep Going", "go"], 
      "jump2": ["you shouldn't have done that… too high… Splat!", "Start over", "start", "Quit", "quit"], 
      "window": ["you open the door and find yourself on the 10th floor. You frantically look around and see a small spiral staircase. Take the stairs or keep looking?", "Spiral stairs", "stairs2", "Look around", "look"], 
      "stairs2": ["you parkour down the stairs… you made it out!  You win! ", "Start over", "start", "Quit", "quit"],
      "look": ["Why would you do that?! the building is about to collapse. time wasted == death! ", "Start over", "start", "Quit", "quit"],
      }
    return game

def playGame(game, nodeOption):
    node = game[nodeOption]
    (description, menuA, nodeA, menuB, nodeB) = node
    print (f"""{description}
    1: {menuA}
    2: {menuB}""")
    choice = input("Please choose 1 or 2: ")
    if choice == "1":
        node = nodeA
    if choice == "2":
        node = nodeB
    return node

main()