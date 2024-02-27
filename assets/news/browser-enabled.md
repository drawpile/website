Slug: browser-enabled
Title: Drawpile in the Browser
Publish: 2024-02-27 17:30:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile's web browser version is still in development, but it's working and usable at this point. It's been enabled on [pub.drawpile.net](/communities/drawpile/) for sessions with a password. Sessions without a password do not allow it at this time.

There's also other communities that let you host sessions accessible via the browser, take a look at [the communities page](/communities/) the see which ones do!

---

## Usage

Invite links will automatically include a button to join via web browser if appropriate. When you host a session, Drawpile will automatically prompt you to copy the invite link. If you closed that dialog, you can get it back through Session → Invite or using the Invite button above the user list in the chat.

You have to use at Drawpile version 2.2.1 or later for it to give you such an invite link. You can find your version under Help → About Drawpile. If it's too old, head to [the download page](/download/) to grab a more recent one.

If you run into problems or find a bug with the browser version take a look at [the help page](/help/) on how to get in contact or report it!

## Server Setup

If you have your own dedicated Drawpile server, you can enable web browser support on it. You only need to do this if you have your own *server*, it's not if you just want to host a *session*! If you're not sure if you have your own server: you don't.

Updating drawpile-srv to least version 2.2.1 and [follow the instructions on the WebSocket server setup](https://docs.drawpile.net/help/server/websocket). The [the all-in-one Docker setup](https://github.com/drawpile/dpserver/) includes the WebSocket configuration in the most recent version, so if you update that, you'll get it automatically.

If you're having trouble getting this working, refer to [the help page](/help/) on how to get in contact.

The web browser version is not available if you're hosting "on this computer", it requires a properly set-up dedicated server.
