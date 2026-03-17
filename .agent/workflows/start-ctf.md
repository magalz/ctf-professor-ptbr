---
description: Start new CTF challenge resolution. Supports flexible input (text + files, image + files, or bare). Always invokes the challenge-classifier agent before starting the Learning Cycle.
---

# /start-ctf — Start CTF Resolution

$ARGUMENTS

---

## Input Modes

This workflow supports three input modes. Detect automatically which mode was used:

| Mode | Example | What to do |
|:---|:---|:---|
| **Bare** | `/start-ctf` | Ask the user to describe the challenge and/or attach files |
| **Text + files** | `/start-ctf SQL injection challenge on a login page` + attached binary/source | Extract description, inventory attached files |
| **Image + files** | `/start-ctf` + screenshot of CTFd challenge page + attached files | Read screenshot for title/tags/description, inventory attached files |

---

## Task

### Step 0: Intake (ALL modes)

1. **Collect inputs:** Identify everything available — text description, attached files (list names and types), images (read visible text from screenshots).
2. **URL Detection & Automated Intake:** If the user provides a URL (CTFd, HackTheBox, TryHackMe):
   - **Invoke** the `ctf-platform-bridge` skill.
   - **Fetch** challenge title, description, and category via `platform_client.py`.
   - **Download** all attachments directly to the sandbox workspace.
   - **Inform** the user: "Detected [Platform] URL. Fetching challenge details and files..."
3. **If bare mode:** Ask the user to provide at minimum: a description of the challenge OR a file OR a screenshot. Do not proceed without at least one input.
4. **Language detection:** Detect the user's language (EN or PT-BR) from their message text. Respond in the same language throughout the session.

### Step 1: Classification (MANDATORY — never skip)

1. **Invoke** the `challenge-classifier` agent with all collected inputs.
2. **Present** the classification block to the user (CTF Type / Category / Class / Difficulty / Artifacts / Hypothesis / Confidence).
3. **Ask for confirmation:** "Does this classification look correct?" / "Essa classificação está correta?"
4. **Wait** for user confirmation before proceeding. If the user corrects, update and re-present.

### Step 2: Scenario Analysis & Triage

- Orchestrate with `ctf-triage-methodology` skill.
- Use the classification from Step 1 to focus the analysis on the correct domain.
- Run `safe_extract.sh` or equivalent static analysis if a file was provided.
- Formulate initial hypotheses without executing any dynamic payloads.
- **Pedagogical Action:** Explain the reasoning behind each observation.

### Step 3: Environment & Toolchain Preparation

- Orchestrate with `security-toolchain-manager` skill.
- Determine required tools for the identified challenge category.
- Guide the user through the Interactive Installation Protocol if dependencies are missing. Explain the purpose of each tool.

### Step 4: Theoretical Foundation & Controlled Exploitation

- Orchestrate with `controlled-execution-framework` skill.
- Enforce the Pedagogical Gate: Explain the vulnerability theory before building the payload.
- Use the `exploit_scaffold.py` structure when applicable.
- Require the user to predict the outcome before executing the exploit.
- Perform Socratic Debugging if the exploit fails.

### Step 5: Review & Mitigation (Upon Flag Capture)

- Orchestrate with `ctf-writeup-architect` skill.
- Consolidate the session history and successful commands into the `writeup_base.md` template.
- Detail the real-world enterprise impact and mitigation strategies.

---

## Usage Examples

```
/start-ctf
/start-ctf SQL injection on a login form + attached source.php
/start-ctf Desafio de criptografia RSA com chave fraca + attached pubkey.pem
/start-ctf [screenshot of CTFd challenge page] + attached binary
/start-ctf web http://10.10.10.10
/start-ctf pwn vulnerable_binary
/start-ctf pcap capture.pcapng
```

---

## Rules

- **Never skip Step 1 (Classification).** Even if the user provides the category explicitly, run the classifier to confirm and enrich.
- **Never proceed to Step 3 until Step 2 is fully resolved.**
- **The professor controls pacing.** If the student rushes, enforce the Socratic Gate.
- **Language follows the user.** If they switched to English mid-session, continue in English.