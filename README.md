# Real-Time Weather Monitoring System

## Setup

1. Clone the repository.
2. Get an API key from OpenWeatherMap.
3. Build and run the app with Docker Compose:
    ```bash
    docker-compose up --build
    ```

### API Key:
Set the API key in the `docker-compose.yml` file or via environment variables.

## Dependencies:
- Python 3.9
- Docker
- MongoDB
- OpenWeatherMap API

## Features:
- Real-time data fetching from the OpenWeatherMap API.
- Daily summaries (avg, min, max temps, dominant condition).
- Alerting system based on user-defined thresholds.
- Basic data visualization.
