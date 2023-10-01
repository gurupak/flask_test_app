from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    name = input('User please tell me your name')
    
    return render_template("home.html",name=name)

@app.route("/about", methods=['GET', 'POST'])
def about():
    if request.method == "POST":
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = int(num1) + int(num2)
        return render_template("about.html", result=result)
    else:
        return render_template("about.html", result="")
# print( __name__)
if __name__ == "__main__":
    app.run(debug=True)