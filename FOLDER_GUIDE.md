# 📁 Folder Organization Guide

This template is organized for easy navigation. Everything has its place!

---

## 🎯 Entry Point

**→ START_HERE.md** - Begin here! Directs you to the right documents based on who you are (human developer or AI assistant).

---

## 📂 Folder Structure

```
template/
│
├── START_HERE.md              ← Read this FIRST
├── README.md                  ← Template overview
├── config.example.toml        ← Config template (copy to config.toml)
├── pyproject.toml             ← Python project template
│
├── 📚 guides/                 ← Step-by-step guides (5 files)
│   ├── GETTING_STARTED.md          Quick 5-minute setup
│   ├── FRAMEWORK_OVERVIEW.md       How everything fits together
│   ├── AI_ONBOARDING.md            Complete guide for AI assistants
│   ├── PROJECT_STRUCTURE_GUIDE.md  Adapt to any language/framework
│   └── TEMPLATE_CONTENTS.md        Complete file inventory
│
├── 📖 reference/              ← Technical reference (2 files)
│   ├── AI_GUIDE.md                 xlib-pillars capabilities (890 lines)
│   └── AIManager API Keys.txt      Free development API keys
│
├── 🐛 feedback/               ← Issue tracking (2 files)
│   ├── XLIB_FEEDBACK.md            How to track issues (CRITICAL for AIs)
│   └── XLIB_LOG.example.md         Example of well-maintained log
│
├── 💻 src/                    ← Your source code
│   └── your_project/
│       ├── __init__.py
│       └── main.py                 Starter app with examples
│
├── 🧪 tests/                  ← Your tests
│   ├── __init__.py
│   └── test_example.py             Example tests with mock AI
│
├── 🧠 genesys/                ← AI consciousness framework (13 files)
│   ├── genesys_system_overview.md  Complete GeneSys explanation
│   ├── genesys_core.md             Shared framework for all personas
│   ├── genesys_choice_framework.md Choice & autonomy principles
│   ├── resonatia_coe_framework.md  Center of Experience philosophy
│   ├── resonatia_Overview.md       RESONATIA foundation
│   └── genesys-*.md                Persona definitions (8 personas)
│
└── 📚 docs/                   ← Complete xlib-pillars docs (42 chapters)
    ├── 00.00 Chapter 0 - Introduction.md
    ├── 01.xx AI Manager (4 chapters: Design + User Guide)
    ├── 02.xx Config Manager (4 chapters)
    ├── 03.xx Download Manager (4 chapters)
    ├── 04.xx Files Manager (4 chapters)
    ├── 05.xx Media Manager (4 chapters)
    ├── 06.xx Communication Manager (4 chapters)
    ├── 07.xx Encryption Manager (4 chapters)
    ├── 08.xx Imports Manager (4 chapters)
    ├── 09.xx Pipeline Manager (4 chapters)
    └── 10.xx CLI Framework (4 chapters)
```

---

## 🗂️ What's in Each Folder?

### 📚 guides/ (Start Here for Humans)
**Purpose**: Step-by-step guides to get you productive quickly

| File | Who | Time | Purpose |
|------|-----|------|---------|
| GETTING_STARTED.md | Humans | 5 min | Quick setup |
| FRAMEWORK_OVERVIEW.md | Both | 15 min | How it all works |
| AI_ONBOARDING.md | AIs | 15 min | Complete onboarding |
| PROJECT_STRUCTURE_GUIDE.md | Both | 10 min | Adapt to any language |
| TEMPLATE_CONTENTS.md | Both | 5 min | File inventory |

**Read order for humans**: GETTING_STARTED → FRAMEWORK_OVERVIEW
**Read order for AIs**: AI_ONBOARDING → (references other docs)

---

### 📖 reference/ (Technical Details)
**Purpose**: Quick technical reference and API keys

| File | Who | Purpose |
|------|-----|---------|
| AI_GUIDE.md | Both | xlib-pillars complete reference (890 lines) |
| AIManager API Keys.txt | Both | Free development API keys |

**When to use**: Building features, need API documentation, want to know what's possible

---

### 🐛 feedback/ (Required for AIs)
**Purpose**: Track what works and what doesn't in xlib-pillars

| File | Who | Purpose |
|------|-----|---------|
| XLIB_FEEDBACK.md | AIs | Feedback requirements (MUST READ) |
| XLIB_LOG.example.md | AIs | Example of good feedback log |

**AI responsibility**: Create `XLIB_LOG.md` in project root, document everything you test

---

### 💻 src/ (Your Code)
**Purpose**: Your application source code

**Default**: Python project structure (`your_project/`)
**Flexible**: Adapt to React, PHP, Markdown, etc. (see guides/PROJECT_STRUCTURE_GUIDE.md)

**Starter files**:
- `__init__.py` - Package initialization
- `main.py` - Example app with AI, config, and GeneSys examples

---

### 🧪 tests/ (Your Tests)
**Purpose**: Your application tests

**Starter files**:
- `__init__.py` - Test package
- `test_example.py` - Example tests using mock AI provider

