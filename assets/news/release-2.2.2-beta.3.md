Slug: release-2.2.2-beta.3
Title: Version 2.2.2-beta.3
Publish: 2024-08-09 18:40:00+02:00
Visible: True
Author: askmeaboutloom
---

The first public beta of Drawpile 2.2.2 is out. You can **[download it in the Beta section on the downloads page](/download/#Beta)**. If you're updating from an earlier version, simply install the new one over it.

This beta is fully compatible with the previous version. You can update to it and still draw with people that are using the main version, you'll just have more features than them. For example, better selections, the ability to transform multiple layers and groups simultaneously, better tablet support and more. **<a href="" target="_blank">Here's some illustrations and videos about what's new.</a>**

If you find any issues, have questions or suggestions or need any help, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact.

Also, if you're wondering, the version number is beta.3 because 1 and 2 were not announced publicly, they were used for preliminary testing. So you didn't miss anything in that regard.

## Changes in this Release

Drawpile 2.2.2-beta.3 represents about six months of development since Drawpile 2.2.1. There's been lots of new features added and bugs fixed.

---

Where appropriate, there'll be links to pages showing off these features.

* Platforms:
    * There's now a macOS version built for Apple Silicon Macs. The Intel Mac version will continue to be available.
* Features:
    * <a href="https://docs.drawpile.net/devblog/2024/02/24/dev-update.html#certificate-handling" target="_blank">Indicate the difference between self-signed and "real" server certificates.</a>
    * <a href="https://docs.drawpile.net/devblog/2024/02/24/dev-update.html#dual-color-button" target="_blank">Add a dual color button, showing the foreground and background color, with the ability to set, swap and reset them.</a>
    * Add "merged without background" as a source for the flood fill tool.
    * Allow choosing a different cursor for erase and alpha locked brushes. Thanks Hipofiz and Rylan for suggesting.
    * Ignore inputs with invalid pressure during strokes. Thanks Lunalatte for reporting.
    * Lock canvas when the session is out of space, showing an appropriate message in the corner, rather than letting you continue drawing. The server needs to be updated for this to be available.
    * Add a message to the reset dialog that you need to be an operator to reset the session, since it's not too clear why the button is disabled otherwise.
    * Make fill source selection a set of buttons for merged image, merged without background and layer, using the dropdown only for the latter thereof. The checked button will be remembered. Thanks Blozzom, Bluestrings and Meru for suggesting.
    * Default redo to both Ctrl+Y and Ctrl+Shift+Z on Windows, Linux and the browser. Thanks Crow for suggesting.
    * Allow configuring the transparency checkerboard colors in the user interface preferences. Thanks lungy for suggesting.
    * Allow copying multiple entries from the event log. Thanks Bluestrings for reporting.
    * Allow toggling vertical sync in the user interface preferences. Default is off, because it can cause input lag.
    * New hardware and software canvas renderers. The hardware renderer is much faster than the old one, especially in the browser. Uses Direct3D on Windows, WebGL in the browser and OpenGL on all other platforms. The software renderer is slightly faster than the old one, useful for cursed hardware or drivers that cause input lag or visual glitches. This is an experimental feature and can be enabled in the General preferences under Renderer.
    * Add system information dialog under Tools > Developer Tools > System Information.
    * <a href="https://docs.drawpile.net/devblog/2024/04/04/dev-update.html#user-pointer-evasion" target="_blank">Hide user pointers when they get close to your cursor. Can be toggled under View > User Pointers > Hide From Cursor.</a> Thanks Crowley for suggesting.
    * Allow filling non-continuous areas. Thanks Ben for suggesting.
    * Allow disabling the zoom, rotation, mirror and flip on-canvas notices in the User Interface preferences. Thanks Partack for suggesting.
    * Allow configuring user pointer stay time through View → User Pointers → Stay Time. Thanks johannesCmayer for suggesting.
    * Allow prompting for layer properties when creating a layer. Can be turned on in the User Interface preferences. Thanks Ben for suggesting.
    * Name layers after the username of the creator by default.
    * Don't require restarting the application when changing kinetic scrolling settings.
    * Don't require restarting the application to switch between desktop and small screen mode. There's also a "dynamic" option now, which will change the mode based on the size of the window, enabled by default on Android and in the browser.
    * Pan or "hand" tool. Lets you move the canvas around by clicking. Thanks DeeJii for suggesting.
    * Show a proper explanation when you can't join a session.
    * On Windows and Linux, new windows now open in a separate process, since that's more efficient and resilient. Can be disabled by setting the DRAWPILE_SINGLE_PROCESS environment variable. Thanks Bluestrings for suggesting.
    * Disable global smoothing for mouse drawing by default, since that really only make sense for tablets and touch. Can be toggled in the input preferences. Thanks nililfin for suggesting.
    * Always show drawing tools toolbar in small screen mode. Thanks Blozzom for suggesting.
    * Make canvas zoom slider use the same increments as the mouse wheel and zoom in/out actions, since stepping by 1% is not useful. Thanks zheida for suggesting.
    * Pixel ruler, available under View > Show Rulers. Thanks fluttershydev for contributing.
    * Translate links copied out of the browser version of Drawpile into something that can be joined when they are pasted into the join page.
    * Better small-screen mode handling. The toggle items now no longer overlap, dialogs get maximized if appropriate, the start and settings dialogs get arranged horizontally.
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#better-selections" target="_blank">Rework selections and transforms entirely. They're now distinct operations. Selections participate in the undo stack.</a>
    * Allow toggling between accurate and fast transform previews. The former is the current kind of preview that actually gets previewed on the layer, the latter is like in Drawpile 2.1, where it's just a vector image drawn on top of everything.
    * Allow picking blend modes and opacity when pasting, stamping and transforming. Thanks blurymind for suggesting.
    * Show layouts action in dock menus. Thanks Elisa for suggesting.
    * Build option -DPROXY\_STYLE=ON to fix the bad contrast in dark themes when not building a patched version of Qt yourself.
    * Indicate fill source in layer list.
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#improved-transforms" target="_blank">Allow transforming multiple layers at once.</a>
    * Make creating a key frame layer copy the layer structure of the closest frame if that's assigned to a layer group. Thanks Ausjamcian for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#more-animation-imports-and-exports" target="_blank">Allow importing animation frames from multiple files and as layers from PSD files, to be found under File -> Import.</a> Thanks Meru, BulletPepper, Ben and RubberRoss for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#more-animation-imports-and-exports" target="_blank">Extend animation export to be a dialog where you pick the format. You can now export frames to a ZIP, allowing Android and the browser to save a series of frames as well. Exporting to MP4 and WEBM videos as well as animated WEBP is also implemented via ffmpeg's libraries.</a>
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#magic-wand-tool" target="_blank">Magic wand select tool. Basically a fill tool, but for selections.</a> Thanks ChristianJohnsten for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/08/09/beta.html#extended-fill-tool" target="_blank">The fill tool now previews fills instead of doing them immediately, allowing cancelling and changing layers before applying it. You can also pick more blend modes, change the opacity and fill the entire selection with it now.</a>
    * Add View > Show Selection Mask, which lets you view selections as a solid mask instead of an outline. This lets you see opacity properly.
    * Allow shrinking fills and magic wand selections. Thanks Meru for suggesting.
    * New dialog Selection > Expand/Shrink/Feather Selection that alters selections accordingly. Thanks MorrowShore for suggesting.
    * Zooming with keyboard shortcuts now zooms in on the cursor when it's pointing at the canvas. If you don't like this, there's new shortcuts that always zoom on the center, which you can bind in the preferences. Thanks Chryssabliss for suggesting.
    * Make header and footer buttons on docks stretch further if there's empty space, making them easier to hit. Thanks MorrowShore for suggesting.
    * Make color sliders dock smaller by showing only one set of sliders at a time and add an input field for a hex color name. Thanks Kawaxte and MorrowShore for suggesting.
    * Don't pop open chat for session auto-resets, just show a note in the corner of the canvas. Needs both client and server to be updated.
    * Support reading and writing WEBP files.
    * Enable high-DPI scaling by default on all platforms except Android. Can be disabled in the user interface preferences if needed.
    * Turn too large transforms into cut and paste operations instead of cancelling them outright.
* Fixes:
    * Don't mess up strokes when hitting undo while still actively drawing them. Thanks Sinamer for reporting.
    * Properly reset angle when undoing a point with the curve tool.
    * Rename "trusted hosts" to "pinned certificates", because that's what they are.
    * Make floating docks stay on top of the main window on macOS. Thanks 6ix for reporting and testing.
    * Make WebSockets compile under Qt < 6.5. Thanks kiroma for reporting.
    * Show web join allowance checkbox in session settings properly, it didn't show up if disabled before.
    * Load annotations from ORA files saved by Drawpile 2.1 properly. Thanks RyanMolyneux for reporting.
    * Brighten up transparency checkerboard to be a bit easier on the eyes. Thanks Crow for suggesting.
    * Don't fail server compilation when turning off webadmin or WebSockets. Thanks leegean for reporting.
    * Save and load annotation vertical alignment to and from ORA files.
    * Put a transparent background behind flat images, rather than using white. Thanks lungy for reporting.
    * Make pasting images from Drawpile into other applications retain transparency on Windows. This is really a bug in those other programs, they pick the wrong format by default, but whatever. Thanks lungy for reporting.
    * Don't reselect and scroll back to default layer after interacting with the layer list by picking a layer or toggling visibility. Thanks MachKerman and Ben for reporting.
    * Load PNGs even when they have corrupt checksums. Thanks xxxx for reporting.
    * Make rotation via View > Rotation > Rotate Canvas (Counter-)Clockwise work properly when it's mirrored or flipped. Thanks Ragged for reporting.
    * Focus existing layer properties dialog if one exists for the layer that properties are requested for.
    * Don't use bilinear interpolation when selection is only moved, rotated by a multiple of 90 degrees, flipped or mirrored, to avoid unnecessary blurring. Thanks lungy for reporting.
    * Change default canvas size to 2000x2000, because 800x600 is a bit outdated. Thanks MorrowShore for for contributing.
    * Don't move view position when pressing side buttons in small screen mode.
    * Make autosave interval actually be in minutes, not in seconds because that's ridiculous. Thanks D'mitri for reporting.
    * Reduce contrast on censor tile stripes to make them less annoying to look at.
    * The main window should now properly restore to its previous position even when that's on a secondary screen. Thanks Moe for reporting.
    * Increase contrast on depressed buttons in dark themes. This is a patch to Qt. Thanks MorrowShore for reporting.
    * Switch out the icon for the extension buttons on squashed menus and toolbars so that they're actually visible in dark themes. This is a patch to Qt.
    * Work around a crash on Linux that happens when hosting with busted versions of Qt 6.6+. Thanks Vanska for reporting.
    * Allow tabbing the main window on macOS again, for some reason Qt disabled it. This is a patch to Qt. Thanks mira for reporting.
    * Ignore mouse clicks caused by briefly touching the canvas on some devices on Windows. Thanks sfin for reporting.
    * Set TCP\_NODELAY on sockets to reduce unnecessary latency.
    * Disable the image memory limit when using Qt 6, because that breaks the loading large files. Thanks LiterallyMe for reporting.
    * Make canvas lock and layers not lock tools that don't actually act on them.
    * Don't overwrite last file on save after resetting the canvas to an external image. Thanks Bluestrings for reporting.
    * Ignore bogus mouse clicks emitted by some tablets after briefly tapping the pen on them. Thanks Ausjamcian for reporting.
    * Make the window fit itself to the screen harder in the browser and on Android. There's also an option under View -> Fit to Screen now to manually force it to do so. Thanks Sidca for reporting and Meru for testing.
    * Properly remember NSFM setting in host dialog. Thanks Bluestrings and cupcake for reporting.
    * Properly check NSFM setting in host dialog based on title if that is configured in the parental controls preferences. Thanks Bluestrings for reporting.
    * Behind blend mode now does opacity math correctly. Thanks Blozzom for reporting.
    * Allow cancelling fill tool with right-click even when that's bound to something else. Thanks SadColor for reporting.
    * Make layer picking work properly in frame mode, it picked the bottom-most instead of the top-most one.
    * Make the fill tool not feather along canvas edge. Thanks Meru for reporting.
    * Properly truncate files when writing them on Android to avoid corruption from leftover junk at the end.
    * Compensate for discontinuity in the classic soft brush radius to make the transition look less bumpy. Thanks BulletPepper for reporting.
    * Don't switch tools while typing into text fields in some situations. Thanks leopardheart982 for reporting.
    * Give color wheel, color palette and navigator docks a minimum size so that they can't be shrunken into nonexistence. Thanks vipperz for reporting.
    * Don't remove layer censors when resetting sessions hosted on the builtin server. Thanks O\_O for reporting.
    * Default kinetic scrolling on Android to touch instead of left click, since the latter conflicts with stuff like dragging layers.
    * Allow importing role lists larger than 100 entries, since public sessions have those. Thanks kale for reporting.
    * Use more accurate timers for performance profiles if the platform supports it.
    * Don't try to update the roles list before becoming an operator, which could lead to a crash. Thanks Bluestrings for reporting.
    * Don't update sessions that were just added to the session browser, since that can lead to a crash because of what is probably a bug in Qt's filtering and sorting. Thanks Bluestrings for reporting.
* Server Features:
    * Allow adding a message when kicking someone through the admin API.
    * Log more a more detailed reason when a client is disconnected, since something like a login error can have many causes.
    * Warn if a command-line argument was ignored due to systemd sockets being used instead.
    * Allow making joining via the browser dependent on if the session has a password or not.
    * <a href="https://docs.drawpile.net/devblog/2024/03/16/dev-update.html#telefragging" target="_blank">Allow registered users to replace themselves when rejoining a session, rather than telling them that their own name is in use. Avoids having to wait for their old self to time out if their internet flakes.</a> Thanks Crow for suggesting.
    * When you pass an option that's not compiled in, the error message will not inform you of that fact, rather than just saying you passed an unknown option with no further information.
    * Allow specifying idleOverride and allowWeb in session templates. Thanks MorrowShore for suggesting.
    * Allow changing session founder names through the admin API.
* Server Fixes:
    * <a href="https://docs.drawpile.net/devblog/2024/03/09/dev-update.html#proper-size-limit-handling" target="_blank">Handle sessions running out of space better, they should no longer end up in an unrecoverable state. The messages in chat are also now translatable, more informative and don't get spammed for every command.</a> Thanks Bluestrings and Charmandrigo for reporting.
    * Include allow web flag when listing a session.
    * Update active drawing users when refreshing a session listing.
    * Properly start extbans checks when running via systemd. Thanks Bluestrings for reporting.
    * Properly sever connections on read, write and timeout errors.
    * Make catchup not take pointlessly long when the session is out of space.
* Tool Features:
    * Add -U/--uncensor parameter to drawpile-timelapse to allow revealing censored layers.
    * Allow cropping in the drawpile-timelapse command-line tool using -x/--crop.
* Removed Features:
    * <a href="https://docs.drawpile.net/devblog/2024/04/17/roomcode-removal.html" target="_blank">Roomcodes. They are a vestige from a time where Drawpile only had a single, central listing server. Nowadays nobody uses these anymore, invite links are the replacement.</a>
    * Zeroconf support, an obscure LAN-only discovery thing that wasn't working anymore anyway.
* Translations:
    * Arabic translation updated by Blozzom.
    * Brazilian Portuguese translation updated by Kett Lovahr.
    * Esparanto translation added by phlostically.
    * French translation updated by Franky Funky.
    * German translation updated by askmeaboutloom.
    * Indonesian translation added by Reza Almanda
    * Italian translation updated by albanobattistella.
    * Norwegian Bokmål translation updated by Mijhael Hansen.
    * Japanese translation updated by ubanis.
    * Russian translation updated by Leaftail and Timofey Bezruchenko.
    * Simplified Chinese translation updated by xxxx and 王晨旭.
    * Ukranian translation updated by neketos851.
    * Thai translation added by Morrow Shore.
    * Turkish translation updated by duennisss.

## Acknowledgements

Thanks to everyone that helped with this release of Drawpile, be it through contributing code, reporting bugs, suggesting features, organizing, helping people who ask questions and anything else. Also special thanks to the community admins that keep the servers running.
