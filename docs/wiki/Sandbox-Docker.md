# 🐳 O Sandbox Kali Linux (Docker)

O **CTF Professor** utiliza um ambiente isolado para garantir que qualquer comando executado pela IA não afete seu computador host. Este isolamento é feito através do **Docker**.

---

## 🛠️ O que há no Sandbox?

A imagem Docker (`cyber-ctf-kali`) é baseada no **Kali Linux Rolling** e vem pré-configurada com as ferramentas essenciais para as categorias mais comuns de CTF:

- **Rede e Recon**: `nmap`, `iproute2`, `curl`, `openvpn`.
- **Análise Binária**: `gdb`, `radare2`, `checksec`, `strace`, `ltrace`, `binutils`.
- **Ambiente de Scripting**: Python 3.10+ pré-configurado com bibliotecas para Pwn e Exploit dev.

---

## 🛡️ Segurança e Isolamento

O sistema de orquestração (`sandbox_manager.py`) utiliza várias flags de segurança ao subir o container:

- **Rede Bridge**: O container tem acesso à internet para desafios que exigem conexão externa, mas está isolado da sua rede local (LAN).
- **Capacidades Específicas**: Habilitamos apenas o necessário (`NET_RAW` para nmap, `SYS_PTRACE` para gdb) em vez de rodar o container como `--privileged`.
- **Seccomp Unconfined**: Permitimos depuração (`ptrace`) para que você possa usar o GDB sem bloqueios do kernel.
- **Limites de Recursos**: O container é efêmero (`--rm`), o que significa que ele é destruído ao ser parado, garantindo que nenhum resíduo de malware persista entre as sessões.

---

## 📂 Volumes e Montagem de Arquivos

Quando você inicia um desafio com arquivos, o sistema monta a pasta do projeto como um **Volume Docker** no caminho `/workspace`.

- **Isso significa que**: Quaisquer alterações feitas pela IA em arquivos dentro do `/workspace` no container aparecerão instantaneamente na sua pasta local no Windows/Mac/Linux.
- **Cuidado**: Embora o container esteja isolado, arquivos que a IA escreve no `/workspace` são reais. Nunca anexe arquivos confidenciais da sua empresa em uma sessão de CTF.

---

## 🔧 Personalizando o Sandbox

Se você precisar de ferramentas extras (ex: `Ghidra`, `Wireshark`, `Sqlmap`), você pode:

1.  **Instalar via Terminal**: Use o comando de execução da IA para rodar um `apt install` dentro do container ativo.
2.  **Modificar o Dockerfile**: Altere o arquivo `.agent/sandbox/Dockerfile` e rode `/install --force-rebuild`.

---

## 🔗 Próximo Passo
👉 [**Retornar para a Home**](Home)
