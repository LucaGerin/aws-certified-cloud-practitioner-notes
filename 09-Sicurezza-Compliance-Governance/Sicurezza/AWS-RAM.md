--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)

# 🔗 AWS Resource Access Manager (RAM)

## Cos'è e come funziona

**AWS Resource Access Manager (RAM)** è un servizio che consente di condividere in modo sicuro le risorse AWS tra account diversi all'interno della stessa organizzazione (definita in [AWS Organizations](09-Sicurezza-Compliance-Governance/Compliance e Governance/AWS-Organizations.md)) o con account AWS esterni. Invece di duplicare risorse o configurazioni, RAM permette la **condivisione diretta** delle risorse, mantenendo il controllo e la gestione centralizzati.

È particolarmente utile in architetture multi-account, facilitando la governance, la riduzione dei costi e la semplificazione della configurazione.

RAM supporta la condivisione di diverse risorse, tra cui:
- VPC Subnet
- Route53 Resolver rules
- Transit Gateway
- License Manager configurations
- AWS Glue data catalog
- Aurora DB snapshots

---

## Caratteristiche principali e vantaggi

- **Condivisione efficiente delle risorse**: evita la duplicazione, riduce la complessità e migliora la coerenza.
- **Integrazione con AWS Organizations**: permette una gestione centralizzata dei permessi e della visibilità.
- **Controllo granulare**: è possibile definire chi può accedere a cosa, anche in modalità read-only.
- **Risparmio sui costi**: alcune risorse, come i Transit Gateway, possono essere condivise tra più account, evitando la necessità di istanziarne diverse.
- **Semplificazione operativa**: la configurazione di risorse condivise in un solo account è visibile e utilizzabile anche dagli altri account autorizzati.

---

## Sicurezza

AWS RAM si integra con:
- **[IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) (Identity and Access Management)** per autorizzare le azioni legate alla condivisione.
- **[AWS Organizations](09-Sicurezza-Compliance-Governance/Compliance e Governance/AWS-Organizations.md)** per limitare la condivisione a specifici account o unità organizzative (OU).
- **Audit e logging tramite [AWS CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)**, che permette di tracciare tutte le operazioni effettuate tramite RAM.

Le risorse condivise non implicano una perdita di controllo: i proprietari delle risorse restano responsabili e possono revocare la condivisione in qualsiasi momento.

---

## Pricing

**AWS Resource Access Manager** è **gratuito**. Non ci sono costi aggiuntivi per la condivisione delle risorse.

Tuttavia, è importante notare che le **risorse condivise mantengono il loro modello di costo originale**. Ad esempio, se si condivide un Transit Gateway, l'account proprietario continua a sostenere i costi di utilizzo, anche se viene usato da altri account.

---

## Confronto con tecnologie AWS simili

| Servizio | Differenza rispetto a RAM |
|----------|-----------------------------|
| **AWS Organizations** | Strumento di gestione degli account, mentre RAM gestisce la condivisione di risorse tra di essi. |
| **VPC Peering / Transit Gateway** | Meccanismi di rete che possono essere condivisi con RAM; RAM non sostituisce ma estende il loro uso. |
| **IAM Cross-account access** | IAM consente accesso a risorse specifiche tramite policy, mentre RAM permette la **condivisione diretta e nativa** delle risorse stesse. |
| **Service Control Policies (SCPs)** | Le SCP regolano le azioni consentite negli account; RAM opera a livello di condivisione di risorse esistenti. |

---

## Conclusione

AWS RAM è uno strumento fondamentale per implementare strategie di **multi-account architecture** in modo efficiente e sicuro. Permette di centralizzare l’allocazione delle risorse condivisibili, mantenendo il controllo e migliorando l’ottimizzazione dei costi e della governance su scala enterprise.
