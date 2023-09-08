from flask_restful import Resource,Api,request
from flask import Flask,jsonify
import requests
import redis
app = Flask(__name__)
r = redis.Redis(host="redis",port="6379", db=0)
api = Api(app)

class GetData(Resource):
    def post(self):
        try:
            print(r.ping())
            code = request.json.get("code", "KHUL.TXT")
            url = f"http://tgftp.nws.noaa.gov/data/observations/metar/stations/{code}"
            response = requests.get(url)
            print(response.status_code)
            if response.status_code == 200:
                '''
                {‘data’: {‘station’: ‘KSGS’, ‘last_observation’: ‘2017/04/11 at 16:00
                GMT’, ‘temperature’: ‘-1 C (30 F)’, ‘wind’: ‘S at 6 mph (5 knots)’}}'''

                if r.get(code):
                    app.logger.debug("This is redis on line 23")
                    app.logger.debug("This is redis on line 23")
                    app.logger.debug("This is redis on line 23")
                    # app.logger.debug("This is type of code ",type(r.get(code)))
                    value = r.get(code)
                    app.logger.debug(type(value))
                    new_val = value.decode()
                    return jsonify({"Redis Data":new_val})

                else:
                    app.logger.debug("THis is normal")
                    print("this is normal redis")
                    r.setex(code, 60,str(response.text))
                    return jsonify({"THis is from web":response.text})

            else:
                return jsonify({"failure": "Something went wrong"})
        except Exception as e:
            return jsonify({"Error":str(e)})
api.add_resource(GetData,"/get_data")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
