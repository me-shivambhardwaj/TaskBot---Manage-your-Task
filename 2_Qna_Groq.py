from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_exa import ExaSearchResults
from langgraph.prebuilt import create_react_agent  # ✅ correct import
from langgraph.checkpoint.memory import MemorySaver
import os

llm = ChatGroq(model="llama-3.3-70b-versatile")

# ✅ Exa tool (replaces GoogleSerperAPIWrapper)
search_tool = ExaSearchResults(exa_api_key=os.environ["EXA_API_KEY"])

tools = [search_tool]  # ✅ pass the tool object, not search.run

memory = MemorySaver()

agent = create_react_agent(  # ✅ correct function name
    model=llm,
    tools=tools,
    checkpointer=memory,
    prompt="You are an amazing AI agent and can search the web as well"  # ✅ 'prompt' not 'system_prompt'
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "who is President of the US"}]},  # ✅ fixed typo 'mesaages'
    {"configurable": {"thread_id": "1"}},
)

print(response["messages"][-1].content)