import random
import time

def current_time():
    """ function to return current time """
    ctime = time.asctime(time.localtime(time.time()))
    return ctime

def password_gen(max_len):
    """ funtiuon to generate paswords """
    digits = ['1','2','3','4','5','6','7','8','9','0']
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
             's','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
             'S','T','U','V','W','X','Y','Z']
    special = ['~','!','@','#','$','%','^','&','*','(',')','=','+','-','_']
    password = ""
    type = int(input("Enter the type of password you want :\n (1) - Alphabetical\n (2) - Numerical\n (3) - Alphanumeric \n (4) - All combined with special character \n --"))
    
    if type == 1:
        alpha = lower + upper
        for i in range(max_len):
            password += random.choice(alpha)
        print(password)
        log(password)
        
    elif type == 2:
        for i in range(max_len):
            password += random.choice(digits)
        print(password)
        log(password)
        
    elif type == 3:
        alphanumeric = upper + lower + digits
        for i in range(max_len):
            password += random.choice(alphanumeric)
        print(password)
        log(password)
        
    elif type == 4:
        combined = digits + lower + upper + special
        for i in range(max_len):
            password += random.choice(combined)
        print(password)
        log(password)
        
def log(password):
    """ Function to store the generated passwords """
    website = input("For which website did you generated the password : ")
    with open ("log.txt" , "a") as f:
        f.write = (f"{ctime} : {website} -- {password}")
        
def view():
    """ Function to view saved passwords. """
    with open ("log.txt" , "r") as f:
        print(f.read())
        
if __name__ == '__main__':
    ctime = current_time()
    print("~~~~ Password Generator ~~~~")
    choice = int(input("Enter (1) to generate a password , enter (2) to view saved passwords : "))
    if choice == 1:
        max_len = int(input("Enter the length of password you want: "))
        password_gen(max_len)
    elif choice == 2:
        view()
    else:
        choice = int(input("Please enter valid choice : "))
    
    
