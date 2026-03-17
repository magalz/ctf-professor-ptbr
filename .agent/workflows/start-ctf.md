---
description: Inicia a resolução de um novo desafio de CTF. Suporta entrada flexível (texto + arquivos, imagem + arquivos, ou direto). Sempre invoca o agente challenge-classifier antes de iniciar o Ciclo de Aprendizado.
---

# /start-ctf — Iniciar Resolução de CTF

$ARGUMENTS

---

## Modos de Entrada

Este fluxo de trabalho suporta quatro modos de entrada. Detecte automaticamente qual modo foi usado:

| Modo | Exemplo | O que fazer |
|:---|:---|:---|
| **Direto (Bare)** | `/start-ctf` | Peça ao usuário para descrever o desafio e/ou anexar arquivos |
| **Pasta Local** | `/start-ctf CTF1` | Verifique `CTFs/CTF1/` em busca de artefatos e descrição |
| **URL** | `/start-ctf https://ctfd.example.com/...` | Busque metadados e baixe arquivos de plataformas de CTF |
| **Texto + arquivos** | `/start-ctf desafio de injeção SQL...` + arquivos anexados | Extraia a descrição, inventarie os arquivos anexados |
| **Imagem + arquivos** | `/start-ctf` + print da tela + arquivos anexados | Leia a imagem para obter a descrição, inventarie os arquivos anexados |

---

## Tarefa

### Passo 0: Ingestão (TODOS os modos)

1. **Colete os inputs:** Identifique tudo o que estiver disponível — descrição em texto, arquivos anexados, imagens.
2. **Detecção de Pasta Local:** Se o argumento corresponder a uma pasta em `CTFs/`:
   - **Invoque** `.agent/scripts/ingest_local.py`.
   - **Carregue** a descrição e a lista de artefatos.
   - **Inicialização:** Crie um arquivo `notes.md` na pasta (se não existir) para acompanhar o progresso.
   - **Informe** o usuário: "Pasta de CTF local detectada. Ingerindo artefatos e inicializando notes.md..."
3. **Detecção de URL e Ingestão Automatizada:** Se o usuário fornecer uma URL (CTFd, HackTheBox, TryHackMe):
   - **Invoque** a skill `ctf-platform-bridge`.
   - **Busque** os detalhes do desafio via `platform_client.py`.
   - **Baixe** todos os anexos diretamente para o workspace do sandbox.
   - **Informe** o usuário: "URL do(a) [Plataforma] detectada. Buscando detalhes e arquivos do desafio..."
4. **Se for modo direto:** Peça ao usuário para fornecer no mínimo: uma descrição, um arquivo ou um print de tela.
5. **Detecção de idioma:** Detecte o idioma do usuário (EN ou PT-BR).

### Passo 1: Classificação (OBRIGATÓRIO — nunca pule)

1. **Invoque** o agente `challenge-classifier` com todos os inputs coletados.
2. **Apresente** o bloco de classificação ao usuário (Tipo de CTF / Categoria / Classe / Dificuldade / Artefatos / Hipótese / Confiança).
3. **Peça confirmação:** "Does this classification look correct?" / "Essa classificação está correta?"
4. **Aguarde** a confirmação do usuário antes de prosseguir. Se o usuário corrigir, atualize e apresente novamente.

### Passo 2: Análise de Cenário e Triagem

- Orquestre com a skill `ctf-triage-methodology`.
- Use a classificação do Passo 1 para focar a análise no domínio correto.
- Execute `safe_extract.sh` ou análise estática equivalente se um arquivo foi fornecido.
- Formule hipóteses iniciais sem executar payloads dinâmicos.
- **Ação Pedagógica:** Explique o raciocínio por trás de cada observação.

### Passo 3: Preparação do Ambiente e Ferramentas

- Orquestre com a skill `security-toolchain-manager`.
- Determine as ferramentas necessárias para a categoria do desafio identificado.
- Guie o usuário pelo Protocolo de Instalação Interativa se faltarem dependências. Explique o propósito de cada ferramenta.

### Passo 4: Base Teórica e Exploração Controlada

- Orquestre com a skill `controlled-execution-framework`.
- Reforce o "Pedagogical Gate": Explique a teoria da vulnerabilidade antes de construir o payload.
- Use a estrutura `exploit_scaffold.py` quando aplicável.
- Exija que o usuário preveja o resultado antes de executar o exploit.
- Realize "Socratic Debugging" se o exploit falhar.

### Passo 5: Revisão e Mitigação (Após Capturar a Flag)

- Orquestre com a skill `ctf-writeup-architect`.
- **Apresente a Flag**: Mostre explicitamente a flag capturada ao usuário.
- **Submissão**: Instrua o usuário a enviá-la na plataforma de CTF (ou ofereça para fazer isso via `platform_client.py` se configurado).
- **Próximo Passo**: Sugira explicitamente executar `/writeup [Nome_da_Pasta]` para gerar um relatório profissional da sessão, detalhando o impacto corporativo e estratégias de mitigação.

---

## Exemplos de Uso

```
/start-ctf
/start-ctf injeção sql em formulário de login + source.php anexado
/start-ctf Desafio de criptografia RSA com chave fraca + pubkey.pem anexado
/start-ctf [print da tela do CTFd] + binário anexado
/start-ctf web http://10.10.10.10
/start-ctf pwn executavel_vulneravel
/start-ctf pcap captura.pcapng
```

---

## Regras

- **Nunca pule o Passo 1 (Classificação).** Mesmo se o usuário fornecer a categoria explicitamente, rode o classificador para confirmar e enriquecer.
- **Nunca prossiga para o Passo 3 até que o Passo 2 esteja resolvido.**
- **O professor controla o ritmo.** Se o aluno se apressar, imponha o "Socratic Gate".
- **O idioma segue o usuário.** Se eles mudarem para o inglês no meio da sessão, continue em inglês.
