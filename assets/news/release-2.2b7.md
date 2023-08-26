Slug: release-2.2b7
Title: Version 2.2 beta 7
Publish: 2023-08-26 23:50:00+02:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2 beta 7 is released! **[Download it here.](/download/)**

If you find any issues, have questions or suggestions, check out the [the help page](/help/) for links!

And if you want to keep up to date on development, there's a <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog now</a>. There's regular updates being posted there, along with videos and pictures showing off the new features.


## Changes in this Release

This release represents about a month of development. There's been fixes, new features and several performance improvements, so if you're on a previous beta version, you should update!

---

Here's all the changes in this release in a big list. Where there's more details, the entries will link to the sections in the development blog, where they usually have accompanying videos or pictures.

* Features:
    * <a href="https://docs.drawpile.net/devblog/2023/08/25/dev-update.html#key-frame-exposure-controls" target="_blank">Allow increasing and decreasing key frame exposure.</a> Thanks Tabuley for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/25/dev-update.html#export-animations-from-the-flipbook" target="_blank">Allow exporting animations from the Flipbook, using the cropping, frame range and speed set in it.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/08/13/dev-update.html#ratchet-canvas-rotation" target="_blank">"Ratchet" canvas rotation shortcut, using Alt+Shift by default. Rotates the canvas in 15° increments.</a> Thanks to Kvothen for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/13/dev-update.html#better-animation-timeline-usability" target="_blank">Add layer on current key frame button is now in the top bar of the timeline, next to the other key frame buttons.</a> Thanks FallenArts for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/13/dev-update.html#better-animation-timeline-usability" target="_blank">Show a notice when there's no tracks yet, rather than just showing an empty timeline grid.</a>
    * Mark window when a chat message is received. On Windows, this makes the icon in the task bar orange. On macOS, it supposedly bounces an icon somewhere. On other platforms it probably does something similar, indicating which window is the one that got a message ready. Thanks Radio for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/13/dev-update.html#muting-notifications" target="_blank">Allow muting notifications for a window.</a> Thanks Blozzom for suggesting.
    * Allow selecting and copying text from the pinned message (through the context menu, it doesn't take keyboard shortcuts.) Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/19/dev-update.html#asynchronous-canvas-rendering" target="_blank">Make canvas rendering and preview painting asynchronous. This should make the UI much more responsive when e.g. changing layer visibility or transforming a large selection.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/08/19/dev-update.html#color-wheel-dextrocardia-cure" target="_blank">Make the color wheel innards go from least to most saturated, putting it in line with how most other software presents it. This can be toggled in the preferences.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/08/19/dev-update.html#translation-constraint" target="_blank">Holding Shift while moving a selection now keeps it along the closest axis.</a> Thanks Kvothen for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/19/dev-update.html#brush-export">Implement brush export and make the brush import also understand classic brushes.</a>
    * <a href="https://docs.drawpile.net/devblog/2023/08/19/dev-update.html#color-slider-space" target="_blank">Make sliders adhere to the chosen color space.</a> Thanks to leandro2222 for suggesting.
    * Increase font size on emoji posted into chat. Thanks to leandro2222 for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2023/08/25/dev-update.html#adding-avatars-during-login" target="_blank">Allow adding an avatar from the login dialog.</a>
    * Add shortcuts to swap the contents of brush slots to allow for a kind of toggling behavior using a single shortcut. Thanks xxxx for suggesting.
* Fixes:
    * Make classic brushes not go brighter when smudging into transparency. Thanks to cada for reporting.
    * Don't filter out undo depth messages when playing back recordings.
    * Make floating docks restore properly again. Thanks SnazComic for reporting.
    * Don't show tag options when right-clicking on a brush preset. Thanks Blozzom for reporting.
    * Properly disable blend mode combo box in layer properties dialog. Thanks xxxx for reporting.
    * Move chat status bar button into a legal position. Thanks Flz for reporting.
    * Correct various errors in text recording reading and writing.
    * Don't keep locally forked canvas states around. This reduces memory usage by a bunch, especially when drawing locally.
    * Actually pick color when adding a color to the color picker through the color dialog.
    * Don't add current color to the palette when creating it. Thanks xxxx for reporting.
    * Make exported palettes not start using the exported location to save changes to. Thanks xxxx for reporting.
    * Enable the lock session menu option properly, it remained stuck disabled in some cases before.
    * Don't claim that a layer is locked when it's just not visible in the current frame.
    * Properly handle canvas resizes while transforming a selection, it now no longer causes the source of the transform to get offset.
    * Show the current color properly on program startup.
    * Make erasing with MyPaint brushes in indirect mode actually work.
    * Show main window maximized by default, because who wants a drawing program in a tiny window.
    * Give docks sensible initial sizes. Thanks to xxxx for reporting.
    * Don't tabify the now invisible-by-default timeline and onion skins by default. Thanks Ben for finding.
    * Make the flipbook remember your last crop, frame range and playback speed for the current window. Thanks Ben for finding.
    * Don't mark guests as registered. Thanks to xxxx for reporting.
    * Allow assigning a shortcut to open the Layouts dialog (F9 by default) and to the entries in the Help menu (nothing by default.)
    * Make reloading the last brush preset slot-specific, since it's nonsense to clobber your current slot with the last preset you set in another one.
    * Properly update the view when the canvas size changes, rather than leaving stale areas outside of the canvas.
    * Make drawpile:// URL handling actually work on Windows. Thanks Sal for reporting.
    * Don't draw the curves for MyPaint brushes in the brush editor with the same color as the background grid.
    * Pre-fill image saving file dialogs with the current filename, rather than the previously opened or saved one. Thanks xxxx for reporting.
    * Make filling transparent areas work better, rather than different surrounding colors making it behave differently.
    * Make layer folders work as sources for flood filling.
 * Translations:
    * Arabic translation created by Arc.
    * Brazilian Portuguese translation updated by Inky1003.
    * Italian translation updated by Bluu.
    * Japanese translation updated by ubanis and Arc.
    * Simplified Chinese translation updated by xxxx.
    * Turkish translation updated by duennisss.


## Acknowledgements

Thank you to everyone who reported issues, suggested features and contributed translations attributed above. Particular thanks as always goes to the mods who keep the servers running.
