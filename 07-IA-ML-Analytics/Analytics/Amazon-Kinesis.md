--> [AWS](/00-Intro/AWS.md)  -  [Data Analytics](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon Kinesis

**Amazon Kinesis** è una suite di servizi [AWS](/00-Intro/AWS.md) pensata per la **raccolta, elaborazione e analisi in tempo reale** di grandi volumi di dati in streaming, come log, clickstream, dati IoT, eventi applicativi e metriche.  
Kinesis permette di costruire applicazioni che reagiscono ai dati **appena generati**, senza doverli prima salvare in un database o in [S3](/02-Storage-services/Amazon-S3.md).

---

## 🧩 Componenti principali

Amazon Kinesis è suddiviso in più servizi specifici:

| Componente                     | Descrizione                                               |
| ------------------------------ | --------------------------------------------------------- |
| **Kinesis Data Streams (KDS)** | Ingestione e bufferizzazione di dati in tempo reale       |
| **Kinesis Data Firehose**      | Ingestione + delivery automatica verso [S3](/02-Storage-services/Amazon-S3.md), [Redshift](/07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md), ecc. |
| **Kinesis Data Analytics**     | Query SQL in tempo reale sui dati in streaming            |
| **Kinesis Video Streams**      | Streaming, archiviazione e analisi di video in AWS        |

---

## 🌟 Caratteristiche principali

- **Ingestione in tempo reale** di milioni di eventi al secondo
- **Bassa latenza (<1 secondo)** per analisi e risposta immediata, in real time
- **Scalabilità automatica** o configurabile (a seconda del servizio)
- **Retention configurabile** (fino a 365 giorni per KDS)
- **Integrazione diretta** con [AWS Lambda](/01-Compute-options/AWS-Lambda.md), [S3](/02-Storage-services/Amazon-S3.md), [Redshift](/07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md), [OpenSearch](/07-IA-ML-Analytics/Analytics/Amazon-OpenSearch.md), etc.
- **Supporto per partition key** e ordinamento dei dati nei flussi
- **Pay-per-use**: paghi solo per i dati elaborati o trasportati

Kinesis Streams tiene i dati di default per 24 ore, ma ha un massimo di retention di 365 giorni.

---

## ✅ Vantaggi

- **Real-time by design**: perfetto per applicazioni moderne reattive
- **Flessibilità**: puoi scegliere tra stream raw, delivery gestito o analisi diretta
- **Facile integrazione** con l’ecosistema AWS
- **Gestione automatica della scalabilità** con Firehose
- **Costo efficiente** per grandi volumi rispetto a soluzioni personalizzate
- **Alta affidabilità** con replicazione automatica dei dati

---

## 🧱 Come vengono gestiti e conservati i dati in Kinesis Streams

In **Amazon Kinesis Data Streams**, i dati sono suddivisi e conservati in **shard**, che sono le unità fondamentali di throughput e parallelismo del servizio.  
Ogni shard può gestire **fino a 1 MB/s in scrittura** e **2 MB/s in lettura**, e conserva i dati in ordine di arrivo per un periodo configurabile (di default 24 ore, estendibile fino a 365 giorni).  
Ogni record inviato a Kinesis viene associato a una **partition key**, che determina in quale shard verrà immagazzinato. Questo meccanismo garantisce **l’ordinamento interno** dei dati all’interno dello stesso shard e permette un **bilanciamento del carico** efficiente tra produttori e consumatori.  
Gli shard possono essere **aumentati o ridotti manualmente** (resharding) o gestiti automaticamente in base al carico, e ogni consumatore può leggere i dati sequenzialmente o in parallelo in base alla strategia di elaborazione adottata (es. fan-out, enhanced fan-out).

![kinesis shards](img/kinesis-streams.png)

---

## 🔥 Amazon Kinesis Data Firehose

**Kinesis Data Firehose** è il componente della famiglia Kinesis pensato per il **caricamento continuo e completamente gestito di dati in tempo reale** verso destinazioni come **Amazon S3, [Redshift](/07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md), OpenSearch, e Splunk**.  
A differenza di Kinesis Data Streams, non richiede gestione di shard o scrittura manuale del codice per il consumo: basta **configurare una destinazione** e Firehose si occupa della **bufferizzazione, trasformazione (opzionale) e consegna dei dati**.  
I dati sono processati e consegnati alla destinazione in real-time (sotto i 60 secondi).  
Si possono specificare trasformazioni personalizzate da effettuare sui dati con [Lambda](/01-Compute-options/AWS-Lambda.md) prima del caricamento.  
È ideale per **pipeline ETL semplificate**, data lake ingest e archiviazione log.  
Firehose supporta anche **conversione in formato Parquet o ORC**, **compressione** e l'integrazione con **Lambda** per trasformazioni in-flight.  
È un servizio completamente **serverless**: scala automaticamente con il volume di dati e si paga solo per ciò che si trasferisce.

![kinesis firehose](img/kinesis-firehouse.png)

Firehose può essere usato per real-time analytics, data lake feeding, Log Data management, IoT Data Integration.

---
### Kinesis Data Analytics

Kinesis Data Analytics è un servizio gestito che consente di **analizzare flussi di dati in tempo reale utilizzando SQL standard o Apache Flink**. 

È progettato per integrarsi facilmente con Kinesis Data Streams e Kinesis Data Firehose, permettendo di eseguire trasformazioni, aggregazioni e filtri sui dati in transito senza doverli prima salvare. Gli utenti possono creare applicazioni di streaming analytics per casi d'uso come il rilevamento di anomalie, il monitoraggio in tempo reale o la creazione di metriche personalizzate, senza dover gestire infrastrutture complesse. 
Inoltre, grazie al supporto per Apache Flink, è possibile implementare logiche avanzate in Java o Scala per elaborazioni più sofisticate.


---

## 🚀 Use Case di Kinesis

- **Monitoraggio in tempo reale** (es. metriche di sistema, applicazioni, utenti)
- **Analisi di clickstream** per e-commerce, advertising, UX
- **Integrazione dati IoT** da sensori, dispositivi connessi, veicoli
- **Elaborazione di log e auditing** (es. sicurezza, debug, compliance)
- **Personalizzazione dinamica** di contenuti e raccomandazioni
- **Alert e risposte automatiche** (es. anomalie, frodi)

---

## 🧠 Scenari in cui è la scelta ideale

Amazon Kinesis è particolarmente indicato quando:

- Hai bisogno di **risposte in tempo reale** (monitoraggio, azioni automatiche)
- Stai costruendo **architetture event-driven**
- Vuoi **evitare batch ETL** e passare all’elaborazione continua
- Lavori con **volumi elevati e costanti di dati** da fonti distribuite
- Vuoi **minimizzare la latenza** tra evento generato ed elaborato

---

## 🔄 Confronto con altri servizi simili

| Servizio               | Quando usarlo                                | Differenze principali                            |
|------------------------|---------------------------------------------|-------------------------------------------------|
| **[Amazon Kinesis](/07-IA-ML-Analytics/Analytics/Amazon-Kinesis.md)**      | Streaming dati in real-time                   | Suite completa per stream ingest, process, store |
| **[Amazon MSK](/07-IA-ML-Analytics/Analytics/Amazon-MSK.md)**              | Quando usi Kafka o vuoi compatibilità Kafka, soprattutto adatto per big data processati in batch  | Gestione Kafka 100% compatibile                   |
| **[Amazon SQS](/05-Development-Messaging-Deploying/Amazon-SQS.md)**              | Per code di messaggi asincroni                | Buffering con maggiore durata, meno real-time     |
| **[Amazon EventBridge](/05-Development-Messaging-Deploying/Amazon-EventBridge.md)** | Per eventi strutturati tra servizi AWS        | Event routing, non adatto a volumi elevati        |
| **[AWS Lambda](/01-Compute-options/AWS-Lambda.md)**               | Per reagire a eventi                         | Ottimo in combinazione con Kinesis (trigger)      |
| **[Amazon SNS](/05-Development-Messaging-Deploying/Amazon-SNS.md)**               | Per notifiche push multi-target              | Meno adatto a flussi continui o logging           |

---

## 📌 Conclusioni

Amazon Kinesis è la soluzione AWS più potente per **data streaming in tempo reale**. Che tu voglia analizzare log, integrare sensori IoT o creare sistemi reattivi, Kinesis ti offre gli strumenti giusti per costruire **applicazioni data-driven**, scalabili e intelligenti.

> “Con Kinesis, ogni secondo conta — perché ogni dato è utile appena nasce.”
