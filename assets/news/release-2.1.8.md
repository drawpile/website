Slug: release-2.1.8
Title: Drawpile 2.1.8 release
Publish: 2019-05-04 09:30:00+03:00
Visible: True
Author: callaa
---

Version 2.1.8 is now out. This release contains a few bug fixes and feature improvements.

In the macOS build, the bundled Qt library version has been updated to the latest version. This
enables Dark Mode support on macOS Mojave, and may improve high-DPI screen support as well.

Bugs fixed:

 * Server: fixed crash when closing a session
 * Fixed formatting in update check dialog when more than one new version is shown
 * Drag&dropping a link to an image onto the canvas now works again
 * Fixed crash when opening an OpenRaster file with missing stack.xml

Feature enhancements:

 * Server: listings are now refreshed in batches instead of individually
 * Background color alpha can now be set in the "new image" dialog
 * Adaptive canvas zoom slider: the minimum value is now always the zoom level needed to fit the whole canvas on screen. [Read more](https://drawpile-dev-diary.tumblr.com/post/184531795642/minimum-zoom)
 * Drawpile can now download the latest version via the "check for updates" dialog
 * New more efficient recording index format. Indexes are now generated faster and the files are smaller. [Read more](https://drawpile-dev-diary.tumblr.com/post/184574203272/recording-indexes)
 * Enabled dark appearance support on macOS
 * Memory usage optimization: only the minimum amount of session history is now kept in memory
 * Manual session reset snapshots are now retained separately for one minute
 * NSFW sessions are no longer hidden by default

