---
description: Analisa um artefato binário para engenharia reversa ou exploração. Detecta automaticamente se o binário é um desafio de RE ou Pwn e direciona para o especialista apropriado.
---

# /analyze-binary - Analisar um Artefato Binário

$ARGUMENTS

---

## Tarefa

Este comando realiza uma análise profunda em um arquivo binário e o direciona para o agente especialista apropriado.

### Passos:

1. **Ingestão**: Identifique o arquivo binário anexado.
   - Se nenhum arquivo estiver anexado, pergunte: "Attach the binary file or provide its path." / "Anexe o arquivo binário ou forneça o caminho."

2. **Análise Inicial** (automática):
   - Execute `file <binario>` para identificar o formato
   - Execute `strings -n 6 <binario>` e procure por padrões interessantes
   - Execute `checksec <binario>` (se for ELF) para mapear proteções
   - Apresente o resumo para o aluno

3. **Decisão de Classificação**:
   - Se uma **conexão remota** (nc/socat/port) for fornecida → Direcione para `binary-exploit-engineer` (Pwn)
   - Se **não houver remoto**, e houver palavras-chave como "crack"/"keygen" → Direcione para `reverse-engineering-specialist` (RE)
   - Se ambíguo → Pergunte ao aluno: "Is there a remote service to connect to?" / "Há um serviço remoto para conectar?"

4. **Transferência para Especialista**: Transfira o contexto para o agente especialista apropriado e continue com sua metodologia.

---

## Exemplos de Uso

```
/analyze-binary
/analyze-binary + crackme anexado
/analyze-binary nc ctf.example.com 1337 + binário anexado
/analyze-binary Binário ELF com conexão remota na porta 9999
```

---

## Regras

- **Sempre execute file + strings + checksec antes de qualquer outra coisa.**
- **Nunca execute o binário às cegas** — analise primeiro.
- **O idioma segue o idioma de entrada do usuário.**
