from flask import Flask,request,render_template
import pickle


app=Flask(__name__)

model=pickle.load(open("model.pkl",'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_diabetes():
    Age=float(request.form.get("Age"))
    BloodPressure=float(request.form.get("BloodPressure"))
    Insulin=float(request.form.get("Insulin"))
    BMI=float(request.form.get("BMI"))
    Glucose=float(request.form.get("Glucose"))

    result=model.predict([[Age,BloodPressure,Insulin,BMI,Glucose]])

    if result[0]==1:
        return "<h1 style='color:green'>Person is Suffering from Diabetes Disease</h1>"
    else:
        return "<h1 style='color:red'>Person is not Suffering from Diabetes Disease</h1>"

app.run(debug=True)

########################################
####################################
##############################