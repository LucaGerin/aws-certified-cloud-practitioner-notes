--> [AWS](AWS.md)  -  [Data Analytics](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Amazon QuickSight

## 📊 Cos’è e come funziona

**Amazon QuickSight** è il servizio SaaS di **Business Intelligence (BI) cloud-native di AWS**, progettato per consentire la **visualizzazione interattiva dei dati** presi dalle data sources su AWS o on-premise, la creazione di **dashboard dinamiche** e l’**analisi avanzata con intelligenza artificiale**. QuickSight permette a utenti tecnici e business di esplorare, analizzare e condividere insight dai dati senza dover gestire infrastrutture.

QuickSight si connette a molteplici fonti dati (es. [S3](Amazon-S3.md), [Redshift](Amazon-Redshift-e-Redshift-Serverless.md), [Athena](Amazon-Athena.md), [RDS](Amazon-RDS.md), MySQL, Salesforce) e consente la creazione di dashboard aggiornate automaticamente, accessibili via browser o embedded in applicazioni.

---

## ✨ Caratteristiche principali e vantaggi

- ⚡ **Performance elevate** grazie a SPICE (motore in-memory)
- 📈 **Dashboard interattive e responsive**, accessibili via web e mobile
- 🤖 **Analisi potenziate da ML** (forecasting, anomaly detection, natural language query)
- 🔌 **Connettività nativa** con servizi AWS: [Athena](Amazon-Athena.md), [Redshift](Amazon-Redshift-e-Redshift-Serverless.md), [S3](Amazon-S3.md), [RDS](Amazon-RDS.md), etc.
- 🔐 **Controllo accessi a livello di riga e colonna**
- 📦 **Embedded BI**: integrazione diretta in portali, app, CRM
- 📤 **Esportazione in PDF, CSV, Excel**
- 🔁 **Refresh automatico** dei dati con pianificazione
- 🌍 Supporto multilingua, multiregione e multitenant

**Vantaggi principali:**
- Nessun server da gestire o aggiornare
- Prezzo competitivo basato sugli utenti attivi (no licenze fisse)
- Tempo di setup e pubblicazione molto rapido
- Accessibile anche da utenti non tecnici
- Dashboard facilmente condivisibili via URL

---

## 🚀 Use case comuni / ideali

- **Cruscotti aziendali** per KPI operativi e finanziari
- **Analisi del traffico sulle applicazioni** per scoprire trend nel loro utilizzo e statistiche
- **Monitoraggio vendite, marketing e campagne di marketing, supply chain**
- **Dashboard self-service** per team interni
- **Embedding di report e visualizzazioni** in applicazioni web
- **Analisi avanzata con AI** per rilevamento anomalie e previsioni
- **Reporting automatizzato** per clienti o stakeholder
- **Visualizzazione dati IoT, log, dati su S3/Redshift**

---

## 💰 Pricing

QuickSight adotta un modello **pay-per-session** (per utenti Reader) e **mensile** (per utenti Author):

| Tipo utente | Costo                                  | Funzioni principali                   |
| ----------- | -------------------------------------- | ------------------------------------- |
| **Reader**  | $0.30/session (fino a $5/mese max)     | Visualizza dashboard, esporta, filtra |
| **Author**  | $18/mese (mensile) o $9/mese (annuale) | Crea, pubblica, modifica dashboard    |

> Il motore **SPICE** ha anche un costo associato in base alla quantità di dati immagazzinati.

---

## 🔄 Confronto con altri servizi AWS simili

| Servizio                        | Finalità principale                         | Differenze rispetto a QuickSight                     |
|--------------------------------|--------------------------------------------|------------------------------------------------------|
| **[Amazon Athena](Amazon-Athena.md)**   | Query SQL serverless                       | Query engine, non visualizzazione                     |
| **[Amazon Redshift](Amazon-Redshift-e-Redshift-Serverless.md)** | Data warehouse OLAP                        | Fonte dati, non BI tool                               |
| **AWS Glue + [SageMaker](Amazon-SageMaker.md)**  | Preprocessing + ML avanzato              | Pipeline e modelli, non dashboard interattive        |
| **Amazon OpenSearch Dashboards** | Visualizzazione log e ricerca              | Ottimizzato per log, non per BI generalista           |

---

## 📌 Conclusioni

**Amazon QuickSight** è la soluzione BI moderna di AWS per aziende che vogliono **rendere accessibili gli insight** su larga scala, sia internamente che esternamente, senza dover investire in infrastrutture costose. Con funzionalità avanzate, intelligenza artificiale integrata e flessibilità di embedding, QuickSight si adatta sia a **startup** che a **grandi imprese**.

> “Dai ai tuoi dati il potere di raccontare storie — con Amazon QuickSight.”
