from ZGameHumanPlay import ZGame
import tkinter as tk

moves = [[0, 0], [0, 0]]
HEIGHT = 960
WIDTH = 1600
POPHEIGHT = 960
POPWIDTH = 430
BUTTONWIDTH = 200
BUTTONHEIGHT = 200
root = tk.Tk()
root.title('ZoF')
isZero = True
howToPlay = "BASIC CONTROLS: In Zombies Or Flu, you play as the mayor of a town infected with the flu as well as " \
            "being invaded by zombies. As mayor, your job is to keep people safe, while protecting your career as a " \
            "politician through placing deployments in neighborhoods. In the game, information about your city, like " \
            "your resources, what day it is and the weather will be displayed"


def changeZero(booleaan):
    isZero = not booleaan


def endTurn():
    isEntryZero = True
    # save deployments poggers
    # wipe moves array
    # reset state, do behind the scenes actions
    # redraw ui


def helpMenu():  # display help menu

    # this is here because python is being mean to me
    howToPlay = "BASIC CONTROLS: In Zombies Or Flu, you play as the mayor of a town infected with the flu as well as " \
                "being invaded by zombies. As mayor, your job is to keep people safe, while protecting your career as " \
                "a politician through placing deployments in neighborhoods. In the game, information about your city, " \
                "like your resources, what day it is and the weather will be displayed. In order to make your move, " \
                "you can select the neighborhood that you want a deployment in by simply clicking on it. This will " \
                "open up another window in which neighborhood specific info is shown, as well as a place to create " \
                "and place deployments. Once you have placed your deployments, you can then end the turn and the next " \
                "turn will begin. Victory will be measured by how high your trust is as well as the amount of active, " \
                "sick and dead people present in the city at the end of the game " \
                "DEPLOYMENTS: below you will find a list of every deployment, as well as what it does" \
                "0: DO NOTHING, this deployment means for one of your 2 builds will do nothing" \
                "1: QUARANTINE OPEN" \
                "2: QUARANTINE FENCED" \
                "3: BITE CENTER DISINFECTANT"\
                "4: BITE CENTER AMPUTATE" \
                "5: ZOMBIE CURE FDA APPROVED - for 1 resource per turn, small chance zombie becomes a zombie bitten, and zombie bitten becomes human" \
                "6: ZOMBIE CURE EXPERIMENTAL - for 1 fear and resource per turn, chance zombie becomes zombie bitten and chance zombie bittne dies or becomes human" \
                "7: OPTIONAL FLU VACCINE -  " \
                "8: MANDATORY FLU VACCINE" \
                "9: FLU MUTATION CENTER" \
                "10:KILN WITH OVERSIGHT - turns dead into dead ashen" \
                "11:KILN WITHOUT OVERSIGHT - turns dead into dead ashen, small chance to turn zombies, sick and zombie bitten into dead ashen, " \
                "12:DON'T PANIC BROADCAST" \
                "13:CALL TO ARMS BROADCAST" \
                "14:SNIPER TOWER CONFIRM " \
                "15:SNIPER TOWER FREE" \
                "16:BRAIN PHEROMONES" \
                "17:MEAT PHEROMONES" \
                "18:BSL4LAB SAFETY ON" \
                "19:BSL4LAB SAFETY OFF" \
                "20:RALLY POINT OPY" \
                "21:RALLY POINT FULL" \
                "22:PRIMED FIREBOMB" \
                "23:FIREBOMB BARRAGE" \
                "24:SOCIAL DISTINCING SIGNS" \
                "25:SOCIAL DISTANCING WITH CELEBRETY ENDORSEMENT" \
                "26:POLICE STATION" \
                "27:SPY INFORMANTS"

    helpWindow = tk.Toplevel()
    x = root.winfo_x()
    y = root.winfo_y()
    helpWindow.geometry("%dx%d+%d+%d" % (WIDTH - POPWIDTH, HEIGHT, x, y))
    howToPlay = tk.Label(helpWindow)
    howToPlay.pack()


def whenClosed(deployinfo, topLevel):  # makes sure we save the buttonListenerFunction stuff
    if isZero:
        moves[0] = deployinfo
    else:
        moves[1] = deployinfo
    topLevel.destroy()
    changeZero(isZero)
    print('pls break')


