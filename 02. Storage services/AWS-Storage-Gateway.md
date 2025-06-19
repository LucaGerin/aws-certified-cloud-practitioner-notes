--> [AWS](AWS.md)  -  [Storage Services](AWS-Storage-Services.md)
# AWS Storage Gateway

![storage gateway logo](stor-gat.png)

**AWS Storage Gateway** è un servizio **ibrido** che collega l'infrastruttura on-premises con il cloud AWS, consentendo di usare lo storage AWS come **estensione naturale dell’ambiente locale**. Il servizio si occupa del trasporto e sincronizzazione dei dati tra l’on-premise e il cloud, con supporto per backup, archiviazione, migrazione e disaster recovery.

---

## 🔧 Cos'è e come funziona

AWS Storage Gateway fornisce diverse modalità per integrare ambienti locali con lo storage cloud AWS. Offre gateway che emulano file server, dischi o librerie a nastro, permettendo di:

- Archiviare dati locali in [Amazon S3](Amazon-S3.md), [Amazon EBS](Amazon-EBS.md) o [Amazon Glacier](Amazon-S3.md)
- Usare protocolli standard come NFS, SMB, iSCSI
- Caching locale per accesso rapido ai dati usati frequentemente
- Automatizzare backup e restore verso il cloud AWS
- Funzionare come punto d’ingresso per il **data processing in AWS**, con eventuale ritorno on-premise

![storage gateway](storage-gateway.png)

---

## ⭐ Caratteristiche principali e vantaggi

- **Integrazione nativa con AWS:** piena compatibilità con [Amazon S3](Amazon-S3.md), [Amazon FSx](Amazon-FSx.md), [Amazon Glacier](Amazon-S3.md), [Amazon CloudWatch](Amazon-CloudWatch.md) e [IAM](AWS-IAM.md)
- **Performance locali + scalabilità cloud:** caching locale + storage scalabile in cloud
- **Compatibilità applicativa:** si integra con ambienti esistenti senza bisogno di riscrivere software
- **Sicurezza integrata:** dati cifrati in transito e a riposo
- **Riduzione dei costi:** evita l’espansione dello storage locale
- **Deployment flessibile:** supporto per VM, appliance fisiche o [Amazon EC2](Amazon-EC2.md)

---

## 🚀 Use Cases

- **Backup e archiviazione** verso [Amazon S3](Amazon-S3.md)
- **Disaster recovery ibrido** per applicazioni locali
- **Accesso multi-sede** a dati condivisi
- **Sostituzione di librerie a nastro** fisiche
- **Migrazione graduale** verso lo storage AWS

---

## 🧱 Tipi di Gateway disponibili

### 1. **File Gateway**

- Espone uno share compatibile con **NFS** o **SMB** (Per windows è più adatto SMB, per Linux è più adatto NFS)
- I file vengono archiviati come oggetti nativi in [Amazon S3](Amazon-S3.md)
- Supporto per caching locale

**Casi d’uso:**

- Backup e archiviazione su cloud
- Integrazione NAS multi-sede
- Conservazione di contenuti

---

### 2. **Volume Gateway**

- Esporta volumi **block storage iSCSI** alle applicazioni locali
- Due modalità operative:
  - **Cached volumes:** i dati risiedono in [S3](Amazon-S3.md), con cache locale
  - **Stored volumes:** i dati sono locali con backup asincrono in cloud

**Casi d’uso:**

- Backup continuo di volumi locali
- Disaster recovery ibrido

---

### 3. **Tape Gateway**

- Emula una **Virtual Tape Library (VTL)** compatibile con software come Veeam o Veritas
- I nastri virtuali sono archiviati in [Amazon S3](Amazon-S3.md) o [Amazon Glacier](Amazon-S3.md)

**Casi d’uso:**

- Archiviazione a lungo termine
- Eliminazione di tape fisici
- Migrazione dei backup su nastro al cloud

---

### 4. **FSx File Gateway**

- Estende file system locali con supporto per [Amazon FSx for Windows File Server](Amazon-FSx.md)
- Offre accesso diretto a file system Windows in AWS tramite SMB

**Casi d’uso:**

- Condivisione file tra sedi
- Estensione di ambienti Active Directory
- Integrazione di applicazioni Windows legacy

---

## 💰 Pricing

AWS Storage Gateway applica costi basati su:

- Volume di dati archiviati in cloud (es. in [Amazon S3](Amazon-S3.md) o Glacier)
- Operazioni di I/O e trasferimenti dati
- Provisioning dell’appliance (VM o hardware dedicato)
- Storage cache locale non incluso nei costi AWS

⚠️ I costi variano a seconda del tipo di gateway e modalità di utilizzo (cached, stored, tape).

---

## 🔐 Sicurezza

- **Crittografia dei dati in transito e a riposo**, con [AWS KMS](AWS-KMS.md)
- **Access control tramite [IAM](AWS-IAM.md)** per azioni sulle risorse
- **Integrazione con [AWS CloudTrail](Amazon-CloudTrail.md)** per auditing
- Caching locale sicuro tramite appliance configurabili

---

## 🔄 Confronto con servizi simili in AWS

| Servizio                      | Tipo                          | Quando usarlo                                                   |
|-------------------------------|-------------------------------|-----------------------------------------------------------------|
| **AWS Storage Gateway**       | Ibrido on-prem ↔ cloud        | Per ambienti locali che necessitano archiviazione o backup      |
| **[AWS Backup](AWS-Backup.md)**           | Backup cloud centralizzato      | Per orchestrare backup di servizi AWS e on-prem                 |
| **[Amazon S3](Amazon-S3.md)**             | Object storage cloud            | Per accesso diretto a oggetti tramite API                       |
| **[Amazon FSx](Amazon-FSx.md)**           | File system cloud gestito       | Per workload compatibili con SMB/NFS/ONTAP                      |
| **[AWS Outposts](AWS-Outposts.md)**       | Infrastruttura ibrida gestita   | Quando serve eseguire servizi AWS localmente per bassa latenza  |

---

## 🛠️ Modalità di deployment

- **Appliance virtuale:** VMware ESXi, Microsoft Hyper-V, Linux KVM
- **Appliance hardware AWS:** dispositivi preconfigurati
- **Deployment in [Amazon EC2](Amazon-EC2.md):** per gateway interamente nel cloud

---

AWS Storage Gateway è perfetto per aziende che vogliono **estendere lo storage locale verso il cloud** in modo graduale, senza perdere compatibilità e con **integrazione nativa nei propri flussi operativi**.
