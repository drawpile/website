Slug: release-2.2b4
Title: Version 2.2 beta 4 and Changes at the Helm
Publish: 2023-06-14 07:00:00+02:00
Visible: True
Author: askmeaboutloom
---

After a long time and much testing behind the scenes, Drawpile 2.2 beta 4 is out! You can grab it [over here](/download/#Beta).

Before getting to describing all the new stuff in this release though, I gotta get the organizational thing out of the way: after working as the lead Drawpile developer for 16 years, callaa has handed over the development to me, askmeaboutloom. The size of the "thank you" in order for creating and maintaining this project is immense beyond description. If you want to leave him your own thanks and wishes, there's a thread on the [Drawpile Discord server](https://discord.gg/M3yyMpC) where you could do so!

I could go on about what stuff is planned from here on out, but I already got so many new features to talk about that I'd rather do that instead and leave the rest for later.

## Changes in this Release

This release represents over 8 months of development, so this is everything I can remember anyway. I'll present them all in a big list, with some further details below.

---

* Features:
    * Android support, for tablets anyway. More details [below](#release22b4-android).
    * Overhauled paint engine. Much faster than it was before, making use of multiple cores and with cow-powered vector processing.
    * A nicer default theme. The Windows 95 look has gone in favor of a sleeker look more than inspired by Krita. It's dark mode by default, but there's other styles to choose from. And if you really want it back, the old style is still there too.
    * Improved animation support, now with a timeline with tracks and key frames and all that. More details [below](#release22b4-timeline).
    * Adjustible undo limit. You're no longer stuck with the 30 undos that are there by default. You can change the undo limit of a session in Session &rarr; Undo Limit.
    * Local canvas backgrounds. Under Edit &rarr; Canvas Background, you can now change the background only for yourself. Useful if the session operator has set it to a glaring white and you'd really like it to be a more gentle gray. Or vice-versa, if you need that stinging in your eyes.
    * Better canvas shortcuts. You can zoom by just scrolling the mouse wheel and resize your brush by holding shift and brushing the pen left and right. To configure this stuff, look in Edit &rarr; Preferences, Canvas Shortcuts.
    * A real stabilizer, similar to the one you have in Krita or Paint Tool SAI. The old smoothing is still there, if your tablet is overly jittery, you can turn smoothing up in Edit &rarr; Preferences, Input.
    * MyPaint brushes support indirect mode now.
    * A brush editor, with settings beyond what you can configure in the dock. Edit &rarr; Brush Settings gets you there.
    * Better MyPaint brush import. You can now import brush packs just like you would in MyPaint, rather than having to unpack the brushes inside and import them individually.
    * Under View &rarr; Layouts, you can now save and restore application layouts, as well as pick from some existing presets. For example, if you have your dockers arranged differently for drawing and animating, you can put those here.
    * Tablet-friendly sliders. If you're used to Krita, you'll know these already.
    * The fill tool now supports gap filling, feathering and a more comprehensible size limit setting.
    * Transform smoothing options. Pick between bilinear and nearest-neighbor. The latter makes working with pixel art possible.
    * Compatibility with 2.1 sessions. Details [below](#releaseb224-compat).
    * There's now a menu on the right of each dock, rather than having two not that useful buttons there. Here you can (un)dock it, make it always floating and close it. Locking docks hides the menu button.
    * Docks can now be placed at the top and bottom of the window too and can now be nested.
    * An option for vertical tabs on side-mounted docks.
    * Holding Shift now lets you arrange docks easier by hiding their title bars. If you find that annoying, turn it off in Docks &rarr; Hold Shift to Arrange.
    * There's more brush presets that come with Drawpile now and they're organized a bit better.
    * Chat now has multiline support, hit Shift+Return to make a newline.
    * The preferences dialog has been tidied up and includes a tablet tester field.
    * On Windows, you can now switch between Windows Ink and Wintab mode without having to restart Drawpile.
    * The frequency and amount of snapshots available in Session &rarr; Reset... can now be adjusted in the preferences.
    * Parental control settings can now be hidden when locked.
* Server features:
    * The server now has a forceNsfm option that will automatically make all sessions hosted on it have the NSFM flag enabled.
    * Messages sent from the server GUI will now be alerts.
* Fixes:
    * Indirect drawing mode now works properly, because it really didn't before. If you don't know what this is about: it makes the brush opacity work different ("opacity" instead of "flow") in a way that some people like a lot.
    * Hiding docks (e.g. by hitting Tab) no longer causes them to change their size and position.
    * Transforms now actually preview on the correct layer, rather than just being an image on top of everything.
    * Session resets no longer jerk your view around or throw you to a different layer. You also get prompted if you want to save the canvas from before the reset, in case something got lost.
    * You can set layer opacity and blend mode again without having to go through the layer properties for it.
    * Recordings and recording indexes now deal with undos properly.
    * Recordings can now be played back at a fast pace again.
    * Switching to a layer folder and back now no longer makes the canvas lock clicking noise.
    * You now have to be operator to pin a chat message.
    * Moving your own layer to your own folder now doesn't require you to have omnipotent permissions anymore.
    * Switching away from the annotation tool no longer spontaneously spawns a blank annotation.
    * On Linux and macOS, the canvas now properly gets focus when you interact with it using a tablet, rather than having to reach for the mouse for it to do so.
* Development:
    * Better infrastructure, making a new release of Drawpile is now almost just one push of a button, rather than having to spend an afternoon building it on three different operating systems.
    * Weblate integration, enabling translation of Drawpile in the browser. Details [below](#releaseb224-weblate).
    * Some development tools are now included included with Drawpile: tablet event logging, performance profiling, artificial lag, artificial disconnects as well as the recording and replaying of debug dumps to help with figuring out desyncs.


<h3 id="release22b4-android">Android Support</h3>

There's an Android version of Drawpile now. It's not some kind of simplified mobile version, it's the same application, just running on Android. That means it *probably* only works on devices with a larger screen, on a phone it probably doesn't fit. But you can just give it a try, maybe you can make it work regardless.

Android support is still very fresh, so if you find any issues I'd be glad to hear about them. Look [here](/help/) to find out where you can report stuff.

Now, the bugbear in the room: will also be an iPad version? In short: no, Apple doesn't allow it. For a longer answer, look [here](/help/FAQ#faq-ios).


<h3 id="release22b4-timeline">Animation Timeline Redux</h3>

Previous Drawpile 2.2 betas already had sort of a timeline, but it was kind of limited. This release comes with a "real" one, with key frames and all that. This really needs a proper manual page explaining how it works, but I'll try to give a short description of how it works anyway.

If you don't see the timeline, you can find it under View &rarr; Docks &rarr; Timeline. It'll start out empty and you can add tracks to it. To view the currently selected frame, you can enable a Frame View.

Unlike in many other programs, layers don't have multiple versions for each key frame. If you want a key frame to have different contents, create a new layer. If you want two key frames to have the same contents, assign the same layer to them. If you assign a group to a key frame, you can also filter the visibility of the layers inside it in the key frame's properties.

There's also more fine-grained onion skins control now. Under View &rarr; Docks &rarr; Onion Skins, you can open the dock that lets you adjust the opacity and color of each skin. Onion skins are enabled on a per-track basis, by clicking on the light bulb icon next to their name.


<h3 id="release22b4-compat">Drawpile 2.1 Compatibility</h3>

Drawpile 2.2.0 beta 4 lets you join sessions hosted with Drawpile 2.1.20. Several features will be disabled: you can't use MyPaint brushes, the animation timeline won't be available, there'll be no layer folders and you can't use nearest-neighbor interpolation for selection transforms.

Most other features *do* work though. You get to use the new stabilizer for example. Flood fill feathering works too. And of course you get the new user interface and speedier paint engine.

However, there is likely to be some desynchronization. For example, since indirect mode is broken on Drawpile 2.1, things will look different between versions if those are used. When a session reset happens, the canvas will revert to one of these looks.

This compatibility mode isn't here to stay. It'll probably stick around for the beta phase and then for a bit longer until we see that most public sessions have switched over to Drawpile 2.2.


<h3 id="release22b4-weblate">Weblate</h3>

Drawpile is now [on Weblate](https://hosted.weblate.org/engage/drawpile/).

Instead of having to install the troublesome Qt translation tools, you can now contribute translations right through the browser. It should also allow you to add new languages there, if the one you want to translate to is missing. If you have a lot to translate, try out the Zen mode, it shows everything in a continuous stream. If you prefer the old tools, Weblate lets you upload the translation files.

We'll automatically be notified when there's new translations made, you don't need to open a Github pull request or something.


## Reporting Issues

If you're having trouble with this release, check out [this page](/help/) for how to report issues or get help.


## Acknowledgements

Other than callaa, this thing wouldn't have been possible without many other people. I didn't keep a list and don't know if they want their (user)names mentioned here, so I'll say it like this instead: thank you all for your help, your contributions, translations, issues raised, bugs reported, suggestions provided, discussions had, arguments fought, test sessions held or joined, builds tried out and time endured. This probably wouldn't have been possible and definitely not as good without you all.

And a special thank you to the mods who keep things running.

See you soon hopefully, the next beta release shouldn't be nearly as long in waiting!
