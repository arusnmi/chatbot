import google.generativeai as genai


gemini_api_key = "AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=gemini_api_key) 
model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')


def generate_custom_recipe(prompt):
    response = model.generate_content(prompt)
    return response.text if response else "Unable to generate a recipe."


def generate_seasonal_recipe(weather):
    season = None  # Initialize season with a default value
    print(weather)
    if weather['temperature'] is not None:
        if weather['temperature'] < 20:
            season = "Winter"
        elif weather['temperature'] > 30:
            season = "Summer"
        elif 20 <= weather['temperature'] <= 30:
            season = "Pleasant"

    if season == "Winter":
        prompt = "I want a warm and hearty dish for winter."
    elif season == "Summer":
        prompt = "I want a light and refreshing dish for summer."
    elif season == "Pleasant":
        prompt = "I want a recipe for the springtime."


