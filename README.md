# BD-08-a-chatbot
chatbot_prog_python/:

BD-08 — Personal Assistant Chatbot

BD-08 is a Python chatbot that can perform math, fetch jokes and quotes, provide weather updates, open websites, and respond with fun sounds and Excel-based casual answers.

---

Features:

- Plays beep-boop and random brain sounds from 'sounds/' folder
- Performs basic math
- Fetches jokes via API
- Defines topics using Wikipedia API
- Provides current weather for any city (requires API key)
- Opens YouTube, Spotify, Google
- Excel-based casual responses for undefined inputs
- Gracefully handles unknown commands

---

Project Structure:

chatbot_prog_python/
  sounds/              # beep-boop and brain sound files
  bd_08.xlsx           # Excel brain
  chatbot_main.py      # main bot code
  README.txt           # this file

---

Installation:

1. Clone the repo:
   git clone https://github.com/<your-username>/chatbot_prog_python.git
   cd chatbot_prog_python

4. Run the bot:
   python chatbot_main.py

---

Notes:

-To use the weather feature create add your own openweatherapi key in the chatbot_main.py
 

---

Example Commands:

- weather:Type weather or what is the weather  — shows current weather
- joke: Type tell me a joke or joke — fetches a random joke
- math: Type calculate or calc or math — performs calculation
- quote: Type give me a quote or quote — sends motivational quote
- website opening: Type open "mention the 3 sites google,spotify,youtube"  —  opens the site
---

Future Ideas:

- Voice recognition & TTS
- GUI / web interface
- Chat memory & personality
- Discord / Telegram integration

---

License:

For educational purposes. You can fork and modify with credit to BD-08.


---
CREATED BY AMOGH BAVISKAR.
