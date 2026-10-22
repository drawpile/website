Slug: release-2.3.1
Title: Version 2.3.1
Publish: 2026-10-22 03:30:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.3.1 is out now! It has lots of new features, bugfixes and performance improvements but is **fully compatible** with Drawpile 2.3.0. You'll be able to draw with people who didn't update, you'll just have more features.

* **[Click here to download the new version](/download/)**! To update, simply install it over the previous one.

There is <strong><a href="https://docs.drawpile.net/help/common/update2x3x1" target="_blank">an illustrated guide showing the new features here</a></strong>. The full changelog follows below.

If you have questions, feedback or trouble using the new version, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact. And if you want to support continued development, you can <nobr><strong><a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donate to the project</span></span></a></strong></nobr>!

## Updating

To update, you should be able to just **[download the new version](/download/)** and just install it over the previous version, that will update it on all operating systems. The new version is fully compatible, you can still join the same sessions with it and vice-versa people who didn't update can join yours.

F-Droid on Android and Flatpak on Linux will get this version soon, it usually takes them a bit. In the application, you'll get a prompt about updating in the coming days as well.

For server owners, it makes sense to update, there are several fixes and improvements. For example, people loitering outside of sessions can now be given a timeout to prevent them from idling forever and you can choose to allow new sessions to replace empty, lingering ones that are about to end anyway instead of refusing to host it with a "server is full" message.

## What's Next

There is also already work going on toward the next version, so you can expect another beta release hopefully soon! Work on a liquify tool is almost finished, which on its own is already very useful. There will also be a crop tool built to work on a collaborative canvas, letting you create selections from the crop area, export it as an image and similar things beyond just resizing the canvas. There are also some contributions to the color wheel pending to flip the triangle around if you're used to it that way from other programs.

Keep an eye <a href="https://docs.drawpile.net/devblog/" target="_blank">on the development blog</a> if you want to read more about it. And of course you can <a href="https://docs.drawpile.net/help/development/contributing" target="_blank">contribute to Drawpile's development</a> or <a href="https://donate.drawpile.org/" target="_blank">make a donation</a> to help keep it going.

## Changes in this Release

There's many new features and improvements, such as:

* The new <a href="https://docs.drawpile.net/help/common/update2x3x1#project-file-format-dppr" target="_blank">dppr project file format</a>, which brings <a href="https://docs.drawpile.net/help/common/update2x3x1#autorecovery" target="_blank">autorecovery</a>, <a href="https://docs.drawpile.net/help/common/update2x3x1#project-playback" target="_blank">time-travel</a> and <a href="https://docs.drawpile.net/help/common/update2x3x1#project-statistics" target="_blank">statistics</a>.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#timelapses" target="_blank">Timelapses</a>, via File → Make Timelapse. This makes a video of your drawing or animation process, some people also (incorrectly) call this "speedpaint". You can even make a cropped timelapse by selecting an area on the canvas first.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#brush-stroke-previews" target="_blank">Stroke previews and brush names</a> in the brushes dock, rather than just thumbnails. You can switch back to those if you prefer of course.
* A <a href="https://docs.drawpile.net/help/common/update2x3x1#brush-history" target="_blank">brush history</a>, to keep a list of recently used brushes. This also lets you restore deleted brushes and keeps unsaved brushes you've requested from other users.
* Many <a href="https://docs.drawpile.net/help/common/update2x3x1#animation-improvements" target="_blank">animation improvements</a>, like letting you select multiple frames, quicker exposure changes, timeline zooming, inverted ranges to work on the tail ends of loops, move locking tracks, more video export options, spritesheet exports and more.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#better-android-support" target="_blank">Better Android support</a>. When Drawpile starts, it asks you how large you want the UI now. Many keyboard issues were fixed and several devices also have received special workarounds to make them work properly. Barrel rotation is also now supported. If Android terminates the application in the background, it will automatically resume where you left off.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#velocity-adjusted-stabilizer" target="_blank">Velocity-adjustment for the stabilizer</a>, speeding up as you make faster strokes.
* A <a href="https://docs.drawpile.net/help/common/update2x3x1#fan-fill" target="_blank">fan fill shape</a> for the shape fill tool, which used to be called lasso fill tool because that was its only shape.
* Performance improvements, like making canvas resizes much faster and use way less memory. Drawpile also starts quicker now.

