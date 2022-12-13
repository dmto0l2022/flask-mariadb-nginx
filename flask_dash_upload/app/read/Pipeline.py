

Jupyter Notebook
DataPipeline Last Checkpoint: 5 hours ago (autosaved) Current Kernel Logo

Python 3 (ipykernel)

    File
    Edit
    View
    Insert
    Cell
    Kernel
    Widgets
    Help

Install Libraries

!pip install xlsxwriter

!pip install  xlrd

!pip install matplotlib

!pip install ipywidgets

!pip install openpyxl

!pip install python-dotenv

!pip install SQLAlchemy

!pip install pymysql

Requirement already satisfied: xlsxwriter in /srv/jupyterhub/env/lib/python3.11/site-packages (3.0.3)
Requirement already satisfied: xlrd in /srv/jupyterhub/env/lib/python3.11/site-packages (2.0.1)
Requirement already satisfied: matplotlib in /srv/jupyterhub/env/lib/python3.11/site-packages (3.6.2)
Requirement already satisfied: contourpy>=1.0.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (1.0.6)
Requirement already satisfied: cycler>=0.10 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (0.11.0)
Requirement already satisfied: fonttools>=4.22.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (4.38.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (1.4.4)
Requirement already satisfied: numpy>=1.19 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (1.23.5)
Requirement already satisfied: packaging>=20.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (22.0)
Requirement already satisfied: pillow>=6.2.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (9.3.0)
Requirement already satisfied: pyparsing>=2.2.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (3.0.9)
Requirement already satisfied: python-dateutil>=2.7 in /srv/jupyterhub/env/lib/python3.11/site-packages (from matplotlib) (2.8.2)
Requirement already satisfied: six>=1.5 in /srv/jupyterhub/env/lib/python3.11/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
Requirement already satisfied: ipywidgets in /srv/jupyterhub/env/lib/python3.11/site-packages (8.0.3)
Requirement already satisfied: ipykernel>=4.5.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipywidgets) (6.19.2)
Requirement already satisfied: ipython>=6.1.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipywidgets) (8.7.0)
Requirement already satisfied: traitlets>=4.3.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipywidgets) (5.7.1)
Requirement already satisfied: widgetsnbextension~=4.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipywidgets) (4.0.4)
Requirement already satisfied: jupyterlab-widgets~=3.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipywidgets) (3.0.4)
Requirement already satisfied: comm>=0.1.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (0.1.2)
Requirement already satisfied: debugpy>=1.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (1.6.4)
Requirement already satisfied: jupyter-client>=6.1.12 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (7.4.8)
Requirement already satisfied: matplotlib-inline>=0.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (0.1.6)
Requirement already satisfied: nest-asyncio in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (1.5.6)
Requirement already satisfied: packaging in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (22.0)
Requirement already satisfied: psutil in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (5.9.4)
Requirement already satisfied: pyzmq>=17 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (24.0.1)
Requirement already satisfied: tornado>=6.1 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipykernel>=4.5.1->ipywidgets) (6.2)
Requirement already satisfied: backcall in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (0.2.0)
Requirement already satisfied: decorator in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (5.1.1)
Requirement already satisfied: jedi>=0.16 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (0.18.2)
Requirement already satisfied: pickleshare in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (0.7.5)
Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.11 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (3.0.36)
Requirement already satisfied: pygments>=2.4.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (2.13.0)
Requirement already satisfied: stack-data in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (0.6.2)
Requirement already satisfied: pexpect>4.3 in /srv/jupyterhub/env/lib/python3.11/site-packages (from ipython>=6.1.0->ipywidgets) (4.8.0)
Requirement already satisfied: parso<0.9.0,>=0.8.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from jedi>=0.16->ipython>=6.1.0->ipywidgets) (0.8.3)
Requirement already satisfied: entrypoints in /srv/jupyterhub/env/lib/python3.11/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets) (0.4)
Requirement already satisfied: jupyter-core>=4.9.2 in /srv/jupyterhub/env/lib/python3.11/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets) (5.1.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /srv/jupyterhub/env/lib/python3.11/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets) (2.8.2)
Requirement already satisfied: ptyprocess>=0.5 in /srv/jupyterhub/env/lib/python3.11/site-packages (from pexpect>4.3->ipython>=6.1.0->ipywidgets) (0.7.0)
Requirement already satisfied: wcwidth in /srv/jupyterhub/env/lib/python3.11/site-packages (from prompt-toolkit<3.1.0,>=3.0.11->ipython>=6.1.0->ipywidgets) (0.2.5)
Requirement already satisfied: executing>=1.2.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets) (1.2.0)
Requirement already satisfied: asttokens>=2.1.0 in /srv/jupyterhub/env/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets) (2.2.1)
Requirement already satisfied: pure-eval in /srv/jupyterhub/env/lib/python3.11/site-packages (from stack-data->ipython>=6.1.0->ipywidgets) (0.2.2)
Requirement already satisfied: six in /srv/jupyterhub/env/lib/python3.11/site-packages (from asttokens>=2.1.0->stack-data->ipython>=6.1.0->ipywidgets) (1.16.0)
Requirement already satisfied: platformdirs>=2.5 in /srv/jupyterhub/env/lib/python3.11/site-packages (from jupyter-core>=4.9.2->jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets) (2.6.0)
Requirement already satisfied: openpyxl in /srv/jupyterhub/env/lib/python3.11/site-packages (3.0.10)
Requirement already satisfied: et-xmlfile in /srv/jupyterhub/env/lib/python3.11/site-packages (from openpyxl) (1.1.0)
Requirement already satisfied: python-dotenv in /srv/jupyterhub/env/lib/python3.11/site-packages (0.21.0)
Requirement already satisfied: SQLAlchemy in /srv/jupyterhub/env/lib/python3.11/site-packages (1.4.45)
Requirement already satisfied: greenlet!=0.4.17 in /srv/jupyterhub/env/lib/python3.11/site-packages (from SQLAlchemy) (2.0.1)
Requirement already satisfied: pymysql in /srv/jupyterhub/env/lib/python3.11/site-packages (1.0.2)

