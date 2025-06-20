--> [AWS](/00-Intro/AWS.md)  -  [Migration Strategies](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Strategies.md)
# AWS Application Discovery Service

![Application Discovery Service](app-disc.png)

**AWS Application Discovery Service** è un servizio progettato per aiutare le aziende a **raccogliere automaticamente informazioni** sui propri data center on-premises, con l'obiettivo di pianificare e semplificare la **migrazione verso [AWS](/00-Intro/AWS.md)**.

---

## 🧩 Caratteristiche principali

- **Crea un inventario automatico** dei server fisici e virtuali
- Raccoglie dati su:
  - **Applicazioni installate**
  - **Sistemi operativi**
  - **Utilizzo CPU e memoria**
  - **Comunicazioni di rete (inbound/outbound)**
- Supporta ambienti:
  - **VMware vCenter**
  - **Windows Server**
  - **Linux Server**
- I dati raccolti vengono utilizzati da strumenti come [AWS-Migration-Hub](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Hub.md)

---

## 🔧 Modalità operative

1. **Agent-based**:
   - Installa un agente su ogni server
   - Raccoglie dati dettagliati sull’host, le app, e i processi

2. **Agentless**:
   - Si integra con vCenter
   - Raccoglie dati sull’infrastruttura virtuale (VM, rete, storage)

---

## 🧪 Use case

- Valutare la **complessità** e la **dipendenza tra sistemi**
- Preparare un **business case per la migrazione**
- Identificare server candidati per **lift-and-shift**
- Integrare i dati in [AWS-Migration-Hub](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Hub.md) o [AWS-Application-Migration-Service](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Application-Migration-Service.md)

---

## 🔐 Sicurezza

- I dati raccolti possono essere criptati
- Comunicazione sicura verso [AWS](/00-Intro/AWS.md)
- [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) per controllare accessi e permessi

---

## 📌 Conclusioni

AWS Application Discovery Service è uno strumento fondamentale per **capire cosa si ha in casa** prima di migrare verso il cloud. Automatizza l’analisi dell’infrastruttura on-premises, rendendo la migrazione più informata, mirata ed efficiente.

> “Conosci il tuo data center, prima di lasciarlo.”
