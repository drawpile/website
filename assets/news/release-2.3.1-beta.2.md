Slug: release-2.3.1-beta.2
Title: Version 2.3.1-beta.2
Publish: 2026-09-23 20:30:00+02:00
Visible: True
Author: askmeaboutloom
---

The second beta for Drawpile 2.3.1 is out now. The first one has already been very stable, so unless major issues are found, this will become the final release. If you want to give feedback before that, now is the time! This is **fully compatible** with Drawpile 2.3.0. You'll be able to draw with people who didn't update, you'll just have more features.

* **[Click here to download and install the beta version](/download/#Beta)**. To update, simply install it over the previous one.

For pictures and videos showing the new stuff in this version <strong><a href="https://docs.drawpile.net/help/common/update2x3x1" target="_blank">take a look at this illustrated guide</a></strong>. For a more detailed breakdown of all the features, read on!

If you have questions, feedback or trouble using the new version, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact. And if you want to support continued development, you can <nobr><strong><a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donate to the project</span></span></a></strong></nobr>!

## Updating

You can download this version **[from the Beta section of the downloads page](/download/#Beta)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

Alternatively, you can run both versions side-by-side. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to do that on different operating systems</a>.

F-Droid on Android and Flatpak on Linux should get this version on their beta channels in the coming week or so. It always takes them a little bit longer to do so.

Server owners can update at their leisure. There are some fixes and improvements, such as not having people linger outside of sessions forever and being clearer about when bans end, but nothing too critical. If you are using the all-in-one Docker server, <a href="https://github.com/drawpile/dpserver/blob/master/README.md#beta-versions" target="_blank">see here how to update</a>.

## Changes in this Release

There's many new features and improvements, such as:

* The new <a href="https://docs.drawpile.net/help/common/update2x3x1#project-file-format-dppr" target="_blank">dppr project file format</a>, which brings <a href="https://docs.drawpile.net/help/common/update2x3x1#autorecovery" target="_blank">autorecovery</a>, <a href="https://docs.drawpile.net/help/common/update2x3x1#project-playback" target="_blank">time-travel</a> and <a href="https://docs.drawpile.net/help/common/update2x3x1#project-statistics" target="_blank">statistics</a>.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#timelapses" target="_blank">Timelapses</a>, via File → Make Timelapse. This makes a video of your drawing or animation process, some people also (incorrectly) call this "speedpaint". You can even make a cropped timelapse by selecting an area on the canvas first.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#brush-stroke-previews" target="_blank">Stroke previews and brush names</a> in the brushes dock, rather than just thumbnails. You can switch back to those if you prefer of course.
* A <a href="https://docs.drawpile.net/help/common/update2x3x1#brush-history" target="_blank">brush history</a>, to keep a list of recently used brushes. This also lets you restore deleted brushes and keeps unsaved brushes you've requested from other users.
* Many <a href="https://docs.drawpile.net/help/common/update2x3x1#animation-improvements" target="_blank">animation improvements</a>, like letting you select multiple frames, quicker exposure changes, timeline zooming, inverted ranges to work on the tail ends of loops, move locking tracks, more video export options, spritesheet exports and more.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#better-android-support" target="_blank">Better Android support</a>. When Drawpile starts, it asks you how large you want the UI now. Many keyboard issues were fixed and several devices also have received special workarounds to make them work properly. Barrel rotation is also now supported.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#velocity-adjusted-stabilizer" target="_blank">Velocity-adjustment for the stabilizer</a>, speeding up as you make faster strokes.
* A <a href="https://docs.drawpile.net/help/common/update2x3x1#fan-fill" target="_blank">fan fill shape</a> for the shape fill tool, which used to be called lasso fill tool because that was its only shape.
* Performance improvements, like making canvas resizes much faster and use way less memory. Drawpile also starts quicker now.

And more! The changelog follows below.

---

These are only the changes since the previous beta. See [that announcement](/news/release-2.3.1-beta.1/) for the changes since 2.3.0.

Where available, there's links to the <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog</a> with more information.

* Features:
    * <a href="https://docs.drawpile.net/devblog/2026/05/25/dev-update.html#touch-actions" target="_blank">Allow triggering any action via touch taps.</a> Thanks Bnuuyman for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/05/25/dev-update.html#touch-actions" target="_blank">Add one-finger double-tap touch action.</a> Lets you bind stuff to tapping twice quickly with a single finger. Thanks Bnuuyman for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/06/07/dev-update.html#frame-multiselection" target="_blank">Allow selecting multiple frames in the timeline, letting you move, copy, delete etc. them all at once.</a> You can use Shift or Ctrl or switch to the "select" timeline tool to do it without keyboard keys.
    * Add support for stylus barrel rotation on Android, for styluses that support it. Thanks kwh0209 for helping test this.
    * Allow fractional scaling for animation exports, in case you need very specific pixel dimensions.
    * <a href="https://docs.drawpile.net/devblog/2026/06/07/dev-update.html#right-click-drawing-configuration" target="_blank">Allow configuring right-click drawing to do nothing (the default), draw with the background color or erase.</a> Thanks noelle and walnut for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/06/07/dev-update.html#layer-selection-shortcuts" target="_blank">Allow selecting color-marked layers via keyboard shortcuts.</a> Thanks anonymous for suggesting.
    * If Drawpile on Android is terminated due to resource exhaustion, such as running out of memory, it will now show a message about it on the next startup. Thanks Bluestrings for suggesting.
    * Add a workaround for full-pressure blotches on Ugee tablets. Enabled by default on Android and the browser where it is known to happen, shouldn't cause interference for styluses that behave normally. Thanks London for reporting.
    * Allow configuring whether a stroke is started only when moving the stylus. Enabled by default, as it was before. Thanks dAVePAGE for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/06/21/dev-update.html#fan-filling" target="_blank">Turn the lasso fill tool into a shape fill tool with two shape options: lasso and fan.</a> The latter option does not produce holes, everything gets filled. Thanks lan700ng and VolutBrum for suggesting.
    * Allow exporting animations and timelapses on Android with the OS-supplied media encoder. Thanks Bluestrings, hpar and marddle for testing.
    * Add a declone key frame layers action. For the selected key frames, it will duplicate the layers referenced by multiple key frames.
    * Add a paste decloned key frame layers action. Will paste and duplicate layers if necessary.
    * Allow configuring the default save file name format under Edit → Preferences → Files. Thanks Bluestrings for suggesting.
    * Show the current layer title on the cursor when using the layer pick canvas shortcut (Ctrl+Shift+Left Click by default.) Thanks Gabr for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/07/06/dev-update.html#brush-history" target="_blank">A history of used brushes, selectable as as a new "History" tag.</a> Deleted brushes and brushes requested from other users will be retained here and can be undeleted or saved respectively until the history is cleared or they are explicitly removed. Thanks Ausjamcian, Geese and Phoneme for suggesting.
    * Add a clear button for the search field in the brushes dock. Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/07/19/dev-update.html#windows-video-export" target="_blank">Allow exporting animations and timelapses on Windows using the OS-supplied media encoder.</a>
    * <a href="https://docs.drawpile.net/devblog/2026/08/09/dev-update.html#project-playback" target="_blank">Project playback, via File → Open Player.</a> Can play back dppr files. This replaces the previous player, dprec and dptxt files will be converted on the fly.
    * Drawpile will now ask you if you start a recording while autorecovery is enabled, to avoid accidentally recording double for no reason. Thanks tiar for reporting.
    * Allow converting dprec and dptxt recordings to dppr files via File → Import → Convert Recordings to Project. You'll also be prompted about it when you use File → Open on these files.
    * Support for Android 16. Older versions continue to be supported, same as before.
    * <a href="https://docs.drawpile.net/devblog/2026/09/07/dev-update.html#udp-activity-stream" target="_blank">Add Tools → Developer Tools → UDP Activity Stream.</a> This emits the cursor position over the canvas view and some other activity over a UDP socket, which can be consumed by stream avatars, brush sound makers and similar programs. Thanks Maniko for suggesting.
    * PNG spritesheet export for animations. Thanks greendyno and ULTRA TECH for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/09/07/dev-update.html#project-repair" target="_blank">Repairing dppr and dpcs files via File → Repair File.</a> If the file is detected to be corrupted, you will also be prompted to repair it when opening or recovering the file.
    * The the position, zoom, rotation, mirror and flip state of the view is now saved in dppr files. This state is restored when resuming a session on Android and following it can be toggled in the playback dialog.
    * When using Save As to save to a new dppr file, the current dppr file will be used as the basis for it, rather than an empty file. Thanks tiar for suggesting.
    * Add File → Merge/split projects. This lets you combine multiple dppr files or pull individual sessions out of them. Adding dprec/dptxt recordings to them is also supported.
    * <a href="https://docs.drawpile.net/devblog/2026/09/20/dev-update.html#browser-additions" target="_blank">Warn about closing the browser tab too quickly after saving,</a> since several browers will truncate the target file to 0 bytes and then write to a temporary file, leaving you with the former if you exit too quickly.
    * <a href="https://docs.drawpile.net/devblog/2026/09/20/dev-update.html#browser-additions" target="_blank">The browser pressure tester now shows the pressure value and lets you toggle whether to optimize for low-pressure styluses like Apple Pencils,</a> in case it doesn't get detected automatically.
    * Allow switching timelapses to be speed-based instead of duration-based. It will calculate the video duration from the given speed. Thanks xxxx for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/09/20/dev-update.html#menu-button" target="_blank">Replace the New and Open buttons in the toolbar with a menu that has common file actions and repeats the top menu bar for systems where that's annoying to access.</a> Thanks tysontan for suggesting.
    * Allow dragging the logo in the timelapse dialog, rather than having to fiddle with the padding sliders.
* Fixes:
    * Make ratchet rotation canvas shortcut work properly when the canvas is mirrored or flipped. Thanks Bovy for reporting.
    * Make default filename use *months* as the second number, not *minutes*. Thanks hipofiz for reporting.
    * Allow dragging initial curve tool point to let you change its control point again. Thanks Astre for reporting.
    * A fix for the application not starting up on Android older than 8. Thanks freyalupen for reporting.
    * Make repeated move transforms not cause the transformation to get scaled by one pixel. Thanks Hermanni for reporting.
    * Give select layer above and below shortcuts a proper title with "layer" in the name so that you have a chance of finding them in the list. Thanks anonymous for reporting.
    * Make sure MyPaint brush strokes start with proper directional values if the brush makes use of them. Previously they could end up with the value being zero degrees instead. Thanks tiar for reporting.
    * Call the Option key on macOS by its proper name. Thanks Axocrat for reporting.
    * <a href="https://docs.drawpile.net/devblog/2026/06/21/dev-update.html#stroke-directionality" target="_blank">Make MyPaint brushes not require movement to put down the first part of their stroke.</a> Brushes that use directional inputs don't do this, since movement is needed to have a direction. Thanks dAVePAGE for reporting.
    * Correct saving of key frame properties to dppr files. Thanks marddle for reporting.
    * Make WEBM video export use a higher quality.
    * Allow hitting enter/return twice on a number input to accept the dialog they're in, rather than entering edit mode again. You can also hold Shift to explicitly accept the dialog and Ctrl to explicitly enter edit mode instead.
    * Take the canvas rotation into account when constraining the angle (Shift by default) in the line and gradient tools. Thanks Ben for reporting.
    * Properly remember the selection of built-in brush tags like All or Untagged.
    * <a href="https://docs.drawpile.net/devblog/2026/07/19/dev-update.html#better-canvas-resizing" target="_blank">Optimize non-tile-aligned canvas resizes.</a> They should now be faster and use less memory. Thanks Bluestrings for reporting.
    * Retrieve file display names properly on Android. They could sometimes end up with wonky names when using file providers with ugly paths.
    * Use the proper input minimum and input maximum ranges in the MyPaint brush settings. Thanks Pine for reporting.
    * Allow toggling the workaround that ignores zero-pressure tablet inputs, in case you have a tablet that reports no pressure despite you pressing the stylus down. SuperDisplay is known to do this. Thanks Tenzin for reporting.
    * Encode special characters in invite links so that they don't cause trouble when copying them around. Thanks Bluestrings for reporting.
    * Make timeline selection tool work properly while dragging over a track with onion skins enabled.
    * A crash when resizing the canvas smaller while a lasso selection is being transformed. Thanks greendyno for reporting.
    * Make Selection → Fill Selection, gradient tool and shape fill tool adhere to layer alpha lock. Thanks hipofiz and Verdrusk for reporting.
    * Show proper download progress for list server favicons.
    * Make double-clicking dock titlebars not toggle them floating, since that's too easy to activate accidentally.
    * Increase the drag threshold for arranging docks and toolbars in general, as well as for docks when not in arrange mode even further, to avoid accidental rearrangements.
    * When saving an ORA file with clipping groups, the animation timeline's frame assignments no longer get garbled. Thanks BluesFlying for reporting.
    * Solve an issue where on some systems you would get disconnected on the first attempt of joining a session and then it worked fine on reconnect. This fix was already applied on Android, but aparently it also rarely happens elsewhere. Thanks Greendyno for reporting.
* Server Features:
    * Tell the user how many hours or minutes remain on their ban if it expires in less than 3 days, since giving just a date can make it confusing with regards to time zones. Thanks Bluestrings for suggesting.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Abdo Alrahman Faiad, Blozzom and Dyaa Okor
    * German translation by askmeaboutloom
    * Indonesian translation by Arif Budiman
    * Japanese translation by ubanis
    * Malay translation by sooleehin7
    * Russian translation by Vorpal Void
    * Simplified Chinese translation by xxxx
    * South American Spanish translation by Manuart

## Acknowledgements

Thanks to everyone that has reported bugs, requested and discussed features, contributed code or documentation and otherwise helped with the development. Also thanks to those in the support channels helping out others and of course the administrators keeping the public servers running. And of course to those that have donated to the project.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
