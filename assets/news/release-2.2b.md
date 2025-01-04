Slug: release-2.2b
Title: Version 2.2 beta
Publish: 2022-08-04 17:30:00+03:00
Visible: True
Author: callaa
---

A long time in the works, the first beta release of Drawpile 2.2 is out!

Despite the seemingly small version number bump, 2.2.0 will be a major release,
including many new features and a complete rewrite of the paint engine.

You can [download](/download/#Beta) the beta release and give the new features a try.
Do note that this is still a Beta version, so you may encounter bugs and broken features!

Two key features introduced in the 2.2 release are *group layers* and *animation timeline*.

---

### Group layers

In 2.2, layers can now be organized into groups and subgroups.

You can create groups by using the new "new group" button or menu action. Layers can be added
to groups by dragging & dropping or by creating new layers when a layer inside a group is selected.

Drawpile now fully supports the OpenRaster file format's layer stack structure, improving interoperability
with other FOSS drawing apps like Krita and Mypaint.

### Animation timeline

Drawpile has had support for making simple frame based animations since before 1.0. In version 2.2,
the animation features are improved further by the addition of a custom timeline editor.

Previously, when exporting a document as an animation, each layer would be treated as a frame.
This method still works and is suitable for very simple animations.
For more complex use cases, e.g. when there are many independently moving actors in the scene,
the timeline editor allows you to select which layers appear in which frame. The number of layers
is now independent from the number of frames in the exported animation.

To create a custom timeline, open the **Timeline** dock (View menu → Docks → Timeline) and check the *Use manual timeline* box.
You can then create frames by clicking on the + symbols. Clicking on a table cell will toggle
the corresponding layer's visibility on that frame. Middle clicking on a frame will quickly select
that frame. Double right clicking will delete one.

### New paint engine

In 2.2, the entire paint engine has been rewritten in the Rust programming language. This change
shouldn't be outwardly visible, except for a couple of nice things:

First, improved stability. The new engine does not suffer from the same kind of memory errors
the old one did. It is also much easier to debug, as some bugs that previously would have crashed
the whole application now merely stop the paint engine and print an error log message.

All paint operations are now performed in a background thread, meaning the UI should always
remain responsive, even when there is a lot going on at the same time. This should be especially
noticable when logging in to a long running session.

The command line utilities `dprectool` and `drawpile-cmd` have been replaced by `drawpile-cli`,
which combines their functionality, and more.

The new paint engine will also allow for some exciting new possibilities, such as a Web based client and
possibly a native mobile application.


### Missing in action: the built-in server

Due to the huge changes to Drawpile's core, the built-in server unfortunately did not make it to this release.
(You can, however, still use the bundled dedicated server.)

It's not gone for good, however! The server will be rewritten during the 2.2 release cycle to support the new paint engine.

Goals for the new server include:

 * Rewrite in Rust for improved security and reliability
 * Websocket connections in addition to plain TCP connections to natively support Web clients (Drawdance)
 * Improved admin API + standard web admin interface
 * Built-in list-server API
 * Built-in thin and thick server modes

