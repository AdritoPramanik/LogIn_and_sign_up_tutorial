import pyrebase

config = {
    "apiKey": "AIzaSyAGmblQoLUVCxHZo1RlTQXX6W41Gxb0q_Y",
    "authDomain": "authentication-5e6f6.firebaseapp.com",
    "databaseURL": "https://authentication-5e6f6-default-rtdb.firebaseio.com",
    "projectId": "authentication-5e6f6",
    "storageBucket": "authentication-5e6f6.appspot.com",
    "messagingSenderId": "850142725039",
    "appId": "1:850142725039:web:5fcfa6fd5bb5f4dbb8655a"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def logIn():
    email = input("Enter your email address : ")
    password = input("Enter Your password : ")
    try:
        log_in = auth.sign_in_with_email_and_password(email, password)
        print("Successfully signed In")
    except:
        print("Invalid email or password")

def signUp():
    choice = input("Are you a new user?[y/n]")
    if choice == "n":
        logIn()
    elif choice == "y":
        email = input("Enter your email address : ")
        password = input("Enter Your password : ")
        try:
            Sign_up = auth.create_user_with_email_and_password(email, password)
            print("Successfully signed Up")
            ask()
        except:
            print("Email exists")
    else:
        print("Please answer in y or n")

def ask():
    ask1 = input("Do you want to login now? [y/n]")
    if ask1 == "y":
        logIn()
    elif ask1 == "n":
        print("Ok sir/mam")
    
    else:
        print("Please answer in y/n")

signUp()








        
       
    





