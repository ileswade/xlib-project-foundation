# xlib-pillars AI Guide

## Quick Reference
- **Package name**: `xlib-pillars`
- **Install**: `pip install xlib-pillars[ai]` (or `[all]` for everything)
- **Import**: `from xlibrary import AIManager` (import name stays `xlibrary`)
- **Repository**: https://github.com/ileswade/xlibrary
- **Python**: >=3.8

## Overview

xlib-pillars is a modular Python library ecosystem built on a pillar architecture. Each pillar is independently installable with its own dependencies, providing specialized functionality without bloating your project. Install only what you need.

**Core Philosophy**: No hidden dependencies, explicit configuration, production-ready defaults, and framework-agnostic design.

## Installation

### Basic Installation
```bash
# Core library (minimal dependencies)
pip install xlib-pillars

# Single pillar
pip install xlib-pillars[ai]
pip install xlib-pillars[config]
pip install xlib-pillars[download]

# Multiple pillars
pip install xlib-pillars[ai,config,download]

# Everything
pip install xlib-pillars[all]
```

### Individual Provider Installation
```bash
# AI providers
pip install xlib-pillars[claude]    # Anthropic Claude only
pip install xlib-pillars[openai]    # OpenAI only
pip install xlib-pillars[deepseek]  # DeepSeek only
```

### Development Installation
```bash
pip install xlib-pillars[dev]  # Development tools
```

---

## Core Pillars

### AI - Multi-Provider AI Abstraction
**Purpose**: Unified interface for Claude, OpenAI, DeepSeek with conversation management
**Install**: `pip install xlib-pillars[ai]`
**Key Classes**: `AIManager`, `AIResponse`, `AIConfig`

**Quick Start**
```python
from xlibrary.ai import AIManager

# Minimal setup (requires explicit API key)
ai = AIManager(api_key="your-api-key")

# Make request with method chaining
response = ai.request("Explain Python decorators").send()
print(response.content)

# Stateful conversation
conversation = ai.start_conversation()
response1 = conversation.request("What is Python?").send()
response2 = conversation.request("Give me an example").send()  # Has context

# Streaming response
for chunk in ai.request_stream("Write a story"):
    print(chunk.content, end="", flush=True)
```

**Common Patterns**
```python
# Provider switching
claude = AIManager(api_key="key", provider="claude", model="current")
openai = AIManager(api_key="key", provider="openai", model="current")
deepseek = AIManager(api_key="key", provider="deepseek", model="current")

# Universal model aliases (work across all providers)
ai_latest = AIManager(api_key="key", model="latest")      # Flagship
ai_current = AIManager(api_key="key", model="current")    # High-performance
ai_fast = AIManager(api_key="key", model="fast")          # Speed-optimized
ai_reasoning = AIManager(api_key="key", model="reasoning") # Thinking-capable

# File attachments with vision models
response = ai.request("What's in this image?") \
    .attach_file("image.jpg") \
    .with_temperature(0.7) \
    .send()

# Testing with mock provider
test_ai = AIManager(provider="mock", model="latest")  # No API key needed
```

**Important Notes**
- API keys must be provided explicitly (no environment variable fallbacks)
- Default provider is Claude with latest model
- Method chaining supported for complex requests
- All providers use identical interface

---

### Config - TOML Configuration Management
**Purpose**: Type-safe configuration with environment variables and encryption
**Install**: `pip install xlib-pillars[config]`
**Key Classes**: `ConfigManager`, `Schema`

**Quick Start**
```python
from xlibrary.config import ConfigManager

# app.toml
# app_name = "My App"
# [database]
# host = "${DB_HOST:localhost}"
# port = 5432

config = ConfigManager("app.toml")
app_name = config.get("app_name")
db_host = config.get("database.host")
db_port = config.get("database.port", type=int)
```

