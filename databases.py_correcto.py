#mongodb+srv://rogerlopez1111:<password>@prediccion2024.4z5uzg0.mongodb.net/
import streamlit as st
import certifi
import pandas as pd
from pymongo import MongoClient

st.title("Prueba")


def connection():
    return MongoClient("mongodb+srv://rogerlopez1111:1929394959697989@prediccion2024.4z5uzg0.mongodb.net/", tlsCAFILE=certifi.where())


conexion = connection()


def getData():
    db = conexion.get_database("Prediccion")
    collection = db.get_collection("ejemplo1")
    items = collection.find()
    data = [{'_id': str(item['_id']), 'name': item['name'], 'physics': item['physics'], 'maths': item['maths'], 'english': item['english']} for item in items]
    return data

def getDataClean():
    db = conexion.get_database("Prediccion")
    collection = db.get_collection("ejemplo1")
    items = collection.find()
    data = [{'name': item['name'], 'physics': item['physics'], 'maths': item['maths']} for item in items]
    return data

datos = getData()
st.dataframe(pd.DataFrame(datos))
limpio = getDataClean()
st.dataframe(pd.DataFrame(limpio))