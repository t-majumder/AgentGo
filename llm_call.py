import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import warnings
warnings.filterwarnings("ignore")
load_dotenv()

##### GPT-OSS-20B ##### 
def gpt_oss_20b(message: str, tools=None):
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        tools=tools,                  
        tool_choice="auto",           
        temperature=0.7
    )
    
    response = llm.invoke(message)  
    return response

##### GPT-OSS-120B #####
def gpt_oss_120b(message: str, tools=None):
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        tools=tools,                  
        tool_choice="auto",           
        temperature=0.7
    )
    
    response = llm.invoke(message)  
    return response


##### Qwen-32B #####
def qwen_32b(message: str, tools=None):
    llm = ChatGroq(
        model="qwen/qwen3-32b",
        tools=tools,                  
        tool_choice="auto",           
        temperature=0.7
    )
    
    response = llm.invoke(message)  
    return response

### Kimi-K2-Instruct-0905 ##
def kimik2(message: str, tools=None):
    llm = ChatGroq(
        model="moonshotai/kimi-k2-instruct-0905",
        tools=tools,                  
        tool_choice="auto",           
        temperature=0.7
    )
    
    response = llm.invoke(message)  
    return response
