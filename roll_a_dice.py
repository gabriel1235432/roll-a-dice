import random 

resposta=input("Voce quer jogar os dados novamente?")

while resposta=='y':
    no=random.randint(1, 6)
    print(no)

    if no == 1:
  
     print("[-----]")
     print("[     ]")
     print("[  0  ]")
     print("[     ]")
     print("[-----]")

     print("[-----]")
     print("[ 0   ]")
     print("[     ]")
     print("[   0 ]")
     print("[-----]")

     print("[-----]")
     print("[     ]")
     print("[0 0 0]")
     print("[     ]")
     print("[-----]")

     print("[-----]")
     print("[0   0]")
     print("[     ]")
     print("[0   0]")
     print("[-----]")

    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")

    print("[-----]")
    print("[0   0]")
    print("[0   0]")
    print("[0   0]")
    print("[-----]")
    
    break