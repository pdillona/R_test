import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data.fish_api_train import getFishDataTrain
from data.fish_api_test import getFishDataTest

# dict타입으로 insert하고 dict타입으로 select하는게 가장 편함 - pymysql 라이브러리(mysql, maria)

# DataFrame도 DB에 insert하고 select가능 - SQLAlchemy(ORM)
# class타입으로도 insert하고 select가능

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")

def insert_Train():
    train = getFishDataTrain()
    train.to_sql("train", engine, index=False, if_exists="replace")

def insert_Test():
    test = getFishDataTest()
    test.to_sql("test", engine, index=False, if_exists = "replace")