**Common Patterns**
```python
# Environment variable interpolation
config = ConfigManager("config.toml")
# In TOML: host = "${DB_HOST:localhost}"  # Default to localhost
print(config.get("database.host"))  # Uses env var or default

# Hierarchical configs (later files override earlier)
config = ConfigManager([
    "base.toml",      # Base config
    "prod.toml",      # Production overrides
    "local.toml"      # Local overrides (optional)
])

# Schema validation
from xlibrary.config import Schema, required, optional, range_check

schema = Schema({
    "database": {
        "host": required(str),
        "port": required(int) | range_check(1, 65535),
        "timeout": optional(float, default=30.0)
    }
})
config = ConfigManager("app.toml", schema=schema)

# Encrypted values
# In TOML: password = "encrypted:FERNET:gAAAAABhZ2I..."
config = ConfigManager("app.toml", encryption_key=os.getenv('ENCRYPTION_KEY'))
password = config.get("database.password")  # Automatically decrypted
```

**Important Notes**
- Dot notation for nested values
- Type-safe access with `type=` parameter
- Supports TOML, environment variables, and encryption
- Auto-reload available with `auto_reload=True`

---

### Download - YouTube & Web Content Downloader
**Purpose**: Download videos, audio, transcripts from YouTube, social media, and web
**Install**: `pip install xlib-pillars[download]`
**Key Classes**: `DownloadManager`, `DownloadConfig`

**Quick Start**
```python
from xlibrary.download import get_video, get_audio, get_transcript, DownloadManager

# Simple convenience functions
video = get_video("https://youtube.com/watch?v=xyz")
audio = get_audio("https://youtube.com/watch?v=xyz", output_dir="~/Music")
transcript = get_transcript("https://youtube.com/watch?v=xyz", languages=["en"])

# Enterprise queue system
dm = DownloadManager(default_output_dir="~/Downloads", max_concurrent=3)
task_id = dm.add_download("https://vimeo.com/123456789")
dm.start_queue()
```

**Common Patterns**
```python
# Advanced configuration
from xlibrary.download import DownloadConfig

video_config = DownloadConfig(
    quality="720p",
    format="mp4",
    embed_subtitles=True,
    embed_metadata=True
)

audio_config = DownloadConfig(
    audio_only=True,
    quality="320k",
    format="mp3"
)

# Transcript-only downloads (no video/audio)
transcript = get_transcript(
    "https://youtube.com/watch?v=xyz",
    languages=["en", "es"],  # Fallback order
    output_dir="~/Transcripts"
)

# Batch downloads
urls = ["url1", "url2", "url3"]
dm = DownloadManager(max_concurrent=3)
for url in urls:
    dm.add_download(url, config=audio_config)
dm.start_queue()
dm.wait_for_completion()

# Progress tracking
def progress_callback(task_id, progress):
    print(f"{task_id}: {progress.percent:.1f}% - {progress.download_speed}")

dm.set_progress_callback(progress_callback)
```

**Important Notes**
- Requires yt-dlp for YouTube downloads
- Supports YouTube, Vimeo, Instagram, TikTok, Twitter, and more
- Mac-optimized formats available
- Progress callbacks for long downloads

---

### Files - File Organization & Management
**Purpose**: File type detection, deduplication, organization, compression
**Install**: `pip install xlib-pillars[files]`
**Key Classes**: `FileManager`

**Quick Start**
```python
from xlibrary.files import FileManager

fm = FileManager()

# Detect file type
file_info = fm.detect_file_type("document.pdf")
print(f"Type: {file_info.file_type}, Size: {file_info.size}")

# Organize messy folder by type
result = fm.organize_by_file_type("/messy/downloads")
print(f"Organized {result.files_processed} files")

# Find and remove duplicates
duplicates = fm.find_duplicates("/photos")
fm.remove_duplicates(duplicates, keep='newest')

# Compress folder
fm.compress_folder("/source/folder", "/archive.zip")
```

**Common Patterns**
```python
# Type detection with security check
file_info = fm.detect_file_type("suspicious.exe")
if file_info.is_type_mismatch:
    print(f"Warning: Claims to be {file_info.declared_type}, actually {file_info.actual_type}")

# Custom organization rules
def organize_by_date(file_info):
    year = file_info.modified_time.year
    file_type = file_info.file_type.value.title()
    return f"{year}/{file_type}"

fm.organize_by_rule("/photos", organize_by_date)

# Duplicate detection and removal
duplicates = fm.find_duplicates("/photos", methods=['hash'])
for group in duplicates:
    print(f"Found {len(group.files)} duplicates, wasting {group.wasted_space} bytes")

removed = fm.remove_duplicates(duplicates, keep='newest')
print(f"Freed {removed.space_recovered} bytes")

# Compression with progress
def progress(current, total, message):
    print(f"{(current/total)*100:.1f}% - {message}")

fm.compress_folder("large_folder", "archive.tar.gz",
                   format="tar.gz", progress_callback=progress)
```

