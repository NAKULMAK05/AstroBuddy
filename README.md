# AstroBuddy AI
AstroBuddy AI is a revolutionary platform that combines the ancient wisdom of astrology with cutting-edge AI technology to provide personalized fitness plans, dream analysis, and astrological insights. By leveraging advanced AI models and AstraDB, AstroBuddy delivers a seamless and transformative user experience.
<br/>

visit YouTube Video for more info : https://www.youtube.com/watch?v=RzIhGIcDukE <br/>
<br/>
  

## Features
### 1. AI-Powered Insights
- Generate personalized astrological insights based on the user’s birth details. 
- Identify life patterns, challenges, and provide remedies. 
- Offer actionable recommendations tailored to the user’s astrological profile.
### 2. Yogi Bot Integration
- Provide customized meditation and workout plans aligned with the user’s astrological traits and challenges.
- Perform dream analysis to uncover psychological and spiritual meanings.
### 3. Interactive Visualizations 
- Generate and render detailed birth charts with graphical representations.
- Display zodiac signs, house alignments, and degree positions in an intuitive format.
### 4. Secure Data Management
- Store all user data and generated insights securely in AstraDB.
- Enable efficient retrieval and future analysis of stored data.
### 5. Comprehensive Dream Analysis 
- Allow users to submit dreams for analysis.
- Use AI to interpret the psychological and astrological meanings of dreams.
## Workflow 
### Step 1: Collect User Inputs
1. **API Endpoint for User Data**
   - Accepts the following details: Birth Time, Birth Date, Birth Place (Latitude & Longitude).
   - Validates input for format and completeness.
   - Converts data into JSON format for further processing.
### Step 2: Generate Birth Chart
1. **Astrological Calculations**
   - Compute the birth chart using advanced algorithms.
   - Output a structured JSON birth chart.
2. **Visualization**
   - Render the birth chart graphically.
3. **Storage**
   - Save the generated chart in AstraDB vector database for future reference.
### Step 3: AI Insight Generation
1. **Retrieve Data**
   - Fetch the birth chart from AstraDB.
2. **Analyze Data**
   - Generate insights, identify patterns, and suggest remedies.
3. **Output to User**
   - Deliver insights in an engaging interface.
### Step 4: Integration with Yogi Bot
1. **Forward Dataset**
   - Share the birth chart and insights with Yogi Bot.
2. **Tailored Recommendations**
   - Provide meditation and workout plans.
   - Analyze user-submitted dreams.
3. **Interactive Experience**
   - Enable real-time interaction with Yogi Bot.
## API Documentation
### 1. Collect User Data
- **Endpoint:** `POST /api/v1/user-data`
- **Input:**
  ```json
  {
    "birth_time": "10:30 AM",
    "birth_date": "1990-05-15",
    "latitude": 40.7128,
    "longitude": -74.0060
  }
  ```
- **Output:**
  ```json
  {"status": "success", "message": "Data received successfully"}
  ```
### 2. Retrieve Birth Chart
- **Endpoint:** `GET /api/v1/birth-chart/{userId}`
- **Output:**
  ```json
  {
    "userId": "12345",
    "birth_chart": {"sun_sign": "Taurus", "moon_sign": "Leo"}
  }
  ```
### 3. Submit Dream for Analysis
- **Endpoint:** `POST /api/v1/dream-analysis`
- **Input:**
  ```json
  {"dream_description": "Flying over a forest during the night"}
  ```
- **Output:**
  ```json
  {"dream_meaning": "You seek freedom and wish to escape current limitations."}
  ```
## Future Enhancements
1. **Multi-language Support**
   - Broaden accessibility by introducing support for multiple languages.
2. **Advanced Visualizations**
   - Offer interactive and customizable birth chart visualizations.
3. **Wearable Device Integration**
   - Integrate with wearables for health tracking and real-time feedback.
4. **Gamification Features**
   - Incorporate gamified elements to engage users in astrology and wellness journeys.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
AstroBuddy AI: Empowering lives through the fusion of astrology and technology
