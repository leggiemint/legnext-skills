#!/usr/bin/env python3
"""
Query the status of a Legnext task

Usage:
    get_task.py <job_id>
    get_task.py 98761286-cdc7-4085-abfe-c9f149ff722b

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
    current_dir = Path.cwd()
    for parent in [current_dir] + list(current_dir.parents):
        env_file = parent / '.env'
        if env_file.exists():
            load_dotenv(env_file)
            break
except ImportError:
    pass


def get_task_status(job_id):
    """
    Get the status of a task from Legnext API

    Args:
        job_id (str): The unique identifier of the job (UUID format)

    Returns:
        dict: Response containing job status, output, and metadata
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
    url = f'https://api.legnext.ai/api/v1/job/{job_id}'
    headers = {
        'x-api-key': api_key
    }

    try:
        # Make API request
        response = requests.get(url, headers=headers, timeout=30)
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
        print("Usage: get_task.py <job_id>")
        print("\nExample:")
        print('  get_task.py 98761286-cdc7-4085-abfe-c9f149ff722b')
        print("\nAPI Key Configuration:")
        print("  The script looks for LEGNEXT_API_KEY in:")
        print("    1. .env file (in current or parent directories)")
        print("    2. Environment variable")
        print("\n  Get your API key from: https://legnext.ai")
        sys.exit(1)

    job_id = sys.argv[1]

    print(f"Querying task status...")
    print(f"Job ID: {job_id}")
    print()

    result = get_task_status(job_id)

    # Pretty print result
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    if 'error' in result:
        sys.exit(1)
    else:
        status = result.get('status')
        print(f"\n✓ Current status: {status}")

        if status == 'completed':
            output = result.get('output', {})
            if 'images' in output or 'image_urls' in output:
                print("✓ Images ready!")
        elif status == 'failed':
            print("✗ Task failed!")
            if 'error' in result:
                print(f"Error: {result['error']}")

        sys.exit(0)


if __name__ == '__main__':
    main()
