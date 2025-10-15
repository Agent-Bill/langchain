# AgentBill LangChain Integration

Automatic usage tracking and billing for LangChain applications.

[![PyPI version](https://badge.fury.io/py/agentbill-langchain.svg)](https://pypi.org/project/agentbill-langchain/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

Install via pip:

```bash
pip install agentbill-langchain
```

With OpenAI support:
```bash
pip install agentbill-langchain[openai]
```

With Anthropic support:
```bash
pip install agentbill-langchain[anthropic]
```

## Quick Start

```python
from agentbill_langchain import AgentBillCallback
from langchain_openai import ChatOpenAI

# Initialize callback
callback = AgentBillCallback(
    api_key="agb_...",
    base_url="https://your-instance.supabase.co",
    customer_id="customer-123"
)

# Add to LangChain
llm = ChatOpenAI(callbacks=[callback])
result = llm.invoke("Hello!")  # Auto-tracked!
```

For full documentation, visit the [GitHub repository](https://github.com/Agent-Bill/langchain).