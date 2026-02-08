import dns.resolver

def dns_enum(domain):
    records = ["A", "AAAA", "MX", "NS", "TXT"] # Aqui podemos ao invés de utilizar uma lista direta no python, podemos ler um arquivo de listas para testar os subdominios.

    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n[+] {record} records:")
            for rdata in answers:
                print(f"  - {rdata}")
        except Exception:
            print(f"\n[-] {record} records not found")

if __name__ == "__main__":
    target = input("Digite o domínio: ")
    dns_enum(target)
