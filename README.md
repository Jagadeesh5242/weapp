# Weather Monitoring Project

## Overview

The Weather Monitoring Project is a real-time data processing system that retrieves weather data from the OpenWeatherMap API and provides summarized insights using rollups and aggregates. The system continuously monitors weather conditions for selected metros in India and stores the results in a MongoDB database.

## Features

- Real-time weather data retrieval for cities in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Daily weather summaries with:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- User-configurable alerting thresholds for temperature and specific weather conditions.
- Visualization of daily weather summaries and triggered alerts.

## Technologies Used

- **Flask**: For building the web application.
- **MongoDB**: For storing weather data.
- **Requests**: To call the OpenWeatherMap API.
- **Docker**: For containerizing the application.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- MongoDB
- Docker (optional, if you want to run in a containerized environment)
- OpenWeatherMap API Key (sign up at [OpenWeatherMap](https://openweathermap.org/) for a free API key)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jagadeesh5242/weapp.git
   cd weapp
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    
3. Install the required dependencies:
   pip install -r requirements.txt
   
4. Set your OpenWeatherMap API key in the environment variable:
    export API_KEY='your_openweathermap_api_key'  # On macOS/Linux
    set API_KEY='your_openweathermap_api_key'  # On Windows

# Running the Application
1.Using Docker
Build and run the application using Docker Compose:

docker-compose up --build

2.Access the application in your web browser:

http://localhost:5000/weather/Delhi
Running Locally

3.Start the Flask application:
python app.py

### Acknowledgements

1.OpenWeatherMap API

2.Flask

3.MongoDB

4.Docker

