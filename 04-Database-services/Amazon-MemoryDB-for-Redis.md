--> [AWS](/00-Intro/AWS.md)  -  [Database Services](/04-Database-services/AWS-Databases.md)
# 🧠 Amazon MemoryDB for Redis

![MemoryDB for Redis](mem-db-for-redis-logo.webp)

**Amazon MemoryDB for Redis** è un servizio di **database in memoria completamente gestito**, compatibile con Redis, progettato per offrire **latenza ultra bassa**, **alta disponibilità** e **durabilità dei dati**.  
È ideale per applicazioni che necessitano di una combinazione tra le prestazioni di un database in memoria e la **persistenza** garantita anche in caso di failover (MemoryDB è multi-AZ di default). 

---

## ⚙️ Cos'è e come funziona

MemoryDB è progettato per scenari mission-critical in cui Redis viene utilizzato non solo come cache ma anche come database primario in-memory.  
Offre replica **sincrona multi-AZ**, journaling e snapshot automatici per garantire durabilità dei dati.  
I dati vengono conservati anche in caso di guasto della zona di disponibilità, garantendo ripristino immediato senza perdita.

![MemoryDB for Redis example](mem-db-for-redis.jpg)

---

## ✨ Caratteristiche principali e vantaggi

- 🔄 **Compatibilità con Redis**: supporta API, client e comandi Redis standard.
- 🛡️ **Alta disponibilità**: replicazione sincrona multi-AZ con failover automatico.
- 💾 **Durabilità dei dati**: journaling + snapshot persistenti.
- ⚡ **Prestazioni**: latenza sotto il millisecondo per operazioni real-time.
- 🔐 **Sicurezza avanzata**:
  - Crittografia in transito e a riposo
  - Accesso solo tramite [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md)
  - Integrazione con [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
  - ACL Redis granulari
- 📈 **Scalabilità orizzontale**: shard multipli configurabili per distribuire carico e dati.

---

## 💼 Use cases

- 🔒 Applicazioni in ambito bancario o finanziario che richiedono persistenza in tempo reale
- 🎮 Applicazioni real-time (giochi multiplayer, trading, messaggistica)
- 👤 Gestione sessioni persistenti utente
- 🧠 Motori di raccomandazione e personalizzazione
- 🌐 Cache persistente per siti web ad alta disponibilità
- 🧮 Database primario in-memory per applicazioni ad alta transazionalità
- 🗺️ Elaborazione dati geospaziali

---

## 🆚 Confronto con Amazon ElastiCache for Redis

| Caratteristica                  | **MemoryDB for Redis**                              | **ElastiCache for Redis**                            |
|---------------------------------|-----------------------------------------------------|------------------------------------------------------|
| Durabilità                      | ✅ Journaling + snapshot persistenti                | ❌ Persistenza opzionale (RDB, AOF)                  |
| Replica multi-AZ sincrona      | ✅                                                  | ❌ Replicazione asincrona                            |
| Failover e recovery             | ✅ Completo e senza perdita                         | ❌ Potenziale perdita di dati                        |
| Posizione nel sistema           | Database in-memory **primario**                    | **Cache** ad alte prestazioni                        |
| Sicurezza                       | ACL, VPC-only, IAM, crittografia forzata           | ACL, VPC, crittografia configurabile                |
| Prezzo                          | Più elevato, workload critici                      | Più economico, workload orientato al caching         |

---

## 🧱 Architettura

- 🧩 Basato su cluster compatibile Redis
- 🔁 Replicazione sincrona tra **nodi primari e secondari**
- 📜 Persistenza tramite **journaling su disco** e **snapshot automatici**
- 🌍 Distribuzione su più **Availability Zone**
- 🧠 Ogni shard può avere una o più repliche, scalando letture e aumentando disponibilità

---

## 🔒 Sicurezza

- 🔐 **Accesso privato**: disponibile solo all’interno di [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md)
- 🔐 **Crittografia forzata** in transito e a riposo (con KMS)
- 👥 **Controllo accessi** tramite [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
- 🧩 **Redis ACL** per definire permessi granulari per utenti/comandi
- 📊 Integrazione con [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) per logging e alerting

---

## 💰 Pricing

Il costo di Amazon MemoryDB for Redis dipende da:

- 🧠 Tipo di nodo (memoria, capacità computazionale)
- 🔢 Numero di **shard** e **repliche**
- 🌍 **Regione** AWS selezionata
- 💾 Utilizzo dello **storage per journaling e snapshot**
- 📦 Trasferimento dati (inbound gratuito, outbound a pagamento)

---

## 📌 Conclusione

**Amazon MemoryDB for Redis** unisce il meglio del caching in memoria e della **durabilità dei database tradizionali**, offrendo **alta disponibilità, sicurezza e performance**.  
È pensato per applicazioni che richiedono **coerenza, velocità e affidabilità**, senza compromettere la persistenza dei dati anche in caso di guasti critici.

> "MemoryDB è il Redis per chi non vuole perdere mai un dato, anche sotto carico estremo e in architetture globali."
