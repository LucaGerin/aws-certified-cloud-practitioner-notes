--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🔐 AWS Secrets Manager

## 📘 Cos'è e come funziona

**AWS Secrets Manager** è un servizio gestito che consente di **archiviare, gestire e ruotare automaticamente segreti** come password, chiavi API, credenziali per database e altri dati sensibili. Aiuta a **migliorare la sicurezza**, evitando di salvare segreti nel codice o nei file di configurazione.

Secrets Manager consente di definire politiche di accesso, monitorare l’uso dei segreti, integrarli con database e servizi AWS, e abilitare la **rotazione automatica tramite [AWS Lambda](AWS-Lambda.md)**.


NB: **Ruotare una access key**, per esempio per un utente **[IAM](AWS-IAM.md)**, in AWS significa sostituire in modo sicuro una chiave di accesso esistente con una nuova. Visto che AWS consente a un utente di avere fino a 2 access keys attive contemporaneamente, quando viene creata una nuova chiave, poi bisogna eliminare quella che si desidera sostituire. Infatti, la chiave "vecchia" rimane valida finché non viene disattivata o eliminata manualmente. AWS **non disattiva automaticamente** la chiave vecchia quando se ne crea una nuova.


---

## ✨ Caratteristiche principali e vantaggi

- 🔐 **Gestione centralizzata e sicura** di segreti e credenziali
- 🔁 **Rotazione automatica dei segreti** con configurazioni personalizzabili
- 🧩 **Integrazione con RDS, Redshift, DocumentDB** per gestione automatica delle credenziali
- 📜 **Controllo accessi IAM granulare**
- 🔎 **Audit delle operazioni** tramite AWS CloudTrail
- 📤 **Accesso via API, SDK, CLI e console**
- ✅ Supporta **versionamento** e ripristino di versioni precedenti dei segreti

---

## 🚀 Use case comuni

- 🔑 Gestione di **password di database** con rotazione automatica
- 🔐 Archiviazione di **token API e chiavi di accesso a servizi esterni**
- 🤖 Integrazione in **CI/CD pipeline** per leggere segreti in modo sicuro
- 🌍 Applicazioni serverless (es. Lambda) che recuperano credenziali al volo
- 📊 Conformità a standard di sicurezza (es. PCI-DSS, GDPR, HIPAA)

---

## 💰 Pricing

Il costo di AWS Secrets Manager include:

- 💲 **$0.40 al mese per ogni segreto attivo**
- 💲 Tariffe per il numero di **chiamate API GetSecretValue**
- 💲 Eventuale uso di **Lambda per la rotazione**


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS                  | Differenze rispetto a Secrets Manager                                |
|-------------------------------|------------------------------------------------------------------------|
| **SSM Parameter Store**       | Supporta variabili e config generiche, ma senza rotazione automatica |
| **AWS KMS**                   | Gestisce chiavi crittografiche, non segreti o credenziali             |
| **Secrets Manager**           | Ottimizzato per segreti critici con funzioni avanzate                 |

---

## 📌 Conclusioni

**AWS Secrets Manager** è una soluzione potente e sicura per gestire segreti nel cloud, migliorando la **protezione dei dati sensibili** e riducendo la complessità nella gestione delle credenziali. È ideale per ambienti **dinamici, automatizzati e ad alta sicurezza**.

> “Gestire i segreti nel codice è rischioso. Secrets Manager li protegge, li ruota e li semplifica.”

