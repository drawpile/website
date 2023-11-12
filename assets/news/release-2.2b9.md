Slug: release-2.2b9
Title: Version 2.2 beta 9
Publish: 2023-11-11 20:30:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2 beta 9 is out now! **[Download it here.](/download/)**

**Update:** There was a problem with Drawpile not starting if it was the first time you ran it. This is fixed in [2.2 beta 10](/news/release-2.2b9/)!

This version is a release candidate. That means no new features are expected to be added to it until the final release, but bugfixes and translations may.

That means if you have any bugs to report or stuff that's still missing for you to work properly, now is the time to report them so that they can get handled before Drawpile comes out of beta! Have a look at [the help page](/help/) on how to report things.

## Changes in this Release

This release represents about a month and a half of development. Among many other things, support for PSD files has been added, the animation tools have received some more improvements and the sound effects have been changed to something less terrifying. The server side has also been upgraded with a variety of features to improve hosting long-term sessions, make moderation easier and hopefully reduce confusion around the login process.

The full set of changes is listed below, along with links to the development blog article that talks about it, if applicable.

---

* Features:
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#jaggy-line-compensation" target="_blank">Interpolate inputs that are far away from each other to compensate against fast strokes producing jagged curves. Can be disabled in the input preferences.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#psd-file-support" target="_blank">Support reading and writing Photoshop Document (PSD) files.</a> Thanks pachuco, onyx, Geese and probably others for suggesting. Thanks xxxx for helping getting it compatible with other software.
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#brush-preset-thumbnail-textery" target="_blank">Allow adding labels onto brush preset thumbnails.</a> Thanks Paris Green for causing this.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#export-image-option" target="_blank">Allow exporting images, which saves them without setting the current file or warning about the image being merged together.</a>
    * Disable selection-dependent menu items (Deselect, Fill Selection etc.) when no selection is present.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#notification-cleanup" target="_blank">In addition to sounds, allow configuring popup bubbles and task bar flashing in notification preferences.</a> Thanks MagicaJaphet and Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#notification-cleanup" target="_blank">Add a notification for unexpected disconnects.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#notification-cleanup" target="_blank">Allow configuring notifications for private messages separately from regular chat messages. Mentions can be configured to use these notifications, allowing silencing of regular chat, but still being notified or stuff directed at you.</a> Thanks leandro2222 for suggesting.
    * Store alpha preserve state of layers in ORA files for better Krita compatibility (requires Krita 5.2.1 or newer.)
    * <a href="https://docs.drawpile.net/devblog/2023/10/29/dev-update.html#onion-skin-wrap" target="_blank">Allow onion skins to wrap around the timeline, toggleable in the onion skins dock.</a> Thanks Hopfel for suggesting.
    * Fill the brush slots with nicer default values on first startup, rather than them all being the same pixel brush.
    * Translate a single-colored bottom layer into background color when loading ORA and PSD files.
    * <a href="https://docs.drawpile.net/devblog/2023/10/29/dev-update.html#drawpile-21-animation-import" target="_blank">Drawpile 2.1 animation import.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/05/dev-update.html#account-rememberage" target="_blank">Remember accounts, not just passwords. Should reduce the clicks and typing needed to log in even if you use multiple accounts.</a>
    * Allow toggling whole tile marking in the inspector, since it makes some things easier to see.
    * <a href="https://docs.drawpile.net/devblog/2023/11/05/dev-update.html#flipbook-improvements" target="_blank">Render flipbook frames in the background and indicate that fact with a loading spinner. It no longer lags the UI and gets done faster because of multithreading.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/05/dev-update.html#flipbook-improvements" target="_blank">Crop flipbook when a selection is present upon opening it.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/05/dev-update.html#flipbook-improvements" target="_blank">Make the flipbook UI clearer. The buttons now look like buttons, the uncrop button has a better icon and only shows while the view is cropped and the speed slider shows how many FPS you're actually running at.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#classic-brush-dynamics" target="_blank">Add velocity and distance dynamics to classic brushes. Similar to how they worked for the input settings before, but more flexible than just a pressure mapping.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#brush-sharing" target="_blank">Allow grabbing the current brush settings of another user.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#touch-tester" target="_blank">Add touch tester, available under the Help menu.</a>
