---
description: Generate a STRIDE-aligned threat model after flag capture. Maps the CTF vulnerability to enterprise risk with CVSS scoring, attack tree, and remediation plan.
---

# /threat-model - Post-Capture Threat Model

$ARGUMENTS

---

## Task

This command generates a structured threat model based on the vulnerability exploited during the CTF session. It bridges the gap between competitive CTF and real-world security analysis.

### Steps:

1. **Context Gathering**: Review the current session's exploit and classification.
   - If no active session, ask: "Describe the vulnerability you want to model." / "Descreva a vulnerabilidade que deseja modelar."

2. **Generate STRIDE Analysis**:

   ```
   ## Threat Model: [Vulnerability Name]

   ### STRIDE Classification

   | Threat | Applies? | Description |
   |:---|:---|:---|
   | **S**poofing | [Yes/No] | [How identity could be faked] |
   | **T**ampering | [Yes/No] | [How data could be modified] |
   | **R**epudiation | [Yes/No] | [How actions could be denied] |
   | **I**nformation Disclosure | [Yes/No] | [What data is exposed] |
   | **D**enial of Service | [Yes/No] | [How availability is affected] |
   | **E**levation of Privilege | [Yes/No] | [How privileges could escalate] |

   ### CVSS v3.1 Scoring
   [Full CVSS breakdown with justification for each metric]

   ### Attack Tree
   [Mermaid diagram showing attack paths]

   ### Enterprise Impact
   [Where this vulnerability exists in corporate environments]

   ### Remediation Plan
   [Specific fixes at code, infrastructure, and process level]
   ```

3. **Present** in the student's detected language.

4. **Follow-up**: Ask if the student wants to explore defensive measures further.

---

## Usage Examples

```
/threat-model
/threat-model SQL Injection in authentication
/threat-model Buffer overflow no servico de autenticacao
```

---

## Rules

- **Only after flag capture or exploit completion** — this is a post-exploitation educational tool
- **Language follows the session language**
- **STRIDE and CVSS must be fully populated** — no shortcuts
