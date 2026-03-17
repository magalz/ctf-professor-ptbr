---
description: Vincula suas contas de plataformas de CTF (CTFd, HackTheBox, TryHackMe) para permitir ingestão automatizada de desafios e submissão de flags.
---

# /link-ctf — Conectar Plataformas de CTF

$ARGUMENTS

---

## Tarefa

### Passo 1: Seleção de Plataforma
Pergunte ao usuário qual plataforma ele deseja conectar:
- **CTFd** (Self-hosted ou Cloud)
- **HackTheBox**
- **TryHackMe**

### Passo 2: Configuração Guiada
Forneça instruções específicas com base na escolha:

#### Para CTFd:
1. Faça login na sua instância CTFd.
2. Vá para **Settings** (Configurações) > **Access Tokens** (Tokens de Acesso).
3. Gere um novo token e forneça a **URL da Plataforma** e o **Token**.

#### Para HackTheBox:
1. Faça login em [app.hackthebox.com](https://app.hackthebox.com/).
2. Vá para **Profile Settings** (Configurações de Perfil) > **App Tokens**.
3. Crie um novo token e forneça-o aqui.

#### Para TryHackMe:
1. Faça login em [tryhackme.com](https://tryhackme.com/).
2. Abra o DevTools do navegador (F12) > Application/Storage > Cookies.
3. Encontre o cookie `connect.sid` e forneça o seu valor.

### Passo 3: Persistência
1. Invoque `install_setup.py` (ou um script de integração dedicado) para salvar os valores no arquivo `.env` local.
2. Garanta que o usuário saiba que suas credenciais estão seguras e armazenadas apenas localmente.

### Passo 4: Verificação
1. Teste a conexão buscando um perfil básico ou lista de desafios.
2. Confirme o sucesso: "✅ Conexão estabelecida com o(a) [Plataforma]!"

---

## Regras
- **Nunca** exiba tokens completos na saída do chat.
- **Explique** que o arquivo `.env` é ignorado pelo Git por segurança.
- A detecção de **Idioma** (PT-BR/EN) deve estar ativa.
