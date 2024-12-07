import google.generativeai as genai
import os 
from app.core.config import settings
import regex as re
from dotenv import load_dotenv

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(model_name = settings.GEMINI_MODEL) # Selected a free model

#funtion to remove all markdowns from the text
def remove_markdowns(text):
    text = re.sub(r'\[.?\]\(.?\)', '', text)  # Remove markdown links
    text = re.sub(r'[#\*`]', '', text)  # Remove markdown symbols
    return text

#function limit the token (input)
def limit_token(text):
    if len(text) > 10000: # Limit the token to 10000 characters
        text = text[:10000]
    return text

#function to paginate the output 
def paginate_output(text):
    if len(text) > 10000: # Limit the token to 10000 characters
        text = text[:10000]
    return text

def gemini_response(text):
    #TODO: Eliminate the markdowns from the text
    #TODO: Make sure to have a limit for the token (input)
    #TODO: Make sure to have a pagination for the output
    text = remove_markdowns(text)
    text = limit_token(text)
    response = model.generate_content(text)
    response.text = paginate_output(response.text)
    return response.text