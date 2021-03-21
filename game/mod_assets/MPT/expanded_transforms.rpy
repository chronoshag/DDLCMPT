#This file contains additional transforms to supplement the ones that exist in the base game.
#They're set to load at a later init order than the standard transforms, so these definitions will automatically replace the base game definitions without issue.
#They're not strictly necessary to include in your project, however the logic for the autofocus system already takes them into account, so excluding the contents of this file will generate errors when the autofocus system attempts to run and doesn't find the things defined in here.
#If you don't wish to include these transforms in your project, but still wish to retain use of the autofocus system, you'll need to go into the autofocus logic and remove any and all references therein to any of these extra transforms.

init 10:
    
    transform tcommon(x=640, z=0.80):
        yanchor 1.0 subpixel True
        on show:
            ypos 1.03
            zoom z*0.95 alpha 0.00
            xcenter x yoffset -20
            easein .25 yoffset 0 zoom z*1.00 alpha 1.00
        on replace:
            alpha 1.00
            parallel:
                easein .25 xcenter x zoom z*1.00
            parallel:
                easein .15 yoffset 0 ypos 1.03
    
    transform t41:
        tcommon(200)
    transform t42:
        tcommon(493)
    transform t43:
        tcommon(786)
    transform t44:
        tcommon(1080)
    transform t31:
        tcommon(240)
    transform t32:
        tcommon(640)
    transform t33:
        tcommon(1040)
    transform t21:
        tcommon(400)
    transform t22:
        tcommon(880)
    transform t11:
        tcommon(640)
    
    transform focus(x=640, z=0.80):
        yanchor 1.0 ypos 1.03 subpixel True
        on show:
            zoom z*0.95 alpha 0.00
            xcenter x yoffset -20
            easein .25 yoffset 0 zoom z*1.05 alpha 1.00
            yanchor 1.0 ypos 1.03
        on replace:
            alpha 1.00
            parallel:
                easein .25 xcenter x zoom z*1.05
            parallel:
                easein .15 yoffset 0
    
    transform f41:
        focus(200)
    transform f42:
        focus(493)
    transform f43:
        focus(786)
    transform f44:
        focus(1080)
    transform f31:
        focus(240)
    transform f32:
        focus(640)
    transform f33:
        focus(1040)
    transform f21:
        focus(400)
    transform f22:
        focus(880)
    transform f11:
        focus(640)
    
    transform tinstant(x=640, z=0.80):
        xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03
    
    transform i41:
        tinstant(200)
    transform i42:
        tinstant(493)
    transform i43:
        tinstant(786)
    transform i44:
        tinstant(1080)
    transform i31:
        tinstant(240)
    transform i32:
        tinstant(640)
    transform i33:
        tinstant(1040)
    transform i21:
        tinstant(400)
    transform i22:
        tinstant(880)
    transform i11:
        tinstant(640)
    
    transform tfinstant(x=640, z=0.80):
        xcenter x yoffset 0 zoom z*1.05 alpha 1.00 yanchor 1.0 ypos 1.03
    
    transform if41:
        tfinstant(200)
    transform if42:
        tfinstant(493)
    transform if43:
        tfinstant(786)
    transform if44:
        tfinstant(1080)
    transform if31:
        tfinstant(240)
    transform if32:
        tfinstant(640)
    transform if33:
        tfinstant(1040)
    transform if21:
        tfinstant(400)
    transform if22:
        tfinstant(880)
    transform if11:
        tfinstant(640)
    
    transform sink(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .5 ypos 1.06
    
    transform s41:
        sink(200)
    transform s42:
        sink(493)
    transform s43:
        sink(786)
    transform s44:
        sink(1080)
    transform s31:
        sink(240)
    transform s32:
        sink(640)
    transform s33:
        sink(1040)
    transform s21:
        sink(400)
    transform s22:
        sink(880)
    transform s11:
        sink(640)
    
    transform sinkfocus(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 alpha 1.00 subpixel True
        easein .5 ypos 1.06 zoom z*1.05
    
    transform sf41:
        sinkfocus(200)
    transform sf42:
        sinkfocus(493)
    transform sf43:
        sinkfocus(786)
    transform sf44:
        sinkfocus(1080)
    transform sf31:
        sinkfocus(240)
    transform sf32:
        sinkfocus(640)
    transform sf33:
        sinkfocus(1040)
    transform sf21:
        sinkfocus(400)
    transform sf22:
        sinkfocus(880)
    transform sf11:
        sinkfocus(640)
    
    transform hop(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .1 yoffset -20
        easeout .1 yoffset 0
    
    transform h41:
        hop(200)
    transform h42:
        hop(493)
    transform h43:
        hop(786)
    transform h44:
        hop(1080)
    transform h31:
        hop(240)
    transform h32:
        hop(640)
    transform h33:
        hop(1040)
    transform h21:
        hop(400)
    transform h22:
        hop(880)
    transform h11:
        hop(640)
    
    transform hopfocus(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
        easein .1 yoffset -21
        easeout .1 yoffset 0
    
    transform hf41:
        hopfocus(200)
    transform hf42:
        hopfocus(493)
    transform hf43:
        hopfocus(786)
    transform hf44:
        hopfocus(1080)
    transform hf31:
        hopfocus(240)
    transform hf32:
        hopfocus(640)
    transform hf33:
        hopfocus(1040)
    transform hf21:
        hopfocus(400)
    transform hf22:
        hopfocus(880)
    transform hf11:
        hopfocus(640)
    
    transform dip(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .25 yoffset 25
        easeout .25 yoffset 0
    
    transform d41:
        dip(200)
    transform d42:
        dip(493)
    transform d43:
        dip(786)
    transform d44:
        dip(1080)
    transform d31:
        dip(240)
    transform d32:
        dip(640)
    transform d33:
        dip(1040)
    transform d21:
        dip(400)
    transform d22:
        dip(880)
    transform d11:
        dip(640)
    
    transform dipfocus(x=640, z=0.80):
            xcenter x yoffset 0 yanchor 1.0 ypos 1.03 alpha 1.00 subpixel True
            parallel:
                easein .25 yoffset 25
                easeout .25 yoffset 0
            parallel:
                easein .5 zoom z*1.05
    
    transform df41:
        dipfocus(200)
    transform df42:
        dipfocus(493)
    transform df43:
        dipfocus(786)
    transform df44:
        dipfocus(1080)
    transform df31:
        dipfocus(240)
    transform df32:
        dipfocus(640)
    transform df33:
        dipfocus(1040)
    transform df21:
        dipfocus(400)
    transform df22:
        dipfocus(880)
    transform df11:
        dipfocus(640)
    
    transform leftin(x=640, z=0.80):
        xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .25 xcenter x
    
    transform l41:
        leftin(200)
    transform l42:
        leftin(493)
    transform l43:
        leftin(786)
    transform l44:
        leftin(1080)
    transform l31:
        leftin(240)
    transform l32:
        leftin(640)
    transform l33:
        leftin(1040)
    transform l21:
        leftin(400)
    transform l22:
        leftin(880)
    transform l11:
        leftin(640)
    
    transform leftinfocus(x=640, z=0.80):
        xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
        easein .25 xcenter x
    
    transform lf41:
        leftinfocus(200)
    transform lf42:
        leftinfocus(493)
    transform lf43:
        leftinfocus(786)
    transform lf44:
        leftinfocus(1080)
    transform lf31:
        leftinfocus(240)
    transform lf32:
        leftinfocus(640)
    transform lf33:
        leftinfocus(1040)
    transform lf21:
        leftinfocus(400)
    transform lf22:
        leftinfocus(880)
    transform lf11:
        leftinfocus(640)
    
    transform rightin(x=640, z=0.80):
        xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .25 xcenter x
    
    transform r41:
        rightin(200)
    transform r42:
        rightin(493)
    transform r43:
        rightin(786)
    transform r44:
        rightin(1080)
    transform r31:
        rightin(240)
    transform r32:
        rightin(640)
    transform r33:
        rightin(1040)
    transform r21:
        rightin(400)
    transform r22:
        rightin(880)
    transform r11:
        rightin(640)
    
    transform rightinfocus(x=640, z=0.80):
        xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
        easein .25 xcenter x
    
    transform rf41:
        rightinfocus(200)
    transform rf42:
        rightinfocus(493)
    transform rf43:
        rightinfocus(786)
    transform rf44:
        rightinfocus(1080)
    transform rf31:
        rightinfocus(240)
    transform rf32:
        rightinfocus(640)
    transform rf33:
        rightinfocus(1040)
    transform rf21:
        rightinfocus(400)
    transform rf22:
        rightinfocus(880)
    transform rf11:
        rightinfocus(640)
    
    #In case you're wondering why this transform exists - I tend to use it as an error-check transform when testing; the transform makes it *incredibly* obvious if something's gone wrong.
    transform kaiju(z=0.90):
        subpixel True
        xcenter 640
        ease 0.95 zoom z*3.25
    
    transform thide(z=0.80):
        subpixel True
        transform_anchor True
        on hide:
            easein .25 zoom z*0.95 alpha 0.00 yoffset -20
    
    transform lhide:
        subpixel True
        on hide:
            easeout .25 xcenter -300
    
    transform rhide:
        subpixel True
        on hide:
            easeout .25 xcenter 2000
    
    #Variable length l/r hides; they allow you to specify how quickly/slowly you want the character to leave the screen when you're using it.
    transform lhidev(t=0.25):
        subpixel True
        on hide:
            ease t xcenter -300
    
    transform rhidev(t=0.25):
        subpixel True
        on hide:
            ease t xcenter 2000



