# mutual

A python package to interact with the Mutuai API.

## Installation

Run `pip install mutual` in the project root directory.

### Usage

```python
import mutual

# to get the api_key
print(mutual.api_key)
# to set the api_key
mutual.api_key = "your_api_key"

# CHAT
mutual.api_key = "your_api_key"
for message in mutual.Chat.create("Hello", "seansbot", "Sean"):
    print(message['content'], end='', flush=True)
# OR
for message in mutual.Chat.create("Hello", bot_name="seansbot", username="Sean", prompt="You are a customer assistant for mutual that provides helpful information"):
    print(message['content'], end='', flush=True)

```
## Chat.create(parameters)
```python
# bot_name --> uniquely identifies the bot tied to the api_key account holder
# bot_id --> uniquely identifies the bot accross all bots
# username --> uniquely identifies person interacting with bot

## OPTIONALS
# prompt (str)--> used to add prompts to bot
# prompt_id (str)--> used to add prompts that are available on the database, prompt overrides this
# judge_id (str)--> used to identify judge prompts. leave for default
# judge_message_id (str)--> used to identiy judge messages. leave for default
# error_logs (bool) --> False by default, hides error messages
# multiplayer_memory (bool) --> True by default, allows mulitplayer 
# context_window (int) --> determines context, default 2
```

```python
# CHAT DEMO
for message in mutual.Chat.create_demo("Hello"):
    print(message['content'], end='', flush=True)

# BOT Instance

# uses bot name
alexbot = mutual.create_bot("bot_name") # THIS WILL CREATE A NEW BOT AND IF BOT WITH BOT NAME EXIST WILL RETURN THAT BOT
for message in alexbot.chat("Hey there", "username"):
    print(message['content'], end='', flush=True)

# can create bot instance passing in these values
alexbot = mutual.create_bot(bot_name="alexbot", prompt="You are a customer assistant for mutual that provides helpful information") 

# bot id
alexbot = mutual.fetch_bot("bot_id or bot_name") # THIS WILL LOOK UP FOR A EXISTING BOT AND GENERATE AN INSTANCE OF THAT BOT
for message in alexbot.chat("Hey there", "Sean"):
    print(message['content'], end='', flush=True)

# update using bot instance
alexbot.update_bot(bot_name='new_bot_name', prompt='You are a window cleaner')

# view bot instance data
print(alexbot.api_key) # prints the api_key
print(alexbot.bot_id) # prints the bot id
print(alexbot.bot_name) # prints the bot name
print(alexbot.prompt_id) # prints the prompt id
print(alexbot.judge_id) # prints the judge_id
print(alexbot.judge_message_id) # prints the judge_message_id

# BOT
# using functions
print(mutual.Bot.get_bots())
print(mutual.Bot.get_bots(limit=100, offset=20))
print(mutual.Bot.get_bot("bot_id or bot_name"))
print(mutual.Bot.create_bot("bot_name", "prompt"))
print(mutual.Bot.create_bot("bot_name", "prompt"))
print(mutual.Bot.update_bot(bot_id="bot_id", bot_name="bot_name", prompt_id="prompt_id", judge_id="judge_id", judge_message_id="judge_message_id"))

# you can also set the bot_id like this so you dont need to pass it in chat
mutual.bot_id = "bot_id"

# to print the bot_id
print(mutual.bot_id)

# PROMPT

print(mutual.Prompt.get_prompts())
print(mutual.Prompt.get_prompt("prompt_id"))
print(mutual.Prompt.create_prompt("prompt_id", "prompt"))
# OR
print(mutual.Prompt.create_prompt(prompt_id="prompt_id", prompt="prompt"))
print(mutual.Prompt.update_prompt("prompt_id", prompt="You are an assistant named Hercules."))

# JUDGE
print(mutual.Judge.get_judges())
print(mutual.Judge.get_judge("judge_id"))
print(mutual.Judge.create_judge("judge_id",
    world_prompt=None,
    action_prompt=None,
    judge_convo_aware=None,
    judge=None,
    judgement_lens=None
))
print(mutual.Judge.update_judge("judge_id",
    world_prompt=None,
    action_prompt=None,
    judge_convo_aware=None,
    judge=None,
    judgement_lens=None
))

# JUDGEMESSAGE
print(mutual.JudgeMessage.get_judge_messages())
print(mutual.JudgeMessage.get_judge_message("judge_message_id"))
print(mutual.JudgeMessage.create_judge_message("judge_message_id",
    default_message=None,
    unnatural_lang_message=None,
    manipulation_message=None))
print(mutual.JudgeMessage.update_judge_message("judge_message_id",
    default_message=None,
    unnatural_lang_message=None,
    manipulation_message=None))

# DEV
response = mutual.Dev.clear("bot_id") # clears memories

# APIKey naming
response = mutual.APIKey.update_api_key("new_api_key_name")
print(response.get("prev_api_key_name", None))
print(response.get("new_api_key_name", None))
print(response.get("api_key", None))

# you can import the functions directly like so
from mutual import Bot, Chat, Dev, Prompt, Judge, JudgeMessage, APIKey
```

# SAMPLE TO PRINT ERRORS
```py
index = 0
for message in mutual.Chat.create_demo("Hello"):
    if index == 0:
        print(message['data']['bot_data']['bot_id'], end='', flush=True)
        print(message['data']['user_data']['username'], end='', flush=True)
        print(message['data']['bot_data']['bot_name'], end='', flush=True)
    index += 1
    print(message['content'], end='', flush=True)
```

# SAMPLE TO PRINT DATA
```py
for message in mutual.Chat.create_demo("Hello"):
    print(message['content'], end='', flush=True)
```

# FLOW EXAMPLE
```py
alexbot = mutual.create_bot("AlexbBot2",prompt="You are a customer assistant for mutual that provides helpful information")
for message in alexbot.chat("hello", username="Alex", flow=True):
    print(message['content'], end='', flush=True)
```
