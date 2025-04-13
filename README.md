# WhatsApp Scheduler App

A simple Android application to schedule WhatsApp messages using Kivy.

## Features
- Schedule WhatsApp messages for a future time
- Simple and intuitive user interface
- Input validation for phone numbers and time format

## Requirements
- Python 3.7+
- Kivy 2.0.0+
- pywhatkit
- Android device or emulator

## Building the App
1. Install buildozer:
```bash
pip install buildozer
```

2. Initialize buildozer (already done):
```bash
buildozer init
```

3. Build the Android APK:
```bash
buildozer android debug deploy run
```

## Usage
1. Enter the recipient's phone number with country code (e.g., +1234567890)
2. Type your message
3. Set the time in 24-hour format (HH:MM)
4. Click "Schedule Message"

## Note
- The app requires an active internet connection
- WhatsApp must be installed on your device
- The phone number must include the country code
