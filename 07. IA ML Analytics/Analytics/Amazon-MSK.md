--> [AWS](AWS.md)  -  [Data Analytics](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon MSK (Managed Streaming for Apache Kafka)

## 🔄 Cos'è e come funziona

**Amazon MSK (Managed Streaming for Apache Kafka)** è un servizio completamente gestito che consente di **eseguire cluster Apache Kafka** su AWS, senza doversi occupare della configurazione, scalabilità, provisioning, upgrades, sicurezza o manutenzione.

MSK offre **Kafka open-source 100% compatibile**, ma con tutta l'affidabilità, integrazione e scalabilità dell'infrastruttura AWS. Puoi utilizzare i tuoi tool Kafka esistenti (produttori, consumatori, connector) e continuare a operare come su un cluster self-hosted, con l’aggiunta del supporto AWS per la gestione automatica.

![MSK example](MSK-example.png)

Amazon Managed Streaming for Apache Kafka (MSK) è adatto soprattutto al processing di big data in batch, mentre per processare streaming di dati in real-time lo strumento indicato è [Amazon Kinesis Data Streams](Amazon-Kinesis.md).

---

## ✨ Caratteristiche principali e vantaggi

- ✅ **100% compatibile con Apache Kafka** (stesse API, CLI, protocolli)
- 🔒 **Sicurezza gestita**: crittografia a riposo e in transito, [IAM](AWS-IAM.md), [VPC](Amazon-VPC.md), TLS, SASL/SCRAM
- ⚙️ **Provisioning automatico** dei broker, storage, networking
- 📈 **Monitoraggio nativo** con Amazon CloudWatch
- 🔁 **Alta disponibilità e fault tolerance** su più zone di disponibilità (AZ)
- 🔄 **Integrazione con Kafka Connect**, Kinesis Data Analytics, [AWS-Lambda](AWS-Lambda.md), [Glue](AWS-Glue.md), [Firehose](Amazon-Kinesis.md)
- 🛠️ Supporto per **Apache ZooKeeper** gestito
- 📦 Possibilità di utilizzare **MSK Serverless**, senza cluster da gestire

---

## 🚀 Use case comuni / ideali

- **Architetture event-driven** basate su Kafka
- **Ingestione dati in tempo reale** da web, IoT, mobile, app
- **Integrazione di microservizi** tramite code e topic Kafka
- **Streaming analytics** con Kinesis Data Analytics o Apache Flink
- **Pipeline ETL moderne** che reagiscono a eventi
- **Audit e tracciamento eventi** distribuiti tra sistemi

---

## 💰 Pricing

Amazon MSK offre due modelli:

### MSK Provisioned
- Prezzo per ora in base a:
  - Numero e tipo di broker EC2
  - Volume di storage (per broker)
  - Trasferimento dati tra AZ
- Backup automatici inclusi

### MSK Serverless
- Paghi in base a:
  - **Throughput effettivo** (MB/s in e out)
  - **Storage utilizzato**
  - Non serve pre-provisioning di broker o storage

> MSK Serverless è ideale per applicazioni **intermittenti o a carico variabile**.


---

## 🔄 Confronto con servizi simili su AWS

| Servizio             | Finalità principale                              | Differenze rispetto a MSK                                   |
|----------------------|---------------------------------------------------|--------------------------------------------------------------|
| **[Amazon Kinesis](Amazon-Kinesis.md)**   | Streaming AWS-native, analisi eventi              | Più semplice da usare, meno flessibile, non Kafka compatibile|
| **[Amazon EventBridge](Amazon-EventBridge.md)** | Event routing strutturato tra servizi AWS       | Per eventi aziendali strutturati, no buffer persistente      |
| **[Amazon SQS](Amazon-SQS.md)/[Amazon SNS](Amazon-SNS.md)**   | Code di messaggi e notifiche push                 | Adatto per pattern asincroni più semplici                    |
| **[Amazon EMR](Amazon-EMR.md) + Kafka** | Kafka su cluster EMR gestito manualmente        | Più controllo, ma anche più gestione                         |

---

## 📌 Conclusioni

**Amazon MSK** unisce la potenza di Apache Kafka con la semplicità della gestione AWS. È la scelta ideale per chi ha già esperienza con Kafka e desidera **migrare su cloud** senza rinunciare a flessibilità, performance e compatibilità.

> “Con MSK, Kafka diventa cloud-native: nessun cluster da gestire, solo stream da far fluire.”
