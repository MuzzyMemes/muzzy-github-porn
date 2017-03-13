def optionMenu():
    Options = ""
    while Options != "A" and Options != "B" and Options != "C" and Options != "Q":
        Options = input("Option A\tSearch for a fixture\nOption B\tOutstanding fixtures\nOption C\tDisplay leaderboard\n\nEnter Q to quit\n\nOption: ")
    if Options== "A":
        optionA();
    elif Options== "B":
        optionB();
    elif Options== "C":
        optionC();
    else:
        exit()

def optionA():
    found=False
    try:
        fi=open("fixtures.txt","r")
        data=fi.readlines()
    except IOError:
        print("\nError: File could not be found!\n")
        optionMenu();
    else:
        fi.close()
        fixnum=input("Please enter the fixture number you would like to look for: ")

        print("fixture number  Fixture Date  Player 1 Nickname  Player 2 Nickname  Fixture Played  Winning Nickname")

        for li in data:
            if(li.split(",")[0]) == fixnum:
                print(li.split(",")[0],li.split(",")[1],li.split(",")[2],li.split(",")[3],li.split(",")[4],li.split(",")[5])
                found=True
        if found==False:
            print("The specified fixture number was not found")
            optionMenu();
def optionB():
    print("similar thing. no point in including it.")
    optionMenu();
    
def optionC():
    try:
        results=open("results.txt","r")
        data=results.readlines()
    except IOError:
        print("\nError: File could not be found!\n")
        optionMenu();
    else:
        results.close()
        print("\nPlayer Nickname"," "*2,"Matches Played"," "*2,"Matches Won"," "*2,"Matches Lost"," "*2,"Points")

        for li in data:
            if(li.split(",")[2]) >= "1":

                points=int(li.split(",")[2])
                type(points)
                pN=int(len(li.split(",")[0]))
                type(pN)
                mP=int(len(li.split(",")[1]))
                type(mP)
                mW=int(len(li.split(",")[2]))
                type(mW)
                mL=int(len(li.split(",")[3]))
                type(mL)
                
                print(li.split(",")[0]," "*(21-pN),li.split(",")[1]," "*(16-mP),li.split(",")[2]," "*(16-mW),li.split(",")[3],points*3)
        

#calls the function optionMenu
optionMenu();
    