import os

from os import environ, path

from dotenv import load_dotenv

#BASE_DIR = path.abspath(path.dirname(__file__))

cwd = os.getcwd()

load_dotenv(path.join(cwd, "env"))

​

UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')

print(UPLOAD_FOLDER)

/uploads

UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')

​

MARIADB_USERNAME = environ.get('MARIADB_USERNAME')

MARIADB_PASSWORD = environ.get('MARIADB_PASSWORD')

MARIADB_DATABASE = environ.get('MARIADB_DATABASE')

MARIADB_CONTAINER = environ.get('MARIADB_CONTAINER')

SQLALCHEMY_DATABASE_URI =  "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" +\

                            MARIADB_PASSWORD + "@" + MARIADB_CONTAINER + ":3306/" +\

                            MARIADB_DATABASE

​

##pymysql

SQLALCHEMY_DATABASE_URI =  "mariadb+pymysql://" + MARIADB_USERNAME + ":" +\

                            MARIADB_PASSWORD + "@" + MARIADB_CONTAINER + ":3306/" +\

                            MARIADB_DATABASE

SQLALCHEMY_DATABASE_URI

'mariadb+pymysql://pythonuser:pythonuser@10.154.0.20:3306/data'

from sqlalchemy import create_engine

​

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

import pandas as pd

import numpy as np

df1 = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})

df1.to_sql('users', con=engine, if_exists='replace')

3

import os

dirname = os.getcwd()

print(dirname)

/srv/jupyterhub/home/jupyterhub/pipeline-202212

os.environ['MPLCONFIGDIR'] = dirname

import matplotlib

#!pip install xlsxwriter

