--> [AWS](00-Intro/AWS.md)  -  [Storage Services](02-Storage-services/AWS-Storage-Services.md)
# Elastic Disaster Recovery (EDR)

**Elastic Disaster Recovery (EDR)** è un servizio cloud-based che consente il **ripristino rapido di server e applicazioni** in caso di guasti, disastri naturali, errori umani o attacchi informatici. Il termine "elastic" fa riferimento alla capacità del servizio di **scalare dinamicamente** in base alle necessità operative, rendendolo particolarmente adatto a scenari cloud come AWS.

---

## 🔧 Cos'è e come funziona

EDR consente di replicare continuamente i dati da server fisici, virtuali o cloud verso AWS. In caso di disastro, è possibile eseguire un failover automatico su [Amazon EC2](01-Compute-options/Amazon-EC2.md). Quando l’ambiente originale torna operativo, si può procedere al **failback**.

### Fasi operative:

1. **Installazione di un agente** sul server di origine
2. **Replica asincrona** dei dati verso [Amazon S3](02-Storage-services/Amazon-S3.md) e [Amazon EBS](02-Storage-services/Amazon-EBS.md)
3. In caso di evento critico, **ripristino automatico** su EC2 con configurazioni predefinite
4. **Failback** con sincronizzazione dei dati per tornare all’ambiente originale

EDR è disponibile come servizio gestito: **AWS Elastic Disaster Recovery (AWS DRS)**.

### ⚙️ Come abilitare AWS Elastic Disaster Recovery

Per abilitare AWS DRS, accedi alla console del servizio, registra i server di origine (on-premises o EC2) e installa l’**AWS Replication Agent** su ciascun sistema da proteggere. Una volta installato, puoi configurare la replica continua verso AWS e definire le impostazioni di recovery (tipo di istanza, rete, storage). In caso di disastro, puoi avviare rapidamente il failover con un clic dalla console.

---

## ⭐ Caratteristiche principali e vantaggi

- **Replica continua e leggera** dei dati, con aggiornamenti in tempo quasi reale
- **Ripristino automatico e orchestrato** su infrastrutture target (es. EC2)
- **Supporto multi-ambiente:** on-premises → cloud, cloud → cloud
- **Test di recovery** eseguibili in produzione senza impatto
- **Scalabilità elastica**: si adatta automaticamente al numero di server protetti
- **Compatibilità** con vari OS, hypervisor e ambienti IT
- **Costi inferiori** rispetto alle soluzioni di DR tradizionali

---

## Tecniche di Disaster recovery di AWS

**NB:** Le seguenti tecniche non sono esclusive di Elastic Disaster Recovery (EDR), ma EDR può essere usato per implementarle.

Le strategie di disaster recovery offerte da AWS possono essere suddivise in quattro approcci principali, che vanno da soluzioni a basso costo e bassa complessità fino a configurazioni avanzate che sfruttano più regioni attive contemporaneamente. 
Queste strategie si collocano lungo uno spettro che bilancia costi, complessità e tempi di ripristino (RTO) e perdita di dati accettabile (RPO):

- **Backup & Restore**: è la soluzione più semplice ed economica. I dati vengono salvati regolarmente e le risorse AWS vengono create e ripristinate solo in seguito a un evento. Ha un RPO/RTO di alcune ore ed è adatta a use case non critici.
- **Pilot Light**: mantiene attivi i dati, ma lascia inattivi i servizi, pronti per essere scalati dopo un evento. Offre RPO/RTO di decine di minuti, con costi moderati.
- **Warm Standby**: replica l'ambiente in una versione più piccola e sempre attiva. È adatta a carichi di lavoro business-critical, con un RPO/RTO di pochi minuti e un costo maggiore.
- **Multi-site Active/Active**: le risorse sono attive in più regioni contemporaneamente. Garantisce ripristino in tempo reale, zero downtime e perdita dati prossima allo zero, ma a costi elevati. È la soluzione ideale per servizi mission-critical.

Le strategie **active/passive** prevedono che una sola regione AWS sia attiva e serva il traffico, mentre l’altra rimanga in attesa e subentri solo in caso di failover.


![Tecniche di disaster recovery](disaster-recovery-options.png)

---

## 🚀 Use Cases

- **Riduzione dei costi del disaster recovery** senza compromettere tempi di ripristino
- **Continuità operativa** per applicazioni business-critical
- **Transizione verso il cloud** con opzione di ritorno
- **Protezione di ambienti ibridi o legacy**
- **Disaster recovery regolamentato**, con requisiti di RTO/RPO

---

## 💰 Pricing

Il pricing di AWS DRS si basa su:

- **Numero di server replicati**
- **Storage utilizzato su [Amazon S3](02-Storage-services/Amazon-S3.md) e [Amazon EBS](02-Storage-services/Amazon-EBS.md)**
- **Durata delle istanze EC2** durante il ripristino (fatturata solo al momento del failover)
- **Operazioni di rete e snapshot**

⚠️ Il costo è generalmente inferiore rispetto a mantenere un'infrastruttura DR sempre attiva.

---

## 🔐 Sicurezza

- **Crittografia dei dati in transito e a riposo** tramite [AWS KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)
- **Controllo degli accessi** e gestione utenti tramite [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)
- **Log e audit** delle operazioni tramite [AWS CloudTrail](08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)
- **Isolamento degli ambienti di recovery** tramite [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md)

---

## 🔄 Confronto con servizi simili in AWS

| Servizio                        | Tipo                         | Quando usarlo                                                  |
|----------------------------------|------------------------------|----------------------------------------------------------------|
| **Elastic Disaster Recovery (EDR)** | DR scalabile cloud-native     | Per replica e failover automatici con RTO/RPO minimi           |
| **[AWS Backup](02-Storage-services/AWS-Backup.md)**            | Backup centralizzato          | Per backup pianificati, non per failover automatico            |
| **[AWS Storage Gateway](02-Storage-services/AWS-Storage-Gateway.md)** | Backup/archiviazione ibrida   | Per protezione dei dati on-premises in modo asincrono          |
| **[AWS Outposts](01-Compute-options/AWS-Outposts.md)**         | Infrastruttura on-prem AWS    | Per eseguire i workload direttamente on-prem, non per failover |

---

Elastic Disaster Recovery è una soluzione moderna, scalabile e conveniente per garantire **resilienza e continuità operativa**, riducendo al minimo il downtime e l'impatto sul business.
