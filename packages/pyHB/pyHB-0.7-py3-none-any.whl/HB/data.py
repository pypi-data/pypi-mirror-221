from pyrogram.types import (
    InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM)


START_TEXT = """
🙋‍♀ **Hello** {},
Welcome To {},
__This is a Smoothest & Powerful HackBot Made By [Team Legend](https://t.me/TeamLegendXD)__

You can use me to hack anyone account by giving me your Pyrogram V1/Pyrogram V2 Or Teleton.
Use the following Below buttons to know about me.
"""
HELP_TEXT = """
🙋‍♀ **Hey** {},
Help Menu Opened Successfully.

Click Below To Get information how to use.
"""
HOME_BUTTON = IKM([[IKB("⬅️ Back", callback_data="back_button")]])

START_BUTTON = IKM(
    [
        [
            IKB("🧑‍💻 Help Menu ", callback_data="help_menu"),
        ],
        [
            IKB("🙋‍♀ Updates", url="https://t.me/TeamLegendBots"),
            IKB("❤️ Support", url="https://t.me/LegendBot_OP"),
        ],
        [
            IKB("ℹ About Me", callback_data="about_me"),
            IKB("👑 Owner", url="https://t.me/LegendBot_Owner"),
        ],
    ]
)


ABOUT_TEXT = """
This is a Powerful & Advanced Telegram HackBot.
Which is used to Hack Telegram Account By Using his Pyrogram & Telethon session.

Pyrogram ~ [Documents](https://pyrogram.org)
Telethon ~ [Documents](https://docs.telethon.dev/)

             Regarding @TeamLegendXD
"""


HACK_TEXT = """

"A" :~ [Check users groups and channels]

"B" :~ [Check user all information like phone number, username... etc]

"C" :~ [Ban a group {give me StringSession and channel/group username i will ban all members there}]

"D" :~ [Know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]

"E" :~ [Join A Group/Channel via StringSession]

"F" :~ [Leave A Group/Channel via StringSession]

"G" :~ [Delete A Group/Channel]

"H" :~ [Check user two step is eneable or disable]

"I" :~ [Terminate All current active sessions except Your StringSession]

"J" :~ [Delete Account]

"K" :~ [Promote a member in a group/channel]

"L" ~ [Demote user admins in a group/channel]

"M" ~ [Demote all admins in a group/channel]

I will add more features Later 😅
"""


HACK_MODS = IKM(
    [
        [
            IKB("A", callback_data="hack_A"),
            IKB("B", callback_data="hack_B"),
            IKB("C", callback_data="hack_C"),
            IKB("D", callback_data="hack_D"),
            IKB("E", callback_data="hack_E"),
        ],
        [
            IKB("F", callback_data="hack_F"),
            IKB("G", callback_data="hack_G"),
            IKB("H", callback_data="hack_H"),
            IKB("I", callback_data="hack_I"),
            IKB("J", callback_data="hack_J"),
        ],
        [
            IKB("K", callback_data="hack_K"),
            IKB("L", callback_data="hack_L"),
            IKB("M", callback_data="hack_M"),
        ],
    ],
)

INFO_TEXT = """
✘ **Information** :
__Get The All Details About Session__

✘ **OTP** :
__Get the last otp of that session__

✘ **2Step**:
__Check that is two step is enable or not__

✘ **Terminate**:
__Terminate/Log out All Devices of that session except the session login.

✘ **Delete**:
__Delete that account which session you provide me__
"""

INFO_MODS = IKM(
    [
        [
            IKB("Information", callback_data="hack_B"),
            IKB("OTP", callback_data="hack_D"),
        ],
        [
            IKB("2 Step", callback_data="hack_H"),
            IKB("Terminate", callback_data="hack_I"),
        ],
        [
            IKB("Delete Account", callback_data="hack_J"),
        ],
    ],
)


GROUP_TEXT = """
✘ **Channel/Group** :
__Get The All channels/group where thats Session ID is admin__

✘ **Leave all group/channel**:
__Leave all the groups/Channel By giving me that id of session__

✘ **Ban all** :
__Ban all the members of group/channel__
**Note**: Id must be admin there with ban rights

✘ **Unban all**:
__Unban all the member of group/channel__
**Note**: Id must be admin there with ban rights

✘ **Join Channel/Group**:
__Join channel or Group easily__

✘ **Leave Channel/Group**:
__Leave Channel/Group Easily__

✘ **Delete Channel/Group**:
__Delete Channel/Group which you want__

✘ **Promote**:
__Promote anyone by session__
**Note**: Id must be admin there with Promote member rights.

✘ **Demote**:
__Demote anyone by session__
**Note**: Id must be admin there with Promote member rights.

✘ **Demote all**:
__Demote all the member of Group by session__
**Note**: Id must be admin there with Promote member rights.

"""

GROUP_MODS = IKM(
    [
        [
            IKB("Channel/Group", callback_data="hack_A"),
            IKB("Leave all", callback_data="hack_n"),
        ],
        [
            IKB("Ban All", callback_data="hack_c"),
            IKB("Unban All", callback_data="hack_o"),
        ],
        [
            IKB("Join", callback_data="hack_e"),
            IKB("Leave", callback_data="hack_f"),
            IKB("Delete", callback_data="hack_g"),
        ],
        [
            IKB("Promote", callback_data="hack_k"),
            IKB("Demote", callback_data="hack_l"),
            IKB("Demote all", callback_data="hack_m"),
        ],
    ],
)

TWO_STEP_BUTTON = IKM(
    [
        [
            IKB("Set 2 Step", callback_data="hack_ha"),
            IKB("Remove 2 Step", callback_data="hack_hb"),
        ],
    ],
)

TERMINATE_BUTTON = IKM(
    [
        [
            IKB("Other Session", callback_data="hack_ia"),
            IKB("My Session", callback_data="hack_ib"),
        ],
    ],
)

BROADCAST_TEXT = """
✘ **send** :
__This is used to send any personal message by username__

✘ **broadcast** :
__This is used to send message to many Group first you have to use command /savelist__
"""

BROADCAST_BUTTON = IKM(
    [
        [
            IKB("Broadcast", callback_data="hack_p"),
            IKB("Send Message", callback_data="hack_q"),
        ],
    ],
)
