Slug: release-2.0.5
Title: Drawpile 2.0.5 Release
Publish: 2017-06-26 19:30:00+03:00
Visible: True
Author: callaa
---

Version 2.0.5 is now out! This release brings many general usability improvements and fixes a few bugs.

Bugs fixed in this release:

 * Fixed flood fill expansion (regression)
 * Fixed concurrency problem in recording playback (controls out of sync with actual playback)
 * Fixed zooming with ctrl+stylus motion
 * Fixed language changing
 * Fixed tool selection when "select all" command was used and the rectangular selection tool was already selected
 * Fixed a bug in the server GUI that could reset server settings

Usability improvements:

 * The number of remembered host addresses is now limited
 * Enter and Esc keys can now be used to end or cancel Bezier curve drawing
 * If a selection exists, undo first undos the selection transformation
 * Improved latency hiding behaviour (avoids blinking strokes while drawing caused by repeated canvas rollbacks)
 * Canvas is now locked on autoreset and a notification chat message is sent
 * Layer selection is now restored after session reset
 * Removed "persistent session" option from the host dialog (this option was misleading since persistence may not be available on the target server. Once a session is started, it can be made persistent via the session settings dialog if the server supports it.)

New features:

 * Added a built-in tablet testing tool
 * Added an option to hide the server address in the status bar
 * Added an option to disable tool toggling shortcut
 * All admin HTTP queries are now logged
 * Added a log file for debug messages

Linux specific fixes:

 * Fixed server build with systemd integration enabled
 * Qt version in AppImage downgraded to 5.6, as tablet hover events are broken in Qt 5.7 and newer

