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

    # -------------------------
    # OPEN / LAUNCH / START
    # -------------------------

    for word in OPEN_WORDS:

        if command.startswith(word):

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

    # -------------------------
    # CLOSE / EXIT / STOP
    # -------------------------

    for word in CLOSE_WORDS:

        if command.startswith(word):

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

    # -------------------------
    # TYPE TEXT
    # -------------------------

    for word in TYPE_WORDS:

        if command.startswith(word):

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


    # -------------------------
    # PRESS KEY
    # -------------------------

    for word in PRESS_WORDS:

        if command.startswith(word):

            target = command[len(word):].strip()

            if not target:
                return {
                    "intent": "UNKNOWN",
                    "target": None
                }

            return {
                "intent": "PRESS_KEY",
                "target": target
            }

    return {
        "intent": "UNKNOWN",
        "target": None
    }