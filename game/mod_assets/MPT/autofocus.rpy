#Special thanks, to folks without which this simplified update would not have been possible:
#RyzekNoavek#0624 for finding the config.sticky_positions variable buried deep in the Renpy 5.6.1 reference manual
#rheat2002#2089 (Fred) for the renpy.display.core.displayable_by_tag logic

default af_enabled = True
define char_list = ["monika","natsuki","yuri","sayori"] #Add any custom characters with sprites to this list.
define config.sticky_positions = True
###
#A note on what exactly sticky positions does:
#
#Sticky positions means that internally, transforms aren't lost when re-showing a character.
#For example, consider the following code:
#
#show yuri 1a at t11
#y "Hello!"
#show yuri 2b
#
#Without sticky positions, if we ask renpy for yuri's transform at the end of the code, it will give us an empty list, as this is the last thing we did.
#Even though visually, Yuri hasn't moved positions.
#
#Sticky positions causes renpy to remember the t11 transform so it will be able to retrieve it later.
#This has a particular visible side effect. Let's make one change:
#
#show yuri 1a at l11
#y "Hello!"
#show yuri 2b
#
#Since the position is sticky, the second show will cause Yuri to animate again.
#It is recommended in these scenarios to utilize the i## transforms to prevent this; like so:
#
#show yuri 1a at l11
#y "Hello!"
#show yuri 2b at i11

#This only matters when showing characters at transforms like this (l## and h##) and only when re-showing them without another transform.
###
#First list is just all the manual mouth tags the user could replace the om/cm tags with.  They intentionally disable the open/close mouth logic.
#We then encode it because we have to.
#If you're using a custom mouth attribute tag, you will need to add it to this list for it to correctly override the logic like these mouths do.
define autofm_manual_mouth_tags = ["ma","mb","mc","md","me","mf","mg","mh","mi","mj","mk","ml","mm","mn","mo","mp","mq","mr"]
define autofm_manual_mouth_tags_encoded = [tag.encode("utf-8") for tag in autofm_manual_mouth_tags]

#Next lists are for logical attribute tags.  These tags are defined on all default MPT characters, and are all "null" attributes - i.e., no graphic is displayed with them, since their only purpose is for logic (like how all the "mood" tags work).
#"afm" is the tag that controls the automatic mouth opening/closing.
#"afz" is the tag that controls the automatic zorder changing.
#These tags are then encoded because...they have to be or they won't work cleanly later.
define autofm_manual_mouth_tags_logic = ["afm"]
define autofz_zorder_logic = ["afz"]
define autofm_manual_mouth_tags_logic_encoded = [tag.encode("utf-8") for tag in autofm_manual_mouth_tags_logic]
define autofz_zorder_logic_encoded = [tag.encode("utf-8") for tag in autofz_zorder_logic]

#Global variable that controls whether the automatic mouth open/close system is enabled in general.  Set to False to turn off behavior in all instances.
default mpt_af_mouth_auto = True

#Global variable that controls whether the automatic zorder system is enabled in general.  Set to False to turn off behavior in all instances.
default mpt_af_zorder_auto = True


init python:
    
    #This function checks if the character currently has a specific mouth attribute; if so, it returns True, which tells the logic not to run.
    #If you wish for any new/custom mouth 
    def mpt_af_manual_tag_mouth_check(character):
        
        global autofm_manual_mouth_tags_encoded
        
        if any(tag in autofm_manual_mouth_tags_encoded for tag in renpy.get_attributes(character)):
            return True
        else:
            return False
    
    #This function checks if the character has the "afm" tag present; if they do, it returns True.
    #If the logic returns False, the automatic mouth open/close action will not occur.
    def mpt_af_manual_tag_mouth_logic_check(character):
        
        global autofm_manual_mouth_tags_logic_encoded
        
        if any(tag in autofm_manual_mouth_tags_logic_encoded for tag in renpy.get_attributes(character)):
            return True
        else:
            return False
    
    #This function checks if the character has the "afz" tag present; if they do, it returns True.
    #If the logic returns False, the automatic zorder change action will not occur.
    def mpt_af_manual_tag_zorder_logic_check(character):
        
        global autofz_zorder_logic_encoded
        
        if any(tag in autofz_zorder_logic_encoded for tag in renpy.get_attributes(character)):
            return True
        else:
            return False

