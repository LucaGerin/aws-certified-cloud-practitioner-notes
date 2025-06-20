--> [AWS](00-Intro/AWS.md)  -  [Intelligenza Artificiale e Machine Leraning](07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon SageMaker

## 🧠 Cos’è e come funziona

**Amazon SageMaker** è la piattaforma AWS completamente gestita per **costruire, addestrare e distribuire modelli di [Machine Learning](07-IA-ML-Analytics/AI e ML/Machine-Learning.md) (ML)** su larga scala. 
SageMaker fornisce un ambiente integrato che supporta l'intero ciclo di vita del ML: 
- preparazione dei dati
- selezione degli algoritmi (ce ne sono molti inclusi)
- addestramento con infrastrutture ottimizzate
- tuning automatizzato
- deployment (Su istanze [Amazon EC2](01-Compute-options/Amazon-EC2.md) ottimizzate, o serverless, o su device edge)
- monitoraggio dei modelli in produzione.

Puoi lavorare con SageMaker da:
- **Console web** con interfaccia grafica
- **Jupyter Notebook gestiti**
- **SDK Python (boto3 e sagemaker-python-sdk)**
- **API REST**

---

## ✨ Caratteristiche principali e vantaggi

- 📦 **Notebook gestiti**: ambienti Jupyter pronti all’uso, scalabili e sicuri
- 🚀 **Training distribuito**: su CPU o GPU, anche su centinaia di istanze
- 🧪 **AutoML (SageMaker Autopilot)**: crea modelli ML senza scrivere codice
- 🎯 **Tuning automatico degli iperparametri**
- 🧱 **Modelli preaddestrati e marketplace**: modelli disponibili da Hugging Face, TensorFlow Hub, PyTorch Hub e terze parti
- 🧬 **SageMaker JumpStart**: template pronti per uso con modelli SOTA
- 🛠️ **Pipelines e MLOps integrati**: versionamento, workflow, CI/CD, monitoraggio drift
- 🔁 **Deployment gestito**: endpoint REST per inferenza in tempo reale o batch
- 📈 **Monitoraggio e explainability**: bias detection, model explainability, drift

**Vantaggi principali:**
- Riduce **il time-to-market** di soluzioni ML
- Adatto sia a **data scientist esperti** che a **principianti**
- Supporta librerie open source: TensorFlow, PyTorch, scikit-learn, XGBoost
- Integrazione profonda con [Amazon S3](02-Storage-services/Amazon-S3.md), [Amazon Redshift](07-IA-ML-Analytics/Analytics/Amazon-Redshift-e-Redshift-Serverless.md), [AWS Glue](07-IA-ML-Analytics/Analytics/AWS-Glue.md), [Amazon Athena](07-IA-ML-Analytics/Analytics/Amazon-Athena.md), Amazon ECR, [AWS IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), [Amazon CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md)
- Sicurezza enterprise-ready: crittografia, audit, [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md), [AWS KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)

---

## 🚀 Use case comuni / ideali

- 🔍 **Analisi predittiva** (churn, vendite, manutenzione predittiva, insurance)
- Creazione di un **motore di raccomandazione**
- 🧾 **Elaborazione linguaggio naturale (NLP)**: analisi sentiment, chatbot, classificazione
- 👁️‍🗨️ **Computer vision**: rilevamento oggetti, riconoscimento immagini, OCR
- 🧪 **Bioinformatica e genomica**: classificazione sequenze, predizione proteine
- 📦 **Supply chain optimization** e previsione domanda
- 📊 **Fraud detection**, scoring finanziario, raccomandazioni
- 🧠 **Training e hosting di LLM (Large Language Models)** con Deep Learning Containers

---

## 💰 Pricing

Amazon SageMaker adotta un **modello pay-per-use**, con tariffe diverse per:

| Componente                        | Prezzo basato su                       |
|----------------------------------|----------------------------------------|
| Notebook istanze                 | Tipo di istanza (es. ml.t3.medium)     |
| Training job                     | Durata, tipo di istanza, storage EBS   |
| Inference endpoint               | Tempo attivo, tipo di istanza          |
| Batch transform job              | Dati processati + tempo di esecuzione  |
| SageMaker Studio (IDE)           | Solo le risorse sottostanti utilizzate |
| SageMaker Autopilot              | Numero di job creati e tipo istanza    |
| SageMaker Serverless Inference   | Numero di richieste e risorse allocate |

> Esiste anche un **livello gratuito per 2 mesi**, con istanze limitate (es. ml.t2.medium).

---

## 🔄 Confronto con altri servizi AWS simili

| Servizio                                | Finalità principale                     | Differenze rispetto a SageMaker                           |
|-----------------------------------------|------------------------------------------|------------------------------------------------------------|
| [AWS Glue](07-IA-ML-Analytics/Analytics/AWS-Glue.md) + [Amazon Athena](07-IA-ML-Analytics/Analytics/Amazon-Athena.md) | Preparazione e interrogazione dati       | Nessun addestramento modelli                              |
| Amazon Forecast   | Previsione temporale                     | ML preconfigurato, limitato a forecasting                  |
| [Amazon Comprehend](07-IA-ML-Analytics/AI e ML/Amazon-Comprehend.md) | NLP-as-a-service                         | API specifiche, no addestramento personalizzato            |
| [Amazon Rekognition](07-IA-ML-Analytics/AI e ML/Amazon-Rekognition.md) | Visione artificiale as-a-service         | API pronte, senza gestione modello                         |
| **SageMaker JumpStart**                 | Modelli pre-addestrati                   | È una parte di SageMaker, utile per iniziare               |
| **[Amazon EC2](01-Compute-options/Amazon-EC2.md)** + Jupyter custom         | Ambiente personalizzato per ML           | Nessuna gestione, nessuna scalabilità o MLOps integrati    |

---

## 📌 Conclusioni

**Amazon SageMaker** è la piattaforma ML più completa su AWS. Offre tutto ciò di cui hai bisogno per costruire e distribuire modelli intelligenti, con strumenti avanzati per **data scientist, ingegneri ML e team di business**. È una soluzione potente, flessibile e sicura per portare l’intelligenza artificiale nei tuoi progetti cloud-native.

> “Con SageMaker, il machine learning smette di essere un esperimento e diventa produzione.”
