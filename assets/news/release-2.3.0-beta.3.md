Slug: release-2.3.0-beta.3
Title: Version 2.3.0-beta.3
Publish: 2025-08-14 20:00:00+02:00
Visible: True
Author: askmeaboutloom
---

Another beta version for Drawpile 2.3.0 is out now. This is mostly just a bugfix release for Windows.

* **[Click here to download and install it](/download/#Beta)**.
* To find out what changed, <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">take a look at this illustrated guide</a>. It has many pictures and videos to show off the new stuff.
* If you want to keep 2.2 installed, <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">take a look at this page on how to install both versions side by side</a>.
* Consider <a href="https://donate.drawpile.org/" target="_blank"><span class="icon-text"><span class="icon"><span class="fas fa-heart"></span></span><span>donating to the project</span></span></a>! Drawpile is developed by one person, donations help spend more time on it and with the cost of keeping the servers running.

If you have questions, feedback or trouble using the new version – especially if it breaks your workflow – take a look at <a href="/help/" target="_blank">the help page</a> on how to get in contact! Almost every feature is added because it was requested by an artist and bugs can only be fixed if they are reported, you can see everyone that contributed in the list of changes below.

## Updating or Installing Side by Side

You can **[download Drawpile from here](/download/#Beta)** and simply install it over the current version. This will update it. The new version is backward-compatible, so you can still join sessions hosted with the previous version.

Alternatively, you can run both versions side-by-side. <a href="https://docs.drawpile.net/help/tech/sidebyside" target="_blank">See here for how to do that on different operating systems</a>.

On the server side, everything is both back- and forward-compatible. Server owners can update if they want, but it's not necessary, people can use any version they wish to host sessions.

## Changes in this Release

Drawpile 2.3.0-beta.3 is only a little over a week of work since the last beta. For an illustrated list of the major changes since 2.2.2, take a look at <a href="https://docs.drawpile.net/help/common/update2x3x0" target="_blank">this page</a>.

It's mostly a bugfix release for a problem on some Windows systems, where the audio system could corrupt itself after playing a sound effect and cause all kinds of weird effects, like not being able to move layers or keyframes, the application hanging when trying to save a file or other inexplicable effects. This is fixed by just using a different audio system (Windows has a lot of them). I'll probably write more about it <a href="https://docs.drawpile.net/devblog/" target="_blank">on the development blog</a> this weekend, since figuring that one out was quite a journey.

But there's also a new feature: <a href="#pixel-art-input-22-compatible" target="_blank">pixel art input</a>, which lets you turn off all the smoothing and stabilization meant for tablets and poke at pixels directly.

---

* Features:
    * Pixel art input for pixel brushes, turns off all smoothing and makes the inputs apply immediately. Thanks Ben, dAVePAGE and Nilifin for reporting.
* Fixes:
    * Allow putting labels on a blank brush thumbnail. Thanks hipofiz for reporting.
    * Remove alpha lock and erase toggle buttons when using the eraser tool.
    * Disable the "modern" WASAPI audio backend, because on some devices it causes crashes in the depths of Windows, makes drag and drop stop working or other strange effects. Thanks Ben, CrustStuff, dAVePAGE and Momo for reporting various different incarnations of this problem.
* Translations (only translations that are completed to a large enough degree are included in the program):
    * German translation by askmeaboutloom.
    * Gothic translation by Roel v.
    * Russian translation by Vint Prox.
    * Ukranian translation by Maksim Gorpinic.

## Acknowledgements

Thanks to the people who helped figure out this mysterious bug and everyone that gave feedback on the release, as well as those who have donated so far! And also thanks to those that keep the community servers running and helping others in the public channels.

We also thank <a href="https://about.signpath.io/" target="_blank">SignPath.io</a> for providing us with code signing for Windows with a certificate by <a href="https://signpath.org/" target="_blank">SignPath Foundation</a>.
