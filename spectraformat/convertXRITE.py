# read tabdelimited data from Ocean Optics HR2000 and convert to csv
import os
from textwrap import indent
from datamod import Background
import datamod2
import re
import sys
path = os.path.join(os.getcwd(),'X-Rite1Profilerexample')
files = [i for i in os.listdir(path) if i.endswith('.txt')]
reflectionwavelengths = []
reflectionvalues = []

darkwavelengths = []
darkvalues = []

refwavelengths = []
refvalues = []
wavelengths = list(range(380,731,10))
for i in files:
    with open(os.path.join(path,i), 'r') as f:
        BEGIN_DATA = False
        for i in f:
            print(i)
            if i.startswith('DESCRIPTOR'):
                projectname = i.split()[1].strip().replace('"','')
            if BEGIN_DATA and not i.startswith('END_DATA'):
                print(i)
                data = i.split("\t")
                name = "_".join([data[0].strip(),data[1].strip()])
                # conert to float
                data = list(map(float, data[5:-1]))
                reflespec = datamod2.SpectrumData(
                type=datamod2.Type1.Reflectance,
                expectedMaxValue = 1,
                expectedMinValue = 0,
                unit=datamod2.Unit1.percentage,
                data=[data]
                )

                wavelenghts = datamod2.VariablesLabels(
                    name='Wavelength',
                    unit=datamod2.Unit.nm,
                    type=datamod2.Type.Wavelenghts,
                    expectedMaxValue = 730,
                    expectedMinValue = 380,
                    data=[wavelengths]
                )


                newfile = datamod2.OpenSpectraFormat(
                    proccesedValue=reflespec,
                    variablesLabels=wavelenghts,
                )
                #pydantic save json to file
                with open(f'{projectname}_{name}.json', 'w') as outfile:
                    outfile.write(newfile.json(indent=4))
            if i.startswith('BEGIN_DATA\n'):
                    BEGIN_DATA = True
            
                


