from random import randint
num = randint(1,100)
guess = 100
guess_done = 0
while guess>0:
    n = int(input("Guess the number:"))
    if(num == n):
	print("Congrats %d" %(score))
	break
    guess_done += 1
    guess -= 1 
    if (n>=1 and n<25):
        print("Your guess is too low")
    elif (n>=25 and n<50):
	print("Your guess is low")
    elif (n>=50 and n<75):
	print("Your guess is high")
    elif (n>=75 and n<100):
	print("Your guess is too high")
else:
    print("No more atrempts left. Have a nice day!!!!!!!!")
score = 100-guess_done
print("Your score is: %d" %(score))
if (score>=75 and score<100):
    print("Cool!!!")
elif(score>=50 and score<75):
    print("Keep trying")
else:
    print("Better luck next time!!")
