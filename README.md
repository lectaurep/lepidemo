<!-- badges -->

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)  

<!-- end of badges-->

# LEPIDEMO : LECTAUREP PIPELINE DEMONSTRATOR

## Going from eScriptorium to TEI-Publisher

This demonstration shows the implementation of a pipeline going from PAGE XML to TEI Publisher created within the frame of the [LECTAUREP](https://lectaurep.hypotheses.org/) project. 

LECTAUREP is a project jointly led by Inria (ALMAnaCH) and the Archives nationales de France (DMC). Its purpose is to facilitate the exploration of thousands of pages of directories listing minutes and deeds redacted by Parisians notaries between the beginning of the 19th century and the mid-20th centuries. To do so, LECTAUREP relies on automatic transcription performed with [Kraken](http://kraken.re/) via the [eScriptorium](https://escriptorium.inria.fr) web application.

Images are loaded on the platform, then transcribed and annotated, and finally exported to PAGE XML files. The last section of the pipeline aims at offering users a platform to visualise, querry and read the pages of the directories. An almost ready-to-use solution consist in using [TEI-Publisher](https://teipublisher.com/index.html), which requires transforming the PAGE XML files into compliant TEI XML.

LEPIDEMO demonstrates how this transformation can be plugged into eScriptorium as a simple python script.

## A Jupyter notebook
The demonstration can be followed step by step using the [lepidemo.ipynb](https://gitlab.inria.fr/almanach/lectaurep/lepidemo/-/blob/master/lepidemo.ipynb) Jupyter scenario. 

## Cite this work
