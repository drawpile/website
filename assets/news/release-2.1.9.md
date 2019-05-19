Slug: release-2.1.9
Title: Drawpile 2.1.9 release
Publish: 2019-05-19 11:00:00+03:00
Visible: True
---

Version 2.1.9 is now out. In addition to bug fixes, this release contains a major change to the built-in server.

Now, when hosting a session using the "This computer" option, a new [thick server](https://drawpile-dev-diary.tumblr.com/post/184820233197/thin-thick-servers-and-session-resets) is used. In practice this means the server no longer needs autoresets and each user joining gets a fresh snapshot of the canvas, ensuring fast login time.

This is a new, still somewhat experimental, feature. If you encounter any bugs, please report them at the bug tracker or the Discord server. If you need or prefer the "thin server" style where the whole session history is sent to new users, you can use the dedicated server instead of the built-in one.

Presently, the standalone/dedicated version of the thick server is still a work in progress and only included in the source code release.

**Note**: if you're running a headless dedicated server, check your command line arguments when updating to 2.1.9. The `--secure` argument has been removed. If TLS is enabled, secure mode is now always used. (The client has never offered an option not to use TLS if it is available. This option was for the benefit of Windows clients in early versions when TLS support was not reliably present in the Windows build.)

Bugs fixed in 2.1.9:

 * Fixed that disabled brush slots were still selectable with a keyboard shortcut
 * Fixed potential crash when logging in to a session
 * Ctrl+C shortcut now works in the chat box
 * Server: fixed crash when using file sessions (regression)
 * Fixed duplicate entries in the "Nearby" server list
 * Very long pinned chat messages no longer force the window to become wider

Other changes:

 * Incompatible sessions are no longer hidden in from the Join dialog
 * Added support for read-only list servers
 * The built-in server is now based on the new Thick Server
 * Server: added support for real password hashing algorithms
 * Server: removed argument `--secure` (secure mode is now always used if TLS is enabled)

