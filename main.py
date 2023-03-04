from Regex.regex_main import regex_main
from t5base.questiongenerator import QuestionGenerator
from t5base.questiongenerator import print_qa
from spacy import load
import nltk

# load('en_core_web_md')
# nltk.download('averaged_perceptron_tagger')
def main():

    text = open('SubjectWise/datasets/EPP/chp1.txt','r', encoding='utf8').read()
    
    # Regex
    # regex_main(text)
    # T5
    qg = QuestionGenerator()
    qalist =qg.generate(text,use_evaluator=False, answer_style = 'sentences')
    print_qa(qalist)
if __name__ == "__main__":
    main()