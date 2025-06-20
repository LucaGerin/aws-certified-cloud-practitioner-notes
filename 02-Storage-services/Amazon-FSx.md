--> [AWS](00-Intro/AWS.md)  -  [Storage Services](02-Storage-services/AWS-Storage-Services.md)

# Amazon FSx

Amazon FSx è un servizio di **file storage e system completamente gestito**, progettato per offrire prestazioni elevate, compatibilità con file system familiari e integrazione con l’ambiente AWS.
Supporta diversi **file system specializzati**, adatti a casi d’uso distinti sia in cloud che in scenari ibridi.

![fsx](fsx.png)

FSx è progettato per lo storage attivo di file, quindi meno adatto per mantenere files a lungo termine.

---

## 📂 File system supportati

### 1. **Amazon FSx for Windows File Server**

- Compatibile con il protocollo **SMB** (Server Message Block)
- Integrazione con Microsoft Active Directory per gestione utenti e permessi
- Supporta funzionalità avanzate come DFS, shadow copies, backup integrati

**Casi d’uso:**

- File server Windows gestiti
- Home directory aziendali
- Applicazioni ERP e CRM in ambienti Windows
- File sharing tra utenti Windows

---

### 2. **Amazon FSx for Lustre**

- File system ad alte prestazioni per workload **HPC (High Performance Computing)**
- **Integrazione con [Amazon S3](02-Storage-services/Amazon-S3.md):** i dati possono essere caricati direttamente da bucket S3
- Progettato per throughput e parallelismo estremi

**Casi d’uso:**

- [Machine learning](07-IA-ML-Analytics/AI e ML/Machine-Learning.md)
- Genomica e modellazione scientifica
- Rendering video, simulazioni e analisi complesse

---

### 3. **Amazon FSx for NetApp ONTAP**

- Estensione cloud di NetApp ONTAP con gestione AWS
- Supporta protocolli multipli: NFS, SMB, iSCSI
- Include snapshot, deduplicazione e compressione automatica

**Casi d’uso:**

- Ambienti ibridi on-premises/cloud
- Backup avanzato e disaster recovery
- Migrazione di workload NetApp esistenti

---

### 4. **Amazon FSx for OpenZFS**

- Basato su OpenZFS, file system open-source noto per affidabilità e performance
- Supporta snapshot istantanei, compressione e copie efficienti

**Casi d’uso:**

- DevOps e ambienti CI/CD
- Compilazione software e sviluppo distribuito
- Backup incrementali e test

---

## ✅ Vantaggi generali di Amazon FSx

- **Completamente gestito:** provisioning, patching, backup e aggiornamenti automatizzati
- **Prestazioni elevate:** IOPS e throughput scalabili in base al file system scelto
- **Integrazione con AWS:** accessibile da istanze [Amazon EC2](01-Compute-options/Amazon-EC2.md), container [Amazon ECS](01-Compute-options/Amazon-ECS.md), [Amazon EKS](01-Compute-options/Amazon-EKS.md), [AWS Lambda](01-Compute-options/AWS-Lambda.md)
- **Supporto per ambienti ibridi:** adatto a workload on-prem e cloud
- **Sicurezza e isolamento:** integrazione con [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md), [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), crittografia nativa e autenticazione Active Directory

---

## 💰 Pricing

Il costo di Amazon FSx dipende da:

- Il tipo di file system selezionato
- Capacità storage e performance provisionate
- Backup, snapshot, throughput e traffico dati

Ogni file system ha un modello di pricing specifico. Il costo può includere:
- Tariffe per GB/mese per storage
- Tariffe per IOPS e throughput (dove applicabile)
- Backup automatici e snapshot

---

## 🔐 Sicurezza

- **Crittografia dei dati a riposo e in transito** con [AWS KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)
- **Accesso controllato tramite [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)** e Active Directory (dove supportato)
- **Isolamento di rete con [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md)** e supporto per Multi-AZ
- **Logging e monitoraggio:** integrazione con [Amazon CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) e [AWS CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)

---

## 🔄 Confronto con altri servizi di file storage

| Servizio                | Tipo                        | Quando usarlo                                               |
|-------------------------|-----------------------------|-------------------------------------------------------------|
| **Amazon FSx**          | File system specializzato (FSx per windows è accessibile con SMB)  | Per workload compatibili con Windows, Lustre, NetApp, ZFS   |
| **[Amazon EFS](02-Storage-services/Amazon-EFS.md)**       | File system condiviso accessibile con NFS      | Per accesso simultaneo da molte istanze Linux               |
| **[Amazon EBS](02-Storage-services/Amazon-EBS.md)**       | Storage a blocchi              | Per volumi collegati a singole istanze EC2                  |
| **[Amazon S3](02-Storage-services/Amazon-S3.md)**         | Object storage                 | Per storage di oggetti scalabile e accesso tramite API      |

---

## 📌 Best Practices

- Scegliere il **file system** più adatto al workload (es. Lustre per ML, Windows File Server per ambienti Windows)
- Utilizzare **backup automatici** per proteggere i dati critici
- Applicare **policy IAM e ACL** per controllo accessi granulare
- Configurare **replica Multi-AZ** dove supportato per alta disponibilità
- Monitorare utilizzo e prestazioni tramite [CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md)

---

Amazon FSx è una soluzione ideale per chi ha bisogno di **prestazioni elevate**, compatibilità con ambienti esistenti e funzionalità avanzate per il file storage, sia in cloud che in ambienti ibridi.
