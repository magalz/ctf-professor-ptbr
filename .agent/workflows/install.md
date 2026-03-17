---
description: Configure the local environment, build the Docker sandbox, and install necessary dependencies. Run this after cloning the repository.
---

# /install — Setup CTF Professor Environment

$ARGUMENTS

---

## Task

### Step 1: Environment Probe (OS & Dependencies)

1. **Invoke** the `security-toolchain-manager` skill to probe the system.
2. **Check for core requirements:**
   - Docker (Required for sandbox)
   - Python 3.8+ (Required for scripts)
   - Git (Required for version control)
3. **Language detection:** Detect the user's language (EN or PT-BR) and respond accordingly.

### Step 2: Docker Sandbox Initialization

1. **Check** if the `cyber-ctf-kali` image exists.
2. **If missing:** Build the image using `.agent/sandbox/Dockerfile`.
   - Command: `docker build -t cyber-ctf-kali .agent/sandbox/`
3. **Verify** image integrity and tool presence inside the container.

### Step 3: Python Dependency Setup

1. **Check** for missing Python libraries used by the system:
   - `mcp` / `fastmcp` (for the sandbox server)
   - `pwntools` (recommended for Pwn challenges)
   - `requests` (for Web challenges)
2. **Offer** to install missing dependencies:
   - Command: `pip install mcp fastmcp pwntools requests`

### Step 4: System Verification

1. **Run** the `.agent/scripts/verify_all.py` script (if applicable) or a subset of it to ensure the environment is ready.
2. **Test** the `sandbox_manager.py` by starting and stopping the container.

### Step 5: Final Configuration

1. **Check** if `mcp_config.json` needs any local path updates.

### Step 6: CTF Platform Connection (Optional)

1. **Link** your CTF accounts to enable automated challenge intake and flag submission.
2. **Select Platform:**
   - **CTFd**: Requires Platform URL and Access Token.
   - **HackTheBox**: Requires App Token (v4).
   - **TryHackMe**: Requires Session Cookie (`connect.sid`).
3. **Guidance:** The agent will provide step-by-step instructions on where to find these tokens for each platform.
4. **Storage:** Credentials are saved securely in a local `.env` file (ignored by Git).

### Step 7: Completion

1. **Confirm** that the user is ready to start their first CTF session with `/start-ctf`.

---

## Usage Examples

```
/install
/install --skip-docker
/install --force-rebuild
```

---

## Rules

- **Transparency:** Always explain what a command does before executing it (especially `docker build` and `pip install`).
- **Safety:** Do not force installations without user consent.
- **Bilingual:** Provide all status messages and prompts in the detected language.
