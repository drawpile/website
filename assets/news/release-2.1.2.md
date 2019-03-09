Slug: release-2.1.2
Title: Drawpile 2.1.2 Stable release
Publish: 2019-03-09 13:40:00+02:00
Visible: True
---

The first stable release of the 2.1 series is now out.

If you haven't yet tried out the beta, check out the [2.1.0](/news/release-2.1.0/) release announcement for
a list of all the new features.

Version 2.0 and 2.1 sessions can coexist on the same server, but a 2.0 client cannot join a 2.1 session or vice versa.
Since it may take some time until everyone has updated to the new version, version 2.0.11 is still available in the release
archive. An updated build of 2.0.11 is available as a ZIP package that does not need installation, so both version can
be run side by side.

Feature changes in 2.1.2:

 * Brush dab max spacing is now 999% and max brush size 255px. These sizes are available via the spinboxes.
 * Implemented fixed layers (a generalization of the old background layer feature)
 * Added Vietnamese translation

Bugs fixed in version 2.1.2:

 * Fixed crash when using flood fill on an canvas without any layers
 * Fixed crash when trying to reset after resetting to the very beginning of the history
 * Clicking on the layer show/hide glyph no longer selects the layer
 * OpenRaster: the xres and yres values are now preserved
 * Fixed canvas not appearing immediately when login dialog was closed
 * Fixed chat username line breaking
 * Fixed Recolor (and other modes) in non-incremental mode

