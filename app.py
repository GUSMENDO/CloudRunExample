from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home', methods =["POST","GET"])
def home():
    return render_template('index.html')

@app.route('/webhook', methods =["POST","GET"])
def webhook():
    data = request.get_json()
    
    edad = data.get("Edad")
    edad = edad * 100
    data["Edad"] = edad
    
    return data

if __name__ == '__main__':
    app.run(debug=True)
