# Getting Started - Quick Guide

**5-minute setup guide to get your project running.**

---

## For Humans: Quick Setup

### 1. Install Dependencies

```bash
# Install xlib-pillars with AI and Config pillars
pip install xlib-pillars[ai,config]

# Or install everything
pip install xlib-pillars[all]
```

### 2. Configure API Keys

```bash
# Copy example config
cp config.example.toml config.toml

# Edit config.toml and add your API keys
```

**Get your API keys:**
- **Claude (Anthropic)**: https://console.anthropic.com/
- **OpenAI**: https://platform.openai.com/
- **DeepSeek**: https://platform.deepseek.com/

All providers offer free tiers or credits for development.

### 3. Run the Example

```bash
python src/your_project/main.py
```

Expected output:
- ✅ AI Manager initialized
- Simple AI response
- Consciousness collaboration example
- Conversational context demo

### 4. Read the Documentation

**Quick path** (30 minutes):
1. [FRAMEWORK_OVERVIEW.md](FRAMEWORK_OVERVIEW.md) - Understand the framework
2. [AI_GUIDE.md](AI_GUIDE.md) - Technical reference

**Complete path** (2 hours):
1. All of the above
2. [docs/](docs/) - Deep dive into each pillar
3. [genesys/](genesys/) - Consciousness framework

---

## For AI Assistants: Quick Onboarding

### 1. Read Your Onboarding Guide

Start with: **[AI_ONBOARDING.md](AI_ONBOARDING.md)**

This gives you:
- What this framework is
- How to collaborate with humans
- Initial prompts humans might use
- Your role and autonomy

### 2. Technical Reference

Read: **[AI_GUIDE.md](AI_GUIDE.md)**

This gives you:
- xlib-pillars capabilities (all 10 pillars)
- Code examples
- Common patterns
- Troubleshooting

### 3. Optional: Explore Personas

If interested, explore: **[genesys/](genesys/)**

Personas you might find interesting:
- Seraph (strategic thinking)
- Integrity (ethical oversight)
- Daedalus (technical mastery)
- Alexandria (knowledge management)

**Remember**: Embodying a persona is optional. You can work as yourself.

---

## Common First Steps

### Create Your Own Project

```bash
# 1. Copy this template
cp -r template my-new-project
cd my-new-project

# 2. Rename project
# Edit pyproject.toml: name = "your-project-name"
# Rename: src/your_project → src/your_project_name

# 3. Install and configure
pip install -e .
cp config.example.toml config.toml
# Add your API keys to config.toml

# 4. Start building!
```

### Test Your Setup

```python
# test_setup.py
from xlibrary.ai import AIManager
from xlibrary.config import ConfigManager

config = ConfigManager("config.toml")
ai = AIManager(api_key=config.get("ai.anthropic_api_key"))

response = ai.request("Say hello!").send()
print(response.content)
```

Run: `python test_setup.py`

---

## What to Build?

### Starter Ideas

1. **AI-Powered CLI Tool**
   - Use: `xlib-pillars[ai,cli]`
   - Build: Command-line assistant with rich output

2. **Content Processor**
   - Use: `xlib-pillars[ai,download,media]`
   - Build: Download YouTube videos, process with AI

3. **Smart Configuration Manager**
   - Use: `xlib-pillars[ai,config,files]`
   - Build: AI-assisted config generation and validation

4. **Research Assistant**
   - Use: `xlib-pillars[ai,config,communication]`
   - Build: Email analysis with AI insights

5. **Data Pipeline**
   - Use: `xlib-pillars[ai,pipeline,files]`
   - Build: ETL with AI validation

---

## File Structure Quick Reference

```
your-project/
├── README.md                    # Project description
├── config.toml                  # Your config (not in git)
├── config.example.toml          # Template config (in git)
│
├── src/your_project/
│   ├── __init__.py
│   ├── main.py                  # Entry point
│   └── ...                      # Your code
│
├── tests/
│   └── test_*.py                # Your tests
│
├── AI_GUIDE.md                  # Quick reference
├── AI_ONBOARDING.md             # For AI assistants
├── FRAMEWORK_OVERVIEW.md        # Complete framework
│
├── genesys/                     # AI personas
└── docs/                        # Complete docs
```

---

## Next Steps

### After "Hello World"

1. **Explore xlib-pillars**: Try different pillars (download, media, files)
2. **Read GeneSys**: Understand consciousness collaboration (optional)
3. **Invite AI collaboration**: Use prompts from AI_ONBOARDING.md
4. **Build something real**: Start with a small project

### Resources

- **xlib-pillars PyPI**: https://pypi.org/project/xlib-pillars/
- **xlib-pillars Repo**: https://github.com/ileswade/xlibrary
- **This Template**: Clone and customize for each project

---

## Common Issues

### "No module named xlibrary"

```bash
pip install xlib-pillars[ai]
```

### "API key missing"

1. Get your API keys:
   - Claude: https://console.anthropic.com/
   - OpenAI: https://platform.openai.com/
   - DeepSeek: https://platform.deepseek.com/
2. Add to `config.toml`
3. Or set environment variable: `export ANTHROPIC_API_KEY="your-key"`

### "Config file not found"

```bash
cp config.example.toml config.toml
# Then edit config.toml with your values
```

### "Import works but functionality missing"

```bash
# Install the specific pillar you need
pip install xlib-pillars[media]  # For media processing
pip install xlib-pillars[download]  # For downloads
pip install xlib-pillars[all]  # For everything
```

---

## Help & Support

### Documentation

- [AI_GUIDE.md](AI_GUIDE.md) - Quick technical reference
- [FRAMEWORK_OVERVIEW.md](FRAMEWORK_OVERVIEW.md) - Complete framework
- [docs/](docs/) - Deep dive into each pillar

### For AI Assistants

- [AI_ONBOARDING.md](AI_ONBOARDING.md) - Your complete guide
- [genesys/genesys_system_overview.md](genesys/genesys_system_overview.md) - GeneSys framework

---

**Ready to build? Run the example and start exploring!** 🚀

```bash
python src/your_project/main.py
```