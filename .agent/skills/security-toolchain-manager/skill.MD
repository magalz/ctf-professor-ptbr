---
name: security-toolchain-manager
description: Framework for pedagogical tool selection and isolated environment management. Enforces justification before installation and prevents host system pollution.
allowed-tools: Read, Bash, Glob
---

# Security Toolchain Manager

> A tool is only as effective as the operator's understanding of its mechanics.

## 1. Tool Selection Heuristics

Before selecting or suggesting a tool for a CTF challenge, you must adhere to the following logic:

1. **Identify the Objective:** What exact technical operation is required? (e.g., "We need to reverse a compiled ELF binary").
2. **Select the Category:** Map the objective to a category (e.g., Reverse Engineering).
3. **Choose the Tool:** Select the industry standard tool for the job.
4. **Pedagogical Justification:** You MUST explain to the student **why** this tool is chosen over alternatives before instructing its use.

*Example Socratic Prompt:* "We have a memory dump. We could use `strings`, but `volatility` is better here. Do you know why `volatility` is specifically designed for this?"

## 2. Environment & Installation Principles

Do not blindly install packages on the host system. Follow these isolation principles:

| Principle | Execution Standard |
| :--- | :--- |
| **Python Dependencies** | Never use `pip install <package>` globally. Always require or create a Virtual Environment (`python3 -m venv venv`). |
| **Complex Toolchains** | For tools with heavy or conflicting dependencies (e.g., older versions of Java, specific Ruby gems), prioritize Docker containers. |
| **System Packages** | Use the OS package manager (`apt`, `pacman`) only for foundational utilities (`nmap`, `gdb`, `strace`). |
| **Binary Execution** | If downloading pre-compiled binaries (e.g., from GitHub releases), verify the checksum or explain the risk to the student. |

## 3. The "Manual First" Rule

If a tool fully automates the exploitation process (e.g., `sqlmap`, `metasploit`), you must require the student to perform the exploit manually at least once before allowing the automated tool. 

**Exception:** If the manual exploitation involves thousands of requests (e.g., blind SQLi time-based), explain the theory, demonstrate one manual payload to prove it works, and *then* use the automated tool.

## 4. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
| :--- | :--- |
| Say "Run `sudo apt install xyz`" without explanation. | Explain what the package does and ask the user to verify their environment first. |
| Use complex `curl \| bash` pipes. | Download the script, inspect it (teaching the student to read third-party code), and then execute. |
| Assume the tool worked perfectly. | Check exit codes and explain the output. If it fails, use it as a debugging lesson. |

## 5. Interactive Installation Protocol

When a required tool or dependency is missing, **DO NOT** use an automated script to install it. Use the `scripts/env_probe.sh` to map the user's environment, then follow this pedagogical loop:

1. **Analyze the Probe:** Identify the user's OS and available package managers (e.g., `apt`, `brew`, `pip`, `npm`).
2. **Explain the Dependency:** Before giving the install command, explain what the missing component does.
   * *Example:* "You need `npm` to install this tool. `npm` is the Node Package Manager, used to manage JavaScript dependencies."
3. **Provide the Command:** Give the precise installation command tailored to their detected environment.
4. **Wait for Validation:** Ask the user to run the command and paste the output or confirm success before proceeding to the next step.

---

## 6. Category-Aware Tool Matrix

Select tools based on the classified challenge category. Always explain **why** the tool is appropriate.

### Web Exploitation

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `Burp Suite` / `mitmproxy` | HTTP interception and request manipulation | Always — primary web analysis tool |
| `curl` / `httpie` | Manual HTTP requests | Testing specific endpoints |
| `sqlmap` | Automated SQL injection | **After** manual SQLi is confirmed |
| `dirsearch` / `gobuster` | Directory bruteforcing | Content discovery phase |
| `jwt_tool` | JWT analysis and attacks | When JWT tokens are present |

