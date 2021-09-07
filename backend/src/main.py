from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from datetime import datetime
from functions import shortener
from sqlalchemy import create_engine
import json

app = Flask(__name__)

cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADER'] = 'Content-Type'
# app.config["SQLALCHEM_DATABASE_URI"] = 'mysql://root:yourpasswd@localhost/url_db'
engine = create_engine('mysql://root:yourpasswd@localhost/url_db')


@app.route('/encode', methods=['POST'])
def encode():

    if request.method == "POST":
        # Getting the current date
        curr_year = datetime.now().strftime('%Y')
        curr_month = datetime.now().strftime('%m')
        curr_day = datetime.now().strftime('%d')

        logic = 0

        date = curr_year + '-' + curr_month + '-' + curr_day

        data = request.json
        inputString = data["params"]["url_string"]
        print("The input string is : ", inputString)
        # Testing for exampleString
        # inputString = "https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-these-few-things-e5aaacd51942"

        # Getting the shortenedString
        shortenedString = shortener(inputString)
        outputString = "http://localhost:8000/" + shortenedString
        # Employing checking with database
        with engine.connect() as connection:
            records = connection.execute('SELECT * FROM url_tbl')

            for eachRow in records:
                if eachRow[1] == shortenedString:
                    logic = 1
                    outputString = "http://localhost:8000/" + shortenedString
                    print(outputString)
                    return(jsonify(outputString))

            if logic == 0:
                # Performing insertion into database
                insertion_query = "INSERT INTO url_tbl (shortened_url, original_url, creation_date) VALUES (%s,%s,%s)"
                outputString = "http://localhost:8000/" + shortenedString
                insertion_val = (shortenedString, inputString, date)
                connection.execute(insertion_query, insertion_val)
                print(outputString)
                return(jsonify(outputString))


@app.route('/<shortened_url>', methods=['GET'])
def getOriginalUrl(shortened_url):
    with engine.connect() as connection:
        try:
            records = connection.execute('SELECT * FROM url_tbl')

            for eachRow in records:
                if eachRow[1] == str(shortened_url):
                    if eachRow[2][:4] == "http" or eachRow[2][:5] == "https":
                        return redirect(eachRow[2], code=302)
                    if eachRow[2][:4] == "www.":
                        return redirect("https://"+eachRow[2][4:], code=302)
                    else:
                        return redirect("https://" + eachRow[2], code=302)
        except Error as e:
            print(e)


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