#!pip install xlrd

#!pip install matplotlib

import xlsxwriter

import xlrd

Introduction

from datetime import datetime

from datetime import datetime

my_date = datetime.now()

print(my_date.isoformat())

2022-12-13T11:21:07.060585

print(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))

2022-12-13T11:21:07.060585

runid = "R" + my_date.strftime('%Y%m%d%H%M%S%f%z')

runid

'R20221213112107060585'

dirname = os.getcwd()

print(dirname)

/srv/jupyterhub/home/jupyterhub/pipeline-202212

# Read XML

​

Upload File
Excel Data Types

The following functions are use to work out the data type of an excel cell.

def validate_date(date_text):

    try:

        format_string = '%Y-%m-%d %H:%M:%S'

        datetime.strptime(date_text, format_string)

        return "OK"

    except ValueError:

        return None

​

def GetDataType(row_in):

    valueasstring = str(row_in['CellValue'])

    if validate_date(valueasstring) != None:

        return 'Date'

    elif valueasstring.isnumeric():

        return 'Number'

    else:

        return 'Text'

​

def add1_2row(row_in):

    return row_in['RowID'] + 1

​

​

def add1_2column(row_in):

    return row_in['ColumnID'] + 1

#from ipywidgets import FileUpload

#upload = FileUpload()

#upload

#import io

#filedf = pd.read_excel(upload.data[0],sheet_name=None, header=None, encoding='utf-8', errors='ignore')

#filedf = pd.read_excel(upload.data[0],sheet_name=None, header=None)

filename = dirname + '/Data.xlsx'

filedf = pd.read_excel(filename,engine='openpyxl', sheet_name=None, header=None)

#/content/drive/MyDrive/Work/Data/Data.xlsx

#filedf

Read All Sheets into Data Frame

sheetnames = list(filedf.keys())

print(sheetnames)

['AgeGenderSheet', 'HomeSheet', 'JobSheet', 'MaritalDepartmentSheet', 'DataMap', 'TemplateValidationMap', 'DataSet', 'Rules', 'Palette', 'PickList', 'MetaData']

Each Sheet is retrieved into Dataframes

DataMapDF = specdf['DataMap'] TemplateValidationMapDF = specdf['TemplateValidationMap'] DataSetDF = specdf['DataSet'] RulesDF = specdf['Rules'] PaletteDF = specdf['Palette'] PickListDF = specdf['PickList'] datadf = pd.DataFrame()

​

​

The following converts the whole spreadsheet into a cell database and this is used throughout for all data frame population.

celldbstagedf = pd.DataFrame()

sheetdf = filedf['DataMap'].copy()

sheetdf["RowID"] = sheetdf.index

#sheetdf

for currentsheetname in sheetnames:

​

    sheetdf = filedf[currentsheetname].copy()

    sheetdf["RowID"] = sheetdf.index

    celldb = pd.melt(sheetdf, id_vars=['RowID'])

    celldb = celldb.rename(columns={"variable": "ColumnID", "value": "CellValue"})

    celldb["CellType"] = "Unset"

    celldb["FileName"] = runid

    celldb["SheetName"] = currentsheetname

    

    celldb["ColumnID"] = celldb["ColumnID"]

​

    try:

        celldb["CellType"] = celldb.apply(GetDataType, axis=1)

        celldb["RowID"] = celldb.apply(add1_2row, axis=1)

        celldb["ColumnID"] = celldb.apply(add1_2column, axis=1)

​

    except:

​

        celldb["CellType"] = 'unknown'

        celldb["RowID"] = 0

        celldb["ColumnID"] = 0

​

    celldbstagedf = pd.concat([celldbstagedf,celldb], ignore_index=True)

​

    celldb = pd.DataFrame()

​

​

fullcelldb = celldbstagedf.copy()

fullcelldb.to_sql('raw_celldb', con=engine, if_exists='replace')

1172