* Fixes:
    * Allow indirect mode in 2.1 sessions when opacity dynamics are disabled. Thanks to Blozzom for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#lch-color-wheel-correction" target="_blank">Make LCH color wheel circle not look so bright and discontinuous.</a>
    * Refresh canvas view harder on resize to avoid artifacts on some systems. Thanks xxxx for reporting.
    * Use proper background color in resize dialog. Thanks xxxx for reporting.
    * Correct a rounding error when converting pixels for display. This corrects both the visuals and the color picker when picking from the merged image. Thanks deovise and hipofiz for reporting.
    * Don't crash when a new user joins when using the builtin server and a local fork is present. Thanks to Kink for reporting.
    * Make build directories outside of the source directory work again. Thanks Aquargent for reporting.
    * Properly handle modifier key releases for keyboard canvas shortcuts. Thanks Daystream for reporting.
    * Make IPv6 addresses work in invite links.
    * Properly add drawpile:// in front of direct invite links when hosting "on this computer".
    * Make MyPaint brush permission not deny drawing with classic brushes. Thanks xxxx for reporting.
    * Offer to crop all avatars, not just non-square ones. Thanks Bluestrings for reporting.
    * Don't restore flipbook to previous location and size if that would put it outside of any available screen. Thanks Ausjamcian for reporting.
    * Prevent banning yourself from sessions.
    * Show proper reasons when a session is terminated, rather than always claiming the server is shutting down.
    * Squash whitespace in session listings to prevent funky display. Thanks yeen for reporting.
    * Play back sounds in a different way that should fix the issues with chugging or wrong output devices that some systems have. Thanks Blozzom and Snover for reporting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#sound-effect-replacement" target="_blank">Replace the terrifying notification sound effects with stuff from KDE's Ocean Sound Theme.</a>
    * Don't delay own laser trails as if it were a stroke from another user. Thanks matt for reporting.
    * Properly update avatar on user markers when they reconnect with a different one. Thanks xxxx for reporting.
    * Show own user marker again when using the laser pointer.
    * Use previous avatar when using the reconnect button after a disconnect.
    * Don't trigger a cacophony of notifications after joining a session, just play a single notification once catchup is done instead.
    * Don't lock tool slots when using the eraser tool, to avoid accidentally getting stuck in it.
    * Make Alt+Space canvas shortcut sorta work in Windows. Thanks Bovy and xxxx for reporting.
    * Nudge catchup if it gets stuck without any messages received for a while.
    * Allow saving and loading files in weird Android folders that chew up the file names internally.
    * Relax transform size restrictions so that transforms of layers that cover the whole canvas don't always get cancelled.
    * Actually put the link that's being joined into the address input when using a web link, rather than leaving it blank.
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#recolor-mode-optimization" target="_blank">Make Recolor (alpha locked) mode way faster.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#making-touch-pads-work-again" target="_blank">Allow using gestures instead of touch screen controls, hopefully making zooming on touch pads work again.</a>
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#ban-rework" target="_blank">Implement a shared bans system, letting owners of multiple servers manage a single list instead of having to keep them in sync manually.</a> Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/14/dev-update.html#ban-rework" target="_blank">Allow exempting users from ban ranges, to help alleviate false positives.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#session-ban-export" target="_blank">Allow exporting and importing session bans. They are encrypted with a per-server key by default.</a> Thanks tincancrab for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#idle-timeout-info-and-override" target="_blank">Allow moderators to exempt sessions from the idle timeout. This ability can be disabled by server owners.</a> Thanks Bluestrings for suggesting.
    * Allow specifying a reason when terminating a session manually.
    * <a href="https://docs.drawpile.net/devblog/2023/10/21/dev-update.html#session-roles-tab" target="_blank">Add Roles tab to session settings to allow changing operator and trusted status of registered users not currently online, as well as allowing importing and exporting this list of users.</a> Thanks tincancrab for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/10/29/dev-update.html#reworked-login-flow" target="_blank">Allow the user to pick how they want to log in, to avoid the common issue of wanting to join as a guest but picking a username that's taken.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/05/dev-update.html#server-rules" target="_blank">Allow servers to have a rules text that users are prompted to accept upon connecting. Clients remember that they accepted the rules and won't prompt again unless they changed since last time.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#server-bits" target="_blank">Allow servers to set a minimum protocol version for sessions being hosted.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#server-bits" target="_blank">Let clients know at the beginning of the login if the session they're trying to join is nonexistent.</a> Thanks Meru for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/11/10/dev-update.html#server-bits" target="_blank"> Allow server owners to make sessions only joinable through direct links.</a> Thanks Meru for suggesting.
* Server Fixes:
    * Error out when invalid --extauth parameter is given to drawpile-srv. Previously it would just keep going and simply not work without any indication as to why. Thanks RAINTARD for running into this.
    * <a href="https://docs.drawpile.net/devblog/2023/10/29/dev-update.html#reworked-login-flow" target="_blank">Don't boot user when they enter an incorrect password, let them try again.</a>
* Translations:
    * Brazilian Portuguese translation updated by Inky1003 and Rhowsl.
    * German translation updated by askmeaboutloom.
    * Italian translation updated by Bluu.
    * Japanese translation updated by ubanis.
    * Simplified Chinese translation updated by xxxx.
    * Spanish translation updated by Juan Daza.


## Documentation

A new article on <a href="https://docs.drawpile.net/help/tech/customassets.html" target="_blank">customizing sounds, icons and themes</a> has been added.


## Acknowledgements

Thanks to everyone who reported issues and suggested features to make Drawpile better. Thank you to the translators who make it more accessible. And as always a special thanks goes to the moderators that continue to keep things running, despite VPS providers trying their best to do otherwise.
