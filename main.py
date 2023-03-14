from Regex.regex_main import regex_main
from t5base.questiongenerator import QuestionGenerator
from t5base.questiongenerator import print_qa
from spacy import load
import nltk

qg = QuestionGenerator()
def generate_MCQ_question(text,numOfQues=10,ansstyle = 'all'):
    qalist =qg.generate(text,use_evaluator=True, answer_style = ansstyle,num_questions = int(numOfQues))
    return qalist
def main():

    text = open('sampleText/owl_rescue.txt','r', encoding='utf8').read()
   
        # Regex
    # regex_main(text)
    # T5
    qg = QuestionGenerator()
    qalist =qg.generate(text,use_evaluator=True, answer_style = 'sentences')
    print_qa(qalist)
if __name__ == "__main__":
    main()