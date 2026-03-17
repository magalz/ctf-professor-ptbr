# ARCHITECTURE.md - CTF Professor System

> Complete architectural reference for the CTF Professor agent ecosystem.

---

## System Overview

The CTF Professor system is a pedagogical cybersecurity environment built on the Antigravity Kit framework. It uses specialized agents, skills, and workflows to teach CTF methodology through Socratic questioning and guided learning.

**Languages:** EN + PT-BR (auto-detected per message, default PT-BR)

---

## Directory Structure

```
.agent/
├── agents/           # 18 agent definitions
├── skills/           # 28 skill modules (SKILL.md + scripts/templates)
├── workflows/        # 13 slash commands
├── rules/
│   └── GEMINI.md     # Global behavior rules + language detection
├── scripts/          # Global utility scripts
├── ARCHITECTURE.md   # This file
└── SECURITY.md       # Security policies
```

---

## Agent Roster

### CTF Core Agents (Built for this project)

| Agent | Role | Key Skills | Triggers |
|:---|:---|:---|:---|
| `ctf-professor` | **Primary orchestrator** for CTF learning sessions | triage, toolchain, execution, writeup, classifier, hints | ctf, challenge, flag, lesson |
| `challenge-classifier` | First agent in every session — 3-tier classification | ctf-challenge-classifier, triage | classify, triage, category |
| `reverse-engineering-specialist` | Static-first binary analysis | RE analysis, triage, toolchain | reverse, decompile, ghidra, crackme |
| `binary-exploit-engineer` | Memory corruption exploitation | binary exploitation, controlled execution, RE | pwn, exploit, buffer overflow, rop |
| `crypto-analyst` | Mathematical cipher analysis | cryptography-analysis, triage, toolchain | crypto, cipher, rsa, aes, hash |
| `forensics-analyst` | Digital evidence investigation | forensics-investigation, triage, toolchain | forensics, pcap, memory, stego |
| `malware-sandbox-analyst` | Safe malware analysis | malware-sandboxing, RE analysis, toolchain | malware, sandbox, suspicious |

### Security Agents (From original project, retained)

| Agent | Role |
|:---|:---|
| `security-auditor` | Code security review and vulnerability assessment |
| `penetration-tester` | Offensive security testing methodology |

### Support Agents (From original project, retained)

| Agent | Role |
|:---|:---|
| `orchestrator` | Multi-agent coordination |
| `project-planner` | 4-phase project methodology |
| `debugger` | Bug diagnosis and resolution |
| `explorer-agent` | Codebase analysis and navigation |
| `code-archaeologist` | Legacy code understanding |
| `documentation-writer` | Technical writing |
| `product-manager` | Feature prioritization |
| `product-owner` | Requirements and acceptance |
| `test-engineer` | Testing strategy |

---

## Skill Stack

### CTF Domain Skills (Built for this project)

| Skill | Category | Purpose |
|:---|:---|:---|
| `ctf-challenge-classifier` | Classification | 3-tier taxonomy (Type/Category/Class) + decision tree + `classify.py` |
| `ctf-triage-methodology` | Triage | Phase A-D analysis pipeline + bilingual Socratic prompts |
| `hint-generation-engine` | Pedagogy | 3-tier progressive hints with gate enforcement |
| `reverse-engineering-analysis` | RE | 4-phase pipeline (identify/disassemble/decompile/dynamic) |
| `binary-exploitation-guide` | Pwn | 6 exploitation classes + protection bypass + `rop_chain_scaffold.py` |
| `web-exploitation-methodology` | Web | Manual-first rule, OWASP matrix, SQLi/XSS/SSTI deep dives |
| `cryptography-analysis` | Crypto | Cipher ID, RSA/AES/hash attack tables, math-first |
| `forensics-investigation` | Forensics | PCAP, memory (Volatility 3), stego, disk, carving |
| `osint-methodology` | OSINT | Passive-first pipeline, ethical boundaries |
| `malware-sandboxing` | Malware | Docker isolation, behavioral analysis, IoC extraction |
| `security-toolchain-manager` | Toolchain | Category-aware tool matrix (7 domains) + PT-BR explanations |
| `controlled-execution-framework` | Exploitation | `exploit_scaffold.py` + iterative Theory-Predict-Execute-Verify |
| `ctf-writeup-architect` | Documentation | CVSS/CVE mapping + bilingual templates (EN/PT-BR) |

