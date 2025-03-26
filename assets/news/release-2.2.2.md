Slug: release-2.2.2
Title: Version 2.2.2
Publish: 2025-03-26 09:40:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile version 2.2.2 is out now. It brings numerous new features, fixes and performance improvements.

* **[Click here to download and install the new version](/download/)**. You just install the new Drawpile over the old one to update.

* For an overview of all the stuff that changed, <a href="https://docs.drawpile.net/help/common/update2x2x2" target="_blank">take a look at this illustrated guide</a>. It's got a bunch of videos and pictures showing off the new features.

*  If you have trouble installing, problems or questions with the new version take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact.

This version is **fully compatible** with the previous one. You can continue to draw with anyone that's using the previous version. If you're already on the latest beta version, not much has changed, but there's still been a few more bugfixes in there that you'll probably want to update anyway.

## How to Update

Go to [the downloads page](/download/), download the new version and install it. This will update Drawpile.

If you're getting Drawpile via F-Droid on Android or Flatpak on Linux, you'll get the updated version as normal once those platforms have it available.

Server owners should update their servers by upgrading their containers when using Docker or grabbing the new version and replacing the old one by hand.

## Changes in this Release

Drawpile 2.2.2 represents just over a year of development since version 2.2.1. Much work and testing has gone into it to make sure that it's stable. If you find any problems anyway, please <a href="/help/" target="_blank">report them</a>!

For an illustrated list of the major changes, take a look at <a href="https://docs.drawpile.net/help/common/update2x2x2" target="_blank">this page</a>. But in short:

* Disruptive session autoresets are gone. The canvas now gets compressed on the fly instead.
* Tablet support has been much improved and many problems with weird tablet drivers worked around.
* Touch gestures have been added: two-finger tap to undo, three-finger tap to redo, one-finger tap and hold to summon a color picker.
* Selections and transforms are now much better. There's now a magic wand tool too.
* You can now select multiple layers to rearrange, group, move or transform them all at once.
* Brushes now remember changes automatically, you can assign shortcuts directly to brushes and can change the number of brush slots.
* The fill tool no longer has a size limit by default, it instead previews fills for you only to avoid "flashbanging" other people.
* You can now export animations in MP4, WEBM and animated WEBP formats, the GIF export has also been improved. You can also import animations from separate frames or the layers of PSD files now.
* Over 100 bugs were fixed and performance has been much improved.

For a full list of changes, since the last beta release, read on below. To see the changes since 2.2.1, take a look at the announcements of <a href="/news/release-2.2.2-beta.3/" target="_blank">the first</a>, <a href="/news/release-2.2.2-beta.4/" target="_blank">the second</a> and <a href="/news/release-2.2.2-beta.5/" target="_blank">the third</a> 2.2.2 betas.

---

Where available, there's links to <a href="https://docs.drawpile.net/devblog/" target="_blank">the development blog</a> with more information.

* Documentation:
    * A <a href="https://docs.drawpile.net/help/common/update2x2x2" target="_blank">What's New in 2.2.2 page</a>, illustrating the changes in version 2.2.2.
    * A guide on <a href="https://docs.drawpile.net/help/draw/mypaint" target="_blank">MyPaint Brush Settings</a>. Thanks Blozzom for contributing.
    * Various <a href="https://docs.drawpile.net/help/" target="_blank">help articles</a> were updated for 2.2.2, mostly with regards to updating screenshots and such.
* Features:
    * Make reset images a bit smaller and much faster. This speeds up manual session resets, canvas compression, hosting and joins in the builtin server. Thanks mukihyena for reporting.
    * Indicate when you have no layer selected so that it doesn't seem like you can draw but nothing happens.
    * Allow hiding the color history swatches on individual color docks. Thanks Stickly for suggesting.
    * Allow making the application full-screen in the browser, using View > Full Screen. Thanks Windy for suggesting.
    * Add constrain and center buttons to the transform tool, for the equivalent of holding Shift and Alt when you don't have a keyboard. Thanks MachKerman for suggesting.
    * Set user agent header when connecting via WebSocket using the client. Thanks Meru for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/03/15/dev-update.html#preferred-sockets" target="_blank">Allow adding a "w" query parameter to session URLs to connect via WebSocket instead.</a> Thanks IZUHU for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/03/15/dev-update.html#browser-language" target="_blank">Allow setting the language in the web version using a query parameter.</a> Many languages don't work properly, but this allows setting it before starting the thing and then having to change it.
