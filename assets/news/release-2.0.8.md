Slug: release-2.0.8
Title: Drawpile 2.0.8 Release and Roadmap to 2.1.0
Publish: 2018-02-11 15:00:00+02:00
Visible: True
---
Version 2.0.8 is now out. This will likely be the last release of the 2.0.x branch, unless more severe bugs are found. The next big release will be version 2.1.0.

Important fixes in this version:

 * Regression fix: autoreset no longer removes session permission settings
 * Manual resets now also preserve permissions
 * Fixed password remembering on Windows (also fixed in 2.0.7.1)
 * Fixed that a server password would also get saved for ext-auth (also fixed in 2.0.7.1)
 * Platform input method context plugins are now included in the AppImage

Other improvements:

 * Server: added support for SSL certificate chains and certificate auto-reloading
 * Server: web admin can now be used with socket activation
 * Server: support ext-auth "did" field
 * Better icons for authenticated users and mods
 * New session option: allow only authenticated users to join (requires server version 2.0.8)
 * Chatbox no longer shows "user joined" messages for users already in the session
 * macOS: a new window is now opened when the application icon is clicked if none is currently open.

---

### Roadmap to 2.1.0

The next major release will be version 2.1.0. From now on, 2.0 is considered the stable branch and will receive bug fix updates only.

The main focus of the 2.1.x series will be improvements to the paint engine. At least, the following things are planned:

 * General improvements to the paint engine (see [2.0.6 release notes](/news/release-2.0.6) for details)
 * MyPaint brushes (maybe)
 * Soft resets
 * A new user access level ("trusted" users; an intermediate between normal users and session operators)

MyPaint brush engine support is something many people have requested and it's something I'm very interested in doing. Even if that feature doesn't make it into 2.1, I will make some architectural changes in preparation for adding it in a later version (probably 2.2.0)

The soft reset feature is a method of resetting the session history in the background without interrupting currently logged in users. It works in a similar way as session snapshotting did in pre-2.0 versions. A soft reset will require some client cooperation to work reliably (meaning all clients in the session should support soft resets,) which is why I'm doing this in version 2.1, rather than a 2.0.x release.

Digression: In version 1.0, the server would request a session snapshot from a random session operator. That snapshot would replace the session history so that joining users would have less stuff to download. (And also because the server had to store the whole history in memory.) The problem was that it was very easy for the server's idea of the session state to go out of sync with the clients (a problem typically triggered by the snapshotting,) which led to broken sessions with layers no-one could draw on, etc. I wasn't able to reproduce all the bugs, so I decided to switch to a whole new architecture in  version 2.0, which eliminates all these problems, at the cost that a reset also resets all the current users.

