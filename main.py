from hashlib import new
from math import dist
from turtle import clear
from flask import Flask,render_template,url_for,request,session,logging,redirect,flash
from flask_cors import CORS
import os
import sys
import main
from flask import jsonify
import utils as coordCalc
import json


allResults=[]; 
app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

@app.route('/my-route') 
# @cross_origin()
def my_route():     
        source_city = request.args.get('st', default = '*', type = str)
        src_country = request.args.get('sc', default = '*', type = str)
        dest_city = request.args.get('dt', default = '*', type = str)
        dest_country = request.args.get('dc', default = '*', type = str)

        # # return jsonify(dict(data=[source_city, src_country, dest_city, dest_country]))
        # print("hello world",file=sys.stdout)
        # print(source_city,src_country,dest_city,dest_country,file=sys.stdout)

        result = coordCalc.lat_lon_calculator(source_city,src_country,dest_city,dest_country)
        
        new_result = {
            'Src_Country':result['Src Country'][0],
            'Src_Lat': result['Src Lat'][0],
            'Src_Lng': result['Src Lng'][0],
            'Src_Port_Lat': result['Src Port Lat'][0],
            'Src_Port_Lng': result['Src Port Lng'][0],
            'Src_Port': result["Src Port"][0],
            'Src_City': result['Src City'][0],
            'Dest_Port_Lat': result['Dest Port Lat'][0],
            'Dest_Port_Lng': result['Dest Port Lng'][0],
            'Dest_Lat': result['Dest Lat'][0],
            'Dest_Lng': result['Dest Lng'][0],
            'Dest_Country': result["Dest Country"][0],
            'Dest_Port': result['Dest Port'][0],
            'Dest_City':result['Dest City'][0]
           
        }
        return (new_result) 
          
       # allResults.append(new_result)  
       # return  jsonify({'coordinates':allResults})
       


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)