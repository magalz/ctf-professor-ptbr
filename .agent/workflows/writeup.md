---
description: Gera um writeup (relatório) completo de CTF baseado no histórico da sessão ou em uma pasta de desafio local específica.
---

# /writeup - Gerar Relatório de CTF

$ARGUMENTS

---

## Tarefa

Este comando faz a transição da sessão de execução para documentação. Ele produz um writeup de CTF pedagógico e profissional.

### Passos:

1. **Agregação de Contexto**
   - **Verificar Argumento**: Se `$ARGUMENTS` contiver o nome de uma pasta (ex: `CTF01`), leia `CTFs/[Pasta]/notes.md` para reunir o histórico da sessão, descrição e a flag.
   - **Sem Argumento**: Se nenhuma pasta for fornecida, analise o histórico imediato da conversa em busca de comandos bem-sucedidos, vulnerabilidades identificadas e scripts executados.

2. **Geração de Rascunho**
   - Orquestre com a skill `ctf-writeup-architect`.
   - Preencha o template apropriado (PT-BR ou EN) usando o contexto agregado.
   - Certifique-se de que a seção "Real-World Impact & Mitigation" traduza a falha do CTF para um cenário corporativo real.

3. **Saída e Salvamento**
   - **Apresentar**: Mostre um resumo ou o rascunho do writeup para o usuário.
   - **Salvamento Automático**: Se uma pasta foi fornecida no Passo 1, crie e salve automaticamente o relatório markdown completo em `CTFs/[Pasta]/writeup.md`.

4. **Revisão do Usuário (Opcional)**
   - Peça confirmação sobre os payloads exatos usados e se algum passo manual executado fora do chat precisa ser incluído.

---

## Exemplos de Uso

```
/writeup
/writeup CTF01
/writeup foque na mitigação do buffer overflow
```

---

## Antes de Iniciar

Se o CTF ainda não estiver concluído e nenhuma pasta for fornecida, esclareça o escopo:
- Estamos escrevendo um relatório parcial até o nosso progresso atual, ou você capturou a flag fora deste chat?
