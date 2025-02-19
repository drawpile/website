Slug: release-2.2.2-beta.5
Title: Version 2.2.2-beta.5, Safari Fixes and Web Updates
Publish: 2025-01-13 07:40:00+01:00
Visible: True
Author: askmeaboutloom
---

*Update on February 19, 2025:* you can now host personal sessions on the public Drawpile server using <a href="https://web.drawpile.net/" target="_blank">the web browser version of Drawpile</a>. Previously it only allowed you to join sessions.

*Update on February 15, 2025:* there's a bug in Safari 18 that prevented the web version of Drawpile from working on iPads. That's been worked around now and it should run again. Thanks grimsley and lunashadowbane for reporting and testing.

The third and, if everything goes to plan, final public beta of Drawpile 2.2.2 is out. You can **[download it in the Beta section on the downloads page](/download/#Beta)**. If you're updating from an earlier version, simply install the new one over it.

Everything in this beta is compatible. You can update to it and still draw with everyone that's on older versions, you'll just get to use all the new features and fixes. For example:

* <a href="https://docs.drawpile.net/devblog/2025/02/01/dev-update.html#multi-layer-selection" target="_blank">Multi-layer selection</a>, letting you rearrange, group, merge etc. many layers at once.
* New <a href="https://docs.drawpile.net/devblog/2024/11/08/dev-update.html#color-circle-dock" target="_blank">color cicle</a> and <a href="https://docs.drawpile.net/devblog/2024/12/14/dev-update.html#reference-dock" target="_blank">reference image</a> docks.
* A <a href="https://docs.drawpile.net/devblog/2025/01/25/dev-update.html#local-sketch-mode" target="_blank">sketch mode for layers</a>, letting you change the opacity and tint of a layer. This is only visible to you, so you can use it even on shared layers.
* <a href="https://docs.drawpile.net/devblog/2025/01/06/dev-update.html#quick-drag" target="_blank">Quick drag for selections</a>, letting you move stuff quickly without entering into a full transform.
* A much expanded <a href="https://docs.drawpile.net/devblog/2025/01/19/dev-update.html#host-page-rework" target="_blank">host session page</a>, with more sensible defaults and more options that previously you had to change in the session settings after hosting.
* Better tablet support, especially for Huion and Gaomon tablets.
* And much more, see below the fold for a full list. And of course everything that was introduced in previous betas, like reworked selections and transforms, getting rid of session autoresets and more.

If you find any issues, have questions or suggestions, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact.

## Changes in this Release

Drawpile 2.2.2-beta.5 represents about three months of development since Drawpile 2.2.2-beta.4. Numerous new features and fixes have been added during that time and, unless any issues are found, the next version should be the final 2.2.2.

---

Some of these have videos and pictures in the development blog, click on the links to get to them!

* Features:
    * <a href="https://docs.drawpile.net/devblog/2024/11/08/dev-update.html#color-circle-dock" target="_blank">Color circle dock with gamut masks, available through View > Docks > Color Circle. Similar to Krita's Artistic Color Selector and MyPaint's HSV/HCY Wheel.</a>
    * <a href="https://docs.drawpile.net/devblog/2024/11/16/dev-update.html#key-frame-layer-search" target="_blank">Add a search bar to the key frame properties dialog.</a>
    * <a href="https://docs.drawpile.net/devblog/2024/11/16/dev-update.html#drag-adjust-canvas-shortcuts" target="_blank">Add canvas shortcuts for changing color hue, saturation/chroma and value/lightness/luminosity.</a> Thanks Dann DecCairns for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/11/16/dev-update.html#drag-adjust-canvas-shortcuts" target="_blank">Make size adjustment canvas shortcut depend on the speed of the drag.</a> Thanks MorrowShore for suggesting.
    * Make list action buttons in settings dialog clearer, adding an edit button for canvas shortcuts. Thanks Maffi for suggesting.
    * Warn when an action will close a relevant window on Android and in the browser. Thanks 3rd\_EFNO for suggesting.
    * Show icons on dock tabs by default, rather than text that gets squashed. In desktop mode, this can be toggled via View > Docks > Show Icons on Tabs.
    * Replace "hold shift to arrange" with View > Docks > Arrange Docks, which doesn't require a keyboard. Thanks 3rd\_EFNO for suggesting.
    * Allow configuring temporary tool switch hold time. Thanks 3rd\_EFNO and pachuco for suggesting.
    * Tilt support on Android. Thanks MorrowShore and Verdrusk for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/12/14/dev-update.html#reference-dock">Reference image dock. Allows opening images in a separate dock and picking colors from them.</a> Thanks 3rd\_EFNO and leandro2222 for suggesting parts of this.
    * Make the canvas resize dialog fit to a floating transform, if present. This allows you to paste an image larger than the canvas and then resize to fit. Thanks Meru for suggesting.
    * Add --pass/-p option to dprectool, to allow configuring which messages are passed through when converting. The default is to pass all messages through, rather than just messages relevant for the client.
    * Right-clicking outside of a transform now applies it. Thanks MorrowShore for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/01/06/dev-update.html#quick-drag" target="_blank">Allow dragging selections to quickly move their contents without having to double-click to deselect and dragging the edge to move the selection itself without its contents.</a> Thanks Blozzom, Lungy, MorrowShore, SadColor and Zheida for suggesting and testing.
    * Add -I/--interpolation option to the drawpile-cmd and drawpile-timelapse commands, to allow using better scaling than bilinear if appropriate. Thanks Saphiros for causing this.
    * Show different cursors for selection replace, unite, exclude and intersect operations. Thanks MorrowShore for suggesting.
    * Raise default undo limit to 60 instead of 30.
    * <a href="https://docs.drawpile.net/devblog/2025/01/19/dev-update.html#host-page-rework" target="_blank">Expand the Host tab in the start dialog, allowing setting up sessions in advance and separating personal from public sessions better.</a>
    * Remember background color as well when using per-slot colors.
    * Allow editing brush names, descriptions and thumbnails when using detached slots.
    * <a href="https://docs.drawpile.net/devblog/2025/01/25/dev-update.html#local-sketch-mode" target="_blank">Allow toggling a "sketch mode" on layers, which will change the opacity and/or tint the layer locally. The exact look of this can be configured in the layer properties.</a> Thanks abrasivetroop and leandro2222 for suggesting.
    * Use the sketch mode tinting for onion skins as well, since it gives better results when there's colored areas involved.
    * Add File > Export Again to let you export to the same file without showing a file picker. Thanks gerroon for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/02/01/dev-update.html#multi-layer-selection" target="_blank">Allow selecting and then moving, grouping, deleting etc. of multiple layers at once. To select multiple layers, hold Shift or Ctrl while making a selection or use the boxes on the right.</a> Thanks MorrowShore for suggesting parts of this.
    * <a href="https://docs.drawpile.net/devblog/2025/02/01/dev-update.html#drag-visibility-toggle" target="_blank">Allow dragging across the layer icons to hide the visibility of multiple layers in a row, rather than having to click each one.</a> Thanks MorrowShore for suggesting.
    * The fill and magic wand tools now always at least fill the initial pixel if gap closing or shrinking would up with a blank result. Thanks MorrowShore for suggesting.
    * Add Blue Apatite, Indigo, Ocean Deep, Pool Table, Rose Quartz, Rust and Watermelon color schemes. Thanks Weenifer for contributing.
* Fixes:
    * Make temporary tool switches by holding a key down work again. Thanks 3rd_EFNO and bunnie for reporting.
    * Disregard hidden layers when layer picking in frame view.
    * Reset locale to "C" after Qt messes it up on startup. Thanks Meru for reporting.
    * Don't use bilinear interpolation in transforms unnecessarily.
    * Remove pointless permissions on Android that Qt includes by default but aren't actually used.
    * Don't default Android to fingerpaint when a pen is present.
    * Work around a crash on Android that sometimes occurs when putting your palm on the screen, which somehow leads to touch events with zero contact points. Thanks Mav for reporting.
    * Uncap aspect ratio on older Android versions. Thanks Molderche for reporting.
    * Work around modifier keys not registering when using a tablet on Wayland. Thanks Absolute Goober for reporting.
    * Don't crash when filling with feathering and a canvas-filling selection. Thanks Meru for reporting.
    * Don't carry over HUD button presses to dock UI in small screen mode. Thanks Meru for reporting.
    * Work around broken transparency when copying images between canvases on Wayland. Thanks Absolute Goober for reporting.
    * Properly ignore system tablet events when using KisTablet drivers on Windows. Thanks Doc for reporting.
    * When enabling a dock and it gets put into a tab, that tab now gets activated.
    * Properly pass tilt and barrel rotation values to MyPaint brushes. Thanks MorrowShore for reporting.
    * Always show color dialogs in HSV color space, since they don't behave correctly in other spaces. Thanks Meru for reporting.
    * Apply pending fills when manipulating layers. Thanks MorrowShore for reporting.
    * Make clicking and dragging fill and magic wand tools work at all zoom levels and drag speeds.
    * Try to retain dock arrangements after resizing the window, the Windows on-screen keyboard squashing the application or rotating a device/monitor. They should no longer remain squished to a smaller size after resizing the window back. Thanks vipperz for reporting.
    * Work around Android devices reporting way too huge motions when panning with two fingers. Thanks quandaledingle44 for reporting.
    * Don't mark the canvas as saved if it was only exported.
    * Round colors to 8 bits in fill and magic wand tools so that they don't get snagged on color differences too small to see on screen. Thanks vipperz for reporting.
    * Don't add blank filenames to recent files list. Thanks Aries Raenidaez for reporting.
    * Don't reset zoom and rotation when lifting and replacing one of two fingers in a pinch or twist operation. Thanks Partack for reporting.
    * Stop tap-and-hold color picking when another finger is added.
    * Use Normal blending in Layer View and Group View modes. Thanks Meru for reporting.
    * Take canvas rotation, mirror and flip into account with regards to pen tilt inputs.
    * Adjust minimum resolution for desktop-screen mode to be a bit larger, to avoid getting a cut-off desktop UI on some phones.
    * Don't cut off the bottom of dialogs on some Android phones. Thanks Anonymous, Bluestrings and Molderche for reporting.
    * Work around Gaomon tablets reporting pen buttons as mouse inputs. They were getting ignored because of an earlier Huion bug workaround.
    * Replace sound playback implementation on Windows to avoid mysterious crashes on some systems. Thanks Anonymous for reporting.
    * Properly put an undo point before layer property changes. Thanks Maffi for reporting.
    * Scroll to the brush in question when creating or overwriting one.
    * Make next/previous brush and tag shortcuts work when using detached slots.
    * Work around the web browser receiving messages while the application is handling messages already. This could cause nonsensical errors like "incompatible server" or "invalid state" or outright crashes during login.
    * Properly save background color of annotations in ORA files.
    * Properly update rotation when choosing an angle from the drop-down in the status bar when the angle is fractionally off the chosen angle. Thanks annoy for reporting.
    * When setting the canvas background color, the dialog now properly previews colors with alpha instead of showing them as opaque.
    * Properly save flipbook crop for when cropping multiple times without resetting in-between. Thanks BornIncompetence for reporting.
    * Properly apply transforms if the only thing you change is the opacity or blend mode. Thanks Blozzom for reporting.
    * Use the Fusion style by default on macOS because the System style has crashing bugs when using it with Sidecar. Thanks Axocrat for reporting.
    * Make the software renderer not create errant dark lines when moving the cursor when fractional scaling is involved. Thanks lambda20xx for reporting.
    * Remove nonsensical license page from Windows installer, Drawpile isn't under the kind of license that requires the user to accept it.
    * Properly open ORA, PSD and brush pack ZIP files when dragging them over the window. Thanks MorrowShore for reporting.
    * Don't show laser trails while catching up. Thanks MorrowShore for reporting.
* Server Features:
    * Allow two-way chat in web admin, letting admins talk to sessions without having to intrude on them. Thanks Bluestrings for suggesting.
    * Show better messages when a session reset happens, specifying if it's compressing, reverting or replacing the canvas. Thanks MorrowShore for suggesting.
    * Treat invalid password and opword hashes in session templates as plain passwords. This still issues a warning, since those kinds of passwords should really be specified by prefixing them with "plain;".
    * Allow authOnly option in session templates.
    * Inform clients of session password changes so that they can update their invite links.
    * Allow filtering server logs via the web admin API. Thanks Bluestrings for suggesting.
    * Allow locking admin API sections to prevent changes on them, optionally with a password that needs to be entered to unlock them.
    * Only treat WebSocket connections from browsers (based on the presence of an Origin header) as requiring extra permissions, to allow desktop and mobile clients to connect via WebSockets without being subjected to extra restrictions.
    * Allow hosting passworded sessions via the browser if password-dependent sessions are enabled, rather than refusing hosting altogether.
    * Allow restricting connections to the correct host name as passed with --local-host. Enabling this requires an updated client, since older ones don't transmit the hostname.
* Server Fixes:
    * Don't pointlessly reload server certificates if they didn't change. Thanks Liz for reporting.
    * Work around too many authenticated users in a session, which could cause a crash. Thanks Liz for reporting.
    * Don't transmit ban lists and logs to non-operators. Thanks Ryngtail for reporting.
    * Don't filter out feature access messages when loading session templates, so that permissions can actually get set properly from them.
    * Make template sessions not appear with a blank title and settings when first joining them.
    * Properly include web socket allowance in template session listings.
    * Allow joining a non-instantiated templated session via a direct link to its alias, rather than telling the user that the session isn't up.
    * Properly start recordings for sessions instantiated from a template.
* Translations (note that only translations that are completed to a signficant degree are included in the program):
    * Arabic translation by Blozzom.
    * Brazilian Portuguese translation by Lil S.
    * Finnish translation by Ricky Tigg.
    * French translation by Floch.
    * German translation by askmeaboutloom.
    * Indonesian translation by Rayytra.
    * Italian translation by Albano Battistella and Kekko.
    * Japanese translation by ubanis.
    * Korean translation by Skyblue Sky.
    * Russian translation by Meiren.
    * Simplified Chinese translation by xxxx.
    * Spanish translation by natkai, ofinxaip, Paico and Rockhopper.
    * Turkish translation by Oğuzhan Uyar.
    * Ukranian translation by Maksim Gorpinic.

## Acknowledgements

Thanks to everyone that helped test things, reported issues, suggested features and otherwise contributed to Drawpile's development. Thanks to the moderators and community administrators that keep the public servers running.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
