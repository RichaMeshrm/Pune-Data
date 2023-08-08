from flask import Flask,render_template,request,jsonify

from project_data.utils import Pune_Prediction

app = Flask(__name__)

@app.route("/")
def home_api():
    print("We are in Homepage")
    # return "Successful"
    return render_template("index.html")

@app.route("/prediction_charges",methods=["POST", "GET"])
def price_prediction():
    if request.method=="GET":
        print("We are in get method")

        total_sqft = eval(request.args.get("total_sqft"))
        bath = eval(request.args.get("total_sqft"))
        balcony = eval(request.args.get("total_sqft"))
        area_type = request.args.get("area_type")
        size = request.args.get("size")
        site_location = request.args.get("site_location")


    object = Pune_Prediction(total_sqft,bath,balcony,area_type,size,site_location)
    charges = object.get_house_price()

    return render_template("index.html", prediction = charges)

if __name__ == "__main__":
    app.run()