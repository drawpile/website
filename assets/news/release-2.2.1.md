Slug: release-2.2.1
Title: Version 2.2.1
Publish: 2024-02-19 06:00:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2.1 is out. You can **[download it here](/download/)**. If you're updating from an earlier version, simply install the new one over it.

If you're having trouble with it or otherwise need help, take a look at <a href="/help/" target="_blank">the help page</a>. You can find ways to get in touch there, or maybe your question is already documented on a page there.

This release brings a fix to a performance issue that caused slowness for most macOS and some Windows systems with funky graphics drivers. So if 2.2.0 felt choppy for you, this likely fixes it.

There's also experimental support for high-DPI displays now. If you have a display with a very large resolution that causes Drawpile's interface to be way too tiny, you can turn it on <a href="https://docs.drawpile.net/devblog/2024/01/27/dev-update.html#experimental-high-dpi-scaling" target="_blank">in the User Interface tab of the Preferences.</a>

Another significant addition is support for the web browser version of Drawpile. If you're drawing on a server that supports it and the server owner permits it, your session invite links will automatically include a button that lets people join through their browser. In that case, the session settings will also show the option to toggle if you want to allow joining from the browser or not.

Server owners have to set up their servers to enable browser access. How this works is currently still being documented, keep an eye [on the help pages](/help/). The same goes for other documentation, like the stuff that changed between 2.1.20 and 2.2.0. Once that's done to a reasonable degree, the updater in 2.1 will start prompting for automatic updates too.

## Changes in this Release

This release represents about a month of development since Drawpile 2.2.0, with some new features added, many bugs fixed and performance improved.

---

Where appropriate, there'll be links to the development blog entries where you can read more about the fixes and features.

* Community Servers:
    * <a href="/communities/ahaven/" target="_blank">ahaven.net</a> community has been added. They provide US-based hosting with sessions being allowed to idle for up to 48 hours.
    * Session listings at the bottom of the <a href="/communities/" target="_blank">community server pages</a> now tell you if a session lets you join via the web browser and how many people are actively drawing in it. Clicking on the join button will lead you to the invite page for that session.
* Documentation:
    * <a href="https://docs.drawpile.net/help/draw/animation" target="_blank">How to animate with Drawpile</a> has now been written up.
    * A page on <a href="https://docs.drawpile.net/help/development/contributing" target="_blank">how you can contribute to Drawpile</a> has been added. This includes many things that don't require you to know anything about programming. For those that do, there's a description of available topics that could be tackled.
    * <a href="https://docs.drawpile.net/help/draw/floodfill" target="_blank">The flood fill tool</a> now has an entry on the help pages.
    * A document on <a href="https://docs.drawpile.net/help/server/sessionoperation" target="_blank">running public sessions</a> has been written up. Hosting sessions that are open to the public comes with some challenges regarding moderation and permission stuff, this document tries to explain how that works and where the knobs you can twiddle are.
* Features:
    * Implement WebSocket support in the server, available with the --websocket-port and --websocket-listen options.
    * Send keepalive messages from the server, if the client indicates support for it. Avoids them disconnecting when too busy uploading to send a ping.
    * <a href="https://docs.drawpile.net/devblog/2024/01/20/dev-update.html#canvas-performance" target="_blank">Allow toggling performance-related canvas view settings, since some systems get slowdowns.</a> Thanks DevonJP for reporting.
    * Active user counts for sessions. A user counts as active if they drew in the last five minutes.
    * Make invite links indicated web client capability and NSFM-ness of sessions so that the invite page can show a "join in the browser" button and an appropriate notice respectively. Thanks Blozzom for suggesting the latter.
    * Add next and previous key frame actions, allowing skipping between key frames in the current track. Thanks BulletPepper for reporting.
    * <a href="https://docs.drawpile.net/devblog/2024/01/27/dev-update.html#experimental-high-dpi-scaling" target="_blank">Add experimental support for high-DPI interface scaling.</a>
    * Show latency in the status message, next to the session size and cursor coordinates. Thanks Meiren for suggesting.
    * Add action to pick color from screen, default shortcut is Shift+I. Thanks Meru for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/01/27/dev-update.html#eraser-actions" target="_blank">Allow switching the current brush to erase mode when using the tablet pen eraser instead of switching to the eraser tool slot. The setting for this is in the Input settings.</a>
    * Make the Windows installer put a shortcut on the desktop.
    * Show last joined address in join dialog.
    * Add some bulk permission commands for (un)trusting and setting layer tiers, explanation available through /modhelp. Thanks Bluestrings for suggesting.
    * Remember last sorting on the browse page. Thanks Bluestrings and Meiren for suggesting.
    * Fill background for copying the merged image with a non-rectangular selection. Thanks Bluestrings for suggesting.
    * Optimize classic brush calculation, making them a good chunk faster. Thanks kiroma for contributing.
