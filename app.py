import main
from flask import Flask,render_template,request
import SubjectWise.generateQuestion as genSubwiseQue


app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    qg =[]
    if request.method == 'POST':
        nQues = request.form['nQues']
        qType = request.form['qType']
        showAns = request.form['showAns']
        Text = request.form['Text']
        qg =[1,2,3]
        qg = main.generate_MCQ_question(Text,nQues,qType)
        message = "True"
        print('submitted')
    return render_template('homepage.html', qg=qg)

@app.route('/other')
def other():
    questions = genSubwiseQue.generate('OnM')
    return render_template('homeQAsked.html',questions = questions)


@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

