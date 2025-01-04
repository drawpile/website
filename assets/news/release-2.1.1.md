Slug: release-2.1.1
Title: Drawpile 2.1.1 Beta
Publish: 2019-02-17 19:45:00+02:00
Visible: True
Author: callaa
---

The second beta of the 2.1 series is here. This release fixes a large number of bugs that were discovered in 2.1.0 beta (as expected.)
For a list of new features in 2.1, see the [2.1.0 release announcement](/news/release-2.1.0/).

Features added in this version:

 * Added support for ext-auth avatars
 * Added server configuration options for disabling avatars
 * Added copy merged action (like copy visible, except background is excluded)

Bugs fixed:

 * Pressing the OK button in the login dialog could crash the application
 * Fixed mouse cursor ghosts when switching tools
 * Autoreset threshold can now be set even when session size is unlimited
 * Autoreset would sometimes fail to work
 * Fixed missing layer attributes after a reset
 * Censor layer flag is now saved in ORA files
 * Fixed ORA file loading regression
 * Background window is no longer raised when notification balloon is shown (Windows specific bug)
 * Fixed onionskin mode settings initialization
 * Fixed zooming when outside the usual zoom range (2.1.0 regression)

