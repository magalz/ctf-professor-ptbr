---
name: ctf-challenge-classifier
description: Systematic CTF challenge classification using a 3-tier taxonomy (CTF Type, Category, Vulnerability Class). Provides decision trees, artifact analysis heuristics, and structured output schemas.
allowed-tools: Read, Bash, Glob, Python
---

# CTF Challenge Classifier

> Classify before you attack. Every challenge has a signature if you know where to look.

---

## 1. The 3-Tier Classification Model

### Tier 1 — CTF Format (Tipo CTF)

| Format | Indicators |
|:---|:---|
| **Jeopardy** | Individual challenges with point values, flag format (e.g., `flag{...}`, `CTF{...}`), no live opponent |
| **Attack/Defense (A/D)** | Teams defend services while attacking others, vulnbox/gameserver mentioned, tick-based scoring |
| **King of the Hill (KotH)** | Maintain control of a machine, persistence-focused, time-based scoring |
| **Mixed/Hybrid** | Combination — look for multiple formats or stages |

### Tier 2 — Domain Category (Categoria)

| Category | Key Signatures |
|:---|:---|
| **Web** | URL provided, HTTP service, source code (PHP/JS/Python), cookies/sessions mentioned |
| **Pwn** | ELF/PE binary, `checksec` output, libc version, nc/socat connection |
| **Crypto** | Ciphertext, public key, mathematical values (n, e, p, q), encoded output |
| **Forense** | `.pcap`/`.pcapng`, memory dump (`.raw`, `.vmem`), disk image, log files |
| **OSINT** | Person/company name, image with metadata, social media reference, "find" verbs |
| **RE** | Binary without remote service, "crack the password", license key, obfuscated code |
| **Rede** | Network capture, protocol analysis, firewall rules, routing tables |
| **Cloud** | AWS/Azure/GCP references, IAM, S3, Lambda, Kubernetes manifests |
| **Mobile** | APK/IPA file, mobile app description, Android/iOS references |
| **AI/ML** | Model file (.h5, .pkl, .onnx), prompt, chatbot, classification task |
| **Hardware/IoT** | Firmware binary, UART/JTAG mentioned, signal capture, embedded device |
| **Misc** | Doesn't fit above — programming puzzles, game hacking, unconventional formats |

### Tier 3 — Vulnerability Class (Classe)

#### Web
SQLi (Blind/Error-based), XSS (Stored/DOM), SSRF, SSTI, IDOR, LFI/RFI, JWT Bypass, Prototype Pollution, GraphQL Injection, XXE, Deserialization, Race Conditions

#### Pwn
Buffer Overflow, ROP Chains, Heap Exploitation (UAF, Double Free, Tcache poisoning), Format String, Integer Overflow, Type Confusion, Kernel Exploitation

