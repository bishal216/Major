import main
from flask import Flask,render_template,request,redirect,url_for
import SubjectWise.generateQuestion as genSubwiseQue
import json
import io
# import pyPDF2
app = Flask(__name__)

app.jinja_env.globals.update(enumerate=enumerate)

# =====================exportPDF
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/generate_pdf')
def generate_pdf():
    # Render your HTML template here
    return render_template('template.html')
# ================================
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/genSubWise')
def SubWise():
    return render_template('SubWise.html')

@app.route('/genFromText',methods = ['GET','POST'])
def genText():
    return render_template('genText.html')

@app.route('/GeneratedQA',methods = ['GET','POST'])
def page4():
    qalist_str = request.args.get('qalist')
    qalist = json.loads(qalist_str)
    showAns = request.args.get('showAns')
    print(qalist)
    questions,answers = process_questions(qalist)
    return render_template('GeneratedQA.html', questions=questions,showAns=showAns,answers=answers)

@app.route('/generateText_pdf')
def generateText_pdf():
    # Render your HTML template here
    return render_template('pdfText.html')

@app.route('/submit', methods=['POST'])
def submit():
    nQues = request.form['nQues']
    qType = request.form['qType']
    showAns = request.form['showAns']
    Text = request.form['Text']
    print('submitted')
    qalist = main.generate_MCQ_question(Text,nQues,qType)
    qalist_str = json.dumps(qalist)
    return redirect(url_for('page4', qalist=qalist_str, showAns = showAns))

@app.route('/submitsubject', methods=['POST'])
def submitSubject():
    sName = request.form['dropdown']
    qalist = genSubwiseQue.generate(sName)
    qalist_str = json.dumps(qalist)
    return redirect(url_for('page5', qalist=qalist_str))

@app.route('/GeneratedQpaper',methods = ['GET','POST'])
def page5():
    qalist_str = request.args.get('qalist')
    qalist = json.loads(qalist_str)
    return render_template('GeneratedQPaper.html', qalist = qalist)

def process_questions(questions):
    question_list = []
    answer_list = []

    for q in questions:
        if q['questiontype'] == 0:
            question = q['question']
            options = [v for k, v in q['answers'].items()]
            answer = q['isCorrect']
            question_list.append({'question': question, 'options': options})
            answer_list.append(answer)
        elif q['questiontype'] == 1:
            question = q['question']
            question_list.append({'question': question})
            answer = q['answers']
            answer_list.append(answer)

    return question_list, answer_list

# @app.route('/generate-pdf')
# def generate_pdf():
#     # Get data to insert into PDF from your database or other source
#     questions = [{'question': 'What is your name?', 'options': ['Alice', 'Bob', 'Charlie']}, {'question': 'What is your age?', 'options': ['18-24', '25-34', '35+']}]
#     answers = ['Alice', '25-34']

#     # Create a new PDF file in memory
#     pdf_buffer = io.BytesIO()
#     pdf_writer = PyPDF2.PdfFileWriter()

#     # Create a new page in the PDF
#     pdf_page = PyPDF2.pdf.PageObject.createBlankPage(None, 400, 400)

#     # Insert text into the PDF page
#     pdf_page.drawText(50, 350, "Survey Results")

#     # Insert questions and answers into the PDF page
#     y = 300
#     for q in questions:
#         pdf_page.drawText(50, y, q['question'])
#         y -= 20
#         if q.get('options'):
#             for option in q['options']:
#                 pdf_page.drawText(70, y, option)
#                 y -= 20
#         y -= 10
#     pdf_page.drawText(50, y, "Answers:")
#     y -= 20
#     for a in answers:
#         pdf_page.drawText(70, y, a)
#         y -= 20

#     # Add the PDF page to the PDF file
#     pdf_writer.addPage(pdf_page)

#     # Write the PDF file to the in-memory buffer
#     pdf_writer.write(pdf_buffer)

#     # Create a response object with the PDF file contents
#     response = make_response(pdf_buffer.getvalue())
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=survey_results.pdf'
#     return response



if __name__ == '__main__':
    app.run(debug=True)
