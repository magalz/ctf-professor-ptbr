---
description: Request a calibrated hint for the current CTF challenge without receiving the answer. Uses the 3-tier progressive hint system.
---

# /hint — Request a Hint

$ARGUMENTS

---

## Task

This command produces a calibrated, progressive hint based on the current challenge context.

### Steps:

1. **Context Check**: Identify the current challenge category and what the student has already tried.
   - If no CTF session is active, respond: "No active CTF session. Use /start-ctf first." / "Nenhuma sessão CTF ativa. Use /start-ctf primeiro."

2. **Determine Tier**: Check which hint tier the student is on:
   - **First `/hint`** → Deliver Tier 1 (Conceptual Direction)
   - **Second `/hint`** → Enforce gate: ask what they tried → If evidence shown, deliver Tier 2 (Tool + Technique)
   - **Third `/hint`** → Enforce gate: ask for tool output → If shown, deliver Tier 3 (Specific Step)
   - **Beyond Tier 3** → Re-evaluate classification or suggest a different approach

3. **Deliver Hint**: Use the `hint-generation-engine` skill to generate the hint in the detected language.

4. **Gate Check**: After delivering the hint, prompt the student to act on it before providing more help.

---

## Usage Examples

```
/hint
/hint estou travado na parte de criptografia
/hint I can't figure out the vulnerability type
```

---

## Rules

- **Never provide the flag or full exploit code via hints.**
- **Always check what the student already tried before escalating.**
- **Language follows the user's input language.**