#### Crypto
RSA (Padding Oracle, Wiener's, Coppersmith), AES (ECB/CBC/GCM), Elliptic Curves (ECC), Diffie-Hellman, Hash Collisions (MD5/SHA1), LLL Algorithm, Known-Plaintext, XOR analysis

#### Forense
Memory Analysis (Volatility), Disk Imaging (Autopsy), Steganography (LSB, Metadata), Log Auditing (SIEM/ELK), File Carving, Timeline Analysis, Browser Forensics

#### OSINT
Geolocalização, SOCMINT (Social Media), Metadata Analysis, Breach Data Analysis, WHOIS/DNS Enumeration, Wayback Machine, Dorking (Google/GitHub/Shodan)

#### RE
Anti-debugging/Anti-VM, Obfuscation, Custom Bytecode, Malware Analysis, Decompilation (C/Go/Rust/Python), Binary Patching, Symbolic Execution (Angr)

#### Rede
Traffic Analysis (PCAP/PCAPNG), Protocol Reversing, Tunneling (ICMP/DNS), Wireless Attacks (WPA3), VPN Bypassing, SMB/AD (Kerberoasting), ARP Spoofing

#### Cloud
S3 Bucket Misconfigurations, IAM Role Assumption, Serverless Exploitation (Lambda/Functions), Kubernetes/Docker Escapes, Azure AD attacks

#### AI/ML
Prompt Injection, Adversarial Attacks, Model Inversion, Data Poisoning

#### Hardware/IoT
Firmware Analysis, JTAG/UART Debugging, Side-channel attacks (Power analysis), Glitching

---

## 2. Decision Tree

Follow this sequence to classify. Stop at the first confident match.

```
INPUT RECEIVED
│
├── Is there an attached file?
│   ├── YES → Run `file <filename>` to get magic bytes
│   │   ├── ELF/PE executable → Pwn or RE
│   │   │   ├── Remote connection (nc/socat) provided? → Pwn
│   │   │   └── No remote, "crack"/"keygen" keywords → RE
│   │   ├── PCAP/PCAPNG → Forense (Rede subcategory)
│   │   ├── Memory dump (.raw, .vmem, .dmp) → Forense
│   │   ├── Image (.png, .jpg, .bmp) → Check steganography or OSINT
│   │   ├── Archive (.zip, .tar, .gz) → Extract safely, re-classify contents
│   │   ├── APK/IPA → Mobile
│   │   ├── Firmware (.bin, .rom) → Hardware/IoT
│   │   ├── Model (.h5, .pkl, .onnx) → AI/ML
│   │   └── Source code → Analyze language and patterns
│   │       ├── PHP/Python/JS with web imports → Web
│   │       ├── C/C++ with socket/memory ops → Pwn
│   │       └── Python with crypto imports → Crypto
│   └── NO → Continue to text/image analysis
│
├── Is there a URL or IP?
│   ├── YES → Web (most likely) or Rede
│   │   ├── HTTP/HTTPS → Web
│   │   └── Non-standard port → Rede or Pwn
│   └── NO → Continue
│
├── Analyze description keywords
│   ├── Crypto terms (RSA, AES, cipher, key, encrypt) → Crypto
│   ├── Forensic terms (memory, pcap, disk, deleted) → Forense
│   ├── OSINT terms (find, person, location, social) → OSINT
│   ├── Cloud terms (S3, Lambda, IAM, bucket) → Cloud
│   └── No match → Misc (ask clarifying questions)
│
└── Analyze screenshot (if present)
    ├── CTF platform UI visible → Extract title, tags, points
    ├── Terminal output → Analyze commands and output
    └── Web page → Web category likely
```

---

## 3. Difficulty Estimation

| Signal | Difficulty |
|:---|:---|
| Points ≤ 100, simple description, common tools | **Iniciante / Beginner** |
| Points 100-300, requires chaining techniques | **Intermediário / Intermediate** |
| Points > 300, custom exploitation, kernel/heap | **Avançado / Advanced** |
| No point value visible | Estimate from artifact complexity |

---

## 4. Fallback: Clarifying Questions

When confidence is low, ask **at most 2 questions** in the detected language:

**PT-BR:**
- "Você tem mais informações sobre a plataforma do CTF (ex: CTFd, HackTheBox, TryHackMe)?"
- "O desafio menciona alguma flag format específica (ex: `FLAG{...}`)?"

**EN:**
- "Do you have more context about the CTF platform (e.g., CTFd, HackTheBox, TryHackMe)?"
- "Does the challenge mention a specific flag format (e.g., `FLAG{...}`)?"

---

## 5. Script Support

| Script | Purpose |
|:---|:---|
| `scripts/classify.py` | Pattern-matching classifier — analyzes file types, magic bytes, and description keywords |

---

## 6. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Classify based only on file extension | Always verify with `file` command (magic bytes) |
| Output "Misc" without trying harder | Exhaust the decision tree first |
| Skip image analysis | Always read visible text from screenshots |
| Classify AND start solving | Classification is separate from solving — hand off to professor |
