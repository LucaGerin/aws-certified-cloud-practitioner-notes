--> [AWS](00-Intro/AWS.md)  -  [Database Services](04-Database-services/AWS-Databases.md)
# AWS Database Migration Service (AWS DMS)

## Introduzione

**AWS Database Migration Service (AWS DMS)** è un servizio gestito che consente di migrare database e data warehouse su AWS in modo semplice, sicuro e con downtime minimo, da on-premise verso il cloud o tra database nel cloud. 

Supporta migrazioni **omogenee** (stesso motore di database) e **eterogenee** (motori diversi), in tempo reale o in batch.

![Database Migration Service](04-Database-services/img/DMS.png)

NB: In caso di **migrazione eterogenea** (cioè tra motori di database diversi, es. da Oracle a PostgreSQL), **AWS DMS non si occupa della conversione dello schema**.
Per questi casi, si deve usare **[AWS Schema Conversion Tool (SCT)](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Schema-Conversion-Tool.md)**, che analizza lo schema del database di origine, lo converte nel formato compatibile con il motore di destinazione, e può anche evidenziare elementi che non possono essere convertiti automaticamente.
Poi, DMS  si occupa di:
- Trasferire **i dati** (dopo che lo schema è pronto sul target),
- Supportare la **replicazione continua** per mantenere sincronizzati origine e destinazione,

---

## Caratteristiche principali

- **Supporto multi-motore**: compatibile con database relazionali (es. MySQL, PostgreSQL, Oracle, SQL Server), NoSQL (MongoDB), e data warehouse (Redshift, Snowflake).
- **Migrazione in tempo reale**: replica dei dati continua con Change Data Capture (CDC).
- **Basso downtime**: applicazioni possono rimanere attive durante la migrazione.
- **Semplicità di gestione**: provisioning e monitoraggio tramite console o API AWS.
- **Sicurezza integrata**: supporto per [VPC](03-CDN-e-Networking/Amazon-VPC.md), crittografia TLS e [KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md).
- **Database consolidation:** permette di consolidare più database in uno solo.

---

## Casi d’uso comuni

- **Migrazione di database on-premise verso AWS**.
	- Per Analytics
	- Per de-commissionare i data center
- **Replica tra database AWS in diverse regioni**.
- **Migrazione da database proprietari a open source** (es. da Oracle a PostgreSQL).
- **Consolidamento di database distribuiti in un unico DB**.
- **Backup continuo verso S3 per analisi o archiviazione**.

---

## Architettura

AWS DMS utilizza tre componenti principali:

- **Endpoint di origine (Source)**: il database da cui migrare i dati.
- **Endpoint di destinazione (Target)**: dove i dati vengono replicati.
- **Replication instance**: server gestito che gestisce la logica di migrazione.

### Flusso di lavoro:
1. Creazione dei due endpoint (source e target).
2. Creazione di una **replication instance**.
3. Configurazione di una **migration task**.
4. Avvio della migrazione iniziale e/o replicazione continua (CDC).

---

## Tipi di migrazione

| Tipo                   | Descrizione                                                            |
|------------------------|------------------------------------------------------------------------|
| **Omogenea**           | Stesso motore (es. MySQL → Amazon RDS MySQL)                          |
| **Eterogenea**         | Motori diversi (es. Oracle → Amazon Aurora PostgreSQL), con il supporto di [SCT](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Schema-Conversion-Tool.md)                |
| **One-time load**      | Copia una tantum dei dati                                              |
| **Full load + CDC**    | Copia iniziale seguita da replica in tempo reale                      |

> 🔧 Per migrazioni eterogenee è consigliato l’uso di **[AWS Schema Conversion Tool (SCT)](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Schema-Conversion-Tool.md)** per adattare schemi, tipi di dato e codice SQL ai formati compatibili con AWS.
> Aiuta anche a tradurre codice, funzioni, viste del database di origine.

---

## Supporto motori (alcuni esempi)

| Origine                        | Destinazione                   |
|-------------------------------|--------------------------------|
| Oracle                        | Amazon RDS, Aurora, Redshift   |
| Microsoft SQL Server          | Amazon RDS, Aurora             |
| MySQL / MariaDB               | RDS, Aurora, Redshift, S3      |
| PostgreSQL                    | RDS, Aurora, Redshift, S3      |
| MongoDB                       | Amazon DocumentDB, S3          |
| SAP ASE, Db2, Sybase, etc.    | Aurora, Redshift, S3           |

---

## Prezzi

I costi dipendono da:

- **Dimensione della replication instance** (ore di utilizzo)
- **Storage allocato** per log temporanei
- **Trasferimento dati**
- **Backup automatici** (se abilitati)

---

## Limitazioni da considerare

- Alcune funzioni avanzate dei motori database potrebbero non essere supportate pienamente (es. stored procedure, trigger).
- La conversione degli schemi richiede un tool separato (AWS SCT).
- Per prestazioni ottimali, è consigliato usare database target già dimensionati.

---

## Conclusione

AWS Database Migration Service è una soluzione potente e flessibile per spostare i dati verso il cloud AWS con minimo downtime. È particolarmente utile per le aziende che desiderano modernizzare la propria infrastruttura, migrare verso motori open-source o consolidare dati distribuiti in un’unica piattaforma scalabile.

