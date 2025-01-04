Slug: release-2.1.15
Title: Drawpile 2.1.15 release
Publish: 2019-12-07 12:25:00+02:00
Visible: True
Author: callaa
---

Version 2.1.15 is now out. This release primarily contains improvements to the server and a couple
small new features to the client application.

One important new feature is support for "portable" mode. If Drawpile is started with the command line
option `--portable-data-dir PATH`, it will store all its configuration in the given path. This allows you
to copy the entire Drawpile folder to a USB stick and have all your settings travel with it.

Another new feature is related to the upcoming "Communities" section on the website. There is a new
button titled "Add" in the Join dialog. When clicked, Drawpile will try to access `http://SERVER-NAME/`.
If it finds a HTML &lt;meta&gt; tag with the name `drawpile:list-server` and a URL in the content,
Drawpile will add it to the list shown in the dialog.

**Server changes:**

 * Added support for list server API 1.6
 * Added `ext_host` and `ext_port` fields to status API endpoint
 * Abuse report token can now be set via admin API
 * List server whitelist can now be edited via the API
 * Fixed memory leak in admin API
 * The server can now also serve web admin site static files
 * Server-gui: Added "welcome message" field

**Bugfixes and improvements**

 * Drawpile-cmd: OpenRaster export format now works
 * Added command line option to override data and config paths (portable app mode)
 * Added "closed" session list filtering option
 * Added "Add" button to join dialog for adding the server's associated list server

