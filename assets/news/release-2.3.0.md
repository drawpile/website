Slug: release-2.3.0
Title: Version 2.3.0
Publish: 2025-11-20 19:30:00+01:00
Visible: True
Author: askmeaboutloom
---

Drawpile version 2.3.0 is out! It brings many new features and numerous fixes. Thanks to everyone who participated in its design and testing during the beta phases.

If you want to support Drawpile's continued development, consider <strong><a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donating to the project</span></span></a></strong>! Drawpile is developed mostly by just one person, donations help spend more time on it and with the cost of keeping the servers running.

* **[Click here to and install the new version](/download/)**. To update, simply install it over the previous one.

To find out what changed, <strong><a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">take a look at this illustrated guide</a></strong>. It has many pictures and videos to show off the new stuff.

If you have questions, feedback or trouble using the new version, take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact.

## Updating

You can **[download Drawpile from here](/download)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

F-Droid on Android and Flatpak/Software Center on Linux had the new version has been submitted to them. They will make the update available on their own time, usually that takes a few days or so.

Server owners are encouraged to update, since it's required for fast reconnects. If you're using the all-in-one Docker setup, see <a href="https://github.com/drawpile/dpserver?tab=readme-ov-file#updating-the-server" target="_blank">the update instructions here</a>. It's not strictly necessary though, servers are both backward- and forward compatible.

