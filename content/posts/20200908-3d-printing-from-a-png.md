---
title: "3D Printing From A PNG"
slug: "3d printing from a png"
date: 2020-09-08T17:00:00-05:00
draft: false
publishdate: 2020-09-08T17:00:00-05:00
tags:
- 3d printing
- how-to
---

This weekend my son asked me to print a character from one of his favorite video games. We looked for existing models. We didn’t find anything. It wouldn’t have mattered because what he wanted was a nominally 2D print that he could paint. DuckDuckGo had hundreds of images. We selected one and tried to import it into OpenSCAD.

The image was a png. PNG images must be imported using the surface() function. We quickly realized this was a bad idea because the image is converted to a height map. I found that import() can accept svg. After a bit more searching we decided to try Inkscape to create the svg file. Inkscape is a powerful tool. There were far too many options but the online community is strong and helped us find a solution.

The solution is straightforward.

- Open the image in Inkscape
- Select the image
- Select Trace Bitmap from the Path menu
- There are several options but the defaults are pretty good. 
- Preview using the Update button
- Save the svg by clicking ok

The old image is still on the palette. Select it and delete. You should be left with a valid svg. This can be saved to disk and imported into OpenSCAD or another program if you prefer. We performed a linear_extrude() on this file. It worked perfectly. I applied a 0.2 mm base layer which we cut away after the print.

We learned a lot from this. The image resolution affects the width of your lines. Since you need a minimum line width for the printer, you should take the final print size into account before selecting an image. Check the pixels/in. Also, if you intend to make several objects that are scaled appropriately then using images with similar resolution and scale is important. Printing flat worked well and our characters are getting better with each print. I think these could also be printed vertically with a small base. It might be a good way to create characters for board games.

![Mr. L](/img/mr-l.jpeg)
