# app/alert_manager.py
class AlertManager:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def check_alerts(self, weather_data):
        alerts = []
        for city, data in weather_data.items():
            if data['temp'] > self.thresholds['temp']:
                alerts.append(f"Alert: Temperature exceeded in {city}. Current temperature: {data['temp']}°C")
        return alerts
