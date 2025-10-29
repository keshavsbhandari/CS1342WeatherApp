
import gradio as gr
from display.format import format_weather_data

def display_weather():
    return gr.Interface(fn=format_weather_data, inputs="text", outputs="text", title="Weather App")
    