parametersheets = ['DataMap', 'TemplateValidationMap', 'DataSet', 'Rules', 'Palette', 'PickList']

placeholders = ", ".join(["%s" for _ in parametersheets])

​

query = '''SELECT * FROM raw_celldb 

           WHERE SheetName in ({});

        '''.format(placeholders)

​

df2 = pd.read_sql_query(query, con=engine, params=(parametersheets))

df2

	index 	RowID 	ColumnID 	CellValue 	CellType 	FileName 	SheetName
0 	251 	1 	1 	SheetName 	Text 	R20221213112107060585 	DataMap
1 	252 	2 	1 	AgeGenderSheet 	Text 	R20221213112107060585 	DataMap
2 	253 	3 	1 	AgeGenderSheet 	Text 	R20221213112107060585 	DataMap
3 	254 	4 	1 	AgeGenderSheet 	Text 	R20221213112107060585 	DataMap
4 	255 	5 	1 	AgeGenderSheet 	Text 	R20221213112107060585 	DataMap
... 	... 	... 	... 	... 	... 	... 	...
884 	1135 	2 	2 	London 	Text 	R20221213112107060585 	PickList
885 	1136 	3 	2 	Liverpool 	Text 	R20221213112107060585 	PickList
886 	1137 	1 	3 	Gender 	Text 	R20221213112107060585 	PickList
887 	1138 	2 	3 	Male 	Text 	R20221213112107060585 	PickList
888 	1139 	3 	3 	Female 	Text 	R20221213112107060585 	PickList

889 rows × 7 columns

​

#df = celldbstagedf[celldbstagedf['SheetName']=='AgeGenderSheet']

parametersheets = ['DataMap', 'TemplateValidationMap', 'DataSet', 'Rules', 'Palette', 'PickList']

DatasetCells = fullcelldb[~fullcelldb.SheetName.isin(parametersheets)]

#DatasetCells

​

#df[~df.country.isin(countries_to_keep)]

Get Picklist Values

Picklist are like a mini Master Data Management System

They define the acceptable values for a partcular Field in Excel

The challenge here was to check one column to a another column that contained a list. I go there in the end.

PickListCells = pd.DataFrame()

# This process uses the full cell database as the column headings are the Picklist Names

PickListCells = fullcelldb[(fullcelldb['SheetName'] == 'PickList')].copy()

# PickListCellsList = PickListCells.groupby('ColumnID')['CellValue'].apply(lambda group_series: group_series.tolist()).reset_index()

​

PickListCellsList = PickListCells.groupby('ColumnID').agg({'CellValue':lambda x: list(x)})

​

# these were odd, but glad I work them out, it is important to realise that these are operations on a number of rows, not just one

# maybe it was the axis that made the difference!

PickListCellsList['KeyWord'] = PickListCellsList.apply(lambda row : row['CellValue'][0], axis = 1)

PickListCellsList['FormulaKeyWord'] = PickListCellsList.apply(lambda row : 'PickList', axis = 1)

PickListCellsList['List'] = PickListCellsList.apply(lambda row : row['CellValue'][1:], axis = 1)

# PickListCellsList['KeyWord'] = PickListCellsList['CellValue']

#PickListCellsList= pd.DataFrame(PickListCellsList, columns=['KeyWord', 'List'])

PickListCellsList = pd.DataFrame(PickListCellsList, columns=['KeyWord', 'FormulaKeyWord', 'List'])

#PickListCellsList.head()

# These were attempts at creating a suitable list for the function to check to

​

# PickListCellsList['Result'] = PickListCellsList['KeyWord'].isin(PickListCellsList['List']).map({True: 0, False: 1})

​

# PickListCellsList['Result'] = PickListCellsList['KeyWord'].str.contains('|'.join(PickListCellsList['List']))

# PickListCellsList['Result'] = PickListCellsList['KeyWord'].str.contains('|'.join(x) for x in PickListCellsList['List'])

