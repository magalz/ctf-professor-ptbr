# CTF Professor - Cybersecurity Education Agent System

> **Um sistema de agentes de IA focado em ensinar ciberseguranca atraves de CTF, nao apenas em resolver desafios.**
>
> **An AI agent system focused on teaching cybersecurity through CTF, not just solving challenges.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: PT-BR](https://img.shields.io/badge/Idioma-PT--BR-009c3b)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-EN-blue)](README.md)
[![Antigravity](https://img.shields.io/badge/Powered%20by-Antigravity-red)](https://antigravity-kit.unikorn.vn)
[![Forked from](https://img.shields.io/badge/Forked%20from-sickn33%2Fantigravity--awesome--skills-lightgrey)](https://github.com/sickn33/antigravity-awesome-skills)

---

## Idioma / Language

- [Portugues Brasileiro](#portugues-brasileiro) ← *Idioma principal*
- [English](#english) ← *Primary documentation reference*

---

## English

### What is this?

**CTF Professor** is a cybersecurity educational environment built on the [Antigravity Kit](https://antigravity-kit.unikorn.vn) framework, originally forked from [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills).

Unlike tools that solve challenges automatically, this system behaves like a **Cybersecurity Professor**:

- It **teaches**, not just solves
- It **guides** through structured reasoning
- It **challenges** your thinking with Socratic questions
- It **enforces** a learning methodology before allowing execution
- It **connects** CTF vulnerabilities to real-world enterprise security
- It **auto-detects** your language (EN/PT-BR) and responds accordingly

### Core Philosophy

> *"Do not just teach how to find the flag; teach the understanding of the vulnerability that allowed it to exist."*

### The Learning Cycle

Every CTF session follows a structured 7-phase learning cycle:

```
1. CLASSIFICATION         -> 3-tier challenge taxonomy (Type/Category/Class)
2. SCENARIO ANALYSIS      -> Categorize the challenge, form initial hypotheses
3. GUIDED RECONNAISSANCE  -> Identify attack vectors with pedagogical explanations
4. THEORETICAL FOUNDATION -> Understand the vulnerability before touching any tool
5. CONTROLLED EXPLOITATION -> Build the exploit step-by-step with Socratic gates
6. FLAG ACQUISITION        -> Validate success; explain what the flag represents
7. MITIGATION & WRITEUP   -> Translate the flaw to enterprise risk and remediation
```

### Agent System (18 agents)

#### CTF Specialist Agents

| Agent | Role |
|:---|:---|
| `ctf-professor` | Lead orchestrator - Socratic educator and pedagogical gatekeeper |
| `challenge-classifier` | 3-tier classification (Type/Category/Class) on every session |
| `reverse-engineering-specialist` | Static-first binary analysis with assembly-level guidance |
| `binary-exploit-engineer` | Theory-Predict-Execute-Verify exploitation cycle |
| `crypto-analyst` | Mathematical cipher analysis, identification-first |
| `forensics-analyst` | PCAP, memory, stego, disk - triage before extraction |
| `malware-sandbox-analyst` | Justification-driven safe malware analysis |
| `security-auditor` | Code review and vulnerability assessment |
| `penetration-tester` | Full engagement simulation |

#### Support Agents

`orchestrator`, `project-planner`, `debugger`, `explorer-agent`, `code-archaeologist`, `documentation-writer`, `product-manager`, `product-owner`, `test-engineer`

### Skill Stack (28 skills)

#### CTF Domain Skills

| Skill | Purpose |
|:---|:---|
| `ctf-challenge-classifier` | 3-tier taxonomy + decision tree + `classify.py` script |
| `ctf-triage-methodology` | Pedagogical recon (Phase A-D) + bilingual Socratic prompts |
| `hint-generation-engine` | 3-tier progressive hints with gate enforcement |
| `reverse-engineering-analysis` | 4-phase RE pipeline (identify/disassemble/decompile/dynamic) |
| `binary-exploitation-guide` | 6 exploit classes + protection bypass + `rop_chain_scaffold.py` |
| `web-exploitation-methodology` | Manual-first rule, OWASP matrix, SQLi/XSS/SSTI deep dives |
| `cryptography-analysis` | Cipher ID, RSA/AES/hash attack tables, math-first |
| `forensics-investigation` | PCAP (Wireshark), memory (Volatility 3), stego, disk, carving |
| `osint-methodology` | Passive-first pipeline, ethical boundaries |
| `malware-sandboxing` | Docker isolation, behavioral analysis, IoC extraction |
| `security-toolchain-manager` | Category-aware tool matrix (7 domains) |
| `controlled-execution-framework` | Exploit scaffolds with Theory-Predict-Execute-Verify |
| `ctf-writeup-architect` | CVSS/CVE mapping + bilingual templates |

### Workflows (13 slash commands)

#### CTF Workflows

| Command | Purpose |
|:---|:---|
| `/start-ctf` | Start the learning cycle (3 input modes: bare / text+files / image+files) |
| `/classify-challenge` | Standalone challenge classification |
| `/hint` | Progressive 3-tier hint with gate enforcement |
| `/analyze-binary` | Deep binary analysis - auto-routes to RE or Pwn specialist |
| `/explain-vulnerability` | Pure educational explanation of any vulnerability class |
| `/threat-model` | Post-capture STRIDE threat model with CVSS |
| `/replay-exploit` | Retention test - reproduce and explain a completed exploit |
| `/debug-exploit` | Socratic debugging when an exploit fails |
| `/writeup` | Generate pedagogical writeup after flag capture |

#### Support Workflows

`/brainstorm`, `/debug`, `/orchestrate`, `/plan`

### Project Structure

```
.agent/
├── agents/              # 18 specialist agent definitions
├── skills/              # 28 skill modules (SKILL.md + scripts/templates)
│   ├── ctf-challenge-classifier/
│   │   ├── SKILL.md
│   │   └── scripts/classify.py
│   ├── binary-exploitation-guide/
│   │   ├── SKILL.md
│   │   └── templates/rop_chain_scaffold.py
│   ├── ctf-writeup-architect/
│   │   └── templates/
│   │       ├── writeup_base.md
│   │       └── writeup_base_ptbr.md
│   └── ...
├── workflows/           # 13 slash command definitions
├── rules/
│   └── GEMINI.md        # Global rules + language detection (R2)
├── scripts/             # Utility scripts
├── ARCHITECTURE.md      # Full system reference
└── SECURITY.md          # Security policies
```

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   cd agentes-ctf
   ```

2. **Start a CTF session** (supports multiple input modes):
   ```
   /start-ctf
   /start-ctf SQL injection on a login page
   /start-ctf [attach screenshot + binary file]
   /start-ctf web http://10.10.10.10
   /start-ctf pwn vulnerable_binary
   ```

3. **When stuck**, ask for a hint:
   ```
   /hint
   ```

4. **Learn about any vulnerability**:
   ```
   /explain-vulnerability buffer overflow
   /explain-vulnerability SQL Injection
   ```

### CTF Categories Supported

| Category | Skill | Classes |
|:---|:---|:---|
| Web | `web-exploitation-methodology` | SQLi, XSS, SSRF, SSTI, IDOR, JWT, XXE, Race Conditions |
| Pwn | `binary-exploitation-guide` | BOF, ROP, Heap (UAF, Tcache), Format String, Kernel |
| RE | `reverse-engineering-analysis` | Anti-debug, Obfuscation, Decompilation, Symbolic Execution |
| Crypto | `cryptography-analysis` | RSA, AES, ECC, Hash, XOR, Padding Oracle |
| Forensics | `forensics-investigation` | Memory (Volatility), PCAP, Stego, Disk, Carving |
| OSINT | `osint-methodology` | Geolocation, SOCMINT, Dorking, Metadata |
| Cloud | (via classifier) | S3, IAM, Lambda, K8s/Docker Escapes |
| AI/ML | (via classifier) | Prompt Injection, Adversarial Attacks |
| Hardware | (via classifier) | Firmware, JTAG/UART, Side-channel |

---

## Portugues Brasileiro

### O que e isso?

**CTF Professor** e um ambiente educacional de ciberseguranca construido sobre o framework [Antigravity Kit](https://antigravity-kit.unikorn.vn), originalmente um fork do [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills).

Diferente de ferramentas que resolvem desafios automaticamente, este sistema se comporta como um **Professor de Ciberseguranca**:

- Ele **ensina**, nao apenas resolve
- Ele **guia** por raciocinio estruturado
- Ele **desafia** seu pensamento com perguntas socraticas
- Ele **aplica** uma metodologia de aprendizado antes de permitir a execucao
- Ele **conecta** vulnerabilidades do CTF com seguranca corporativa real
- Ele **detecta automaticamente** seu idioma (EN/PT-BR) e responde adequadamente

### Filosofia Central

> *"Nao ensine apenas como encontrar a flag; ensine a compreensao da vulnerabilidade que permitiu sua existencia."*

### O Ciclo de Aprendizado

```
1. CLASSIFICACAO          -> Taxonomia 3 niveis (Tipo/Categoria/Classe)
2. ANALISE DO CENARIO     -> Categorizar o desafio, formular hipoteses
3. RECONHECIMENTO GUIADO  -> Identificar vetores de ataque com explicacoes
4. BASE TEORICA           -> Compreender a vulnerabilidade antes de usar ferramentas
5. EXPLORACAO CONTROLADA  -> Construir o exploit passo a passo com gates socraticas
6. CAPTURA DA FLAG        -> Validar sucesso; explicar o que a flag representa
7. MITIGACAO E WRITEUP    -> Traduzir a falha para risco corporativo e remediacao
```

### Sistema de Agentes (18 agentes)

| Agente | Funcao |
|:---|:---|
| `ctf-professor` | Orquestrador principal - educador socratico |
| `challenge-classifier` | Classificacao 3 niveis em cada sessao |
| `reverse-engineering-specialist` | Analise binaria estatica-primeiro |
| `binary-exploit-engineer` | Ciclo Teoria-Prever-Executar-Verificar |
| `crypto-analyst` | Analise matematica de cifras |
| `forensics-analyst` | PCAP, memoria, stego, disco |
| `malware-sandbox-analyst` | Analise segura de malware |
| `security-auditor` | Revisao de codigo e avaliacao de vulnerabilidades |
| `penetration-tester` | Simulacao de engajamento completo |

### Fluxos de Trabalho (Slash Commands)

| Comando | Proposito |
|:---|:---|
| `/start-ctf` | Iniciar sessao (3 modos: vazio / texto+arquivos / imagem+arquivos) |
| `/classify-challenge` | Classificacao standalone de desafio |
| `/hint` | Dica progressiva 3 niveis com gate |
| `/analyze-binary` | Analise profunda de binario |
| `/explain-vulnerability` | Explicacao educacional pura |
| `/threat-model` | Modelo de ameacas STRIDE pos-captura |
| `/replay-exploit` | Teste de retencao - reproduzir e explicar |

### Como Comecar

1. **Clone o repositorio**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   cd agentes-ctf
   ```

2. **Inicie uma sessao CTF**:
   ```
   /start-ctf
   /start-ctf Injecao SQL em pagina de login
   /start-ctf pwn binario_vulneravel
   ```

3. **Quando travar**, peca uma dica:
   ```
   /hint
   ```

---

## Credits / Creditos

| Project | Role |
|:---|:---|
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | Original upstream skills repository |
| [Antigravity Kit](https://antigravity-kit.unikorn.vn) | Agent/Skill/Workflow framework |

All upstream work retains its original MIT License. This project's CTF-specific additions are also MIT licensed.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
