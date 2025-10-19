Slug: release-2.3.0-beta.4
Title: Version 2.3.0-beta.4
Publish: 2025-10-19 15:25:00+02:00
Visible: True
Author: askmeaboutloom
---

The next beta version for Drawpile 2.3.0 is out. Unless major issues are found, this is expected to be the last beta before the final release.

That means now good time to give feedback on it if something doesn't work or you don't like any of the changes! Without reports to the contrary, things will not change further.

* **[Click here to download and install it](/download/#Beta)**.
* To find out what changed, <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">take a look at this illustrated guide</a>. It has many pictures and videos to show off the new stuff.
* If you want to keep 2.2 installed, <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">take a look at this page on how to install both versions side by side</a>.
* Consider <a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donating to the project</span></span></a>! Drawpile is developed by one person, donations help spend more time on it and with the cost of keeping the servers running.

If you have questions, feedback or trouble using the new version – especially if it breaks your workflow – take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact! Almost every feature is added because it was requested by an artist and bugs can only be fixed if they are reported, you can see everyone that contributed in the list of changes below.

## Updating or Installing Side by Side

You can **[download Drawpile from here](/download/#Beta)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

Alternatively, you can run both versions side-by-side. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to do that on different operating systems</a>.

As usual, the Android version on F-Droid should get the new version in the coming week or two. Flatpak for Linux should already have it ready.

On the server side, everything is both back- and forward-compatible. Server owners can update if they want, but it's not necessary, people can use any version they wish to host sessions. Upgrading is required to make use of fast reconnects though.

## Changes in this Release

Drawpile 2.3.0-beta.4 represents about 2 months of development since the last version. For an illustrated list of the major changes since 2.2.2, take a look at <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">this page</a>.

Major new features include:

* Better Android and macOS support in general. Support specifically for Android 15 and macOS Tahoe.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#anti-overflow-23-only" target="_blank">Anti-overflow brush filling.</a> Makes brush strokes "stay within the lines" on another layer.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#selection-action-bar-22-compatible" target="_blank">A selection action bar.</a> Lets you know that a selection is active even when it's off-screen and giving you immediate access to deselection and other common actions.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#binary-transform-22-compatible" target="_blank">Binary transform mode.</a> Gives better results than Nearest when transforming artwork with hard edges.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#fast-reconnects-22-compatible" target="_blank">Fast reconnects.</a> You won't have to wait through the catchup from scratch anymore, it instead fast-forwards you to where you left off. This requires the server you're drawing on to be updated.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#more-stable-sockets-22-compatible" target="_blank">More stable sockets.</a> Drawpile will try to use WebSockets if possible and only fall back to raw TCP if that doesn't work, since it reduces interference and blocks from internet providers.
* And of course many features from previous releases, such as <a href="https://docs.drawpile.net/help/common/update2x3x0#layer-clipping-23-only" target="_blank">layer clipping</a>, <a href="https://docs.drawpile.net/help/common/update2x3x0#lasso-fill-tool-22-compatible" target="_blank">lasso fills</a>, <a href="https://docs.drawpile.net/help/common/update2x3x0#oklab-blend-mode-23-only" target="_blank">OKLAB mode</a> and <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">much more</a>.

Also numerous fixes and smaller improvements. Read on for a full list of changes.

---

Where available, there's links to the <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog</a> or <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">changes guide</a> with more information.

* Features:
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#chat-enhancements-22-compatible" target="_blank">Make true /roll messages in chat have a blue tint to make cheating more difficult. They're also translatable now, rather than always being in English.</a> Thanks KosmonautKat, lambda20xx and Potete for suggesting.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#layer-blocking-22-compatible" target="_blank">Allow "blocking" of layers. It works like censoring a layer, but the censor is only visible to you. It lets you hide stuff you don't want to see, but still be aware that it's there so you don't draw over other people's art.</a>
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#anti-overflow-23-only" target="_blank">Anti-overflow fill for brushes.</a> Thanks Ausjamcian, Axocrat and Null for suggesting.
    * Exit Drawpile when the last window is closed on macOS, like on all other systems. You can reenable this behavior in the user interface preferences if you want it back.
    * Allow closing modal dialogs on macOS using Command+Q. Thanks Axocrat for suggesting.
    * Increase/decrease key frame exposure actions for all visible tracks, bound to Ctrl+Shift+Alt+Plus/Minus by default. This lets you shift frames on multiple frames at once, rather than having to move each track individually.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#binary-transform-22-compatible" target="_blank">Binary interpolation mode for transforms. Works like Bilinear, but tries to keep the opacity of pixels the same so that you can scale stuff drawn with a binary brush without making it all blurry.</a> Thanks TGS for suggesting.
    * Don't ask for login method, username and password again when reconnecting. Thanks Meru for reporting.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#chat-enhancements-22-compatible" target="_blank">Don't show chat until connecting to a session and remember the size of it even when it was hidden.</a>
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#chat-enhancements-22-compatible" target="_blank">Send button in chat, for virtual keyboards where hitting return is inconvenient.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/10/12/dev-update.html#user-interfacing" target="_blank">Long-press to open context menus. Enabled by default on Android and in the browser. Can be toggled in the user interface preferences.</a>
    * Higher-quality zoom using the hardware renderer. Thanks cromachina for contributing.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#animation-timeline-additions-23-only" target="_blank">Allow for fractional framerates instead of only allowing whole numbers.</a>
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#animation-timeline-additions-23-only" target="_blank">Make the timeline use a frame range instead of always strictly constraining it from 1 to the maximum frame count and chomping away any frames beyond the end.</a>
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#animation-timeline-additions-23-only" target="_blank">Allow double-clicking on empty timeline frames to create key frames and on the header to edit the framerate and frame range.</a> Thanks Greendyno for suggesting.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#animation-timeline-additions-23-only" target="_blank">Start blank canvases with a single timeline track pre-created, similar to how it works with layers.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/10/12/dev-update.html#forward-compatibility" target="_blank">Allow joining sessions if there's only a minor protocol incompatibility. An outdated client like this won't handle any new features and therefore their canvas may desynchronize, so they can't reset or compress it.</a>
    * Make compiling Drawpile with WebSocket support mandatory. This avoids accidentally ending up with an application that's unable to connect to certain servers.
    * <a href="https://docs.drawpile.net/devblog/2025/10/12/dev-update.html#connection-changes" target="_blank">Allow explicitly picking between WebSockets and TCP sockets in the join, browser and host pages of the start dialog.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/10/12/dev-update.html#connection-changes" target="_blank">Prefer connecting via WebSockets, fall back to TCP if it fails or takes too long. Connections to localhost or IP addresses continue to use TCP by default.</a> Thanks Bluestrings for suggesting.
    * Show connection socket type in the net status field in the bottom-right corner.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#selection-action-bar-22-compatible" target="_blank">Selection and transform action bar. Shows up when a selection or transform is active to give quick access to common operations, such as deselecting or applying the transform.</a> Thanks CosmosX007 and Geese for suggesting, Blozzom for testing.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#better-lock-and-view-mode-status-22-compatible" target="_blank">Add buttons to the lock notice to unlock the canvas, reset the session when it's out of space or uncensor layers.</a> Thanks Phoneme for suggesting.
    * <a href="https://docs.drawpile.net/help/common/update2x3x0#better-lock-and-view-mode-status-22-compatible" target="_blank">Indicate whether a non-normal view mode is active and give a way to get out of it in the lock notice. Can be disabled in the user interface preferences.</a> Thanks Geese for suggesting.
    * Show lock message even when it doesn't affect the current tool (without actually locking anything.)
    * Allow detaching the chat but keeping it on top of the main window or all other windows. Thanks Bluestrings and Blozzom for suggesting.
    * Automatically switch to frame view mode when the animation timeline is sufficiently fiddled with.
* Fixes:
    * Unpremultiply alpha values when exporting to animated WEBP so that partially transparent pixels come out looking correct.
    * Make the preferences menu item on macOS open the preferences again.
    * Make mouse wheel to adjust brush sizes not skip over small values on wheels that make big steps. Thanks Meiren for reporting.
    * Make zoom tool detect clicks properly, rather than detecting tiny motions as a rectangle to zoom into. Thanks Scruff for reporting.
    * Make freehand tool icon appear again if starting up with the eraser selected. Thanks Meiren for reporting.
    * Make software renderers handle canvas sizes with dimensions beyond 32767 pixels properly. Thanks Ben for reporting.
    * Open ORA files with width or height greater than 32767 pixels. Thanks Nimono for reporting.
    * Make layer clipping onto pass-through groups work the same as it does in other programs (that is, make it not clip.)
    * Make clicking with touchpad not trigger touch color picker.
    * Properly enable or disable session permission boxes and sliders according to compatibility mode and operator status.
    * Make key frame visibility attributes work properly in compatibility mode.
    * Disable native message boxes, they're broken on macOS Tahoe and don't add anything except an inconsistent appearance.
    * Make start, login, invite and numerous other dialogs have proper title bars on macOS, rather than being those weird sheets. Thanks Axocrat for reporting.
    * Don't show duplicate full screen action in view menu on macOS.
    * Make window maximized when leaving full screen on macOS, rather than crumpling it down to a small size and messing up the docks arrangement.
    * Properly reconnect to sessions when using an invite code, rather than asking for a password the second time around.
    * Properly reconnect when using a WebSocket URL, rather than replacing the path inappropriately.
    * Don't incorrectly redo already gone undone commands after a series of undos and redos. Thanks Sinamer for reporting.
    * Properly check for session reset size so that oversized resets don't end up in disconnects.
    * Show a proper error message when a manual reset fails, rather than claiming that an auto-reset failed.
    * Handle reordering of layers with large ids properly. This was only a problem in the UI, it does not cause desync. Thanks Bluesflying for reporting.
    * Remove accessibility features, because they cause crashes on macOS and possibly also other operating systems even though Drawpile doesn't use them. This is a patch to Qt. Thanks kal^-^ for reporting.
    * Make sliders less annoying: double-clicking now starts editing instead of clicking and holding, hitting Escape now unfocuses the slider and sliders now no longer block shortcuts keys that wouldn't have any effect on them. Thanks Blozzom and incoheart for reporting.
    * Allow right-clicking on the lasso fill and gradient tools to cancel them even if right-click is bound to a canvas shortcut. Thanks Blozzom for reporting.
    * Reset flipbook crop, speed and frame range when a different canvas is loaded.
    * Clear layer selection when selecting a blank frame. Thanks Pumpkin for reporting.
    * Properly persist changes to blend, alpha preserve and erase modes when they're changed on the brush dock. Thanks cromachina for reporting.
    * Don't disconnect brush shortcuts when changing other shortcuts. Thanks cromachina for reporting.
    * Properly disable join button when an empty address is entered.
    * Make deselect work on identity transforms. Previously it would cancel the transform, but not actually deselect.
    * Properly autoselect default layer on join. Thanks Bluestrings for reporting.
    * Make chat recognize user as operator even when they are for some rason not in the user list. Thanks Bluestrings for reporting.
    * Properly restore chat size when reattaching.
    * Properly save accounts on the web when asked when the server doesn't support browser authentication. Thanks Bluestrings and Evil Sonic for reporting.
    * Don't hang when quickly switching tools while strokes with smudge sync are in progress. Thanks D'mitri for reporting and helping find this.
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2025/09/14/dev-update.html#fast-reconnects" target="_blank">Fast reconnects. Clients now remember the state of the history when they got disconnected and skip ahead in the catchup sequence if possible.</a> Thanks Bluestrings for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/09/28/dev-update.html#server-management" target="_blank">Allow toggling archive mode on individual sessions instead of using server default.</a> Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/09/28/dev-update.html#server-management" target="_blank">Add server setting for a minimum autoreset threshold, to avoid users setting it to a too low value and causing excessive resets.</a> Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/09/28/dev-update.html#server-management" target="_blank">Allow overriding session size limit for individual sessions.</a> Thanks Bluestrings for suggesting.
* Removed Server Feature
    * Socket activation. Attempting to pass sockets via systemd now just raises an error and tells you to uninstall drawpile-srv.socket. This was a pretty obscure feature that apparently wasn't working properly anyway and only ever seems to get used unintentionally. Thanks Bluestrings for reporting.
* Server Fixes:
    * Don't restrict binary (.dprec) templates to the current version.
    * Apply archive and size limit setting immediately, not only when a session is started.
    * Properly treat autoreset threshold with zero value as no autoreset.
* Tool Features:
    * Make drawpile-timelapse command-line tool fill the background with the canvas background color instead of black.
* Tool Fixes:
    * Make drawpile-cmd actually write to stdout when passing "-" as the output file, like the help claims. Thanks incoheart for reporting.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Web Developer.
    * Catalan translation by Roger VC
    * European Portuguese translation by Victor Araújo.
    * German translation by askmeaboutloom.
    * Gothic translation by Roel v.
    * Italian translation by Alabo Battistella
    * Japanese translation by ubanis.
    * Russian translation by anoNIM, Desutorakuta, Karutuna, Puuur, Redbear and XblateX.
    * Spanish translation by Manuart.
    * Turkish translatiion by Nilay.
    * Ukranian translation by Maksim Gorpinic, neketos851 and XblateX.

## Acknowledgements

Thanks to everyone who reported issues, suggested features, tested and donated to Drawpile, and to those who helped out others in the public chats. Also thanks to the folks who keep the public servers running and letting everyone draw there for free.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
