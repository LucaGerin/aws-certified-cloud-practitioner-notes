--> [AWS](AWS.md)  -  [Database Services](AWS-Databases.md)
# ⚡ Amazon ElastiCache

![Elasticache](elasticache.png)

**Amazon ElastiCache** è un servizio completamente gestito che consente il deployment, l'esecuzione e la scalabilità di **archivi di dati in memoria** nel cloud AWS, compatibili con **Redis** o **Memcached**. 
È progettato per migliorare la **velocità e le prestazioni** delle applicazioni web e data-intensive riducendo il carico sui database principali, fornendo una cache in memoria ad alta velocità e bassa latenza.

NB: Se si cerca un servizio che sia sempre completamente gestito per lo storage in-memoy, ma che abbia **alta availability** e sia **orientato alla durability** dei dati, per la creazione di un applicazione, [Amazon MemoryDB for Redis](Amazon-MemoryDB-for-Redis.md) è preferibile a ElastiCache.

---

## ⚙️ Cos'è e come funziona

Amazon ElastiCache permette di utilizzare Redis o Memcached in modalità fully-managed, eliminando la necessità di gestire manualmente provisioning, patching, monitoraggio o failover.  
Opera all’interno di un [Amazon VPC](Amazon-VPC.md) per garantire isolamento di rete, e può essere distribuito su più **Availability Zone** per alta disponibilità.

Sono supportate due modalità di funzionamento:

- **Standalone / Replica group** (master + replica)
- **Cluster Mode Enabled** (sharding automatico Redis)

![Elasticache example](elasticache-example.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🔄 **Supporto per Redis e Memcached**: scegli il motore più adatto alla tua architettura.
- 🧠 **Dati in memoria**: latenza sotto il millisecondo, ottimo per real-time.
- 📦 **Riduzione del carico sul database**: caching dei risultati più richiesti.
- 🛡️ **Sicurezza integrata**:
  - Integrazione con [IAM](AWS-IAM.md)
  - Crittografia **in transito** e **a riposo**
  - Supporto per ACL (Redis)
- ♻️ **Alta disponibilità**: failover automatico, replica multi-AZ (Redis)
- 📈 **Scalabilità flessibile**: Cluster Redis con sharding orizzontale
- 🔧 **Gestione semplificata**: provisioning, patching, backup automatici

---

## 💼 Use cases

- 🗃️ **Caching delle query di database** (es. MySQL, PostgreSQL)
- 🧾 **Session store** per app web scalabili
- 🧮 **Leaderboard e contatori** in tempo reale
- 📢 **Pub/Sub messaging** (Redis)
- 📊 **Rate limiting e gestione API**

---

## 🧠 Differenze tra Redis e Memcached

| Caratteristica         | Redis                                | Memcached                             |
|------------------------|--------------------------------------|----------------------------------------|
| Tipi di dati avanzati  | ✅ Liste, Set, Hash, Stream, ecc.    | ❌ Solo key-value                      |
| Persistenza dei dati   | ✅ (RDB, AOF, snapshot)               | ❌ Nessuna persistenza                 |
| Replica e failover     | ✅ (nativo)                           | ❌                                     |
| Sharding automatico    | ✅ Con Cluster Mode                   | ✅ Solo lato client                    |
| Pub/Sub                | ✅                                    | ❌                                     |
| Sicurezza avanzata     | ✅ ACL, TLS, IAM                      | ❌ Supporto limitato                   |

---

## 💰 Pricing

I costi di ElastiCache dipendono da:

- ✅ Motore scelto: Redis o Memcached
- ✅ Tipo e numero di nodi
- ✅ Configurazione multi-AZ e snapshot (solo Redis)
- ✅ Region AWS selezionata
- ✅ Trasferimento dati (inbound gratuito, outbound con tariffa)

---

## 🔒 Sicurezza

Amazon ElastiCache implementa una serie di misure per garantire la protezione dei dati:

- 🔐 **Crittografia a riposo** e **in transito** (Redis)
- 🔒 **Access control list (ACL)** per Redis
- 🌐 **Isolamento di rete** tramite [Amazon VPC](Amazon-VPC.md)
- 📜 **IAM** per controllo degli accessi e gestione delle policy
- 📊 **Monitoraggio con CloudWatch**

---

## 🔁 Confronto con altri servizi AWS

| Servizio           | Tipo                          | Persistenza | Performance   | Use case principali                          |
|--------------------|-------------------------------|-------------|---------------|----------------------------------------------|
| ElastiCache        | In-memory (Redis/Memcached)   | ❌/✅        | 🔥 Altissima   | Caching, sessioni, real-time                 |
| [Amazon RDS](Amazon-RDS.md)         | Relazionale (SQL)             | ✅           | ⚡ Alta        | DB web/app, transazioni                      |
| [Amazon DynamoDB](Amazon-DynamoDB.md)    | NoSQL key-value               | ✅           | ⚡ Alta        | IoT, mobile, low-latency access              |
| [MemoryDB for Redis](Amazon-MemoryDB-for-Redis.md) | In-memory (Redis con durabilità) | ✅        | 🔥 Altissima   | Applicazioni distribuite, microservizi       |

---

## 📌 Conclusione

**Amazon ElastiCache** è la soluzione ideale per **applicazioni cloud ad alte prestazioni** che richiedono una gestione rapida dei dati, **riduzione della latenza** e **alleggerimento del database primario**. Grazie al supporto per Redis e Memcached, offre flessibilità e scalabilità in diversi scenari architetturali.

> “Per ogni applicazione che richiede velocità immediata nella gestione dei dati, ElastiCache è la risposta giusta.”
