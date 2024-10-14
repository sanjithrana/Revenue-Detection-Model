
import pickle
from flask import Flask,request,render_template,url_for


app = Flask(__name__,template_folder='templets')
model_lr = pickle.load(open('modell.pkl','rb'))

@app.route('/',methods = ['GET']) #url
def index():
    return render_template('index.html')

   

@app.route('/predict',methods =['GET','POST'])
def predict():
    prediction = model_lr.predict(request.form.get('Temperature'))
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text = f'Total Revenu is Genarated is Rs : {output}/-')


if __name__  == '__main__':
    app.run(debug=True)

