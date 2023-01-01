from flask import Flask,render_template,request
import joblib
from helpers.dummies1_py import *

app=Flask(__name__)

model=joblib.load('models/model.h5')
scaler=joblib.load('models/scaler.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    ApplicantIncome=float(request.form['ApplicantIncome'])
    CoapplicantIncome=float(request.form['CoapplicantIncome'])
    LoanAmount=float(request.form['LoanAmount'])
    Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
    Credit_History=request.form['credit_history']
    Gender=request.form['gender']


    data=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term]+credit_history[Credit_History]+gender[Gender]
    final_data=scaler.transform([data])
    pred=model.predict(final_data)[0]

    return render_template('prediction.html',credit=pred)

if __name__=='__main__':
    app.run()