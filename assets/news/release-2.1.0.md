Slug: release-2.1.0
Title: Drawpile 2.1.0
Publish: 2019-02-13 19:30:00+02:00
Visible: True
---

After a long wait, Drawpile 2.1.0 beta is finally here.

This is the first release of the 2.1.x series, which is not compatible with the 2.0.x series. (The 2.1 server supports both 2.0 and 2.1 clients, however. See the [version compatibilty chart](/help/compatibility/) for details.)

As the first release of a new incompatible series, this is a *beta* release. Once all the potential showstopping bugs are found and fixed, 2.1 will become the new stable series.

Read on for a list of new features and changes.

---

### Big new features

**Tiered access controls**: There are now four user tiers: guests, registered users, trusted users and operators. Operators can mark any user as trusted. Access to various features can be granted based on the tier. Trusted users can be given a permission to kick/ban non-trusted users. [Read more here](https://drawpile-dev-diary.tumblr.com/post/172864608647/feature-access-tiers).

**Canvas background**: Drawpile no longer creates a background layer by default. Instead, you can set a background color. If you wish to use a background layer anyway, you can set the background color to transparent and create a layer yourself and it will work exactly the same as before. [Read more here](https://drawpile-dev-diary.tumblr.com/post/172592327187/canvas-background).

**User avatars**: You can now select an avatar image when logging in. The avatar is shown in the chat box, the user list and user cursors.

**Improved chat**: The chat box and user list have been updated for a more modern look. [Read more here](https://drawpile-dev-diary.tumblr.com/post/181522891537/chat-panel-facelift)

**Private messaging**: You can now open private chats with individual users.

**Smarter autoresetting**: The autoreset threshold is now adjustable from the session settings dialog and can even be disabled entirely. (The server can still set a hard maximum size limit.) Additionally, the server now tries to select the user with the fastest connection to perform the reset. Note that server version 2.1 is needed for autoresetting to work at all. [Read more here](https://drawpile-dev-diary.tumblr.com/post/175050666722/session-autoreset).

**Censored layers**: Individual layers can now be tagged for censoring. When censoring is enabled, tagged layers will be filled with a censor bar pattern. (Censoring can be locked via the parental controls settings.) [Read more here](https://drawpile-dev-diary.tumblr.com/post/175308366692/censored-layers).

**Redesigned join dialog**: The "join session" dialog now includes the session listing directly.

**Zoom tool**: You can now use a new tool to zoom in and out. [Read more here](https://drawpile-dev-diary.tumblr.com/post/181974144637/zoom-tool).

**Square pixel brush**: There is now a square shape option for the pixel brush.

**WebM video export**: Recordings and animations can now be exported directly to WebM video format. (Replaces the semi-broken ffmpeg exporter.)


### Smaller features and changes

**Simplified host dialog**: The "host session" dialog has been simplified. The "settings" tab has been removed, since it was an obsolete holdover from version 1.0.

**Layers menu**: The layer menu button is replaced by a new menu in the main menubar. Keyboard shortcuts can now be used to create layers and toggle solo view mode (among other things.) Common operations (add/delete layers) can still be accessed in the layer box by right clicking.

**Navigator controls**: Zoom and rotation can now be adjusted via the navigator dock. [Read more here](https://drawpile-dev-diary.tumblr.com/post/181845570377/navigator-dock-improvements).

**Status bar controls**: The zoom and rotation sliders in the status bar have been replaced with comboboxes. The mirror and flip actions were moved to the tool bar.

**Keyboard shortcuts** are now shown in toolbar tooltips.

**Template export**: You can now export the current canvas as a template for use with the dedicated server.

**Bonjour on Windows**: If Bonjour is installed, Drawpile can use it to announce and find servers on the local network. [Read more here](https://drawpile-dev-diary.tumblr.com/post/182783596187/servers-nearby).


### Big internal changes

**Premultiplied colors**: Pixels are now stored in premultiplied ARGB format. This fixes some strange color artifacts that happen when using very light colors and also makes basic alpha blending operations slightly faster. [Read more here](https://drawpile-dev-diary.tumblr.com/post/172280623402/premultiplied-alpha).

**Optimized layer initialization**: Initial layer content is now drawn in a more efficient way. This makes session resets (and initialization from an existing image) slightly faster. [Read more here](https://drawpile-dev-diary.tumblr.com/post/172317676012/optimizing-layer-initialization).

**Clientside brush engines**: Instead of sending PenMove events, Drawpile now sends precomputed dab vectors. This is a potentially controversial change, since it does make session histories bigger, however I believe the tradeoff is worth it. This change simplifies the application's internal architecture, improves forward compatibility, eliminates certain bugs entirely, makes the watercolor brush faster and makes it possible to implement soft resetting and integrate the MyPaint brush engine. (In short, how it should have been done since the beginning.) Read more [here](https://drawpile-dev-diary.tumblr.com/post/171836308437/rethinking-penmoves) and [here](https://drawpile-dev-diary.tumblr.com/post/172558360502/penmoves-vs-drawdabs-redux).




