Slug: release-2.3.1-beta.1
Title: Version 2.3.1-beta.1
Publish: 2026-05-16 16:45:00+02:00
Visible: True
Author: askmeaboutloom
---

The first beta for Drawpile 2.3.1 has been released. It has many new features, such as autorecovery, timelapses, animation improvements, dynamic scaling on Android and more, as well as numerous bugfixes. But like the small increase in the version number implies, it is *fully compatible* with version 2.3.0.

* **[Click here to download and install the beta version](/download/#Beta)**. To update, simply install it over the previous one.

This has already been out and tested for a while as an "alpha" version for a while, so it should be stable and ready for use. Especially if you're using Drawpile for offline drawing, the autorecovery feature makes it worth using the beta. For animators, there also big enough improvements that this will be the superior version. On Android, there's also been a number of improvements and compatibility for more devices.

For a list of what changed, <strong><a href="https://docs.drawpile.net/help/common/update2x3x1" target="_blank">take a look at this guide</a></strong>. There's pictures and videos there describing the new stuff.

If you have questions, feedback or trouble using the new version, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact. And if you want to support continued development, you can <nobr><strong><a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donate to the project</span></span></a></strong></nobr>!

## Updating

You can download this version **[from the Beta section of the downloads page](/download/#Beta)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

Alternatively, you can run both versions side-by-side. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to do that on different operating systems</a>.

F-Droid on Android and Flatpak on Linux should get this version on their beta channels in the coming week or so. It always takes them a little bit longer to do so.

Server owners can update if they want, although it is not necessary. The most significant thing is that you can now restrict how long users can linger outside of a session, letting you prevent them idling in the session list for example, and some fixes for cases where clients weren't properly disconnected after their session ended. If you are using the all-in-one Docker server, <a href="https://github.com/drawpile/dpserver/blob/master/README.md#beta-versions" target="_blank">see here how to update</a>.

## Changes in this Release

There's many features and fixes in this version, such as:

* <a href="https://docs.drawpile.net/help/common/update2x3x1#autorecovery" target="_blank">Autorecovery</a>. If Drawpile exits unexpectedly, Windows reboots your computer for updates or Android terminates Drawpile in the background, you can recover your session, usually right up to the moment it stopped. This replaces the (not very automatic) autosave mechanism and makes offline drawing much more robust.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#project-file-format-dppr" target="_blank">A new "project" file format</a>, called dppr. Stores the whole history of your canvas, based on the autorecovery feature.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#timelapses" target="_blank">Timelapses</a>, via File → Make Timelapse. This makes a video of your drawing or animation process, some people also (incorrectly) call this "speedpaint". You can even make a cropped timelapse by selecting an area on the canvas first.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#brush-stroke-previews" target="_blank">Stroke previews and brush names</a> in the brushes dock, rather than just thumbnails. You can switch back to those if you prefer of course.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#animation-improvements" target="_blank">Animation improvements</a>, like exposure changes, timeline zooming, inverted ranges to work on the tail ends of loops, move locking tracks and more.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#better-android-support" target="_blank">Better Android support</a>. When Drawpile starts, it asks you how large you want the UI now. Many keyboard issues were fixed and several devices also have received special workarounds to make them work properly.
* <a href="https://docs.drawpile.net/help/common/update2x3x1#velocity-adjusted-stabilizer" target="_blank">Velocity-adjustment for the stabilizer</a>, speeding up as you make faster strokes.
* Performance improvements, like better brush loading to make Drawpile start up faster or speeding up synchronized smudging.

And a lot more. The full changelog follows below.

---

Where available, there's links to the <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog</a> with more information. Note that these sometimes mention that something isn't implemented yet because they weren't at the time, but usually later block posts give an update that it has been implemented in the assorted bits section at the bottom.

* Features:
    * Allow setting a blank brush cursor in the tools preferences. Thanks mixnmatt for suggesting.
    * Show rectangle selection extents in the status bar. Thanks Mercia for suggesting.
    * Allow selecting custom color scheme files dropped into the application data.
    * <a href="https://docs.drawpile.net/devblog/2025/12/21/dev-update.html#autosaving" target="_blank">Replace autosave mechanism with more robust autorecovery mechanism.</a>
    * Allow toggling eraser, erase mode and alpha preserve via canvas shortcut. Thanks SOLARIS for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/02/02/dev-update.html#statistics" target="_blank">Allow viewing project statistics</a>, such as length of sessions and work time, via File → Project statistics. Requires enabling autorecovery and saving to a dppr file.
    * <a href="https://docs.drawpile.net/devblog/2026/02/02/dev-update.html#timelapses" target="_blank">Timelapses, via File → Make timelapse.</a> Requires enabling autorecovery and saving to a dppr file.
    * <a href="https://docs.drawpile.net/devblog/2026/02/02/dev-update.html#canvas-shortcut-actions" target="_blank">Allow triggering undo, redo, hide docks and any other actions via canvas shortcut.</a> Thanks RubySnoot for suggesting.
    * Make right-clicking with the freehand tool draw with the background color. Thanks doughie for suggesting.
    * Add next/previous frame within range actions, to move through the timeline but wrap at the edges of the frame range. Holding shift while pressing arrow keys actuates this action as well. Thanks BulletPepper for suggesting.
    * Add "set speed by FPS", "reset range" and "reset speed" actions to the flipbook. They are now behind the button that previously had only two zoom-related actions.
    * <a href="https://docs.drawpile.net/devblog/2026/02/15/dev-update.html#android-scaling" target="_blank">Ask for a UI scale on startup on Android</a>, letting you adjust it and view the result, rather than having to restart Drawpile and potentially be left in an unworkable state. You can also pick the interface mode while you're at it.
    * <a href="https://docs.drawpile.net/devblog/2026/02/15/dev-update.html#rotation-tool" target="_blank">Rotation tool.</a> Similar to the Pan and Zoom tools, this lets you rotate the canvas just by clicking on the canvas. Thanks Cryankiebuillars for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/03/01/dev-update.html#curve-inputs" target="_blank">Add numeric input fields to curve inputs to allow the exact numeric values of each curve point to be set exactly.</a> Thanks Saphiros for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/03/01/dev-update.html#brush-preview-options" target="_blank">Brush preview styles.</a> You can now toggle between the full style with the rainbow circles and a plain style that matches the UI colors and doesn't try to preview every aspect of the brush. You can also toggle the display of the brush's title and thumbnail. There's also the option of disabling the preview altogether. The default is to show the thumbnail and title with plain style, since that gives the best tradeoff between showing the relevant information without being too distracting. Thanks fadi123go for suggesting.
    * Only load brush thumbnails as they are needed. This should speed up startup if you have a lot of brushes.
    * <a href="https://docs.drawpile.net/devblog/2026/03/01/dev-update.html#brush-stroke-previews" target="_blank">Allow choosing between thumbnails, strokes or both in the brushes dock.</a> The default is both, since it gives the most amount of information at a glance.
    * Allow arbitrary scaling of brush dock sizes with a slider instead of a fixed set of sizes.
    * Bind mouse button 5 to toggling the eraser by default. This makes three-button styluses have useful behavior.
    * <a href="https://docs.drawpile.net/devblog/2026/03/01/dev-update.html#ffmpeg-exports" target="_blank">Allow using external ffmpeg for animation exports.</a> This adds some more video codecs that normally don't come with Drawpile.
    * An overview page for the shortcut preferences, to hopefully cut down on users not being able to find where to assign mouse buttons or similar.
    * Make the key frame delete action also delete the associated layer and add a separate unassign key frame action that only gets rid of the key frame.
    * Move the timeline track manipulation buttons into the top-left corner of the timeline above the tracks which was previously just a blank space.
    * <a href="https://docs.drawpile.net/devblog/2026/03/16/dev-update.html#timeline-exposure-tool" target="_blank">Add an exposure tool to the timeline</a>, which allows shifting multiple frames around without keyboard shortcuts. It is also accessible by holding Alt.
    * <a href="https://docs.drawpile.net/devblog/2026/03/16/dev-update.html#timeline-zoom" target="_blank">Allow zooming the animation timeline.</a> There's a zoom menu on the timeline header now, you can use Ctrl+Mouse Wheel and you can bind keyboard shortcuts to it. Thanks Myathingoss for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/03/16/dev-update.html#flipbook-looping" target="_blank">Allow playing back and exporting the tail end of an animation loop</a> by setting the playback start larger than the end in the flipbook. This will play from flipbook range start to timeline range end, restarting from the timeline range start and playing until the flipbook range end, skipping the frames in the middle. Thanks Saphiros for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/03/16/dev-update.html#key-frame-move-locking" target="_blank">Allow locking frame dragging on timeline tracks</a> to prevent accidental frame moving, overwriting and changes in exposure. Thanks Saphiros for suggesting.
    * You can now configure the main menu bar actions in the shortcuts. They are also no longer dependent on which language you have Drawpile set to.
    * <a href="https://docs.drawpile.net/devblog/2026/03/16/dev-update.html#spinner-sliding" target="_blank">Allow dragging over numeric inputs to adjust their value.</a> They also now don't annoyingly select the prefix and suffix anymore when you click on them. Thanks LingjenKaos for suggesting.
    * Translate double-tap gesture on Huawei styluses on Android to the F25 key. Thanks noalero for suggesting.
    * Allow clearing log files in the Files preferences. This is particularly useful on Android, where you can't manually delete them (although they probably don't take up much space either way.)
    * Add "Anti-Strain", "Apple Pencil" and "Xiaomi Stylus" as a preset options for the global pressure curve.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Generate a session password if none is set, rather than spewing an error telling the user they need to go fix it themselves.</a>
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">When attempting to host a public session without a title, offer to host it invite-only instead of just showing an error.</a> Thanks hyper for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Move operator password settings to roles page, to avoid users mistaking it for the session password setting.</a> Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Show a warning that removing the password from a session will make it public.</a> Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Add a prompt to the invite dialog to make sessions passworded if they're public and a button to open the session settings</a>, to make those a bit easier to find. Thanks Bluestrings for suggesting.
    * Load brush preset data and thumbnails on demand instead of preloading them. This makes startup, switching tags and other operations that reload brushes much faster, especially if you have a lot of brushes.
    * Add sections to the brush editor settings list and group the settings accordingly. Thanks Blozzom for suggesting.
    * A notice in the invite dialog if the server or session doesn't support or restricts joining via web browser, with a prompt to use invite codes instead if appropriate. Thanks Bluestrings for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/27/dev-update.html#stabilizer-velocity-adjustment" target="_blank">Adjust stabilizer with velocity.</a> Enabled by default with a curve that lessens the stabilization for faster strokes, which makes it much more usable without having to constantly adjust the slider.
    * <a href="https://docs.drawpile.net/devblog/2026/05/10/dev-update.html#autoresume" target="_blank">Automatically resume drawings on Android</a>, since the system will terminate Drawpile when it's in the background without giving you a chance to save. To avoid this, cleanly exit the application via File → Quit or by pressing the back button. Thanks tiar for suggesting.
    * Provide a better default name by default instead of just punting to "Untitled". The suggested name is now automatically prefixed with a date and tries to use a cleaned-up version of the session title if drawing online. Thanks tiar for suggesting.
* Fixes:
    * Force canvas view dimensions to be even on hardware renderers, since otherwise the view gets scrunched on some graphics cards.
    * Make MyPaint brushes properly handle input values exactly on the point of a stair-step curve. Thanks Blozzom for testing.
    * Don't show MyPaint curves as continuing in a straight line outside the first and last point, since they don't.
    * Work around tablets not reporting when the eraser is brought near. Thanks Lauwenmark for reporting.
    * Work around some some Android devices eating three- and four-finger taps unconditionally. Thanks Afiq for reporting.
    * Don't try to set the one-finger touch input on Android according to whether the device says it has a stylus attached because devices just lie about it. It's always set to be dynamically detected by default now.
    * Make stylus buttons on some external tablets on Android work properly. The pen buttons used to not activate until pressing the pen down and release only if the pen was continued to be held. This is a patch to Qt.
    * Clamp OKLAB colors the proper way round. Thanks Bonbli for reporting.
    * Make setting kinetic scrolling to touch drag not trigger long-presses immediately on Android.
    * Properly clear invalid selection areas when masking brush strokes (shouldn't happen in the first place though.)
    * Make stylus buttons on Xiaomi devices act as right and middle clicks instead of page up and page down. Can be toggled in the tablet preferences. This is a patch to Qt.
    * Make lines not come out all jaggy on Xiaomi devices by ignoring the (wrong) tablet position history. Can be toggled in the tablet preferences. This is a patch to Qt.
    * Default the global pressure curve on Xiaomi devices to be really steep, because their stylus has a similarly high threshold as Apple Pencils do.
    * When saving a file, ask whether to overwrite it after confirming the format to avoid overwriting files unquestioned.
    * Properly preview editable fills when switching layers.
    * Disable the annoyingly slow and sometimes even crashy animations when rearranging docks and toggling toolbar extensions. They now just occur instantly instead.
    * Properly disable color marker and blending option buttons in the layer properties dialog when you don't have permission to modify those. Thanks xxxx for reporting.
    * Make bezier curve tool work with touch drawing. Thanks Notester32 for reporting.
    * Make refreshing flipbook not reset the playback to the beginning. Thanks BulletPepper for reporting.
    * Keep flipbook range to match the canvas range when it did so before even when closing the flipbook. Thanks BulletPepper for reporting.
    * Make fonts not be a wonky size on some Android devices.
    * Properly enable clipping and alpha lock controls in layer dock when switching from a non-editable to an editable layer. Thanks xxxx for reporting.
    * Don't clamp brushes with out of range inputs from the mere act of opening the brush editor. Thanks Phoneme for reporting.
    * Render repeated animation frames into exports, since some players get confused by frames held longer.
    * Use a fixed random seed for the brush preview so that it doesn't change erratically when adjusting a parameter, which made it hard to see what was actually changing.
    * Properly update alpha inherit icon when switching between dark and light themes. Thanks xxxx for reporting.
    * Center brush dock thumbnails instead of having them left-aligned. Thanks MorrowShore for reporting.
    * Handle additional stylus buttons on Android correctly. This makes some three-button styluses no longer interpret two of the side buttons as middle mouse.
    * Show correct MyPaint outline size when switching tools. It could sometimes end up showing an unadjusted size.
    * Properly mark MyPaint brushes as having been modified when modifying inputs other than pressure.
    * Don't limit flipbook range to 99 when opening it.
    * Make color selection in annotation tool asynchronous so that it doesn't crash in the browser. Thanks Curiosity for reporting.
    * Make status bar not end up huge when reattaching chat. Thanks hpar and xxxx for reporting.
    * Slow down the update rate of the status bar, since it causes performance issues on some devices. Thanks Liz and Hyper ifg for reporting.
    * Don't focus flipbook when it's already open to allow refreshing it without it taking away the keyboard focus from the main window.
    * Make lone presses of the Alt key not focus the menu bar, since that interferes with shortcuts.
    * Don't consider the canvas eligible for long-pressing to open a (nonexistent) context menu.
    * Ignore motions right before releasing a numeric slider so that lifting the stylus doesn't annoyingly nudge the value off what you meant to pick.
    * Some text input on Android where spacebar wouldn't work, the view would turn blue on some devices, the text area would block stylus input or the text menu would cover up the text.
    * Handle F13 to F24 keys on Android and translate F21 to middle click by default. This is a workaround for OnePlus devices that inexplicably press this keyboard key when you press the button on their stylus. Thanks Clover\_Yan for reporting.
    * Translate transforms with oversized selection masks to cut and paste operations instead of cancelling the transform. Thanks phanie for reporting.
    * Properly reset user id after leaving an online session and opening a file or creating a new image in the same window. Previously you would count as different users in different contexts, leading to permissions appearing wrong and your own strokes getting a user marker. Thanks grimsley for reporting.
    * Occasional crashes when using anti-overflow with a non-zero expand value at the edge of the canvas. Thanks Ausjamcian for reporting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#synchronized-smudging-speedups" target="_blank">Immediately send local drawing commands from freehand strokes to the paint engine.</a> This makes synchronized smudging way faster on some devices (and no perceptible difference on most others.)
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#synchronized-smudging-speedups" target="_blank">Cancel strokes lingering from synchronized smudging when a new one is started.</a> This prevents long-running strokes from just taking forever to finish and prevents the program hanging in some pathological cases.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#synchronized-smudging-speedups" target="_blank">Don't enable synchronized smudging on MyPaint brushes that don't have it explicitly set and only have infinitesimal smudge factor.</a> There's several brushes where all it does is slow down the stroke with no perceptible difference.
    * Set frame ranges properly when only changing one side of the frame range in a session that doesn't have both sides set yet. Thanks dAVePAGE for reporting.
    * Properly load frame ranges from ORA files that don't have any timeline defined.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Default session host type to passworded instead of remembering that you had it set to public.</a> This is a safer option than accidentally hosting something in public you didn't mean to and ending up in a panic trying to get the strangers out. Thanks Bluestrings and watt for reporting.
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#passworded-session-improvements" target="_blank">Change the wording on public and passworded session options to make it clearer what they do.</a> Thanks Bluestrings, hyper and tiar for suggesting.
    * Close invite dialog when disconnecting.
    * Don't change current brush when using the brushes dock's search bar.
    * Allow skipping around in the playback dialog again. This was caused by the check whether the canvas size is valid or not being flippe the wrong way round. Thanks Saova for reporting.
    * Properly preview lines, curves, circles and rectangles when using a brush with smudging turned on. Thanks retarj\_o\_burro for reporting.
    * Don't clear save paths when reconnecting to a session. This was particularly annoying on Android, since you can't save over existing files there. Thanks tiar for reporting.
    * Make automatic switching to frame view mode work properly even when the timeline isn't a floating or tabbed widget. The lack of a tab bar caused it to get misdetected as hidden.
    * Solve an issue where on some Android devices you would get disconnected on the first attempt of joining a session and then it worked fine on reconnect. Thanks Bluestrings for reporting.
    * Allow unsetting default layers again. Previously that operation got incorrectly filtered out as attempting to set the default layer to an invalid id.
    * <a href="https://docs.drawpile.net/devblog/2026/05/10/dev-update.html#initial-layer-selection-correction" target="_blank">Select the bottom-most layer to start with if no default layer is set.</a> Previously you'd end up on the newest layer, which was unpredictable and often enough confounding if you ended up on somebody's shading layer or similar.
    * Properly hide and lock drawing on hidden layers in frame view. Thanks hipofiz for reporting.
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2026/05/10/dev-update.html#sessionlessness" target="_blank">Allow disconnecting clients that linger too long without a session</a>, either before joining/hosting one or after having left. The duration is configurable by server owners, not limited by default.
* Server Fixes:
    * Only show the fact that a session was reported in the event log, but leave the details to only be visible to the server owners. Thanks Liz for reporting.
    * Log streamed resets being blocked properly. Thanks grimsley for reporting.
    * Properly disconnect notify all clients when a session is shut down. Previously it could miss some of them and leave them lingering without a session.
* Removed Server Features:
    * <a href="https://docs.drawpile.net/devblog/2026/04/13/dev-update.html#block-new-joins-removal" target="_blank">Closing sessions, called "block new joins" in the client.</a> It's just a worse variant of setting/changing the password on the session to make it invite-only. That has none of the downsides of locking yourself out, letting strangers join if they time it right and the session becoming public on its own after everyone has left.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Mohamed Elmogy and Shakhabit.
    * Brazilian Portuguese translation by Donizete J. R. Vida and Elliot S.
    * Catalan translation by Roger VC.
    * Czech translation by Pavel Borecki.
    * European Portuguese translation by ssantos and Victor Araújo.
    * German translation by askmeaboutloom.
    * Hindi translation by Chandramauli.
    * Indonesian translation by Arif Budiman and evan.
    * Japanese translation by ubanis.
    * Korean translation by Larry Choi, PIXELHIZE and Yeoleum.
    * Russian translation by Alevtina Karashokova.
    * Simplified Chinese translation by Wang Chenxzu and xxxx.
    * Spanish translation by Manuart.

## Acknowledgements

Thanks to everyone that has reported bugs, requested and discussed features, contributed code or documentation and otherwise helped with the development. Also thanks to those in the support channels helping out others and of course the administrators keeping the public servers running. And of course to those that have donated to the project.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
