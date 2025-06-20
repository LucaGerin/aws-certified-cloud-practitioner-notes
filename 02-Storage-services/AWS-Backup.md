--> [AWS](/00-Intro/AWS.md)  -  [Storage Services](/02-Storage-services/AWS-Storage-Services.md)

# AWS Backup

**AWS Backup** è un servizio completamente gestito che consente di centralizzare e automatizzare il **backup dei dati** attraverso vari servizi AWS e ambienti on-premises. Il servizio aiuta le organizzazioni a proteggere i dati in modo coerente, conforme e scalabile.

![AWS Backup logo](awsbackup.jpg)

---

## 🔧 Cos'è e come funziona

AWS Backup fornisce un approccio centralizzato per configurare, eseguire e monitorare i backup delle risorse AWS e on-premises. Consente di:

- Definire piani di backup (backup plans) per schedulare backup automatici
- Applicare regole di conservazione, cifratura e versioning
- Ripristinare dati in modo granulare e selettivo
- Estendere la protezione dei dati anche a volumi locali tramite [AWS Storage Gateway](/02-Storage-services/AWS-Storage-Gateway.md)
- Utilizzare backup cross-region e cross-account per resilienza e disaster recovery

![vault](backup-vault.png)

---

## ⭐ Caratteristiche principali e vantaggi

- **Backup centralizzato:** Un’unica interfaccia per gestire il backup di risorse come [Amazon EBS](/02-Storage-services/Amazon-EBS.md), [Amazon RDS](/04-Database-services/Amazon-RDS.md), [Amazon DynamoDB](/04-Database-services/Amazon-DynamoDB.md), [Amazon EFS](/02-Storage-services/Amazon-EFS.md), [Amazon FSx](/02-Storage-services/Amazon-FSx.md), [Amazon S3](/02-Storage-services/Amazon-S3.md) (con limitazioni) e [AWS Storage Gateway](/02-Storage-services/AWS-Storage-Gateway.md)
- **Automazione con backup plans:** Schedulazione automatica, regole di conservazione e tagging
- **Backup incrementali:** Riduzione dello spazio occupato e dei costi
- **Restore granulare:** Ripristino rapido e preciso
- **Monitoraggio e auditing:** Integrazione con [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) e [AWS Organizations](09-Sicurezza-Compliance-Governance/Compliance e Governance/AWS-Organizations.md)
- **Compatibilità multi-account e cross-region** per elevata disponibilità
- **Compliance:** Facilita l’adesione a normative come GDPR, HIPAA, ISO

---

## 🚀 Use Cases

- **Backup centralizzato** per ambienti multi-account e multi-servizio
- **Conformità normativa:** Applicazione coerente di policy per GDPR, HIPAA, ISO, ecc.
- **Disaster recovery** tramite copie cross-region
- **Protezione da cancellazioni accidentali** o ransomware
- **Hybrid cloud backup:** Protezione di volumi on-prem tramite [AWS Storage Gateway](/02-Storage-services/AWS-Storage-Gateway.md)
- **Long-term archiving** con cicli di vita configurabili

---

## 💰 Pricing

Il costo di AWS Backup dipende da:

- **Volume di dati protetti (per GB al mese)**
- **Tipo di servizio protetto** (es. EBS, RDS, EFS, ecc.)
- **Regione AWS**
- **Snapshot aggiuntivi** o backup cross-region (se configurati)

⚠️ I backup incrementali e le policy di ciclo di vita contribuiscono a ridurre il costo complessivo.

---

## 🔐 Sicurezza

- **Crittografia dei backup** a riposo tramite [AWS KMS](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)
- **Controllo accessi granulari** tramite [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
- **Audit e log delle operazioni** tramite [AWS CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)
- **Isolamento logico** dei dati tra account tramite backup cross-account
- Supporto per **compliance standards** e certificazioni (SOC, ISO, HIPAA)

---

## 🔄 Confronto con servizi simili in AWS

| Servizio                    | Funzione                            | Quando usarlo                                               |
|-----------------------------|--------------------------------------|-------------------------------------------------------------|
| **AWS Backup**              | Gestione backup centralizzata        | Quando serve coordinare backup multi-servizio e multi-account |
| **Snapshot manuali (EBS/RDS)** | Backup specifico per singola risorsa | Quando serve controllo puntuale su una risorsa             |
| **[Amazon S3](/02-Storage-services/Amazon-S3.md) + Lifecycle Policy** | Archiviazione con versioning        | Per dati in oggetti, non strutturati                       |
| **[AWS Storage Gateway](/02-Storage-services/AWS-Storage-Gateway.md)** | Backup da ambienti on-prem          | Per ambienti ibridi o locali                               |

---

## 🧩 Servizi supportati

- [Amazon EC2](/01-Compute-options/Amazon-EC2.md) (tramite volumi [Amazon EBS](/02-Storage-services/Amazon-EBS.md))
- [Amazon RDS](/04-Database-services/Amazon-RDS.md) (tutti i motori)
- [Amazon DynamoDB](/04-Database-services/Amazon-DynamoDB.md)
- [Amazon EFS](/02-Storage-services/Amazon-EFS.md)
- [Amazon FSx](/02-Storage-services/Amazon-FSx.md) (Windows, Lustre, ONTAP, OpenZFS)
- [Amazon S3](/02-Storage-services/Amazon-S3.md) (supporto limitato)
- [AWS Storage Gateway](/02-Storage-services/AWS-Storage-Gateway.md)

---

AWS Backup è la soluzione ideale per **team DevOps**, infrastrutture distribuite e aziende che vogliono gestire i propri backup in modo **centralizzato, scalabile, conforme e sicuro**.