* Fixes:
    * Make annotations not cause glitches when moving them around when using the software renderer. Thanks Meru for reporting.
    * <a href="https://docs.drawpile.net/devblog/2025/02/16/dev-update.html#going-on-safari" target="_blank">Work around WebKit bug 284752 that prevents Drawpile from working on Safari 18.</a> Thanks grimsley for reporting.
    * Correct weird letter spacing in the font rendering on Windows. Thanks Sinamer for reporting.
    * Generate the catchup image in the background when hosting on the builtin server, rather than hanging the client. Thanks mukihyena for reporting.
    * Slightly delay restoring dock layouts after the window is resized to avoid a crash on macOS. Thanks Axocrat for reporting.
    * Properly update the checkbox on View > Full Screen if the OS forces the application out of it. Thanks Sinamer for reporting.
    * Restore window maximized after exiting the application from full screen mode. Thanks Sinamer for reporting.
    * Only remember dock sizes when the window is maximized or full screen on operating systems where that's possible to tell. Thanks Meiren for reporting.
    * Make tablet positions work on Cintiqs under Windows Ink with UI scaling and when it's not set to be the primary monitor. The old behavior is available via Edit > Tablet Driver > Windows Ink Non-Native, in case this breaks something else. Thanks Axocrat and Liz for reporting, Weenifer for reporting and testing, Maffi for reporting additional issues.
    * Remove the "KisTablet" prefix from the tablet driver names in Windows, it's a technical name that doesn't add anything useful.
    * Show current tier in the layer permissions menu again. Thanks Meiren for reporting.
    * Reduce selection outline resolution instead of punting to the blue selection mask when it gets too large. Thanks Meru, MorrowShore and Shane for reporting.
    * Change temporary tool switch setting text to say that only the primary shortcut will cause it. This was unintentional, but it's useful. Thanks 3rd_EFNO for reporting.
    * Use proper background images in Windows installer instead of those ugly red discs. Thanks evilTriangle for reporting.
    * Correct intermittent errors when connecting, reconnecting or otherwise opening a new main view in the browser that could hang the application.
    * Make pan, zoom, inspector and color picker tools not get locked by the session catching up or resetting. Thanks Greendyno for reporting.
    * Don't show canvas during catchup when using software renderer.
    * Fix keyboard shortcuts, enter and backspace not reacting on some devices in the browser. Thanks Greendyno for reporting.
    * Keep leading spaces and zeroes the same when creating or duplicating a layer. Thanks Greendyno for reporting.
    * Make user markers not leave streaks in the software renderer when fractional UI scaling is involved. Thanks lambda20xx for reporting.
    * Don't crash on invalid certificates when connecting via WebSocket. Thanks IZUHU for reporting.
    * Remember whether a host was connected to via WebSocket by adding the "w" query parameter to it.
    * Don't reset reference dock position when toggling dock visibility. Thanks izzy for reporting.
    * Remove language selection in the web version for now, since it doesn't do anything. Thanks Albano Battistella for reporting.
    * Show and select existing track title when renaming it. Thanks Greendyno for reporting.
    * Properly resize login dialog on Android when showing session listings so that you can actually read something.
    * Don't make kinetic touch scrolling jerk around when moving the finger over the scroll bar.
    * Properly linkify URLs with an @ in the path.
    * Default kinetic scroll on Android and the browser to left-click, since that works better and also covers touch.
    * Allow dragging layers and sliding across the checkboxes in the layer list even when kinetic scrolling with left-click or touch is enabled by making the left and right areas not react to scroll. This is a patch to Qt.
    * Work around a crash on Windows when toggling kinetic scroll settings.
    * Properly show current layout on first layouts dialog run. Thanks Dib for reporting.
    * Deduplicate brush and tag names when exporting brushes. Thanks Blozzom for reporting.
    * Don't crash under Windows 7 when attempting to play two sounds once. Thanks pachuco for reporting.
* Tool Features:
    * Add -u/--users parameter to dprectool, which will print out a table of user statistics along with names and ids.
    * Add --include-user-ids parameter to dprectool, allowing to pass a comma-separated list of user ids to only include visual changes from.
    * Add -i/--image option to the drawpile-cmd command, to allow e.g. converting an ORA to a PNG file or similar on the command line.
    * Add PSD and WEBP format support to the drawpile-cmd command.
* Tool Fixes:
    * Disable image reader limit in command-line tools under Qt6.
* Server Features:
    * Add a separate permission for hosting via browser and whether to take this permission from ext-auth. This also fixes the issue where it would ask you to log in when trying to host from the browser, just to then tell you that you're not allowed to do so anyway. Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/03/01/dev-update.html#invite-codes" target="_blank">Invite codes, allowing inviting people with revokable links that override regular session restrictions.</a> Thanks Bluestrings and Liz for suggesting.
    * Add a "prefer WebSockets" option. Clients will generate appropriate invite links and announcements will contain this preference.
* Server Fix:
    * Additional checks and logging to avoid and diagnose temporary failures in streamed resets. Thanks Will for reporting.
    * Remove browser users when a session's password is removed and the server only allows browsers in passworded sessions. Thanks Bluestrings for reporting.
    * Allow refreshing external bans even when the section is locked. Thanks Bluestrings for reporting.
* Removed Features:
    * Toggling between web and direct links in the invite dialog. Drawpile will translate the web link if you paste it into the join dialog anyway, so the distinction was pointless.
    * Username lists in external session announcements. They were never used.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Blozzom.
    * Dutch translation by Zepho.
    * European Portuguese translation by Victor Araújo.
    * French translation by Skye Wilson and Nicolas Rivard.
    * German translation by askmeaboutloom.
    * Italian translation by Albano Battistella.
    * Japanese translation by ubanis.
    * Simplified Chinese translation by xxxx and wcxu21.
    * Spanish translation by mg729, Tomás Lobo and Traveller Manu.
    * Turkish translation by Bora Atıcı.
    * Ukranian translation by Maksim Gorpinic and neketos851.
    * Vietnamese translation by BlackFire123654 and Cas Pascal.

## What's Next

Development isn't stopping here of course, there's already several more features at the ready for a 2.3.0 release that couldn't be included yet for compatibility reasons.

There's also some work going into a new canvas file format, which is going pretty well. It's around 3000% (that's not a typo, it's three thousand percent) faster to save and load than ORA, while giving smaller file sizes to boot.

If you want to keep tabs on Drawpile's development, you can check out <a href="https://docs.drawpile.net/devblog/" target="_blank">the development blog</a>, where updates are usually posted every one or two weeks, depending on how much has been going on.

## Acknowledgements

Thanks to everyone that helped test things, reported issues, suggested features and otherwise contributed to Drawpile's development. Thanks to the moderators and community administrators that keep the public servers running.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
