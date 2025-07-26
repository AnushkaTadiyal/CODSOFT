import random
import string

print("---------THIS IS  AN AUTO PASSWORD GENERATOR---------")

length=int(input("Enter the desired length of the password: ")) 
if (length<5):
    print("Password must be more than 5 characters.")
    exit()
else:
    include_upper=input("Include uppercase(A,B,...) letters (y/n):").lower()
    include_lower=input("Include lowercase letters(a,b,...) (y/n):").lower()
    include_digits=input("Include digits(1,2,....) (y/n):").lower()
    include_symbols=input("Include symbols(~,!,@,....) (y/n):").lower()
      
password=""
characters=""
if include_upper=="y":
    characters+=string.ascii_uppercase
    password+=random.choice(string.ascii_uppercase)   
if include_lower=="y":
    characters+=string.ascii_lowercase
    password+=random.choice(string.ascii_lowercase)
if include_digits=="y":
    characters+=string.digits
    password+=random.choice(string.digits)
if include_symbols=="y":
    characters+=string.punctuation
    password+=random.choice(string.punctuation)

if characters == "":
        print("You must select at least one character type.")
else:
    while len(password) < length:
        password += random.choice(characters)
        
print("\nYour generated password is:", password)
        
        
def save_to_file(password):
    with open("generated_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to 'generated_passwords.txt'.")

save = input("Do you want to save the password to a file? (y/n): ").lower()
if save == 'y':
    save_to_file(password)
    
    
print("!!THANK YOU!!")