#!/usr/bin/env python3
"""
CTF Platform Client - CTF Professor
===================================
Unified API client for interacting with CTFd, HackTheBox, and TryHackMe.
Handles metadata fetching, file downloads, and flag submissions.
"""

import os
import sys
import json
import requests
import logging
from pathlib import Path
from typing import Dict, Optional, Any
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("platform_bridge")

class PlatformClient:
    def __init__(self):
        self.workspace = Path(".agent/sandbox/workspace")
        self.workspace.mkdir(parents=True, exist_ok=True)
        self._load_env()

    def _load_env(self):
        """Load credentials from local .env file if it exists."""
        self.config = {}
        env_path = Path(".env")
        if env_path.exists():
            with open(env_path, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        self.config[key] = value

    def identify_platform(self, url: str) -> Optional[str]:
        """Identify CTF platform from URL."""
        domain = urlparse(url).netloc.lower()
        if "hackthebox.com" in domain:
            return "htb"
        if "tryhackme.com" in domain:
            return "thm"
        # CTFd is usually self-hosted, so we check if the user configured a CTFd URL
        ctfd_url = self.config.get("CTFD_URL", "")
        if ctfd_url and urlparse(ctfd_url).netloc.lower() in domain:
            return "ctfd"
        return "ctfd" # Default fallback for custom domains

    def fetch_ctfd_challenge(self, challenge_id: str) -> Optional[Dict[str, Any]]:
        """Fetch challenge from CTFd API."""
        url = f"{self.config.get('CTFD_URL')}/api/v1/challenges/{challenge_id}"
        headers = {
            "Authorization": f"Token {self.config.get('CTFD_TOKEN')}",
            "Content-Type": "application/json"
        }
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.raise_for_status()
            data = r.json().get("data", {})
            
            # Fetch files
            files_url = f"{self.config.get('CTFD_URL')}/api/v1/challenges/{challenge_id}/files"
            rf = requests.get(files_url, headers=headers, timeout=10)
            if rf.status_code == 200:
                data["files"] = rf.json().get("data", [])
            
            return data
        except Exception as e:
            logger.error(f"Failed to fetch CTFd challenge: {e}")
            return None

    def download_file(self, url: str, filename: str) -> Optional[Path]:
        """Download file to sandbox workspace."""
        headers = {}
        # Add auth if it's a CTFd internal file
        if self.config.get("CTFD_URL") in url:
             headers["Authorization"] = f"Token {self.config.get('CTFD_TOKEN')}"
        
        try:
            r = requests.get(url, headers=headers, stream=True, timeout=30)
            r.raise_for_status()
            dest = self.workspace / filename
            with open(dest, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"Downloaded: {filename}")
            return dest
        except Exception as e:
            logger.error(f"Failed to download {filename}: {e}")
            return None

    def submit_flag_ctfd(self, challenge_id: str, flag: str) -> bool:
        """Submit flag to CTFd."""
        url = f"{self.config.get('CTFD_URL')}/api/v1/challenges/attempt"
        headers = {
            "Authorization": f"Token {self.config.get('CTFD_TOKEN')}",
            "Content-Type": "application/json"
        }
        payload = {"challenge_id": challenge_id, "submission": flag}
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=10)
            status = r.json().get("data", {}).get("status")
            return status == "correct"
        except Exception as e:
            logger.error(f"Failed to submit flag to CTFd: {e}")
            return False

if __name__ == "__main__":
    # Basic CLI test
    client = PlatformClient()
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "fetch" and len(sys.argv) > 2:
            data = client.fetch_ctfd_challenge(sys.argv[2])
            print(json.dumps(data, indent=2))
        elif cmd == "submit" and len(sys.argv) > 3:
            success = client.submit_flag_ctfd(sys.argv[2], sys.argv[3])
            print(f"Correct: {success}")