init 1 python:
    def get_onscreen_chars():
        '''
        Subroutine to count the number of characters currently being displayed on-screen.
        '''
        global char_list
        number_of_chars = 0
        for c in char_list: #Loop to determine amount of on-screen characters.
            if renpy.showing(c):
                number_of_chars +=1
        return(number_of_chars)

    def af_mouth_zorder(char,a):
        '''
        Subroutine if user wants to use the auto-mouth feature. Focuses the speaker.
        '''
        global char_list
        if not mpt_af_manual_tag_mouth_check(char) and mpt_af_manual_tag_mouth_logic_check(char): #Check if either the character has a unique mouth assigned to them or if the "afm" tag is not present.  The former must return False and the latter must return True, otherwise no mouth control will occur.
            if mpt_af_manual_tag_zorder_logic_check(char) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                renpy.show(char + " om",at_list=[focus(a.xpos)], zorder = 10) #character is in focus, automatic mouth control says to open the mouth, and automatic zorder places them at a high zorder.
            else: #Automatic zorder check has failed.
                renpy.show(char + " om",at_list=[focus(a.xpos)]) #character is in focus and automatic mouth control says to open the mouth, but automatic zorder is NOT engaged.
        else: #Character either has a unique mouth assigned to them or does not have the "afm" tag present; mouth control will not occur.
            if mpt_af_manual_tag_zorder_logic_check(char) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                renpy.show(char,at_list=[focus(a.xpos)], zorder = 10) #character is in focus and automatic zorder places them at a high zorder, but automatic mouth control is NOT engaged; no change to mouth.
            else: #Zorder control is disabled.
                renpy.show(char,at_list=[focus(a.xpos)]) #Character is in-focus, but automatic zorder is NOT engaged and automatic mouth control is also NOT engaged.
        for c in char_list: #This loop is for any and all characters shown on-screen that are NOT the speaker.
            if renpy.showing(c) and c != char: #Determines if the character is the both on-screen and NOT the speaker.
                if not mpt_af_manual_tag_mouth_check(c) and mpt_af_manual_tag_mouth_logic_check(c): #Check if either the character has a unique mouth assigned to them or if the "afm" tag is not present.  The former must return False and the latter must return True, otherwise no mouth control will occur.
                    if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                        renpy.show(c + " cm",at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)], zorder = 0) #character is unfocused, automatic mouth control says to close the mouth, and automatic zorder places them at a low zorder.
                    else: #Zorder check has not passed, no change to zorder.
                        renpy.show(c + " cm",at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)]) #character is unfocused, automatic mouth control says to close the mouth, but automatic zorder does NOT engage; no change to zorder.
                else: #Character either has a unique mouth assigned to them or does not have the "afm" tag present; mouth control will not occur.
                    if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                        renpy.show(c,at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)], zorder = 0) #character is unfocused and automatic zorder places them at a low zorder, but automatic mouth control is NOT engaged; no change to mouth.
                    else: #Zorder control is disabled.
                        renpy.show(c,at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)]) #Character is unfocused, but automatic zorder is NOT engaged and automatic mouth control is also NOT engaged.
                        
    def af_just_zorder(char,a):
        '''
        Your mouth is now moving manually.
        '''
        global char_list
        if mpt_af_manual_tag_zorder_logic_check(char) and mpt_af_zorder_auto: #If both the global zorder variable is true and the speaking character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
            renpy.show(char,at_list=[focus(a.xpos)], zorder = 10) #character is in focus and automatic zorder places them at a high zorder, but automatic mouth control is NOT engaged; no change to mouth.
        else: #Zorder control is disabled.
            renpy.show(char,at_list=[focus(a.xpos)]) #Character is in-focus, but automatic zorder is NOT engaged and automatic mouth control is also NOT engaged.
        for c in char_list: #This loop is for any and all characters shown on-screen that are NOT the speaker.
            if renpy.showing(c) and c != char: #Determines if the character is the both on-screen and NOT the speaker.
                if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                    renpy.show(c,at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)], zorder = 0) #character is unfocused and automatic zorder places them at a low zorder, but automatic mouth control is NOT engaged; no change to mouth.
                else:
                    renpy.show(c,at_list=[tcommon(renpy.display.core.displayable_by_tag("master",c).xpos)]) #Character is unfocused, but automatic zorder is NOT engaged and automatic mouth control is also NOT engaged.
    def af_solo_mouth(char):
        '''
        Subroutine for solo auto-mouth. Adjusts open/closed mouth but doesn't focus.
        '''
        if not mpt_af_manual_tag_mouth_check(char) and mpt_af_manual_tag_mouth_logic_check(char): #Check if either the character has a unique mouth assigned to them or if the "afm" tag is not present.  The former must return False and the latter must return True, otherwise no mouth control will occur.
            if mpt_af_manual_tag_zorder_logic_check(char) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                renpy.show(char + " om", zorder = 10) #Automatic mouth control says to open the mouth and automatic zorder places them at a high zorder, but no change in focus.
            else: #Automatic zorder check has failed.
                renpy.show(char + " om") #Automatic mouth control says to open the mouth, but automatic zorder is NOT engaged nor does the focus change.
        else: #Character either has a unique mouth assigned to them or does not have the "afm" tag present; mouth control will not occur.
            if mpt_af_manual_tag_zorder_logic_check(char) and mpt_af_zorder_auto: #If both the global zorder variable is true and the character has the "afz" attribute, automatic zorder will engage, otherwise system will not.
                renpy.show(char, zorder = 10) #Automatic zorder places them at a high zorder, but automatic mouth control is NOT engaged; no change to mouth nor does the focus change.
            else: #Zorder control is disabled.
                return #All checks have come back false, and so nothing is being changed in regards to the character.  Don't bother showing them, just eject out of the callback.

