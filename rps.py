name1 = input("What is your name? : ")
name2 = input("What is your name? : ")

print("Welcome to the game "+name1+" and "+name2)

chance1 = input(name1+ " Choose between rock, paper and scissors: ") 
chance2 = input(name2+ " Choose between rock, paper and scissors: ") 


if chance1 == chance2:
    print(name1+ " ties with " +name2)
if chance1 == "rock" and chance2== "paper":
    print(name2+ " wins!")
if chance1 == "paper" and chance2== "rock":
    print(name1+ " wins!")
if chance1 == "rock" and chance2== "scissors":
    print(name1+ " wins!")
if chance1 == "scissors" and chance2== "rock":
    print(name2+ " wins!")
if chance1 == "paper" and chance2== "scissors":
    print(name2+ " wins!")
if chance1 == "scissors" and chance2== "paper":
    print(name1+ " wins!")