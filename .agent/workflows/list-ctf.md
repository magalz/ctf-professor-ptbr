---
description: Lista todos os desafios de CTF locais armazenados no diretório CTFs/.
---

# /list-ctf — Gerenciar Desafios Locais

$ARGUMENTS

---

## Tarefa

### Passo 1: Escanear o Diretório CTFs
1. **Invoque** `.agent/scripts/list_ctfs.py`.
2. **Exiba** uma tabela dos desafios encontrados em `CTFs/`.

### Passo 2: Análise
Para cada pasta, mostre:
- **Nome**: O nome da subpasta.
- **Artefatos**: Número total de arquivos.
- **Status**: 
    - `🆕 Novo`: Apenas arquivos, sem anotações (notes).
    - `⏳ Em Progresso`: Contém um arquivo `notes.md`.
    - `🏁 Resolvido`: Contém um arquivo com "flag" no nome.
- **Flag**: A flag encontrada (se o desafio estiver resolvido).

---

## Exemplos de Uso

```
/list-ctf
```

---

## Regras
- **Formatação**: Apresente a lista em um formato de tabela limpo e legível.
- **Estado Vazio**: Se o diretório estiver vazio, encoraje o usuário a criar sua primeira pasta.
