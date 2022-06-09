import os 
import json
from flask import Flask,abort
from flask_cors import CORS, cross_origin
import numpy as np
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#http://myspectradb/entrypoint/spectra1234/reflectance/nm/100/openspectra?range=300-1000&step=0.1
@app.route("/<spectrum>/<modality>/<unit>/<expectedMaxValue>")
@cross_origin()
def getspectrum(spectrum,modality,unit,expectedMaxValue):
    if expectedMaxValue not in ["1","100","none"]:
        abort(400,"ExpectedMaxValue must be one of: 1,100,none")
    with open(f'/Users/univr/Documents/SpectraInteroperability/spectraformat/{spectrum}.json') as f:
        data = json.load(f)

    if int(data['proccesedValue']['expectedMaxValue']) != int(expectedMaxValue):
        scalefactor = int(expectedMaxValue)/data['proccesedValue']['expectedMaxValue']
        scaledarray = np.array(data['proccesedValue']['data'])*scalefactor
        data['proccesedValue']['expectedMaxValue'] = int(expectedMaxValue)
        data['proccesedValue']['data'] = scaledarray.tolist()
    return data