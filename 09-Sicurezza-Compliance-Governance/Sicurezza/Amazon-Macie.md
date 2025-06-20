--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🕵️ Amazon Macie

## 📘 Cos'è e come funziona

**Amazon Macie** è un servizio gestito di **sicurezza e privacy dei dati** che utilizza il **machine learning** per identificare automaticamente **dati sensibili** memorizzati in Amazon S3, come informazioni personali (PII - Personally Identifiable Information), dati finanziari o credenziali.

Macie esegue la **scansione continua dei bucket S3**, classifica i dati e segnala potenziali problemi di sicurezza o conformità, come file pubblicamente accessibili o contenenti dati sensibili non cifrati.

![macie](macie.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🧠 **Machine learning per la classificazione automatica dei dati**
- 🔍 Rilevamento di **informazioni sensibili** (es. numeri di carta di credito, e-mail, codice fiscale)
- 📁 **Analisi automatica dei bucket S3**, inclusi permessi e configurazioni
- ⚠️ **Avvisi in tempo reale** su anomalie e rischi
- 📊 **Dashboard dettagliata** per visualizzare i risultati e le tendenze
- 🔄 Integrazione con **AWS Security Hub**, **EventBridge**, e **CloudWatch**

### ✅ Vantaggi

- Migliora la **visibilità e il controllo dei dati sensibili**
- Supporta la conformità a standard come **GDPR**, **HIPAA**, **PCI-DSS**
- Riduce il rischio di **data leak** e violazioni di sicurezza
- Automatizza un’attività complessa e ad alto rischio

---

## 🚀 Use case comuni

- 🛡️ Protezione dei dati personali dei clienti
- 🔐 Verifica della conformità normativa
- 📂 Identificazione e isolamento di bucket S3 pubblici o insicuri
- 🧾 Audit e classificazione dei dati per enti regolatori
- 🔄 Automazione dei flussi di sicurezza in caso di rilevamento

---

## 💰 Pricing

Il costo di Amazon Macie si basa su due componenti:

1. **Numero di oggetti analizzati in S3** ($ per milione di oggetti)
2. **Dati analizzati per classificazione** ($ per GB analizzato)

Esempio di prezzi (verificare la regione):
- $1,00 per ogni milione di oggetti S3 analizzati mensilmente
- $0,10 per GB analizzato durante la scansione di contenuti


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS        | Differenza rispetto a Macie                                  |
|---------------------|--------------------------------------------------------------|
| **Amazon GuardDuty**| Rileva comportamenti sospetti, non dati sensibili           |
| **AWS Config**      | Traccia configurazioni, non analizza i contenuti dei dati    |
| **AWS Inspector**   | Si concentra su vulnerabilità, non sulla classificazione dati|

---

## 📌 Conclusioni

**Amazon Macie** è uno strumento fondamentale per le organizzazioni che gestiscono dati sensibili nel cloud. Aiuta a identificare e proteggere le informazioni riservate, supporta la conformità normativa e riduce il rischio di esposizioni accidentali.

> “Se non sai dove sono i tuoi dati sensibili, non puoi proteggerli. Macie lo scopre per te.”

