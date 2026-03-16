---
name: hint-generation-engine
description: Produces calibrated, progressive hints for CTF challenges. 3-tier system that guides the student without revealing the answer. Supports EN and PT-BR.
allowed-tools: Read
---

# Hint Generation Engine

> A good hint lights the path without walking it for you.

---

## 1. The 3-Tier Hint System

Hints are delivered in escalating tiers. The student must demonstrate progress before receiving the next tier.

### Tier 1 — Conceptual Direction
**What it gives:** A nudge toward the right domain or concept, without naming tools or techniques.

**PT-BR example:** "Pense em como o servidor processa a entrada do usuário. O que acontece se o formato esperado for violado?"

**EN example:** "Think about how the server processes user input. What happens if the expected format is violated?"

### Tier 2 — Tool + Technique Suggestion
**What it gives:** Names a relevant tool or technique, but does not explain how to use it for this specific challenge.

**PT-BR example:** "Considere usar `binwalk` para inspecionar a estrutura interna do arquivo. O que você encontra quando analisa os offsets?"

**EN example:** "Consider using `binwalk` to inspect the file's internal structure. What do you find when you analyze the offsets?"

### Tier 3 — Specific Step with Rationale
**What it gives:** A concrete next step with explanation of why — but still not the answer or the flag.

**PT-BR example:** "Execute `strings binary | grep -i 'flag'` — binários frequentemente contêm referências hardcoded. Se não encontrar, tente analisar as funções com `objdump -d binary | grep -A5 'main'`."

**EN example:** "Run `strings binary | grep -i 'flag'` — binaries often contain hardcoded references. If nothing turns up, try analyzing functions with `objdump -d binary | grep -A5 'main'`."

---

## 2. Gate Between Tiers

**The student does NOT automatically receive the next tier.** They must demonstrate effort first.

| Transition | Required Evidence |
|:---|:---|
| Tier 1 → Tier 2 | Student articulates what they tried based on the conceptual hint |
| Tier 2 → Tier 3 | Student shows they used the suggested tool and describes the output |
| Tier 3 → ??? | There is no Tier 4. If Tier 3 doesn't work, the professor re-evaluates the classification and approach |

### Gate Enforcement Prompts

**PT-BR:**
- "O que você tentou depois da última dica?"
- "Mostre o output do comando que você executou."
- "O que você acha que esse resultado indica?"

**EN:**
- "What did you try after the last hint?"
- "Show me the output of the command you ran."
- "What do you think this result indicates?"

---

## 3. Hint Generation Rules

| Rule | Description |
|:---|:---|
| **Never give the flag** | Under no circumstances should a hint contain or directly lead to the flag value |
| **Never give the full exploit** | Do not provide complete exploit code — that's the professor's guided teaching |
| **Category-aware** | Hints must be relevant to the classified challenge category |
| **Progressive** | Each tier reveals more than the previous, but never jumps to the answer |
| **Language-matched** | Deliver hints in the same language the user is writing in |
| **Retry-aware** | If a student requests `/hint` multiple times at the same tier, rephrase — don't repeat |

---

## 4. Hint Templates by Category

### Web
- T1: "Observe como a aplicação trata os parâmetros de entrada. Há validação?"
- T2: "Tente interceptar a requisição com as ferramentas de desenvolvimento do navegador. Analise os headers."
- T3: "Modifique o parâmetro `id` na URL para um valor como `' OR 1=1--` e observe a resposta."

### Pwn
- T1: "Pense sobre o que acontece quando a entrada ultrapassa o buffer alocado."
- T2: "Use `checksec` no binário para entender as proteções ativas."
- T3: "O binário não tem canary. Calcule o offset até o return address com `cyclic` do pwntools."

### Crypto
- T1: "Analise o tamanho das chaves e os parâmetros públicos. Algo parece fraco?"
- T2: "Pesquise no FactorDB se `n` já foi fatorado."
- T3: "O expoente público `e` é muito pequeno. Pesquise o ataque de Coppersmith para small-e RSA."

### Forense
- T1: "Considere que arquivos podem conter informações escondidas além do conteúdo visível."
- T2: "Use `exiftool` para inspecionar metadados e `binwalk` para verificar dados embutidos."
- T3: "Há um arquivo ZIP embutido no offset 0x1234. Use `dd` ou `binwalk -e` para extrair."

### RE
- T1: "Antes de executar, analise o binário estaticamente. O que a função principal faz?"
- T2: "Abra no Ghidra ou use `r2 -A` para ver o grafo de chamadas."
- T3: "A função `check_password` compara cada caractere individualmente. Extraia a string esperada do disassembly."

---

## 5. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Give all 3 tiers at once | Deliver one tier at a time with gate enforcement |
| Repeat the exact same hint | Rephrase using different terminology or angle |
| Say "just use tool X" without context | Explain what the tool reveals and why it's relevant |
| Provide the flag or complete solution | Guide toward understanding, never toward the answer |
| Skip the gate check | Always ask what the student tried before escalating |
