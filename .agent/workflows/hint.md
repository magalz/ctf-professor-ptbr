---
description: Solicite uma dica calibrada para o desafio de CTF atual sem receber a resposta direta. Usa o sistema de dicas progressivas de 3 níveis.
---

# /hint — Solicitar uma Dica

$ARGUMENTS

---

## Tarefa

Este comando produz uma dica calibrada e progressiva baseada no contexto atual do desafio.

### Passos:

1. **Verificação de Contexto**: Identifique a categoria atual do desafio e o que o aluno já tentou.
   - Se nenhuma sessão de CTF estiver ativa, responda: "No active CTF session. Use /start-ctf first." / "Nenhuma sessão CTF ativa. Use /start-ctf primeiro."

2. **Determinar Nível (Tier)**: Verifique em qual nível de dica o aluno está:
   - **Primeiro `/hint`** → Entregue Nível 1 (Direção Conceitual)
   - **Segundo `/hint`** → Imponha "gate": pergunte o que eles tentaram → Se mostrarem evidências, entregue Nível 2 (Ferramenta + Técnica)
   - **Terceiro `/hint`** → Imponha "gate": peça a saída da ferramenta → Se mostrada, entregue Nível 3 (Passo Específico)
   - **Além do Nível 3** → Reavalie a classificação ou sugira uma abordagem diferente

3. **Entregar Dica**: Use a skill `hint-generation-engine` para gerar a dica no idioma detectado.

4. **Verificação (Gate Check)**: Após entregar a dica, incentive o aluno a agir sobre ela antes de fornecer mais ajuda.

---

## Exemplos de Uso

```
/hint
/hint estou travado na parte de criptografia
/hint não consigo descobrir o tipo de vulnerabilidade
```

---

## Regras

- **Nunca forneça a flag ou o código completo do exploit através das dicas.**
- **Sempre verifique o que o aluno já tentou antes de escalar o nível.**
- **O idioma segue o idioma de entrada do usuário.**
