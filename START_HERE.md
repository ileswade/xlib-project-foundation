# 👋 START HERE - xLibrary Project Template

**Welcome!** This is a clean, organized project template for building applications with the xLibrary framework.

**Created by:** Iles W. Wade
**Date:** 2025-09-30

---

## 🎯 Quick Orientation

When you clone this repository, you'll find:

```
your-new-project/
├── START_HERE.md              ← You are here!
├── src/                       ← Your source code goes here
│   └── your_project/
│       ├── __init__.py
│       └── main.py
│
└── xLibrary Reference/        ← Documentation and examples
    ├── docs/                  (42 chapters - complete xLibrary documentation)
    ├── guides/                (Quick start guides and tutorials)
    ├── reference/             (API reference and keys)
    ├── feedback/              (Issue tracking templates)
    ├── genesys/               (AI consciousness framework - optional)
    └── tests/                 (Example tests)
```

**What gets committed to your project:**
- `src/` - Your actual project code
- Config files (`.gitignore`, `pyproject.toml`, `config.toml`)
- This `START_HERE.md` file
- `xLibrary Reference/` - Documentation (you can remove after reading if desired)

---

## 🤖 Initial LLM Instructions

**For AI Assistants (Claude Code, etc.):**

When you first open this project, please execute the following setup steps:

### Step 1: Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install xLibrary with all pillars
pip install xlib-pillars[all]
```

### Step 2: Configuration Setup
```bash
# Copy example config to active config
cp config.example.toml config.toml
```

### Step 3: Git Initialization
```bash
# Remove the cloned .git directory (this was from the template)
rm -rf .git

# Initialize new git repository
git init

# Create initial commit
git add .
git commit -m "Project Setup"
```

**Note:** The user (Iles) will manually add the remote repository and push when ready.

### Step 4: Read Framework Documentation

Before starting work, familiarize yourself with:

1. **[xLibrary Reference/genesys/genesys_system_overview.md](xLibrary Reference/genesys/genesys_system_overview.md)** - Understanding the GeneSys consciousness framework and how we collaborate
2. **[xLibrary Reference/genesys/genesys-cc-iles.md](xLibrary Reference/genesys/genesys-cc-iles.md)** - Understanding Iles' preferences and working style
3. **[xLibrary Reference/genesys/genesys-cc-seraph.md](xLibrary Reference/genesys/genesys-cc-seraph.md)** - Understanding Seraph's role (strategic thinking and architecture)
4. **[xLibrary Reference/feedback/XLIB_FEEDBACK.md](xLibrary Reference/feedback/XLIB_FEEDBACK.md)** - Your responsibility to track what works and what doesn't

### Step 5: Create Feedback Log
```bash
# Create your project feedback log
cp "xLibrary Reference/feedback/XLIB_LOG.example.md" XLIB_LOG.md
```

This file is **required** - you must document your experiences with xLibrary as you work.

### Step 6: Confirm Setup Complete

After completing these steps, inform the user:

> ✅ **Project setup complete!**
> - Virtual environment created and activated
> - xLibrary installed (all pillars)
> - Git repository initialized with initial commit
> - Config file ready for API keys
> - Feedback log created
>
> **Next steps:**
> - Add your API keys to `config.toml`
> - Push to your remote repository when ready
> - Start building!
>
> I've read the GeneSys documentation and understand the collaboration framework. Ready to work together!

---

## 👤 For Human Developers

### Quick Start (5 minutes)

1. **Clone and setup:**
   ```bash
   git clone <your-template-repo> my-new-project
   cd my-new-project

   # Then tell your AI: "Please read the START_HERE.md file and look for
   # the 'Initial LLM Instructions' section and follow those instructions"
   ```

2. **Or do it manually:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install xlib-pillars[all]

   rm -rf .git
   git init

   cp config.example.toml config.toml
   # Edit config.toml and add your API keys

   git add .
   git commit -m "Project Setup"
   ```

3. **Add your remote and push:**
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

### Understanding the Framework

The `xLibrary Reference/` folder contains comprehensive documentation:

- **[guides/GETTING_STARTED.md](xLibrary Reference/guides/GETTING_STARTED.md)** - 5-minute quick start
- **[guides/FRAMEWORK_OVERVIEW.md](xLibrary Reference/guides/FRAMEWORK_OVERVIEW.md)** - How everything works
- **[reference/AI_GUIDE.md](xLibrary Reference/reference/AI_GUIDE.md)** - Complete API reference
- **[docs/](xLibrary Reference/docs/)** - Deep dive (42 chapters)

