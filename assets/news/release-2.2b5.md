Slug: release-2.2b5
Title: Version 2.2 beta 5
Publish: 2023-06-21 08:30:00+02:00
Visible: True
Author: askmeaboutloom
---

Much faster than last time, Drawpile 2.2 beta 5 is out! Get it here [over here](/download/#Beta).

If you find a bug or run into any issues with this release, check out [the help page](/help/) for how to report issues and where to ask questions. All reports are appreciated, they help make the program better! We can only fix what we know about, after all.


## Changes in this Release

This release represents just about a week of development, but it has some important fixes in there! So it's highly recommended you upgrade to it.

---

* Fixed a really stupid bug that caused sessions to seemingly revert to 2.1 mode.
* Made the new default theme *actually* the default theme, don't sync it with the theme from Drawpile 2.1.
* Fixed saving and loading settings even when Drawpile 2.1 corrupted them.
* Fixed saving of shortcuts and probably also some other settings that didn't let you clear stuff anymore.
* Allowed ordering of list servers in the preferences again.
* Made chat pins work properly again.
* Allowed color picking when using the selection tool again.
* Brought back the old averaging smoothing, as another option in addition to the new time-based stabilizer.
* Miscellaneous fixes and prettifications in the settings dialog.
* Fixed stabilizer settings being forgotten when closing the program.
* Non-floating selections now stick around after hitting Delete, since you might want to delete on multiple layers.
* Fixed some crashes when closing the window when it's in a funky state.
* Made settings only save to disk when you're not doing anything in the program, to avoid causing chugging on slow disks.
* Fixed Copy Merged to actually work and not just copy a blank rectangle.
* Fixed floating docks not being resizable on macOS.
* Fixed pasting images with weird color formats.
* Added an NSFM option to the host dialog, letting you turn that on right from the get-go.
* Called NSFM the same everywhere in the program, instead of mixing up "NSFM", "NSFW" and "age-restricted" in different places.
* Added a context menu to the join dialog, if you want to copy stuff out of there.
* Made popup messages ("Connecting..." and such) work on Wayland.
* Made nearest-neighbor transform actually work, it ended up being forced to bilinear every time.
* Made the stabilizer not run at a really low framerate on Windows.
* Split Shortcuts and Canvas Shortcuts into two settings pages again.
* Fixed shortcuts not getting assigned when closing the preferences without clicking somewhere else first.
* Made conflicting shortcuts actually show errors instead of silently doing nothing.
* Fixed tool slots swizzling their colors when multiple windows were open.
* Allow holding left-click on the timeline frames and scrubbing left and right for a quick preview.
* Pick better layers when switching animation frames and tracks, so that you don't end up stuck on layers that aren't actually in your current frame.
* You can now add keyboard shortcuts for a whole lot more stuff, such as swatch colors, dock visibility and pretty much all actions you can pick from the menu that inexplicably didn't let you assign shortcuts to them before.
* Fixed the authentication dialog messages looking wonky.
* Made the session password dialog look less squashed.
* Made links in server messages clickable.
* Brought back the version check in a way that should work also for  beta versions, on all platforms and in other languages.
* Allowed saving the log file on Android, since you can't view it directly.
* Made alert chat message backgrounds less bright.
* Updated Chinese, German and Portuguese translations.


## Acknowledgements

Thanks for the warm messages of support and for testing out the previous release!

Extra thanks for reporting issues, helping with reproducing bugs and providing translations go to Ben, Bluestrings, blozzom, Charmandrigo, harley, hipofiz, Inky1003, Meru, TsumiBro, vipperz, yeen, xxxx and Zvez.

And as before, a special thank you goes to the mods that keep the official servers running.
