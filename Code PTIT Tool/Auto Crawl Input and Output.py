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
                                          

                                    # AUTO EXECUTING C++ FILE

                                # Thanks for the helping of HlightT

TargetFile = "TEST.cpp"

if InitProcessCompleted:

    AUTO_SCRIPT_4 = f"\nExecuting {TargetFile} ...."

    print(colored(AUTO_SCRIPT_4, "green"), end = ' ')

    CMD_1 = "g++ -std=c++14 TEST.cpp -o TEST"

    CMD_2 = ".\TEST"

    os.system(CMD_1)

    os.system(CMD_2)

    print(colored(STATUS_SCRIPT_3, "green"))

else:

    print(colored(f"\nCan't execute {TargetFile} due to failed in INIT_FILE_PROCESS", "red"))


                                        # AUTO JUDGING C++ FILE

if InitProcessCompleted:

    OutputFile = open(
        "C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\output.txt", "r")

    JudgeFile = open(
        "C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\answer.txt", "r")

    OldOutputLines = OutputFile.readlines()

    OldJudgeLines = JudgeFile.readlines()

    # FORMATTING OUTPUT AND JUDGE FILE

    NewOutputLines = []

    for String in OldOutputLines:

        if String == '\n' or String == ' ':

            continue

        if String[len(String) - 1] == '\n': 
            
            newString = String[:-1]

            newString = ' '.join(newString.split())

            NewOutputLines.append(newString)

        else:   
            
            NewOutputLines.append(String)


    NewJudgeLines = []

    for String in OldJudgeLines:

        if String == '\n' or String == ' ':

            continue

        if String[len(String) - 1] == '\n': 
            
            newString = String[:-1]

            newString = ' '.join(newString.split())

            NewJudgeLines.append(newString)

        else:   
            
            NewJudgeLines.append(String)

        #  JUDGING


    def PassPretests() -> bool:

        global NewOutputLines

        global NewJudgeLines

        firstIter = int(0)

        secondIter = int(0)

        while firstIter < len(NewOutputLines) and secondIter < len(NewJudgeLines):

            if NewOutputLines[firstIter] != NewJudgeLines[secondIter]:

                return False

            firstIter += 1

            secondIter += 1

        if firstIter < len(NewOutputLines) or secondIter < len(NewJudgeLines):

            return False

        return True


    class WrongVerdictMessage:

        def MissingCharacters(Line, Position):

            print(colored(
                f"Missing character, line {Line}, position {Position}", "red"))

        def TooManyCharacters(Line, Position):

            print(colored(
                f"Too many characters, line {Line}, position {Position}", "red"))

        def WrongCharacter(Line, Position):

            print(colored(
                f"Expected {NewJudgeLines[Line-1][Position-1]}, but Found {NewOutputLines[Line-1][Position-1]} at line {Line}, position {Position}", "red"))

        def MissingLine(Line):

            print(colored(f"Missing line from line {Line}"))

        def TooManyLines(Line):

            print(colored(f"Too many lines from line {Line}"))

        def RunTimeError():

            print(colored("RTE", "red"))


    class NotPassPretests:

        global NewOutputLines

        global NewJudgeLines

        class WrongAnswerVerdict:

            def WrongInSubstring() -> WrongVerdictMessage:

                for i in range(len(NewOutputLines)):

                    if len(NewOutputLines[i]) != len(NewJudgeLines[i]):

                        if (len(NewJudgeLines[i]) > len(NewJudgeLines[i])):

                            return WrongVerdictMessage.TooManyCharacters(i + 1, len(NewJudgeLines) + 1)

                        return WrongVerdictMessage.MissingCharacters(i + 1, len(NewOutputLines) + 1)

                    else:

                        for j in range(len(NewJudgeLines[i])):

                            if NewOutputLines[i][j] != NewJudgeLines[i][j]:

                                return WrongVerdictMessage.WrongCharacter(i + 1, j + 1)

            def MissingLine() -> WrongVerdictMessage:

                return WrongVerdictMessage.MissingLine(len(NewOutputLines))

            def TooManyLines() -> WrongVerdictMessage:

                return WrongVerdictMessage.TooManyLines(len(NewJudgeLines))

        class RunTimeError:

            def RunTimeError() -> WrongVerdictMessage:

                return WrongVerdictMessage.RunTimeError()


    PassPretestsVerdict = False

    if PassPretests():

        PassPretestsVerdict = True

        print(colored("Passed Pretests!\n", "green", "on_green"))

    else:

        print(colored("\nWrong answer verdict: ", "red"), end = '')

        if len(NewOutputLines) == 0:
            NotPassPretests.RunTimeError.RunTimeError()

        elif len(NewOutputLines) == len(NewJudgeLines):
            NotPassPretests.WrongAnswerVerdict.WrongInSubstring()

        elif len(NewOutputLines) < len(NewJudgeLines):
            NotPassPretests.WrongAnswerVerdict.MissingLine()

        else:
            NotPassPretests.WrongAnswerVerdict.TooManyLines()

        print(colored("Output   : ", "yellow"), NewOutputLines, sep = '')

        print(colored("Expected : ", "yellow"), NewJudgeLines, sep = '')


                                    # AUTO SUBMIT WHEN PASSED PRETESTS

    AUTO_SCRIPT_5 = "Submitting to Code Ptit ..."

    if PassPretestsVerdict:

        File_dir = "C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\TEST.cpp"

        print(colored(AUTO_SCRIPT_5, "yellow"))

        UploadFile = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/form/div/div[2]/input")

        UploadFile.send_keys(File_dir)

        Submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/form/button")

        Submit_button.click()

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/span")))

        SubmitStatus = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/span")

        TimeExecuting = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]")

        MemoryUsage = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]")

        print("--------------------------------\nStatus |", "   Time    |", " Memory", sep = ' ')

        AUTO_SCRIPT_6 = f"  |  {TimeExecuting.text}   | {MemoryUsage.text}"
        
        if SubmitStatus.text == "CE":

            print(colored("CE  ", "red", "on_red"))

        elif SubmitStatus.text == "AC":

            print(colored("AC  ", "green", "on_green"), end = '')

            print(AUTO_SCRIPT_6)

        else:

            print(colored(f"{SubmitStatus.text}  ", "red", "on_red"), end = '')

            print(AUTO_SCRIPT_6)



    

