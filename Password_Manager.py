import string
import random
import os

class Password:
    def __init__(self,websiteName,userName,password,key):
        self.websiteName = websiteName
        self.userName = userName
        self.password = encrypted(password, key)
        self.key = key

def encrypted(password, key):
        encrypted_password = ""
        for i in range(len(password)):
            newKey = ord(password[i]) + key
            encrypted_password = encrypted_password + chr(newKey)
        return encrypted_password

def decrypted(password, key):
    decrypted_password = ""
    for i in range(len(password)):
        newKey = ord(password[i]) - key
        decrypted_password = decrypted_password + chr(newKey)
    return decrypted_password

def password_strength(password):
    strength = 0

    if len(password) < 8:
        return "Password should be at least 8 characters long."
    else:
        strength += 1
    for char in password:
        if char.isupper():
            strength += 1
            break
    for char in password:
        if char.islower():
            strength += 1
            break   
    for char in password:
        if char.isdigit():
            strength += 1
            break
    for char in password:
        if char in string.punctuation:
            strength += 1
            break
    if strength == 2:
        return "Password is weak. \nPassword should contain at least one uppercase letter, one lowercase letter, one digit and one special character."
    elif strength <= 3:
        return "Password is moderate."
    elif strength <= 6:
        return "Password is strong."

def password_generator(length):

    if(length<8):
        print("Password length should be at least 8 characters")
    else:
        allCombination = string.ascii_letters + string.digits + string.punctuation
        password = ""
        for a in range(length):
            password = password + random.choice(allCombination)
        print("Generated Password: " + password)

listOfPasswords = []

while True:
    print("Enter Your Choice")
    print(" ")
    print("1. Add a password")
    print(" ")
    print("2. Update a password")
    print(" ")
    print("3. Delete a password")
    print(" ")
    print("4. Find a password")
    print(" ")
    print("5. Show saved list")
    print(" ")
    print("6. Password Strength Test")
    print(" ")
    print("7. Generate a password")
    print(" ")
    print("8. Export all passwords as a text file")
    print(" ")

    print("0. Exit the Program")
    print(" ")

    choice = int(input())

    if choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Add a password")
        print(" ")

        print("Enter Website Name: ")
        websiteName = input()
        print(" ")
        
        print("Enter Username: ")
        userName = input()
        print(" ")

        print("Enter password: ")
        password = input()
        print(" ")

        print("Enter key: ")
        key = int(input())
        print(" ")

        password = Password(websiteName,userName,password,key)

        listOfPasswords.append(password)

        print("Password Added")
        print(" ")
        print("---------------------------------")

    elif choice == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Update a password")
        print(" ")
        print("Enter the website name: ")
        websiteName = input()
        print("Enter the username: ")
        userName = input()

        found = False

        for passwordObject in listOfPasswords:
            if passwordObject.websiteName == websiteName and passwordObject.userName == userName:

                found = True
                if found:
                    print("Information Found")
                      
                print("Enter the new Password")
                newPassword = input()
                print("Enter the new Key")
                newKey = int(input())
                
                passwordObject.password = encrypted(newPassword, newKey)
                passwordObject.key = newKey
                print("Password Updated")
                print("---------------------------------")
                break

        if not found:
            print("Website name or username not found in the list")   
            print("---------------------------------")

    elif choice == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Delete a password")
        print(" ")

        print("Enter the website name: ")
        websiteName = input()

        print("Enter the username: ")
        userName = input()

        found = False
        for passwordObject in listOfPasswords:
            if passwordObject.websiteName == websiteName and passwordObject.userName == userName:
                listOfPasswords.remove(passwordObject)
                found = True
                print("Password Deleted")
                print("---------------------------------")
                break

        if not found:
            print("Website name or username not found in the list")
            print("---------------------------------")
        
    elif choice == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Find a password")
        print(" ")
        print("Enter the website name: ")
        websiteName = input()
        print("Enter the username: ")
        userName = input()
        print(" ")

        found = False
        for passwordObject in listOfPasswords:
            if passwordObject.websiteName == websiteName and passwordObject.userName == userName:
                print("Password Found.\nEnter key to decrypt the password: ")
                key = int(input())
                if key != passwordObject.key:
                    print("Invalid Key")
                    print("---------------------------------")
                    found = True
                    break
                print("Your Password is: ",decrypted(passwordObject.password, key))
                print("---------------------------------")
                found = True
                break

        if not found:
            print("Website name not found in the list")
            print("---------------------------------")
    
    elif choice == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Showing saved list")
        print(" ")
        if len(listOfPasswords) == 0:
            print("No passwords saved")
            print("---------------------------------")
        else:
            print("---------------------------------")
            for passwordObject in listOfPasswords:
                print("Website Name: ",passwordObject.websiteName)
                print("Username: ",passwordObject.userName)
                print("---------------------------------")
            print("")

    elif choice == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Password Strength Test")
        print(" ")
        print("Enter the password to test its strength: ")
        password = input()
        print(" ")
        print(password_strength(password))
        print(" ")
        print("---------------------------------")

    elif choice == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Generate a password")
        print(" ")
        print("Enter the length of the password: ")
        length = int(input())
        print(" ")
        password_generator(length)
        print(" ")
        print("---------------------------------")        

    elif choice == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exporting passwords to a text file")
            print(" ")

            with open("passwords.txt", "w") as file:
                for passwordObject in listOfPasswords:
                    file.write("Website Name: " + passwordObject.websiteName + "\n")
                    file.write("Username: " + passwordObject.userName + "\n")
                    file.write("Password: " + decrypted(passwordObject.password, passwordObject.key) + "\n")
                    file.write("---------------------------------\n")

            print("Passwords exported to passwords.txt")
            print("---------------------------------")

    elif choice == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program.\nExiting the Program...")
        break

    else:
        print("Invalid choice")

    