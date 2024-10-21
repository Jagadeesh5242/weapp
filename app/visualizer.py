# app/visualizer.py
import matplotlib.pyplot as plt
from datetime import datetime


class Visualizer:
    def plot_daily_summary(self, summaries):
        dates = [summary['date'] for summary in summaries]
        avg_temps = [summary['avg_temp'] for summary in summaries]
        max_temps = [summary['max_temp'] for summary in summaries]
        min_temps = [summary['min_temp'] for summary in summaries]

        plt.plot(dates, avg_temps, label='Avg Temp')
        plt.plot(dates, max_temps, label='Max Temp')
        plt.plot(dates, min_temps, label='Min Temp')

        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Daily Weather Summary')
        plt.legend()
        plt.show()
