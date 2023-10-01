from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    name = "Irfan"
    age = "45"    
    data = {'name': name, 'age': age}
    return jsonify(data)

# @app.route("/about", methods=['GET', 'POST'])
# def about():
#     if request.method == "POST":
#         num1 = request.form['num1']
#         num2 = request.form['num2']
#         result = int(num1) + int(num2)
#         return render_template("about.html", result=result)
#     else:
#         return render_template("about.html", result="")
# print( __name__)
if __name__ == "__main__":
    app.run(debug=True)