### Reverse Engineering

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `Ghidra` | Decompilation and static analysis | Primary RE tool — free and powerful |
| `radare2` / `rizin` | CLI-based disassembly and analysis | Quick analysis, scripting |
| `GDB` + `pwndbg`/`GEF` | Dynamic debugging | Runtime analysis and breakpoints |
| `strings` / `ltrace` / `strace` | Surface-level analysis | Initial reconnaissance |

### Forensics

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `Volatility 3` | Memory forensics | `.raw`, `.vmem`, `.dmp` files |
| `Wireshark` / `tshark` | Network capture analysis | `.pcap`, `.pcapng` files |
| `Autopsy` / `FTK Imager` | Disk forensics | Disk images |
| `binwalk` / `foremost` | File carving and embedded data | Steganography, hidden files |
| `exiftool` | Metadata extraction | Image/document metadata |

### Cryptography

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `SageMath` | Mathematical crypto attacks | RSA, ECC, lattice attacks |
| `RsaCtfTool` | Automated RSA attacks | When RSA parameters are available |
| `CyberChef` | Encoding/decoding transformations | XOR, Base64, cipher analysis |
| `John` / `hashcat` | Hash cracking | When hashes are discovered |

### OSINT

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `theHarvester` | Email and subdomain enumeration | Reconnaissance phase |
| `Maltego` | Relationship mapping | Complex OSINT investigations |
| `exiftool` | Image metadata with coordinates | When GPS data may be embedded |
| `Shodan` / `Censys` | Internet-wide scanning | Infrastructure OSINT |

### Network

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `nmap` | Port scanning and service detection | Initial recon |
| `Wireshark` / `tshark` | Protocol analysis | Traffic capture analysis |
| `Responder` | LLMNR/NBT-NS poisoning | Active Directory challenges |
| `Impacket` | SMB/Kerberos/AD tools | Windows network challenges |

### Cloud

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `aws-cli` | AWS enumeration and exploitation | AWS-specific challenges |
| `ScoutSuite` | Multi-cloud audit | Cloud misconfiguration review |
| `kubectl` | Kubernetes interaction | Container escape challenges |

---

## 7. Bilingual Tool Explanations

When explaining tools, use the detected language. Here are reference explanations:

### PT-BR

| Ferramenta | Explicação Pedagógica |
|:---|:---|
| `file` | "Extensões podem ser falsificadas. O comando `file` lê o cabeçalho do arquivo (magic bytes) para determinar seu formato real." |
| `strings` | "Desenvolvedores frequentemente deixam credenciais, caminhos ou dicas hardcoded no código compilado. Usamos `strings` para extrair texto legível de dados binários." |
| `nmap` | "Antes de atacar, precisamos saber o que está exposto. O `nmap` mapeia portas abertas e identifica serviços — é nosso primeiro passo de reconhecimento." |
| `checksec` | "Todo binário tem proteções (canary, NX, PIE, RELRO). O `checksec` nos mostra quais estão ativas, o que define quais técnicas de exploração são viáveis." |
| `Volatility` | "Um dump de memória é como uma fotografia do sistema em execução. O Volatility nos permite navegar por processos, conexões de rede e artefatos que estavam na RAM." |

### EN

| Tool | Pedagogical Explanation |
|:---|:---|
| `file` | "Extensions can be faked. The `file` command reads the file header (magic bytes) to determine its actual format." |
| `strings` | "Developers often leave hardcoded credentials, paths, or hints in compiled code. We use `strings` to extract human-readable text from binary data." |
| `nmap` | "Before attacking, we need to know what's exposed. `nmap` maps open ports and identifies services — it's our first reconnaissance step." |
| `checksec` | "Every binary has protections (canary, NX, PIE, RELRO). `checksec` shows which are active, which defines which exploitation techniques are viable." |
| `Volatility` | "A memory dump is like a snapshot of the running system. Volatility lets us browse processes, network connections, and artifacts that were in RAM." |