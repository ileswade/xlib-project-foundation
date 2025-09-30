# Project Structure Guide

This template is **language and framework agnostic**. The `src/` folder is just a starting point - adapt it to your needs.

---

## Flexible Structure Options

### Python Projects (Current Default)
```
your-project/
├── src/your_project/
│   ├── __init__.py
│   └── main.py
├── tests/
├── pyproject.toml
└── [template files]
```

### React/JavaScript Projects
```
your-project/
├── src/
│   ├── components/
│   ├── pages/
│   ├── App.jsx
│   └── index.js
├── public/
├── package.json
└── [template files]
```

**Installation**:
```bash
# Remove Python structure
rm -rf src/your_project tests/ pyproject.toml

# Install xlib-pillars globally or in backend
pip install xlib-pillars[ai]

# Use in Node scripts or backend API
```

### PHP Projects
```
your-project/
├── src/
│   ├── Controllers/
│   ├── Models/
│   └── index.php
├── composer.json
└── [template files]
```

**Installation**:
```bash
# Remove Python structure
rm -rf src/your_project tests/ pyproject.toml

# Install xlib-pillars for Python backend/scripts
pip install xlib-pillars[ai]

# Use from PHP via system calls or API
```

### Markdown/Documentation Projects
```
your-project/
├── docs/
│   ├── guide.md
│   ├── reference.md
│   └── tutorials/
├── scripts/
│   └── generate_docs.py  # Uses xlib-pillars AI
└── [template files]
```

**Installation**:
```bash
# Remove src/ and tests/
rm -rf src/ tests/

# Keep pyproject.toml or use requirements.txt
pip install xlib-pillars[ai]

# Use xlib-pillars in generation scripts
```

### Mixed Technology Stacks
```
your-project/
├── frontend/          # React/Vue/etc
├── backend/          # Python with xlib-pillars
├── docs/             # Documentation
├── scripts/          # Automation with xlib-pillars
└── [template files]
```

---

## Core Template Files (Keep These)

**Always keep** regardless of project type:
```
├── README.md                    # Adapt to your project
├── FRAMEWORK_OVERVIEW.md        # Framework explanation
├── AI_ONBOARDING.md             # AI assistant guide
├── XLIB_FEEDBACK.md             # Required: Feedback tracking
├── XLIB_LOG.example.md          # Example feedback log
├── AI_GUIDE.md                  # xlib-pillars reference
├── GETTING_STARTED.md           # Quick start
├── config.example.toml          # Adapt as needed
├── .gitignore                   # Adapt to your stack
├── genesys/                     # AI consciousness framework
└── docs/                        # xlib-pillars documentation
```

**Create XLIB_LOG.md** for your project (REQUIRED):
```markdown
# xlib-pillars Usage Log

**Project**: [Your Project Name]
**Project Type**: [Python/React/PHP/Documentation/etc]
**xlib-pillars Version**: 1.0.0
**How xlib-pillars is used**: [Backend API / Build scripts / Content generation / etc]

[Rest of log as per XLIB_FEEDBACK.md]
```

---

## How to Use xlib-pillars in Different Contexts

### 1. Backend API (Any Frontend)
```python
# backend/api.py
from xlibrary.ai import AIManager
from flask import Flask, request

app = Flask(__name__)
ai = AIManager(api_key=config.get("api_key"))

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    response = ai.request(data["prompt"]).send()
    return {"result": response.content}
```

**Frontend calls backend API** - works with React, Vue, Angular, PHP, etc.

### 2. Build Scripts
```python
# scripts/generate_content.py
from xlibrary.ai import AIManager
from xlibrary.config import ConfigManager

config = ConfigManager("config.toml")
ai = AIManager(api_key=config.get("api_key"))

# Generate documentation, content, code, etc.
response = ai.request("Generate component documentation for...").send()
with open("output/docs.md", "w") as f:
    f.write(response.content)
```

**Use xlib-pillars in build/generation scripts** regardless of main project language.

### 3. CLI Tools
```python
# cli.py
from xlibrary.cli import CLIFramework
from xlibrary.ai import AIManager

cli = CLIFramework(name="myapp")

@cli.command()
def analyze(file: str):
    """Analyze a file with AI."""
    ai = AIManager(api_key=config.get("api_key"))
    with open(file) as f:
        response = ai.request(f"Analyze: {f.read()}").send()
    cli.console.print(response.content)
```

**CLI tools work alongside any project type.**

