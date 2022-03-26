from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.
 
Use the buttons below to learn more!

By @CodeWorld360
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/codeworld360/23")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing Bots ♥", url="https://t.me/codeworld360")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/scripthelper360")],
    ]

    # Help Message
    HELP = """
1) Add me as "Admin" to a group.
 
2) Add me to the particular chat as "Admin" where you want to force your users to join. It can be any group or channel, public or private.
 
3) To activate me, type /fsub "chat_id" or "username" . Use /id if you need a chat id.
Example: /fsub-1001680664179 or /forcesubscribe-1001574595767
 
4) [Optional] Use /settings to change settings!
 
5) You are now all set to go. Leave the rest to me.

✨ **Available Commands** ✨

/fsub - See the current force subscribe chat for more information.
/fsub chat_id/username - Force users to join the particular chat.
/settings - Change Group Settings.
/id - Get the chat id of any group or channel.
/about - About The Bot.
/help - I am ready to help you.
/start - Start the Bot.

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribing bot by @CodeWorld360

Source Code : [Click Here](https://github.com/ScriptHelper/ForceSub_2.0Bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @TGBDeveloper
    """
