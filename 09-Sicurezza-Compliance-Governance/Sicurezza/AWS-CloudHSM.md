--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🔐 AWS CloudHSM

## 📘 Cos'è e come funziona

**AWS CloudHSM (Hardware Security Module)** è un servizio che fornisce **moduli hardware dedicati** per la **gestione sicura delle chiavi crittografiche**, ospitati all'interno del cloud AWS.

Con CloudHSM, le organizzazioni possono **generare, archiviare e gestire chiavi crittografiche** all'interno di dispositivi conformi allo standard **FIPS 140-2 livello 3**, mantenendo **il pieno controllo delle chiavi**, senza che AWS possa accedervi.

CloudHSM è ideale per scenari che richiedono **requisiti di conformità rigorosi**, come **PCI-DSS**, **HIPAA**, **GDPR** o normative governative.  

I principali casi d’uso includono la **gestione delle chiavi di crittografia dei dati**, il **signing digitale**, la **protezione delle chiavi di database e applicazioni sensibili** e l’**accelerazione delle operazioni SSL/TLS per server web**.


---

## ✨ Caratteristiche principali

- 🛡️ **Moduli hardware dedicati (HSM)** completamente gestiti
- 🔑 **Controllo esclusivo delle chiavi crittografiche** da parte del cliente
- 🧪 Certificazione **FIPS 140-2 Livello 3**
- 🌐 **Alta disponibilità** tramite cluster distribuiti in più Availability Zones
- ⚙️ Compatibilità con librerie standard PKCS#11, JCE, OpenSSL
- 🔗 Integrazione con applicazioni personalizzate e middleware HSM-aware

---

## ✅ Vantaggi

- ✅ Adempie ai **requisiti di conformità più severi**
- ✅ **Controllo completo** delle chiavi da parte del cliente, senza accesso AWS
- ✅ Alta disponibilità, failover e scalabilità orizzontale automatica
- ✅ Supporta **crittografia simmetrica e asimmetrica**
- ✅ Nessuna gestione hardware fisica da parte del cliente

---

## 🚀 Use case comuni

- Si può usare CloudHSM per esternalizzare i processi SSL dei web server, liberandoli da quel compito.
- 💳 Applicazioni di pagamento conformi a **PCI-DSS**
- 🏥 Crittografia dei dati sanitari secondo **HIPAA**
- 📦 Firma digitale di software e certificati
- 🔐 Protezione di chiavi root in ambienti di gestione dei certificati (PKI)
- ⚖️ Requisiti normativi per enti governativi o bancari
- 🔗 Crittografia as-a-service per applicazioni sensibili

---

## 💰 Pricing

Il prezzo è basato su:

- Numero di **istanze HSM attive** (on-demand)
- Nessun costo upfront
- Tariffa oraria per ogni HSM allocato


---

## 🔄 Confronto con AWS KMS

| Caratteristica        | AWS CloudHSM                        | [AWS KMS](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)                               |
|------------------------|--------------------------------------|----------------------------------------|
| Controllo chiavi       | Cliente ha **pieno controllo**       | AWS gestisce le chiavi                 |
| Certificazione         | FIPS 140-2 Level 3                   | FIPS 140-2 Level 2                     |
| Integrazione           | PKCS#11, JCE, OpenSSL                | API AWS native                         |
| Complessità gestione   | Più complesso (clustering, failover) | Semplice e totalmente gestito          |
| Prezzo                 | Più costoso                          | Più economico                          |

---

## 📌 Conclusioni

**AWS CloudHSM** è la soluzione perfetta per le organizzazioni che necessitano di **controllo completo, conformità normativa rigorosa** e protezione crittografica tramite hardware certificato. Sebbene sia più complesso e costoso rispetto ad AWS KMS, offre **livelli di sicurezza e flessibilità più elevati**, adatti a casi d’uso critici e regolamentati.

> “Quando la conformità non è un’opzione ma un obbligo, CloudHSM è la risposta.”

