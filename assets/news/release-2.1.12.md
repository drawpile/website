Slug: release-2.1.12
Title: Drawpile 2.1.12 release
Publish: 2019-10-20 18:15:00+03:00
Visible: True
---

Version 2.1.12 is now out. This release contains various improvements to the user interface.

One big new feature in this version is *configurable canvas shortcuts*.
This allows you to change the shortcut keys for canvas related actions (e.g.
scrolling, rotating and color picker mode.) This, unfortunately, meant changing one existing
shortcut: pressing the space bar now acts the same as pressing the middle mouse button. This
might conflict with your existing muscle memory, but the shortcuts are now fully consistent.

When holding down modifier keys, the mouse cursor is now updated to indicate the active mode:
zoom, rotate, color pick or layer pick.

Another big change is improved brush preview and editing. A new visual style is now used
to better indicate the effect of the current blending mode. The "watercolor mode" button
has been removed, instead smudging is now always available for all brush shapes.

There is also a change in the way brush presets are stored internally. Rather than the
settings file or the registry, presets are stored as individual files. This should make
it less likely that the presets disappear seemingly with no reason, and it also makes it
possible to back up and copy them.

One more big UI change is a new drag handle style for selections. Instead of having to
use keyboard shortcuts to rotate a selection, clicking on the selection now switches
the handles between scaling and rotation/skew mode.

**Bugs fixed:**

 * Fixed lockup when opening a layered TIFF file
 * Fixed responsivity of tool quick adjustment by dragging
 * Server: session files are now named consistently
 * Fixed crash when using large-radius color picker near the edge of the canvas

**Other changes:**

 * Added Italian translation (contributed by Albano Battistella)
 * The same default curve is now used for velocity pressure emulation mode
 * drawpile-cmd: added support for outputting to stdout
 * The same default curve is now used for velocity pressure emulation mode
 * Server: file backed session file naming is now consistent when archive mode is enabled
 
