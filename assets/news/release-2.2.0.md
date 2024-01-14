Slug: release-2.2.0
Title: Version 2.2.0
Publish: 2024-01-13 23:59:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2.0 is out now! You can **[download it here](/download/)**. If you're updating from an earlier version, simply install the new one over it.

This is a final release and is ready for use right now. We're still updating the documentation, Docker and Flatpak, as well as waiting for Microsoft to process our submission of the program to them in the hopes that it will prevent SmartScreen warnings and other such annoyances. Users of Drawpile 2.1 won't be prompted to update automatically just yet while that's still going on. Once that's all done, there'll be another news post with all the stuff you missed if you haven't been using the 2.2 betas.

You can always download it manually though if you want to get your hands on the new stuff! This new version is compatible with sessions hosted by 2.1, so you can still draw with everyone that's on the old version. The server is also compatible, so server owners don't need to update immediately either.

Development of course doesn't stop here. If you find a bug, have a suggestion or otherwise need help, take a look at [the help page](/help/) on how to get in contact.

In particular, there's a web browser version of Drawpile being worked on, which is already functional and in testing. You can read more about that below.

## Changes in this Release

This release represents about a month of development since Drawpile 2.2.0-beta.11. Other than one small server feature, it's just been bugfixes since then.

---

This list does not include all the changes since 2.1.20. There'll be another, bigger news post later for that. If you want to read up on it now, you can go through [the previous news](/news/) and look at the beta release notes.

* Fixes:
    * Make pressure-less mode work with pens on Android. Thanks molluscdotgov for reporting.
    * Don't start dragging keyframes when they're moved only a minuscule amount. Thanks Meru for reporting.
    * Remove duplicate port from displayed network address when hosting under a non-default port. Thanks SadColor for reporting.
    * Keep focus on brush sliders when typing into them. Thanks MachKerman for reporting.
    * Show the fill tool size limit rectangle even when the outline width is set to zero pixels. Thanks Blozzom for reporting.
    * Unlist sessions more reliably when terminating sessions hosted "on this computer". Thanks to Buch for helping figure this out.
    * Don't select a newly created layer when there's a default layer.
    * Give the timeline dock a sensible minimum height. Thanks Kink for reporting.
    * Don't exit the program in the pathological case of initiating a quit, being prompted to save, cancelling the save dialog and then saving again.
    * Properly update current layer fill source when switching layers.
    * Cap the number of threads used for parallel processing, because 128 core CPUs exist.
    * Move back button in login dialog to the left side. Thanks Blozzom for reporting.
    * Properly forget password when editing account and unchecking the "remember password" box. Thanks Meru for reporting.
    * Apply chosen interpolation to pasted images. Thanks Deovise and Hipofiz for reporting.
    * Properly disable Session > Reset option when there's no canvas present that could be reset.
    * Allow opening PSD files and importing Drawpile 2.1 animations on Android. Thanks ariqhadiyan for reporting.
    * Don't act like the user entered incorrect account credentials if a session unexpectedly requires a password. Thanks Bluestrings for reporting.
    * Don't leave one-finger touch setting blank when "do nothing" is selected. Thanks BornIncompetence for reporting.
    * Shorten and normalize debounce delay to be 250 milliseconds for the layer opacity/blend mode, onion skins and timeline controls, rather than being a bunch of different values. Thanks robotto for reporting.
    * Remember invite link type setting properly. Thanks Bluestrings for reporting.
    * Try to keep the start dialog behind other dialogs it spawns harder. Thanks Bluestrings and shablagoo for reporting and Buch for finding issues with the fix.
    * Use a single palette in GIF export to prevent flickering. The palette is generated from the merged image. Thanks Hopfel and Bluestrings for reporting.
* Server Fixes:
    * Add --ssl-key-algorithm parameter to allow non-RSA SSL keys, defaulting to guessing the most common formats RSA and EC. Thanks Bluestrings for reporting.
    * Show an error message if listing on a certain server is not allowed.
    * Prevent users from being assigned permission flags they're denied by the server configuration, which could lead to a weird superposition of being flagged as a moderator, but not actually having moderator permissions. Thanks Bluestrings for reporting.
* Server Features:
    * Allow setting web admin auth through `DRAWPILESRV_WEB_ADMIN_AUTH` environment variable. The `--web-admin-auth` parameter takes precedence.
* Translations:
    * Arabic translation updated by Blozzom.
    * Brazilian Portuguese translation updated by Inky1003.
    * Czech translation updated by Hannah Oravcová.
    * European Portuguese translation updated by ssantos.
    * German translation updated by askmeaboutloom.
    * Italian translation updated by albanobattistella.
    * Japanese translation updated by ubanis.
    * Korean translation updated by TapodJointer.
    * Russian translation updated by anoNIM, Just Vitas and Redbear.
    * Simplified Chinese translation updated by Mach Kerman and xxxx.
    * Spanish translation updated by Juan Daza.

## Web Browser Version

Development on a browser version of Drawpile has started and is in a pretty usable state at this point, although it's still pretty early and there's plenty of issues to solve. It has been tested to work pretty much anywhere, including on iPad.

It's the whole of Drawpile running in the browser, not a pared-down web version. So it looks pretty much the same as the application does anywhere else and can do just about all of the same things.

This is not up on the official community servers, but work is happening to start making it available for server owners. Some kind of closed testing on the community servers will probably be coming too. If you're interested in getting your hands on it, keep your eyes on <a href="https://docs.drawpile.net/devblog/" target="_blank">the development blog</a> and/or <a href="/discord/" target="_blank">the Discord server</a>.

## Acknowledgements

Thanks to everyone who has been testing the beta versions, reported issues, contributed features, fixes or translations and otherwise helping to make Drawpile better. Also thanks to those providing help and keeping the community servers going.
