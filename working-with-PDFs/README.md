Water Your PDF 
---------------------------

`temp.pdf` - source pdf in which you want to Add watermark
`water.pdf` - watermark pdf

> You have to rename your PDFs and replace the existing two in the *working-with-PDFs* folder.

Using the Command Line
--------------------------

###About PyPDF2
PyPDF2 is a pure-python PDF toolkit originating from the pyPdf project. It is currently maintained by Phaseit, Inc. PyPDF2 can extract data from PDF files, or manipulate existing PDFs to produce a new file. PyPDF2 is compatible with Python versions 2.6, 2.7, and 3.2 - 3.5.

###Installation

(Pip installation - *python3 install pip*)
`pip3 install PyPDF2`

###Time to Watermark
Inside the project folder, run:

`python3 watermark.py temp.pdf water.pdf`

Note
-------------------------

[Here](https://www.sejda.com/watermark-pdf) you can create your own custom Watermark.
Just use the blank.pdf which I provided.