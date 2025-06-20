--> [AWS](00-Intro/AWS.md)  -  [Data Analytics](07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon Athena

**Amazon Athena** è un servizio **serverless di query interattiva** che consente di eseguire **SQL direttamente su dati archiviati in [Amazon S3](02-Storage-services/Amazon-S3.md)** (in formato csv, jason, avro, parquet). 
Non richiede provisioning o gestione di server, ed è ideale per data analyst e ingegneri che vogliono interrogare rapidamente i dati con **prezzi basati sul volume di dati analizzati**.
E' adatto anche ad analisi complesse su big data con grandi Join e window functions.

Athena si paga per query e per TB scanned.

---

## 🧩 Caratteristiche principali

- **Esegui query SQL su S3** in modo nativo
- Compatibile con **Presto/Trino** come motore di esecuzione
- Supporta **formati efficienti**: CSV, JSON, Parquet, ORC, Avro
- Integrazione con **[AWS Glue Data Catalog](07-IA-ML-Analytics/Analytics/AWS-Glue.md)**
- Può usare **funzioni definite dall’utente (UDF)** in JavaScript
- Output delle query salvato automaticamente in S3
- Compatibile con strumenti BI come **[Amazon QuickSight](07-IA-ML-Analytics/Analytics/Amazon-QuickSight.md)**

---

## ✅ Vantaggi

- **100% serverless**: nessuna infrastruttura da configurare
- **Pagamento a consumo**: paghi solo per i dati effettivamente scansionati
- **Velocità di setup**: pronta in pochi minuti
- **Supporto per data lake** su S3
- **Query federate** su altre fonti dati ([RDS](04-Database-services/Amazon-RDS.md), [Redshift](07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md), JDBC, ecc.)
- **Sicurezza integrata** con [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), KMS, e [Lake Formation](AWS-Lake-Formation.md)

---

## 🚀 Use case tipici

- Query su Log salavati in S3
- **Analisi ad hoc** di file di log, esportazioni, eventi, IoT
- Eseguire queries su click-stream data
- **Esplorazione di dati grezzi** in data lake
- **Creazione di dashboard interattive** con QuickSight
- **Audit e security analytics** (es. log CloudTrail, [VPC](03-CDN-e-Networking/Amazon-VPC.md) Flow, GuardDuty)
- Analisi dei costi di AWS e Usage reports
- **Validazione dati** e debug di pipeline ETL (es. output Glue)

---

## 🔧 Esempio di query

```sql
SELECT user_id, COUNT(*) AS accessi
FROM logs_web
WHERE status = 200
  AND year = 2024 AND month = 5
GROUP BY user_id
ORDER BY accessi DESC
LIMIT 10;
```

> I dati nel bucket S3 devono essere organizzati in **partizioni (es. year, month, day)** per ottimizzare performance e costi.

---

## 🔐 Sicurezza e governance

- Controllo accesso con **[IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)** o **Lake Formation**
- Crittografia **in transito** e **a riposo (SSE-KMS)**
- Audit tramite **[AWS CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)**
- **Query logging** disponibile su S3

---

## 📦 Differenze con altri servizi simili

| Servizio             | Quando usarlo                                | Caratteristiche principali                       |
|----------------------|-----------------------------------------------|--------------------------------------------------|
| **[Amazon Athena](07-IA-ML-Analytics/Analytics/Amazon-Athena.md)**           | Query SQL su file in S3                       | Serverless, analisi interattiva, ad hoc          |
| **[Amazon Redshift](07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md)**         | Data warehouse con cluster (OLAP)             | Alte prestazioni su dati strutturati             |
| **[Amazon EMR](07-IA-ML-Analytics/Analytics/Amazon-EMR.md) (Hive/Spark)** | Big Data batch o stream processing            | Complesso, potente, cluster gestito              |

---

## 🛠️ Best Practices

- Usa formati **columnar compressi** (Parquet, ORC) per ridurre i costi
- **Partiziona i dati** per velocizzare le query e ridurre i dati scansionati
- Mantieni ordinati i file nel bucket (es. `/logs/year=2024/month=05/`)
- Usa il **[Glue Data Catalog](07-IA-ML-Analytics/Analytics/AWS-Glue.md)** per centralizzare la definizione delle tabelle
- Configura **limiti di spesa** se usato in ambienti aperti o sandbox

---

## 📌 Conclusioni

Amazon Athena è uno strumento potente e flessibile per **analizzare dati su S3 in modo rapido e senza overhead infrastrutturale**. Ideale per data lake e log analytics, consente di estrarre valore dai dati con query SQL standard, integrandosi perfettamente nell’ecosistema AWS.

> “Con Athena, i tuoi dati su S3 diventano subito interrogabili — senza provisioning, senza attese.”

