--> [AWS](AWS.md)  -  [Data Analytics](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon Redshift e Redshift Serverless

**Amazon Redshift** è il servizio di **data warehouse in cloud** offerto da AWS, progettato per l’**analisi di grandi volumi di dati** tramite SQL ad alte prestazioni. Redshift permette di eseguire query complesse su petabyte di dati in modo rapido, affidabile e integrato con l’ecosistema AWS.

Con **Redshift Serverless**, AWS introduce una modalità ancora più flessibile: l’**esecuzione on-demand di query SQL**, senza dover creare e gestire cluster.

---

## 🧩 Cos'è Amazon Redshift?

Amazon Redshift è un database columnar ottimizzato per carichi analitici (OLAP) e data warehousing. Supporta:

- **Query SQL standard** ad alte prestazioni
- Massively Parallel Processing (MPP): è in grado di eseguire query complesse in parallelo.
- Gestione dei dati automatizzata: backup, replica, scaling avengono in automatico e senza downtime.
- Progettato per OLAP, analytics e reporting.
- Caricamento dati da S3, DynamoDB, RDS, Kinesis, ecc.
- Integrazione con BI tools ([QuickSight](Amazon-QuickSight.md), Tableau, Power BI)
- Compressione automatica e parallelismo massiccio (MPP)
- **Data lake integration** con Redshift Spectrum (query dirette su dati in S3)

---

## ☁️ Cos'è Redshift Serverless?

**Redshift Serverless** ti consente di:
- Eseguire query **senza provisioning di cluster**
- Pagare solo per l’**uso effettivo (query execution time)**
- Scalare automaticamente risorse compute e memoria
- Accedere ai dati con la stessa interfaccia di Redshift tradizionale

---

## 🔄 Differenze tra Redshift e Redshift Serverless

| Caratteristica        | Redshift Classic         | Redshift Serverless            |
|------------------------|--------------------------|---------------------------------|
| Provisioning           | Manuale (cluster dedicato) | Automatico (no cluster)         |
| Costi                  | Basati su uptime         | Basati sul consumo (RPU/h)      |
| Scalabilità            | Manuale / elastic resize | Automatica                      |
| Avvio                  | Sempre attivo            | On-demand                       |
| Ideale per             | Carichi persistenti      | Accesso saltuario, on-demand    |

> 💡 **RPU (Redshift Processing Unit)**: unità di misura per la potenza computazionale in Redshift Serverless

---

## 🛠️ Caratteristiche chiave (entrambe le versioni)

- **Columnar storage** per query ottimizzate
- **Materialized views** per prestazioni accelerate
- **Workload Management (WLM)** per bilanciare risorse
- **Federated Query** per interrogare altri database (RDS, Aurora)
- **Machine Learning integrato**: creazione di modelli ML direttamente da SQL
- **Sicurezza avanzata**: [VPC](Amazon-VPC.md), KMS, [IAM](AWS-IAM.md), Redshift Spectrum + Lake Formation

---

## ✅ Use case comuni

- **Data warehouse aziendale** su petabyte di dati
- Dashboard BI e reporting interattivo
- Integrazione con data lake, per esempio su S3
- Analisi log, clickstream, IoT
- ML + Analisi predittiva (AutoML integrato)

---

## 🔐 Sicurezza e compliance

- Supporto per **[VPC](Amazon-VPC.md), [KMS](AWS-KMS.md), [IAM](AWS-IAM.md), SSO**
- **Audit logging** con [CloudTrail](Amazon-CloudTrail.md)
- **Crittografia a riposo e in transito**
- Compatibile con GDPR, HIPAA, PCI-DSS

---

## 📌 Conclusioni

Amazon Redshift, nelle sue varianti **provisioned** e **serverless**, è uno dei data warehouse più potenti e scalabili sul cloud. Offre prestazioni elevate, sicurezza integrata e un ricco ecosistema di integrazione con altri servizi AWS per analizzare qualsiasi tipo di dato, ovunque si trovi.

> “Che si abbia un petabyte di dati o solo una query da lanciare, Redshift offre velocità e flessibilità.”
