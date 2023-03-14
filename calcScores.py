import nltk
import json
from nltk.translate.bleu_score import sentence_bleu
from t5base.questiongenerator import QuestionGenerator

          
def QAGen(fileDir):
    fin = codecs.open(fileDir, 'r', encoding='ansi')
    text = fin.read()  
    qg = QuestionGenerator()
    qalist =qg.generate(text,use_evaluator=True, answer_style = 'MCQ')
    q =  [d['question'] for d in qalist]
    return q
def RefQ(fileDir):  
    with open(fileDir, 'r') as f:
        data = json.load(f)
    q =  [d['question'] for d in data]
    return q
           
def BLEU(textFileDir,refQFileDir):
    n=0
    totalBLEU = 0
    generated_questions = QAGen(textFileDir)
    reference_questions = RefQ(refQFileDir)
    for i in range(len(generated_questions)):
        gen_tokens = generated_questions[i].split()
        ref_tokens = [ref[i].split() for ref in reference_questions]
        bleu_score = sentence_bleu(ref_tokens, gen_tokens, weights=(0.25, 0.25, 0.25, 0.25))
        n = n+1
        totalBLEU = totalBLEU + bleu_score
    return totalBLEU/n

BLEU('SubjectWise/datasets/Software/Chapter 1.txt','SubjectWise/datasets/SE/Chapter1.txt')