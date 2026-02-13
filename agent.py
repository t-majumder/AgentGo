import json
from llm_call import gpt_oss_120b
import tools

TOOL_SCHEMAS = [
{
    "type": "function",
    "function":{
        "name": "wikipedia_search", 
        "description": "Search website Wikipedia to get information about a topic.", 
        "parameters": {
            "type": "object",
            "properties":{
                "query":{"type": "string"}
            },
            "required": ["query"]
        }
        
    }
},
{
    "type": "function",
    "function":{
        "name": "web_search", 
        "description": "Search the web to get information about a topic.", 
        "parameters": {
            "type": "object",
            "properties":{
                "query":{"type": "string"}
            },
            "required": ["query"]
        }
        
    }
},
{
    "type": "function",
    "function":{
        "name": "web_scraper", 
        "description": "Scrape the web page for relevant information by choosing best URL from the websearch tool op and llm.", 
        "parameters": {
            "type": "object",
            "properties":{
                "query":{"type": "string"}
            },
            "required": ["query"]
        }
        
    }
},
{
    "type": "function",
    "function":{
        "name": "calculator", 
        "description": "Perform mathematical calculations given an expression.", 
        "parameters": {
            "type": "object",
            "properties":{
                "expression":{"type": "string"}
            },
            "required": ["expression"]
        }
        
    }
},
{
    "type": "function",
    "function":{
        "name": "current_time", 
        "description": "Get the current time.", 
        "parameters": {
            "type": "object",
            "properties":{},
            "required": [],
            }
        }
    }
]

# Defining the set of tools available to the agent
TOOL_FUNCTIONS = {
    "wikipedia_search": tools.wikipedia_search,
    "web_search": tools.web_search,
    "web_scraper": tools.web_scraper,
    "calculator": tools.calculator,
    "current_time": tools.current_time
}

import json

def run_agent(user_input: str) -> str:
    messages = [
        {"role": "system", "content": "You are an intelligent agent that can use tools to assist with user queries."},
        {"role": "user", "content": user_input},
    ]
    
    max_iterations = 15  # Prevent infinite loops
    
    for iteration in range(max_iterations):
        response = gpt_oss_120b(messages, tools=TOOL_SCHEMAS)
        print(f"\n--- Iteration {iteration + 1} ---")

        if hasattr(response, 'tool_calls') and response.tool_calls:
            # Add assistant message to history
            messages.append({
                "role": "assistant",
                "content": response.content or "",
                "tool_calls": response.tool_calls  # Already in correct format
            })
            
            # Execute each tool call
            for tool_call in response.tool_calls:
                tool_name = tool_call['name']
                args = tool_call['args']
                
                args = {k: v for k, v in args.items() if k}
                
                print(f"Calling tool: {tool_name} with arguments: {args}")
                
                # Execute the tool
                result = TOOL_FUNCTIONS[tool_name](**args)
                print(f"Tool result: {result[:200] if len(str(result)) > 200 else result}")
                
                # Add tool result to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call['id'],
                    "name": tool_name,
                    "content": str(result)
                })
            continue
        return response.content if hasattr(response, 'content') else str(response)
    
    return "Maximum iterations reached. Unable to complete the request."