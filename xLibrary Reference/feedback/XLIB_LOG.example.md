# xlib-pillars Usage Log - EXAMPLE

**Project**: Video Processing Pipeline
**xlib-pillars Version**: 1.0.0
**Date Started**: 2024-01-15
**Last Updated**: 2024-01-22

---

## Pillars Used
- [x] AI - Multi-provider AI integration
- [x] Config - Configuration management
- [x] Download - YouTube video downloads
- [x] Media - Video processing and watermarking
- [ ] Files - (Not used yet)
- [ ] Communication - (Not used yet)
- [ ] Encryption - (Not used yet)
- [ ] Imports - (Not used yet)
- [ ] Pipeline - (Not used yet)
- [ ] CLI - (Not used yet)

---

## What Works ✅

### AI Manager - Basic Requests
**Feature**: `AIManager.request().send()`
**Status**: Working perfectly
**Notes**: Tested with Claude, OpenAI, and DeepSeek. All providers work consistently.
**Code Example**:
```python
from xlibrary.ai import AIManager
ai = AIManager(api_key="key", provider="claude")
response = ai.request("Analyze this video transcript").send()
# Works: Returns AIResponse with content
```
**Tested**: 2024-01-15

### AI Manager - Streaming
**Feature**: `AIManager.request_stream()`
**Status**: Working perfectly
**Notes**: Real-time streaming works great for long responses. Tested with 2000+ token responses.
**Code Example**:
```python
for chunk in ai.request_stream("Write a detailed analysis"):
    print(chunk.content, end="", flush=True)
# Works: Streams response in real-time
```
**Tested**: 2024-01-16

### Config Manager - TOML Loading
**Feature**: `ConfigManager("config.toml")`
**Status**: Working perfectly
**Notes**: Loads TOML files correctly, handles nested values with dot notation.
**Code Example**:
```python
from xlibrary.config import ConfigManager
config = ConfigManager("app.toml")
api_key = config.get("ai.api_key")
timeout = config.get("api.timeout", type=float)
# Works: Correctly loads and type-casts values
```
**Tested**: 2024-01-15

### Config Manager - Environment Variables
**Feature**: Environment variable interpolation in TOML
**Status**: Working perfectly
**Notes**: `${VAR:default}` syntax works as documented.
**Code Example**:
```toml
# In config.toml:
api_key = "${ANTHROPIC_API_KEY}"
host = "${DB_HOST:localhost}"
```
```python
config = ConfigManager("config.toml")
# Works: Correctly interpolates env vars with defaults
```
**Tested**: 2024-01-15

### Download Manager - YouTube Videos
**Feature**: `get_video()` convenience function
**Status**: Working perfectly
**Notes**: Successfully downloaded 50+ YouTube videos in various qualities.
**Code Example**:
```python
from xlibrary.download import get_video
video_path = get_video("https://youtube.com/watch?v=xyz", output_dir="~/Videos")
# Works: Downloads video successfully
```
**Tested**: 2024-01-17

### Media Manager - Video Trimming
**Feature**: `MediaManager.trim_video()`
**Status**: Working perfectly
**Notes**: Frame-accurate trimming works great. Tested with multiple timestamp formats.
**Code Example**:
```python
from xlibrary.media import MediaManager
mm = MediaManager()
result = mm.trim_video("input.mp4", start_time="1:30", end_time="3:45")
# Works: Creates accurately trimmed video
```
**Tested**: 2024-01-18

---

## What Doesn't Work ❌

### AI Manager - Streaming with File Attachments
**Feature**: `request_stream()` with attached files
**Status**: Broken
**Error**: `ValueError: Cannot stream responses with file attachments`
**Expected**: Should stream response even when files are attached
**Actual**: Raises exception immediately when `.stream()` called with attached files
**Code to Reproduce**:
```python
from xlibrary.ai import AIManager
ai = AIManager(api_key="key")
for chunk in ai.request("Analyze this").attach_file("data.csv").stream():
    print(chunk.content)
# Raises: ValueError: Cannot stream responses with file attachments
```
**Workaround**: Use non-streaming request for file attachments:
```python
response = ai.request("Analyze this").attach_file("data.csv").send()
print(response.content)
# Works but loses real-time feedback
```
**Impact**: Medium - Can work around but loses real-time progress
**Reported**: 2024-01-16

