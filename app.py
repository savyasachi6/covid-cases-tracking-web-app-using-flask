from flask import Flask, render_template, request,send_file

from covid import Covid

covid=Covid()

import pandas as pd

df=pd.read_csv('country.csv')

app = Flask(__name__)

a=df['country']

@app.route('/')
def details():

   
   
   return render_template('details.html',a=a)


@app.route('/result',methods = ['POST', 'GET'])

def result():

   total_active=covid.get_total_active_cases()
   total_deaths=covid.get_total_deaths()
   total_cases =covid.get_total_confirmed_cases()

   country= request.form.get('country')
    


   status=covid.get_status_by_country_name(country)


   
   return render_template("result.html" , total_cases=total_cases,total_deaths=total_deaths,total_active=total_active,status=status)


if __name__ == '__main__':

   app.run(debug = True)
   