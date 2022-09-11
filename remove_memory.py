# A function to remove memory from the dialogue
def remove_memory(dialogue):
    dialogue = dialogue.split(":")

    if dialogue[0] == "Human":
        dialogue[1] = dialogue[1][:-2]
        del dialogue[0:2]
        dialogue.insert(0,"AI")

    elif dialogue[0] == "AI":
        dialogue[1] = dialogue[1][:-5]
        del dialogue[0:2]
        dialogue.insert(0,"Human")

    dialogue = ":".join(dialogue)

    return dialogue