# ["".join(x) for x in lst]

# PickListCellsList['ListAsString'] = PickListCellsList['List'].str.join('-')

# PickListCellsList['ListAsTuple'] = tuple(PickListCellsList['CellValue'])

​

#MyList = pd.DataFrame()

#MyList =  PickListCellsList

# still do not know why the following DOES NOT WORK!

# MyList['Result'] = PickListCellsList['ListAsString'].isin(PickListCellsList['KeyWord'])

​

# leaving this as a rememberance of the 6 hours spent on this!

# MyList['Result1'] = PickListCellsList['KeyWord'].apply(lambda x: any(i in x for i in PickListCellsList['List']))

# MyList['Result2'] = PickListCellsList['ListAsString'].str.contains(PickListCellsList['KeyWord'])

# mask = df['A'].apply(lambda x: any(i in x for i in search_list))

# PickListCellsList['Result2'] = PickListCellsList['ListAsTuple'].str.contains(PickListCellsList['KeyWord'])

# PickListCellsList['Result2'] = PickListCellsList['KeyWord'].str.contains(tuple(PickListCellsList['List']))

# PickListCellsList['ListAsTuple'].isin(PickListCellsList['KeyWord'])

# MyList['Result2'] = PickListCellsList['List'].apply(lambda x: True if (PickListCellsList.KeyWord in x).any() else False)

######### MyList['sing'] = 'Single'

# MyList['res1'] = MyList.apply(lambda ts: any(ts == 'Single'), axis=1)

# MyList['res2'] = MyList.apply(lambda ts: MyList['KeyWord'].str.contains('Single'), axis=1)

######### MyList['res3'] = MyList.apply(lambda x: x['sing'] in x['ListAsTuple'], axis=1)  ###############

######### MyList['res4'] = MyList.apply(lambda x: x['sing'] in x['List'], axis=1).map({True: 1, False: 0}) ###############

# # # # dataset.apply(lambda x: x['CellValue'] in x['PickList'], axis=1).map({True: 1, False: 0})

# data['Activity].str.contains('skin diving')

# lambda x : True if (x > 10 and x < 20) else False

#MyList.head()

# https://stackoverflow.com/questions/48460234/pandas-apply-valueerror-the-truth-value-of-a-series-is-ambigous

Get Data Map

DataMapCells = pd.DataFrame()

DataMapCells = fullcelldb[(fullcelldb['SheetName'] == 'DataMap')].copy()

#DataMapCells.head()

Below extracts a Sheet from the cell database and reshapes it to it original tabular form.

DataMap = pd.DataFrame()

DataMap = DataMapCells.pivot_table(index = ['RowID'], values = 'CellValue',columns = 'ColumnID', aggfunc = 'max')

ColumnHeadings = DataMap.iloc[0]

ColumnHeadingsList = list(ColumnHeadings)

print(ColumnHeadingsList)

ColumnHeadingsListTuple = enumerate(ColumnHeadingsList,start=1)

ColumnHeadingsListDict = dict(ColumnHeadingsListTuple)

print(ColumnHeadingsListDict)

DataMap = DataMap.rename(columns=ColumnHeadingsListDict)

DataMap = DataMap.drop([1])

#DataMap.head()

Make Rules Database

RulesCells = pd.DataFrame()

RulesCells = fullcelldb[(fullcelldb['SheetName'] == 'Rules')].copy()

#RulesCells.head()

RulesMatrix = pd.DataFrame()

RulesMatrix = RulesCells.pivot_table(index = ['RowID'], values = 'CellValue',columns = 'ColumnID', aggfunc = 'max')

ColumnHeadings = RulesMatrix.iloc[0]

ColumnHeadingsList = list(ColumnHeadings)

print(ColumnHeadingsList)

ColumnHeadingsListTuple = enumerate(ColumnHeadingsList,start=1)

ColumnHeadingsListDict = dict(ColumnHeadingsListTuple)

