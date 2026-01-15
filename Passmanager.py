import hashlib
import getpass

passwod_manager={}

def create_account():
  username=input("enter your username")
  password = getpass.getpass("enter your desired password")
  hashed_password=hashlib.sha256(password.encode().hexdigest())
  password_manager[username]=hashed_password
print("account created sucessfully!")

def log_in():
  username=input("enter your username")
  password = getpass.getpass("enter your desired password")
  hashed_password=hashlib.sha256(password.encode().hexdigest())
  if username in password_manager.keys() and password_manager[username]==hashed_password:
    print("Login successful")
  else:
    print("invalid username or password")

def main():
  while True:
    choice=input("enter 1 to create account,2 to login or 0 to exit:")
    if choice==1:
      create_account()
    elif choice==2:
      log_in()
    elif choice==3:
      break
    else:
      print("invalid choice")