And more, see the changelog below.

---

It lists only the changes since the previous beta release. Which aren't that many, it was already very stable and close to the final release. See [the 2.3.1-beta.1 announcement](/news/release-2.3.1-beta.1/) and [the 2.3.1-beta.2 announcement](/news/release-2.3.1-beta.2/) for the rest of the changes since 2.3.0.

The <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog</a> also has frequent updates on what's going on with development if you want to read more about it.

* Features:
    * Remove the "Normal View" button from the timeline header, since you can just press the frame view button to exit it. This makes the timeline fit better on small screens.
    * Add a drag zoom mode to the zoom tool. This is the default, since it's more useful and consistent with the rotation and pan tools. You can still use the select zoom by right-clicking, holding the constrain key (Shift by default) or switching the mode of the tool. Thanks Shuko for suggesting.
    * Give the zoom tool nice header buttons to zoom in, out, fit and reset.
    * On Android, hide any open docks in small screen mode when pressing the back button before closing the main window. Thanks anonymous for suggesting.
    * Handle Lenovo Tab stylus presses on Android by translating them to F26 to F30. Thanks Moody2357 for helping to figure this out.
    * Add some new brushes in the Drawpile category and a new Secret's Brushes category with ribbons, halftones and more provided by Blozzom.
* Fixes:
    * Make dock tab icons show up properly on Qt 6.11, they could end up blank there.
    * Don't skip initial command when playing back recordings. This caused the canvas size command to be skipped on old converted recordings, meaning its size stayed at zero and nothing would play. Thanks dango for reporting.
    * Make hitting "save" after joining a session in the same window not save over the save file from a previous session in the same window. Unless you are reconnecting to the same session, in which case it will save over the file as it should. The logic for this was reversed from what it should be. Thanks Bonbli and D'mitri for reporting.
    * Also select layers when multiple key frames are selected.
    * Properly select layers when switching focused tracks when the selected frame was already visible.
    * Revert default save format to the new default even if it has been changed before, since it's better to make you change it again than lose timelapse data. Thanks Sheepolution for reporting.
    * A crash on Windows when unchecking the show conflicts checkbox while still editing a shortcut. Thanks yellow circle for reporting.
    * Make animation playback not get stuck when switching from a reversed range to a normal one without refreshing.
    * Properly apply the parent group's opacity in the rendered animation as well, rather than just on the canvas.
    * Make start screen take less horizontal space in small screen mode. Thanks anonymous for reporting.
    * Make the zoom tool behave more predictably, it now doesn't do weird stuff like letting you select an area and then zooming out on it.
    * Give better icons to zoom in, zoom out and reset zoom, so that they don't all just look like rectangles at a glance.
    * Properly indicate that the previous session is being resumed on Android. Thanks tiar for reporting.
    * Correctly restore local state like layer visibility when resuming a session with a snapshot on Android. Thanks tiar for reporting.
    * Work around the Wacom Movinkpad update showing a cursor when using the stylus that will flicker out of existence every time you press down the stylus. It will now show no cursor for the stylus, as it did before. Thanks Sylvanticus for reporting.
* Server Features:
    * Allow new sessions to clobber empty, non-persistent, lingering sessions. Server owners can enable this to prevent "server is full" errors that would resolve themselves by waiting a few minutes for these lingering sessions to time out. Sessions with the lowest time spent drawing are terminated first. Thanks Bluestrings for suggesting.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Brazilian Portuguese translation by MangledPuppet.
    * German translation by askmeaboutloom.
    * Japanese translation by ubanis.
    * Russian translation by mauv the bluest cat ever.
    * Simplified Chinese translation by xxxx.
    * Spanish translation by Manuart.

## Acknowledgements

Thanks to everyone that has reported bugs, requested and discussed features, contributed code or documentation and otherwise helped with the development. Also thanks to those in the support channels helping out others and of course the administrators keeping the public servers running. And of course to those that have donated to the project.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
