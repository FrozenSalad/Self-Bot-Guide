# on_modal *event*

### Intro
An event for catching interactions with modals made by the user bot

## Functions

**Disclaimer:**
- **A Modal can only be triggered via an interaction made by the bot and the modal is directed to the user**
    - *You cannot capture other people's modals*
    - *Modals triggered not by an interaction will not be detected, so trying to trigger a modal by hand and getting the bot to do something will not do anything*


#### Initiating a modal for capture:

Let's say we triggered a modal by clicking a button on a bot's message (this is just an example):
```py
#After the component is clicked, a modal interaction should have been triggered     
@bot.event
async def on_modal(modal: discord.Modal):
    #Get the modal.title
    if modal.title == "Say Hello Back!":
        #Use components
        if modal.components:
            for action_row in modal.components:
                for textinput in action_row.children:
                    #Use text input to submit a response in a text box, there's also something for different placeholders in the text box if there are more than one like if textinput.placeholder == ""
                    if isinstance(textinput, discord.TextInput):
                        answer = "Hello"
                        await textinput.answer(answer)
                        #Submit the modal
                        await modal.submit()
                                        
```

**This just uses the discord.Modal *class* so anything goes**