print(ColumnHeadingsListDict)

RulesMatrix = RulesMatrix.rename(columns=ColumnHeadingsListDict)

RulesMatrix = RulesMatrix.drop([1])

RulesMatrix.head()

RulesMatrix.head()

The above is the Rules definition sheet. It used KeyWords to define the checks. Below forms a list of KeyWords that are relevant to a particular field in a DataSet

Rules2Apply = pd.DataFrame()

Rules2Apply = pd.melt(RulesMatrix, id_vars=['RuleID', 'DataSetID', 'FieldID'])

Rules2Apply

Rules2Apply.value.unique()

Rules2Apply = Rules2Apply.rename(columns={"ColumnID": "RuleType", "value": "KeyWord"})

Rules2Apply = Rules2Apply[Rules2Apply.KeyWord.notnull()]

Rules2Apply.KeyWord.unique()

# df['A'] = df.apply(lambda x: x['B'] if x['A']==0 else x['A'], axis=1)

# The following adds the KeyWord Null into the Rules list - if Null is N, this means Nulls are Not Allowed

Rules2Apply['KeyWord'] = Rules2Apply.apply(lambda x: x['RuleType'] if x['KeyWord']=='N' else x['KeyWord'], axis=1)

#Rules2Apply['New'] = Rules2Apply.apply(lambda x: x['RuleType'] if x['KeyWord']=='N' else x['KeyWord'], axis=1)

Rules2Apply.KeyWord.unique()

PickListCellsList

Rules2Apply = pd.merge(Rules2Apply,PickListCellsList, on=['KeyWord'],how='left')

​

Rules2Apply

Add Code and Formulae to Rules Database

Palette defines the Rule Text and Rule Formula.

PaletteCells = pd.DataFrame()

PaletteCells = fullcelldb[(fullcelldb['SheetName'] == 'Palette')].copy()

PaletteCells.head()

Palette = pd.DataFrame()

Palette = PaletteCells.pivot_table(index = ['RowID'], values = 'CellValue',columns = 'ColumnID', aggfunc = 'max')

ColumnHeadings = Palette.iloc[0]

ColumnHeadingsList = list(ColumnHeadings)

print(ColumnHeadingsList)

ColumnHeadingsListTuple = enumerate(ColumnHeadingsList,start=1)

ColumnHeadingsListDict = dict(ColumnHeadingsListTuple)

print(ColumnHeadingsListDict)

Palette = Palette.rename(columns=ColumnHeadingsListDict)

Palette = Palette.drop([1])

Palette.head()

DatasetCells = pd.DataFrame()

DatasetCells = fullcelldb[(fullcelldb['SheetName'] == 'DataSet')].copy()

DatasetCells

Datasets = pd.DataFrame()

Datasets = DatasetCells.pivot_table(index = ['RowID'], values = 'CellValue',columns = 'ColumnID', aggfunc = 'max')

ColumnHeadings = Datasets.iloc[0]

ColumnHeadingsList = list(ColumnHeadings)

print(ColumnHeadingsList)

ColumnHeadingsListTuple = enumerate(ColumnHeadingsList,start=1)

ColumnHeadingsListDict = dict(ColumnHeadingsListTuple)

print(ColumnHeadingsListDict)

Datasets = Datasets.rename(columns=ColumnHeadingsListDict)

Datasets = Datasets.drop([1])

Datasets.head()

​

#palette = pd.merge(palette, PaletteDF, on=['KeyWord'],how='left')

​

Tests2Do = pd.merge(Datasets, Rules2Apply, on=['FieldID', 'DataSetID'])

Tests2Do['KeyWord'] = Tests2Do.apply(lambda x: x['FormulaKeyWord'] if x['FormulaKeyWord']=='PickList' else x['KeyWord'], axis=1)

Tests2Do.head(5)

Tests2DoWithFormula = pd.merge(Tests2Do, Palette, on=['KeyWord'])

