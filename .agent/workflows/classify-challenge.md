---
description: Executa o pipeline de classificação de desafios sem iniciar o ciclo completo de resolução. Útil para triagem rápida ou autoavaliação.
---

# /classify-challenge — Classificar um Desafio de CTF

$ARGUMENTS

---

## Tarefa

Este comando executa o pipeline de classificação em um desafio de forma independente. Ele NÃO inicia o Ciclo de Aprendizado completo.

### Passos:

1. **Ingestão**: Colete todos os inputs fornecidos (descrição, arquivos, capturas de tela).
   - Se nenhum input for fornecido, pergunte ao usuário: "Describe the challenge or attach the files." / "Descreva o desafio ou anexe os arquivos."

2. **Classificar**: Invoque o agente `challenge-classifier`.
   - Analise texto, arquivos (magic bytes, extensões) e imagens (texto visível).
   - Produza o bloco de classificação de 3 níveis (Tipo de CTF / Categoria / Classe / Dificuldade / Artefatos / Hipótese / Confiança).

3. **Apresentar**: Exiba o bloco de classificação para o usuário.

4. **Parar**: NÃO prossiga para a triagem ou exploração. Se o usuário quiser continuar, sugira o uso de `/start-ctf`.

---

## Exemplos de Uso

```
/classify-challenge
/classify-challenge Arquivo anexado: misterioso.bin
/classify-challenge Desafio de 200 pontos, categoria não informada
/classify-challenge [print da página do desafio]
```

---

## Regras

- **Apenas classificação.** Este workflow não aciona o Ciclo de Aprendizado.
- **O idioma segue o usuário.**
