Slug: release-2.2b11
Title: Version 2.2 beta 11
Publish: 2023-12-08 20:00:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2 beta 11 is out, **[download it here!](/download/)**

This version fixes all relevant bugs that were reported. Unless new major bugs are found, this state will become the final release of 2.2.0.

If you still have issues to report, do so now! Take a look at [the help page](/help/) for links to the (new!) web chat, Discord and GitHub.

Translations can also still be updated and added, you can do so over at <a href="https://hosted.weblate.org/engage/drawpile/" target="_blank">Weblate</a>.

## Changes in this Release

This release represents a little less than a month of development. It contains lots of bugfixes and some translation updates.

---

Some of these points link to the development blog, where you can read more about those fixes and features.

* Meta:
    * Drawpile is now on libera.chat, providing a chatroom you can join directly through your browser or any IRC client. <a href="/irc/" target="_blank">Look here for details.</a>.
    * There's now 32 bit releases provided for Windows and Android. This isn't relevant for most people, since most devices have been 64 bit for over a decade, but still nice to have the remaining few included too.
* Community Servers:
    * <a href="/communities/foxdice/" target="_blank">FoxDice Drawpile Group</a> community has been added. They provide multiple public servers in Asian regions. If you're from there, you can use these servers for lower latency.
    * <a href="/communities/sugar-and-spice/" target="_blank">Sugar and Spice</a> community has been added. They provide private hosting, their rules explain how to gain access.
* Features:
    * Add libera.chat link to start dialog. It links to <a href="/irc/" target="_blank">this page</a>.
    * <a href="https://docs.drawpile.net/devblog/2023/11/25/dev-update.html#login-flow-shortcut" target="_blank">Shortcut login flow on servers that only support guest and internal account logins.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/25/dev-update.html#tablet-driving" target="_blank">Allow changing tablet driver through Edit menu on Windows.</a>
    * Add a Tablet Setup link in the start dialog. It links to <a href="https://docs.drawpile.net/help/tech/tablet" target="_blank">this documentation page</a>.
    * Focus the input field on the Join page when switching to it so that you can immediately paste a link without having to click it.
