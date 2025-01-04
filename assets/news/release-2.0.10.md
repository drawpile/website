Slug: release-2.0.10
Title: Drawpile 2.0.10
Publish: 2018-03-17 18:00:00+02:00
Visible: True
Author: callaa
---
Version 2.0.10 is now out. This is a minor bugfix release.

Changes in this version are:

 * Server: improved protection against data loss if server is terminated abruptly
 * Wintab relative tablet mode (mouse mode) hack must now be enabled explicitly, since it can cause glitches for normal tablet users
 * Removed tablet bug workaround mode (no longer necessary with the improved tablet event handlers. It now cause more problems than it fixes.)
 * Bugfix: creating layers with duplicate IDs is no longer possible
 * Bug workaround: the server now autokicks a user who is de-opped while resetting to prevent the reset image from garbling the session
 * Server: added a new option for automatically clearing database log history
 * Fixed crash when replacing current canvas with a new one while a selection existed
 * macOS version is now built with an older Qt version to restore support for older OSX versions

