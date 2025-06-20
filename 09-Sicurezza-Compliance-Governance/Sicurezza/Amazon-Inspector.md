--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🧪 Amazon Inspector

## 📘 Cos'è e come funziona

**Amazon Inspector** è un servizio gestito che **scansiona automaticamente le risorse AWS** alla ricerca di **vulnerabilità di sicurezza**, **configurazioni errate** e **esposizioni non intenzionali**. È progettato per aiutare i team DevOps e SecOps a garantire che le risorse siano sicure e aggiornate, riducendo i rischi prima che diventino problemi reali.

Inspector funziona analizzando istanze **EC2**, **container su Amazon ECR**, e **funzioni Lambda**, eseguendo controlli di sicurezza basati su **database CVE**, configurazioni di rete e permessi IAM.

---

## ✨ Caratteristiche principali e vantaggi

- 🔍 **Rilevamento automatico di vulnerabilità (CVEs)** in EC2, container, Lambda
- 🔁 **Scansione continua** e senza agenti manuali (per molte risorse)
- 🔐 Analisi delle **permissività eccessive** in Lambda e configurazioni insicure
- 🧩 Integrazione nativa con **AWS Organizations**, **Security Hub**, **EventBridge**
- ⚠️ **Prioritizzazione delle vulnerabilità** in base a rischio e contesto
- 📜 **Report dettagliati** per remediation, audit e conformità
- 🚀 Nessuna interruzione delle applicazioni durante la scansione

---

## ✅ Vantaggi

- Identifica rapidamente le **vulnerabilità più critiche**
- Aiuta nella **conformità a standard** come CIS, PCI-DSS, HIPAA, ISO 27001
- Automatizza la sicurezza nel **ciclo di vita delle applicazioni**
- Riduce la superficie di attacco in ambienti cloud dinamici
- Abilita flussi di lavoro automatici di remediazione

---

## 🚀 Use case comuni

- 🔎 Scansione automatica di EC2 per patch mancanti o software obsoleto
- 📦 Analisi di immagini container su Amazon ECR prima del deployment
- ☁️ Identificazione di Lambda con IAM policy troppo permissive
- ⚙️ Monitoraggio continuo delle vulnerabilità in ambienti CI/CD
- 🧑‍💼 Verifiche di sicurezza automatizzate per audit e conformità

---

## 💰 Pricing

Amazon Inspector ha un prezzo basato su:

- Numero e tipo di risorse scansionate (EC2, container, Lambda)
- Frequenza delle scansioni

---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS           | Differenze rispetto a Amazon Inspector                             |
|------------------------|---------------------------------------------------------------------|
| **GuardDuty**          | Rileva minacce comportamentali e traffico sospetto, non CVE         |
| **Security Hub**       | Aggrega e prioritizza i risultati (anche da Inspector)              |
| **AWS Config**         | Traccia configurazioni, non esegue scansioni di vulnerabilità       |
| **Macie**              | Si concentra sui dati sensibili, non sui software vulnerabili       |

---

## 📌 Conclusioni

**Amazon Inspector** è uno strumento fondamentale per identificare e correggere vulnerabilità note prima che possano essere sfruttate. Automatizza la sicurezza nel cloud AWS, rendendo più semplice per i team DevOps e sicurezza mantenere infrastrutture aggiornate, sicure e conformi.

> “La sicurezza non è un'opzione extra — è parte del ciclo di sviluppo. Amazon Inspector la integra nel tuo flusso.”

