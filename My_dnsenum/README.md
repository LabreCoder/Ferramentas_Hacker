# 🔎 DNS Enumeration Tool (Base)

Uma ferramenta simples de **DNS Enumeration** escrita em Python, criada com o objetivo de **entender como funciona a enumeração DNS na prática**, antes de partir para ferramentas mais complexas do mercado.

Este projeto faz parte do estudo de **reconhecimento (recon)** e **levantamento de informações** em ambientes de segurança da informação.

---

## 🎯 Objetivo

- Compreender como consultas DNS funcionam
- Identificar informações expostas por um domínio
- Criar uma base para futuras evoluções (bruteforce, threads, wordlists, etc.)
- Evitar o uso de ferramentas prontas sem entender o funcionamento interno

---

## 🧠 O que a ferramenta faz

A ferramenta consulta e exibe os seguintes registros DNS de um domínio:

- **A** – Endereço IPv4
- **AAAA** – Endereço IPv6
- **MX** – Servidores de e-mail
- **NS** – Servidores de nomes
- **TXT** – Informações textuais (SPF, validações, etc.)

---

## 📦 Requisitos

- Python 3.x
- Biblioteca `dnspython`

Instalação da dependência:
```bash
pip install dnspython