**Important Notes**
- Requires python-magic for accurate type detection
- Windows: python-magic-bin auto-installed
- Dry run mode available for safe operations
- Supports hash-based and fuzzy duplicate detection

---

### Media - Video & Image Processing
**Purpose**: Video trimming, watermarking, thumbnails, format conversion
**Install**: `pip install xlib-pillars[media]`
**Key Classes**: `MediaManager`, `WatermarkConfig`

**Quick Start**
```python
from xlibrary.media import MediaManager, WatermarkConfig, WatermarkPosition

mm = MediaManager()

# Video trimming with flexible timestamps
result = mm.trim_video(
    "input.mp4",
    start_time="2:30.5",      # 2 minutes 30.5 seconds
    end_time="f5400",         # Frame 5400
    output_path="trimmed.mp4"
)

# Smart watermarking (auto-scales to any resolution)
watermark = WatermarkConfig(
    watermark_path="logo.png",
    position=WatermarkPosition.BOTTOM_RIGHT,
    auto_scale=True,
    opacity=0.8
)
mm.watermark_video("video.mp4", watermark, "branded.mp4")

# Extract thumbnails
thumbnails = mm.extract_thumbnails(
    "video.mp4",
    times=["0:30", "2:15.5", "f7200"],
    output_dir="thumbnails/"
)
```

**Common Patterns**
```python
# Flexible timestamp formats (all work)
formats = [
    "2:30.5",           # Minutes:seconds.ms
    "01:23:45.678",     # Hours:minutes:seconds.ms
    "f5400",            # Frame number
    "150.75",           # Decimal seconds
    "01:23:45:12",      # SMPTE timecode
    "123456ms"          # Milliseconds
]

# Master watermark (one logo for all resolutions)
watermark = WatermarkConfig(
    watermark_path="4K_logo.png",  # High-res master
    position=WatermarkPosition.BOTTOM_RIGHT,
    max_width_percent=0.20,  # 20% of video width
    auto_scale=True  # Adapts automatically
)

# Works on 720p, 1080p, 4K without changes
for video in ["video_720p.mp4", "video_1080p.mp4", "video_4K.mp4"]:
    mm.watermark_video(video, watermark, f"branded_{video}")

# Animated watermarks
animated_watermark = WatermarkConfig(
    watermark_path="logo.png",
    position=WatermarkPosition.CENTER,
    animation=WatermarkAnimation.FADE_IN_OUT,
    animation_duration=5.0,
    opacity=0.9
)

# Batch processing
videos = ["v1.mp4", "v2.mp4", "v3.mp4"]
results = mm.batch_watermark(
    videos, watermark, "output/",
    progress_callback=lambda c, t, f: print(f"{c}/{t}: {f}")
)
```

**Important Notes**
- Requires FFmpeg installed on system
- Frame-accurate trimming with `f` prefix
- Watermarks auto-scale across resolutions
- Supports animated watermarks (fade, pulse, scroll)

---

### Communication - Email & Messaging
**Purpose**: Gmail integration, multi-channel messaging, email automation
**Install**: `pip install xlib-pillars[communication]`
**Key Classes**: `CommManager`, `EmailQuery`

**Quick Start**
```python
from xlibrary.communication import CommManager, EmailQuery

comm = CommManager()
gmail = comm.gmail(credentials_path="gmail_credentials.json")

# Send email
message = gmail.compose()
message.to("recipient@example.com")
message.subject("Hello")
message.body("This is a test message")
result = message.send()

# Search emails
messages = gmail.search(
    EmailQuery()
    .from_sender("boss@company.com")
    .is_unread()
    .limit(10)
)

for msg in messages:
    print(f"From: {msg.sender}, Subject: {msg.subject}")
    if msg.has_attachments():
        msg.download_attachments("downloads/")
```

