"""Basic LangChain + AgentBill example"""

from agentbill_langchain import AgentBillCallback
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# 1. Initialize AgentBill callback
callback = AgentBillCallback(
    api_key="agb_your_api_key_here",  # Replace with your actual API key from dashboard
    base_url="https://bgwyprqxtdreuutzpbgw.supabase.co",
    customer_id="customer-demo-123",
    debug=True  # See what's being tracked
)

# 2. Create LangChain components
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

prompt = PromptTemplate.from_template(
    "You are a helpful assistant. {question}"
)

chain = LLMChain(llm=llm, prompt=prompt)

# 3. Run with callback - everything auto-tracked!
print("Running LangChain with AgentBill tracking...")
result = chain.invoke(
    {"question": "What is 2+2? Explain step by step."},
    config={"callbacks": [callback]}
)

print("\nResult:", result["text"])

# 4. Track revenue for profitability
callback.track_revenue(
    event_name="chat_completion",
    revenue=0.10,  # What you charged the customer
    metadata={"subscription": "pro", "feature": "chat"}
)

# 5. Flush any remaining signals
callback.flush()

print("\n✅ Complete! Check your AgentBill dashboard for:")
print("  - Token usage (prompt + completion)")
print("  - Model costs (auto-calculated)")
print("  - Latency metrics")
print("  - Prompt profitability (cost vs revenue)")