---
title: "Parametric LEGO Compatible Blocks in OpenSCAD"
slug: "Parametric LEGO Compatible Blocks in OpenSCADo"
date: 2020-02-19T22:26:10-05:00
draft: false
publishdate: "2020-02-19"
tags:
- hobbies
- programming
- 3d printing
---

My son and I recently started a project. We are building a remote controlled robot on a [tank chassis][4]. We are using an [Arduino][1] to communicate with a [motor driver][2] and a few sensors. I wanted to 3D print a custom housing for the Arduino that will also serve as the body structure for the robot.

I considered knocking this out in SolidWorks, but I've been interested in [OpenSCAD][3] and this seemed like a good project for open source tools.

I intend to add "nubs" to the structure that will mate with LEGO. This will allow my son to modify the design and add "features". He's six currently.

Before developing the actual components I decided to get my feet wet with OpenSCAD by creating a parameterized brick generator. It turned out well.

Here's the code

    $fa = 1;
    $fs = 0.4;
    
    // CONSTANTS
    L_WID = 8;   // 1 brick unit is 8 mm
    L_TOL = 0.2; // 0.2 mm tolerance for fit
    L_HGT = 3.2; // bricks come in 3.2, 6.4, 9.6 heights
    L_THK = 1.6; // brick thickness
    tol = 0.001; // connection tolerance for printing

    // PARAMETERS SPECIFIED IN INTEGER UNITS (1,2,...)
    LEN = 4;
    WID = 2;
    HGT = 3;        // 1, 2, 3 (3.2, 6.4, 9.6)
    COL = "grey";

    // BRICK
    color(COL) union() {
    // create the basic brick structure
    // remove the interior (wall thickness is 1.6 mm)
        difference() {
            cube([(L_WID*LEN)-L_TOL,(L_WID*WID)-L_TOL,(L_HGT*HGT)]);
            translate([L_THK-L_TOL/2,L_THK-L_TOL/2,0])
    cube([(L_WID*LEN)-L_TOL-3.2,(L_WID*WID)-L_TOL-3.2,(L_HGT*HGT)-1.6]);
        }
    
        // create the connection points 1 cylinder per unit length
        // and 1 cylinder per unit width
        for (dx=[0:1:LEN-1]) {    // loop LEN
            for (dy=[0:1:WID-1])  // loop WID
                translate([3.9+(dx*L_WID),3.9+(dy*L_WID),(L_HGT*HGT)-tol])
                cylinder(h=1.8,r=2.4);
        }
    
        // create the structural cylinder inside the brick
        // if the brick is 1 unit wide or long no cylinder is needed
        if (LEN > 1 && WID > 1) {
            for (dx=[0:1:LEN-2]) {   // loop LEN
                for (dy=[0:1:WID-2]) // loop WID
                    translate([7.9+(dx*L_WID),7.9+(dy*L_WID),0])
                        difference () {
                            cylinder(h=L_HGT*HGT-L_THK+tol,r=3.25);
                            cylinder(h=L_HGT*HGT-L_THK,r=2.4);
                        }
            }
        }
    } 

![Brick](/img/brick.jpg)

Standard rectangular bricks are generated accurately by changing the LEN, WID, HGT parameters. The color can take any [R,G,B] triplet or standard ["web"][5] colors. However, this is only for viewing on the render screen. Actual bricks will print in whatever color filament you load in your printer.

[1]: https://www.arduino.cc
[2]: https://www.adafruit.com/product/1438
[3]: http://www.openscad.org/
[4]: https://www.amazon.com/gp/product/B07C2Q63XG/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1
[5]: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#color
