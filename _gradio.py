import gradio

def greet(name, is_male, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    gender = "Male" if is_male else "Female"
    greeting = f"{salutation} {name}. It is {temperature} degrees today. {name} is a {gender}."
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gradio.Interface(
    fn=greet,
    inputs=[
        gradio.inputs.Textbox(label="Name"),
        gradio.inputs.Checkbox(label="Is Male?"),
        gradio.inputs.Checkbox(label="Is Morning?"),
        gradio.inputs.Slider(minimum=0, maximum=100, label="Temperature")
    ],
    outputs=["text", "number"]
    
)
demo.launch(share=True)
