Slug: release-2.0.7
Title: Drawpile 2.0.7 Release
Publish: 2018-01-26 18:10:00+02:00
Visible: True
Author: callaa
---

Version 2.0.7 is now out, a bit earlier than intended. This release fixes a couple
serious bugs introduced in the [2.0.6 release](/news/release-2.0.6) and adds some feature
improvements too.

Regression fixes:

 * Windows specific: Fixed a missing DLL that resulted in a Windows 95 UI style
 * Fixed that you couldn't enter a password protected session after logging in with a registered user account
 * Fixed duplicate colors in the color history palette
 * Fixed flipbook downscaling

New features:

 * Added a "remember my password" feature. Makes using registered accounts much easier!
 * Flipbook now upscales if the canvas or cropped area is very small
 * The "show password protected sessions" checkbox now retains its state

Other bug fixes:

 * Fixed that paste & area fill could be done on a locked layer (locally, did not affect other users)
 * Improved selection scaling behavior. Proportional scaling mode now maintains aspect ratio correctly.

