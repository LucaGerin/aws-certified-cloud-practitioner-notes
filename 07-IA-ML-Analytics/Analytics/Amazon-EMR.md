--> [AWS](00-Intro/AWS.md)  -  [Data Analytics](07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon EMR (Elastic MapReduce)

**Amazon EMR** è il servizio AWS, consistente in una piattaforma per i big Data, per l'elaborazione distribuita di **grandi quantità di dati** utilizzando framework open source come **Apache Spark, Hadoop, Hive, Presto, HBase, Trino, e altri**. 

Offre una piattaforma scalabile e completamente gestita per **Big Data, analisi batch, machine learning, trasformazioni ETL e query interattive**.

---

## 🧩 Cos'è Amazon EMR?

Amazon EMR semplifica il deployment, la configurazione e la gestione di cluster Big Data su AWS. 

È ottimizzato per eseguire **job paralleli** su petabyte di dati, sfruttando la potenza computazionale di **[EC2](01-Compute-options/Amazon-EC2.md), [EBS](02-Storage-services/Amazon-EBS.md) e [S3](02-Storage-services/Amazon-S3.md)** in modo elastico e con costi ottimizzati.

---

## 🌟 Caratteristiche principali e Vantaggi

- Supporta dati strutturati, semi-strutturati, non strutturati.
- Supporto per framework Big Data più popolari: **Spark, Hadoop, Hive, HBase, Trino, Presto, Flink**
- Deploy su **[EC2](01-Compute-options/Amazon-EC2.md), [Amazon EKS](01-Compute-options/Amazon-EKS.md) (EMR on EKS)** o **serverless (EMR Serverless)**
- Integrazione nativa con **Amazon S3** per lo storage dati
- **Auto-scaling dei nodi** e gestione dei task in parallelo
- Supporto per **custom AMI, bootstrap actions** e **notebook Jupyter**
- Interfaccia via **CLI, SDK, API** o **AWS Management Console**
- **Gestione semplificata** di cluster Spark/Hadoop rispetto all'on-premises
- **Pay-per-use**: paghi solo per il tempo e le risorse usate
- Possibilità di usare **spot instances** per ridurre i costi
- **Alta scalabilità** automatica in base al carico
- **Separazione dello storage** (su S3) dallo compute
- **Flessibilità d'esecuzione**: puoi usare EMR su EC2, EKS o serverless

![Amazon EMR](Amazon-EMR.png)

---

## 🚀 Use case comuni

- **Data analysis e processing** di genomic data
- **Elaborazione ETL** su grandi dataset non strutturati o semi-strutturati
- **Machine Learning distribuito** (Spark MLlib, XGBoost su Spark, ecc.)
- **Analisi clickstream** e web log
- **Query SQL massive** con Hive, Presto o Trino
- **Generazione di report aggregati** a partire da fonti eterogenee
- **Migrazione workload Hadoop** da on-premises verso il cloud

---

## 🔄 Tipi di deployment

| Modalità           | Descrizione                                       | Quando usarla                                 |
|--------------------|---------------------------------------------------|-----------------------------------------------|
| **EMR su EC2**     | Cluster completo su istanze EC2                   | Massimo controllo e personalizzazione         |
| **EMR on EKS**     | Esegue job EMR su un cluster [Amazon EKS](01-Compute-options/Amazon-EKS.md)           | Ambienti Kubernetes, workload containerizzati |
| **EMR Serverless** | Esegue job Spark senza provisioning               | Semplicità e scalabilità automatica           |

---

## 🔐 Sicurezza e accesso

- Integrazione con **[IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)**, **KMS**, **[VPC](03-CDN-e-Networking/Amazon-VPC.md)**, **SG**, **SSM**
- Supporto per **Kerberos, LDAP**, multi-tenancy e crittografia
- Audit tramite **[CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)** e logging su **[S3](02-Storage-services/Amazon-S3.md)** o **[CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md)**

---

## 💰 Pricing

Il prezzo di Amazon EMR dipende da:
- **Tipo e numero di istanze [EC2](01-Compute-options/Amazon-EC2.md) usate**
- Durata di esecuzione dei job
- Eventuali **servizi esterni** usati (S3, CloudWatch, [EBS](02-Storage-services/Amazon-EBS.md))
- Uso di **spot instances** (può ridurre i costi fino al 90%)

> EMR Serverless applica un costo in base alle risorse effettivamente usate (vCPU-secondi e GB-secondi).

---

## 🔄 Confronto con altri servizi simili

| Servizio           | Quando usarlo                                | Differenze principali                          |
|--------------------|-----------------------------------------------|------------------------------------------------|
| **Amazon EMR**     | Big Data batch o stream processing            | Altamente personalizzabile, Spark/Hadoop-based |
| **[AWS Glue](07-IA-ML-Analytics/Analytics/AWS-Glue.md)**       | ETL gestito e serverless                      | No cluster, interfaccia visiva, meno flessibile|
| **[Amazon Athena](07-IA-ML-Analytics/Analytics/Amazon-Athena.md)**  | Query SQL su dati in S3                       | Serverless, query rapide su dati statici       |
| **[Amazon Redshift](07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md)**| Data warehouse relazionale (OLAP)             | Ottimizzato per query su dati strutturati      |
| **[Amazon OpenSearch](07-IA-ML-Analytics/Analytics/Amazon-OpenSearch.md)** | Ricerca full-text e analisi log           | Adatto per text search e analytics             |

---

## 🛠️ Best Practices

- Usa **Parquet o ORC** per minimizzare I/O e costi
- Metti i dati in **[S3](02-Storage-services/Amazon-S3.md) partizionati e compressi**
- Separa i nodi **master, core, task** per gestione più efficace
- Valuta **EMR Serverless** per carichi intermittenti
- Usa **spot instances** per job batch non critici
- Usa **auto-terminate** per risparmiare in ambienti di test

---

## 📌 Conclusioni

Amazon EMR è una delle piattaforme più potenti per eseguire workload Big Data scalabili e flessibili nel cloud. Che tu stia elaborando dati con Spark, migrando un cluster Hadoop o costruendo pipeline complesse, EMR ti permette di **concentrarti sul lavoro** anziché sulla gestione dell’infrastruttura.

> “Con EMR, il tuo cluster Big Data diventa flessibile, veloce e cloud-native.”
