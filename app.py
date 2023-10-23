from flask import Flask, render_template, request
import pandas as pd
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

app = Flask(__name__)

def load_qa_data(csv_file):
    return pd.read_csv(r"C:\Users\aksha\OneDrive\Documents\QnA System Akshay\frontend\mwoz_data_qna.csv")

def find_answer(question, qa_df):
    question = question.lower()
    matched_row = qa_df[qa_df['question'].apply(lambda x: x.lower()) == question]
    if len(matched_row) > 0:
        return matched_row.iloc[0]['answer']
    else:
        return "Answer not found for the given question."

@app.route('/', methods=['GET', 'POST'])
def index():
    qa_df = load_qa_data('mwoz_data_qna.csv')

    if request.method == 'POST':
        user_question = request.form['question']
        answer = find_answer(user_question, qa_df)
    else:
        user_question = ""
        answer = ""

    return render_template('index.html', user_question=user_question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
