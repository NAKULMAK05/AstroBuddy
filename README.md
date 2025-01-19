# AstroBuddy

**AstroBuddy** is an interactive web application that provides users with celestial navigation, stargazing assistance, and astronomy-related information in real time. Whether you're an amateur astronomer or just a curious stargazer, AstroBuddy is your go-to companion for exploring the night sky.

---

## Features

- **Star Identification:** Point your device at the night sky to identify stars, constellations, and planets in real-time.
- **AR Mode:** Enables augmented reality-based navigation to overlay celestial objects on your device screen.
- **Celestial Events:** Displays information about upcoming celestial events like meteor showers, eclipses, and planetary alignments.
- **Real-Time Tracking:** Track the current location of the International Space Station (ISS) and other celestial bodies.
- **Location-Based Customization:** Uses your GPS location to provide personalized sky maps and relevant celestial data.
- **Search and Explore:** Search for specific stars, planets, or constellations and get guided directions to locate them in the sky.

---

## How It Works

AstroBuddy leverages modern web technologies and APIs to provide real-time astronomy information and interactive features. Here is a breakdown of how it functions:

1. **User Location Access:**

   - Uses the Geolocation API to fetch the user's current latitude and longitude.
   - Provides location-specific stargazing data and celestial maps.

2. **Sky Mapping:**

   - Renders a dynamic sky map using libraries like `three.js` for 3D visualization.
   - Combines astronomical data to display constellations, planets, and other celestial bodies in their real-time positions.

3. **AR Navigation:**

   - Integrates AR.js or WebXR to enable augmented reality-based celestial navigation.
   - Displays overlays for celestial objects when viewed through the device camera.

4. **Celestial Data Fetching:**

   - Uses APIs like NASA Open APIs, Stellarium API, or Skyfield for retrieving accurate astronomical data.
   - Displays detailed information about stars, constellations, and planetary movements.

5. **User Interaction:**

   - Provides an intuitive UI for selecting celestial objects and getting information.
   - Allows users to search for specific objects or events and navigate to them using AR.

---

## Required Libraries and Dependencies

AstroBuddy uses the following libraries and tools to deliver its features:

### Frontend:

- **React.js:** For building the user interface.
- **Three.js:** For rendering the 3D celestial map.
- **AR.js/WebXR:** For augmented reality integration.

### Backend:

- **Node.js:** For server-side functionality.
- **Express.js:** For API routing and middleware handling.

### APIs:

- **Geolocation API:** To determine the user's location.
- **NASA Open APIs:** For fetching astronomical data.
- **Skyfield/Stellarium APIs:** For real-time celestial data.

### Additional Libraries:

- **Axios:** For making API requests.
- **React-Leaflet:** For rendering maps (optional).
- **Moment.js:** For handling date and time formats.
- **Compass.js:** For real-time compass direction (if applicable).

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NAKULMAK05/astrobuddy.git
   ```

2. Navigate to the project directory:

   ```bash
   cd astrobuddy
   ```

3. Install the dependencies:

   ```bash
   npm install
   ```

4. Start the development server:

   ```bash
   npm start
   ```

5. Open your browser and navigate to `http://localhost:3000` to view the app.

---

## Usage

1. **Enable Location Services:** Ensure location services are enabled on your device for accurate sky maps.
2. **Use AR Mode:** Tap the "Enable AR" button to activate augmented reality and point your device at the sky to explore celestial objects.
3. **Search for Celestial Objects:** Use the search bar to find specific stars, constellations, or planets.
4. **View Celestial Events:** Check the events section for upcoming astronomical phenomena.
5. **Track Real-Time Data:** Get live updates on the position of celestial bodies and events.

---

## Contributing

We welcome contributions to AstroBuddy! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

AstroBuddy is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments

- NASA Open APIs for providing astronomical data.
- The developers of Three.js and AR.js for their amazing tools.
- All contributors to open-source libraries and frameworks used in this project.
-

