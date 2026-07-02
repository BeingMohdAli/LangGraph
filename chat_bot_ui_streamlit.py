{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21dd542f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from chat\n",
    "from langchain_core.messages import HumanMessage\n",
    "\n",
    "# st.session_state -> dict -> \n",
    "CONFIG = {'configurable': {'thread_id': 'thread-1'}}\n",
    "\n",
    "if 'message_history' not in st.session_state:\n",
    "    st.session_state['message_history'] = []\n",
    "\n",
    "# loading the conversation history\n",
    "for message in st.session_state['message_history']:\n",
    "    with st.chat_message(message['role']):\n",
    "        st.text(message['content'])\n",
    "\n",
    "#{'role': 'user', 'content': 'Hi'}\n",
    "#{'role': 'assistant', 'content': 'Hi=ello'}\n",
    "\n",
    "user_input = st.chat_input('Type here')\n",
    "\n",
    "if user_input:\n",
    "\n",
    "    # first add the message to message_history\n",
    "    st.session_state['message_history'].append({'role': 'user', 'content': user_input})\n",
    "    with st.chat_message('user'):\n",
    "        st.text(user_input)\n",
    "\n",
    "    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)\n",
    "    \n",
    "    ai_message = response['messages'][-1].content\n",
    "    # first add the message to message_history\n",
    "    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})\n",
    "    with st.chat_message('assistant'):\n",
    "        st.text(ai_message)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv (3.13.12.final.0)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