### Download Manager - Playlist Download with Config
**Feature**: Downloading playlists with custom DownloadConfig
**Status**: Broken
**Error**: `AttributeError: 'str' object has no attribute 'quality'`
**Expected**: Should use config for each playlist item
**Actual**: Config gets converted to string somewhere in processing
**Code to Reproduce**:
```python
from xlibrary.download import DownloadManager, DownloadConfig
dm = DownloadManager()
config = DownloadConfig(quality="720p", format="mp4")
task = dm.add_download("https://youtube.com/playlist?list=xyz", config=config)
dm.start_queue()
# Raises: AttributeError: 'str' object has no attribute 'quality'
```
**Workaround**: Download playlist items individually:
```python
# Get playlist URLs first (manually or with yt-dlp)
urls = ["url1", "url2", "url3"]
for url in urls:
    dm.add_download(url, config=config)
dm.start_queue()
# Works: Each video downloads with correct config
```
**Impact**: High - Significantly more code for playlists
**Reported**: 2024-01-19

### Media Manager - Watermark with Animated GIF
**Feature**: Using animated GIF as watermark
**Status**: Broken
**Error**: `RuntimeError: Animated watermarks not supported`
**Expected**: Should use first frame of GIF or animate it
**Actual**: Raises exception when GIF has multiple frames
**Code to Reproduce**:
```python
from xlibrary.media import MediaManager, WatermarkConfig
mm = MediaManager()
watermark = WatermarkConfig(watermark_path="logo.gif")
mm.watermark_video("video.mp4", watermark, "output.mp4")
# Raises: RuntimeError: Animated watermarks not supported
```
**Workaround**: Convert GIF to PNG first:
```python
from PIL import Image
img = Image.open("logo.gif")
img.seek(0)  # Get first frame
img.save("logo.png")
watermark = WatermarkConfig(watermark_path="logo.png")
mm.watermark_video("video.mp4", watermark, "output.mp4")
# Works: Uses static PNG
```
**Impact**: Low - Easy workaround
**Reported**: 2024-01-20

---

## Unclear/Needs Testing ❓

### Config Manager - Schema Validation Performance
**Feature**: Schema validation with large configs
**Status**: Uncertain
**Behavior**: Validation seems slow with configs >500 lines
**Observations**:
- Small configs (50 lines): instant validation
- Large configs (500+ lines): 2-3 second delay
- Not sure if this is expected or a performance issue
**Questions**:
- Is schema validation supposed to be this slow?
- Is there a way to cache validation results?
**Needs**: Performance testing with various config sizes
**Tested**: 2024-01-21

### Download Manager - Concurrent Download Limits
**Feature**: `max_concurrent` parameter
**Status**: Uncertain
**Behavior**: Setting `max_concurrent=10` seems to only use 5 threads
**Observations**:
- Set to 10, observe 5 active downloads
- Set to 20, observe 5 active downloads
- Not sure if there's a hard limit somewhere
**Questions**:
- Is there a maximum concurrent download limit?
- Does it depend on the download source?
**Needs**: Testing with various concurrent limits
**Tested**: 2024-01-22

---

## Workarounds Created 🔧

### Workaround: Streaming Progress for File Analysis
**Problem**: Can't stream AI responses when files are attached
**Workaround**:
```python
# Show "processing" message while waiting
import threading
import time

def show_progress():
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    idx = 0
    while processing:
        print(f"\r{chars[idx % len(chars)]} Processing file...", end="", flush=True)
        time.sleep(0.1)
        idx += 1

processing = True
progress_thread = threading.Thread(target=show_progress, daemon=True)
progress_thread.start()

response = ai.request("Analyze").attach_file("large_file.csv").send()

processing = False
print("\r✅ Analysis complete!                ")
print(response.content)
```
**Notes**: Gives user feedback without actual streaming
**When to use**: File attachments that take >5 seconds to process
**Created**: 2024-01-16

### Workaround: Batch Video Processing with Progress
**Problem**: Media processing doesn't show progress for batch operations
**Workaround**:
```python
from xlibrary.media import MediaManager
mm = MediaManager()

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]
total = len(videos)

for idx, video in enumerate(videos, 1):
    print(f"[{idx}/{total}] Processing {video}...")
    result = mm.trim_video(video, start_time="0:30", end_time="2:00")
    print(f"✅ Completed: {result.output_path}")

print(f"\n✅ All {total} videos processed!")
```
**Notes**: Manual progress tracking for batch operations
**When to use**: Processing multiple videos/images
**Created**: 2024-01-18

