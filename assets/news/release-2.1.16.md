Slug: release-2.1.16
Title: Version 2.1.16 and website changes
Publish: 2020-02-09 15:55:00+02:00
Visible: True
Author: callaa
---

Version 2.1.16 is now out. This release adds a few new features to the server, a couple of usability improvements and some bug fixes.

Additionally, **there are some changes to the way public session announcements work**. The website sections *Gallery* and *Servers* have been replaced by the new **Communities** section.

The old `drawpile.net` list server and public server are replaced by the new `pub.drawpile.net` server. Enter the server address and click the *Add* button to quickly add it to the list in the join dialog.

All sessions hosted at `pub.drawpile.net` are automatically listed, so there is no need to announce them manually anymore. You can, however, announce sessions hosted at other servers like before. If you're running a server of your own, you can submit it for inclusion on the communities page.

---

Changes in Drawpile version 2.1.16 include:

 * When unexpectedly disconnected from a server, a notification bar is now shown at the top of the screen.
 * Passwords are now stored securely using the platform keychain
 * Selections are now properly clipped to the canvas size
 * Copying or cutting a moved selection now works as expected
 * Fixed brush size adjustment shortcut (needed two presses to adjust)
 * List servers can now be manually sorted
 * The *drawpile.net* list server is no longer included by default

Server improvements include:

 * Added support for ext-auth "trusted" flag
 * Added "last active" timestamp to user list API
 * Added option to ignore ext-auth HOST flag (limits hosting to local accounts only)
 * Changed session ID style from GUID to ULID (filenames now sort by creation time)

With this release out the way, work on the version 2.2 branch can now begin. While I'm not making
any promises yet, I'm exploring some ideas that *might* enable some cool things in the future,
such as the often requested iPad and Web versions.

