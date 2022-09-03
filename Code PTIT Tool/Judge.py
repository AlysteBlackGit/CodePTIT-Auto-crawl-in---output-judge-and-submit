from termcolor import colored                                                    

OutputFile = open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\output.txt", "r")

JudgeFile = open("C:\\Users\\Admin\\Downloads\\VS Code Projects\\C++ Projects (VSC)\\answer.txt", "r")

OldOutputLines = OutputFile.readlines()

OldJudgeLines = JudgeFile.readlines()


                                            # FORMATTING OUTPUT AND JUDGE FILE
NewOutputLines = []

for String in OldOutputLines:

    if String == '\n':

        continue

    newString = String[:-1]

    NewOutputLines.append(newString)


NewJudgeLines = []

for String in OldJudgeLines:

    if String == '\n':

        continue

    newString = String[:-1]

    NewJudgeLines.append(newString)



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

        print(colored(f"Missing character, line {Line}, position {Position}", "red", "on_red"))

    def TooManyCharacters(Line, Position):

        print(colored(f"Too many characters, line {Line}, position {Position}", "red", "on_red"))

    def WrongCharacter(Line, Position):

        print(colored(f"Expected {NewJudgeLines[Line-1][Position-1]}, but Found {NewOutputLines[Line-1][Position-1]} at line {Line}, position {Position}", "red", "on_red"))

    def MissingLine(Line):

        print(colored(f"Missing line from line {Line}", "red", "on_red"))

    def TooManyLines(Line):

        print(colored(f"Too many lines from line {Line}", "red", "on_red"))

    def RunTimeError():

        print(colored("RTE", "red", "on_red"))

class NotPassPretests:

    global NewOutputLines

    global NewJudgeLines

    class WrongAnswerVerdict:

        def WrongInSubstring() -> WrongVerdictMessage:

            for i in range(len(NewOutputLines)):

                if len(NewOutputLines[i]) != len(NewJudgeLines[i]):

                    if (len(NewJudgeLines[i]) > len(NewJudgeLines[i])):  return WrongVerdictMessage.TooManyCharacters(i + 1, len(NewJudgeLines) + 1)

                    return WrongVerdictMessage.MissingCharacters(i + 1, len(NewOutputLines) + 1)
                
                else:

                    for j in range(len(NewJudgeLines[i])):

                        if NewOutputLines[i][j] != NewJudgeLines[i][j]:  return WrongVerdictMessage.WrongCharacter(i + 1, j + 1)
                

        def MissingLine() -> WrongVerdictMessage:

            return WrongVerdictMessage.MissingLine(len(NewOutputLines))

        def TooManyLines() -> WrongVerdictMessage:

            return WrongVerdictMessage.TooManyLines(len(NewJudgeLines))

    
    class RunTimeError:

        def RunTimeError() -> WrongVerdictMessage:

            return WrongVerdictMessage.RunTimeError()


if PassPretests():

    print(colored("Passed Pretests!", "green", "on_green"))

else:

    if len(NewOutputLines) == 0:   NotPassPretests.RunTimeError.RunTimeError()

    elif len(NewOutputLines) == len(NewJudgeLines):   NotPassPretests.WrongAnswerVerdict.WrongInSubstring()

    elif len(NewOutputLines) < len(NewJudgeLines):  NotPassPretests.WrongAnswerVerdict.MissingLine()

    else:  NotPassPretests.WrongAnswerVerdict.TooManyLines()