Tests2DoWithFormula.head()

Get Start Anchor Cells

Start Anchors are where tables are mapped from, every dataset in the spreadsheet must be anchored to a uniquely identifiable cell in a particular sheet.

startanchors = pd.DataFrame()

startanchors = pd.DataFrame(Datasets, columns=['DataSetID', 'SheetName', 'ReferenceTextStart'])

startanchors = startanchors.rename(columns={"ReferenceTextStart": "CellValue"})

startanchors = startanchors.drop_duplicates()

startanchors.head()

​

Get All End Anchor Cells

End anchors are where a dataset finishes. Probably at the next Start Anchor. This does mean that blank rows are validated and one needs to filter these out later.

endanchors = pd.DataFrame()

endanchors = pd.DataFrame(Datasets, columns=['DataSetID', 'SheetName', 'ReferenceTextEnd'])

endanchors = endanchors.rename(columns={"ReferenceTextEnd": "CellValue"})

endanchors = endanchors.drop_duplicates()

endanchors.head()

Find Start Anchors

Now we look for the start and finish anchor cells for each dataset.

findstartanchors = pd.DataFrame()

findstartanchors = pd.merge(startanchors, fullcelldb, on=['SheetName', 'CellValue'])

findstartanchors = findstartanchors.rename(columns={"RowID": "AnchorRow", "ColumnID": "AnchorColumn"})

findstartanchors = pd.DataFrame(findstartanchors, columns=['DataSetID', 'SheetName', 'AnchorRow', 'AnchorColumn'])

findstartanchors.head()

Find End Anchors

Some datasets have no finish anchors as they are the last table in the sheet.

findendanchors = pd.DataFrame()

findendanchors = pd.merge(endanchors, fullcelldb, on=['SheetName', 'CellValue'])

findendanchors = findendanchors.rename(columns={"RowID": "EndRow"})

findendanchors = findendanchors[findendanchors.CellValue.notnull()]

findendanchors = pd.DataFrame(findendanchors, columns=['DataSetID', 'SheetName', 'EndRow'])

findendanchors.head()

​

Join Anchors Together

Join the anchors to allow them to be joined with the data table As stated above, some DataSets have NaN as the EndRow as there is no further data in the sheet

anchors = pd.DataFrame()

anchors = pd.merge(findstartanchors, findendanchors, on=['DataSetID', 'SheetName'], how='left')

anchors.head()

Using Anchors and Dataset Create Map to Find Data

The DataSet defines where the DataSets can be found from the Start Anchor Cells The following joins the found cells with the DataSet map.

​

​

datasetmap = pd.DataFrame()

datasetmap = pd.merge(Datasets, anchors, on=['DataSetID', 'SheetName'], how='left')

datasetmap = pd.DataFrame(datasetmap,

                          columns=['DataSetID', 'SheetName', 'FieldID',

                                   'AnchorRow', 'AnchorColumn','EndRow',

                                   'RowFromReferenceText',

                                   'ColumnFromReferenceText','FieldPosition'])

​

Show Dataset Map

datasetmap.head()

Find where Data Starts and what Columns Fields are In

One needs to now calculate the actual rows and columns of where the DataSet is. The above table is relative to the Anchor Cells

datasetmap['StartRow'] = datasetmap['AnchorRow'] + datasetmap['RowFromReferenceText']

datasetmap['FieldColumn'] = datasetmap['AnchorColumn'] + datasetmap['ColumnFromReferenceText']

dataset = pd.DataFrame()

dataset = pd.merge(fullcelldb, datasetmap, on=['SheetName'], how='left')

## the above may seem a cartesian join and may need to be looked at if this slows the process down

dataset

Filter Out Data after End Anchor Row

dataset = dataset[(dataset.RowID >= dataset.StartRow) &

(dataset.ColumnID == dataset.FieldColumn) &

((dataset.RowID < dataset.EndRow) | pd.isnull(dataset.EndRow))]

