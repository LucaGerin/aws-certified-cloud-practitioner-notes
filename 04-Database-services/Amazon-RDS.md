--> [AWS](/00-Intro/AWS.md)  -  [Database Services](/04-Database-services/AWS-Databases.md)
# 🗄️ Amazon RDS (Relational Database Service)

**Amazon RDS** è un servizio di **database relazionale completamente gestito** che semplifica la configurazione, l'esecuzione e la scalabilità di database SQL nel cloud.  

Consente di **automatizzare attività amministrative complesse**, che per RDS sono gestite da AWS, come provisioning hardware, patching, backup e ripristino, lasciando agli sviluppatori il focus sulla logica applicativa.

![Amazon RDS](RDS.png)

---

## ⚙️ Cos'è e come funziona

Amazon RDS permette di lanciare un database SQL in pochi clic o API call. AWS gestisce il provisioning, la configurazione, i backup, l'alta disponibilità, il patching e il monitoraggio.  
Gli utenti possono selezionare il motore desiderato, specificare le dimensioni dell'istanza e i parametri di rete e sicurezza, mentre RDS si occupa dell’infrastruttura sottostante.

---

## 🧩 Motori di database supportati

- **MySQL**
- **PostgreSQL**
- **MariaDB**
- **Oracle**
- **SQL Server**
- **Amazon Aurora** *(compatibile con MySQL e PostgreSQL)*

---

## ✨ Caratteristiche principali e vantaggi

- ⚙️ **Provisioning automatico**: CPU, RAM e storage gestiti automaticamente da AWS  
- 💾 **Backup automatici**: snapshot giornalieri, backup point-in-time e retention configurabile  
- ♻️ **Alta disponibilità (Multi-AZ)**: replica sincrona e failover automatico tra zone di disponibilità  
- 🔐 **Sicurezza integrata**:
  - [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) per il controllo degli accessi
  - Integrazione con [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md) per l’isolamento di rete
  - **Crittografia at-rest** con [AWS KMS](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md) e in-transit con SSL  
- 📈 **Scalabilità verticale**: modifiche dell'istanza anche a caldo  
- 📊 **Monitoraggio continuo** con Amazon CloudWatch

---
### 🛠️ Tipi di Deployment in Amazon RDS

**Amazon RDS** supporta diversi tipi di deployment per soddisfare esigenze di **disponibilità, scalabilità e resilienza**.  
- 🧩 **Single-AZ Deployment**: l’istanza è ospitata in una sola Availability Zone. Adatto a workload non critici o ambienti di sviluppo/test.
- 🛡️ **Multi-AZ Deployment**: RDS mantiene una replica sincrona in una seconda AZ, garantendo **failover automatico** in caso di guasto dell'istanza primaria. Migliora la disponibilità, ma **non aumenta la capacità di lettura**.
- 📖 **Read Replicas**: permettono di creare **repliche asincrone** dell’istanza primaria in una o più AZ o regioni. Utili per **scalare le letture**, migliorare le performance o per analisi/reporting senza impattare il database primario.

Combinando Multi-AZ e Read Replicas, puoi ottenere una **soluzione altamente resiliente e scalabile** per ambienti di produzione mission-critical.

Per replicare tra regioni diverse, la **Cross-Region Read Replica** va abilitata manualmente, ed è disponibile solo per alcuni motori RDS. La replica Cross-Region è **asincrona** e usata più per **disaster recovery** o per **letture globali**, non per alta disponibilità in tempo reale.


___

## 💼 Use cases

- 🌐 Applicazioni web e mobile con persistente SQL backend  
- 🛍️ Sistemi e-commerce  
- 🏢 Applicazioni enterprise (ERP, CRM, ecc.)  
- 📊 Reporting e sistemi OLAP  
- 🔁 Modernizzazione e migrazione di database legacy on-premise  
- 🏥 Applicazioni regolamentate in ambito sanitario, finanziario, pubblico

---

## 💰 Pricing

Il costo di Amazon RDS si basa su:

- **Tipo e dimensione dell’istanza**
- **Motore database selezionato**
- **Storage allocato** (GB/mese)
- **Backup aggiuntivi**
- **Trasferimento dati in uscita**

Aurora ha un modello di pricing separato. Il backup automatico fino a 100% dello storage allocato è gratuito.

---

## 🔒 Sicurezza

- ✅ **Crittografia dei dati at-rest** tramite [AWS KMS](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md) (obbligatoria in fase di creazione)
- ✅ **Replica cifrata** per abilitare la cifratura su istanze esistenti
- ✅ **Sicurezza di rete** tramite:
  - Security Groups
  - [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) per accesso via API
  - [VPC](/03-CDN-e-Networking/Amazon-VPC.md) per isolamento e routing
- ✅ **Audit logging** e tracciamento con AWS CloudTrail

---

## 🔁 Confronto con servizi simili

| Servizio         | Tipo                  | Gestione | Alta disponibilità | Multi-engine | Caching integrato |
|------------------|-----------------------|----------|--------------------|---------------|-------------------|
| **Amazon RDS**   | Relazionale (SQL)     | ✅ Sì     | ✅ Sì (Multi-AZ)     | ✅ Sì         | ❌ No             |
| **Amazon Aurora**| Relazionale (MySQL/PG)| ✅ Sì     | ✅ Alta (cluster)    | ❌ Solo 2     | ❌ No             |
| **Amazon DynamoDB** | NoSQL key-value    | ✅ Sì     | ✅ Sì                | ❌ No         | ✅ DAX            |

---

## 📌 Conclusione

Amazon RDS è la soluzione ideale per chi desidera un database SQL **scalabile, sicuro, ad alta disponibilità** e **senza gestione manuale dell’infrastruttura**.  
È progettato per aziende e sviluppatori che vogliono eliminare la complessità dell’amministrazione dei database, accelerando lo sviluppo e riducendo il rischio operativo.

> “Con RDS, il tuo database è sempre disponibile, aggiornato e protetto — senza doverlo gestire direttamente.”
