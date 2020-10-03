from tkinter import *
from PIL import ImageTk, Image

#Vox, HEV Suit, and Marines database of sayable things

vox = [
"", "a", "accelerating", "accelerator", "accepted", "access", "acknowledge", "acknowledged", "acquired", "acquisition", "across", "activate", "activated", "activity", "adios", "administration", "advanced", "after", "agent", "alarm", "alert", "alien", "aligned", "all", "alpha", "am", "amigo", "ammunition", "an", "and", "announcement", "anomalous", "antenna", "any", "apprehend", "approach", "are", "area", "arm", "armed", "armor", "armory", "arrest", "ass", "at", "atomic", "attention", "authorize", "authorized", "automatic", "away", "b", "back", "backman", "bad", "bag", "bailey", "barracks", "base", "bay", "be", "been", "before", "beyond", "biohazard", "biological", "birdwell", "bizwarn", "black", "blast", "blocked", "bloop", "blue", "bottom", "bravo", "breach", "breached", "break", "bridge", "bust", "but", "button", "buzwarn", "bypass", "c", "cable", "call", "called", "canal", "cap", "captain", "capture", "ceiling", "celsius", "center", "centi", "central", "chamber", "charlie", "check", "checkpoint", "chemical", "cleanup", "clear", "clearance", "close", "code", "coded", "collider", "command", "communication", "complex", "computer", "condition", "containment", "contamination", "control", "coolant", "coomer", "core", "correct", "corridor", "crew", "cross", "cryogenic", "d", "dadeda", "damage", "damaged", "danger", "day", "deactivated", "decompression", "decontamination", "deeoo", "defense", "degrees", "delta", "denied", "deploy", "deployed", "destroy", "destroyed", "detain", "detected", "detonation", "device", "did", "die", "dimensional", "dirt", "disengaged", "dish", "disposal", "distance", "distortion", "do", "doctor", "doop", "door", "down", "dual", "duct", "e", "east", "echo", "ed", "effect", "egress", "eight", "eighteen", "eighty", "electric", "electromagnetic", "elevator", "eleven", "eliminate", "emergency", "energy", "engage", "engaged", "engine", "enter", "entry", "environment", "error", "escape", "evacuate", "exchange", "exit", "expect", "experiment", "experimental", "explode", "explosion", "exposure", "exterminate", "extinguish", "extinguisher", "extreme", "f", "facility", "fahrenheit", "failed", "failure", "farthest", "fast", "feet", "field", "fifteen", "fifth", "fifty", "final", "fine", "fire", "first", "five", "flooding", "floor", "fool", "for", "forbidden", "force", "forms", "found", "four", "fourteen", "fourth", "fourty", "foxtrot", "freeman", "freezer", "from", "front", "fuel", "g", "get", "go", "going", "good", "goodbye", "gordon", "got", "government", "granted", "great", "green", "grenade", "guard", "gulf", "gun", "guthrie", "handling", "hangar", "has", "have", "hazard", "head", "health", "heat", "helicopter", "helium", "hello", "help", "here", "hide", "high", "highest", "hit", "hole", "hostile", "hot", "hotel", "hour", "hours", "hundred", "hydro", "i", "idiot", "illegal", "immediate", "immediately", "in", "inches", "india", "ing", "inoperative", "inside", "inspection", "inspector", "interchange", "intruder", "invallid", "invasion", "is", "it", "johnson", "juliet", "key", "kill", "kilo", "kit", "lab", "lambda", "laser", "last", "launch", "leak", "leave", "left", "legal", "level", "lever", "lie", "lieutenant", "life", "light", "lima", "liquid", "loading", "locate", "located", "location", "lock", "locked", "locker", "lockout", "lower", "lowest", "magnetic", "main", "maintenance", "malfunction", "man", "mass", "materials", "maximum", "may", "medical", "men", "mercy", "mesa", "message", "meter", "micro", "middle", "mike", "miles", "military", "milli", "million", "minefield", "minimum", "minutes", "mister", "mode", "motor", "motorpool", "move", "must", "nearest", "nice", "nine", "nineteen", "ninety", "no", "nominal", "north", "not", "november", "now", "number", "objective", "observation", "of", "officer", "ok", "on", "one", "open", "operating", "operations", "operative", "option", "order", "organic", "oscar", "out", "outside", "over", "overload", "override", "pacify", "pain", "pal", "panel", "percent", "perimeter", "permitted", "personnel", "pipe", "plant", "platform", "please", "point", "portal", "power", "presence", "press", "primary", "proceed", "processing", "progress", "proper", "propulsion", "prosecute", "protective", "push", "quantum", "quebec", "question", "questioning", "quick", "quit", "radiation", "radioactive", "rads", "rapid", "reach", "reached", "reactor", "red", "relay", "released", "remaining", "renegade", "repair", "report", "reports", "required", "research", "resevoir", "resistance", "right", "rocket", "roger", "romeo", "room", "round", "run", "safe", "safety", "sargeant", "satellite", "save", "science", "scream", "screen", "search", "second", "secondary", "seconds", "sector", "secure", "secured", "security", "select", "selected", "service", "seven", "seventeen", "seventy", "severe", "sewage", "sewer", "shield", "shipment", "shock", "shoot", "shower", "shut", "side", "sierra", "sight", "silo", "six", "sixteen", "sixty", "slime", "slow", "soldier", "some", "someone", "something", "son", "sorry", "south", "squad", "square", "stairway", "status", "sterile", "sterilization", "storage", "sub", "subsurface", "sudden", "suit", "superconducting", "supercooled", "supply", "surface", "surrender", "surround", "surrounded", "switch", "system", "systems", "tactical", "take", "talk", "tango", "tank", "target", "team", "temperature", "temporal", "ten", "terminal", "terminated", "termination", "test", "that", "the", "then", "there", "third", "thirteen", "thirty", "this", "those", "thousand", "threat", "three", "through", "time", "to", "top", "topside", "touch", "towards", "track", "train", "transportation", "truck", "tunnel", "turn", "turret", "twelve", "twenty", "two", "unauthorized", "under", "uniform", "unlocked", "until", "up", "upper", "uranium", "us", "usa", "use", "used", "user", "vacate", "valid", "vapor", "vent", "ventillation", "victor", "violated", "violation", "voltage", "vox_login", "walk", "wall", "want", "wanted", "warm", "warn", "warning", "waste", "water", "we", "weapon", "west", "whiskey", "white", "wilco", "will", "with", "without", "woop", "xeno", "yankee", "yards", "year", "yellow", "yes", "you", "your", "yourself", "zero", "zone", "zulu", "_comma", "_period"
]
fvox = [
"", "acquired", "activated", "administering_medical", "adrenaline_shot", "alert", "am", "ammo_depleted", "ammo_pickup", "antidote_shot", "antitoxin_shot", "armor_compromised", "armor_gone", "atmospherics_on", "automedic_on", "beep", "bell", "biohazard_detected", "bio_reading", "bleeding_stopped", "blip", "blood_loss", "blood_plasma", "blood_toxins", "boop", "buzz", "chemical_detected", "communications_on", "danger", "deactivated", "east", "eight", "eighteen", "eighty", "eleven", "evacuate_area", "fifteen", "fifty", "five", "flatline", "four", "fourteen", "fourty", "fuzz", "get_44ammo", "get_44pistol", "get_9mmclip", "get_alien_wpn", "get_assault", "get_assaultgren", "get_battery", "get_bolts", "get_buckshot", "get_crossbow", "get_egon", "get_egonpower", "get_gauss", "get_grenade", "get_medkit", "get_pistol", "get_rpg", "get_rpgammo", "get_satchel", "get_shotgun", "get_tripmine", "health_critical", "health_dropping", "health_dropping2", "heat_damage", "hev_critical_fail", "hev_damage", "hev_general_fail", "hev_logon", "hev_shutdown", "hiss", "hours", "immediately", "innsuficient_medical", "internal_bleeding", "major_fracture", "major_lacerations", "medical_repaired", "meters", "minor_fracture", "minor_lacerations", "minutes", "morphine_shot", "munitionview_on", "near_death", "nine", "nineteen", "ninety", "north", "one", "onehundred", "online", "pain_block", "percent", "pm", "position", "powerarmor_on", "powermove_on", "powermove_overload", "power_below", "power_level_is", "power_restored", "radiation_detected", "range", "remaining", "safe_day", "seconds", "seek_medic", "seven", "seventeen", "seventy", "shock_damage", "six", "sixteen", "sixty", "south", "targetting_system", "ten", "thirteen", "thirty", "three", "time_is_now", "time_remaining", "torniquette_applied", "twelve", "twenty", "twentyfive", "two", "vitalsigns_on", "voice_off", "voice_on", "warning", "weaponselect_on", "weapon_pickup", "west", "wound_sterilized", "your", "_comma", "_period"
]
hecu = [
"", "a!", "a", "affirmative!", "affirmative", "alert!", "alert", "alien!", "alien", "all!", "all", "am!", "am", "anything!", "are!", "are", "area!", "area", "ass!", "ass", "at!", "away!", "backup!", "backup", "bag!", "bastard!", "bastard", "blow!", "bogies!", "bogies", "bravo!", "bravo", "call!", "casualties!", "charlie!", "charlie", "check!", "check", "checking!", "checking", "clear!", "clear", "clik", "command!", "command", "continue!", "continue", "control!", "control", "cover!", "creeps!", "creeps", "damn!", "damn", "delta!", "delta", "down!", "down", "east!", "east", "echo!", "echo", "eightymeters", "eliminate", "everything", "fall!", "fiftymeters", "fight!", "fight", "fire!", "fire", "five!", "five", "fivemeters", "force!", "force", "formation!", "formation", "fortymeters", "four!", "four", "foxtrot!", "foxtrot", "freeman!", "freeman", "get!", "go!", "go", "god!", "god", "going!", "going", "got!", "got", "grenade!", "gr_alert1", "gr_die1", "gr_die2", "gr_die3", "gr_idle1", "gr_idle2", "gr_idle3", "gr_loadtalk", "gr_mgun1", "gr_mgun2", "gr_mgun3", "gr_pain1", "gr_pain2", "gr_pain3", "gr_pain4", "gr_pain5", "gr_reload1", "gr_step1", "gr_step2", "gr_step3", "gr_step4", "guard!", "guard", "have!", "have", "he!", "heavy!", "heavy", "hell!", "hell", "here!", "here", "hg_civvies", "hg_sucks", "hold!", "hold", "hole!", "hole", "hostiles!", "hostiles", "hot!", "hot", "hundredmeters", "i!", "i", "in!", "in", "is!", "is", "kick!", "lay!", "left!", "left", "lets!", "lets", "level!", "level", "lookout!", "lookout", "maintain!", "maintain", "mission!", "mission", "mister!", "mister", "mother!", "move!", "move", "movement!", "movement", "moves!", "moves", "my!", "my", "need!", "negative!", "negative", "neutralize!", "neutralized!", "niner!", "niner", "no!", "no", "north!", "north", "nothing!", "nothing", "objective!", "objective", "of!", "of", "oh!", "ok!", "ok", "one!", "one", "onefiftymeters", "orders!", "orders", "our!", "out!", "out", "over!", "over", "patrol!", "patrol", "people!", "people", "position!", "position", "post!", "post", "private!", "private", "quiet!", "quiet", "radio!", "radio", "recon!", "recon", "request!", "right!", "right", "roger!", "roger", "sector!", "sector", "secure!", "secure", "seventymeters", "shit!", "shit", "shot!", "shot", "sign!", "sign", "signs!", "signs", "silence!", "silence", "sir!", "sir", "six!", "six", "sixtymeters", "some!", "some", "something!", "something", "south!", "south", "squad!", "squad", "stay!", "stay", "suppressing!", "sweep!", "sweep", "take!", "tango!", "tango", "target!", "target", "team!", "team", "tenmeters", "that!", "that", "the!", "the", "there!", "there", "these!", "these", "thirtymeters", "this!", "this", "those!", "those", "three!", "three", "tight!", "tight", "twentymeters", "two!", "two", "twohundredmeters", "uhh", "under!", "up!", "up", "we!", "we've!", "we've", "we", "weapons!", "weapons", "weird!", "weird", "west!", "west", "will!", "yeah!", "yeah", "yes!", "yes", "yessir!", "yessir", "you!", "you", "your!", "your", "zero!", "zero", "zone!", "zone", "zulu!", "zulu"
]

