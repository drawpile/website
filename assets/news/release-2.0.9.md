Slug: release-2.0.9
Title: Drawpile 2.0.9
Publish: 2018-02-25 12:00:00+02:00
Visible: True
Author: callaa
---
Version 2.0.9 is now out. The main focus of this release is improved graphics tablet support.
If you've been having problems using a graphics tablet with Drawpile, there's a good change
this version will fix them.

Drawpile now uses [Krita's](https://krita.org/) new Windows Ink support code (good news for
all Surface Pro users!), as well as their improved Wintab and XInput2 tablet event handlers.

After updating, remember to try unchecking the "enable bug workarounds" setting. Chances are
you won't need it anymore.

Other fixes in this release:

 * Recordings are now prefiltered. This fixes various recording playback problems.
 * Fixed random duplicate frames in exported animations
 * Reverted the real time color history update feature
 * Active color is now remembered independently of the color history when swapping with X

