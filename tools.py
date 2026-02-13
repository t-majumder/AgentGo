import wikipedia
import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from datetime import datetime
from llm_call import gpt_oss_20b, gpt_oss_120b, qwen_32b, kimik2
import math
import warnings
warnings.filterwarnings("ignore")


###------------------------------------------------------------
## Wikipedia Search
###------------------------------------------------------------
def wikipedia_search(query:str) -> str:
    try:
        summary = wikipedia.summary(query, sentences=10)
        return summary
    except Exception as e:
        return f"Error: {str(e)}"

###------------------------------------------------------------
# DuckDuckGo Search
###------------------------------------------------------------
def web_search(query:str) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
        return results

###------------------------------------------------------------
# Web Scraping
###------------------------------------------------------------
def web_scraper(query:str) -> str:
    warnings.filterwarnings("ignore")
    try:
        url_prompt = query + f"\n\nFind a best relevant URL from here for the above query and summary and provide it to me. return only the most relevant url no wikipedia url please. Two searches at max Please select the most relevant url from the list of results." # Prompt to find a relevant url for the query and summary
        url = gpt_oss_120b(url_prompt).content # Calling the llm class to find a relevant url for the query and summary

        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for tag in soup(['script', 'style']):
            tag.decompose()
            
        text = soup.get_text() 
        text = text[:1000]  # Upto here text is scrapped but the issue is a lot of garbage is there. 
        summarized_text = gpt_oss_20b(text + "\n\nSummarize the above content please as much as possible and keep only the important portions.") # Calling the llm class to summarize the text
        
        return summarized_text.content
    
    except Exception as e:
        return f"Error: {str(e)}"

###------------------------------------------------------------
# Calculator tool
###------------------------------------------------------------
def calculator(expression: str) -> str:
    try:
        result = str(eval(expression, {"__builtins__": None}, math.__dict__))
        return result
    except Exception as e:
        return f"Error: {str(e)}"

###------------------------------------------------------------
# Current time tool
###------------------------------------------------------------
def current_time() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")



# if __name__ == "__main__":
#     query = "Tell me about the latest news in india today"
#     print("Wikipedia Search Result:")
#     print(wikipedia_search(query))
    
#     print("\nDuckDuckGo Search Results:")
#     results = web_search(query)
#     for result in results:
#         print(result)
    
#     url_prompt = query + f"{web_search(query)}\n\nFind a best relevant URL from here for the above query and summary and provide it to me. return only the most relevant url no wikipedia url please. Please select the most relevant url from the list of results." # Prompt to find a relevant url for the query and summary
#     url = gpt_oss_120b(url_prompt).content # Calling the llm class to find a relevant url for the query and summary
#     #url = "https://mausam.imd.gov.in/newdelhi/"
#     print("\nWeb Scraping Result:")
#     print(f"Searched Url: {url}\n" + web_scraper(url))
#     expression = "2 + 3 * 4"
#     print("\nCalculator Result:")
#     print(calculator(expression))
#     print("\nCurrent Time:")
#     print(current_time())
    