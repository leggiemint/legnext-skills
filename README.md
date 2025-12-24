# Legnext Skills

Midjourney image generation and prompt engineering skills for Claude Code, powered by Legnext API.

## Skills

### legnext-midjourney
Generate AI images using Midjourney through the Legnext API with complete workflow automation.

**Features:**
- Submit and poll Midjourney image generation tasks
- Automatic task status tracking and result retrieval
- API key verification and balance checking
- Support for all Midjourney V7 parameters

**Requirements:** Legnext API key from [legnext.ai/app/api-keys](https://legnext.ai/app/api-keys)

---

### midjourney-prompting
Expert Midjourney prompt engineering guidance without API integration.

**Features:**
- Convert natural language to optimized Midjourney prompts
- 7-Element Framework for systematic prompt construction
- Midjourney V7 best practices and parameter guidance
- Photography terminology for photorealistic results

**No API required** - Pure prompt engineering expertise.

---

## Installation

### Quick Install

**1. Download the skills you need:**
   - [legnext-midjourney.zip](../../raw/main/legnext-midjourney.zip) - Image generation via Legnext API
   - [midjourney-prompting.zip](../../raw/main/midjourney-prompting.zip) - Prompt engineering only

**2. Unzip to Claude skills directory:**
```bash
# For legnext-midjourney (with API)
unzip legnext-midjourney.zip -d ~/.claude/skills/

# For midjourney-prompting (no API needed)
unzip midjourney-prompting.zip -d ~/.claude/skills/
```

**3. Restart Claude Code** (if running)

That's it! The skills are now available in Claude Code.

---

## Setup

### For legnext-midjourney

**1. Get API key:** [legnext.ai/app/api-keys](https://legnext.ai/app/api-keys)

**2. Configure API key:**
```bash
# Option 1: Create .env file (recommended)
echo "LEGNEXT_API_KEY=your-api-key-here" > .env

# Option 2: Set environment variable
export LEGNEXT_API_KEY=your-api-key-here
```

**3. Install dependencies:**
```bash
cd ~/.claude/skills/legnext-midjourney
pip install -r requirements.txt
```

**4. Verify:**
```bash
python scripts/verify_api_key.py
```

### For midjourney-prompting

No setup required.

---

## Usage

### Using legnext-midjourney

Once installed and configured, simply ask Claude Code to generate images:

```
User: "Generate a professional headshot with studio lighting"
Claude: *Uses legnext-midjourney skill to create optimized prompt and generate image*
```

Or use the scripts directly:
```bash
# Complete workflow (recommended)
cd ~/.claude/skills/legnext-midjourney
python scripts/generate_and_wait.py "a majestic lion in savanna, golden hour --ar 16:9 --v 7"

# Check account balance
python scripts/verify_api_key.py
```

### Using midjourney-prompting

Ask Claude Code for prompt engineering help:

```
User: "I need a cyberpunk city scene for a poster"
Claude: *Uses midjourney-prompting skill to craft optimized Midjourney prompt*
```

The skill will convert your natural language request into an effective Midjourney prompt with appropriate parameters.

---

## Security

**Never commit API keys or secrets!**

- `.env` files are gitignored
- Use environment variables for API keys
- Check `.gitignore` before committing

---

## License

MIT

---

## Support

- Legnext API: support@legnext.ai
- Skill issues: [GitHub Issues](https://github.com/[your-username]/legnext-midjourney-imagine/issues)
- API keys: [legnext.ai/app/api-keys](https://legnext.ai/app/api-keys)
