--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🔐 AWS Certificate Manager (ACM)

## 📘 Cos'è e come funziona

**AWS Certificate Manager (ACM)** è un servizio gestito che consente di **creare, distribuire e gestire certificati SSL/TLS** per proteggere le comunicazioni su web e applicazioni. 
ACM semplifica l'acquisizione e il rinnovo di certificati, rimuovendo la necessità di eseguire attività manuali come la generazione delle CSR, la configurazione dei certificati e il rinnovo periodico.

I certificati possono essere utilizzati su servizi AWS come:
- **Elastic Load Balancer (ELB)**, 
- **Amazon CloudFront**, 
- **API Gateway**, 
- **AWS App Runner**

Ci sono due modi per convalidare e verificare l'emissione di un certificato di sicurezza da parte di AWS Certificate Manager:
1. Creare un record **CNAME** nella zona DNS (hosted zone) del dominio.
2. Confermare tramite email inviata all'indirizzo email del richiedente.


---

## ✨ Caratteristiche principali e vantaggi

- 🔐 **Emissione e rinnovo automatico** dei certificati SSL/TLS
- ⚙️ **Distribuzione integrata** con servizi AWS (ELB, CloudFront, ecc.)
- 🌍 **Supporto a certificati pubblici e privati**
- 🔄 **Gestione centralizzata dei certificati** da una console unificata
- 🛡️ **Miglioramento della sicurezza** con cifratura HTTPS
- 📆 **Nessuna scadenza dimenticata**: rinnovo automatico incluso

### ✅ Vantaggi

- Elimina la complessità della gestione manuale dei certificati
- Riduce il rischio di errori e di certificati scaduti
- Migliora l’esperienza utente con HTTPS sempre attivo
- Supporta la conformità a standard di sicurezza (es. PCI-DSS)

---

## 🚀 Use case comuni

- 🌐 Abilitare **HTTPS su siti web** e applicazioni hosted in AWS
- 📡 Proteggere **API pubbliche o private** tramite API Gateway
- 🛡️ Crittografare comunicazioni tramite **CloudFront o ELB**
- 🧪 Certificati privati per ambienti interni tramite **ACM Private CA**

---

## 🔐 Tipi di certificati supportati

| Tipo                        | Descrizione                                            |
|-----------------------------|---------------------------------------------------------|
| **Certificati pubblici**    | Rilasciati gratuitamente da ACM per domini validati    |
| **Certificati privati**     | Rilasciati tramite ACM Private CA (servizio opzionale) |

---

## 💰 Pricing

- ✅ **Certificati pubblici rilasciati da ACM sono gratuiti** se utilizzati con servizi AWS
- 💰 **Certificati privati** richiedono l’uso di **ACM Private Certificate Authority**, che è a pagamento


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS           | Differenze rispetto a ACM                                    |
|------------------------|--------------------------------------------------------------|
| **AWS Secrets Manager**| Conserva segreti e credenziali, non certificati TLS          |
| **AWS KMS**            | Gestisce chiavi crittografiche, non certificati pubblici     |
| **ACM Private CA**     | Estensione di ACM per creare un’autorità certificatrice privata|

---

## 📌 Conclusioni

**AWS Certificate Manager** è lo strumento ideale per **gestire la crittografia HTTPS in modo sicuro e senza sforzo**, eliminando la necessità di gestire manualmente i certificati. È una scelta fondamentale per chi desidera **proteggere le comunicazioni nel cloud** e garantire **continuità e sicurezza** ai propri servizi.

> “ACM ti dà certificati validi e aggiornati, senza che tu debba mai preoccupartene.”

