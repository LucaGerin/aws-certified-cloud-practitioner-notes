--> [AWS](00-Intro/AWS.md)  -  [Sicurezza](09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🕵️‍♂️ Amazon Detective

## 📘 Cos'è e come funziona

**Amazon Detective** è un servizio gestito che, anche facendo uso di AI, aiuta i team di sicurezza a **indagare più rapidamente su potenziali incidenti di sicurezza** in AWS. 
Raccoglie automaticamente dati e log da servizi come **Amazon GuardDuty**, **AWS CloudTrail**, **VPC Flow Logs** e **AWS Config**, e li correla per creare una **vista interattiva e approfondita degli eventi** legati a un'entità (es. un utente IAM, un'istanza EC2 o un indirizzo IP).

Con Amazon Detective, è possibile **esplorare graficamente la cronologia degli eventi**, identificare il comportamento anomalo e comprendere la causa principale di un potenziale attacco o accesso non autorizzato.

![Detective example](detective-example.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🧠 **Analisi automatica e correlazione di dati di sicurezza** da più servizi AWS
- 🔍 **Visualizzazione dettagliata** del comportamento delle risorse nel tempo
- 🧩 **Integrazione diretta con Amazon GuardDuty** e AWS Security Hub
- 🧭 **Esplorazione interattiva** degli eventi (timeline, grafi, relazioni tra entità)
- 🕓 **Storico dei dati** mantenuto fino a 1 anno
- 🚫 Nessuna configurazione o agente da installare
- 📦 Basato su **grafi di conoscenza (graph-based engine)** per correlazioni efficienti

---

## ✅ Vantaggi

- Accelera la **fase di investigazione post-incident**
- Riduce il tempo necessario a comprendere la **causa e l'impatto di un attacco**
- Evita l'analisi manuale di enormi quantità di log
- Aiuta i team di sicurezza a **collaborare e prendere decisioni più informate**
- Si integra perfettamente con flussi **SIEM e SOAR** esistenti

---

## 🚀 Use case comuni

- 🔎 Investigazione di alert provenienti da **GuardDuty o Security Hub**
- 👤 Analisi delle attività di un utente IAM sospetto
- 🌐 Tracciamento di **connessioni di rete insolite** in uscita da un'istanza EC2
- 📁 Analisi delle modifiche a configurazioni o policy IAM
- ⏳ Ricostruzione temporale di un incidente per auditing o forensics

---

## 💰 Pricing

Amazon Detective ha un **modello di pricing basato sul volume dei dati elaborati**:

- Costo per GB di dati ingeriti e analizzati (da CloudTrail, [[VPC](03-CDN-e-Networking/Amazon-VPC.md)](Amazon-VPC.md) Flow Logs, GuardDuty)
- Nessun costo iniziale o minimo mensile

---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS         | Differenze rispetto a Amazon Detective                            |
|----------------------|--------------------------------------------------------------------|
| **GuardDuty**        | Rileva minacce, ma non aiuta a indagarne la causa                 |
| **Security Hub**     | Aggrega e prioritizza gli alert, ma non offre analisi grafiche     |
| **CloudTrail**       | Registra eventi, ma richiede analisi manuale                      |
| **Inspector**        | Esegue vulnerability scanning, non analisi di incidenti           |

---

## 📌 Conclusioni

**Amazon Detective** è un potente strumento per investigare in modo **efficiente e visuale** su problemi di sicurezza nel cloud AWS. È pensato per aiutare i team a **capire rapidamente cosa è successo, come, quando e con quale impatto**, migliorando le capacità di risposta e riducendo il tempo di analisi forense.

> “Quando ricevi un alert, non basta sapere *che* è successo — serve sapere *perché*. Amazon Detective lo scopre per te.”

