#!/usr/bin/env python3
"""
Submit an image generation task and wait for completion

This script combines imagine.py and get_task.py to provide a complete workflow:
1. Submit the image generation task
2. Poll for status updates
3. Return the final result when complete

Usage:
    generate_and_wait.py "prompt text here" [--interval SECONDS] [--max-wait SECONDS]
    generate_and_wait.py "a beautiful sunset --v 7" --interval 5 --max-wait 300

Environment variables required:
    LEGNEXT_API_KEY: Your Legnext API key from the dashboard

Configuration:
    The script automatically looks for a .env file in the current directory
    or parent directories and loads LEGNEXT_API_KEY from it.
"""

import sys
import os
import time
import json
import argparse
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

from imagine import submit_imagine_task
from get_task import get_task_status


def generate_and_wait(prompt, poll_interval=5, max_wait_time=180, initial_wait=10):
    """
    Submit an image generation task and wait for completion

    Args:
        prompt (str): The text prompt for image generation
        poll_interval (int): Seconds to wait between status checks (default: 5)
        max_wait_time (int): Maximum seconds to wait before timing out (default: 180)
        initial_wait (int): Initial wait before first status check (default: 10)

    Returns:
        dict: Final task result or error information
    """
    # Step 1: Submit the task
    print(f"Step 1: Submitting imagine task...")
    print(f"Prompt: {prompt}\n")

    result = submit_imagine_task(prompt)

    if 'error' in result:
        return result

    job_id = result.get('job_id')
    print(f"✓ Task submitted! Job ID: {job_id}")
    print(f"Initial status: {result.get('status')}\n")

    # Step 2: Initial wait
    print(f"Step 2: Initial wait ({initial_wait}s)...")
    time.sleep(initial_wait)

    # Step 3: Poll for completion
    print(f"Step 3: Polling for completion (every {poll_interval}s, max {max_wait_time}s)...\n")

    elapsed = initial_wait
    while elapsed < max_wait_time:
        status_result = get_task_status(job_id)

        if 'error' in status_result:
            return status_result

        status = status_result.get('status')
        print(f"[{elapsed}s] Status: {status}")

        # Check if completed
        if status == 'completed':
            print(f"\n✓ Task completed successfully!")
            return status_result

        # Check if failed
        if status == 'failed':
            print(f"\n✗ Task failed!")
            return status_result

        # Wait before next poll
        time.sleep(poll_interval)
        elapsed += poll_interval

    # Timeout
    return {
        'error': 'Timeout',
        'details': f'Task did not complete within {max_wait_time} seconds (typical: 30-80s)',
        'job_id': job_id,
        'last_status': status
    }


def main():
    parser = argparse.ArgumentParser(
        description='Submit Midjourney image generation task and wait for completion'
    )
    parser.add_argument('prompt', help='Text prompt for image generation')
    parser.add_argument('--interval', type=int, default=5,
                       help='Polling interval in seconds (default: 5)')
    parser.add_argument('--max-wait', type=int, default=180,
                       help='Maximum wait time in seconds (default: 180)')
    parser.add_argument('--initial-wait', type=int, default=10,
                       help='Initial wait before first check in seconds (default: 10)')

    args = parser.parse_args()

    # Check API key
    if not os.environ.get('LEGNEXT_API_KEY'):
        print("Error: LEGNEXT_API_KEY not found")
        print("\nPlease configure your Legnext API key:")
        print("\n  Option 1 (Recommended): Create a .env file")
        print("    echo \"LEGNEXT_API_KEY=your-api-key-here\" > .env")
        print("\n  Option 2: Set environment variable")
        print("    export LEGNEXT_API_KEY=your-api-key-here")
        print("\n  Get your API key from: https://legnext.ai")
        print("  (Dashboard → API Settings)")
        sys.exit(1)

    print("=" * 60)
    print("Legnext Midjourney Image Generation")
    print("=" * 60)
    print()

    result = generate_and_wait(args.prompt, args.interval, args.max_wait, args.initial_wait)

    print("\n" + "=" * 60)
    print("Final Result:")
    print("=" * 60)
    print(json.dumps(result, indent=2))

    # Extract and display images if available
    if result.get('status') == 'completed':
        output = result.get('output', {})

        # Try different possible keys for image URLs
        image_urls = (
            output.get('images') or
            output.get('image_urls') or
            output.get('imageUrls') or
            []
        )

        if image_urls:
            print("\n" + "=" * 60)
            print("Generated Images:")
            print("=" * 60)
            for i, url in enumerate(image_urls, 1):
                print(f"{i}. {url}")

        # Display seed if available
        if 'seed' in output:
            print(f"\nSeed: {output['seed']}")

    # Exit with appropriate code
    sys.exit(0 if result.get('status') == 'completed' else 1)


if __name__ == '__main__':
    main()
