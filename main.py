from agent import run_agent

while True:
    print(f"\n{'='*50}")
    query = input(f"\nEnter your query (or 'exit' to quit): ")
    print(f"\n{'='*50}")
    if query.lower() == 'exit':
        break
    
    response = run_agent(query)
    print("Agent Response:", response)
    