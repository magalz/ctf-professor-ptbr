#!/usr/bin/env python3
"""
CTF Challenge Classifier — Pattern Matching Engine

Analyzes file artifacts and description keywords to produce a preliminary
classification. Designed to support the challenge-classifier agent.

Usage:
    python classify.py <file_path>
    python classify.py --description "SQL injection on login page"
    python classify.py <file_path> --description "200 points, web category"
"""

import argparse
import os
import struct
import sys

# === Magic Bytes Database ===
MAGIC_BYTES = {
    b"\x7fELF": ("ELF Binary", "Pwn/RE"),
    b"MZ": ("PE Executable", "Pwn/RE"),
    b"\xca\xfe\xba\xbe": ("Mach-O / Java Class", "RE"),
    b"\xfe\xed\xfa": ("Mach-O Binary", "RE"),
    b"PK": ("ZIP Archive", "Forense/Misc"),
    b"\x1f\x8b": ("GZIP Archive", "Forense/Misc"),
    b"\x89PNG": ("PNG Image", "Forense/OSINT"),
    b"\xff\xd8\xff": ("JPEG Image", "Forense/OSINT"),
    b"GIF8": ("GIF Image", "Forense/OSINT"),
    b"\xd4\xc3\xb2\xa1": ("PCAP (Little-Endian)", "Forense/Rede"),
    b"\xa1\xb2\xc3\xd4": ("PCAP (Big-Endian)", "Forense/Rede"),
    b"\x0a\x0d\x0d\x0a": ("PCAPNG", "Forense/Rede"),
    b"SQLite format": ("SQLite Database", "Forense"),
    b"MDMP": ("Windows Minidump", "Forense"),
    b"\x00asm": ("WebAssembly", "RE/Web"),
    b"%PDF": ("PDF Document", "Forense/Misc"),
}

# === Extension Mapping ===
EXT_MAP = {
    # Pwn / RE
    ".elf": "Pwn/RE", ".exe": "Pwn/RE", ".dll": "RE",
    ".so": "RE", ".o": "RE", ".bin": "Pwn/RE/Hardware",
    # Forensics / Network
    ".pcap": "Forense/Rede", ".pcapng": "Forense/Rede",
    ".raw": "Forense", ".vmem": "Forense", ".dmp": "Forense",
    ".e01": "Forense", ".dd": "Forense",
    # Crypto
    ".pem": "Crypto", ".pub": "Crypto", ".key": "Crypto",
    ".crt": "Crypto", ".enc": "Crypto", ".aes": "Crypto",
    # Web
    ".php": "Web", ".html": "Web", ".js": "Web",
    ".asp": "Web", ".aspx": "Web", ".jsp": "Web",
    # Mobile
    ".apk": "Mobile", ".ipa": "Mobile",
    # AI/ML
    ".h5": "AI/ML", ".pkl": "AI/ML", ".onnx": "AI/ML",
    ".pt": "AI/ML", ".pth": "AI/ML",
    # Hardware
    ".rom": "Hardware", ".hex": "Hardware",
    # Archives
    ".zip": "Misc", ".tar": "Misc", ".gz": "Misc",
    ".7z": "Misc", ".rar": "Misc",
    # Images (potential stego)
    ".png": "Forense/OSINT", ".jpg": "Forense/OSINT",
    ".jpeg": "Forense/OSINT", ".bmp": "Forense/OSINT",
    ".gif": "Forense/OSINT",
}

