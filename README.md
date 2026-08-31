# ARVA - AI Voice Recognition Assistant

ARVA is a voice-controlled AI assistant that listens to user commands and performs automated tasks on Windows systems. It uses speech recognition to convert voice input into actionable commands that control applications, files, and system functions.

## 🎯 Features

- **Voice Command Recognition**: Uses Google's speech recognition API to understand spoken commands
- **Application Control**: Open, launch, and close applications
- **File & Folder Management**: Navigate and open files and folders (Downloads, Documents, Desktop, Pictures, Videos)
- **Keyboard Control**: Type text and press keyboard keys/hotkeys
- **Mouse Control**: Click, double-click, right-click, scroll, and move the mouse
- **Screen Interaction**: 
  - Take screenshots
  - Read text from the screen using OCR
  - Click on text elements on the screen
- **Command Parsing**: Natural language processing to parse and understand user intents
- **Natural Exit**: Say "exit", "quit", "stop", or "goodbye arva" to terminate the program

## 📋 Command Examples

### Application Control
- "Open Chrome"
- "Launch VS Code"
- "Close Notepad"

### File & Folder Operations
- "Open my documents"
- "Open desktop"
- "Open config.txt"

### Text & Keyboard
- "Type Hello World"
- "Press Enter"
- "Press Control Shift S" (hotkey combination)

### Mouse Operations
- "Click"
- "Double click"
- "Right click"
- "Scroll up"
- "Scroll down"
- "Move cursor to 500 1000"

### Screen Operations
- "Take screenshot"
- "Read the screen"
- "Click button" (finds and clicks on text/element)

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- Microphone for voice input
- Windows OS (the windows module requires Windows)

### Required Dependencies
```bash
pip install SpeechRecognition
pip install pyaudio
pip install Pillow
pip install pytesseract
pip install pyautogui
pip install pynput
```

### Additional Setup
For OCR functionality, you'll need Tesseract OCR:
1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to the default location or update the path in the code

## 🚀 Usage

Run the main script:
```bash
python main.py
```

The assistant will display:
```
================================
        ARVA Assistant
================================
Say a command. Say 'exit' to stop.
```

Simply speak your command into the microphone. The assistant will process your command and execute the corresponding action.

## 📁 Project Structure

```
ARVA/
├── main.py              # Main entry point and command loop
├── voice.py             # Speech recognition functionality
├── command.py           # Command execution engine
├── parser.py            # Natural language command parser
├── windows/             # Windows-specific modules
│   ├── controller.py    # Application and file operations
│   ├── keyboard.py      # Keyboard input control
│   ├── mouse.py         # Mouse control
│   ├── screen.py        # Screenshot functionality
│   └── ocr.py          # Text recognition from images
├── tests/              # Test suite
└── Testing/            # Additional test files
```

## 🔧 Core Components

### `main.py`
Entry point that sets up the voice listening loop and processes user commands.

### `voice.py`
Handles microphone input and converts speech to text using Google's speech recognition API.

### `parser.py`
Parses natural language commands and extracts intent and target parameters. Supports 40+ command patterns including:
- Open/Launch/Start commands
- Close/Stop/Exit commands
- Type/Write commands
- Mouse and keyboard operations
- Screenshot and screen reading

### `command.py`
Executes the parsed commands by calling appropriate Windows system functions.

## 📝 Command Parsing

The parser supports flexible command syntax with optional prefixes:
- "Hey ARVA, open Chrome" 
- "Arva, please open Chrome"
- "Could you open Chrome"
- "Open Chrome"

All variations are normalized and processed identically.

## ⚙️ System Requirements

- **OS**: Windows
- **Python**: 3.7 or higher
- **Audio Input**: Working microphone
- **Disk Space**: ~100MB for dependencies

## 🐛 Troubleshooting

### "I couldn't understand you"
- Speak clearly and at a normal pace
- Check microphone is working and positioned correctly
- Ensure no background noise

### "Speech recognition service is unavailable"
- Check internet connection (Google's API requires online connection)
- Verify firewall isn't blocking network access

### OCR not working
- Ensure Tesseract OCR is installed
- Update the path in `windows/ocr.py` if installed to custom location

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by aryanns11-art

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 🔮 Future Enhancements

- [ ] Custom wake word support
- [ ] Offline speech recognition
- [ ] Linux and macOS support
- [ ] Context-aware commands
- [ ] Command history and shortcuts
- [ ] User profiles and preferences
- [ ] Web-based control panel
