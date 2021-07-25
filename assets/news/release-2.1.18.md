Slug: release-2.1.18
Title: Version 2.1.18
Publish: 2021-07-25 16:30:00+03:00
Visible: True
---

After a long pause, version 2.1.18 is finally out. This release includes the usual bug fixes, as well as a few cool new features, courtesy of Github user askmeaboutlo0m.

Bug fixes include:

 * Fixed inconsistent zooming at certain values
 * Fixed brush size adjustment shortcuts not working consistently
 * Fixed that undo operations would cause the layer list to scroll
 * Fixed moving a layer to the bottom-most position

New features:

 * Added French and Portugese translations
 * Input preferences can now be saved per tool
 * Brush cursor outline width can now be changed
 * Layer properties can now be edited in a dialog
 * Color wheel shape is now selectable
 * Maximum brush size and spacings can now be extended (affects sliders)
 * Added selection perspective transform mode

Breaking changes:

 * The way the active tool settings are saved is not compatible with previous Drawpile versions. Switching back to an older version after using 2.1.18 will result in missing tool settings.