# === Description Keyword Patterns ===
KEYWORD_PATTERNS = {
    "Web": [
        "sql", "injection", "xss", "csrf", "ssrf", "ssti", "idor",
        "login", "cookie", "session", "jwt", "api", "http", "url",
        "web", "php", "html", "javascript", "graphql", "xxe",
        "deserialization", "prototype pollution", "race condition",
        "lfi", "rfi", "upload",
    ],
    "Pwn": [
        "buffer overflow", "bof", "rop", "heap", "format string",
        "stack", "shellcode", "exploit", "binary", "pwn", "nc ",
        "netcat", "libc", "canary", "nx", "pie", "aslr", "uaf",
        "double free", "tcache", "kernel",
    ],
    "Crypto": [
        "rsa", "aes", "cipher", "encrypt", "decrypt", "key",
        "modulus", "exponent", "prime", "hash", "xor", "base64",
        "caesar", "vigenere", "ecc", "elliptic", "diffie",
        "padding oracle", "cbc", "ecb", "gcm",
    ],
    "Forense": [
        "memory", "volatility", "pcap", "forensic", "disk",
        "steganography", "stego", "hidden", "deleted", "carving",
        "autopsy", "timeline", "log", "siem", "browser",
    ],
    "OSINT": [
        "osint", "geolocation", "social media", "metadata",
        "person", "find", "locate", "whois", "dns", "dorking",
        "shodan", "breach",
    ],
    "RE": [
        "reverse", "decompil", "disassembl", "crackme", "keygen",
        "obfuscat", "anti-debug", "ghidra", "ida", "radare",
        "angr", "binary patch", "malware",
    ],
    "Rede": [
        "network", "traffic", "protocol", "tunnel", "wireless",
        "vpn", "kerberos", "smb", "active directory", "arp",
        "icmp", "dns tunnel",
    ],
    "Cloud": [
        "s3", "bucket", "iam", "lambda", "serverless",
        "kubernetes", "docker", "container", "azure", "aws", "gcp",
    ],
    "AI/ML": [
        "prompt injection", "adversarial", "model", "machine learning",
        "neural", "ai", "llm", "chatbot", "poisoning",
    ],
    "Hardware": [
        "firmware", "jtag", "uart", "spi", "side-channel",
        "glitch", "iot", "embedded", "hardware",
    ],
}


def classify_file(filepath: str) -> dict:
    """Classify a file by magic bytes and extension."""
    result = {
        "filename": os.path.basename(filepath),
        "magic_type": "Unknown",
        "magic_category": "Misc",
        "ext_category": "Misc",
        "file_size": 0,
    }

    if not os.path.isfile(filepath):
        result["error"] = f"File not found: {filepath}"
        return result

    result["file_size"] = os.path.getsize(filepath)

    # Read first 16 bytes for magic detection
    with open(filepath, "rb") as f:
        header = f.read(16)

    # Check magic bytes (longest match first)
    for magic, (desc, cat) in sorted(
        MAGIC_BYTES.items(), key=lambda x: -len(x[0])
    ):
        if header.startswith(magic):
            result["magic_type"] = desc
            result["magic_category"] = cat
            break

    # Check extension
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    if ext in EXT_MAP:
        result["ext_category"] = EXT_MAP[ext]

    return result


def classify_description(description: str) -> dict:
    """Classify based on description keywords."""
    desc_lower = description.lower()
    scores = {}

    for category, keywords in KEYWORD_PATTERNS.items():
        score = sum(1 for kw in keywords if kw in desc_lower)
        if score > 0:
            scores[category] = score

    if not scores:
        return {"category": "Misc", "confidence": "Baixa", "scores": {}}

    top = max(scores, key=scores.get)
    top_score = scores[top]

    if top_score >= 3:
        confidence = "Alta"
    elif top_score >= 2:
        confidence = "Média"
    else:
        confidence = "Baixa"

    return {
        "category": top,
        "confidence": confidence,
        "scores": scores,
    }


def main():
    parser = argparse.ArgumentParser(
        description="CTF Challenge Classifier — Pattern Matching Engine"
    )
    parser.add_argument(
        "file", nargs="?", help="Path to the challenge file/artifact"
    )
    parser.add_argument(
        "--description", "-d", type=str, default="",
        help="Challenge description text"
    )
    args = parser.parse_args()

    if not args.file and not args.description:
        parser.error("Provide at least a file path or --description")

    print("=" * 50)
    print("  CTF Challenge Classifier")
    print("=" * 50)

    # File analysis
    if args.file:
        file_result = classify_file(args.file)
        print(f"\n📁 File: {file_result['filename']}")
        print(f"   Size: {file_result['file_size']} bytes")
        print(f"   Magic: {file_result['magic_type']}")
        print(f"   Category (magic): {file_result['magic_category']}")
        print(f"   Category (ext):   {file_result['ext_category']}")

    # Description analysis
    if args.description:
        desc_result = classify_description(args.description)
        print(f"\n📝 Description Analysis:")
        print(f"   Category: {desc_result['category']}")
        print(f"   Confidence: {desc_result['confidence']}")
        if desc_result["scores"]:
            print(f"   All scores: {desc_result['scores']}")

    print("\n" + "=" * 50)
    print("  Use this output to inform the classifier agent.")
    print("=" * 50)


if __name__ == "__main__":
    main()