* Fixes:
    * Default to previous directory when saving a fresh file. Thanks Crow for reporting.
    * Don't force TLS socket algorithms, since ECDSA certs seem to not like them. Thanks Bluestrings for reporting.
    * Log message queue read, write and timeout errors properly. Thanks Pepper for reporting.
    * Properly handle cancelling a connection while it's being established. Thanks Fox for reporting.
    * Don't resize brush settings unnecessarily larger when switching between brush types. Thanks Meiren for reporting.
    * Try to handle switching between tablet pen and eraser more consistently. Thanks Daystream for reporting.
    * Properly refer to "layer" and "layer group" in layer actions depending on what is selected. Thanks Momo for reporting.
    * Save censored layers into PSDs properly. Thanks Blozzom for reporting.
    * Don't allow copying, cutting and color picking from censored layers.
    * Rotate brush and fill outline along with the canvas. Thanks Bluestrings for reporting and xxxx for helping solve some issues with it.
    * Don't reset opacity multiply inputs to default when loading a brush that doesn't have it set. Thanks Blozzom for reporting.
    * Limit MyPaint brush dab counts to more sensible values, since the defaults from MyPaint are pointlessly high and can cause chugging. Thanks Blozzom for reporting.
    * Don't blink last user cursors again when making a selection.
    * Make user cursors trail MyPaint brush strokes better, only smoothing it out when there's jitter. Thanks Blozzom for reporting.
    * Widen the stripes of the censor pattern so that it's easier on the eyes. Thanks Ben for reporting.
    * Don't remember uncensor layers across restarts, to avoid being exposed to things you didn't want to just because you forgot to toggle it back off.
    * Properly show censored layers in the list even when they are revealed.
    * Properly apply layer properties if the layer changed since opening them.
    * Hide disconnection banner after establishing connection to a session.
    * Make censoring layer groups actually have an effect.
    * Don't use 64 bit stuff in 32 bit Windows installer.
    * Don't break pinned start menue shortcuts when updating on Windows. Thanks Bluestrings and anonymous for reporting.
    * <a href="https://docs.drawpile.net/devblog/2024/02/03/dev-update.html#optimizing-the-multidab-optimization" target="_blank">Use proper measurements to decide on how much painting to do in a single step, hopefully preventing chugging caused by certain brushes.</a>
    * Don't show user cursors while catchup dialog is open.
    * Don't gray out layer ACL tier settings when a layer is assigned to users exclusively, since those settings are not exclusive.
    * Don't include stuff from before session reset when restarting a recording because of one. Thanks Meiren for reporting.
    * Don't overwrite recordings on Windows if the file names contain non-ASCII symbols. Thanks Meiren for reporting.
    * Make log file on Windows log non-ASCII symbols properly.
    * Don't reorder listing servers when sorting by title in the browse tab.
    * Only ask for confirmation when a self-signed TLS certificate changes, not when a "real" one renews. Thanks Bluestrings and Pepper for reporting.
    * Make bezier curve tool generate smooth curves at small sizes, rather than getting jaggy. Thanks Crow for reporting.
    * Make navigator slider not eat keyboard inputs when navigator is undocked. Thanks anonymousduck for reporting.
    * Disregard hidden frames when rendering animations. Thanks Etide for reporting.
    * Load default settings values after the program has initialized, avoiding crashes that can happen on Windows when building in debug mode. Thanks kiroma for reporting and testing.
* Server Features:
    * Allow limiting the maximum number of users per session. Moderators and administrators can override this.
    * Allow server owners to kick users not connected to a session.
    * Log when a wrong password is entered for server accounts and sessions, disconnect the user after too many wrong tries.
* Server Fixes:
    * Allow reading users' trusted status through the API, because it's something you can write through it.
    * Time out clients that take too long to disconnect gracefully. Thanks Bluestrings for reporting.
    * When hosting without an account is enabled, also allow it for anyone *with* an account. Thanks ahaven for finding this.
    * Don't report temporary server bans as permanent. Thanks Bluestrings for reporting.
    * Properly convert between IPv4 and IPv6 when checking IP bans. Thanks Bluestrings for reporting.
    * Save catchup keys to file-backed sessions so that the counter doesn't reset upon a server restart.
    * Log client host and join attempts even when unsuccessful. Thanks Bluestrings for reporting.

## Acknowledgements

Thanks to all the folks who contributed to this release of Drawpile, be it through code, bug reports, suggestions, requests or helping out other folks. Particular thanks go to the people running and maintaining the public servers, giving people places to draw together.
