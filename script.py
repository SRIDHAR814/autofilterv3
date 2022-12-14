class Script(object):
    START_TXT = """๐๐ฒ๐น๐น๐ผ {},

๐ ๐ ๐ป๐ฎ๐บ๐ฒ ๐ถ๐  <a href=https://t.me/{}>{}</a>!
i am ๐๐๐๐ ๐๐๐๐๐๐ ๐๐๐  <a href='https://t.me/sridhar814'>sridhar</a> my boss and you can use me in your groups now.

"""

    HELP_TXT = """Hey {}

<b>Here Is The Help For My Commands.</b>"""

    ABOUT_TXT = """
โญโโโโโโโโโโโโโโโโโโโโโโฃ 
โฃโชผ  แดส ษดแดแดแด: {}
โฃ โชผ แดสแดแดแดแดส: <a href='https://t.me/sridhar814'>sridhar</a>
โฃโชผ สษชสสแดสส: <a href='https://docs.pyrogram.org/'>Pyrogram</a>
โฃโชผ ๐๐๐๐: <a href='https://github.com/ccadmin1/Movie-Bot'>แดสษชแดแด</a>
โฃโชผ แดแดแดแด สแด๊ฑแด: <a href='https://www.mongodb.com/'>MongoDB</a>
โฃโชผ สแดแด ๊ฑแดสแด แดส: <a href='https://heroku.com'>Heroku</a>
โฃโชผ สแดษชสแด ๊ฑแดแดแดแด๊ฑ: v2.0.1 [ Beta ]
โฐโโโโโโโโโโโโโโโโโโโโโโฃ"""

    SOURCE_TXT = """<b>Source:</b>
IMDb is a Open source project.
Source: <a https://github.com/ccadmin1/Movie-Bot'>GitHub - Click here ๐</a>

<b>DEVS:</b>
- <a href='https://t.me/sridhar814'>sridhar</a>

"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - add a filter in chat.
โข /filters - list all the filters of a chat.
โข /del - delete a specific filter in chat.
โข /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code>{fullname}</code>: The user's full name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Replied Message.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - connect a particular chat to your PM.
โข /disconnect  - disconnect from a chat.
โข /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
โข /paste [text] - paste the given text on Pasty
โข /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
โข /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
โข /id - get id of a specified user.
โข /info  - get information about a user.
โข /json - get the json details of a message.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
โข /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข More search tools can be found on inline.
โข Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
โข /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on group.
โข These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
โข /ban - ban a user.
โข /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
โข /mute - mute a user.
โข /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
โข /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on group.
โข These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
โข /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
โข /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works only group.
โข These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - to get the rescent errors.
โข /stats - to get status of files in db.
โข /delete - to delete a specific file from db.
โข /users - to get list of my users and ids.
โข /chats - to get list of the my chats and ids.
โข /leave - to leave from a chat.
โข /disable - do disable a chat.
โข /ban_users - to ban a user.
โข /unban_users - to unban a user.
โข /channel - to get list of total connected channels.
โข /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """
โญโโโโโโโโโโโโโโโโโโโโโโฃ
<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB
โฐโโโโโโโโโโโโโโโโโโโโโโฃ"""


    FORCESUB_TXT = """**
**๐ JOIN THIS CHANNEL & TRY AGAIN ๐**"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
โข /throw or /dart - t๐ m๐บ๐๐พ drat 
โข /roll or /dice - roll the dice 
โข /goal or /shoot - to make a goal or shoot
โข /luck or /cownd - Spin the Lucky
โข /runs strings

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
โข /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
โข /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
โข /song or /mp3 (songname) - download song from yt servers.
โข /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
โข /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
โข /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
โข Only Digits Are Allowed
โข Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
โข /share (text or reply to message)

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup ๐ฅ
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """โYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """๐ฎ Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """โI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

