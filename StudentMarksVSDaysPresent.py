import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    cup_of_coffee = []
    sleep_hours = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            cup_of_coffee.append(float(row["Marks In Percentage"]))
            sleep_hours.append(float(row["Days Present"]))
    return {"x":cup_of_coffee, "y":sleep_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present is :- ", correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as f:
        df1 = csv.DictReader(f)
        fig = px.scatter(df1, x="Marks In Percentage", y="Days Present")
        fig.show()

def setup():
    data_path = "StudentMarksvsDaysPresent.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
