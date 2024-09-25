# disord.Modal *class*

### Intro
Utilization of the discord.Modal *class*, this will utilize other classes like components

## Functions
**For a Modal to be captured it must be triggered by an interaction**
 
#### **Examples:**
```py
# This'll use the on_modal event to show it's functionality

@bot.event'
async def on_modal(modal: discord.Modal):
    # Showing some attributes
    if modal.title == "Whatever":
        print()
    
    if modal.custom_id == "Whatever":
        print()


    # Utilizing modal.submit() / modal.components / discord.TextInput

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
                #If more than one text box
                for action_row in modal.components:
                    for input in action_row.children:
                        if isinstance(input, discord.TextInput):
                            if input.label == "Box 1":
                                input.answer("Whatever1")
                            
                            elif input.label == "Box 2":
                                input.answer("Whatever2")
                        
                        await modal.submit()

                    #For selection menus in modals
                    for menu in action_row.children:
                        if isinstance(menu, discord.SelectMenu):
                            for option in menu.options:
                                if option.label = "Choose Me!":
                                    await menu.choose()
                                    await modal.submit
```
