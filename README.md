#  Project: Microsoft Autogen Multi-Agent System with Local LLM & RAG
## This project will demonstrate how to set up Autogen agents, integrate a local Hugging Face LLM, implement external function calls, and create RAG-based retrieval agents for QA & code suggestions.
# We have to create a small working demo using Microsoft Autogen, a framework for multi-agent AI systems. Here’s a breakdown of what you need to do:
# 1. Use a Local LLM from Hugging Face: Instead of using cloud-based AI models, we need to integrate an open-source LLM (like Llama 2, Mistral, or Falcon) from Hugging Face.
# 2. Set up Two AI Agents
## UserProxy Agent: This acts as a human-like user that interacts with the AI system.
## Assistant Agent: This is an AI that processes requests and provides responses.
# 3. Use External Function Calls
# Your agents should be able to call external Python functions (for example, fetching live weather data, running a mathematical calculation, or querying a database).
# These functions should be mapped properly to the agents' chat workflow.
# 4. Implement RAG (Retrieval-Augmented Generation) for QA & Code
# RetrieveAgents should fetch relevant information for:
## QA (Question Answering): The model should search a knowledge base to answer user questions.
## Code: The model should retrieve relevant code snippets when asked for programming-related help.
