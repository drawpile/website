Slug: release-2.1.11
Title: Drawpile 2.1.11 release
Publish: 2019-06-23 11:40:00+03:00
Visible: True
---

Version 2.1.11 is now out. In addition to bug fixes, this release adds one long awaited feature: the ability to detach the chat box into a separate window.

Another important change is to the server. IP bans now only apply to guest users. When a user with a registered account is banned, the ban is applied to the account only. This is to combat false positives caused by many unrelated people sharing the same IP address because of NAT.

Bugs fixed:

 * Fixed that brush color was uninitialized on fresh install
 * Fixed that using "/me" in a direct message would send it as a public message
 * Fixed incorrect layer when moving selection if active layer was changed before the move ended
 * Fixed single pixel shift when moving or copy&pasting freeform selections
 * Fixed that read-only listservers were included in the session settings "add listing" buttons
 * Client now refuses to autoreset if it knows it isn't fully caught up yet

Other changes:

 * Join dialog's session list sort order and column is now remembered
 * Server: registered user bans are no longer IP bans
 * Server: op and trusted status is now remembered by user account, rather than username
 * An error message is now shown if a login message is oversize
 * Chat box can now be detached into its own window

