Slug: release-2.3.0-beta.1
Title: Version 2.3.0-beta.1 and Donations
Publish: 2025-08-06 12:00:00+02:00
Visible: True
Author: askmeaboutloom
---

The first beta of Drawpile version 2.3.0 is out now. It has many new features, such as **layer clipping**, **lasso fills**, **a gradient tool**, **realistic pigment blending**, **OKLAB mode**, **pixel-perfect mode**, **a new file format that's 3000% faster** and much more. There is also **a version for Windows on ARM** now, if you have such a device. And of course numerous fixes and stability improvements. It is **backward-compatible**, so you can join sessions hosted with the previous version.

**[Click here to download and install it](/download/#Beta)**. You can use both the current and the beta version side by side, the beta uses a different icon so you can tell them apart. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to that</a>.

To find out what's new, <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">take a look at this page</a>. It has videos and pictures showing everything off.

You can also now <a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donate to the project</span></span></a>! Drawpile is largely developed by only a single person, donations let me spend more time working on it and helps pay to keep the servers running.

If you have questions, feedback or trouble using the new version – especially if it breaks your workflow – take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact! Almost every feature is added because it was requested by an artist and bugs can only be fixed if they are reported, you can see everyone that contributed in the list of changes below.

## Updating or Installing Side by Side

You can **[download Drawpile from here](/download/#Beta)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

Alternatively, you can run both versions side-by-side. The beta uses a different icon so that you can tell the two apart. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to do that on different operating systems</a>.

On the server side, everything is both back- and forward-compatible. Server owners can update if they want, but it's not necessary, people can use any version they wish to host sessions.

## Changes in this Release

Drawpile 2.3.0-beta.1 represents a bit over 4 months of development since version 2.2.2. Many people contributed with suggestions and bug reports and are listed below. If you find any issues, please <a href="/help/" target="_blank">report them</a>!

For an illustrated list of the major changes, take a look at <a href="https://docs.drawpile.net/help/common/update2x3x2" target="_blank">this page</a>.

---

Where available, there's links to <a href="https://docs.drawpile.net/devblog/" target="_blank">the development blog</a> with more information.

* Features:
    * <a href="https://docs.drawpile.net/devblog/2025/03/29/dev-update.html#clipping-groups" target="_blank">"Clip to layer below"</a> toggle on layers, for people used to that way of alpha preserving. Will be loaded from and saved to PSD files.
    * <a href="https://docs.drawpile.net/devblog/2025/03/29/dev-update.html#explicit-alpha-preserve" target="_blank">"Inherit alpha" toggle on layers and "preserve alpha" toggle on tools, for people used to that way of alpha preserving from Krita.</a> You can toggle automatic alpha preserverance in the user interface preferences. Thanks Bubble for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/04/05/dev-update.html#markers-and-density" target="_blank">"Greater Density" blend mode, which will only draw where it will increase opacity.</a> Works like "Greater" in Krita and "Compare Density" in CSP, minus the glitches when you use different colors. Thanks Annoy suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/04/05/dev-update.html#markers-and-density" target="_blank">"Marker" blend mode, which will only increase opacity, but always change the color.</a> Works like the marker in SAI and sorta similar to "Alpha Darken" in Krita, minus the glitches for different colors again. Thanks cromachina for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/04/05/dev-update.html#paint-modes" target="_blank">Bring back the indirect normal mode from Drawpile 2.1 as another paint mode option.</a>
    * Allow using blend modes with MyPaint brushes, rather than restricting them to normal, recolor and erase.
    * Allow using MyPaint brush color dynamics in indirect mode.
    * Remember who changed tiles across session resets and compressing the canvas. Thanks Bluestrings for suggesting and callaa for originally implementing it before it fell off again for compatibility.
    * Make the Shine (SAI) blend mode work exactly like in SAI, even with alpha preserve off. Thanks cromachina for providing the logic for this.
    * Implement more blend modes: Vivid Light, Pin Light, Difference, Darker Color, Lighter Color, Shade (SAI), Shade/Shine (SAI), Burn (SAI), Dodge (SAI), Burn/Dodge (SAI), Hard Mix (SAI) and Difference (SAI). Thanks cromachina for providing the logic for the SAI blend modes.
    * <a href="https://docs.drawpile.net/devblog/2025/04/12/dev-update.html#bigger-brushes" target="_blank">Increase maximum brush size to 1000.</a> Session operators can limit this and the default limit for non-operators is 255. Thanks ariqhadiyan and TGS for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/04/12/dev-update.html#spectral-color-mixing" target="_blank">Pigment blend mode, which allows for more realistic color mixing.</a> Session operators can restrict this mode and by default it's only enabled for operators, since it's very performance-intensive. Thanks chaitae for suggesting, username and xxx for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/04/26/dev-update.html#layer-identification" target="_blank">Increase maximum layer count to 32767 per user, up from the previous 256.</a> Operators can also now limit the layer count in the session settings. Thanks haxekhaex2 for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/04/26/dev-update.html#selection-drawing" target="_blank">Allow drawing on selections via Selection → Draw on Selection.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/04/26/dev-update.html#selection-drawing" target="_blank">Allow changing the color of the selection mask via View → Set Selection Mask Color.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/05/03/dev-update.html#drawing-inside-selections" target="_blank">Make selections mask brush strokes.</a> Can be toggled via Selection → Mask Brush Strokes With Selection. Thanks Bluestrings for testing.
    * Switch pixel compression algorithm to zstd, which is many times faster than the old gzip. Thanks Bonbli for suggesting a way to get better compression with this.
    * Don't require paste permission for transforms that modify the opacity or blend mode.
    * <a href="https://docs.drawpile.net/devblog/2025/05/03/dev-update.html#layer-alpha-lock" target="_blank">Allow alpha locking layers.</a> This basically works the same as enabling alpha lock on the tool you're using, it's just there for people that are used to doing it this way from other programs.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#more-layer-locks" target="_blank">Allow locking layer properties to avoid accidentally changing e.g. the blend mode.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#more-layer-locks" target="_blank">Allow locking layer positions to avoid accidentally moving them.</a> Thanks Athena for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#long-long-canvas" target="_blank">Increase canvas size limit to up to 1 million pixels as long as the total canvas size doesn't exceed 1073676289 pixels (32767 squared).</a> Previously each dimension was limited to 32767 instead. Thanks johannesCmayer and yvantot for suggesting and MajorCooke for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#and-deselect" target="_blank">Add shortcuts that switch tools and deselect in a single action.</a> Thanks Bonbli for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#dpcs-file-format" target="_blank">New .dpcs canvas file format that's much faster and in most cases also leads to smaller sizes.</a> Thanks Bonbli for suggesting an optimization to this; CosmosX007, Fanshen and hpar for reporting issues.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#gradient-tool" target="_blank">A gradient tool, which works inside of selections.</a> Thanks ChristianJohnsten, lambda20x, Malrn and Maffi for suggesting.
    * Preview brushes with fixed X and Y offsets with an offset outline. Thanks Phoneme for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/05/17/dev-update.html#classic-jitter" target="_blank">Add jitter setting for classic brushes, available in the brush settings.</a> This setting offsets the dabs from the center of the stroke, useful for pencil, charcoal or spraycan brushes.
    * Show the time it took to open, save and export files in the status bar.
    * Make arrow keys navigate the animation timeline when it has focus. Thanks MorrowShore for suggesting.
    * Add support for opening and exporting images in Quite Okay Image Format (QOI).
    * <a href="https://docs.drawpile.net/devblog/2025/06/07/dev-update.html#smudge-sync" target="_blank">Add a "synchronize smudging" brush setting.</a> This will make the brush stroke wait for itself before smudging, which is slower, but required for some smudge brushes to work properly when making fast strokes. Thanks Donatello and xxxx for reporting.
    * <a href="https://docs.drawpile.net/devblog/2025/06/07/dev-update.html#classic-smudge" target="_blank">Allow classic brushes to smudge with transparency.</a> This can be toggled in the brush settings. The old mode now calls itself "blending" instead to be able to tell it apart. Thanks xxxx for suggesting and lambda20xx for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/06/07/dev-update.html#lasso-fill-tool" target="_blank">A lasso fill tool, bound to Shift+F by default.</a> Thanks EvilKitty3, Fallen, Geese, MorrowShore and Juzeror for suggesting, Blozzom and Bonbli for suggesting additions to it.
    * <a href="https://docs.drawpile.net/devblog/2025/06/07/dev-update.html#escape-selections" target="_blank">Allow pressing Escape (or whatever you bound "cancel action" to) to deselect.</a> Can be disabled in the tool preferences. Thanks RannyBergamotte for suggesting.
    * Upscale small animations by whole numbers to fill the flipbook view. Can be toggled using the zoom button at the bottom. Thanks Ian700ng for suggesting.
    * Allow assigning keyboard shortcuts to tool blend modes. Thanks Izzy and Meru for suggesting.
    * Show tooltips of tool buttons immediately, so that you can tell better what they do without having to wait for them.
    * <a href="https://docs.drawpile.net/devblog/2025/06/21/dev-update.html#harmony-swatches" target="_blank">Harmony swatches, showing color harmonies for the current color to make palettes or shade with.</a> Can be enabled and configured through the hamburger by right-click menu on the color wheel. Thanks tiar for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/06/21/dev-update.html#hide-your-tools" target="_blank">Add View → Always Show Side/Bottom Toolbar actions to let you choose whether to always show those toolbars in small screen mode or only when something is folded out using the tabs on the side.</a> Thanks CosmosX007 for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/06/21/dev-update.html#pick-your-tools" target="_blank">Allow reordering and toggling which drawing tools are visible in the toolbar, via e.g. Tools → Configure drawing toolbar.</a> Thanks MorrowShore for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/06/21/dev-update.html#oklab" target="_blank">Add OKLAB blend mode for layers and brushes.</a> Thanks Bonbli for contributing.
    * Auto-correct attempts to host on http(s) sites by extracting the host portion from them. Thanks Charmandrigo for suggesting.
    * Add shortcuts to change brush opacity and hardness. Thanks justanotatest for suggesting.
    * Allow defining a separate pressure curve for the stylus eraser tip in the tablet preferences. Thanks CosmosX007 for suggesting.
    * Allow turning off system file dialogs on Windows, in case they somehow cause trouble. Thanks CrustStuff for suggesting.
    * Allow swapping the sides of docks, toolbars and on-canvas buttons via View → Left-Handed Mode in small screen mode. Thanks yoossy for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/07/05/dev-update.html#redirects" target="_blank">Redirect handling in the client, allowing servers to forward connections to other servers, with the option of only accepting signed redirects.</a>
    * <a href="https://docs.drawpile.net/devblog/2025/07/19/dev-update.html#pixel-perfection" target="_blank">Add pixel-perfect option for pixel brushes, available in the brush editor and under the paint mode dropdown.</a> Thanks Meru and Squishy for suggesting, lan700ng for testing.
    * <a href="https://docs.drawpile.net/devblog/2025/08/02/dev-update.html#annotation-backgrounds" target="_blank">Use the canvas background color or the color behind the canvas as the background color for the annotation editor, depending on where the annotation is placed.</a> Thanks Blozzom for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/03/16/dev-update#lightnessdarkness-to-alpha" target="_blank">Add Edit → Lightness/Darkness to Alpha action.</a> Thanks Ben for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2024/03/16/dev-update#annotation-aliasing" target="_blank">Allow switching annotation rendering between vector, smooth and pixel fonts.</a> Thanks cvrsoiioo4 for suggesting.
    * Add a build for Windows on ARM. Thanks fizbin for testing.
    * Allow setting hostaddress, hostpass, username and userpass URL parameters in the browser, as a workaround for when you can't type anything into the text fields. Thanks N8theGr8 for bringing this up.
    * Let operators create annotations beyond the 256 per-user maximum. Like with layers, this will use annotations of user 0 first, then 255, 254 etc. Thanks to Devil Like Me for reporting.
    * <a href="https://docs.drawpile.net/devblog/2025/04/05/dev-update.html#color-marking" target="_blank">Assigning colors to layers and key frames.</a> Thanks MorrowShore and hpar respectively for suggesting.
    * Smoothing for touch panning, zooming and rotation. Can be configured and disabled in the touch preferences. Thanks Jay-Man for suggesting, 3rd_EFNO and lan700ng for testing.
    * Make Drawpile build on the Haiku operating system again. Thanks Begasus for contributing.
    * Add pressure tester to browser startup page. Thanks Shivani for contributing.
    * Add language selector to browser startup page.
    * Add a brush setting to disallow others in a session to use it. This does not prevent them from replicating the brush in other ways, but this setting is there if you feel strongly about not making it easy. Thanks Blozzom for suggesting.
    * Bind deselect to both Ctrl+Shift+A and Ctrl+D by default, since other software is inconsistent in this regard. Thanks Geese for suggesting.
    * Donation and feedback links. They don't cause any extra pop-ups, but if they annoy you regardless, they can be summarily disabled in the preferences.
* Fixes:
    * Change the dptxt recording format to use JSON to represent message bodies instead of a bespoke format that sometimes doesn't round-trip properly.
    * <a href="https://docs.drawpile.net/devblog/2025/04/05/dev-update.html#paint-modes" target="_blank">Make indirect wash mode actually work like it's supposed to, without causing weird effects for soft brushes. The previous mode is now available as a separate paint mode.</a>
    * Don't displace annotations when resizing the canvas to the left or top.
    * Make MyPaint brush outline more accurate to the actual maximum size of the brush (although it still can't account for crazier brushes.)
    * Don't mark the canvas as having unsaved changes from just making a selection on it. Thanks MachKerman for reporting.
    * Don't include credentials in the URL when opening a new window on reconnect, they're only for use in the same window. Thanks MachKerman for reporting.
    * Save and restore smudge minimum value properly instead of resetting it to zero.
    * Don't disconnect when receiving an unknown message from user 0. Thanks Blozzom and unsername for reporting.
    * Compensate jagged curves in when using the lasso select tool. Thanks Blozzom for reporting.
    * Properly stop flood fills at selection boundaries. Thanks Bluestrings for reporting.
    * Don't reattach detached brushes when switching slots. Thanks MachKerman for reporting.
    * Don't switch away from a detached brush when only right-clicking, just like it works when you disable brush detaching altogether. Thanks MachKerman for reporting.
    * Don't allow toggling toolbars in small screen mode, since they will just reappear again. Thanks CosmosX007 for reporting.
    * Add some space to the sides of the bottom toolbar in small-screen mode so that the undo and record buttons don't get eaten by rounded corners. Thanks March for reporting.
    * Detect eraser pen tip on Android, since the eraser doesn't report it's in proximity until it hits the surface, similar to the browser. Thanks CosmosX007 for reporting.
    * Remember loops field in animation export dialog during a single run, instead of resetting it to 1 every time.
    * Disable audio playback under 32 bit Windows, since it just crashes.
    * Clear text in the annotation tool when deselecting, since it makes it seem like you can still type in there.
    * Don't reselect default layer after picking a layer from the canvas or via the timeline. Thanks Meru for reporting.
    * Properly snap pixel brush outlines in the correct spot and don't snap soft brush outlines at all. Thanks Meru for reporting.
    * Disable color wheel preview on macOS, since it breaks dragging on the wheel like it does on Android. Thanks Millie for reporting.
    * Don't crash on some systems when selecting multiple layers and merging them. Thanks cromachina for reporting.
    * A rare crash when faced with a lot of identically-named brushes assigned to the same shortcut. Thanks Blozzom for reporting.
    * Allow changing the background color when you have background permissions, previously it checked for canvas resize permission instead.
    * Make fill tool apply to the layer it was executed on when "edit pending fills" is disabled. Thanks Greendyno for reporting.
    * Don't set a 0% opacity layer to 1% opacity when switching it out of sketch mode. Thanks Meru for reporting.
    * Properly reset layer visibility when creating a layer with the same ID as a previously hidden layer when you have a high-ish ping. Thanks MachKerman for reporting.
    * Don't start a kinetic scroll of the surrounding view when trying to adjust curve or slider. Thanks 3rd_EFNO for reporting.
    * Make MyPaint brushes not pick up transparency from outside of the canvas. Thanks Meiren and yvantot for reporting.
    * Properly render sketch mode layers when the actual layer opacity is zero.
    * Remove warning about Firefox on Android not supporting pressure sensitivity, since it does now. Thanks tiar for reporting.
    * Correct warning about Firefox on Linux not supporting pressure sensitivity, since it does work on some systems. Thanks Kuuuube for reporting.
    * Don't crash on macOS when inputting an invalid session address to join. Thanks Charmandrigo for reporting and Axocrat for testing.
    * Restore normal layer view mode when loading a canvas into the same window.
    * Replace the notification sound playback backend, which should make it work on Android, the Linux AppImage and on 32 bit Windows. It should hopefully also no longer have occasional crashes on some Linux and Windows systems.
    * Make click detection more sensitive, to avoid accidentally creating tiny selections when trying to just click to deselect. Thanks Bluestrings for reporting.
* Tool Features:
    * Add -B/--background-color option to drawpile-timelapse command to set an override background color. Thanks Bluestrings for suggesting.
* Server Features:
    * <a href="https://docs.drawpile.net/devblog/2025/07/19/dev-update.html#session-thumbnails" target="_blank">Session thumbnail generation, by requesting the client to generate one.</a> Currently only through the web admin API, thumbnails are not displayed anywhere or generated automatically yet.
    * Add settings to filter disallowed user and session names. Thanks Bluestrings for suggesting.
    * Allow marking individual sessions as unlisted, as well as a setting to automatically unlist all or browser-hosted sessions. Thanks Bluestrings for suggesting.
    * Allow adding server log entries via API. Thanks Bluestrings for suggesting.
    * Add a "browser" flag to the API, to be able to tell whether a user is connected via web browser.
    * Add a --no-gui option to explicitly run the server without a graphical shell.
* Server Fixes:
    * Properly prefer users with better OS, net quality or ping for autoresets, even if they responded first. Thanks Blozzom for reporting.
    * Interpret the connection quality setting sent by clients correctly when choosing who to pick for autoresets. Thanks Blozzom and grimsley for reporting.
    * The server now checks whether it can actually start with a GUI if you run it without arguments on Linux and other non-macOS Unix systems, rather than trying it and crashing because you don't have a graphical environment. Thanks Epiglottal Axolotl for reporting.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Ahmed Essam.
    * Brazilian Portuguese translation by Inky 1003 and Zeevee.
    * Catalan translation by Roger VC.
    * European Portuguese translation by ssantos and Victor Araújo.
    * French translation by Nicolas Rivard.
    * German translation by askmeaboutloom.
    * Gothic translation by Roel v.
    * Italian translation by Isy.
    * Japanese translation by ubanis.
    * Polish translation by Krzysztof Bursa, Kuba18 and tiar.
    * Simplified Chinese translation by xxxx.
    * Spanish translation by Manuart, Rockhopper and Shiki.
    * Turkish translation by polarwood.
    * Ukranian translation by Maksim Gorpinic and neketos851.
    * Vietnamese translation by BlackFire123654 and Cas Pascal.

## What's Next

Several fixes and a few of the features will be backported for another release in the 2.2 series, probably sometime soonish.

Work on 2.3.0 will continue, there is still a few more features that are slated to be included. For example, <a href="https://docs.drawpile.net/devblog/2025/08/02/dev-update.html#work-in-progress-brush-fill" target="_blank">anti-overflow brush filling, for which work is already in progress</a>. Or updating stuff to target the latest Android version because Google requires it for some reason, even though Drawpile doesn't need any of the new features.

And of course we want to hear feedback from artists using the new version. If it breaks your workflow or there is something you want improved or fixed, <a href="/help/" target="_blank">the help page</a> say so!

## Acknowledgements

Thanks to everyone that contributed code, bug reports, feedback, donations and everything else to make Drawpile. Also thanks to all the people that help other folks in the public channels and keep the servers running smoothly.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
