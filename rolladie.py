import random

choice=input("Do you want to roll a die? (y/n)")

while(choice == "y"):
    num=random.randint(1,6)
    if num==1:
        print("[---------]")
        print("[---------]")
        print("[----0----]")
        print("[---------]")
        print("[---------]")
    elif num==2:
        print("[---------]")
        print("[------0--]")        
        print("[---------]")
        print("[--0------]")
        print("[---------]")
    elif num==3:
        print("[---------]")
        print("[------0--]")
        print("[----0----]")
        print("[--0------]")
        print("[---------]")
    elif num==4:
        print("[---------]")
        print("[--0---0--]")
        print("[---------]")
        print("[--0---0--]")
        print("[---------]")
    elif num==5:
        print("[---------]")
        print("[--0---0--]")
        print("[----0----]")
        print("[--0---0--]")
        print("[---------]")
    else:
        print("[---------]")
        print("[--0---0--]")
        print("[--0---0--]")
        print("[--0---0--]")
        print("[---------]")
    choice=input("Do you want to roll a die again? (y/n)")


print("Rerun to roll a die")

   