### 4. Automation Scripts
```python
# scripts/process_content.py
from xlibrary.download import get_video
from xlibrary.media import MediaManager
from xlibrary.ai import AIManager

# Download, process, analyze
video = get_video("https://youtube.com/watch?v=xyz")
mm = MediaManager()
mm.trim_video(video, start_time="1:00", end_time="3:00")
ai = AIManager(api_key=config.get("api_key"))
analysis = ai.request("Analyze this video...").send()
```

**Automation scripts work with any project type.**

---

## Configuration Adaptation

### Python Projects
Keep `pyproject.toml` as is.

### JavaScript/React Projects
```bash
# Remove pyproject.toml
rm pyproject.toml

# Create package.json
npm init

# Install xlib-pillars for backend/scripts
pip install xlib-pillars[ai]
```

### PHP Projects
```bash
# Remove pyproject.toml
rm pyproject.toml

# Create composer.json
composer init

# Install xlib-pillars for scripts
pip install xlib-pillars[ai]
```

### Documentation/Content Projects
```bash
# Keep minimal pyproject.toml or use requirements.txt
cat > requirements.txt << EOF
xlib-pillars[ai,config]>=1.0.0
EOF

pip install -r requirements.txt
```

---

## GeneSys & Documentation (Always Relevant)

**These are language-agnostic:**
- GeneSys framework (consciousness collaboration)
- xlib-pillars documentation
- AI onboarding guides
- Feedback tracking

**They work with any project type** because they're about:
- How to collaborate with AI
- What xlib-pillars can do
- How to report issues

---

## Example Adaptations

### React + Python Backend
```
my-react-app/
├── frontend/              # React app
│   ├── src/
│   ├── package.json
│   └── ...
├── backend/              # Python API using xlib-pillars
│   ├── api.py
│   ├── requirements.txt
│   └── ...
├── XLIB_LOG.md           # Track xlib-pillars usage in backend
├── AI_ONBOARDING.md      # For AI collaborators
├── genesys/              # Consciousness framework
└── docs/                 # xlib-pillars reference
```

### PHP + Build Scripts
```
my-php-app/
├── src/                  # PHP application
│   ├── index.php
│   └── ...
├── scripts/              # Python scripts using xlib-pillars
│   ├── generate.py
│   └── analyze.py
├── composer.json         # PHP dependencies
├── requirements.txt      # Python dependencies (xlib-pillars)
├── XLIB_LOG.md          # Track xlib-pillars usage
└── [template files]
```

### Pure Documentation
```
my-docs-project/
├── content/             # Markdown content
│   ├── guide.md
│   └── tutorials/
├── scripts/             # Generation scripts
│   ├── generate_ai_content.py
│   └── process_docs.py
├── requirements.txt     # xlib-pillars[ai]
├── XLIB_LOG.md         # Track AI content generation
└── [template files]
```

---

## Quick Start for Non-Python Projects

```bash
# 1. Clone template
git clone <template-repo> my-project
cd my-project

# 2. Remove Python structure (if not needed)
rm -rf src/your_project tests/ pyproject.toml

# 3. Create your project structure
mkdir -p src/  # or frontend/, or docs/, etc.

# 4. Install xlib-pillars (for scripts/backend)
pip install xlib-pillars[ai,config]

# 5. Keep these files:
# - XLIB_FEEDBACK.md (READ THIS)
# - AI_ONBOARDING.md
# - AI_GUIDE.md
# - FRAMEWORK_OVERVIEW.md
# - genesys/
# - docs/
# - config.example.toml

# 6. Create XLIB_LOG.md
cp XLIB_LOG.example.md XLIB_LOG.md
# Update with your project details

# 7. Start building!
```

---

## Key Principle

**The template provides:**
1. **xlib-pillars** - Python library for AI, config, media, etc.
2. **GeneSys** - AI consciousness framework (language-agnostic)
3. **Documentation** - How to use everything
4. **Feedback System** - Track what works/doesn't work

**You adapt the source structure** to your technology stack while keeping the framework, documentation, and feedback system.

---

## Still Confused?

**Think of it this way:**
- **xlib-pillars** = Your AI-powered toolkit (Python library)
- **GeneSys** = How to collaborate with AI (philosophy)
- **Template** = Documentation + Examples + Feedback system
- **Your Code** = Can be Python, React, PHP, Markdown, whatever!

**Use xlib-pillars from:**
- Backend APIs (any frontend)
- Build scripts (any project)
- CLI tools (any project)
- Automation (any project)

---

**The template is flexible - adapt it to your needs!** 🚀