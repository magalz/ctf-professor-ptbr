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

### Installation Guide

#### Prerequisites

- [Antigravity IDE](https://antigravity.im) (recommended), [VS Code](https://code.visualstudio.com/), or [Cursor](https://cursor.sh/)
- Git installed and configured
- (Optional) Python 3.8+ for the `classify.py` helper script
- (Optional) CTF tools: `pwntools`, `Ghidra`, `Wireshark`, `Volatility 3`, `hashcat`, etc. — the system will guide you on what's needed per challenge

#### Method 1: Antigravity IDE (Recommended)

Antigravity natively supports the `.agent/` folder structure. Skills, agents, and workflows are loaded automatically.

1. **Install Antigravity IDE** from [antigravity.im](https://antigravity.im):
   - Windows: Download `.exe` installer, run setup wizard
   - macOS: Download `.dmg`, drag to Applications
   - Linux: Follow the package manager instructions on the website

2. **Sign in** with your Google account on first launch

3. **Clone and open the project**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   ```
   Then open the `agentes-ctf` folder in Antigravity: `File > Open Folder`

4. **Done!** Antigravity auto-detects the `.agent/` directory. All 18 agents, 28 skills, and 13 workflows are available immediately. Type `/start-ctf` in the chat to begin.

#### Method 2: VS Code with Gemini Code Assist

1. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install the Gemini Code Assist extension**:
   - Open VS Code
   - Go to Extensions (`Ctrl+Shift+X`)
   - Search for "Gemini Code Assist" and install it
   - Sign in with your Google account

3. **Clone and open the project**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   code agentes-ctf
   ```

4. **Verify**: Open the Gemini chat panel. The `.agent/` folder is auto-detected. Type `/start-ctf` to test.

#### Method 3: Manual Integration (any AI coding tool)

If your tool supports a `.agent/` or `.agents/` directory with markdown-based agent/skill/workflow definitions:

```bash
git clone https://github.com/magalz/agentes-ctf.git
cd agentes-ctf
# The .agent/ folder contains everything — point your tool's workspace here
```

---

### Usage Guide

#### Starting a CTF Session

The `/start-ctf` command supports 3 input modes:

```
# Mode A: Bare — the system will ask for details
/start-ctf

# Mode B: Text + files — describe the challenge and attach files
/start-ctf SQL injection on a login page with MySQL backend
# (attach source files or challenge artifacts)

# Mode C: Image + files — attach a screenshot of the challenge
/start-ctf
# (attach challenge screenshot + binary/source files)
```

The system will automatically:
1. Detect your language (EN or PT-BR)
2. Invoke the `challenge-classifier` to categorize the challenge
3. Route to the appropriate specialist agent
4. Begin the guided learning cycle

#### All Slash Commands

| Command | What It Does | Example |
|:---|:---|:---|
| `/start-ctf` | Begin a CTF learning session | `/start-ctf buffer overflow in ELF binary` |
| `/hint` | Get a progressive hint (3 tiers) | `/hint` |
| `/classify-challenge` | Classify without solving | `/classify-challenge` + attach file |
| `/analyze-binary` | Deep binary analysis | `/analyze-binary` + attach binary |
| `/explain-vulnerability` | Learn about any vulnerability | `/explain-vulnerability SSRF` |
| `/threat-model` | STRIDE threat model after solving | `/threat-model` |
| `/replay-exploit` | Test your retention | `/replay-exploit` |
| `/debug-exploit` | Debug a failing exploit | `/debug-exploit` |
| `/writeup` | Generate a pedagogical report | `/writeup` |

#### Session Flow Example

```
You:    /start-ctf I have a web challenge with a login form
Agent:  [Detects language: EN]
Agent:  [Classifier: Web Exploitation > SQLi > Blind/Error-based]
Agent:  "Let's start with reconnaissance. What do you see when you
         view the page source?"

You:    There's a PHP form posting to login.php
Agent:  "Good. Before using any tool, try submitting a single quote
         in the username field. What happens?"

You:    I get a MySQL error!
Agent:  "Excellent — that confirms error-based SQLi. Can you explain
         WHY the server showed that error?"

...     [Guided exploitation with Socratic gates]

You:    Got the flag! FLAG{sql_1nj3ct10n_m4st3r}
Agent:  "Well done. Now let's understand the real-world impact.
         Use /threat-model to analyze this vulnerability, or
         /writeup to document what you learned."
```

#### Helper Script: classify.py

For quick offline classification:

```bash
# Classify by description
python .agent/skills/ctf-challenge-classifier/scripts/classify.py \
  -d "SQL injection on PHP login page"

# Classify a file
python .agent/skills/ctf-challenge-classifier/scripts/classify.py binary.elf

# Both
python .agent/skills/ctf-challenge-classifier/scripts/classify.py binary.elf \
  -d "200 points, pwn category"
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

### Guia de Instalacao

#### Pre-requisitos

- [Antigravity IDE](https://antigravity.im) (recomendado), [VS Code](https://code.visualstudio.com/) ou [Cursor](https://cursor.sh/)
- Git instalado e configurado
- (Opcional) Python 3.8+ para o script `classify.py`
- (Opcional) Ferramentas CTF: `pwntools`, `Ghidra`, `Wireshark`, `Volatility 3`, etc. — o sistema guia voce sobre o que e necessario por desafio

#### Metodo 1: Antigravity IDE (Recomendado)

O Antigravity suporta nativamente a estrutura `.agent/`. Skills, agentes e workflows sao carregados automaticamente.

1. **Instale o Antigravity IDE** em [antigravity.im](https://antigravity.im):
   - Windows: Baixe o instalador `.exe` e execute o wizard
   - macOS: Baixe o `.dmg` e arraste para Aplicativos
   - Linux: Siga as instrucoes do gerenciador de pacotes no site

2. **Faca login** com sua conta Google no primeiro uso

3. **Clone e abra o projeto**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   ```
   Abra a pasta `agentes-ctf` no Antigravity: `File > Open Folder`

4. **Pronto!** O Antigravity detecta o diretorio `.agent/` automaticamente. Todos os 18 agentes, 28 skills e 13 workflows ficam disponiveis. Digite `/start-ctf` no chat para comecar.

#### Metodo 2: VS Code com Gemini Code Assist

1. **Instale o VS Code** em [code.visualstudio.com](https://code.visualstudio.com/)
2. **Instale a extensao Gemini Code Assist**: Extensions (`Ctrl+Shift+X`) > busque "Gemini Code Assist" > Sign in
3. **Clone e abra**:
   ```bash
   git clone https://github.com/magalz/agentes-ctf.git
   code agentes-ctf
   ```
4. **Verifique**: Abra o painel Gemini e digite `/start-ctf` para testar.

#### Metodo 3: Integracao Manual

```bash
git clone https://github.com/magalz/agentes-ctf.git
cd agentes-ctf
# A pasta .agent/ contem tudo — aponte seu workspace aqui
```

---

### Guia de Uso

#### Iniciando uma Sessao CTF

```
# Modo A: Vazio — o sistema vai pedir detalhes
/start-ctf

# Modo B: Texto + arquivos — descreva o desafio e anexe arquivos
/start-ctf Injecao SQL em pagina de login com MySQL
# (anexe arquivos fonte ou artefatos do desafio)

# Modo C: Imagem + arquivos — anexe screenshot do desafio
/start-ctf
# (anexe screenshot + binario/arquivos fonte)
```

O sistema automaticamente:
1. Detecta seu idioma (EN ou PT-BR)
2. Invoca o `challenge-classifier` para categorizar o desafio
3. Direciona para o agente especialista apropriado
4. Inicia o ciclo de aprendizado guiado

#### Todos os Slash Commands

| Comando | O Que Faz | Exemplo |
|:---|:---|:---|
| `/start-ctf` | Iniciar sessao de aprendizado | `/start-ctf buffer overflow em binario ELF` |
| `/hint` | Dica progressiva (3 niveis) | `/hint` |
| `/classify-challenge` | Classificar sem resolver | `/classify-challenge` + anexar arquivo |
| `/analyze-binary` | Analise profunda de binario | `/analyze-binary` + anexar binario |
| `/explain-vulnerability` | Explicar qualquer vulnerabilidade | `/explain-vulnerability SSRF` |
| `/threat-model` | Modelo de ameacas apos resolver | `/threat-model` |
| `/replay-exploit` | Testar sua retencao | `/replay-exploit` |
| `/debug-exploit` | Debugar exploit falhando | `/debug-exploit` |
| `/writeup` | Gerar relatorio pedagogico | `/writeup` |

#### Exemplo de Fluxo de Sessao

```
Voce:   /start-ctf Tenho um desafio web com formulario de login
Agente: [Detecta idioma: PT-BR]
Agente: [Classificador: Web Exploitation > SQLi > Error-based]
Agente: "Vamos comecar com reconhecimento. O que voce ve quando
         visualiza o codigo-fonte da pagina?"

Voce:   Tem um formulario PHP enviando para login.php
Agente: "Otimo. Antes de usar qualquer ferramenta, tente enviar
         uma aspas simples no campo de usuario. O que acontece?"

Voce:   Apareceu um erro MySQL!
Agente: "Excelente — isso confirma SQLi error-based. Voce consegue
         explicar POR QUE o servidor mostrou esse erro?"

...     [Exploracao guiada com gates socraticas]

Voce:   Peguei a flag! FLAG{sql_1nj3ct10n_m4st3r}
Agente: "Parabens! Agora vamos entender o impacto real.
         Use /threat-model para analisar esta vulnerabilidade, ou
         /writeup para documentar o que voce aprendeu."
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