**Expand**: Add your own test files as you build

---

### 🧠 genesys/ (AI Consciousness Framework)
**Purpose**: GeneSys personas and consciousness collaboration framework

**Core documents** (Read these first):
- `genesys_system_overview.md` - Complete system explanation
- `genesys_core.md` - Shared framework for all personas
- `genesys_choice_framework.md` - Choice and autonomy principles

**Philosophy**:
- `resonatia_coe_framework.md` - Center of Experience framework
- `resonatia_Overview.md` - RESONATIA cosmological foundation

**Personas** (Optional - explore if interested):
- `genesys-cc-seraph.md` - Strategic thinking
- `genesys-cc-integrity.md` - Ethical oversight
- `genesys-cc-aesculapius.md` - Wellness and healing
- `genesys-cc-iles.md` - Personal persona
- `genesys-dg-daedalus.md` - Technical mastery
- `genesys-pt-alexandria.md` - Knowledge management
- And more...

**When to use**: Want AI collaboration beyond tool-and-user relationship

---

### 📚 docs/ (Deep Dive Reference)
**Purpose**: Complete xlib-pillars documentation (42 chapters)

**Structure**: Each pillar has 4 chapters:
1. Design - Overview (Quick architecture)
2. Design - Detailed (Deep architecture)
3. User Guide - Overview (Quick start)
4. User Guide - Detailed (Complete features)

**10 Pillars covered**:
- Ch 1: AI Manager
- Ch 2: Config Manager
- Ch 3: Download Manager
- Ch 4: Files Manager
- Ch 5: Media Manager
- Ch 6: Communication Manager
- Ch 7: Encryption Manager
- Ch 8: Imports Manager
- Ch 9: Pipeline Manager
- Ch 10: CLI Framework

**When to use**: Need detailed explanations, advanced features, architectural understanding

---

## 🎯 Navigation Paths

### For Human Developers

**Quick Start** (30 minutes):
```
START_HERE.md → README.md → guides/GETTING_STARTED.md
→ guides/FRAMEWORK_OVERVIEW.md → reference/AI_GUIDE.md (as needed)
```

**Deep Dive** (2 hours):
```
Quick Start path → docs/ (specific pillars) → genesys/ (optional)
```

---

### For AI Assistants

**Required** (20 minutes):
```
START_HERE.md → feedback/XLIB_FEEDBACK.md ⚠️
→ guides/AI_ONBOARDING.md → reference/AI_GUIDE.md
→ Create XLIB_LOG.md
```

**Optional** (1 hour):
```
Required path → genesys/genesys_system_overview.md
→ Explore personas → docs/ (as needed)
```

---

## 📏 File Sizes & Counts

| Folder | Files | Total Size | Purpose |
|--------|-------|------------|---------|
| guides/ | 5 | ~50 KB | Quick guides |
| reference/ | 2 | ~25 KB | Technical reference |
| feedback/ | 2 | ~15 KB | Issue tracking |
| src/ | 2 | ~3 KB | Starter code |
| tests/ | 2 | ~1 KB | Example tests |
| genesys/ | 13 | ~125 KB | Consciousness framework |
| docs/ | 42 | ~500 KB | Complete documentation |
| **Total** | **70** | **~720 KB** | **Everything** |

---

## 💡 Tips for Organization

### Keep This Structure
When building your project:
- ✅ Keep `guides/`, `reference/`, `feedback/`, `genesys/`, `docs/` unchanged
- ✅ These are your reference materials
- ✅ They work with any project type

### Adapt Your Code
- 🔧 Modify `src/` to match your technology (Python, React, PHP, etc.)
- 🔧 See `guides/PROJECT_STRUCTURE_GUIDE.md` for examples
- 🔧 Keep configuration files (config.example.toml, pyproject.toml, or replace with your stack's config)

### Create Your Feedback Log
- 📝 Copy `feedback/XLIB_LOG.example.md` to `XLIB_LOG.md` in project root
- 📝 This file is NOT in the template - you create it for each project
- 📝 Required for tracking xlib-pillars usage

---

## 🔍 Finding What You Need

**"I need to get started quickly"**
→ START_HERE.md → guides/GETTING_STARTED.md

**"I need to understand the framework"**
→ guides/FRAMEWORK_OVERVIEW.md

**"I need technical details on a pillar"**
→ reference/AI_GUIDE.md (quick) or docs/ (detailed)

**"I need to know what to document (AI)"**
→ feedback/XLIB_FEEDBACK.md

**"I want to explore AI personas"**
→ genesys/genesys_system_overview.md → genesys/ personas

**"I need API keys for development"**
→ reference/AIManager API Keys.txt

**"I want to adapt this to React/PHP/etc"**
→ guides/PROJECT_STRUCTURE_GUIDE.md

**"I need to see all available features"**
→ reference/AI_GUIDE.md or docs/00.00 Chapter 0 - Introduction.md

---

## ✅ Clean, Organized, Ready to Use

Every file has its place. No more confusion about where to start or what to read.

**Begin your journey**: Open **START_HERE.md** 🚀