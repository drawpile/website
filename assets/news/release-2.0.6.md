Slug: release-2.0.6
Title: Drawpile 2.0.6 Release
Publish: 2018-01-21 19:00:00+02:00
Visible: True
Author: callaa
---

Version 2.0.6 is now done! It's been 6 months since the last release, but
to make up for it, this update is packed full of new features and bug fixes.

### Tablet problems after updating Windows 10

Many have a encountered new tablet bug after installing the Windows 10 creators update:
Drawing with a stylus drags the canvas instead of paining.
Whether by design or a bug, Windows now generates touch events for the stylus. Touch
is typically used for scrolling, which is what is happening here.
This change has affected many applications, so it's not just Drawpile.

Currently, there is no true fix to this problem, but *there is a workaround*: uncheck
the "scroll with finger" checkbox in the preferences. If you're not getting any
pressure sensitivity, try also checking the "bug workaround mode" checkbox.

### Canvas clearing session reset bug

I found a number of distinct bugs that could corrupt the canvas in some circumstances
during a session reset. The most easily triggered one is that if a user is drawing
at the exact moment the reset finishes, the canvas can disappear entirely. This happend
on a per-user basis: users who weren't drawing or joined later were unaffected. This bug
is now fixed.

In another case, a client could submit an empty reset. I'm not entirely sure yet what
causes it, but I've added a check that blocks empty reset snapshots.

There may be still some reset related bugs remaining, but it should generally work a
bit more robustly now.

### User accounts

Perhaps the most important new feature in this release is enhanced support
for user account registration. Drawpile has supported user accounts for
a long time, but without a way for users to register accounts by themselves,
it hasn't been of little use.

Version 2.0.6 introduces a new feature that makes it possible for web sites
to provide Drawpile user accounts. You will now be able to register a user
account here at drawpile.net to use on the public server. It is even possible
for other servers to accept drawpile.net accounts or create their own.

At the moment, the only thing you can do with drawpile.net user accounts is
reserve usernames to use on the public server, but new website features 
are coming soon!

Note: if you try logging in using a reserved username with a version older
than 2.0.6, you will get a somewhat cryptic error message saying "Invalid state".

Read on for a full list of other new features added and bugs fixed, and also
some ideas for future development.

---
 
### New features

 * Added support for external authentication
 * Added a selection shear mode (hold Shift+Alt and drag to shear)
 * Added a menu item for terminating a session (moderator feature)
 * Flipbook view can now be cropped
 * Added a quick layer picking mode (hold shift+control to select a layer)
 * Palettes can now be imported and exported directly from the UI
 * Added a feature for sending abuse reports (support must be enabled serverside for this to work)
 * Added a "server title" field to server GUI
 * Added an option to disable tablet eraser detection
 * Added a command line tool for rendering recordings
 * Added an option to hide password protected session in the join dialog

Two new canvas shortcuts were added in this version. Check the [shortcuts help page](/help/shortcuts/)
for a list of all (uncustomizable) keyboard shortcuts.

### Usability improvements

 * Changing the active color now immediately updates the color history
 * Saving OpenRaster files is now much faster (in common cases)
 * Saving is now done in the background. (Autosave no longer interrupts work)

### Bugs fixed in this release

 * Fixed joining a template session by URL
 * Fixed flood fill on erased areas
 * Reset is now aborted if the user loses OP status before it's ready
 * Reset is now cancelled if a snapshot cannot be produced
 * Fixed disappearing canvas if user was drawing during a reset
 * Windows specific: audio.dll is now put into the right folder (fixes missing sounds)
 * Recording is now automatically restarted on session reset
 * Fixed crash when cancelling bezier curve drawing with right click
 * Regression fix: brush outline now snaps to pixel centers again when using a hard edged brush

### Future development roadmap

I will soon start working on version 2.1.0. This will be a client-incompatible
update, meaning that while 2.1 and 2.0 sessions can co-exist on the same server,
a session started with Drawpile 2.0.6 can only be joined by other 2.0.x series
versions and one started with 2.1.0 only supports 2.1.x versions.

I might release one or two 2.0.x series versions before 2.1.0 to fix any serious
bugs that might be found.

The primary focus of version 2.1.0, and the reason for breaking compatibility,
will be paint engine enhancements. A problem that has plagued Drawpile
ever since the first version are the weird color artefacts that appear when
painting with a very low-opacity brush. Some of them may (and certainly
a few other problems do) stem from the early uninformed choice to store pixels
with non-premultiplied alpha values.

So, the first thing to do is to convert everything to use premultiplied alpha.

Next, something I want to try is [MyPaint's 60-bit pixel format](http://mypaint.org/blog/2008/11/21/new-pixel-format/).
If switching to premultiplied alpha won't fix the color fringing problem,
the 7 extra bits of precision per color channel will. (Although it has the downside
of doubling the amount of memory required to store the canvas. I may skip this
one if just changing the pixel composition algorithm yields sufficient improvement.)

Last but not least, I'm going to attempt adding support for MyPaint brushes.
MyPaint's brush engine is available as an independent library and has been
integrated by many other applications, including GIMP and Krita. From what
I've studied of the code so far, it looks like integration should be possible,
even if all features might not be usable.

When/if I get MyPaint brushes working, the question is what to do with
the old brush engine? MyPaint brushes are not so good for pixel art,
but for everything else they do more and work better that the current
system. So, I'm probably going to replace Drawpile's old brushes
with two separate brush engines: a very simple and fast pixel brush
for pen mode and MyPaint brushes for everything else.

Some open questions still remain. Can all the blending modes still be used with
MyPaint brushes? MyPaint iself only supports normal paint, eraser, alpha lock
and colorize modes; a strict subset of what Drawpile supports.

Can all MyPaint brush features can be used? For example, it's not yet clear to me if the
random number brush input can be easily kept in sync across all instances. Also, the behavior
of certain brushes is affected by how fast the cursor is moved and even by the hovering
motion between strokes. Including all this in the protocol may not be straightforward.

