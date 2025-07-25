# MCP YouTube Extract

[![PyPI version](https://badge.fury.io/py/mcp-youtube-extract.svg)](https://badge.fury.io/py/mcp-youtube-extract)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Model Context Protocol (MCP) server for YouTube operations, demonstrating core MCP concepts including tools and logging.

## Features

- **MCP Server**: A fully functional MCP server with:
  - **Tools**: Extract information from YouTube videos including metadata and transcripts
  - **Comprehensive Logging**: Detailed logging throughout the application
  - **Error Handling**: Robust error handling with fallback logic for transcripts
  - **Multiple Transports**: Supports both stdio and SSE (Server-Sent Events) protocols
- **YouTube Integration**: Built-in YouTube API capabilities:
  - Extract video information (title, description, channel, publish date)
  - Get video transcripts with intelligent fallback logic
  - Support for both manually created and auto-generated transcripts

## 📦 Available on PyPI

This package is now available on PyPI! You can install it directly with:

```bash
pip install mcp-youtube-extract
```

Visit the package page: [mcp-youtube-extract on PyPI](https://pypi.org/project/mcp-youtube-extract/)

## Installation

### Quick Start (Recommended)

The easiest way to get started is to install from PyPI:

```bash
pip install mcp-youtube-extract
```

Or using pipx (recommended for command-line tools):

```bash
pipx install mcp-youtube-extract
```

This will install the latest version with all dependencies. You can then run the MCP server directly:

```bash
mcp_youtube_extract
```

### Using uv (Development)

For development or if you prefer uv:

#### Installing uv

**On Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**

uv is written in Rust, so you'll need the Rust toolchain first.

1. **Install Rust (Recommended Method)**
   1. Visit this link or copy and paste it into your browser:
      👉 https://win.rustup.rs/
   2. The **installer (rustup-init.exe)** will download automatically
   3. Run the installer and proceed with default options:
      - This installs `cargo`, `rustc`, `rustup`, `rustdoc`, etc.
      - After installation, `C:\Users\[username]\.cargo\bin` is automatically added to PATH

2. **Install uv from GitHub (Direct Method)**

   After Rust is installed, install uv with this command:
   ```powershell
   cargo install --git https://github.com/astral-sh/uv uv
   ```
   This command fetches and builds the latest version of uv directly from the GitHub repository.

#### Setting up the project

Once uv is installed:

```bash
# Clone and install the project
git clone https://github.com/hwang2006/mcp_youtube_extract.git
cd mcp_youtube_extract

# Install dependencies (including dev dependencies)
uv sync --dev

# Set up your API key for development
cp .env.example .env
# Edit .env and add your YouTube API key
```

### From source

1. Clone the repository:
   ```bash
   git clone https://github.com/hwang2006/mcp_youtube_extract.git
   cd mcp_youtube_extract
   ```

2. Install in development mode:
   ```bash
   uv sync --dev
   ```

## Configuration

### Environment Variables

For **development**, create a `.env` file in the project root with your YouTube API key:

```bash
# YouTube API Configuration
YOUTUBE_API_KEY=your_youtube_api_key_here
```

For **production**, set the environment variable directly in your system:

```bash
export YOUTUBE_API_KEY=your_youtube_api_key_here
```

**Required:**
- `YOUTUBE_API_KEY`: Your YouTube Data API key (required for video metadata)

### Getting Your YouTube API Key

To use this MCP server, you'll need a YouTube Data API key. Here's how to get one:

#### Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" at the top of the page
3. Click "New Project" and give it a name (e.g., "MCP YouTube Extract")
4. Click "Create"

#### Step 2: Enable the YouTube Data API

1. In your new project, go to the [API Library](https://console.cloud.google.com/apis/library)
2. Search for "YouTube Data API v3"
3. Click on it and then click "Enable"

#### Step 3: Create API Credentials

1. Go to the [Credentials page](https://console.cloud.google.com/apis/credentials)
2. Click "Create Credentials" and select "API Key"
3. Your new API key will be displayed - copy it immediately
4. Click "Restrict Key" to secure it (recommended)

#### Step 4: Restrict Your API Key (Recommended)

1. In the API key settings, click "Restrict Key"
2. Under "API restrictions", select "Restrict key"
3. Choose "YouTube Data API v3" from the dropdown
4. Click "Save"

#### Step 5: Set Up Billing (Required)

1. Go to the [Billing page](https://console.cloud.google.com/billing)
2. Link a billing account to your project
3. **Note**: YouTube Data API has a free tier of 10,000 units per day, which is typically sufficient for most use cases

#### API Key Usage Limits

- **Free Tier**: 10,000 units per day
- **Cost**: $5 per 1,000 units after free tier
- **Typical Usage**:
  - Getting video info: ~1 unit per request
  - Getting transcripts: ~1 unit per request
  - Most users stay well within the free tier

#### Security Best Practices

- **Never commit your API key** to version control
- **Use environment variables** as shown in the configuration section
- **Restrict your API key** to only the YouTube Data API
- **Monitor usage** in the Google Cloud Console

## Usage

### Running the MCP Server

#### Using PyPI Installation (Recommended)

```bash
# Install from PyPI
pip install mcp-youtube-extract

# Run the server
mcp_youtube_extract
```

#### Using Development Setup

```bash
# Using uv
cd mcp_youtube_extract
uv run mcp_youtube_extract

# Or directly
python -m mcp_youtube_extract.server
```

### Direct Function Call (Quick Testing)

For quick testing or one-off extractions, you can call the YouTube extraction function directly using Python's `-c` flag:

#### Basic Usage

```bash
# Extract Rick Astley video (Never Gonna Give You Up)
cd mcp_youtube_extract
uv run python -c "from dotenv import load_dotenv; load_dotenv(); from src.mcp_youtube_extract.server import get_yt_video_info; print(get_yt_video_info('dQw4w9WgXcQ'))"
```

#### With Error Handling

```bash
uv run python -c "
try:
    from dotenv import load_dotenv
    load_dotenv()
    from src.mcp_youtube_extract.server import get_yt_video_info
    result = get_yt_video_info('dQw4w9WgXcQ')
    print(result)
except Exception as e:
    print(f'Error: {e}')
"
```

#### Save Output to File

```bash
uv run python -c "
from dotenv import load_dotenv
load_dotenv()
from src.mcp_youtube_extract.server import get_yt_video_info
result = get_yt_video_info('dQw4w9WgXcQ')
with open('video_info.txt', 'w', encoding='utf-8') as f:
    f.write(result)
print('Video information saved to video_info.txt')
"
```

#### Extract Multiple Videos

```bash
uv run python -c "
from dotenv import load_dotenv
load_dotenv()
from src.mcp_youtube_extract.server import get_yt_video_info

videos = ['dQw4w9WgXcQ', 'jNQXAC9IVRw', '9bZkp7q19f0']
for video_id in videos:
    print(f'\\n=== Processing {video_id} ===')
    try:
        print(get_yt_video_info(video_id))
    except Exception as e:
        print(f'Error: {e}')
    print('\\n' + '='*60)
"
```

**Note**: Replace `'dQw4w9WgXcQ'` with any YouTube video ID you want to extract. The video ID is the part after `v=` in a YouTube URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).

### Command Line Interface (CLI)

For more convenient command-line usage, you can use the included CLI script:

#### Basic Usage

```bash
# Extract full video information and transcript
uv run python yt_extract_cli.py dQw4w9WgXcQ
```

#### Advanced Options

```bash
# Get only video information (skip transcript)
uv run python yt_extract_cli.py dQw4w9WgXcQ --info-only

# Get only transcript (skip video info)
uv run python yt_extract_cli.py dQw4w9WgXcQ --transcript-only

# Save output to a file
uv run python yt_extract_cli.py dQw4w9WgXcQ --output video_info.txt
uv run python yt_extract_cli.py dQw4w9WgXcQ -o video_info.txt

# Combine options: save only video info to file
uv run python yt_extract_cli.py dQw4w9WgXcQ --info-only -o video_metadata.txt
```

#### CLI Help

```bash
# See all available options
uv run python yt_extract_cli.py --help
```

**CLI Features:**
- **Flexible output**: Choose video info only, transcript only, or both
- **File output**: Save results directly to a file
- **Progress indicators**: See what's happening during extraction
- **Error handling**: Clear error messages for troubleshooting
- **Help system**: Built-in help with `--help` flag

### Transport Protocols

This MCP server supports two transport protocols:

#### **stdio Transport (Default - Production Use)**
- **Best for**: Claude Desktop integration and production deployments
- **Configuration**: Default transport when running `mcp_youtube_extract`
- **Usage**: Communicates via standard input/output streams
- **Integration**: Works seamlessly with MCP clients like Claude Desktop

#### **SSE Transport (Testing & Debugging)**
- **Best for**: Development, testing, and debugging MCP servers
- **Configuration**: HTTP-based Server-Sent Events protocol
- **Benefits**: 
  - Easy testing with curl commands
  - Real-time monitoring of server responses
  - Web browser compatibility for quick checks
  - Detailed debugging capabilities

**For comprehensive SSE testing and debugging**, see the detailed guide in [`mcp-sse-guide.md`](mcp-sse-guide.md). This guide covers:

- Setting up SSE transport for testing
- Step-by-step MCP protocol handshake sequence
- Testing with curl commands and browser
- Troubleshooting common issues
- Transport protocol comparison and use cases

**Quick SSE Testing Setup:**
```bash
# Start server with SSE transport (modify server.py)
mcp.run(transport="sse")  # Instead of mcp.run()

# Test with curl
curl -N -H "Accept: text/event-stream" http://127.0.0.1:8000/sse
```

### Running Tests

```bash
# Run all pytest tests
uv run pytest

# Run specific pytest test
uv run pytest tests/test_with_api_key.py

# Run tests with coverage
uv run pytest --cov=src/mcp_youtube_extract --cov-report=term-missing
```

**Note**: The `tests/` directory contains 4 files:
- `test_context_fix.py` - Pytest test for context API fallback functionality
- `test_with_api_key.py` - Pytest test for full functionality with API key
- `test_youtube_unit.py` - **Unit tests** for core YouTube functionality
- `test_inspector.py` - **Standalone inspection script** (not a pytest test)

**Test Coverage**: The project currently has 62% overall coverage with excellent coverage of core functionality:
- `youtube.py`: 81% coverage (core business logic)
- `logger.py`: 73% coverage (logging utilities)
- `server.py`: 22% coverage (MCP protocol handling)
- `__init__.py`: 100% coverage (package initialization)

### Running the Inspection Script

The `test_inspector.py` file is a standalone script that connects to the MCP server and validates its functionality:

```bash
# Run the inspection script to test server connectivity and functionality
uv run python tests/test_inspector.py
```

This script will:
- Connect to the MCP server
- List available tools, resources, and prompts
- Test the `get_yt_video_info` tool with a sample video
- Validate that the server is working correctly

### Using the YouTube Tool

The server provides one main tool: `get_yt_video_info`

This tool takes a YouTube video ID and returns:
- Video metadata (title, description, channel, publish date)
- Video transcript (with fallback logic for different transcript types)

**Example Usage:**
```python
# Extract video ID from YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
video_id = "dQw4w9WgXcQ"
result = get_yt_video_info(video_id)
```

### Client Configuration

To use this MCP server with a client, add the following configuration to your client's settings:

#### Using PyPI Installation (Recommended)

```json
{
  "mcpServers": {
    "mcp_youtube_extract": {
      "command": "mcp_youtube_extract",
      "env": {
        "YOUTUBE_API_KEY": "your_youtube_api_key"
      }
    }
  }
}
```

#### Using Development Setup

```json
{
  "mcpServers": {
    "mcp_youtube_extract": {
      "command": "uv",
      "args": [
        "--directory",
        "<your-project-directory>",
        "run",
        "mcp_youtube_extract"
      ],
      "env": {
        "YOUTUBE_API_KEY": "your_youtube_api_key"
      }
    }
  }
}
```

## Development

### Project Structure

```
mcp_youtube_extract/
├── src/
│   └── mcp_youtube_extract/
│       ├── __init__.py
│       ├── server.py          # MCP server implementation
│       ├── youtube.py         # YouTube API utilities
│       └── logger.py          # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── test_context_fix.py    # Context API fallback tests
│   ├── test_inspector.py      # Server inspection tests
│   ├── test_with_api_key.py   # Full functionality tests
│   └── test_youtube_unit.py   # Unit tests for core functionality
├── logs/                      # Application logs
├── yt_extract_cli.py          # Command-line interface script
├── mcp-sse-guide.md           # SSE transport testing guide
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules (includes coverage files)
├── .python-version            # Python version specification
├── pyproject.toml             # Project configuration
├── LICENSE                    # MIT License
├── uv.lock                    # UV package lock file
└── README.md
```

### Testing Strategy

The project uses a comprehensive testing approach:

1. **Unit Tests** (`test_youtube_unit.py`): Test core YouTube functionality with mocked APIs
2. **Integration Tests** (`test_context_fix.py`, `test_with_api_key.py`): Test full server functionality
3. **Manual Validation** (`test_inspector.py`): Interactive server inspection tool
4. **Transport Testing**: SSE transport protocol testing guide (`mcp-sse-guide.md`)

### Error Handling

The project includes robust error handling:
- **Graceful API failures**: Returns appropriate error messages instead of crashing
- **Fallback logic**: Multiple strategies for transcript retrieval
- **Consistent error responses**: Standardized error message format
- **Comprehensive logging**: Detailed logs for debugging and monitoring

### Building

```bash
# Install build dependencies
uv add --dev hatch

# Build the package
uv run hatch build
```

## Documentation

- **README.md** - Main project documentation (this file)
- **mcp-sse-guide.md** - Comprehensive guide for SSE transport protocol testing
- **API Documentation** - Inline documentation in source code
- **Test Documentation** - Testing strategy and coverage reports

## Acknowledgments

This project is based on the original [mcp_youtube_extract](https://github.com/sinjab/mcp_youtube_extract) repository by [sinjab](https://github.com/sinjab). This updated mcp_youtube_extract repo includes additional enhancements:

- **Windows installation guide** for uv and Rust toolchain
- **SSE transport testing guide** (`mcp-sse-guide.md`)
- **Enhanced CLI interface** with additional options
- **Comprehensive transport protocol documentation**
- **Extended testing and debugging capabilities**

Special thanks to the original author for creating the foundational MCP YouTube extraction framework.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

If you encounter any issues or have questions, please:
1. Check the [existing issues](https://github.com/hwang2006/mcp_youtube_extract/issues)
2. Create a new issue with detailed information about your problem
3. Include logs and error messages when applicable
4. For SSE transport issues, refer to the [`mcp-sse-guide.md`](mcp-sse-guide.md) troubleshooting section
