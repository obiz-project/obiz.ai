import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Ansi Colors // change the colors displayed on the terminal

| Color                                  | Font code        | Background code  |
|----------------------------------------|------------------|------------------|
| Black                                  | \x1B[30m         | \x1B[40m         |
| Red                                    | \x1B[31m         | \x1B[41m         |
| Green                                  | \x1B[32m         | \x1B[42m         |
| Yellow                                 | \x1B[33m         | \x1B[43m         |
| Blue                                   | \x1B[34m         | \x1B[44m         |
| Magenta                                | \x1B[35m         | \x1B[45m         |
| Cyan                                   | \x1B[36m         | \x1B[46m         |
| White                                  | \x1B[37m         | \x1B[47m         |
| Any palette color (with V in [0-255])  | \x1B[38;5;Vm     | \x1B[48;5;Vm     |
| Any RGB color (with values in [0-255]) | \x1B[38;2;R;G;Bm | \x1B[48;2;R;G;Bm |
'''
# color definitions
black =  "\x1B[30m"
red = "\x1B[31m"
green = "\x1B[32m"
yellow = "\x1B[33m"
blue = "\x1B[34m"
magenta = "\x1B[35m"
cyan = "\x1B[36m"
white = "\x1B[37m"
# colors end

done = False

def loading(): # loading animation
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(1,5):
        time.sleep(0.1)
        print(green,'loading |')
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(white,'loading /')
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(green,'loading -')
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(white,'loading \\')
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')


def require_input(): #input management
   print(magenta)
   user_input = input("What can I do for you?: ")
   user_input = user_input.lower()
   print(white)
   print("#"*80)
   print("\n")
   print(magenta)
   print("User: ",user_input)
   response(user_input)


def start_page(): #initial start page
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#"*80)
    print(green,'Obiz.ai Alpha v1.0.2 ', yellow,'|', blue,' Terminal Based', white)
    for i in range(1,3):
        print("\n")
    print("#"*80)
    require_input()


def response(user_input): #response handling
    if user_input == "":
        print("Error: no valid input")
    else:
        if "hello" or "hi" or "howdy" or "hi" in user_input:
            for i in range(1,2):
              print("\n")
            print(green)
            with open('/Users/student/Documents/GitHub/obiz.ai/aiv2/greetings.txt', 'r') as file: #change this to your specified path
              responses_ai = file.readlines()
              response_ai = random.choice(responses_ai)
            print(response_ai +', how can I help you')
            print(white)
            for i in range(1,2):
              print("\n")
        if "search" in user_input:
            for i in range(1,2):
                print("\n")
            print(green)
            new_user_input = user_input.replace("search","")
            print("searching the web for ", new_user_input)
            for i in range(1,2):
                print("\n")
            driver = webdriver.Chrome()
            driver.get("https://www.google.com")
            search_box = driver.find_element("q")
            search_box.send_keys(new_user_input)
            search_box.submit()
        if "compass" in user_input:
            for i in range(1,2):
                print("\n")
            print(green)
            new_user_input = user_input.replace("search","")
            print("Opening Compass")
            for i in range(1,2):
                print("\n")
            driver = webdriver.Chrome()
            driver.get("https://compass.education")
            driver.maximize_window()
            time.sleep(20)
            driver.close()
            print("execution successful")
             
    

def get_message():
    pass

if __name__ == "__main__":
    start_page()