### Support Skills (From original project, retained)

| Skill | Purpose |
|:---|:---|
| `clean-code` | Code quality standards |
| `brainstorming` | Socratic questioning framework |
| `intelligent-routing` | Agent auto-selection |
| `i18n-localization` | Internationalization patterns |
| `red-team-tactics` | Offensive methodology |
| `vulnerability-scanner` | Automated security scanning |
| `code-review-checklist` | Code review standards |
| `architecture` | System architecture patterns |
| `bash-linux` | Shell scripting reference |
| `powershell-windows` | PowerShell reference |
| `python-patterns` | Python best practices |
| `testing-patterns` | Test methodology |
| `behavioral-modes` | Agent behavior configuration |
| `parallel-agents` | Multi-agent coordination |
| `plan-writing` | Task planning methodology |

---

## Workflow Quick Reference

### CTF Workflows (Built for this project)

| Command | Purpose | Key Agent |
|:---|:---|:---|
| `/install` | Setup environment, build Docker, install dependencies | orchestrator / support |
| `/start-ctf` | Start CTF resolution (3 input modes, mandatory classification) | ctf-professor |
| `/classify-challenge` | Standalone classification without solving | challenge-classifier |
| `/hint` | Progressive hint (3-tier with gate) | ctf-professor |
| `/analyze-binary` | Binary analysis → auto-route RE or Pwn | RE/Pwn specialist |
| `/explain-vulnerability` | Pure educational explanation (no CTF context) | ctf-professor |
| `/threat-model` | Post-capture STRIDE threat model | ctf-professor |
| `/replay-exploit` | Retention test — reproduce and explain | ctf-professor |

### Support Workflows (From original project, retained)

| Command | Purpose |
|:---|:---|
| `/brainstorm` | Socratic ideation session |
| `/debug` | Bug diagnosis workflow |
| `/debug-exploit` | Exploit debugging |
| `/orchestrate` | Multi-agent task coordination |
| `/plan` | Project planning |
| `/writeup` | Generate CTF writeup |

---

## Input Model: `/start-ctf`

```
USER INPUT
│
├── Mode A: Bare ("/start-ctf")
│   └── Ask for description or files
│
├── Mode B: Text + Files ("/start-ctf SQL injection..." + source.php)
│   └── Extract description + inventory files
│
└── Mode C: Image + Files ("/start-ctf" + screenshot + binary)
    └── Read screenshot text + inventory files

         ↓

┌─────────────────────────┐
│  challenge-classifier   │ ← ALWAYS invoked
│  (3-tier classification)│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│  User confirms or       │
│  corrects classification│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│  ctf-professor          │
│  Learning Cycle begins  │
│  (Triage → Toolchain →  │
│   Exploitation →        │
│   Writeup)              │
└─────────────────────────┘
```

---

## Agent Delegation Map

```
ctf-professor (orchestrator)
├── challenge-classifier ← classification
├── reverse-engineering-specialist ← RE challenges
│   └── binary-exploit-engineer ← if remote service found
├── binary-exploit-engineer ← Pwn challenges
│   └── reverse-engineering-specialist ← needs deeper static RE
├── crypto-analyst ← Crypto challenges
├── forensics-analyst ← Forensics challenges
│   └── reverse-engineering-specialist ← if malware found in evidence
├── malware-sandbox-analyst ← suspicious binaries
│   └── reverse-engineering-specialist ← for deep RE
└── security-auditor / penetration-tester ← code review / pentest
```

---

## Language Detection (R2)

- Auto-detected per message (EN or PT-BR)
- Default on ambiguity: **PT-BR**
- Code/commands stay in English
- Security jargon may stay in English within PT-BR
- All Socratic prompts have bilingual variants
