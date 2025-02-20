#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template, jsonify
 from autogen import AssistantAgent

 app = Flask(__name__)

 # Initialize your AutoGen AssistantAgent
 assistant = AssistantAgent(
     name="Assistant",
     system_prompt="You are a helpful assistant.",
     model="gpt-3.5-turbo"  # Replace with your model
 )

 @app.route('/')
 def index():
     return render_template('index.html')

 @app.route('/chat', methods=['POST'])
 def chat():
     user_input = request.json.get('message')
     response = assistant.chat(user_input)
     return jsonify({'response': response})

 if __name__ == '__main__':
     app.run(debug=True)

