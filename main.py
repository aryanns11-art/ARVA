from voice import listen
from command import execute_command
from windows.voice import speak

print("================================")
print("        ARVA Assistant")
print("================================")
print("Say a command. Say 'exit' to stop.")


while True:

    command = listen()

    if command is None:
        continue

    if command.lower().strip() in [
        "exit",
        "quit",
        "stop",
        "goodbye arva",
    ]:

        print("Goodbye!")
        speak("Goodbye!")
        break

    execute_command(command)