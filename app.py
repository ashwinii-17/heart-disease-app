from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    male = float(request.form["male"])
    chol = float(request.form["chol"])
    sysbp = float(request.form["sysbp"])
    diabp = float(request.form["diabp"])
    bmi = float(request.form["bmi"])
    heartrate = float(request.form["heartrate"])
    glucose = float(request.form["glucose"])

    risk_score = 0

    # simple rules
    if age > 50:
        risk_score += 1
    if chol > 240:
        risk_score += 1
    if sysbp > 140:
        risk_score += 1
    if bmi > 30:
        risk_score += 1
    if glucose > 120:
        risk_score += 1

    if risk_score >= 3:
        result = "⚠ High Risk of Heart Disease"
        result_class = "result-negative"
    else:
        result = "✅ Low Risk of Heart Disease"
        result_class = "result-positive"

    return render_template(
        "index.html",
        prediction_text=result,
        result_class=result_class
    )

if __name__ == "__main__":
    app.run(debug=True)