### Workaround: Retry Failed Downloads
**Problem**: No automatic retry for failed downloads
**Workaround**:
```python
from xlibrary.download import get_video, DownloadError
import time

def download_with_retry(url, max_retries=3, delay=5):
    """Download with automatic retry on failure"""
    for attempt in range(max_retries):
        try:
            return get_video(url)
        except DownloadError as e:
            if attempt < max_retries - 1:
                print(f"Retry {attempt + 1}/{max_retries} after {delay}s...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise
    return None

# Usage
video = download_with_retry("https://youtube.com/watch?v=xyz", max_retries=5)
```
**Notes**: Implements exponential backoff for retries
**When to use**: Unstable network or flaky sources
**Created**: 2024-01-19

---

## Performance Notes 📊

### AI Manager Response Times
- **Claude Sonnet**: ~2-3 seconds for simple requests, ~15-30s for complex analysis
- **OpenAI GPT-4**: ~3-5 seconds for simple requests, ~20-40s for complex analysis
- **Streaming**: Starts in <1 second, chunks arrive every 0.1-0.3 seconds
- **With files**: +5-10 seconds for file processing before response starts

### Download Manager Throughput
- **Single YouTube video (720p)**: ~30 seconds for 10-minute video
- **Concurrent (3 videos)**: All complete in ~45 seconds total
- **Large files (1GB+)**: Speed depends on network, usually 5-10 MB/s

### Media Manager Processing Times
- **Video trimming (5-minute 1080p)**: ~15 seconds
- **Watermarking (5-minute 1080p)**: ~60 seconds
- **Batch watermarking (10 videos)**: ~10 minutes total
- **Memory usage**: ~500MB for typical video processing

### Config Manager
- **Small configs (<100 lines)**: <10ms load time
- **Large configs (500+ lines)**: ~2-3 seconds with schema validation
- **Without validation**: Always <50ms regardless of size

---

## Suggestions for Library Improvement 💡

1. **AI Manager: Add retry parameter**
   ```python
   ai = AIManager(api_key="key", auto_retry=True, max_retries=3)
   # Would handle transient failures automatically
   ```

2. **AI Manager: Support streaming with files**
   - Currently broken (see "What Doesn't Work")
   - Would greatly improve UX for long file analysis

3. **Config Manager: Add validation caching**
   - Cache validation results based on file hash
   - Would speed up large config loading

4. **Download Manager: Add progress callbacks**
   ```python
   def on_progress(task_id, percent, speed, eta):
       print(f"{percent}% - {speed} - ETA: {eta}")

   dm.set_progress_callback(on_progress)
   ```

5. **Download Manager: Support playlist configs**
   - Fix bug where DownloadConfig doesn't work with playlists
   - High priority - major pain point

6. **Media Manager: Add batch processing with progress**
   ```python
   results = mm.batch_watermark(
       videos=["v1.mp4", "v2.mp4"],
       watermark=config,
       progress_callback=lambda current, total: print(f"{current}/{total}")
   )
   ```

7. **All Managers: Add dry-run mode**
   ```python
   mm = MediaManager(dry_run=True)
   result = mm.trim_video(...)  # Shows what would happen, doesn't execute
   ```

8. **All Managers: Better error messages**
   - Include suggestions for common errors
   - Include links to documentation
   - Include example code for fixes

9. **Add logging utilities**
   ```python
   from xlibrary.utils import setup_logging
   setup_logging(level="DEBUG", file="app.log")
   # Would make debugging much easier
   ```

10. **Documentation: Add more real-world examples**
    - Current docs are good but more complete examples would help
    - Especially for combining multiple pillars
    - Video processing + AI analysis workflow examples

---

## Summary Statistics

- **Total Features Tested**: 15
- **Working Perfectly**: 6 (40%)
- **Has Issues**: 3 (20%)
- **Unclear/Needs Testing**: 2 (13%)
- **Workarounds Created**: 3
- **Days of Active Use**: 7
- **Overall Experience**: Positive - issues are manageable with workarounds

---

## Final Notes

**Overall Assessment**: xlib-pillars is a solid foundation despite being a work in progress. The issues we've encountered have workable solutions, and the library's modular design makes it easy to work around problems in one pillar without affecting others.

**Would Recommend**: Yes, especially for rapid prototyping. The AI abstraction layer alone is worth using the library.

**Main Pain Points**:
1. Streaming with file attachments (blocked, waiting for fix)
2. Playlist downloads with custom config (workaround exists but tedious)
3. Documentation could use more complete examples

**Best Parts**:
1. Consistent API across all pillars
2. Excellent error messages (most of the time)
3. Mock provider for testing
4. Good TypeScript-style type hints
5. Fast development iteration

---

**Last Updated**: 2024-01-22
**Next Review**: 2024-01-29