init 2 python:
    def autofocus(char, event, interact=True,*args,**kwargs):
        '''
        The main attraction.
        
        The logic here is fairly simple. First, we add up all the characters on screen, and only continue if there's more than one.
        We get the xpos of the speaking character and show the speaking character focused at that position.
        Then, we check who else is being shown, and move them back.
        
        Custom characters with sprites should be added to the char_list variable in order for them to be included.
        '''
        global char_list
        #This list holds transforms that are likely to cause the autofocus problems (usually because they have an animation)
        #Add to this list as necessary.
        exception_transforms = [r11, r21, r22, r31, r32, r33, r41, r42, r43, r44, rf11, rf21, rf22, rf31, rf32, rf33, rf41, rf42, rf43, rf44, l11, l21, l22, l31, l32, l33, l41, l42, l43, l44, lf11, lf21, lf22, lf31, lf32, lf33, lf41, lf42, lf43, lf44, lhide, rhide]
        global mpt_af_mouth_auto
        global mpt_af_zorder_auto
        global af_enabled
        if not interact or not renpy.showing(char) or renpy.get_at_list(char)[0] in exception_transforms or not af_enabled: #Bail if the speaking character doesn't logically make sense to apply logic to.
            return
        a = renpy.display.core.displayable_by_tag("master", char)
        if event == "begin":
            if get_onscreen_chars() > 1 and renpy.showing(char): #If there are enough on-screen characters, focus system engages.  Entire below branch of this "if" check is specifically for the character that is currently speaking
                if mpt_af_mouth_auto: af_mouth_zorder(char,a)#Check global mouth control variable.  System cannot engage if this does not return True.
                else: af_just_zorder(char,a) #Global mouth control variable has returned False; no change to mouth.
            elif renpy.showing(char) and mpt_af_mouth_auto: #There is only one character on-screen, and they're the one that is talking.  By default, focus will not engage on this single character.  We still need to check for the rest of the controlling variables though, since without doing this basically any and all other systems immediately stop working for just one character.
                af_solo_mouth(char)#Check global mouth control variable.  System cannot engage if this does not return True.
            else: return
                #The speaking character isn't on screen at all. 
    def autofocus_narrator(event, interact=True, **kwargs):
        '''
        Autofocus for characters that don't have a sprite. By default, these are the narrator and the MC.
        
        What this is doing is checking each of the characters on screen and seeing if they're in a "focused" state.
        If they are, it unfocuses them.
        Unfortunately, you can't directly compare two transforms since each transform object is unique every time it's used.
        The hacky workaround here is to take a string version of the object and compare the line number of the on-screen transform to the line number of the "focus" transform.
        If those are the same, the character is "focused" and needs to be unfocused.
        '''
        global char_list
        global mpt_af_mouth_auto
        global mpt_af_zorder_auto
        if not interact or not af_enabled:
            return
        if event == "begin":
            for c in char_list:
                if renpy.showing(c):
                    a = renpy.display.core.displayable_by_tag("master", c)
                    als = str(renpy.get_at_list(c)[0])
                    fcs = str(focus(a.xpos))
                    b = als[als.find(",")+len(","):als.rfind(")")]
                    d = fcs[fcs.find(",")+len(","):fcs.rfind(")")]
                    if b==d:
                        if mpt_af_mouth_auto: #Check if automatic mouth control is enabled.
                            if not mpt_af_manual_tag_mouth_check(c) and mpt_af_manual_tag_mouth_logic_check(c): #Check if specific mouth is in use and if the logical attribute is not present.
                                if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #Check if automatic zorder control should be applied.
                                    renpy.show(c + " cm",at_list=[tcommon(a.xpos)], zorder = 0) #Automatic mouth control is enabled, unfocus the character, change zorder.
                                else: #No automatic zorder control.
                                    renpy.show(c + " cm",at_list=[tcommon(a.xpos)]) #Automatic mouth control is enabled, unfocus the character, do not change zorder.
                            else: #Specific mouth in use OR the logical attribute is not present, no change to mouth.
                                if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #Check if automatic zorder control should be applied.
                                    renpy.show(c,at_list=[tcommon(a.xpos)], zorder = 0) #No change to mouth, unfocus the character, change zorder.
                                else: #No automatic zorder control.
                                    renpy.show(c,at_list=[tcommon(a.xpos)]) #No change to mouth, unfocus the character, do not change zorder.
                                renpy.show(c,at_list=[tcommon(a.xpos)])
                        else: #Automatic mouth control is not enabled.
                            if mpt_af_manual_tag_zorder_logic_check(c) and mpt_af_zorder_auto: #Check if automatic zorder control should be applied.
                                    renpy.show(c,at_list=[tcommon(a.xpos)], zorder = 0) #No change to mouth, unfocus the character, change zorder.
                            else: #No automatic zorder control.
                                renpy.show(c,at_list=[tcommon(a.xpos)]) #No change to mouth, unfocus the character, do not change zorder.
                    elif mpt_af_mouth_auto and not mpt_af_manual_tag_mouth_check(c) and mpt_af_manual_tag_mouth_logic_check(c):
                        renpy.show(c+" cm")
    def n_af(speaker,dialog):
        '''
        This function turns the autofocus off for a dialog line, then turns it all back on.
        
        Use this if a particular line of dialog is causing problems, for example, a line after multiple animated transforms.
         $n_af(y,"Hello World") will say "Hello World" with no autofocus.
        '''
        if not renpy.in_rollback():
            narrator.display_args["callback"] = None
            mc.display_args["callback"] = None
            s.display_args["callback"] = None
            m.display_args["callback"] = None
            n.display_args["callback"] = None
            y.display_args["callback"] = None
        renpy.say(speaker,dialog)
        narrator.display_args["callback"] = autofocus_narrator
        mc.display_args["callback"] = autofocus_narrator
        s.display_args["callback"] = af_callback_s
        m.display_args["callback"] = af_callback_m
        n.display_args["callback"] = af_callback_n
        y.display_args["callback"] = af_callback_y
    #This ensures we always have the callbacks running (they don't get saved or loaded)
    #The callbacks can be added to the Character definitions instead if you like.
    #Doing it this way ensures that we don't blow away changes to Character objects you've defined other places (probably definitions.rpy)
    from functools import partial
    af_callback_s = partial(autofocus,"sayori")
    af_callback_n = partial(autofocus,"natsuki")
    af_callback_m = partial(autofocus,"monika")
    af_callback_y = partial(autofocus,"yuri")
    narrator.display_args["callback"] = autofocus_narrator
    mc.display_args["callback"] = autofocus_narrator #If you're using sprites for MC, make a callback for him similar to above, since he shouldn't be treated as a narrator then.
    s.display_args["callback"] = af_callback_s
    m.display_args["callback"] = af_callback_m
    n.display_args["callback"] = af_callback_n
    y.display_args["callback"] = af_callback_y
        