--> [AWS](00-Intro/AWS.md)  -  [Auditing, Monitoring, Logging](08-Auditing-Monitoring-Logging/Auditing-Monitoring-Logging.md)
# 🩺 AWS Health Dashboard

## 📘 Cos’è e come funziona

**AWS Health Dashboard** è un servizio che fornisce **visibilità centralizzata e in tempo reale** sullo stato di salute dei servizi AWS e sull’impatto che eventuali eventi (e.g., la manutenzione programmata da AWS) possono avere sulle tue risorse specifiche. 
È progettato per aiutare sviluppatori, DevOps e team IT a **monitorare e rispondere rapidamente** a problemi di disponibilità, manutenzioni pianificate, cambiamenti di configurazione e altri eventi rilevanti.

Esistono due versioni:
- 🔍 **AWS Health Dashboard (public)**: mostra lo stato generale dei servizi AWS (disponibile pubblicamente).
- 🏥 **AWS Health Dashboard – Your Account**: mostra eventi **specifici per il tuo account**, inclusi impatti sulle tue risorse.

---

## ✨ Caratteristiche principali e vantaggi

- 📡 **Monitoraggio eventi in tempo reale** che impattano i servizi AWS utilizzati
- 📄 **Dettagli specifici per account**: impatti su istanze EC2, RDS, Lambda, ecc.
- 📅 **Storico eventi** e accesso a notifiche passate
- 🔧 **Manutenzioni programmate**: avvisi sulle modifiche pianificate da AWS
- 📤 **Integrazione con CloudWatch Events / EventBridge** per automatizzare le risposte
- 📬 **Notifiche configurabili** tramite SNS, email, Lambda o dashboard personalizzate
-  Può essere acceduta da AWS oppure tramite una AWS Heath API.

---

## 🚀 Use case comuni / ideali

- 🧭 **Identificare rapidamente problemi in corso** su regioni o servizi AWS
- 📍 **Ricevere alert personalizzati** quando le proprie risorse sono impattate
- 🧑‍💻 **Assistere nelle operazioni di troubleshooting**
- 🛠️ **Prepararsi a manutenzioni pianificate** su infrastrutture critiche
- 📊 **Raccogliere dati per audit o report di disponibilità**

---

## 🛠️ Integrazione con altri servizi

AWS Health Dashboard si integra facilmente con:

- **Amazon EventBridge**: per attivare azioni automatiche in risposta agli eventi (es. invio alert, esecuzione di runbook)
- **AWS Organizations**: per visualizzare la salute dell’intera organizzazione
- **AWS Lambda**: per automatizzare risposte personalizzate agli eventi
- **AWS CLI e SDK**: per consultare eventi programmaticamente

---

## 🔐 Accesso e sicurezza

- L’accesso al **dashboard pubblico** è libero
- Il **dashboard specifico per account** richiede accesso autenticato con permessi [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) appropriati.
- I dati visibili sono **privati e personalizzati** per il tuo account AWS.

---
## Confronto con CloudWatch

Il servizio che ti informa su eventi di servizio, interruzioni, modifiche pianificate e notifiche relative al tuo account è **AWS Health Dashboard**.

Sebbene sia possibile configurare **CloudWatch Alarms** per rilevare indirettamente alcune interruzioni di servizio (ad esempio tramite cali di metriche), **solo AWS Health Dashboard** fornisce informazioni **ufficiali e tempestive** su:
- problemi operativi in corso,
- manutenzioni programmate,
- modifiche che potrebbero influenzare le tue risorse,
- notifiche specifiche per il tuo account.

> In sintesi: **CloudWatch ti aiuta a reagire a ciò che accade, mentre AWS Health Dashboard ti informa in anticipo su ciò che sta per accadere.**

---
## 📌 Conclusioni

**AWS Health Dashboard** è uno strumento essenziale per mantenere alta la disponibilità e la resilienza dei tuoi workload su AWS. Fornisce una visione chiara e tempestiva degli eventi che possono influire sulle tue risorse e ti aiuta a reagire in modo rapido e informato.

> “Con AWS Health Dashboard, sai sempre cosa succede — prima che diventi un problema.”

