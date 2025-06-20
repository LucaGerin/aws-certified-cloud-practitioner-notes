--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🔥 AWS Network Firewall

## 📘 Cos'è e come funziona

**AWS Network Firewall** è un **servizio stateful di firewall gestito** che consente di **controllare e ispezionare il traffico di rete** a livello di [VPC](/03-CDN-e-Networking/Amazon-VPC.md) (Virtual Private Cloud). È progettato per fornire protezione avanzata contro minacce alla rete, filtrando pacchetti **stateful** e **stateless** con regole personalizzabili e complesse.

Il firewall viene distribuito all’interno delle **subnet di protezione** in una [VPC](/03-CDN-e-Networking/Amazon-VPC.md) e può essere utilizzato per monitorare e controllare il traffico tra subnet, verso Internet, o tra [VPC](/03-CDN-e-Networking/Amazon-VPC.md) tramite **Transit Gateway** o **Gateway Load Balancer**.

---

## ✨ Caratteristiche principali e vantaggi

- 🧱 **Filtri stateless e stateful** su traffico in ingresso e uscita
- 🌐 **Controllo su IP, porta, protocollo, dominio, FQDN**
- 🧠 **Regole avanzate di filtraggio** basate su pattern e firme (Suricata compatible)
- 🛠️ **Gestione centralizzata tramite AWS Firewall Manager**
- 📊 **Logging dettagliato** del traffico accettato/rifiutato su CloudWatch, S3 o Kinesis
- 🔁 **Alta disponibilità automatica** e scalabilità orizzontale gestita da AWS
- 🧩 **Integrazione con [VPC](/03-CDN-e-Networking/Amazon-VPC.md), Transit Gateway, e altri servizi AWS**

### ✅ Vantaggi

- Protegge le reti cloud da **attacchi noti e comportamenti sospetti**
- Evita **minacce interne** tramite ispezione profonda del traffico interno alla [VPC](/03-CDN-e-Networking/Amazon-VPC.md)
- Aiuta nella **conformità normativa** (es. PCI-DSS, HIPAA)
- Offre **visibilità e controllo** granulari senza dover gestire hardware o software firewall

---

## 🚀 Use case comuni

- 🔐 Segmentazione sicura delle subnet all’interno di una [VPC](/03-CDN-e-Networking/Amazon-VPC.md)
- 🛡️ Ispezione del traffico tra [VPC](/03-CDN-e-Networking/Amazon-VPC.md) tramite AWS Transit Gateway
- 🌍 Filtraggio DNS o blocco di domini sospetti
- 🧾 Logging e auditing centralizzato del traffico di rete
- ⚠️ Protezione da malware e exploit tramite regole Suricata personalizzate

---

## 💰 Pricing

Il prezzo di AWS Network Firewall si basa su:
- Numero di **firewall endpoint attivi per AZ**
- Volume di **traffico ispezionato** (GB)
- **Log generati**, se inviati a CloudWatch, S3 o Kinesis

---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS        | Differenze rispetto a AWS Network Firewall                    |
| ------------------- | ------------------------------------------------------------- |
| **Security Groups** | Firewall a livello istanza, stateful ma semplice              |
| **NACLs**           | Firewall a livello subnet, stateless, non ispeziona contenuto |
| **AWS WAF**         | Protezione layer 7 (HTTP/HTTPS), utile per applicazioni web   |
| **AWS Shield**      | Protezione contro attacchi DDoS, non un firewall tradizionale |

---

## 📌 Conclusioni

**AWS Network Firewall** è una soluzione potente e scalabile per proteggere la rete all'interno del cloud AWS. Offre **controlli granulari, gestione centralizzata e protezione avanzata** per ambienti cloud complessi e regolamentati.

> “Non fermarti a proteggere le istanze: proteggi la rete stessa, con un firewall cloud-native.”