* Fixes:
    * Actually disable brush taking in 2.1 sessions, last attempt didn't stick. Thanks again Blozzom for reporting.
    * Also show mute notifications action when right-clicking the chat. Thanks Blozzom for reporting.
    * Make brush palette less immensely slow. Thanks lowontrash for reporting.
    * Show kick and ban messages in the correct order, without duplicates. Thanks xxxx for reporting.
    * Force the canvas to refresh on resize even harder because some systems still get artifacts. Thanks xxxx for reporting.
    * Default the mouse wheel to pan the canvas on macOS instead of zooming it, since that makes more sense for its two-dimensional scroll wheels. Thanks Charmandrigo for reporting.
    * Make Apple Magic Trackpad and hopefully other touch pads work. Thanks Charmandrigo for reporting and helping figure this out.
    * Add a close button to the tablet tester, playback, event log and flipbook dialogs so that it can be closed on Android and other systems without window decorations without having to press some button or key combination.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#phoning-in" target="_blank">Enable fingerpainting on Android by default if the device doesn't have a stylus.</a>
    * Prefer versioned lconvert executable over unversioned one to make things work on Fedora. Thanks lowontrash for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#noninstall" target="_blank">Look in source directory for assets when building, making running from the build directory possible. Can be turned off with -DSOURCE_ASSETS=OFF.</a> Thanks Meru, lowontrash and probably others for running into issues with this.
    * Make large circles and curves drawn with the circle and curve tool not look all jaggy.
    * Make large rectangles close properly with MyPaint brushes. Thanks haxekhaex2 for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#phoning-in" target="_blank">Allow horizontal scrolling in the preferences dialog so the close button doesn't get thrown off-screen on mobile.</a> Thanks Xkower for reporting.
    * Allow scrolling of preferences and start dialog sidebar.
    * Move preferences dialog sidebar to the top on macOS and to the bottom on Android, to fit better with how those systems work. Thanks Snover and Xkower.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#phoning-in" target="_blank">Make copying and pasting work on Android.</a> Thanks ariqhadiyan for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#phoning-in" target="_blank">Open files in the background to avoid "not responding" warnings.</a> Thanks ariqhadiyan for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/11/18/dev-update.html#phoning-in" target="_blank">Force main window to fit screen on Android whenever the docks change, to avoid spills beyond the edge of the screen.</a> Thanks Xkower for reporting.
    * Don't load ORA files in parallel on Android. This is slower, but avoids the application getting terminated for using too much memory. Thanks ariqhadiyan for reporting.
    * Make keyboard modifiers work better on Android. Thanks ariqhadiyan for reporting.
    * Default Export Image option to export as PNG instead of ORA, because that's what that option is for. Thanks SadColor for reporting.
    * Properly restore avatar again when reconnecting to a session on a 2.1 server. Thanks xxxx for reporting.
    * Make kinetic scrolling work in brush editor categories list.
    * Make canvas rendering not get stuck when switching frames really quickly. Thanks Kink and Hopfel for reporting.
    * Update color swatch when using fill selection, recolor selection and color erase selection.
    * Only update color swatch when using tools that actually put those colors on the canvas.
    * Make color palette swatch select last used color so that it doesn't get stuck when switching brush slots. Thanks Meru for reporting.
    * Make Copy Merged and Copy Without Background from a floating selection work again. Thanks Meru for reporting.
    * Make Export Selection, Copy Merged and Copy Without Background adhere to current view mode. Thanks Bovy for reporting.
    * Make fill tool adhere to current view mode (minus onion skins) when using Merged Image as the source. Thanks Meru for reporting.
    * Don't crash when changing saturation in color dialog when using HSL or LCH color models. Thanks Meru for reporting.
    * Don't deadlock when saving and clearing password fallback.
    * Reset floating selection when filling it to avoid weird effects if the fill is inside the originally selected area. Thanks Meru for reporting.
    * Properly load annotations and timeline from ORA files without a background. Thanks MyaThingoss for reporting.
    * Don't hide dock titlebars when pressing shift when a text field is in focus, since that might hide a field you're currently typing in. Thanks Trite for reporting.
    * Disable Hold Shift to Arrange by default, since it's not needed most of the time.
    * Don't claim every username is taken when connecting to a server with the old login flow doesn't allow guest logins, instead tell the user that they need an account. Thanks Meru for reporting.
    * Give checkbox outlines more contrast, since they're virtually invisible in most themes. This is a patch to Qt.
    * Change italic to bold text, since the former is not readable in Chinese script.
    * Make keep aspect ratio checkbox in resize dialog keep the current aspect ratio, not the original one.
    * Don't act like keep aspect ratio is checked when resizing from a selection. Thanks Meru for reporting.
    * Make onion skin color partially transparent by default so that they don't turn into solid blocks on colored stuff. Thanks BulletPepper for reporting.
    * Clarify the host dialog by adding additional messages that explain common sources of confusion, such as the title being required, disallowing invite links as the title, the password being necessary to host a private session and "host on this computer" requiring port forwarding.
    * Prevent jittering pixels on the canvas at certain zooms and rotations. Thanks Bluestrings, Meru and taiyu for reporting this. Also thanks Meru for actually finding the solution and contributing this fix.
    * Don't reset brush mode when clicking on the freehand tool button from a different tool. Thanks Big Piston for reporting.
    * Render annotations when saving to PNG and JPEG. Thanks chrystalclear and Rykuta for reporting.
    * Don't reset annotation settings to weird values when there's no text. Thanks Blozzom for reporting.
    * When hiding a layer group, indicate that all containing layers are hidden too. Thanks Missile for reporting.
    * Take scroll into account when reordering tracks. Thanks Meru for reporting.
    * Show proper ext-auth URL when prompting for a login. Thanks xxxx for reporting.
    * Properly show server info URL as a clickable link when prompting for a login.
    * Handle view mode changes (frame view, onion skins etc.) properly in drawpile-cmd and drawpile-timelapse tools.
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2023/11/25/dev-update.html#web-admin" target="_blank">The dpwebadmin frontend has been updated for the 2.2 server.</a>
* Server Fixes:
    * No longer show "cannot look up one session and then join another" when joining a session with an ID alias. Thanks Kink and Fabian for finding this.
* Translations:
    * Korean translation created by TapodJointer.
    * German translation updated by askmeaboutloom.
    * Italian translation updated by Bluu.
    * Japanese translation updated by ubanis.
    * Simplified Chinese translation updated by xxxx.

## Acknowledgements

Thanks to everyone reporting issues, providing translations and otherwise helping to make Drawpile better. Thank you to the moderators of the community servers who keep things running.
