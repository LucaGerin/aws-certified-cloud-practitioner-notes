--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🔐 AWS KMS (Key Management Service)

## 📘 Cos'è e come funziona

**AWS Key Management Service (KMS)** è un servizio gestito che consente di **creare, gestire e controllare le chiavi crittografiche** utilizzate per proteggere i dati nelle applicazioni e nei servizi AWS. 
KMS supporta la **crittografia a chiave simmetrica e asimmetrica**, e consente sia la gestione automatica delle chiavi da parte di AWS sia la gestione manuale da parte del cliente.

Le chiavi KMS possono essere utilizzate per cifrare oggetti [S3](Amazon-S3.md), volumi [EBS](Amazon-EBS.md), segreti in Secrets Manager, database [RDS](Amazon-RDS.md), parametri in [Systems Manager](Tag-e-AWS-Systems-Manager.md) e altro ancora.

---

## ✨ Caratteristiche principali e vantaggi

- 🔐 **Gestione centralizzata delle chiavi crittografiche (CMK)**
- 🔁 **Rotazione automatica delle chiavi**
- 🧩 **Integrazione con oltre 100 servizi AWS**
- ✅ **Controlli granulari tramite IAM & policy di key-level**
- 📜 **Log delle operazioni** di cifratura e decifratura tramite **AWS CloudTrail**
- 🧠 Supporto per **HSM gestiti (FIPS 140-2)** per esigenze ad alta sicurezza

### ✅ Vantaggi

- Riduce la complessità nella gestione della crittografia
- Supporta la conformità a standard come **GDPR**, **HIPAA**, **PCI-DSS**
- Consente **auditing completo** delle operazioni di cifratura
- Consente **deleghe e controlli avanzati** su chi può usare una chiave e come

---

## 🔑 Tipi di chiavi KMS

| Tipo                         | Descrizione                                      |
|------------------------------|--------------------------------------------------|
| **Customer managed key (CMK)** | Chiavi create e gestite manualmente dal cliente |
| **AWS managed key**          | Chiavi create e gestite automaticamente da AWS   |
| **AWS owned key**            | Usate internamente da AWS, non visibili al cliente |
| **Chiavi asimmetriche**      | Usate per firmare e verificare dati o cifrare/decriptare con RSA/ECC |

---

## 🚀 Use case comuni

- 🧾 Crittografia automatica dei dati in S3, [EBS](Amazon-EBS.md), RDS, DynamoDB
- 🧑‍💼 Protezione di segreti, token e password in Secrets Manager o Parameter Store
- 🧠 Gestione delle chiavi in applicazioni personalizzate con SDK o API
- 🔒 Firma digitale e verifica di documenti o transazioni (con chiavi asimmetriche)
- 📊 Audit e logging delle attività crittografiche

---

## 💰 Pricing

Il costo di AWS KMS è basato su:

- **Numero di chiavi attive** ($1/mese per chiave customer managed)
- **Operazioni crittografiche** (es. cifratura, decifratura, firma, verifica)
- Le **chiavi gestite da AWS** (AWS managed) sono **gratuite** nella maggior parte dei casi

---

## 🔄 Confronto con servizi simili AWS

| Servizio AWS          | Differenze rispetto a KMS                                 |
|------------------------|-----------------------------------------------------------|
| **[AWS Secrets Manager](AWS-Secrets-Manager.md)**| Protegge e ruota segreti, ma utilizza KMS per cifrarli    |
| **[Amazon Macie](Amazon-Macie.md)**       | Identifica i dati sensibili che sono salvati, ma non li cifra                |
| **[AWS CloudHSM](AWS-CloudHSM.md)**       | Offre HSM dedicati per requisiti crittografici avanzati   |

---

## 📌 Conclusioni

**AWS KMS** è il cuore della crittografia su AWS. Fornisce strumenti sicuri e scalabili per proteggere dati, applicazioni e segreti, aiutando le organizzazioni a rispettare requisiti normativi e di sicurezza, mantenendo al contempo controllo e tracciabilità.

> “Crittografare i dati è importante. Sapere chi può usare le chiavi lo è ancora di più.”

