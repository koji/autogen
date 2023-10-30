import autogen

config_list_gpt35 = autogen.config_list_from_json(
     "OAI_CONFIG_LIST",
   file_location=".",
   filter_dict={
       "model": {
           "gpt-3.5-turbo",
       }
   },
)

llm_config = {
   "config_list": config_list_gpt35,
   "seed": 42,
   "request_timeout": 600,
   "temperature": 0.7,
}

agent_a = autogen.AssistantAgent(
   name="Agent-A",
   system_message="",
   llm_config=llm_config,
)
agent_b = autogen.AssistantAgent(
   name="Agent-B",
   system_message="",
   llm_config=llm_config,
)
agent_c = autogen.AssistantAgent(
   name="Agent-C",
   system_message="",
   llm_config=llm_config,
)
agent_d = autogen.AssistantAgent(
   name="Agent-D",
   system_message="",
   llm_config=llm_config,
)
agent_e = autogen.AssistantAgent(
   name="Agent-E",
   system_message="",
   llm_config=llm_config,
)

TOPIC=""

groupchat = autogen.GroupChat(
   agents=[agent_a, agent_b, agent_c, agent_d, agent_e], messages=[], max_round=6
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

manager.initiate_chat(manager, message=TOPIC)
all_messages = manager.chat_messages[agent_a]
