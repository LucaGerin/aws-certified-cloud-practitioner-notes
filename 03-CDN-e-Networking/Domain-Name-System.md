--> [AWS](00-Intro/AWS.md)  -  [CDN e Networking](03-CDN-e-Networking/Rete-globale-AWS.md)
# Domain Name System (DNS)

Il **DNS (Domain Name System)** è un sistema fondamentale di Internet che **traduce i nomi di dominio leggibili dagli esseri umani** (es. `www.example.com`) negli **indirizzi IP** comprensibili dai computer (es. `192.0.2.1`). In pratica, è come una **rubrica telefonica di Internet**.

---

## Come funziona il DNS

1. L'utente digita un dominio nel browser (`www.example.com`).
2. Il computer interroga un **resolver DNS** locale (di solito fornito dal provider internet).
3. Il resolver interroga una serie di server DNS, fino a trovare l’indirizzo IP associato.
4. L’indirizzo IP viene restituito al browser, che può ora connettersi al sito web.

![dns](dns.png)

---

## Tipi di record DNS comuni

|Tipo|Descrizione|
|---|---|
|`A`|Associa un nome di dominio a un indirizzo IPv4|
|`AAAA`|Associa un nome a un indirizzo IPv6|
|`CNAME`|Alias per un altro nome di dominio|
|`MX`|Specifica i server di posta per il dominio|
|`TXT`|Testi liberi, usati per SPF, DKIM, verifiche|
|`NS`|Indica i name server autoritativi del dominio|
|`SRV`|Specifica servizi disponibili su porte specifiche|
|`PTR`|Record inverso, da IP a nome|

---

## Gerarchia del DNS

- **Root DNS Server:** in cima alla gerarchia (`.`)
- **Top-Level Domain (TLD):** gestisce estensioni come `.com`, `.org`, `.it`
- **Name Server autoritativi:** forniscono la risposta finale per un dominio specifico

---

## Cache DNS

I resolver DNS e i browser **memorizzano temporaneamente** le risposte DNS per migliorare le prestazioni e ridurre il traffico. Il tempo di validità è regolato dal valore **TTL (Time-To-Live)**.

---

## DNS e sicurezza

- **DNSSEC:** aggiunge firme crittografiche per autenticare le risposte DNS
- **Protezione da spoofing e attacchi cache poisoning**
- **Firewall e filtri DNS** per bloccare domini malevoli

---

## DNS in ambito cloud

Servizi cloud come AWS, Azure, Google Cloud offrono DNS gestiti, che:

- Scalano automaticamente
- Sono integrati con il resto dell'infrastruttura cloud
- Offrono routing avanzato (geografico, failover, latenza)

➡️ Un esempio è **Amazon Route 53**, il servizio DNS di AWS, che approfondiremo in un documento dedicato.

---

## Conclusione

Il DNS è essenziale per il funzionamento moderno di Internet. Conoscere la sua struttura, i record principali e il suo ruolo nelle architetture cloud è fondamentale per qualsiasi sviluppatore, sysadmin o architetto IT.

---

La versione Amazon di DNS è **[[Amazon-Route-53]]**