#set some needed variables...

root = Tk()
root.title("Half Life 1 Sentence Tester")
VoxOrFvox = IntVar()
VoxOrFvox.set(1)
slicing = ""
sliced = ""
tainted = 0

#actually check the things when the Check! button is clicked

def check_buttononclick():
    tainted = 0

    #cut up the input
    slicing = tobechecked.get()
    sliced = slicing.split(" ")

    #run through and check the input if Vox is selected

    if VoxOrFvox.get() == 1:
        for word in sliced:
          print(word)
          if not word in vox:
              tainted = 1
              print("'"+word+"' not ok!")
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0,"'"+word+"' is not a valid word the Vox can say!")
          elif tainted == 0:
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0, "'"+slicing+"' is a valid sentence the Vox can say.")
        if tainted == 0:
            print("'"+slicing+"' is ok!")
        else:
            print("'"+slicing+"' is not ok.")
    
    #run through and check the input if HEV is selected

    if VoxOrFvox.get() == 2:
        for word in sliced:
          print(word)
          if not word in fvox:
              tainted = 1
              print("'"+word+"' not ok!")
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0,"'"+word+"' is not a valid word the HEV Suit can say!")
          elif tainted == 0:
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0, "'"+slicing+"' is a valid sentence the HEV Suit can say.")
        if tainted == 0:
            print("'"+slicing+"' is ok!")
        else:
            print("'"+slicing+"' is not ok.")

    #run though and check the input if HECUs are selected

    if VoxOrFvox.get() == 3:
        for word in sliced:
          print(word)
          if not word in hecu:
              tainted = 1
              print("'"+word+"' not ok!")
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0,"'"+word+"' is not a valid word a marine can say!")
          elif tainted == 0:
              ThisIsTheOutput.delete(0, END)
              ThisIsTheOutput.insert(0, "'"+slicing+"' is a valid sentence a marine can say.")
        if tainted == 0:
            print("'"+slicing+"' is ok!")
        else:
            print("'"+slicing+"' is not ok.")
    return

#make things to stick onto the screen, i.e. buttons, switches, and inputs.

inputframe = LabelFrame(root, text="Input", padx=5, pady=5)
rb1 = Radiobutton(inputframe, text="VOX (Normal Announcer)", variable=VoxOrFvox, value=1)
rb2 = Radiobutton(inputframe, text="FVOX (The HEV Suit)", variable=VoxOrFvox, value=2)
rb3 = Radiobutton(inputframe, text="HECUs (Marines)", variable=VoxOrFvox, value=3)
tobechecked = Entry(inputframe, width=100)
check_button = Button(inputframe, text="Test!", command=check_buttononclick)
outputframe = LabelFrame(root, text="Output", padx=5, pady=5)
ThisIsTheOutput = Entry(outputframe, width=100)

#throw said things onto the screen

inputframe.pack(padx=10)
tobechecked.pack()
rb1.pack(side=LEFT)
rb2.pack(side=LEFT)
rb3.pack(side=LEFT)
check_button.pack(side=RIGHT)
outputframe.pack()
ThisIsTheOutput.pack()

#make the quit button and stick it onto the screen

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

#i'm not fully sure what this does but it's needed

root.mainloop()

