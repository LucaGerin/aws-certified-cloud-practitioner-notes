--> [AWS](/00-Intro/AWS.md)
# Intelligenza Artificiale, Machine Learning e Analytics su AWS

[AWS](/00-Intro/AWS.md) offre un ecosistema completo di **servizi di Intelligenza Artificiale (AI), Machine Learning (ML) e Analisi dei Dati**, pensato per supportare tutte le fasi di un progetto data-driven: dalla raccolta dei dati alla creazione di modelli predittivi fino alla messa in produzione di soluzioni intelligenti.

Con AWS, le organizzazioni possono:
- Analizzare dati in tempo reale o batch
- Creare modelli ML personalizzati
- Usare API AI pre-addestrate (vision, linguaggio, raccomandazioni)
- Costruire data lake e pipeline analitiche scalabili
- Lavorare con ambienti serverless, gestiti o on-premises

---

## 🧠 Servizi di Intelligenza Artificiale (AI)

Questi servizi offrono **modelli pre-addestrati** accessibili tramite API, senza richiedere esperienza in ML:

| Servizio                                        | Funzione principale                                    |
| ----------------------------------------------- | ------------------------------------------------------ |
| **[Amazon Rekognition](07-IA-ML-Analytics/AI e ML/Amazon-Rekognition.md)** | Analisi di immagini e video (face detection, OCR)      |
| **[Amazon Comprehend](07-IA-ML-Analytics/AI e ML/Amazon-Comprehend.md)**   | Analisi del linguaggio naturale (sentiment, entità)    |
| **[Amazon Transcribe](07-IA-ML-Analytics/AI e ML/Amazon-Transcribe.md)**   | Conversione voce-testo (trascrizione automatica)       |
| **[Amazon Polly](07-IA-ML-Analytics/AI e ML/Amazon-Polly.md)**             | Sintesi vocale (testo → audio realistico)              |
| **[Amazon Translate](07-IA-ML-Analytics/AI e ML/Amazon-Translate.md)**     | Traduzione automatica multilingua                      |
| **[Amazon Lex](07-IA-ML-Analytics/AI e ML/Amazon-Lex.md)**                 | Costruzione di chatbot con NLP + ASR (come Alexa)      |
| **[Amazon Textract](07-IA-ML-Analytics/AI e ML/Amazon-Textract.md)**       | Estrazione di testo e tabelle da documenti scansionati |
| **Amazon Personalize**                          | Raccomandazioni personalizzate in tempo reale          |
| **Amazon Forecast**                             | Previsioni di serie temporali (es. domanda, vendite)   |
| **Amazon Bedrock**                              | Accesso a modelli generativi (LLM) tramite API         |
| **[Amazon Kendra](07-IA-ML-Analytics/AI e ML/Amazon-Kendra.md)**           | Motore di ricerca intelligente basato su AI            |

---

## 🤖 Machine Learning (ML) - Costruzione e Addestramento Modelli

Strumenti e servizi per **data scientist e sviluppatori [Machine-Learning](07-IA-ML-Analytics/AI e ML/Machine-Learning.md) (ML)**:

| Servizio                                    | Descrizione                                                    |
| ------------------------------------------- | -------------------------------------------------------------- |
| **[Amazon SageMaker](07-IA-ML-Analytics/AI e ML/Amazon-SageMaker.md)** | Piattaforma completa per build, train, deploy di modelli       |
| - Studio                                    | IDE visuale per ML                                             |
| - Autopilot                                 | ML automatico (AutoML)                                         |
| - Ground Truth                              | Etichettatura dati assistita                                   |
| - Model Registry                            | Versionamento e governance dei modelli                         |
| **AWS Deep Learning AMI**                   | Immagini EC2 ottimizzate per TensorFlow, PyTorch, ecc.         |
| **AWS Neuron**                              | Supporto per inferenza su hardware AWS Inferentia              |
| **Amazon EC2 Trn1/Inf1**                    | Istanza ottimizzata per training/inferenza ad alte prestazioni |

---

## 📊 Servizi di Analytics e Big Data

### Data lake, ingestion e trasformazione

| Servizio                                      | Descrizione                                |
| --------------------------------------------- | ------------------------------------------ |
| **[Amazon S3](/02-Storage-services/Amazon-S3.md)**                                 | Storage centrale per data lake             |
| **[AWS Glue](/07-IA-ML-Analytics/Analytics/AWS-Glue.md)**                   | ETL serverless e catalogo dati             |
| **AWS Data Pipeline**                         | Orchestrazione di flussi dati              |
| **AWS Lake Formation**                        | Creazione e governance sicura di data lake |
| **[AWS Data Exchange](/07-IA-ML-Analytics/Analytics/AWS-Data-Exchange.md)** | Acquisizione e uso di dati da parti terze  |

### Query, analytics e motori SQL

| Servizio                                                        | Descrizione                       |
| --------------------------------------------------------------- | --------------------------------- |
| **[Amazon Athena](/07-IA-ML-Analytics/Analytics/Amazon-Athena.md)**                           | Query SQL serverless su S3        |
| **[Amazon Redshift](/07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md)** | Data warehouse cloud scalabile    |
| **[Amazon EMR](/07-IA-ML-Analytics/Analytics/Amazon-EMR.md)**                                 | Hadoop/Spark gestito per Big Data |
| **[Amazon OpenSearch](/07-IA-ML-Analytics/Analytics/Amazon-OpenSearch.md)**                   | Ricerca e analisi full-text       |
| **[Amazon QuickSight](/07-IA-ML-Analytics/Analytics/Amazon-QuickSight.md)**                   | Business Intelligence e dashboard |

### Streaming e real-time analytics

| Servizio                                         | Descrizione                                      |
| ------------------------------------------------ | ------------------------------------------------ |
| **[Amazon Kinesis](/07-IA-ML-Analytics/Analytics/Amazon-Kinesis.md)**          | Ingestione e analisi di dati in streaming        |
| **[Amazon MSK](/07-IA-ML-Analytics/Analytics/Amazon-MSK.md)**                  | Kafka gestito su AWS                             |
| **[AWS Database Migration Service](/04-Database-services/AWS-Database-Migration-Service.md)** | Migrazione dati in tempo reale tra DB            |
| **Amazon DataZone**                              | Catalogo e condivisione dati a livello aziendale |

---

## 🔐 Sicurezza, Governance e Monitoraggio

| Servizio                            | Descrizione                                            |
|-------------------------------------|--------------------------------------------------------|
| **[AWS IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)**           | Controllo accessi granulari                           |
| **AWS CloudTrail**                  | Tracciamento delle azioni su dati e modelli           |
| **AWS Config**                      | Governance e conformità delle risorse                 |
| **AWS Audit Manager**               | Automazione di audit e report                         |

---

## 📌 Conclusioni

[AWS](/00-Intro/AWS.md) mette a disposizione un ampio ventaglio di servizi per costruire, addestrare e distribuire **soluzioni intelligenti** su larga scala. Dalle API AI pre-addestrate a strumenti avanzati per data scientist, fino a infrastrutture Big Data e motori analitici, AWS è un punto di riferimento per realizzare architetture **data-driven, predittive e automatizzate**.

> “Dai dati all'intelligenza artificiale: su AWS, ogni fase ha il suo servizio dedicato.”