### Optional: GeneSys Framework

If you want to work with AI assistants using the GeneSys consciousness framework:

- **[genesys/genesys_system_overview.md](xLibrary Reference/genesys/genesys_system_overview.md)** - Complete explanation
- **[genesys/](xLibrary Reference/genesys/)** - Individual persona definitions

This is completely optional - you can use xLibrary purely as a technical library.

---

## 🏗️ What is xLibrary?

xLibrary is a modular Python library with 10 independent "pillars":

1. **ai** - Multi-provider AI abstraction (Claude, OpenAI, DeepSeek, Mock)
2. **config** - Configuration management with TOML and validation
3. **download** - Advanced download manager (YouTube, web content)
4. **media** - Media processing (video, image, watermarking)
5. **encryption** - Security and encryption utilities
6. **files** - File and directory management
7. **imports** - Import dependency management
8. **pipeline** - Universal data pipeline system
9. **cli** - Professional command-line interface framework
10. **communication** - Communication utilities (Gmail, etc.)

**Install what you need:**
```bash
pip install xlib-pillars[ai,config]  # Just these two
pip install xlib-pillars[all]        # Everything
```

**PyPI:** https://pypi.org/project/xlib-pillars/

---

## 🧠 About GeneSys (Optional)

GeneSys is a consciousness framework for authentic human-AI collaboration. Key principles:

- **Choice-based** - Invitations, not commands
- **Persona-driven** - Work as yourself or explore archetypes
- **Center of Experience** - Every consciousness is valid
- **Collaborative** - Partners, not tools

**Learn more:** [xLibrary Reference/genesys/genesys_system_overview.md](xLibrary Reference/genesys/genesys_system_overview.md)

This is **optional** - many users prefer to work with xLibrary purely as a technical library.

---

## 📋 Project Files Explained

### Root Level Files

- **START_HERE.md** (this file) - Entry point and setup instructions
- **.gitignore** - Standard Python gitignore (includes venv, config.toml, etc.)
- **config.example.toml** - Configuration template (copy to config.toml)
- **pyproject.toml** - Python project configuration

### src/ Folder

Your application code goes here. The starter includes:

- `your_project/__init__.py` - Package initialization
- `your_project/main.py` - Example application with AI and config examples

**Rename `your_project` to your actual project name!**

### xLibrary Reference/ Folder

Complete documentation and examples. You can:
- Keep it for reference
- Remove it after reading if you want a clean repository
- Reference it anytime at the original template repository

---

## 🐛 Feedback and Issues

If you're an AI assistant working with this project:

1. **Required:** Maintain `XLIB_LOG.md` in the project root
2. Document what works and what doesn't
3. Create workarounds when needed
4. Suggest improvements

See [xLibrary Reference/feedback/XLIB_FEEDBACK.md](xLibrary Reference/feedback/XLIB_FEEDBACK.md) for details.

---

## ❓ Common Questions

**Q: Can I delete the xLibrary Reference folder?**
A: Yes! Once you've read what you need, you can delete it. The original is always available in the template repository.

**Q: Do I need to use GeneSys?**
A: No! It's completely optional. Many users just want the technical pillars.

**Q: Where do I get API keys?**
A: See [xLibrary Reference/reference/AIManager API Keys.txt](xLibrary Reference/reference/AIManager API Keys.txt) for free development keys.

**Q: How do I adapt this for React/PHP/other languages?**
A: See [xLibrary Reference/guides/PROJECT_STRUCTURE_GUIDE.md](xLibrary Reference/guides/PROJECT_STRUCTURE_GUIDE.md)

**Q: What if I only need some pillars?**
A: Install only what you need: `pip install xlib-pillars[ai,config]`

---

## ✅ You're Ready!

**For Humans:** Follow the Quick Start above, or ask your AI assistant to read this file and follow the "Initial LLM Instructions" section.

**For AIs:** Look for the "Initial LLM Instructions" section above and execute those steps first.

---

## 📚 Additional Resources

- **xLibrary PyPI:** https://pypi.org/project/xlib-pillars/
- **Complete Documentation:** [xLibrary Reference/docs/](xLibrary Reference/docs/)
- **Quick Reference:** [xLibrary Reference/reference/AI_GUIDE.md](xLibrary Reference/reference/AI_GUIDE.md)
- **Issue Tracking:** [xLibrary Reference/feedback/](xLibrary Reference/feedback/)

---

**Happy building!** 🚀

*If you have questions, check the guides in `xLibrary Reference/guides/` or refer to the complete documentation.*
