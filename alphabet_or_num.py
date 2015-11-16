def main():
    character = str(input("Enter a character:"))
    if(character.isalpha() == True):
        print("The character is an alphabet")
    elif(character.isalnum() == True):
        print("The character is a number")
    else:
        print("It's not an alphabet and a number")

if __name__ == '__main__':
    main()
