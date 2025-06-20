--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🛡️ AWS Shield

## 📘 Cos'è e come funziona

**AWS Shield** è un servizio di **protezione contro attacchi DDoS (Distributed Denial of Service)** progettato per difendere le applicazioni ospitate su AWS da interruzioni causate da traffico malevolo. 
Shield protegge automaticamente servizi come **Amazon CloudFront, Route 53, Global Accelerator, Elastic Load Balancer (ALB/NLB)** e **EC2**.

Shield è disponibile in due versioni:
- **AWS Shield Standard**: incluso gratuitamente in tutti gli account AWS, offre protezione automatica contro attacchi DDoS comuni a livello di rete.
- **AWS Shield Advanced**: servizio premium che fornisce protezione potenziata, report dettagliati, mitigazione personalizzata e supporto 24/7 da parte del DDoS Response Team (DRT).

---

## ✨ Caratteristiche principali e vantaggi

### 🆓 AWS Shield Standard

- Protezione automatica contro attacchi volumetrici e comuni su livelli 3 e 4
- Integrato nativamente con i principali servizi AWS (CloudFront, ELB, ecc.)
- Nessuna configurazione richiesta

### 💼 AWS Shield Advanced

- Rilevamento avanzato degli attacchi (Layer 3–7)
- **Mitigazione personalizzata automatica** in base al tipo di attacco
- **Protezione contro costi di scaling** dovuti a DDoS
- **Reportistica dettagliata e notifiche** via CloudWatch e AWS WAF
- Accesso al **DDoS Response Team (DRT)** di AWS 24/7
- Integrazione con AWS WAF per regole dinamiche
- Protezione per **applicazioni personalizzate su EC2 o Load Balancer**

---

## 🚀 Use case comuni

- 🌍 Protezione di **siti pubblici o API** accessibili da Internet
- 🛡️ Difesa contro attacchi DDoS a **livello di rete o applicativo**
- 🧩 Integrazione con CloudFront, ALB, Route 53 per maggiore resilienza
- 🆘 Mitigazione e risposta immediata in ambienti sensibili o regolamentati

---

## 💰 Pricing

- ✅ **AWS Shield Standard**: gratuito per tutti i clienti AWS
- 💰 **AWS Shield Advanced**:
  - Costo fisso mensile (es. $3.000/mese per account)
  - Include accesso al DDoS Response Team e protezione da costi di scaling


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS          | Differenze rispetto a Shield                                   |
|------------------------|---------------------------------------------------------------|
| **AWS WAF**           | Filtra richieste Layer 7 (app), non difende da attacchi DDoS volumetrici |
| **AWS Network Firewall** | Protezione a livello di rete (Layer 3/4), non specifico contro DDoS |
| **Security Groups / NACLs** | Controllo base del traffico, non in grado di mitigare DDoS         |

---

## 📌 Conclusioni

**AWS Shield** è il pilastro della difesa contro gli attacchi DDoS in AWS. La versione **Standard** è un’ottima protezione di base gratuita per tutti, mentre **Shield Advanced** è pensato per organizzazioni critiche o regolamentate che necessitano di visibilità, supporto e mitigazione avanzata.

> “Prepararsi a un attacco DDoS non è una possibilità: è una necessità. AWS Shield ti protegge, automaticamente.”

