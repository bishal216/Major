from t5base.questiongenerator import QuestionGenerator
from t5base.questiongenerator import print_qa
import codecs
import json
def main():
    # subjects = [('EES',5),('EPP',6),('OnM',4)]
    # for subject in subjects:
        # for i in range(1,subject[1]+1,1):
            # fileDir = 'SubjectWise/datasets/'+subject[0]+'/chapter'+str(i)+'.txt'
            fileDir = 'SubjectWise/datasets/Software/Chapter 10.txt'
            opFileDir = 'SubjectWise/questions/SE/Chapter10.txt'
            fin = codecs.open(fileDir, 'r', encoding='ansi')
            # opFileDir = 'SubjectWise/questions/'+subject[0]+'/chapter'+str(i)+'.txt'
            text = fin.read()
            qg = QuestionGenerator()
            qalist =qg.generate(text,use_evaluator=False, answer_style = 'sentences')
            fout= open(opFileDir,"w+")
            for qa in qalist:
        # write each item on a new line
                fout.write(json.dumps(qa))
            fout.close() 
if __name__ == "__main__":
    main()