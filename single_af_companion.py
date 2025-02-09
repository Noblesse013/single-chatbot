import gradio as gr
import subprocess

def run_ollama(prompt):
    """Run Ollama with the given prompt and return the output."""
    command = f'ollama run mistral "{prompt}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def chatbot(user_input, theme):
    """Chat with the Single AF Virtual Companion."""
    if "joke" in user_input.lower():
        prompt = "Tell me a funny joke about being single."
    elif "advice" in user_input.lower():
        prompt = "Give me some uplifting advice for someone who is single on Valentine's Day."
    elif "celebrate" in user_input.lower():
        prompt = "Write a short celebration message for someone who is proudly single."
    else:
        prompt = f"Respond to this in a friendly and supportive way: {user_input}"

    response = run_ollama(prompt)
    return response, theme

# Custom CSS for light and dark themes
custom_css = """
.light-theme { background-color: #ffffff; color: #000000; }
.dark-theme { background-color: #1e1e1e; color: #ffffff; }
"""

# Gradio Interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# 🌟 Single AF Virtual Companion 🌟")
    gr.Markdown("Welcome to your Single AF Virtual Companion! Get jokes, advice, or celebrate singlehood with me.")

    # Dropdown for theme selection
    theme = gr.Dropdown(choices=["Light", "Dark"], value="Light", label="Select Theme")

    # Chatbot interface
    with gr.Row():
        user_input = gr.Textbox(lines=2, placeholder="Type something to your Single AF Companion...", label="Your Message")
        output = gr.Textbox(lines=4, label="Companion", interactive=False)

    # Examples for quick input
    gr.Examples(
        examples=["Tell me a joke!", "Give me some advice.", "Celebrate singlehood with me!"],
        inputs=user_input
    )

    # Button to submit input
    submit_button = gr.Button("Send")

    # Function to handle theme and chatbot response
    def update_theme_and_chat(user_input, theme):
        response, _ = chatbot(user_input, theme)
        return response, theme

    # Set up interactivity
    submit_button.click(
        fn=update_theme_and_chat,
        inputs=[user_input, theme],
        outputs=[output, theme]
    )

    # Dynamically update the theme
    def apply_theme(theme):
        if theme == "Light":
            return gr.update(classes="light-theme")
        else:
            return gr.update(classes="dark-theme")

    theme.change(
        fn=apply_theme,
        inputs=theme,
        outputs=demo
    )

# Launch the app
demo.launch()