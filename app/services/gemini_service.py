import google.generativeai as genai
import os 
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(model_name = settings.GEMINI_MODEL) # Selected a free model

def gemini_response(text):
    #TODO: Eliminate the markdowns from the text
    #TODO: Make sure to have a limit for the token (input)
    #TODO: Make sure to have a pagination for the output
    response = model.generate_content(text)
    return response.text