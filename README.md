# SpectraInteroperabilityFramework
Prototypes for sharing and visualizing and comparing spectra from different repositories


The phylosofy of the package is to make open and interoperable the data collected by multiple instruments, in particular spectroscopic techniques (such as UV-VIS-NIR, FT-IR and Raman spectroscopy). Spectral data is particularly challenging because comparing data from multiple instruments require a high level of standardization in the procedure of collecting data and the processing of the data. 

Hence it is suggested to limit the processing and provide the data at his "rawest" level, the spectral server can provide the required processing for the correct visualization. For instance averaging, boxcar averaging and smoothing can all affect the results of the visualization often hiding dangerous artifacts.

Follows an example of possible user interactions for adding spectra from differente sources:

![An example of the behaviour of the viewer](example.gif?raw=true "The viewer consuming the spectra fromat")

This implementation uses Python and consists of: 

## A spectral server
A spectral server handles the request and return the spectra in the desired modality and range it consists of an API (similar to IIIF Image API).

Possible use case could be:
I want my spectra showing the reflectance in nanometer mapped between 0 to 100 values.

```
http://myspectradb/entrypoint/spectra1234/reflectance/nm/100/openspectra?range=300-1000&step=0.1&
```
Other common operation performed by the spectral server are reinterpolate the data. Smoothing and boxcar averaging.

## A common spectral data format
An open spectral data format is design using LOUD principles for generating Open Usable linked data. It uses JSON-LD format mantaining a the same time the data at the "rawest" level and the ready-to-use processed value. 

It allows annotations, spectra peaks can be annotated and linked with a bibliographic reference.

```
datamodel-codegen --input spectraformat-schema.json --output datamod.py
```



## A format for describing dataset of spectra
A collection of spectra can be described using another representation using JSON dataformat that allows to group spectra linked by some criteria. 

## A visualizer 
The visualizer allows to easily compare different spectra, these spectra can be responses of the spectral sever.

## Try the prototype
We use pipenv for managing the virtual enviroments.

```
pip install pipenv
cd spectraserver/
pipenv sync
pipenv shell
flask run 
```

This will start the spectra server.

## Unit of measurement

['nm','um','cm-1','µm','arbitrary unit']  