**Common Patterns**
```python
# Advanced email search
query = (EmailQuery()
    .from_sender("client@company.com")
    .subject_contains("invoice")
    .has_attachment()
    .date_range("2024-01-01", "2024-12-31")
    .is_unread()
    .sort_by("date", SortOrder.DESC)
    .limit(50)
)
messages = gmail.search(query)

# Rich HTML email with attachments
rich_message = gmail.compose()
rich_message.to(["team@company.com", "manager@company.com"])
rich_message.cc("hr@company.com")
rich_message.subject("Q4 Report")
rich_message.html_body("<h2>Report</h2><p>Please review...</p>")
rich_message.attach("report.pdf")
rich_message.attach("charts.xlsx")
rich_message.send()

# Automated email processing
automation = EmailAutomationManager()

# Forward invoices to accounting
automation.add_processing_rule(
    condition={'type': 'sender', 'value': 'billing@vendor.com'},
    action={'type': 'forward', 'to': 'accounting@company.com'}
)

# Label urgent messages
automation.add_processing_rule(
    condition={'type': 'subject_contains', 'value': 'urgent'},
    action={'type': 'add_label', 'label': 'Priority'}
)

automation.process_inbox()
```

**Important Notes**
- Requires Gmail API credentials (OAuth2)
- Supports batch operations for efficiency
- Rate limiting built-in
- Email attachments limited to 25MB (Gmail)

---

### Encryption - Secure Encryption & Signatures
**Purpose**: File/string encryption, digital signatures, password hashing
**Install**: `pip install xlib-pillars[encryption]`
**Key Classes**: `EncryptionManager`, `SymmetricAlgorithm`

**Quick Start**
```python
from xlibrary.encryption import EncryptionManager

em = EncryptionManager()

# String encryption (AES-256-GCM by default)
encrypted = em.encrypt_string("confidential data", "password")
decrypted = em.decrypt_string(encrypted, "password")

# File encryption
em.encrypt_file("document.pdf", "document.enc", password="secret")
em.decrypt_file("document.enc", "decrypted.pdf", password="secret")

# Digital signatures
key_pair = em.generate_key_pair("rsa_2048", "signing_key")
signature = em.sign_data("important document", "signing_key")
is_valid = em.verify_signature("important document", signature, "signing_key")

# Secure password hashing (Argon2)
password_hash = em.hash_password("user_password")
is_correct = em.verify_password("user_password", password_hash)
```

**Common Patterns**
```python
# Advanced encryption with algorithm selection
from xlibrary.encryption import SymmetricAlgorithm

encrypted = em.encrypt_string(
    "api_key",
    password="master_password",
    algorithm=SymmetricAlgorithm.CHACHA20_POLY1305,
    additional_data="api_context"
)

# File encryption with compression
result = em.encrypt_file(
    "large_database.sql",
    "database.enc",
    password="db_key",
    compress_before_encrypt=True,
    verify_integrity=True,
    progress_callback=lambda c, t, f: print(f"{(c/t)*100:.1f}%")
)

# Digital signatures for documents
contract = "Contract text..."
signature = em.sign_data(contract, "company_signing_key")
is_valid = em.verify_signature(contract, signature, "company_signing_key")

# Export public key for sharing
public_key = em.export_public_key("company_signing_key", format="pem")

# Key management
master_key = em.generate_master_key("db_master", SymmetricAlgorithm.AES_256_GCM)
derived_key = em.derive_key("db_master", "users_table_encryption")
```

**Important Notes**
- Uses cryptography library (modern, secure)
- Default AES-256-GCM for symmetric encryption
- Argon2id for password hashing
- RSA/ECDSA for signatures

---

### Imports - Dependency Management
**Purpose**: Smart import management, security scanning, dependency resolution
**Install**: `pip install xlib-pillars[imports]`
**Key Classes**: `ImportManager`

**Quick Start**
```python
from xlibrary.imports import ImportManager

im = ImportManager()

# Smart import - installs if missing
pandas = im.smart_import("pandas", min_version="1.5.0")
df = pandas.DataFrame({"a": [1, 2, 3]})

# Secure installation with scanning
result = im.install_package_secure(
    "requests>=2.28.0",
    scan_vulnerabilities=True,
    check_licenses=True
)

# Auto-discover missing imports
discovery = im.get_discovery_manager()
missing = discovery.discover_missing_imports("./src")
requirements = discovery.auto_generate_requirements("./project")
```

