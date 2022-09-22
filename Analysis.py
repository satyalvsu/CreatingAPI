from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os
import tabulate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('home.html')

@app.route('/analysis', methods=['POST'])  # This will be called from UI
def data_analysis():

    if (request.method=='POST'):
        file=request.files['myfile']

        # file_data=File(file)

        df = pd.read_csv(file)
        result = df.describe().T
        result=pd.DataFrame(result)
        format = lambda x: '%.2f' % x
        result = result.applymap(format)
        # result=result.style
        res=(result.to_html(classes='table table-stripped'))









    return render_template('result.html', data=res)








if __name__ == '__main__':
    app.run(debug=True)
