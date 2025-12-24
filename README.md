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


Then: Browse and install plugins → legnext-midjourney-imagine → Select skill → Install now

### Manual Installation

```bash
# Download skill .zip from releases
unzip legnext-midjourney.zip -d ~/.claude/skills/
unzip midjourney-prompting.zip -d ~/.claude/skills/
```

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
