from flask import Flask,render_template,request
from args import *
import pickle
import numpy  as np
with open("Model.pkl",'rb') as mod:
    model=pickle.load(mod)
with open("Scaler.pkl",'rb') as mod:
    scaler=pickle.load(mod)

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    # print(request.method)
    # print(request.form)
    if(request.method=='POST'):
        bedrooms= request.form['bedrooms']
        bathrooms= request.form['bathrooms']
        SqFt= request.form['SqFt']
        location= request.form['location_mapping']
        direction= request.form['direction_mapping']
        property_type= request.form['property_type_mapping']
        status= request.form['status_mapping']

        data=np.array([[bedrooms,bathrooms,SqFt,location,direction,property_type,status]])
        trans_data=scaler.transform(data)
        return str(model.predict(trans_data)[0])
    else:
        return render_template('index.html',location_mapping=location_mapping,direction_mapping=direction_mapping,
                              property_type_mapping=property_type_mapping,status_mapping=status_mapping)
    
@app.route('/second')
def second_page():
    return 'I am in second page'
@app.route('/second')
def third_page():
    return 'I am in third page'

app.run(use_reloader = True,debug=True)