def buttonListenerFunction(cityNum):  # city method clicker, will eventually chose team based on button pressed

    selected = tk.IntVar()
    cityMenu = tk.Toplevel()  # create window to display city info
    x = root.winfo_x()
    y = root.winfo_y()
    cityMenu.geometry("%dx%d+%d+%d" % (POPWIDTH, POPHEIGHT, x + 1100, y))
    global dropDownMenu
    global infoFrame, cityFrame, pictureFrame, censusFrame, trustNstuffFrame, buildingsFrame
    global populationNum, trustRank, activeLabel, activeCount, sickLabel, sickCount, zombieLabel, zombieCount, deadLabel, deadCount
    infoFrame = tk.Frame(cityMenu, bg='blue')
    infoFrame.place(relwidth=1, relheight=.2)
    cityFrame = tk.Frame(cityMenu, bg='yellow')
    cityFrame.place(rely=.2, relwidth=1, relheight=.6)
    pictureFrame = tk.Frame(cityMenu, bg='red')
    pictureFrame.place(rely=.8, relwidth=1, relheight=.2)
    censusFrame = tk.Frame(infoFrame, bg='purple')
    censusFrame.place(relx=.05, rely=.6, relwidth=.7, relheight=.6)
    trustNstuffFrame = tk.Frame(infoFrame, bg='yellow')
    trustNstuffFrame.place(relx=.1, rely=.1, relwidth=.7, relheight=.4)
    buildingsFrame = tk.Frame(cityFrame, bg='white')

    buildingsFrame.place(relx=.1, rely=.3, relwidth=.8, relheight=.6)
    populationNum = tk.Label(trustNstuffFrame, text='#people', bg='yellow')
    populationNum.place(relx=.1, rely=.3)
    trustRank = tk.Label(trustNstuffFrame, text='trust', bg='yellow')
    trustRank.place(relx=.5, rely=.3)

    dropDownMenu = tk.OptionMenu(cityFrame, selected, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    dropDownMenu.pack()

    activeLabel = tk.Label(censusFrame, text='ACTIVE', bg='purple', font=("Arial", 16))
    activeLabel.grid(row=0, column=0)
    activeCount = tk.Label(censusFrame, text="#active", bg='purple', font=("Arial", 16))
    activeCount.grid(row=1, column=0)
    sickLabel = tk.Label(censusFrame, text="SICK", bg='purple', font=("Arial", 16))
    sickLabel.grid(row=0, column=1)
    sickCount = tk.Label(censusFrame, text="#sick", bg='purple', font=("Arial", 16))
    sickCount.grid(row=1, column=1)
    zombieLabel = tk.Label(censusFrame, text="ZOMBIES", bg='purple', font=("Arial", 16))
    zombieLabel.grid(row=0, column=2)
    zombieCount = tk.Label(censusFrame, text="#zombies", bg='purple', font=("Arial", 16))
    zombieCount.grid(row=1, column=2)
    deadLabel = tk.Label(censusFrame, text="DEAD", bg='purple', font=("Arial", 16))
    deadLabel.grid(row=0, column=3)
    deadLabel = tk.Label(censusFrame, text="#dead", bg='purple', font=("Arial", 16))
    deadLabel.grid(row=1, column=3)

    cityMenu.protocol("WM_DELETE_WINDOW", lambda: whenClosed([cityNum, selected], cityMenu))
    # deploymentsPicture = [1]*28
    # deploymentsImageList = [...]
    # coming soon when making gui work with actual code
    # for i in range(len(city deployments list))
    #       deploymentsPicture[i] = tk.Frame(buildingsFrame, image = deploymentsImageList[city deployments list [i]]
    #       deploymentsPicture[i].place(nifty algorithm to figure out x and y ,width = 100,height = 100)
    #


# Michael, Chris and Athi: no you can't just write meaningless comments in your mod code

# Alex: haha shungite go brrrrrr


def resetEverything():  # the name is misleading, this is the main state of what the user sees
    global canvas, background_image, prettyPicture, cityImage, topFrame, labelList, helpButton, endTurnButton, buttonList
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='images/uibgv5.png')  # my pictures smile, will eventually simplify this part
    prettyPicture = tk.Label(root, image=background_image)
    prettyPicture.place(x=0, y=0)
    cityImage = tk.PhotoImage(file='images/cityPog.png')

    topFrame = tk.Frame(root, bg='white')
    topFrame.place(height=20, relwidth=1)

    labelList = ['SMH my head', '10 resourches', '2 builds', 'clear weather']
    for iter in range(4):
        labelList[iter] = tk.Label(topFrame, text=labelList[iter], bg='white')
        labelList[iter].place(relx=iter * .25)

    helpButton = tk.Button(topFrame, text='HELP', borderwidth=0, command=helpMenu)
    endTurnButton = tk.Button(topFrame, text='END', borderwidth=0, command=endTurn)
    endTurnButton.place(relx=.85)
    helpButton.place(relx=.925)

    # arrays for the buttons
    cordList = [[270, 100], [525, 100], [780, 100], [270, 350], [525, 350], [780, 350], [270, 630], [525, 630],
                [780, 630]]
    buttonList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(buttonList)):
        buttonList[i] = tk.Button(root, text='pog button', borderwidth=0, image=cityImage,
                                  command=lambda: buttonListenerFunction(i))
        buttonList[i].place(x=cordList[i][0], y=cordList[i][1], width=BUTTONWIDTH, height=BUTTONHEIGHT)
        # buttons made here


resetEverything()
root.mainloop()
