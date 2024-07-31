# from flask import Flask,render_template,request

# app = Flask(__name__)

# # print("the one ",app)


# @app.route("/")
# def hello_world():
#     return render_template("index.html")

# if __name__ == "__main__":
#      app.run(port=5001)

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/",methods=["POST"])
def cal():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["number1"])
            num2 = float(request.form["number2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        except ValueError:
            result = "Error: Invalid input"

    return render_template("index.html", result=result)
        

if __name__ == '__main__':
    app.run(debug=True,port=5000)