**Common Patterns**
```python
# Lazy imports (load only when accessed)
numpy_lazy = im.lazy_import("numpy")
pandas_lazy = im.lazy_import("pandas", ["DataFrame"])
# Modules not loaded until used
arr = numpy_lazy.array([1, 2, 3])  # Now numpy loads

# Dependency resolution
requirements = ["django>=4.0", "djangorestframework>=3.14", "celery>=5.2"]
resolver = im.get_resolver()
resolution = resolver.resolve_dependencies(
    requirements,
    strategy="conservative"
)

if resolution.success:
    for package in resolution.install_order:
        print(f"Install {package.name}=={package.version}")

# Security scanning
scan_result = im.security_scan("requests==2.28.0")
print(f"Security score: {scan_result.security_score}/10")
print(f"Vulnerabilities: {len(scan_result.vulnerabilities)}")

# CI/CD integration
security_report = im.security_scan_all()
if security_report.critical_vulnerabilities:
    print("CRITICAL: Security vulnerabilities found!")
    sys.exit(1)
```

**Important Notes**
- Lazy loading improves startup time
- Security scanning uses multiple databases
- Supports private/corporate registries
- Lock file generation for reproducible builds

---

### Pipeline - Data Pipeline Orchestration
**Purpose**: ETL pipelines, task orchestration, distributed processing
**Install**: `pip install xlib-pillars[pipeline]`
**Key Classes**: `PipelineManager`, `Pipeline`, `Task`

**Quick Start**
```python
from xlibrary.pipeline import PipelineManager, Pipeline

pm = PipelineManager()
data_pipeline = Pipeline("data_processing")

@data_pipeline.task("extract")
def extract_data():
    return {"data": [1, 2, 3, 4, 5]}

@data_pipeline.task("transform", depends_on=["extract"])
def transform_data(extract_result):
    data = extract_result["data"]
    return {"transformed": [x * 2 for x in data]}

@data_pipeline.task("load", depends_on=["transform"])
def load_data(transform_result):
    print(f"Loading: {transform_result['transformed']}")
    return {"status": "loaded"}

result = pm.execute_pipeline(data_pipeline)
print(f"Success: {result.success}")
```

**Common Patterns**
```python
# Parallel task execution
ml_pipeline = Pipeline("ml_training")

@ml_pipeline.task("prepare_data")
def prepare_data():
    return {"features": [[1,2], [3,4]], "labels": [0, 1]}

# These run in parallel
@ml_pipeline.task("train_model_a", depends_on=["prepare_data"])
def train_rf(data):
    return {"model": "rf", "accuracy": 0.85}

@ml_pipeline.task("train_model_b", depends_on=["prepare_data"])
def train_svm(data):
    return {"model": "svm", "accuracy": 0.82}

@ml_pipeline.task("select_best", depends_on=["train_model_a", "train_model_b"])
def select_best(model_a, model_b):
    return max([model_a, model_b], key=lambda x: x["accuracy"])

result = pm.execute_pipeline(ml_pipeline, parallel=True)

# Distributed execution
distributed_pm = PipelineManager({
    "cluster_mode": "kubernetes",
    "worker_nodes": 3
})
result = distributed_pm.execute_distributed(big_data_pipeline)

# Monitoring and metrics
pm.enable_monitoring(
    metrics=["execution_time", "memory_usage"],
    alerts=["task_failure"]
)
performance = pm.get_performance_report(pipeline.name)
```

**Important Notes**
- Tasks define dependencies with `depends_on`
- Parallel execution when dependencies allow
- Supports distributed clusters (Kubernetes)
- Built-in retry logic and error handling

---

### CLI - Command-Line Framework
**Purpose**: Build professional CLI tools with rich output
**Install**: `pip install xlib-pillars[cli]`
**Key Classes**: `CLIFramework`

**Quick Start**
```python
from xlibrary.cli import CLIFramework

cli = CLIFramework(name="myapp", version="1.0.0")

@cli.command()
def hello(name: str = "World"):
    """Say hello to someone."""
    cli.console.print(f"Hello, {name}!", style="green")

@cli.command()
def status():
    """Show system status."""
    cli.console.print("[bold green]✓[/] System Online")
    cli.console.print("[yellow]![/] 3 warnings")
    cli.console.print("[red]✗[/] Database offline")

if __name__ == "__main__":
    cli.run()
```

