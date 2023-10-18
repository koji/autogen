import autogen

config_list = [
    {
        'api_type': 'open_ai',
        'api_base': 'http://localhost:1234/v1',
        'api_key': "NULL"
    }
]


llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}


assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
    # system_message=""
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=20,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved an full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Could you write a python file and then create solution folder and store the code in that folder.
The problem that I want you to solve is below.

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
Run the above FizzBuzz code with 100.
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)
