--> [AWS](/00-Intro/AWS.md)  -  [Database Services](/04-Database-services/AWS-Databases.md)
# ⚡ Amazon DynamoDB

**Amazon DynamoDB** è un **database NoSQL completamente gestito e serverless**, progettato per supportare **applicazioni ad alte prestazioni** con **scalabilità automatica** e **latenza ultra-bassa**.  

Grazie alla sua architettura nativa per il cloud, offre performance costanti anche a **milioni di richieste al secondo**, senza necessità di provisioning o gestione manuale dell’infrastruttura.

![Amazon DynamoDB](DynamoDB.png)

Caratteristica peculiare di DynamoDB è che, pur essendo NoSQL, supporta le proprietà ACID (Atomicity, Consistency, Isolation, Durability).
Di default, DynamoDB offre delle letture di dati "*eventually consistent*", ma si può impostare su letture "*strongly consistent*".

---

## 📘 Cos'è e come funziona

Amazon DynamoDB è un database key-value e documentale, in cui ogni record è un item con chiavi primarie (partition key + optional sort key) e attributi flessibili.  
Supporta sia **modelli dati semplici** che strutture **annidate** in formato JSON.

Offre due modalità di utilizzo:
- **On-demand**: addebito basato su richieste effettive
- **Provisioned**: capacità assegnata manualmente, con supporto per auto-scaling

È integrato con l’intero ecosistema AWS ([Lambda](/01-Compute-options/AWS-Lambda.md), [API Gateway](/Others/Amazon-API-Gateway.md), [EventBridge](/05-Development-Messaging-Deploying/Amazon-EventBridge.md), [AppSync](/Others/Amazon-AppSync.md)) e può essere esteso con stream, TTL, backup e query complesse via **DynamoDB PartiQL**.

---

## ✨ Caratteristiche principali e vantaggi

- 🧩 **Modello dati flessibile**: key-value e document (JSON)
- 🚀 **Prestazioni costanti**: latenza singola cifra di millisecondi
- ☁️ **Completamente gestito**: niente patching, replica o provisioning da gestire
- 📈 **Scalabilità automatica**: cresce e si adatta in base al traffico
- 🔁 **Backup integrato**: backup on-demand e continuo (PITR) tra diverse regioni
- 🔐 **Sicurezza nativa**: [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), crittografia (KMS), [VPC](/03-CDN-e-Networking/Amazon-VPC.md)
- 📡 **Stream e integrazioni**: DynamoDB Streams, [Amazon EventBridge](/05-Development-Messaging-Deploying/Amazon-EventBridge.md), [AWS Lambda](/01-Compute-options/AWS-Lambda.md)
- 🧠 **Query SQL-like**: supporto a PartiQL per operazioni compatibili SQL

---
### 🌍 DynamoDB Global Tables

Le **DynamoDB Global Tables** sono una versione di tabelle, creabili esplicitamente in DynamoDB, che permettono di **replicare automaticamente i dati tra più regioni AWS**, offrendo **alta disponibilità e bassa latenza** a livello globale. 
Ogni replica è completamente attiva (multi-master), consentendo letture e scritture locali in ogni regione.  
Sono ideali per applicazioni **distribuite su più Availability Zone o regioni**, che richiedono **continuità operativa e sincronizzazione dati in tempo reale** anche in caso di guasti o failover.

---
### ⚡ DynamoDB Accelerator (DAX)

**DynamoDB Accelerator (DAX)** è un **cache in-memory completamente gestito** per Amazon DynamoDB, progettato per offrire **latenze di lettura di pochi microsecondi** anche su carichi elevati. 

DAX gestisce automaticamente il caching delle query più frequenti, riducendo la necessità di accedere ripetutamente al database e alleggerendo il carico su DynamoDB. 
È compatibile con le API standard di DynamoDB, quindi **non richiede modifiche significative all'applicazione**.  

DAX è particolarmente utile per **applicazioni ad alta frequenza di lettura**, come motori di raccomandazione, e-commerce, giochi e analytics in tempo reale.

---

## 🚀 Use cases

- 🌐 Web e mobile apps a traffico elevato
- 🛍️ E-commerce e flash sale (es. Black Friday)
- 🕹️ Giochi online e IoT (alta concorrenza, accessi frequenti)
- 📊 Logging e tracciamento real-time
- 🧠 Session store e gestione shopping cart
- 🔄 Backend per applicazioni serverless basate su [AWS Lambda](/01-Compute-options/AWS-Lambda.md)

---

## 💰 Pricing

Il costo dipende da:

- Modalità scelta (on-demand o provisioned throughput)
- Capacità di lettura e scrittura
- Volume di storage
- Utilizzo di backup, stream, TTL, Global Tables e Accelerator (DAX)

**On-demand** è ideale per carichi variabili o imprevedibili.  
**Provisioned** conviene in ambienti con traffico prevedibile e costante.

---

## 🔒 Sicurezza

- 🔐 **Crittografia at-rest**: abilitata di default con **[AWS KMS](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)**
- 🧑‍💼 **[IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) fine-grained access control**: autorizzazioni a livello di tabella, item, attributo
- 🌐 **Isolamento tramite [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md)** con **VPC endpoints**
- 📋 **CloudTrail**: monitoraggio di tutte le operazioni eseguite sul database tramite [Amazon CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)
- 📄 **Compliance**: certificazioni PCI DSS, HIPAA, ISO 27001, SOC 1/2/3

---

## ⚙️ Confronto con altri servizi AWS

| Servizio                        | Tipo di database         | Latenza  | Modello dati       | Quando usarlo                              |
| ------------------------------- | ------------------------ | -------- | ------------------ | ------------------------------------------ |
| **DynamoDB**                    | NoSQL key-value          | 🟢 Bassa | Flessibile (JSON)  | App real-time, scalabilità massiva, IoT    |
| **[Amazon RDS](/04-Database-services/Amazon-RDS.md)** | SQL relazionale          | 🟡 Media | Relazionale (SQL)  | App legacy, integrazioni esistenti SQL     |
| **[Amazon Aurora](/04-Database-services/Amazon-Aurora.md)**               | SQL relazionale avanzato | 🟡 Media | Relazionale (SQL)  | App moderne SQL ad alta disponibilità      |
| **[Amazon ElastiCache](/04-Database-services/Amazon-ElastiCache.md)**          | In-memory                | 🟢 Ultra | Key-value semplice | Cache, contatori, Pub/Sub                  |
| **[Amazon MemoryDB](/04-Database-services/Amazon-MemoryDB-for-Redis.md)**             | In-memory durabile       | 🟢 Ultra | Redis compatibile  | Database primari in-memory con persistenza |

---

## 📌 Conclusione

**Amazon DynamoDB** è la soluzione ideale per applicazioni che richiedono **scalabilità automatica, disponibilità elevata e latenza ridotta**, senza dover gestire l’infrastruttura sottostante.  
È una base solida per architetture serverless, distribuite e moderne.

> “Con DynamoDB, la tua applicazione scala automaticamente. Tu devi solo preoccuparti del codice.”
