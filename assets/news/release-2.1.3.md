Slug: release-2.1.3
Title: Drawpile 2.1.3 release
Publish: 2019-03-16 12:00:00+02:00
Visible: True
Author: callaa
---

Version 2.1.3 is now out, the second stable release of the 2.1 series.

Feature changes in this release are:

 * Righthand side of the viewport is now indicated in the navigator when the view is rotated
 * Navigator now only shows the canvas pixel content. User cursors and other decorations are no longer shown. To improve general drawing performance, navigator refresh rate is capped to 2 updates per second.
 * Chatbox is now restored to 2.0.0 style, but there is now an option to enable a 2.0 style mode. (Right click on chatbox and select *compat mode*)
 * Added inspector tool. [Read more here.](https://drawpile-dev-diary.tumblr.com/post/183452691227/canvas-inspector-tool)
 * Added a users tab to the server log dialog. All users, including those who have logged out, are listed there. The undo/redo and ban commands can be used on logged out users as well.
 * Server change: added support for banning users who have logged out

Bugs fixed:

 * Fixed showing layers in user cursors
 * Fixed crash when changing tools mid-stroke
 * Open/save dialogs now remember the last used folder

