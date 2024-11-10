Slug: release-2.2.2-beta.4
Title: Version 2.2.2-beta.4
Publish: 2024-11-08 09:00:00+01:00
Visible: True
Author: askmeaboutloom
---

The second public beta of Drawpile 2.2.2 is out. You can **[download it in the Beta section on the downloads page](/download/#Beta)**. If you're updating from an earlier version, simply install the new one over it.

This beta is fully compatible. You can update to it and still draw with everyone on the main version and the previous beta, you'll just have more features than them, such as:

* <a href="https://docs.drawpile.net/devblog/2024/09/13/dev-update.html#brush-attachment" target="_blank">Brushes now remember changes, your current brush shows up in the tool dock</a> and <a href="https://docs.drawpile.net/devblog/2024/10/13/dev-update.html#shortcuttage" target="_blank">you can make shortcuts to brushes directly</a>.
* <a href="https://docs.drawpile.net/devblog/2024/09/28/dev-update.html#touch-gestures" target="_blank">More touch gestures: two-finger tap to undo, three-finger tap to redo, holding down with one finger for a color picker.</a>
* <a href="https://docs.drawpile.net/devblog/2024/11/01/dev-update.html#fill-optimization" target="_blank">Faster fill and magic wand tool.</a> They also <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#retool-fill-tool" target="_blank">no longer require a second click to confirm</a>.
* Better tablet support, particularly for Huion tablets.
* If you're drawing on an updated server and your operator(s) are using this version, you will no longer get session autoresets interrupting the drawing. <a href="https://docs.drawpile.net/devblog/2024/08/30/dev-update.html#streamed-autoresets" target="_blank">The canvas is compressed on the fly instead.</a>

And many more fixes and features. See below the fold for a full list!

If you find any issues, have questions or suggestions or need any help, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact.

## Changes in this Release

Drawpile 2.2.2-beta.4 represents about three months of development since Drawpile 2.2.2-beta.4. Many features were added and bugs fixed.

---

Where available, there'll be links with more details and illustrations if appropriate.

* Platforms:
    * Android 14 is now supported.
    * Drawpile has been accepted into F-Droid. As of November 10 2024, <a href="https://f-droid.org/packages/net.drawpile/" target="_blank">it is available on the platform</a>.
* Features:
    * <a href="https://docs.drawpile.net/devblog/2024/08/17/dev-update.html#animation-export-scaling" target="_blank">Allow scaling animation exports.</a> Thanks Hopfel for animating across a giant canvas.
    * <a href="https://docs.drawpile.net/devblog/2024/08/30/dev-update.html#color-dockage" target="_blank">Add settings button to color wheel, sliders and palette at the top-left of the dock. For the wheel, this allows changing the settings here now instead of having to go into the preferences.</a> For the sliders, you can now toggle the color space here and decide whether to show all sliders and the hex input. For the palette, this just moves the menu button that used to be in the row below. Thanks MachKerman for suggesting.
    * Allow aligning the color wheel to the top of the dock instead of the center. Can be toggled in the dock's menu. Thanks MorrowShore for suggesting.
    * Preview selected color on the color wheel. Can be toggled in the dock's menu. Thanks MorrowShore for suggesting.
    * Toggle layer visibility action, available in the Layer menu. Mostly useful to let assign a keyboard shortcut to it. Thanks incoheart for suggesting.
    * Remember ranges set for MyPaint brushes in the settings editor, rather than implicitly fitting them to the curve. Thanks Verdrusk for suggesting.
    * Allow importing MyPaint brushes in old version formats instead of saying they contain invalid JSON. Thanks bunnie for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/09/13/dev-update.html#brush-attachment" target="_blank">Attach brushes to slots, showing which brush you selected and remembering changes to them.</a> This attachment can be disabled in the tool preferences.
    * <a href="https://docs.drawpile.net/devblog/2024/09/13/dev-update.html#playing-slots" target="_blank">Allow configuring the number of brush slots in the tool settings, from 1 to 9, in addition to the everpresent eraser slot.</a> Thanks vipperz for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/09/28/dev-update.html#touch-gestures" target="_blank">Extended touch tap gestures, among them two-finger tap to undo, three-finger tap to redo and tap-and-hold to summon the color picker.</a> Can be configured in the preferences under the Touch tab. Thanks InconsolableCellist and many others for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/09/28/dev-update.html#rotation-snapping" target="_blank">Snap canvas rotation around 0° by default.</a> If you don't want this, you can set the canvas shortcut or touch rotation to "free rotate canvas" instead.
    * <a href="https://docs.drawpile.net/devblog/2024/09/28/dev-update.html#color-picker-sampling-circle" target="_blank">Show a color preview when picking a color from the canvas.</a> Can be toggled in the tool preferences.
    * Add Layer > Group View to show the parent group of the current layer in isolation. Thanks Rylan for suggesting.
    * Allow choosing between a round and square expansion/shrinking kernel in flood fill, magic wand and when altering a selection. The latter is particularly useful for pixel art. Thanks Bigcheese and MorrowShore for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/10/13/dev-update.html#shortcuttage" target="_blank">Put all shortcuts onto a single settings page, showing conflicts between them better. Allow searching for shortcuts by name and keybinding, as well as filtering out only conflicts.</a> Thanks MajorCooke for suggesting parts of this.
    * Allow assigning keyboard shortcuts to brushes. Assigning the same shortcut to multiple brushes will toggle through them. Thanks annoy for suggesting.
    * Use hardware renderer on Android by default.
    * Replace GIF export with ffmpeg's libraries, since they are also used for videos. It's way faster, generates much better palettes and supports transparent backgrounds. Thanks dAVePAGE and JJ for reporting issues in this regard.
    * <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#retool-fill-tool" target="_blank">Allow configuring flood fill preview and confirmation behavior, defaulting to the simplest mode similar to single-user software, but still previewing fills locally first.</a> The magic wand always works this way for now, since selections are local only anyway.
    * <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#expansion-prompt" target="_blank">Show resize dialog when expanding canvas, to avoid accidental resizes and improve performance by doing the expansions all in one step.</a> The keyboard shortcuts to expand the canvas work in this dialog now and also auto-repeat if you hold them down. Thanks Bluestrings and tobiasBora for suggesting things in this regard.
    * <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#less-annotation-mess" target="_blank">Empty annotations are now automatically deleted when you deselect them, to avoid the common clutter of stray empty annotations across the canvas.</a> If you really did want an empty annotation, you can hit undo and it will return.
    * <a href="https://docs.drawpile.net/devblog/2024/11/01/dev-update.html#fill-tolerance-adjustment" target="_blank">Allow clicking and dragging the fill and magic wand tools to adjust the tolerance.</a>
* Fixes:
    * Solve rendering glitches with selection outlines that happen on some systems. Thanks xxxx for reporting.
    * Allow disabling the application proxy in the network preferences and automatically detect bad proxy configurations that can't actually make connections. Thanks FishEggsThe for reporting.
    * <a href="https://docs.drawpile.net/devblog/2024/08/17/dev-update.html#proxy-handling" target="_blank">Improve socket error messages, listing the error code and adding extra information on what to do if a proxy error occurs.</a> Thanks FishEggsThe for reporting.
    * Center soft brushes on the cursor better, they got offset to the top-left from correcting for size discontinuity before. Thanks Meiren for reporting.
    * Don't mess up gridmap settings when opening brush settings dialog and initially changing a value in it. Thanks Blozzom for reporting.
    * Default "confirm action" to both the regular enter key as well as the one on the numpad. Thanks MachKerman for reporting.
    * Scale outer color wheel ring with the size of the widget. Thanks MorrowShore for reporting.
    * Allow pressing the numpad enter key to apply an action and Ctrl+Equal in addition to Ctrl+Plus to zoom in. Thanks MachKerman and Sinamer for reporting.
    * Prevent artifacts around brush cursor when the canvas is rotated in software renderer mode. Thanks Sinamer for reporting.
    * Don't consider the flood fill's own preview when filling the merged image. Thanks Meru for reporting.
    * Make joining through a direct link not put the desktop client into single-session mode. Thanks Bluestrings for reporting.
    * Work around Huion tablets emitting mouse clicks every few pen presses and causing full-pressure strokes to be started. Thanks Blozzom, DT and and Dumb Dog Disease for reporting.
    * Clamp palette swatch sizes to more reasonable bounds. Thanks MachKerman for reporting.
    * Correct some UI scaling problems with brush outlines, canvas centering, dock toggling, pixel grid and transform handles. Thanks annoy for reporting.
    * In layer view mode, render the layer truly in isolation instead of applying opacities, visibilities or alpha preserve to it. Thanks MachKerman and incoheart for reporting.
    * Save and export images according to the current view mode. Thanks incoheart for reporting.
    * Make MyPaint brushes not ignore the first stroke made with them. This would also sometimes lead to a blank preview.
    * Don't ignore double-clicks when toggling layer visibility or check state. Thanks Chryssabliss for reporting.
    * <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#issues-of-scale" target="_blank">Make user interface scaling not round to multiple of 100% anymore.</a> Thanks blau, Buch, Chryssabliss and ShotgunnerFox for reporting.
    * Don't use system message boxes on Android, since they behave in various broken and nonsensical ways, like showing you a yes button three times. Thanks Hopfel for reporting.
    * Don't unnecessarily scale full-canvas animations by a single pixel.
    * Constrain aspect ratio of transform scaling properly, it was getting offset by the distance between the clicked point and the actual corner. Thanks Blozzom for reporting.
    * <a href="https://docs.drawpile.net/devblog/2024/10/25/dev-update.html#permission-clarification" target="_blank">Indicate denied permissions by showing a message to that effect, rather than just disabling the actions and leaving you guessing.</a> Thanks Venesio for reporting.
    * Clicking off of an annotation will no longer instantly create a new one in that spot. It will instead only deselect the annotation that was selected.
    * The Delete Empty Annotations can now be undone without undoing what happened before it as well.
    * Make mouse click canvas shortcuts not override key canvas shortcuts. Thanks incoheart for reporting.
    * Make login dialog not spill off-screen on mobile devices.
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2024/08/30/dev-update.html#streamed-autoresets" target="_blank">Streamed autoresets that don't interrupt the session to bring it down to a smaller size, instead the compressed state is built up in the background and replaced on the fly.</a>
    * Provide more session status information for administrators, such as the autoreset state.
    * Allow checking session, operator and server account passwords via the API. This can be used to password-protect recordings or similar. Thanks Meru for contributing.
    * Integrate with systemd watchdog.
    * Setting a minimum protocol version of dp:4.24.0 now tells clients that they're using a Drawpile version too old for this server, rather than leaving them sitting at a session list where they can join no sessions.
    * <a href="https://docs.drawpile.net/devblog/2024/11/01/dev-update.html#persistence-permission" target="_blank">Always allow server admins, moderators and users with the new PERSIST flag to toggle session persistence.</a> The global persistence setting still allows anyone to toggle this. Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/11/01/dev-update.html#lingering-existence" target="_blank">Allow admins to specify a linger time for empty sessions, which will let even non-persistent sessions live on for that time to allow people a chance to reconnect.</a>
    * Add API endpoints to get and create session listings. Thanks Meru for contributing.
* Server Fixes:
    * Don't get announcement refreshes stuck in an infinite loop. Thanks Meru for reporting.
* Translations (note that only translations that are completed to a signficant degree are included in the program):
    * Arabic translation updated by Blozzom.
    * German translation updated by askmeaboutloom.
    * Italian translation updated by albanobattistella.
    * Japanese translation updated by ubanis.
    * Norwegian Bokmål translation updated by Michael Aure.
    * Simplified Chinese translation updated by xxxx.
    * Spanish translation updated by Rockhopper.
    * Russian translation updated by George Bogdanoff and влад вас.
    * Vietnamese translation updated by Nguyễn Hương Duyên.
    * Indonesian translation updated by Reza Almanda.
    * Polish translation updated by Krzysztof Bursa.

## Acknowledgements

Thanks to all the people testing Drawpile, reporting issues, suggesting features and otherwise contributing to Drawpile. Also thanks to the moderators and community admins that keep those servers running.

Thanks also go out to <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
