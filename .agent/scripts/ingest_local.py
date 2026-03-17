#!/usr/bin/env python3
"""
Local Ingest - CTF Professor
============================
Analyzes a subfolder in CTFs/ and prepares a summary for the agent.
Helps when using the CLI to avoid manual file attachment.
"""

import os
import sys
import json
from pathlib import Path

def ingest_folder(folder_name: str):
    root = Path(".")
    ctf_path = root / "CTFs" / folder_name
    
    if not ctf_path.exists():
        return {"error": f"Folder 'CTFs/{folder_name}' not found."}

    files = list(ctf_path.iterdir())
    summary = {
        "folder": folder_name,
        "description": "",
        "artifacts": [],
        "images": []
    }

    # Common description file names
    desc_names = ["desc.txt", "desc.md", "info.txt", "readme.md", "challenge.txt"]
    
    for f in files:
        if f.is_file():
            # Check for description
            if f.name.lower() in desc_names:
                try:
                    summary["description"] = f.read_text(encoding='utf-8')
                except:
                    pass
            
            # Categorize artifacts
            ext = f.suffix.lower()
            if ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]:
                summary["images"].append(f.name)
            else:
                summary["artifacts"].append(f.name)
                
    # If no description file, use the first .txt or .md file
    if not summary["description"]:
        for f in files:
            if f.suffix.lower() in [".txt", ".md"]:
                try:
                    summary["description"] = f.read_text(encoding='utf-8')
                    break
                except:
                    pass

    return summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No folder name provided."}))
        sys.exit(1)
        
    result = ingest_folder(sys.argv[1])
    print(json.dumps(result, indent=2))
