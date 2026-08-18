OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run",
]

CLOSE_WORDS = [
    "close",
    "stop",
    "exit",
    "quit",
]

FOLDER_NAMES = [
    "downloads",
    "documents",
    "desktop",
    "pictures",
    "videos",
]

TYPE_WORDS = [
    "type",
    "write",
]

PRESS_WORDS = [
    "press",
]

COMBINATION_WORDS = [
    "hotkey",
]

MOUSE_CLICK_WORDS = [
    "click",
]

MOUSE_DOUBLE_CLICK_WORDS = [
    "double click",
]

MOUSE_RIGHT_CLICK_WORDS = [
    "right click",
]

MOUSE_SCROLL_WORDS = [
    "scroll",
]

MOVE_MOUSE=[
    'move',
]

def clean_command(command):

    command = command.lower().strip()

    prefixes = [
        "hey arva",
        "arva",
        "please",
        "can you",
        "could you",
        "would you",
    ]

    changed = True

    while changed:

        changed = False

        for prefix in prefixes:

            if command.startswith(prefix):
                command = command[len(prefix):].strip()

                changed = True

    return command

def parse_command(command):

    if command is None:
        return None

    command = clean_command(command)

    # ------------OPEN / LAUNCH / START-----------------------

    for word in OPEN_WORDS:

        if command == word or command.startswith(word + " "):
            target = command[len(word):].strip()
            target = target.removeprefix("my ")
            target = target.removesuffix(" folder")
            target = target.removesuffix(" file")
            if not target:
                return {
                    "intent": "UNKNOWN",
                    "target": None
                }
            if target in FOLDER_NAMES:
                return {
                    "intent": "OPEN_FOLDER",
                    "target": target
                }
            if "." in target:
                return {
                    "intent": "OPEN_FILE",
                    "target": target
                }
            return {
                "intent": "OPEN_APP",
                "target": target
            }

    # ------------CLOSE / EXIT / STOP------------------
    
    for word in CLOSE_WORDS:

        if command == word or command.startswith(word + " "):
            
                target = command[len(word):].strip()
                if not target:
                    return {
                        "intent": "UNKNOWN",
                        "target": None
                    }
                return {
                    "intent": "CLOSE_APP",
                    "target": target
                }

    # -------------TYPE TEXT-------------------------------------

    for word in TYPE_WORDS:

        if command == word or command.startswith(word + " "):

            target = command[len(word):].strip()

            if not target:
                return {
                    "intent": "UNKNOWN",
                    "target": None
                }

            return {
                "intent": "TYPE_TEXT",
                "target": target
            }

    # -------------PRESS KEY-------------------

    for word in PRESS_WORDS:

        if command == word or command.startswith(word + " "):
            target = command[len(word):].strip()
            if not target:
                return {
                    "intent": "UNKNOWN",
                    "target": None
                }
            if ' ' in target:
                return{
                    'intent':'PRESS_HOTKEY',
                    'target': target
                }
            return {
                "intent": "PRESS_KEY",
                "target": target
            }

    # -------MOUSE DOUBLE CLICK----------
    
    if command == "double click":

        return {
            "intent": "MOUSE_DOUBLE_CLICK",
            "target": None
        }
    
    # ----------MOUSE RIGHT CLICK---------------
    
    if command == "right click":

        return {
            "intent": "MOUSE_RIGHT_CLICK",
            "target": None
        }


    # ----------MOUSE CLICK-------------------------
    
    if command == "click":

        return {
            "intent": "MOUSE_CLICK",
            "target": None
        }


    # ------------MOUSE SCROLL-----------------------

    if command == "scroll up":

        return {
            "intent": "MOUSE_SCROLL",
            "target": "up"
        }


    if command == "scroll down":

        return {
            "intent": "MOUSE_SCROLL",
            "target": "down"
        }


    # ------------ MOUSE MOVE -----------------------

    if command.startswith("move mouse to "):

        target = command[len("move mouse to "):].strip()
        parts = target.split()

        if len(parts) != 2:
            return {
                "intent": "UNKNOWN",
                "target": None
            }

        try:
            x = int(parts[0])
            y = int(parts[1])

        except ValueError:
            return {
                "intent": "UNKNOWN",
                "target": None
            }

        return {
            "intent": "MOUSE_MOVE",
            "target": (x, y)
        }


    
    

    return {
        "intent": "UNKNOWN",
        "target": None
    }