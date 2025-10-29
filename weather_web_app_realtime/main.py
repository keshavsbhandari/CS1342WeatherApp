# main.py
from display.show import display_weather

# Launch the Gradio app
if __name__ == "__main__":
    # Create the Gradio interface
    interface = display_weather()
    interface.launch(share=True)