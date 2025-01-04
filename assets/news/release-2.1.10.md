Slug: release-2.1.10
Title: Drawpile 2.1.10 release
Publish: 2019-05-30 11:40:00+03:00
Visible: True
Author: callaa
---

Version 2.1.10 is now out. This is a bugfix release with no new features.

The most important change in this version is reduced memory consumption. An error in 2.1.8 ended up causing excessive memory use when joining a large session, which could cause the application to crash when it ran out of memory, especially when using the 32 bit version. This release should fix that and allow the other changes that were added in that version to work properly, leading to even smaller memory footprint than the previous version.

Bugs fixed in 2.1.10:

 * Fixed that settings for the built-in server (such as the default port) were being ignored
 * Fixed that an early undo could clear out the canvas size
 * Fixed excessive memory consumption
 * Fixed canvas jumping when resized by another user
 * Fixed extra messages at the beginning of a session recording
 * Server: fixed that web-admin API HTTP headers were case sensitive


Other changes:

 * Bundled color widgets updated to latest upstream version
 * Application version number is now shown in a tooltip if a session is incompatible

