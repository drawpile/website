Slug: release-2.1.14
Title: Drawpile 2.1.14 release
Publish: 2019-11-17 12:00:00+02:00
Visible: True
---

Version 2.1.14 is now out. This is another bugfix release that fixes some of the regressions that weren't fixed already in the previous version.

The primary big change in this version is that brush preset sorting by drag & drop works again. There is also a new related feature: presets can now be sorted into folders!

Note for people running servers: the admin API root path has changed! The paths are now prefixed with "/api", so "/status/" becomes "/api/status/". This change is to better support the new work-in-progress web admin frontend.

**Bugs fixed:**

 * Fixed dab spacing in default brush presets
 * Fixed that selecting a brush preset could change the eraser slot into a non-erasing mode
 * Fixed brush preset reordering by drag&drop
 * Fixed that pressing spacebar while drawing would cause strange input handling behavior
 * Bugfix: don't allow pasting by drag&drop if cut&paste is disabled

