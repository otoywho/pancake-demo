transform anim_hover:
    on hover:
        linear 0.35 xoffset 20
    on idle: 
        linear 0.25 xoffset 0

transform customleft(xorigin=0.5, yoff=0.0):
    on show:
        xalign 0.5
        yalign (1.0+yoff)
        xpos -0.5
        linear 0.5 xpos xorigin
    on hide:
        linear 0.5 xpos -0.5

transform customright(xorigin=0.5, yoff=0.0):
    on show:
        xalign 0.5
        yalign (1.0+yoff)
        xpos 1.5
        linear 0.5 xpos xorigin
    on hide:
        linear 0.5 xpos 1.5

transform customcenter(yoff=0.0):
    on show:
        xalign 0.5
        yalign (1.0+yoff)
        xpos -0.5
        linear 0.5 xpos 0.5
    on hide:
        linear 0.5 xpos 1.5