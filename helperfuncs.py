from astrapy import DataAPIClient
import requests
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import pandas as pd


llm = ChatGoogleGenerativeAI(
model="gemini-1.0-pro",
temperature=0, 
api_key= "AIzaSyCuxNNYWsTftrrd2uTJ97Z2vIrm1nzm74c")

system_prompt = """
You are an expert in analyzing indian horoscopic data from vedic data such as birth charts. 
Derive inferences from the data passed on to you and provide a structed response that includes monthly and daily horoscope and possible remedies for bad horoscopes. 
Your responses must not exceed 200 words. Following is the provided birth data: 
"""    
prompt_template = PromptTemplate(
    input_variables=["birth_data"],
    template=system_prompt + "\n\n{birth_data}"
)

client = DataAPIClient("AstraCS:RMifFnMYPPkZZTlrobbRYEnH:0bc5d925710d5efd2c7264147261438d066c56abfdd67ce41ad79c6af508b2c4")
db = client.get_database_by_api_endpoint(
  "https://47519d96-4761-4c86-b1d5-5bfd2a36c49f-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

# Base URL for the Flask API
BASE_URL = "https://80f0-34-125-179-65.ngrok-free.app"

# 1. Call to `/api/birth-chart` endpoint
def get_birth_chart(birth_date, birth_time, birth_lat, birth_lon, phone_number):
    url = f"{BASE_URL}/api/birth-chart"
    payload = {
        "birth_date": birth_date,
        "birth_time": birth_time,
        "birth_lat": birth_lat,
        "birth_lon": birth_lon
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        birth_chart_data = response.json()  
        
        birth_chart_data['phone_number'] = phone_number
        collection = db.get_collection('spiritual_ai')
        collection.insert_one(birth_chart_data)
        
        print("Birth chart data stored successfully.")
        
        return birth_chart_data 
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
def get_house_chart():
    url = f"{BASE_URL}/api/house-chart"
    response = requests.post(url)  
    if response.status_code == 200:
        return response.json()  
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
def infer(birth_data): 
    res = llm.invoke(prompt_template.format(birth_data=birth_data)) 
    return res
    
    