If you have a session that was hosted with the previous version, you have to rehost it to make it update to the new version. You can still join it though, Drawpile 2.3 is backward-compatible (you won't be able to use all the new features though.)

## Changes in this Release

There's many new features in this version, such as:

* <a href="https://docs.drawpile.net/help/common/update2x3x0#fast-reconnects-22-compatible" target="_blank">Fast reconnects</a> that make it so that you no longer have to wait through the catchup sequence again and <a href="https://docs.drawpile.net/help/common/update2x3x0#more-stable-sockets-22-compatible" target="_blank">more stable socket connections</a> by default.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#layer-clipping-23-only" target="_blank">Clipping layers</a>, also known as clipping groups or clip to layer below.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#layer-alpha-lock-22-compatible" target="_blank">Alpha locking of layers</a>, rather than only being able to do it on your tool.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#gradient-tool-22-compatible" target="_blank">A gradient tool</a> tool and <a href="https://docs.drawpile.net/help/common/update2x3x0#lasso-fill-tool-22-compatible" target="_blank">a lasso fill tool</a>.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#greater-density-and-marker-blend-modes-23-only" target="_blank">Marker brush mode</a>, which makes the brush not compound opacity across multiple strokes.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#oklab-blend-mode-23-only" target="_blank">OKLAB</a> and <a href="https://docs.drawpile.net/help/common/update2x3x0#pigment-blend-mode-23-only" target="_blank">Pigment</a> blend modes, for more realistic color blending.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#anti-overflow-23-only" target="_blank">Anti-overflow filling</a>, to avoid your brush spilling out of the lines.
* <a href="https://docs.drawpile.net/help/common/update2x3x0#selections-masking-brush-strokes-23-only" target="_blank">Selections now mask your brush</a>, meaning the brush draws only inside of the selection.
* More pixel and binary art features: <a href="https://docs.drawpile.net/help/common/update2x3x0#pixel-perfect-22-compatible" target="_blank">pixel-perfect mode</a> that prevents doubled-up pixels, <a href="https://docs.drawpile.net/help/common/update2x3x0#pixel-art-input-22-compatible" target="_blank">pixel art input</a> that lets you poke at individual pixels directly and a <a href="https://docs.drawpile.net/help/common/update2x3x0#binary-transform-22-compatible" target="_blank">binary transform mode</a> that does a better job at scaling binary artwork.
* And yet even more, <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">take a look at the full list here</a>.

A full list of changes since <a href="release-2.3.0-beta.4">the last beta release</a> follows below. The final release of Drawpile 2.3.0 represents about a month of development since that beta.

---

Where available, there's links to the <a href="https://docs.drawpile.net/devblog/" target="_blank">development blog</a> or <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">changes guide</a> with more information.

* Features:
    * Add crop to selection action in the selection menu. Not any different to the resize canvas action, but there for discoverability.
    * <a href="https://docs.drawpile.net/devblog/2025/10/26/dev-update.html#lasso-select-stabilizer" target="_blank">Allow using stabilizer and smoothing with lasso select tool.</a>
    * Add touch draw pressure settings, because apparently some screen tablets on Android use touch inputs instead of stylus ones. Thanks SurgeonTaco for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/11/16/dev-update.html#color-pickings" target="_blank">Add extra thickness to the color sampling ring in the area where the colors meet to give better visibility of the comparison.</a> Thanks tiar for suggesting.
    * <a href="https://docs.drawpile.net/devblog/2025/11/16/dev-update.html#color-pickings" target="_blank">Allow toggling color sampling ring in the color picker tool settings.</a>
    * Skip the username selection when reconnecting to a session in the browser using a drawpile.net account. It now automatically picks the same username again as it does on other platforms.
    * <a href="https://docs.drawpile.net/devblog/2025/11/16/dev-update.html#new-layouts" target="_blank">Three new layout presets under View → Layouts.</a> Thanks Ausjamcian, lambda20xx and Scruff for providing them.
    * <a href="https://docs.drawpile.net/devblog/2025/11/16/dev-update.html#new-brushes" target="_blank">Several new brush presets in the Drawpile tag.</a> Thanks Annoy, Blozzom and lambda20xx for providing them.
* Fixes:
    * Don't show "exit layer view" notice when there's no canvas.
    * Properly remove the "unsaved changes" marker when saving to DPCS.
    * Don't remember interpolation mode on transform tool, since it's too easy to mess up art from having a stale mode set.
    * Make mipmap usage in hardware renderer configurable, since it causes performance issues with some graphics cards or drivers. Defaults to off. Thanks Bluestrings and Sinamer for reporting.
    * Make setting the hue slider to 359 in HSL space not turn out gray. Thanks BornIncompetence for reporting.
    * Make sliders not show a text selection cursor on Android when they're not in edit mode.
    * Make layer list items not show a text selection cursor on Android.
    * Correctly calculate the distance to move before a press is no longer considered a long-press. The calculation ended up with incorectly small values in most cases.
    * Improve long-press handling for context menus to act more like a real right-click would.
    * Don't delay long-presses by left-click or touch kinetic scrolling.
    * Make dragging a layer onto its own canvas not paste its contents. Dragging layers between different windows is still possible. Thanks Blozzom and Pepper for reporting.
    * Make the "alpha lock layer for you" a buttton in the layer dock, rather than having it in the lock menu. Otherwise the inherit alpha button is too confusing to people not used to that feature existing. Thanks Phoneme for reporting.
    * Only add actually picked colors to the color picker history, not every color hovered over along the way.
    * Make opening settings dialog not exit fullscreen on Android.
    * On Android devices with a screen large enough to show a full desktop UI, dialogs no longer get full-screened by default. The start and settings dialogs also no longer use their vertical design meant for tiny screens. Thanks tiar for reporting.
    * Replace some symbols in messages that don't show up properly on Android with equivalent ones that do.
    * Default MyPaint brushes to use synchronized smudging, since many of them only work properly with it turned on.
    * Select proper file type and remove the extension on the name input field when saving on Android and the browser.
    * Make color picker color dialog use the current foreground color when manually adding a color. Thanks Phoneme for reporting.
    * Show an error message on Linux under Wayland when attempting to pick a color from the screen with a hint to use Xorg instead. Thanks Meru and Phoneme for reporting.
    * Remove pick from screen button in the browser, since it doesn't work there.
    * Don't enter fullscreen in the browser when reopening the main window. Thanks Bluestrings for reporting.
    * Remember local state when reconnecting, such as layer/track visibility, sketch mode, alpha lock, view mode etc. Thanks Bluestrings and hpar for reporting.
    * Make keyboards like GBoard not eat all your hardware keyboard shortcuts after editing text once. This is a patch to Qt. Thanks justanotatest for reporting.
    * Unfocus chat when collapsing it so that you don't continue typing into it while it's gone.
    * Fall back to the application storage on Android when proper storage is unavailable. This is a patch to Qt. Thanks Sherb for reporting.
    * Use different zoom levels for hardware and software renderers, depending on which ones work better in the respective modes.
    * Default hardware renderer to single-buffering, since the system default buffering can add an immense amount of input lag.
    * Properly disable the save as ORA/DPCS actions while another save is going.
    * Don't process brush dabs that are invisible due to being infinitesimally tiny, fully transparent or infinitely soft (as opposed to only skipping their processing when they fulfilled all three criteria.) Thanks Blozzom for reporting.
* Removed Features:
    * <a href="https://docs.drawpile.net/devblog/2025/11/16/dev-update.html#old-setting-transitions" target="_blank">Migration of settings from very old versions of Drawpile.</a> That code no longer works properly, but it's doubtful anyone would want to port their settings from a 2017 version of Drawpile anyway.
* Server Fixes:
    * Don't claim that dprec templates are incompatible when they're not.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * Arabic translation by Albirinsisat Alsamara.
    * Filipono translation by JP Lagado.
    * German translation by askmeaboutloom.
    * Indonesian translation by evan.
    * Japanese translation by ubanis.
    * Russian translation by Gladius Gingin.
    * Simplified Chinese translation by xxxx.
    * Ukrainian translation by Maksim Gorpinic.

## Acknowledgements

Thanks to all the people that helped design features, found bugs and tested this release to make it as good as it is. Also thanks to everyone that helps out others in the chats, keeps the community servers running and those who donated to the project!

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
