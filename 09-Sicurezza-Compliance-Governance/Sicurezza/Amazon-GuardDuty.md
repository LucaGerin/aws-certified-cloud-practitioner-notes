--> [AWS](00-Intro/AWS.md)  -  [Sicurezza](09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🕵️ Amazon GuardDuty

![logo](guardduty-logo.jpeg)

## 📘 Cos'è e come funziona

**Amazon GuardDuty** è un servizio gestito di **rilevamento intelligente delle minacce** per l’ambiente AWS. Utilizza **machine learning, analisi comportamentale e fonti di threat intelligence** per individuare attività sospette o potenzialmente dannose che potrebbero indicare un compromesso nella sicurezza.

GuardDuty analizza automaticamente i **log VPC Flow, AWS CloudTrail, Route 53 DNS query** (e altri, se abilitati) per identificare comportamenti anomali senza dover installare agenti su EC2 o altre risorse.

![GuardDuty](guardduty.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🤖 **Rilevamento automatico delle minacce** basato su ML e pattern noti
- 📊 Analisi continua di **CloudTrail, [VPC](03-CDN-e-Networking/Amazon-VPC.md) Flow Logs, DNS logs**
- 🛡️ Database aggiornato di **threat intelligence** (AWS + terze parti)
- 🧠 Rilevamento di **attività anomale, esfiltrazione di dati, accessi non autorizzati**
- 🔁 Nessun agente da installare, completamente **serverless**
- 🌍 **Supporto multi-account** via AWS Organizations
- 📤 Integrazione con **AWS Security Hub**, **EventBridge**, e automazioni personalizzate

---

## ✅ Vantaggi

- Riduce il tempo necessario per identificare e rispondere a minacce
- Rileva **attacchi che bypassano i controlli tradizionali** (es. accesso da IP sospetti)
- Migliora la **visibilità sulla sicurezza** delle risorse AWS
- Si configura in pochi click e **non richiede manutenzione**
- Aiuta nella conformità con normative come **PCI-DSS**, **HIPAA**, **GDPR**

---

## 🚀 Use case comuni

- 🕵️ Rilevamento di accessi sospetti o da IP malevoli
- 🧪 Monitoraggio per attività anomale da utenti IAM o root
- 📤 Identificazione di esfiltrazioni di dati via DNS o reti
- 🛡️ Protezione continua e senza agenti per ambienti cloud
- ⚠️ Notifica automatica e risposta ad incidenti (via Lambda o EventBridge)

---

## 💰 Pricing

GuardDuty è **pay-per-use**, basato su:

- Numero di eventi analizzati (CloudTrail, DNS, VPC logs)
- Eventuale attivazione di log EKS Audit, S3 data events, ecc.

---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS          | Differenze rispetto a GuardDuty                                   |
|------------------------|--------------------------------------------------------------------|
| **AWS Inspector**     | Scansione di vulnerabilità, non analisi comportamentale           |
| **Security Hub**      | Aggrega risultati (incluso GuardDuty), ma non rileva direttamente |
| **CloudTrail**        | Fornisce i log, ma non analizza il comportamento                  |
| **Macie**             | Identifica dati sensibili, non minacce comportamentali            |

---

## 📌 Conclusioni

**Amazon GuardDuty** è una soluzione potente e gestita per il **rilevamento proattivo delle minacce** nel cloud AWS. È semplice da attivare, non richiede manutenzione, e offre un monitoraggio continuo che protegge dagli attacchi più comuni e sofisticati.

> “Non basta sapere *chi* accede al cloud, ma *come*. GuardDuty ti dice se qualcosa non torna.”

