--> [AWS](AWS.md)  -  [Compute Options](AWS-Compute-Options.md)
# AWS Lambda

![lambda](lambda.png)
AWS Lambda è un servizio di **calcolo serverless** che consente di eseguire codice in risposta a eventi, senza dover gestire server o infrastrutture sottostanti. È progettato per eseguire funzioni brevi, leggere e altamente scalabili in risposta a trigger provenienti da altri servizi AWS o da fonti esterne.

---

## 🔧 Cos'è e come funziona

Lambda consente di scrivere funzioni che vengono eseguite **on demand**, in risposta a eventi come:
- Caricamento di un file su [Amazon S3](Amazon-S3.md)
- Inserimento o aggiornamento di dati in [Amazon DynamoDB](Amazon-DynamoDB.md)
- Chiamata HTTP tramite Amazon API Gateway
- Eventi di flusso da Amazon Kinesis o Amazon EventBridge

Il codice può essere caricato direttamente come script o impacchettato in **container Docker**, e Lambda lo esegue in un ambiente isolato e temporaneo, garantendo **scalabilità automatica** e **alta disponibilità**.

---

## ⭐ Caratteristiche principali e vantaggi

- **Event-driven:** Esecuzione automatica in risposta a trigger da oltre 200 servizi AWS
- **Scalabilità automatica:** Lambda avvia automaticamente istanze parallele in base al volume degli eventi
- **Supporto multi-linguaggio:** Node.js, Python, Java, Go, Ruby, .NET e container personalizzati
- **Gestione automatica delle risorse:** Nessuna necessità di provisioning, patching o gestione server
- **Durabilità e disponibilità:** Funzioni replicate su più zone di disponibilità
- **Prezzi a consumo:** Si paga solo per i millisecondi di esecuzione e la quantità di memoria utilizzata

---

## 🚀 Use Cases

- **Elaborazione file in S3:** Attivare funzioni quando un file viene caricato su [Amazon S3](Amazon-S3.md)
- **Backend serverless per applicazioni web o mobile**
- **Integrazione tra servizi [AWS](AWS.md):** orchestrare flussi tra S3, DynamoDB, SNS, SQS, ecc.
- **Automazione IT:** esecuzione pianificata (cron jobs), controllo e auditing
- **Costruzione di API REST** o GraphQL tramite Amazon API Gateway + Lambda

---

## 💰 Pricing

- **Basato sull’esecuzione:** Il costo è proporzionale a:
  - Numero di richieste
  - Durata dell’esecuzione (in millisecondi)
  - Memoria allocata (da 128 MB a 10 GB)
- **Free Tier:** 1 milione di richieste gratuite e 400.000 GB-secondi al mese

⚠️ I costi possono aumentare con un elevato numero di chiamate concorrenti o lunghi tempi di esecuzione.

---

## 🔐 Sicurezza

- **IAM per accesso controllato:** Le funzioni Lambda possono avere ruoli IAM dedicati (execution role)
- **Isolamento per funzione:** Ogni esecuzione avviene in un ambiente isolato
- **VPC Integration:** Possibilità di eseguire funzioni Lambda in reti private
- **Logging e audit:** Integrazione nativa con Amazon CloudWatch Logs e AWS X-Ray

---

## 🔄 Confronto con servizi simili in AWS

| Servizio        | Tipo                  | Quando usarlo                                              |
|------------------|------------------------|------------------------------------------------------------|
| **Lambda**       | Serverless Function    | Per task brevi, eventi asincroni e applicazioni scalabili  |
| **Fargate**      | Serverless container   | Per workload containerizzati più complessi o persistenti   |
| **ECS/EKS**      | Container orchestrati  | Quando serve controllo completo su container e networking  |
| **EC2**          | Istanze gestite        | Per app legacy o custom che richiedono accesso al sistema  |

---

## 📊 Integrazioni e strumenti consigliati

- **Monitoring e tracing:** Amazon CloudWatch Logs, AWS X-Ray, Datadog
- **CI/CD:** AWS CodePipeline, GitHub Actions, Serverless Framework
- **Orchestrazione di funzioni:** AWS Step Functions
- **Gestione pacchetti:** Layers per riutilizzare librerie tra più funzioni

---

## 📌 Best Practices

- Tenere le funzioni piccole e specializzate (principio *single responsibility*)
- Limitare il cold start usando VPC configurati correttamente e runtime leggeri
- Gestire i secret tramite AWS Secrets Manager o Parameter Store
- Utilizzare i **timeout appropriati** per evitare esecuzioni lunghe e costose
- Abilitare il **monitoraggio proattivo** con CloudWatch Alarms

---

AWS Lambda è ideale per applicazioni event-driven, flussi di lavoro automatizzati, microservizi e sviluppo agile, offrendo un bilanciamento ottimale tra **costo**, **scalabilità** e **manutenzione nulla**.
