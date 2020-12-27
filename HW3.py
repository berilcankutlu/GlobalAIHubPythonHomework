Name = input("Please enter your name: ")
print("Welcome {}".format(Name))

word = ['c','a','t']
counter = 10
while counter!=0:
        letter = input("Enter a letter: ")

        if letter in word:
            print("You found one letter!")
        else:
            counter= counter - 1




if counter==0:
    print("You have been defeated! Muhahahaah")
else:
    print("Congratulations! You won!!")
