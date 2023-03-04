import Regex.aqgFunction

# Main Function
def regex_main(inputText):
    # Create AQG object
    aqg = Regex.aqgFunction.AutomaticQuestionGenerator()

    # inputTextPath = "pathHere"
    # readFile = open(inputTextPath, 'r+', encoding="utf8")
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')


    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)

    # aqg.DisNormal(questionList)

    return 0

