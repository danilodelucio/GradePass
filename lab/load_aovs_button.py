def setShuffle(shuffle_value):
    with this_node:
        shuffle = nuke.toNode("MainShuffle")
        shuffle["in"].setValue(shuffle_value)

this_node = nuke.thisNode()
input_node = this_node.input(0)

if input_node:
    # Storing all the channels
    channels = input_node.channels()

    extra_passes = ["crypto", "normal", "vector", "depth", "uv", "position", "pref", "worldPosition"]
    subchannels_list = [".red", ".green", ".blue", ".alpha"]

    light_passes = list(set([c.split('.')[0] for c in channels]))

    for ep in extra_passes:
        for lp in light_passes:
            if ep in lp.lower():
                light_passes.remove(lp)

    print(light_passes)

    if len(light_passes) > 1:
        this_node["select_aov"].setValues(light_passes)
        this_node["select_aov"].setValue(0)

        setShuffle(light_passes[0])        

        print("- " + str(len(light_passes)) + " Light passes have been loaded!")
    else:
        this_node["select_aov"].setValues(["none"])

        setShuffle("rgb")

        print("- RGB passes not found!")