# the | above is an OR as if there is no EndRow for the dataset you want to

# allow the data through

dataset

Create a CellValue as Number for use in Formulae

dataset1 = dataset[['DataSetID', 'SheetName', 'FieldID', 'RowID', 'ColumnID','CellValue', 'CellType']].copy()

dataset1['DataSetID']

dataset1['CellValueAsNumber'] = pd.to_numeric(dataset1['CellValue'], errors='coerce')

dataset1.head(5)

Create a List of Checks to do

todolist = pd.DataFrame()

todolist = pd.merge(dataset1, Tests2DoWithFormula, on=['DataSetID', 'FieldID'])

todolist.head(5)

Create a List of distinct formula to apply

formulas = pd.DataFrame()

formulas = pd.DataFrame(todolist, columns=['KeyWord','PythonFormula'])

formulas = formulas.drop_duplicates()

formulas.head(10)

Prepare Results Table

global bigresults

littletodolist = pd.DataFrame()

littletodolistworking = pd.DataFrame()

bigresults = pd.DataFrame()

​

# this was an important test as if you do not have copy you get an error as it believes

# you are trying to change a view

#littletodolist = todolist[(todolist.KeyWord == 'PickList')].copy()

#littletodolist.head(100)

#filterdf = pd.DataFrame()

#filterdf = todolist[(todolist.KeyWord == 'PickList')].copy()

#filterdf.head()

# littletodolist.loc[littletodolist.KeyWord == 'Text', 'Result'] = np.where(littletodolist['CellType'] == 'Text', 1, 0)

Loop through each Formula and apply to the To Do List

todolist = todolist.rename(columns={'CellValue_x': 'CellValue'})

##todolist.columns

for index, row in formulas.iterrows():

  # print(row['KeyWord'],row['PythonFormula'])

​

  pf = row['PythonFormula']

  kw = row['KeyWord']

 

  try:

      pf1 = pf.replace("dataset", "littletodolist")

  except:

      pf1 = "1"

  littletodolist = todolist[(todolist.KeyWord == kw)].copy()

  formula2do = "littletodolist['Result'] = " + pf1

  print(kw)

  print(formula2do)

  exec(formula2do)

  ##print(littletodolist)

  ##try:

  ##bigresults = pd.concat([bigresults, littletodolist], ignore_index=True).drop_duplicates().reset_index(drop=True)

  bigresults = pd.concat([bigresults, littletodolist]) ##, ignore_index=True).drop_duplicates().reset_index(drop=True)

  ##except:

  #  bigresults = bigresults

littletodolist['Result'] = np.where(littletodolist['CellType'] == 'Text', 1, 0)

Add a sequence to the Results for use in Reporting

bigresults['ResultID'] = bigresults.index

bigresults.head(5)

Narrow down Results to useful columnns

usefulresults = pd.DataFrame()

usefulresults = pd.DataFrame(bigresults, columns=['DataSetID','FieldID','RowID','ColumnID','CellValue','CellType','CheckPerformed', 'Result'])

usefulresults.head()

Summarise Results

resultssummary = pd.DataFrame()

# index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])

# resultssummary.head()

​

resultssummary = bigresults[['DataSetID','FieldID','CheckPerformed', 'Result', 'ResultID']].groupby(['DataSetID', 'FieldID', 'CheckPerformed']).agg(['count'])

resultssummary.head(5)

Pivot Results

# rownamearray = pd.array(['DataSet','FieldID'], dtype=str)

# newct = pd.crosstab(bigresults.DataSet,bigresults.FieldID,bigresults.CheckPerformed,bigresults.Result,rownames=rownamearray, colnames=['Result'])

​

newct = bigresults.pivot_table(index = ['DataSetID','FieldID','CheckPerformed'], values = 'ResultID',columns = 'Result', aggfunc = 'count')

newct

Plot Stack Bar
Show Stack

newct.plot(kind='barh', stacked=True)

