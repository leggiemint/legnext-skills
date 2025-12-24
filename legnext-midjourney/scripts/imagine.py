#!/usr/bin/env python3
"""
Submit an image generation task to Legnext API

Usage:
    imagine.py "prompt text here"
    imagine.py "a beautiful sunset --v 7 --ar 16:9"

Environment variables required:
    LEGNEXT_API_KEY: Your Legnext API key from the dashboard

Configuration:
    The script automatically looks for a .env file in the current directory
    or parent directories and loads LEGNEXT_API_KEY from it.
"""

import sys
import os
import json
import requests
from pathlib import Path

# Load .env file if present
try:
    from dotenv import load_dotenv
    # Search for .env file in current and parent directories
    current_dir = Path.cwd()
    for parent in [current_dir] + list(current_dir.parents):
        env_file = parent / '.env'
        if env_file.exists():
            load_dotenv(env_file)
            break
except ImportError:
    # python-dotenv not installed, skip .env file loading
    pass


def submit_imagine_task(prompt):
    """
    Submit an image generation task to Legnext API

    Args:
        prompt (str): The text prompt for image generation (can include Midjourney parameters)

    Returns:
        dict: Response containing job_id and status, or error information
    """
    # Get API key from environment
    api_key = os.environ.get('LEGNEXT_API_KEY')
    if not api_key:
        return {
            'error': 'LEGNEXT_API_KEY not found',
            'details': (
                'Please configure your Legnext API key:\n\n'
                '  Option 1 (Recommended): Create a .env file\n'
                '    echo "LEGNEXT_API_KEY=your-api-key-here" > .env\n\n'
                '  Option 2: Set environment variable\n'
                '    export LEGNEXT_API_KEY=your-api-key-here\n\n'
                '  Get your API key from: https://legnext.ai\n'
                '  (Dashboard → API Settings)'
            )
        }

    # Prepare request
    url = 'https://api.legnext.ai/api/v1/diffusion'
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }

    payload = {'text': prompt}

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            'error': 'API request failed',
            'details': str(e),
            'status_code': getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: imagine.py \"prompt text here\"")
        print("\nExample:")
        print('  imagine.py "a cyberpunk city at night --v 7 --ar 16:9"')
        print("\nAPI Key Configuration:")
        print("  The script looks for LEGNEXT_API_KEY in:")
        print("    1. .env file (in current or parent directories)")
        print("    2. Environment variable")
        print("\n  Get your API key from: https://legnext.ai")
        sys.exit(1)

    prompt = sys.argv[1]

    print(f"Submitting imagine task...")
    print(f"Prompt: {prompt}")
    print()

    result = submit_imagine_task(prompt)

    # Pretty print result
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    if 'error' in result:
        sys.exit(1)
    else:
        print(f"\n✓ Task submitted successfully!")
        print(f"Job ID: {result.get('job_id')}")
        print(f"Status: {result.get('status')}")
        sys.exit(0)


if __name__ == '__main__':
    main()
