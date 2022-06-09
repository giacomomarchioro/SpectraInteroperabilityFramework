# read tabdelimited data from Ocean Optics HR2000 and convert to csv
import os
from textwrap import indent
import datamod3
import re
import sys
path = os.path.join(os.getcwd(),'testdataJCAMP','LABCALC.DX')
reflectionwavelengths = []
reflectionvalues = []

darkwavelengths = []
darkvalues = []

refwavelengths = []
refvalues = []
metadata = []
with open(path,'r') as f:
    for i in f:
        if "\t" in i:
            wavelength, value = i.split("\t")
            reflectionwavelengths.append(float(wavelength))
            reflectionvalues.append(float(value))
        if ":" in i: 
            key,value = i.split(":",1) 
            metadata.append({key:value.strip()})


reflespec = datamod3.SpectrumData(
    type=datamod3.Type1.Reflectance,
    expectedMaxValue = 100,
    expectedMinValue = 0,
    unit=datamod3.Unit1.percentage,
    data=[reflectionvalues]
)

refspec = datamod3.SpectrumData(
    type=datamod3.Type1.Counts,
    expectedMaxValue = 100,
    expectedMinValue = 0,
    unit=datamod3.Unit1.arbitrary_unit,
    data=[refvalues]
)

darkspc = datamod3.SpectrumData(
    type=datamod3.Type1.Counts,
    expectedMaxValue = 100,
    expectedMinValue = 0,
    unit=datamod3.Unit1.arbitrary_unit,
    data=[darkvalues]
)


wavelenghts = datamod3.VariablesLabels(
    name='Wavelength',
    unit=datamod3.Unit.nm,
    type=datamod3.Type.Wavelenghts,
    expectedMaxValue = 1097.04,
    expectedMinValue = 188.45,
    data=[reflectionwavelengths]
)


newfile = datamod3.OpenSpectraFormat(
    id="http://localhost:5000/OceanOptics_example1.json",
    metadata=metadata,
    proccesedValue=reflespec,
    variablesLabels=wavelenghts,
    background=darkspc,
    reference=refspec,
)

#pydantic save json to file
with open('OceanOptics_example1.json', 'w') as outfile:
    outfile.write(newfile.json(indent=2))
