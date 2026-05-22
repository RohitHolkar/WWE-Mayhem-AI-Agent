import google.generativeai as genai

genai.configure(api_key="AIzaSyA6-Wrj-9iZIbYfeu2b0_Q8RgAiq0k0jx4")

for model in genai.list_models():
    print(model.name)