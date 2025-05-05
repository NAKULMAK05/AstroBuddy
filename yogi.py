import os
import streamlit as st
from helperfuncs import get_birth_chart, get_house_chart, infer
import plotly.graph_objects as go
import datetime
import requests
import google.generativeai as genai
import pandas as pd
import numpy as np



# Load Gemini API Key securely
# added more features
GEMINI_API_KEY = "AIzaSyCuxNNYWsTftrrd2uTJ97Z2vIrm1nzm74c"
genai.configure(api_key=GEMINI_API_KEY) 

def run_gemini_agent(messages: list, instructions: str) -> dict:
    """
    Interact with the Gemini agent API using conversation history.

    :param messages: List of message history in the format [{"role": "user", "content": "text"}, ...]
    :param instructions: Instructions for the Gemini agent
    :return: A dictionary containing the bot's response
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Construct the input prompt
        prompt_text = instructions + "\n\n" + "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages]
        )
        response = model.generate_content(prompt_text)

        return {"output": response.text if response.text else "No response from the bot."}

    except Exception as e:
        return {"output": f"Error interacting with the Gemini API: {e}"}



def chatbot_ui():
    st.sidebar.header("🤖 Chat with Yogi Bot")
    st.sidebar.markdown("Ask any astrology-related question or seek advice from the bot.")

    # Display the uploaded image above the chatbot
    st.sidebar.image(r"yogi.jpg", caption="Yogi Bot", use_column_width=True)

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat display
    with st.sidebar.expander("Chatbot Session", expanded=True):
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(
                    f"<div style='text-align: right;'><b>You:</b> {message['content']}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(f"<b>Yogi Bot:</b> {message['content']}", unsafe_allow_html=True)

        user_message = st.text_input("Your Message", placeholder="Ask the astrology bot anything...")
        if st.button("Send"):
            if user_message:
                # Add user message to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_message})

                with st.spinner("Yogi Bot is thinking..."):
                    bot_instructions = "You are an astrology bot. Provide detailed and insightful astrological responses."
                    response = run_gemini_agent(st.session_state.chat_history, bot_instructions)
                    bot_reply = response.get("output", "Sorry, I couldn't process your request.")

                # Add bot reply to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})


def main():
    st.set_page_config(
        page_title="Divine Astrology App",
        page_icon="✨",
        layout="centered",
    )

    # Title Section
    st.title("✨AstroBuddy : Your Personal Spiritual Guide")
    st.markdown(
        """
        <p style="text-align: center; font-size: 18px; color: #5A5A5A;">
        Discover the mysteries of the cosmos with our birth chart generator. Align your spiritual path with celestial insights.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Section 1: Input Details
    st.header("🌟 Provide Your Birth Details")
    st.markdown("Fill in the details below to generate your birth chart.")

    # Input fields
    # Input fields
    col1, col2 = st.columns(2)

    with col1:
    # Input for birth details
        name = st.text_input("Name", placeholder="Enter your full name")
        gender = st.selectbox("Gender", options=["Male", "Female", "Other"], help="Select your gender")
        birth_date = st.date_input("Birth Date", value=datetime.date(2000, 1, 1))
        birth_lat = st.number_input(
            "Birth Latitude", value=40.7128, format="%.6f", help="Enter latitude in decimal format (e.g., 40.7128)."
    )

    with col2:
    # Input for location and time
        city = st.text_input("City", placeholder="Enter your birth city")
        state = st.text_input("State", placeholder="Enter your birth state")
        birth_time = st.time_input("Birth Time", value=datetime.time(12, 0))
        birth_lon = st.number_input(
            "Birth Longitude", value=-74.0060, format="%.6f", help="Enter longitude in decimal format (e.g., -74.0060)."
    )


    st.sidebar.header("📞 Contact Info")
    phone_number = st.sidebar.text_input(
        "Phone Number", placeholder="Enter your phone number", help="This helps associate the chart with your details."
    )

    # Chatbot integration
    chatbot_ui()

    st.divider()
    
    # Section 2: Generate Charts
    st.header("🛠️ Generate Your Chart")
    if st.button("Generate Birth Chart"):
        with st.spinner("Generating your divine birth chart..."):
            # Fetch birth chart data
            birth_chart_data = get_birth_chart(
                str(birth_date), str(birth_time), birth_lat, birth_lon, phone_number
            )
        
        if birth_chart_data:
            st.success("✨ Birth chart generated successfully!")
            
            # Display birth chart data in a readable format
            if "houses" in birth_chart_data:
                st.markdown("### 🏠 Houses Data")
                # Convert house data to a readable table
                houses_data = birth_chart_data["houses"]
                houses_table = [
                    {"House Name": house[0], "Zodiac Sign": house[1], "Degree Position": house[2]}
                    for house in houses_data
                ]
                # Display the table in a custom style
                st.table(houses_table)

            # AI insights section with enhanced styling
            st.markdown("### 🌌 AI Insights")
            with st.spinner("AI is analyzing your chart..."):
                res = infer(birth_chart_data)

            st.markdown(
                f"""
                <div class="ai-insights">
                    <h4>AI-Generated Inference</h4>
                    <p>{str(res.content)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error("🚨 Failed to generate birth chart. Please check your inputs.")
    

    st.markdown("")
    # Generate House Chart
    if st.button("Generate House Chart"):
        with st.spinner("Generating house chart..."):
            house_chart_json = get_house_chart()
            fig = go.Figure(house_chart_json)
            st.plotly_chart(fig, use_container_width=True)

    # Footer
    st.divider()
    st.markdown(
        """
        <p style="text-align: center; font-size: 14px; color: #7d7d7d;">
        ✨ For personalized consultations, contact a professional astrologer.  
        <br> Made with 💖 to guide your spiritual journey.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Custom CSS Styling
    st.markdown(
        """
        <style>
            body {
                background: #f4f7f6;
                color: #4a4a4a;
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
            }
            h1 {
                font-family: 'Lora', serif;
                font-size: 36px;
                color: #5a4d63;
                text-align: center;
                margin-top: 20px;
            }
            h2 {
                color: #7f6d85;
                text-align: center;
            }
            .stButton button {
                background-color: #c6705c;
                color: white;
                border: none;
                border-radius: 30px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .stButton button:hover {
                background-color: #b25d4d;
                transform: translateY(-2px);
            }
            .stButton button:focus {
                outline: none;
            }
            .ai-insights {
                background: linear-gradient(to right, #fff6e6, #ffe9c0);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            }
            .ai-insights h4 {
                color: #c6705c;
            }
            .ai-insights p {
                font-size: 16px;
                color: #5A5A5A;
                text-align: justify;
            }
            .stButton button {
                background-color: #c6705c;
                color: white;
                border: none;
                border-radius: 30px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }

            .stButton button:hover {
                background-color: #b25d4d;
                transform: translateY(-2px);
            }

            .stButton button:focus {
                outline: none;
            }

            .stTextInput input {
                background-color: #ffffff;
                color: #5A5A5A;
                border-radius: 10px;
                border: 2px solid #ddd;
                font-size: 14px;
                margin-bottom: 15px;
                width: 100%;
            }

            .stTextInput input:focus {
                outline: none;
                border: 2px solid #c6705c;
            }

            .table-container {
                background: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            }

            .house-table {
                width: 100%;
                margin-top: 20px;
                border-collapse: collapse;
            }

            .house-table th, .house-table td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }

            .house-table th {
                background-color: #ffe9c0;
                color: #c6705c;
                font-weight: bold;
            }

            .house-table tr:hover {
                background-color: #f2f2f2;
            }

            .header-section {
                text-align: center;
                padding: 40px 20px;
                background: linear-gradient(to right, #fdf0eb, #f5c7b1);
                border-radius: 15px;
                box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
                margin-bottom: 40px;
            }

            .header-section h1 {
                font-size: 48px;
                font-family: 'Lora', serif;
                color: #5a4d63;
                text-transform: uppercase;
            }

            .header-section p {
                font-size: 20px;
                color: #7a6f7d;
                margin-top: 10px;
                font-style: italic;
            }

            .footer {
                text-align: center;
                padding: 20px;
                background-color: #f1f1f1;
                border-top: 1px solid #e0e0e0;
                font-size: 14px;
                color: #7d7d7d;
            }

            .footer a {
                color: #c6705c;
                text-decoration: none;
                font-weight: bold;
            }

            .footer a:hover {
                text-decoration: underline;
            }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Custom header section with gradient background
    st.markdown("""
        <div class="header-section">
            <h1>✨ AstroBuddy : Your Personal Spiritual Guide</h1>
            <p>Embark on a journey of self-discovery with celestial insights</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content of the page
    st.markdown(
        """
        <p style="text-align: center; font-size: 18px; color: #5A5A5A;">
        Explore the cosmic forces at play in your life. Align your destiny with the stars and planets through personalized birth charts.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Add input forms, charts, and other interactive elements as in previous steps

    # Footer
    st.markdown(
        """
        <div class="footer">
            <p>✨ For personalized consultations, reach out to a professional astrologer.</p>
            <p>Made with 💖 to guide your spiritual journey.</p>
            <p>Visit our <a href="https://www.yourwebsite.com" target="_blank">website</a> for more insights.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
