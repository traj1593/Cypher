'''
Program: Cypher
Filename: cypher-tRaj-00.py
Author: Tushar Raj
Description: Encryption scheme where each letter in the alphabet is represented by a number
Revisions: No revisions made
'''
#There is no import statement
#There are no literal constraint
#There are no class defined

def inputdata(word): #checks the user input is correct or not
    '''
    This function accepts the input from the user and checks if the value contains any special character and numeric value
    Input: user input from the console which is string type
    output: returns strings data type
    '''
    count = 1
    special = "!@#$%^&*()+?_=,<>/"
    number = "1234567890"
    while(count):
        if (any( i in special for i in word)): #picks up each character from the word variable and then checks in special variable if it is present, if present run this if
            print("****Input cant have special character. Please Enter the valid entry****\n") #display the user that input contain special character
            progress = input("Please enter if you want to continue with Cypher Program(y/n): ") #ask user if he want to continue with the program again
            if( progress == 'y' or progress == 'Y' ): 
                word = input("\nEnter a word: ") #ask user to input the word again
            if( progress == 'n' or progress == 'N' ):
                exit() #exit the program if he enter no
        elif(any( i in number for i in word)): #checks if the entered user input is number
            print("****Please Enter the valid string which dosent contain numbers****\n")
            progress = input("Please enter if you want to continue with Cypher Program(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                word = input("\nEnter a word: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
        else:
            return word
        continue


### Step 1: Announce, prompt and get Response
print("Cypher:")
print("Program to encode a word\n")

# Main Program starts here
#Prompt user to get the word for encrypting and convert all letters into lowercase
value = input("Enter a word: ")
checked_value = inputdata(value) #calling function inputdata to check the data entered is correct or not
lower_checked_value = checked_value.lower() #lower method converts all letter of the object to lower case and and lowercase character remail untouched

###Step 2: Calculate the encoded value of  the word
y = "" #initializes a null string type variable which will be used for storing the encoded value
for i in lower_checked_value:
    x=str(ord(i)-ord('a')) # taking the integer value of the character picked by loop and subtracting 97(value of small 'a' to get the encoded value
    y=y+x+" " # adding the encoded value to the null string

###Step 3: Display the final result to the user
#print the encoded value to the user
print("The code for \"{0}\" is: {1}".format(checked_value,y))
#print that the Cypher program ended
print("\n****Cypher program ended****")
