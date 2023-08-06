from pyrogram.types import BotCommand


async def set_bot_cmds(app):
    await app.set_bot_commands(
        [
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Open Help Menu"),
            BotCommand("group", "Open Mods Related Group"),
            BotCommand("info", "Login Related Button"),
            BotCommand("send", "Broadcast & Custom Dm to anyone"),
            BotCommand("savelist", "save the list for use in Broadcast"),
            BotCommand(
                "savesession",
                "Save your session you don't need to send manually session",
            ),
            BotCommand("getsession", "Get your session which has been saved"),
            BotCommand("clearsession", "Clear your session from our database"),
            BotCommand("botstats", "Check how many people has cloned my bot"),
            BotCommand("copy", "Copy this bot easily"),
            BotCommand(
                "clear", "Clear your bot token from our database to stop your bot"
            ),
            BotCommand("cleartoken", "Clear all token from our database"),
            BotCommand(
                "stats", "This is used to check how many person are using this bot"
            ),
            BotCommand("broadcast", "Send Message who has started me"),
            BotCommand("clearusers", "Clear all the users who has started me"),
            BotCommand("hack", "Open Old Menu"),
        ]
    )
