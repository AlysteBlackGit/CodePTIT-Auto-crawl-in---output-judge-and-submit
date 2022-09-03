from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.color import Color

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import StaleElementReferenceException

from selenium.common.exceptions import TimeoutException  

from termcolor import colored

import datetime

import time

import os


                    # AUTO CRAWL INPUT, OUTPUT IN CORRECT FORM - EXECUTING - JUDGING - SUBMIT BOT
                                    

                                            # LOG IN CODE.PTIT.EDU.VN

AUTO_SCRIPT_1 = "Crawling Data ......\n"

Path = input()

NewOptions = Options()

NewOptions.add_argument("--headless")

NewOptions.add_argument("--user-data-dir=C:\\Users\\Admin\\Downloads\\VS Code Projects\\Python Projects (VSC)\\UserData2")

driver = webdriver.Chrome(executable_path = "C:\\Program Files (x86)\\Chrome Driver\\chromedriver.exe", chrome_options = NewOptions)

driver.get(Path)

print(colored(AUTO_SCRIPT_1, "white", "on_yellow"))

                                   
                                    # CRAWL IN - OUTPUT, INIT IN - OUTPUT IN CORRECT FORM



AUTO_SCRIPT_2 = "Init Input data to INIT_INPUT_FILE"

AUTO_SCRIPT_3 = "Init Output data to INIT_ANSWER_FILE"

STATUS_SCRIPT_1 = "Successfull"

STATUS_SCRIPT_2 = "Failed"

STATUS_SCRIPT_3 = "Completed"

Input = driver.find_elements(By.TAG_NAME, "td")

InitProcessCompleted = True

with open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\init_input.txt", "w") as Init_inputFile:
   
    print(colored(AUTO_SCRIPT_2, "yellow"))

    if len(Input) > 1:

        Init_inputFile.write(Input[2].text)
    
        print(colored(STATUS_SCRIPT_1, "green", "on_green"))

    else:
  
        InitProcessCompleted = False

        print(colored(STATUS_SCRIPT_2, "white", "on_red"))

with open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\init_answer.txt", "w") as Init_answerFile:

    print(colored(AUTO_SCRIPT_3, "yellow"))

    if len(Input) > 2:

        Init_answerFile.write(Input[3].text)

        print(colored(STATUS_SCRIPT_1, "green", "on_green"))

    else:

        InitProcessCompleted = False

        print(colored(STATUS_SCRIPT_2, "white", "on_red"))

Init_inputData = []

Init_answerData = []

Init_inputFile = open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\init_input.txt", "r")

Init_answerFile = open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\init_answer.txt", "r")



inpStr = Init_inputFile.readlines()

Init_inputData.append(inpStr)


ansStr = Init_answerFile.readlines()

Init_answerData.append(ansStr)


with open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\input.txt", "w") as InputFile:

    for items in Init_inputData[0]:

        if items == '\n':

            continue

        else:

            line = items

            line = ' '.join(line.split())

            InputFile.write(f"{line}\n")

with open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\answer.txt", "w") as AnswerFile:

    for items in Init_answerData[0]:

        if items == '\n':

            continue

        else:

            line = items

            line = ' '.join(line.split())

            AnswerFile.write(f"{line}\n")


Init_inputFile.close()

Init_answerFile.close()
                                          

    

