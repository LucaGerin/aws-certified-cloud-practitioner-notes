--> [AWS](00-Intro/AWS.md)  -  [Sicurezza](09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🧰 AWS Firewall Manager

## 📘 Cos'è e come funziona

**AWS Firewall Manager** è un servizio di **gestione centralizzata delle policy di sicurezza** per ambienti multi-account in AWS. 
Ti consente di **creare e applicare automaticamente regole di sicurezza** come **AWS WAF, AWS Shield Advanced, AWS Network Firewall**, **VPC security groups** e **DNS Firewall** su più account e regioni, sfruttando l'integrazione con **AWS Organizations**.

Firewall Manager è pensato per semplificare e standardizzare l'applicazione delle policy di rete e sicurezza, particolarmente utile in ambienti complessi o regolamentati.

![Firewall Manger](firewall-manager.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🛠️ **Gestione centralizzata delle regole** di sicurezza su tutti gli account dell'organizzazione
- 🔄 **Applicazione automatica delle policy** a nuovi account e risorse
- 📏 Supporta regole per:
  - **AWS WAF** (Web Application Firewall)
  - **AWS Shield Advanced**
  - **AWS Network Firewall**
  - **Amazon Route 53 Resolver DNS Firewall**
  - **VPC security groups auditing**
- 🔍 **Monitoraggio della conformità** in tempo reale
- 🧩 Integrazione con **AWS Organizations** per la gestione multi-account
- 📊 Notifiche e logging tramite CloudWatch, SNS e AWS Config

---

## ✅ Vantaggi

- Applica standard di sicurezza in modo **coerente e automatico**
- Riduce errori di configurazione grazie al **controllo centralizzato**
- Favorisce la **conformità normativa** e la governance
- Reagisce in tempo reale ai cambiamenti nell'infrastruttura
- Riduce il carico operativo su team distribuiti

---

## 🚀 Use case comuni

- 🏢 Gestione della sicurezza in ambienti multi-account tramite AWS Organizations
- 🛡️ Distribuzione uniforme delle regole AWS WAF su tutte le applicazioni aziendali
- 🔄 Protezione automatica di nuove risorse con Shield Advanced o Network Firewall
- 🔍 Audit e rilevamento delle configurazioni di sicurezza non conformi
- 🧪 Automatizzazione della sicurezza in ambienti CI/CD

---

## 💰 Pricing

Il costo di **AWS Firewall Manager** è basato su:

- 💲 Numero di policy attive
- 💲 Eventuali costi aggiuntivi per i servizi sottostanti (WAF, Shield, Network Firewall)


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS          | Differenze rispetto a Firewall Manager                          |
|------------------------|------------------------------------------------------------------|
| **AWS WAF**           | Definisce regole, ma non le distribuisce tra account             |
| **AWS Organizations** | Gestione identità e risorse, non policy di sicurezza             |
| **AWS Config**        | Traccia risorse e compliance, ma non applica policy automaticamente |
| **Security Hub**      | Fornisce insight e raccomandazioni, non enforcement diretto      |

---

## 📌 Conclusioni

**AWS Firewall Manager** è lo strumento ideale per le organizzazioni che devono applicare policy di sicurezza coerenti in ambienti multi-account. Automatizza la distribuzione, garantisce la conformità e offre una visione centralizzata del tuo livello di protezione.

> “Con Firewall Manager, la sicurezza non è più un’opzione manuale: è automatica e distribuita.”

