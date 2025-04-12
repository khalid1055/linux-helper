# 🔧 linux-helper

💻 **`linux-helper`** is an AI-assisted command-line companion designed for **everyday Linux users**, not just developers.

This tool allows you to write simple, natural English instructions like:

```
Show me the files here  
Install VLC  
What is my IP address?  
Search for "error" in logs  
```

…and automatically translates them into the correct Linux commands:

```bash
ls
sudo apt install vlc
ip a
grep -r "error" /var/log/
```

---

## 💡 Why linux-helper?

Most Linux tools are built for advanced users and developers.  
**`linux-helper`** simplifies the Linux experience for **students, tech enthusiasts, and new users** by acting as a smart shell assistant.

- 🧠 Understands natural English input
- ⚙️ Suggests or runs real system commands
- 💬 Explains what each command does before execution
- 🔒 Works offline (local matching engine, with optional AI integrations)
- 🧱 Modular design (fuzzy, exact, or AI-based matching)

---

## 🛠️ Built with:

- Python 3
- RapidFuzz for fuzzy matching
- Modular architecture (easy to extend)
- JSON-based command mapping

---

## 🚀 Roadmap:

- 🤖 Local AI model integration (LLaMA, Mistral, GPT4All)
- 💻 Optional GUI (Tkinter, Textual, or Web-based)
- 📦 pip and .deb install support

---

## 📂 Project Structure:

```bash
linux-helper/
│
├── main.py              # CLI entry point
├── matcher/
│   ├── __init__.py
│   ├── base.py          # Base matcher interface
│   ├── fuzzy.py         # Fuzzy matching logic
│   ├── exact.py         # Exact match logic
│   └── embedding.py     # (planned) AI matching
├── commands.json        # Natural phrases to command mapping
└── README.md
```

---

## ✨ Getting Started (coming soon)

```bash
pip install linux-helper
linux-helper
```

This will launch the assistant, ready to interpret and execute your natural-language Linux tasks.

---

## 🤝 Contributing

Want to add more commands, improve accuracy, or build a GUI? Pull requests are welcome!

---

## 📜 License

MIT License. Use it, modify it, share it.

