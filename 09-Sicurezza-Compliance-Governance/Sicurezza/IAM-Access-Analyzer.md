--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🔍 AWS IAM Access Analyzer

## 📘 Cos'è e come funziona

**IAM Access Analyzer** è uno strumento integrato in **AWS Identity and Access Management (IAM)** che ti consente di **identificare e monitorare gli accessi non intenzionali alle tue risorse AWS**. Analizza le policy di accesso (IAM, risorse, bucket S3, KMS, SQS, ecc.) per determinare **quali entità esterne** (es. utenti di altri account AWS, servizi, organizzazioni) **possono accedere alle tue risorse**.
Analizza la storia degli accessi alle risorse per proporre delle policies IAM che siano in più aderenti possibile al [Principio del Least Privilege](Sicurezza-Compliance-Governance.md).

Il servizio utilizza tecniche di **analisi formale** per fornire risultati affidabili e dettagliati, indicando chi può accedere a cosa e da dove.

---

## ✨ Caratteristiche principali e vantaggi

- 🔐 **Rilevamento automatico** di accessi pubblici o da altri account AWS
- 🧠 **Analisi continua o ad-hoc** delle policy
- 📄 **Risultati leggibili** con dettagli su risorse, identità e permessi concessi
- 📌 **Supporta più tipi di risorse**: S3, KMS, [IAM](AWS-IAM.md) roles, Lambda, SQS, ecc.
- 🔄 **Integrazione con AWS Organizations** per l’analisi multi-account
- ✅ **Suggerimenti per rimedi** in caso di accessi non desiderati

### ✅ Vantaggi

- Aumenta la **visibilità e la sicurezza** dei permessi
- Supporta il principio del **least privilege**
- Aiuta a prevenire **data leak** o configurazioni errate
- Riduce i rischi di **conformità** o audit negativi
- Automatizzabile via API e integrabile con **CloudTrail**, **Config**, **Security Hub**

---

## 🚀 Use case comuni

- 🔎 Verificare chi può accedere a un bucket S3 e da dove
- 🧑‍💻 Controllare se un ruolo [IAM](AWS-IAM.md) è accessibile da entità esterne
- 🏢 Audit di sicurezza per ambienti multi-account
- 🔁 Automazione nel ciclo CI/CD per validare le policy prima del deploy
- 🚫 Identificare e correggere permessi troppo permissivi in ambienti sensibili

---

## 💰 Pricing

**IAM Access Analyzer è gratuito.**

Non ci sono costi aggiuntivi per l’uso del servizio. Viene incluso direttamente all’interno di **IAM**, e puoi eseguire analisi **senza costi extra**.

---

## 📌 Conclusioni

**IAM Access Analyzer** è uno strumento essenziale per garantire che le tue risorse AWS siano accessibili solo da chi dovrebbe davvero poterle usare. Aiuta a **individuare accessi eccessivi o non intenzionali**, supportando la costruzione di ambienti cloud **sicuri, conformi e ben gestiti**.

> “Non puoi proteggere ciò che non sai che è esposto — Access Analyzer te lo mostra chiaramente.”

