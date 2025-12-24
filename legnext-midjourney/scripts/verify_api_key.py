#!/usr/bin/env python3
"""
Verify Legnext API key by checking account balance

Usage:
    verify_api_key.py
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


def verify_api_key():
    """
    Verify API key by checking account balance

    Returns:
        dict: Verification result with balance info or error
    """
    api_key = os.environ.get('LEGNEXT_API_KEY')
    if not api_key:
        return {
            'valid': False,
            'error': 'LEGNEXT_API_KEY not found',
            'details': 'Please configure your API key first'
        }

    url = 'https://api.legnext.ai/api/account/balance'
    headers = {'X-API-KEY': api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('code') == 200:
            balance_data = data.get('data', {})
            return {
                'valid': True,
                'balance_usd': balance_data.get('balance_usd'),
                'available_credits': balance_data.get('available_credits'),
                'available_points': balance_data.get('available_points'),
                'account_id': balance_data.get('account_id')
            }
        else:
            return {
                'valid': False,
                'error': 'API returned error',
                'details': data.get('message', 'Unknown error')
            }

    except requests.exceptions.RequestException as e:
        return {
            'valid': False,
            'error': 'API request failed',
            'details': str(e)
        }


def main():
    print("Verifying Legnext API key...")
    print()

    result = verify_api_key()

    if result.get('valid'):
        print("✓ API key is valid")
        print(f"  Account ID: {result.get('account_id')}")
        print(f"  Balance: ${result.get('balance_usd'):.2f} USD")
        print(f"  Credits: {result.get('available_credits')}")
        print(f"  Points: {result.get('available_points')}")
        sys.exit(0)
    else:
        print("✗ API key verification failed")
        print(f"  Error: {result.get('error')}")
        print(f"  Details: {result.get('details')}")
        sys.exit(1)


if __name__ == '__main__':
    main()
