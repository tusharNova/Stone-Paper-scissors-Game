import sys , random

print("WelCome....")
print("let`s play🪨 (Stone)---📃(Paper)--✂️ (Scissors)")   
bot = "Neo-🤖"
data =f"""Some  rules
1) Your playing with {bot} (*The BOT*)
2) Winner show at last of Game
 Enjoy Game 🤘
"""
print(data)
player = input("Enter your name :-")
player = player.strip()+"-😎"
print(f"{bot} :- Let`s play {player}")
print(f"{bot} :- First is you")
cnt1 = 0 # for count of Player points
cnt2 = 0 # for count of Bot points
def select(tool):
    if tool == "stone":
        return "🪨"
    elif tool =="paper":
        return  "📃" 
    else:
        return "✂️"
def choices():
    lis = """ 
1 for Stone
2 for paper
3 for scissor"""
    global cnt1 , cnt2 , bot ,player
    smap ={
    1 : "stone",
    2 : "paper",
    3 : "scissor"}
    print(lis)
    pout = int(input("Choose anything form above:- "))
    if pout >3:
        print("Choose form only 1 ,2 ,3")
        choices()
    else:
        playert = smap[pout]
        playert = select(playert)
        print(f"{player}:- choose {playert}")
        f = ["stone","paper","scissor"]
        tools = random.choices(f) # random() get random result for bot
        bott = str(tools[0])
        bott = select(bott)
        print(f"{bot} :- choose {bott}")
        print("-"*20)
            # for Scissors case 
        if playert == "✂️" and bott =="🪨" :
            print(f"{bot} get 1 point")
            cnt2+=1 # for add point to bot
        elif playert == "✂️" and bott == "✂️" :
            print("It`s draw !")
        elif playert == "✂️" and bott == "📃" :
            print(f"{player} get 1 point")
            cnt1+=1 # for add point to player

            # for Paper case
        elif playert == "📃" and bott =="🪨" :
            print(f"{player} get 1 point")
            cnt1+=1 # for add point to player
        elif playert == "📃" and bott == "📃" :
            print("It`s draw !")
        elif playert == "📃" and bott == "✂️" :
            print(f"{bot} get 1 point")
            cnt2+=1 # for add point to bot
            # for stone case
        elif playert == "🪨" and bott == "📃" :
            print(f"{bot} get 1 point")
            cnt2+=1 # for add point to bot    
        elif playert == "🪨" and bott == "🪨" :
            print("It`s draw !")
        elif playert == "🪨" and bott == "✂️" :
            print(f"{player} get 1 point")
            cnt1+=1 # for add point to player

        ans = input("If want to Continue press [y/n]")

        if ans == ("y" or "Y" or "Yes"):

            print(f"Totol no of point {player} is {cnt1}")
            print(f"Totol no of point {bot} is {cnt2}")
            
            choices()
        else:
            print("-"*25)
            if cnt1 > cnt2:
                print(f"{player} is Winner have {cnt1} points")
            else:
                print(f"{bot} is Winner have {cnt2} points")
                print("Better Luck next time")
            sys.exit()
choices()