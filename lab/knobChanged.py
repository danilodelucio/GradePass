def setShuffle(shuffle_value):
    with this_node:
        shuffle = nuke.toNode("MainShuffle")
        shuffle["in"].setValue(shuffle_value)

this_node = nuke.thisNode()
this_knob = nuke.thisKnob()

if this_knob.name() in ("viewer"):
    viewer = this_node["viewer"].getValue()
    
    with this_node:
        switch_node = nuke.toNode("MainSwitch")
        switch_node["which"].setValue(viewer)

if this_knob.name() in ("disable_adjustments"):
    disable_check = this_node["disable_adjustments"].getValue()
    disable_label = this_node["label_disable_text"]

    if int(disable_check) == 1:
        disable_label.setValue("<h3><font color='#CC3333'>ALL ADJUSTMENTS ARE DISABLED!")
    else:
        disable_label.setValue("            ")

if this_knob.name() in ("select_aov"):
    aov = this_node["select_aov"].value()

    setShuffle(aov)
