from flask import Flask, jsonify, render_template, request, url_for
import config
from utils import SelPrice



app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('welcome to Used Car Price prediction')
    return render_template('index.html')


@app.route("/predict_price",methods=["GET","POST"])
def prediction():
    if request.method == 'POST':
        data = request.form
        
        print('Data :',data)

        sell_price = SelPrice(data)
        price = sell_price.predict_selling_price()
        return render_template("index.html",prediction=price)
        # return jsonify({'Status': price})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)