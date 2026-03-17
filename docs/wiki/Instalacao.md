# ⚙️ Guia de Instalação e Configuração

Configurar o **CTF Professor** é um processo automatizado, mas requer alguns pré-requisitos fundamentais no seu computador.

## 🛠️ Pré-requisitos (No seu Computador Host)

Antes de começar, certifique-se de ter instalado:

1.  **IDE de Desenvolvimento**: Recomendamos o [Antigravity IDE](https://antigravity.google) para uma experiência nativa, ou [VS Code](https://code.visualstudio.com/) com a extensão Gemini Code Assist.
2.  **Docker**: Essencial para rodar o sandbox Kali Linux. Certifique-se de que o daemon do Docker está rodando e seu usuário tem permissão para usá-lo.
3.  **Python 3.8+**: Necessário para rodar os scripts de orquestração localmente.
4.  **Git**: Para clonar o repositório.

---

## 🚀 O Comando Mágico: `/install`

Após clonar o repositório e abrir a pasta na sua IDE, o primeiro comando que você deve executar é:

```
/install
```

### O que o `/install` faz automaticamente?

1.  **Sonda o Ambiente**: Verifica se Docker, Python e Git estão acessíveis.
2.  **Configura o Sandbox Kali**: Constrói (Build) a imagem Docker `cyber-ctf-kali` a partir do `Dockerfile` local. Esta imagem contém todas as ferramentas de segurança pré-configuradas.
3.  **Instala Dependências Python**: Instala bibliotecas como `mcp` (para comunicação IA-Sandbox), `pwntools` e `requests`.
4.  **Valida o Sistema**: Roda scripts de verificação para garantir que a IA consegue dar comandos ao container.

---

## 🐳 Entendendo a Separação Host vs. Sandbox

O sistema foi desenhado para manter seu PC limpo.

- **Host (Seu PC)**: Fica apenas com os scripts leves de Python que servem como o "Cérebro" do sistema.
- **Sandbox (Docker)**: É o "Braço" técnico. Todas as ferramentas pesadas (`nmap`, `gdb`, `wireshark`, etc.) ficam presas dentro do container, isoladas do seu sistema principal.

### Caso ocorra erros no Docker

Se o comando `/install` falhar no passo do Docker, verifique:
- Se o Docker está rodando: `docker ps`.
- No Windows: Use WSL2 como backend do Docker Desktop.
- No Linux: Adicione seu usuário ao grupo docker: `sudo usermod -aG docker $USER`.

---

## ✅ Próximo Passo

Com o ambiente configurado, você está pronto para o seu primeiro desafio. 
👉 [**Aprenda a Usar os Comandos**](Como-Usar)
