import random
no= random.randint(1,7)
Hello=str(input("Hello would you like you roll a dice (Say yes if so): "))
if (Hello == "yes"):
    if(no==1):
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif(no==2):
        print("[0    ]")
        print("[     ]")
        print("[    0]")
    elif(no==3):
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    elif(no==4):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif(no==5):
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    elif(no==6):
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
else:
    print("Please say YES if you want to roll the dice.")