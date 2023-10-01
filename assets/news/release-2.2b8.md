Slug: release-2.2b8
Title: Version 2.2 beta 8
Publish: 2023-09-30 23:59:59+02:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2 beta 8 is released! **[Download it here.](/download/)**

If you want to report issues or make a suggestion, have a look at the [the help page](/help/).

**Note:** this is currently not available on Android because Google decided to break the toolchain. I'll figure it out.


## Changes in this Release

This release represents about a month of development. The server and the command-line tools have been updated now, which means that hosting on your computer is available again. Also, Drawpile now works on Android phones, rather than just tablets. And of course there's been many smaller features and fixes along the way.

---

Here's all that changed. When there's more information about it and maybe a video or screenshot showing it off, it'll be linked.

* Features:
    * <a href="https://docs.drawpile.net/devblog/2023/09/01/dev-update.html#mark-re-used-key-frames" target="_blank">Draw a hatching pattern on frames in the timeline that are the same as the currently visible one, making it easier to figure out if it's being re-used.</a>
    * Bring back dprectool, the command-line tool that converts Drawpile recordings. It should work mostly the same as it did in Drawpile 2.1.
    * Apply parent folder opacity to frames within it, useful for sketch tracks. Thanks to TeaLord9000 for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/09/09/dev-update.html#small-screen-mode" target="_blank">Add a "small screen" mode, which should make the application usable on phones.</a> Thanks to Verdrusk for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/09/09/dev-update.html#font-size-override" target="_blank">Allow changing the application font size, rather than using the system default that may be garbage, especially on Android.</a> Also Verdrusk's fault.
    * Locking docks now also locks toolbars, rather than still allowing you to move them around on accident.
    * <a href="https://docs.drawpile.net/devblog/2023/09/09/dev-update.html#kinetic-scrolling" target="_blank">Kinetic scrolling. This lets you click/tap/touch scrollable stuff and fling it around instead of using the scroll bars or wheel. Configurable in the preferences.</a> Thanks again Verdrusk.
    * Capture volume rocker on Android and bind it to undo and redo by default. Thanks to cl for suggesting.
    * Add compatibility for Drawpile 2.1's broken indirect mode.
    * Add a setting for the background color behind the canvas. Thanks to Nightshade for suggesting.
    * Let operators create layers beyond the 256 per-user maximum. They will use layers of user 0 first, then 255, 254 etc. Thanks to haxekhaex2 for reporting.
    * Bring back drawpile-cmd, the command-line tool that renders Drawpile recordings to images. Should also mostly work like it did in Drawpile 2.1.
    * <a href="https://docs.drawpile.net/devblog/2023/09/16/dev-update.html#drawpile-timelapse" target="_blank">Implement drawpile-timelapse, a new command-line tool that turns Drawpile recordings into timelapse videos.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/09/23/dev-update.html#builtin-server" target="_blank">Bring back the builtin server, allowing you to host "on this computer" again.</a>
    * Stick ID alias and listing hosting options behind an advanced options checkbox, since they keep causing confusion.
    * <a href="https://docs.drawpile.net/devblog/2023/09/23/dev-update.html#ffmpeg-path-pickage" target="_blank">Allow choosing ffmpeg path on Windows.</a> Thanks xxxx for suggesting.
    * Allow the client to translate server messages, rather than having them always be in English.
    * Show if the current brush is in erase or alpha lock mode in the toolbar and allow resetting it via a click. Thanks Geese for suggesting.
    * Paste in center of the canvas (instead of the center of the view) when the pasted image size is equal to or larger than the canvas size. Thanks Meru for suggesting.
* Fixes:
    * Apply color wheel direction to color dialogs too. Thanks Blozzom for reporting.
    * Don't smoothe the canvas view when at 100% zoom with the canvas rotated at a right angle, since that just blurs it for no reason. Thanks SadColor for reporting.
    * Make flipbook shortcut work while the flipbook is in focus, causing it to refresh its view.
    * Cap flipbook range properly, rather than letting you set a range beyond the last frame.
    * Remove the useless "?" button from dialogs in Windows. Thanks vipperz for reporting.
    * Turn off input event compression, which causes jaggy lines on slow devices.
    * Make flipbook extend the playback range if it was on the last frame and new ones are added to the timeline.
    * Make two-finger zoom and rotation not go completely crazy when the canvas is mirrored or flipped. Thanks BoyOnion for reporting.
    * Don't crash when picking a brush preset on Android. Thanks to zetalambo and VeeBeeArt for reporting.
    * Selections finally no longer sometimes disappear when transforming them. Thanks to Spuzzy, Xan and xxxx for reporting.
    * Make the receive delay not delay your own undos.
    * Make Drawpile 2.1 binary (dprec) recordings play back properly. Text (dptxt) recordings are not supported.
    * Synchronize rendering during recording playback properly.
    * Don't duplicate local fork on soft reset or undo depth change.
    * Make Erase, Divide and Subtract layer modes in ORA files compatible with Krita.
    * Make host page in the start dialog work properly on Arabic and other right-to-left languages.
    * Move brushes to the proper place in MediBang-esque layout. Thanks xxxx for reporting.
    * Replace the reset notice dialog with less disruptive on-canvas messages. If you continue drawing, the notice about saving the previous state will dismiss itself. Thanks to Blozzom, vipperz, xxxx, zheida and probably others for reporting.
    * Make preferences dialog not use custom layouts anymore. Fixes the dialog getting stuck at an unusably tiny size on Windows, makes it work with Arabic and other right-to-left languages and allows resizing the dialog as well as scrolling its contents.
    * Drag-zooming (Ctrl+Middle Click by default) now zooms on the initial click location, rather than the center of the canvas. Thanks to Valaek for reporting.
    * Don't select layer when toggling its visibility.
    * Show a crossed-out folder icon for hidden layer groups, rather than switching to the layer icon for them. Thanks to Blozzom for reporting.
    * Give erase mode its own icon so that it doesn't get confused for the eraser slot. Thanks Geese for reporting.
    * Single-pixel offset when pasting with an existing selection present. Thanks Meru for reporting.
* Server Features:
    * Add --web-admin-allowed-origin option, to set the Access-Control-Allow-Origin header to the given value. Particularly useful for development, where you don't particularly want to set up an nginx to make CORS happy. Thanks Chem for reporting.
    * Update the server to use the 2.2 protocol.
    * Make catchup explicit. Solves both the "stuck at 99%" problem during session resets and the canvas too be unlocked too early.
* Server Fixes:
    * Fix up some invalid casts and thread ownership issues. Not sure if they actually caused issues in practice, but especially on Windows they might have.
* Translations:
    * Arabic translation updated by Arc.
    * Italian translation updated by Bluu.
    * Japanese translation updated by ubanis.
    * Simplified Chinese translation updated by xxxx.
    * Turkish translation updated by duennisss.


## Acknowledgements

Thanks to everyone for reporting and suggesting stuff, they should be attributed above. Also thank you to the translators. And as always a special thanks goes to the moderators that continue to keep things running.

