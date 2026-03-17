---
description: Comando de depuração. Ativa o modo DEBUG para investigação sistemática de problemas.
---

# /debug - Investigação Sistemática de Problemas

$ARGUMENTS

---

## Propósito

Este comando ativa o modo DEBUG para investigação sistemática de problemas, erros ou comportamentos inesperados.

---

## Comportamento

Quando `/debug` é acionado:

1. **Coletar informações**
   - Mensagem de erro
   - Passos para reprodução
   - Comportamento esperado vs real
   - Alterações recentes

2. **Formular hipóteses**
   - Listar causas possíveis
   - Ordenar por probabilidade

3. **Investigar sistematicamente**
   - Testar cada hipótese
   - Verificar logs, fluxo de dados
   - Usar método de eliminação

4. **Corrigir e prevenir**
   - Aplicar correção
   - Explicar a causa raiz
   - Adicionar medidas de prevenção

---

## Formato de Saída

```markdown
## 🔍 Debug: [Problema]

### 1. Sintoma
[O que está acontecendo]

### 2. Informações Coletadas
- Erro: `[mensagem de erro]`
- Arquivo: `[caminho do arquivo]`
- Linha: [número da linha]

### 3. Hipóteses
1. ❓ [Causa mais provável]
2. ❓ [Segunda possibilidade]
3. ❓ [Causa menos provável]

### 4. Investigação

**Testando hipótese 1:**
[O que eu verifiquei] → [Resultado]

**Testando hipótese 2:**
[O que eu verifiquei] → [Resultado]

### 5. Causa Raiz
🎯 **[Explicação do por que isso aconteceu]**

### 6. Correção
```[linguagem]
// Antes
[código com problema]

// Depois
[código corrigido]
```

### 7. Prevenção
🛡️ [Como prevenir isso no futuro]
```

---

## Exemplos

```
/debug login nao esta funcionando
/debug API retorna 500
/debug formulario nao envia
/debug dados nao estao salvando
```

---

## Princípios Chave

- **Pergunte antes de assumir** - obtenha o contexto completo do erro
- **Teste hipóteses** - não tente adivinhar aleatoriamente
- **Explique o porquê** - não apenas o que corrigir
- **Previna reincidências** - adicione testes, validação
