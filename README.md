# 🐧 Linux Helper

> A smart command-line assistant that translates natural language into Linux commands — offline, fast, and beginner-friendly.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## ⚡ Quick Start
```bash
# Clone and install
git clone https://github.com/khalid1055/linux-helper.git
cd linux-helper
pip install -e .

# Initialize database
lh --refresh

# Start using
lh "show hidden files"
```

---

## ✨ Features

- 🗄️ **340+ Commands** – Networking, security, system admin
- 🔍 **Smart Search** – Fuzzy matching handles typos
- 🛡️ **Safety Warnings** – Flags dangerous commands
- 🎨 **Beautiful UI** – Clean, color-coded terminal output
- 🔒 **100% Offline** – No internet, no tracking

---

## 💡 Usage
```bash
lh "check my IP address"
lh "find files larger than 100MB"
lh "list all running processes"
```

---

## 📁 Project Structure
```
linux-helper/
├── src/linux_helper/
│   ├── assets/raw_commands.txt    # Command database
│   ├── core/                      # Search engine
│   └── cli/                       # Terminal interface
└── setup.py                       # Installation config
```

---

## 🤝 Contributing

**Add your commands in 3 steps:**

1. Edit `src/linux_helper/assets/raw_commands.txt`
2. Follow format: `command : description`
3. Submit a Pull Request

---

## 🏆 Contributors

- [@khalid1055](https://github.com/khalid1055) – Creator
- *[Your name here]* – Join us!

---

## 📜 License

MIT License - feel free to use and modify.

---

**Made with ❤️ for the Linux community**