**Common Patterns**
```python
# Commands with options
@cli.command()
def deploy(
    environment: str,
    dry_run: bool = False,
    verbose: bool = False
):
    """Deploy to environment."""
    if dry_run:
        cli.console.print("[yellow]Dry run mode[/]")
    cli.console.print(f"Deploying to {environment}...")

# Interactive workflows
@cli.command()
def setup():
    """Interactive setup."""
    name = cli.prompt("Enter your name")
    email = cli.prompt("Email", default="user@example.com")
    password = cli.prompt("Password", password=True)

    if cli.confirm("Save configuration?"):
        cli.console.print("[green]Saved![/]")

# Selection menus
deployment = cli.select(
    "Choose target:",
    choices=["development", "staging", "production"]
)

# Progress bars
with cli.progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for i in range(100):
        time.sleep(0.01)
        progress.update(task, advance=1)

# Command groups
@cli.group()
def database():
    """Database operations."""
    pass

@database.command()
def migrate():
    """Run migrations."""
    pass
```

**Important Notes**
- Built on Click and Rich libraries
- Automatic help generation
- Rich terminal output (colors, tables, progress)
- Type-safe command arguments

---

## Best Practices

### Installation
- Install only pillars you need to minimize dependencies
- Use virtual environments for project isolation
- Pin versions in production (`xlib-pillars[ai]==1.0.0`)

### Configuration
- Always provide explicit API keys (no env fallbacks)
- Use schema validation for config files
- Store encrypted values for sensitive data
- Use type-safe config access (`type=int`)

### Error Handling
```python
# Always handle provider-specific errors
from xlibrary.ai import AIManager, MissingCredentialsError, ProviderError

try:
    ai = AIManager(api_key="key")
    response = ai.request("Hello").send()
except MissingCredentialsError as e:
    print(f"Setup needed: {e.solution}")
except ProviderError as e:
    print(f"Provider issue: {e}")
```

### Resource Management
```python
# Reuse manager instances
ai = AIManager(api_key="key")
for question in questions:
    response = ai.request(question).send()  # Reuses connection

# Don't create new instances in loops (inefficient)
```

### Testing
```python
# Use mock providers for testing
test_ai = AIManager(provider="mock", model="latest")
response = test_ai.request("Test").send()
assert response.content  # Predictable mock response
```

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Install the pillar you're trying to use
pip install xlib-pillars[ai]  # For AI functionality
pip install xlib-pillars[all]  # For everything
```

**API Authentication Failures**
```python
# AI: Provide API key explicitly
ai = AIManager(api_key="your-actual-key")

# Gmail: Check credentials file exists
gmail = comm.gmail(credentials_path="gmail_credentials.json")
```

**Missing Dependencies**
```bash
# Files pillar on macOS/Linux
pip install python-magic

# Media pillar
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux

# Download pillar
pip install yt-dlp
```

**Configuration Not Found**
```python
# Use absolute paths or check current directory
from pathlib import Path
config_path = Path("config.toml").absolute()
config = ConfigManager(str(config_path))
```

**Performance Issues**
```python
# Enable caching for heavy operations
pm = PipelineManager({"caching": {"enabled": True}})

# Use lazy imports for faster startup
numpy_lazy = im.lazy_import("numpy")
```

### Getting Help
- Check method signatures: Most methods have detailed docstrings
- Use type hints: All public APIs are fully typed
- Enable debug mode: Many managers support `debug=True` parameter
- Review examples: Each pillar has comprehensive usage examples above

## Version Compatibility

- Python: 3.8, 3.9, 3.10, 3.11, 3.12
- All pillars are independently versioned
- Core library has minimal dependencies
- Optional dependencies only loaded when pillars installed

## Migration Notes

If migrating from `xlibrary` to `xlib-pillars`:
- Package name changed: `pip install xlib-pillars`
- Import name unchanged: `from xlibrary import AIManager`
- All APIs remain backward compatible
- New features: explicit API keys, improved error messages

---

**This guide provides everything needed to integrate xlib-pillars into AI-powered applications. All examples are production-ready and follow best practices.**