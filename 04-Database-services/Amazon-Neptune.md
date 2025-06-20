--> [AWS](00-Intro/AWS.md)  -  [Database Services](04-Database-services/AWS-Databases.md)
# 🧠 Amazon Neptune

![Neptune](neptune.png)

**Amazon Neptune** è un servizio di **database a grafo completamente gestito** progettato per elaborare query complesse su dati altamente connessi. Supporta sia il modello **Property Graph** (con il linguaggio **Gremlin**) sia il modello **RDF** (con **SPARQL**), offrendo una piattaforma potente per navigare ed estrarre valore da relazioni intricate tra dati.

---

## ⚙️ Cos'è e come funziona

Amazon Neptune è ottimizzato per carichi di lavoro a grafo in cui la **navigazione tra relazioni** è una parte essenziale delle query.  
Offre **alta disponibilità**, prestazioni elevate e integrazione nativa con l'ecosistema AWS.

Supporta due principali modelli:

- **Property Graph** (con il linguaggio Gremlin – Apache TinkerPop)
- **RDF (Resource Description Framework)** (con SPARQL – W3C)

Gestisce provisioning, backup, patching e failover in modo completamente automatizzato.

---

## ✨ Caratteristiche principali e vantaggi

- 🔄 **Supporto multi-modello**: Gremlin per Property Graph, SPARQL per RDF  
- 📡 **Alta disponibilità**: replica multi-AZ, failover automatico < 30 secondi  
- 🔐 **Sicurezza integrata**:
  - Integrazione con [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
  - Isolamento tramite [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md)
  - Crittografia **at-rest** e **in-transit** con [AWS KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md) e TLS
  - Auditing con [CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)  
- ⚙️ **Performance ottimizzate** per grafi: indexing automatico, query veloci  
- 🧩 **Servizio completamente gestito**: riduce i costi operativi e la complessità di gestione  
- 📈 **Integrazione con altri servizi AWS**: [Amazon CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md), [S3](02-Storage-services/Amazon-S3.md), [CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)  

---

## 💼 Use cases

- 🧑‍🤝‍🧑 **Social graph**: utenti, amicizie, gruppi, post e interazioni  
- 🛍️ **Motori di raccomandazione**: correlazioni tra preferenze e comportamenti  
- 🧠 **Knowledge graph**: strutture semantiche per rappresentare concetti e relazioni  
- 🕵️ **Rilevamento frodi**: identificazione di pattern sospetti e connessioni anomale  
- 🌐 **Gestione di reti IT/IoT**: modelli di interconnessione tra dispositivi e infrastrutture  
- 🧬 **Analisi di dati biologici**: strutture molecolari e genomica

---

## 💰 Pricing

I costi di Amazon Neptune sono calcolati in base a:

- Tipo e dimensione dell’istanza database
- Storage utilizzato (GB/mese)
- I/O requests
- Backup (oltre lo storage gratuito)
- Trasferimento dati in uscita

La replica tra Availability Zone è gratuita. Il backup fino allo stesso ammontare dello storage è incluso.

---

## 🔒 Sicurezza

Amazon Neptune protegge i dati a più livelli:

- ✅ **Crittografia at-rest** con [AWS KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)
- ✅ **Crittografia in-transit** con TLS
- ✅ **Controllo accessi** con [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
- ✅ **Isolamento di rete** con [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md)
- ✅ **Monitoraggio** e auditing via [Amazon CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) e [CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)  

---

## 🔁 Confronto con altri database AWS

| Servizio          | Tipo DB             | Ottimizzato per       | Linguaggi supportati        | Casi d'uso tipici             |
|-------------------|---------------------|------------------------|-----------------------------|-------------------------------|
| Amazon Neptune     | Grafo (Property, RDF)| Relazioni complesse    | Gremlin, SPARQL             | Social, raccomandazioni, IoT |
| [Amazon RDS](04-Database-services/Amazon-RDS.md)         | Relazionale (SQL)    | Query relazionali      | SQL (MySQL, PostgreSQL…)    | Web, ERP, CRM                 |
| [Amazon DynamoDB](04-Database-services/Amazon-DynamoDB.md)    | NoSQL key-value      | Scalabilità e velocità | Parti-QL, SDK AWS           | Sessioni, IoT, cache          |
| Amazon DocumentDB  | Documenti JSON       | Document-oriented      | MongoDB API                 | CMS, profili utente           |

---

## 📌 Conclusione

Amazon Neptune è la scelta ideale quando i dati non sono solo da archiviare ma da **navigare**: quando contano le **relazioni tra entità**, più che le entità stesse.  
Con il supporto per linguaggi standard come **Gremlin** e **SPARQL**, e l'infrastruttura gestita di AWS, consente di costruire **applicazioni grafiche scalabili, sicure e performanti**.

> “Per dati fortemente connessi, Amazon Neptune è il grafo più intelligente del cloud.”
