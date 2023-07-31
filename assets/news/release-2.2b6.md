Slug: release-2.2b6
Title: Version 2.2 beta 6
Publish: 2023-07-31 23:59:00+02:00
Visible: True
Author: askmeaboutloom
---

Drawpile 2.2 beta 6 is released! **[Download it here.](/download/#Beta)**

If you run into any issues, have a question or a suggestion of some sort, check out the [the help page](/help/) for links!


## Changes in this Release

This release represents a bit over a month of development. There's been many fixes and some new features, so if you're on a previous beta version, it's strongly recommended to update to this one!

---

All of the changes are here in one big list, you can find more details on the bigger features [below](#release22b6-startdialog).

* Features:
    * Allow adding key frames and an associated layer or group with a single action. More details [below](#release22b6-framelayer).
    * Allow duplicating key frames along with their contents.
    * Add a flipbook button to the timeline dock.
    * Hide the indirect mode button in the brush dock instead of just disabling it, since it's hard to tell the difference otherwise.
    * Allow viewing tile and draw context memory usage in the statistics dialog.
    * Improved canvas view. It now allows scrolling further beyond the edges, has more sensible zoom steps and shows messages about locks and canvas transformations.
    * Clarify when asking for a session password versus an account password.
    * Add shortcuts to move the canvas around, for people who want to do it with something other than the arrow keys.
    * Enable auto-repeat for shortcuts where it's sensible, such as zooming, moving the canvas, undo, redo or switching between layers, frames and tracks.
    * Allow clicking and dragging the inspector around, so that it's easier to hit small sections.
    * Make Linux AppImage more compatible with older Linuxes.
    * Automatically join a session when given a URL on startup, rather than waiting for another button press.
    * Allow including session passwords into URL.
    * Implement an invite dialog, to make it easier to directly let people join a session without listing it publicly. More details [below](#release22b6-invites).
    * Show a warning when joining an NSFM session, since it might not be obvious to new users what they're in for.
    * Implement a start dialog instead of dumping the user into a blank canvas and making them pick through the menu at the top. Replaces the join, host, new and update dialogs, unifying them into a single one instead that should reduce the number of clicks required to do pretty much anything. More details [below](#release22b6-startdialog).
    * Add a button to the color picker to pick from the screen.
    * Allow focusing the canvas by double-tapping the Alt key, as well as an assignable shortcut for it, which is Ctrl+Tab by default.
    * Show coordinates in the view status bar.
    * Make the server browser columns resizable.
    * Allow filtering duplicates in the server browser.
* Fixes:
    * Don't forget account password when entering a wrong session password.
    * Smoothe out the timing of strokes received over the network to not make them appear jerky because of the paint engine drawing them too fast.
    * Lock timeline controls when the canvas or user is locked.
    * Put changing the timeline frame count behind a button, since it might get mixed up with the current frame on accident.
    * Slow down user markers only for MyPaint brushes and snappy for classic brushes as well as when a new line is started.
    * Fixed a crash when resizing the canvas while an indirect stroke is in progress.
    * Put unpinning behind operator permissions too, just like pinning.
    * Make the canvas view not jigger anymore when you zoom it out at certain sizes.
    * Lock drawing when the user is locked.
    * Make KisTablet Windows Ink the default tablet driver on Windows, because the Qt one is pretty busted.
    * Re-synchronize the canvas when local desynchronization is detected, rather than just keeping going with a broken state for ages.
    * Don't reset the layer properties dialog when someone else changes a layer. This would cause renames to get reverted to the original name, for example, which is really annoying.
    * Make default layer actually select itself when joining a canvas.
    * Move notifications to their own preferences page, since the network page was out of room and squashed some controls.
    * Make preference notes larger so that they work better in non-Latin writing systems.
    * Make the password page of the login dialog not so annoyingly large.
    * Handle duplicated shortcuts by complaining about it, rather than doing nothing.
    * Don't fire an assertion when moving a selection out of bounds. This is not an error.
    * Default color wheel to HSV mode, not HSL.
    * Stretch columns of the ban list so they don't look so weirdly cut off.
    * Don't revert settings with a default value that have an old version of some other value.
    * Make layer picking and the inspector pay attention to the layer view mode, so that picking layers when animating works properly.
    * Allow pixel brushes to have a minimum of zero pixels, rather than treating both 0 and 1 as 1.
    * Make chat line not scroll into oblivion when dragging over it.
    * Make the UI not mess up the sizes of docks and chat when starting it on Windows.
    * Make brush outline update even when docks are hidden.
    * Make secure connections work in the Linux AppImage.
    * Make newlines show up properly when the chat is in context mode.
    * Handle key presses and releases while dragging the canvas, since some people start the drag before pressing the key and would like their inputs to not be ignored.
    * Wrap server title in the login dialog to make it not stretch the window into eternity.
    * Allow opening links in the server title. They were turned into links, but those couldn't actually be clicked.
    * Properly disable the NSFM session setting when it can't be changed.
    * Make the color palette work properly again, it was broken in various ways. Also makes the color picker look like it used to in 2.1.
    * Put resize arrows at the corners of the selection, rather than offset on the far ends.
    * Don't displace selection by some subpixel amount when moving it around.
    * Prioritize sending of pings and pongs so that a lot of queued messages don't cause a disconnect.
    * Make filtering closed sessions actually work.
    * Make pinned messages persist again even when chat recording is turned off.
    * Don't grab colors from way too far away when using classic brushes.
    * Avoid colors tending toward black when smudging.
    * Make the cursors for the line, rectangle, ellipse and curve tools look less skrunkly.
    * Prefer Drawpile's own icons over system icons, to avoid nonsensical icons being used on Linux.
* Server Features:
    * Relay listing errors to the client, rather than leaving them in silence.
    * Add maximum user count and closed state to listings.
    * Expedite listing refreshes when something important changes, like the NSFMness, title or closedness of a session.
* Server Fixes:
    * Make the server GUI exist again, it got lost in the build scripts.
    * Make the server GUI compatible with Qt6.
 * Translations:
    * Update Brazilian Portuguese, German, Italian, Russian, simplified Chinese and Spanish translations.
    * Add translation to Portuguese Portuguese.
    * Add translation to Turkish.


<h3 id="release22b6-startdialog">Start Dialog</h3>

Instead of dumping you into a blank canvas when you start the program, you now get a dialog that gives you more sensible points to jump into a drawing session. This should cut down on the number of clicks needed to do pretty much anything, since you no longer have to fiddle through the menus at the top. It's also nicer for new users, since they're no longer stranded in a white void to start with. You can also check for news and updates here right away.

For power users who want to save yet another click, there's a command line option to make Drawpile start on the page you want, allowing you to make shortcuts for different uses. For example, if you run it with `--start-page host`, it will start on the host page, `--start-page none` won't show the dialog at all. To see all options, run Drawpile with `--help`.


<h3 id="release22b6-invites">Invites</h3>

Drawpile now makes it more obvious how to get people to join your drawing session directly. Before, this was hidden pretty well, you had to right-click an unmarked corner at the bottom of the canvas to be given the option to copy the link to your session. Now, you're immediately given an invite link when you host a session. You can also open that dialog again through Session → Invite… or pressing the Invite button at the top of the chat's user list.

The invite link itself has also been upgraded. It's now a clickable link that will bring you to a web page that will try to open Drawpile directly, similar how Discord, Zoom and similar applications do it. The page also lets you copy the link directly, if you prefer that, as well as providing a link to where to download the program. There's also the option of including the session password into the link itself, so that cuts out another step in the process.

Lastly, if you paste the link into Drawpile's "Join" page directly, that'll also just work, you don't need to go through that web page. There's also still the option of copying the `drawpile://` link, if you don't care for all the new-fangled stuff above.


<h3 id="release22b6-framelayer">Animation Frame and Layer Combinations</h3>

You can now add animation frames and layers with a single action, which mirrors the way the timeline works in other programs. You can either get to these actions by right-clicking on a frame and selecting the action or using the shortcuts assigned to them.

The options available are "Create Layer on Key Frame", "Create Group on Key Frame" and "Duplicate Key Frame", with further options where to place the new frame. This will effectively create a layer or group and immediately assign it to the current, next or previous frame, rather than having to do those steps individually.


## Acknowledgements

Extra thanks for reporting issues, helping with reproducing bugs and providing translations go to Blozzom, Bluestrings, bluu, Buch, cada, Desutorakuta, duennisss, guiguizada, gurgerburger, hipofiz, Inky1003, Juan Daza, Meru, Nag'em, Pockatiel, Sheepolution, ssantos, taiyu, th3mk00kz, val, vipperz, xxxx and zetalambo.

And a special thank you goes to the mods that keep the community servers running.
