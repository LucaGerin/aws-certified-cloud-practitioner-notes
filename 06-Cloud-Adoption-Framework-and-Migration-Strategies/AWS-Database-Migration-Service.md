--> [AWS](AWS.md)  -  [Migration Strategies](AWS-Migration-Strategies.md)
# AWS Database Migration Service (AWS DMS)

**AWS Database Migration Service (DMS)** è un servizio gestito da [AWS](AWS.md) che consente di migrare facilmente database verso e all'interno di AWS. Supporta **migrazioni continue o una tantum** di dati tra database eterogenei (es. Oracle → PostgreSQL) o omogenei (es. MySQL → [Amazon-RDS](Amazon-RDS.md) for MySQL).

![DMS](06-Cloud-Adoption-Framework-and-Migration-Strategies/img/DMS.png)

---

## 🧩 Caratteristiche principali

- **Supporto per database eterogenei**: es. SQL Server → [Amazon-Aurora](Amazon-Aurora.md), Oracle → PostgreSQL
- **Migrazioni omogenee e eterogenee** (es. MySQL → Aurora o Oracle → PostgreSQL)
- **Replica dei dati in tempo reale**
- **Replica continua (CDC)**: usa la tecnica **Change Data Capture** per replicare modifiche in tempo reale
- **Alta disponibilità**: opzione Multi-AZ per fault tolerance
- **Nessun downtime**: progettato per minimizzare l'impatto su database sorgente
- **Gestione semplificata**: completamente gestito da [AWS](AWS.md), senza necessità di installare software lato sorgente o destinazione

---

## 🔄 Tipi di migrazione supportati

1. **Migrazione omogenea**  
   Esempio: [Amazon-RDS](Amazon-RDS.md) for MySQL → [Amazon-Aurora](Amazon-Aurora.md) MySQL  
   → struttura e motore del database sono simili

2. **Migrazione eterogenea**  
   Esempio: Oracle → [Amazon-Aurora](Amazon-Aurora.md) PostgreSQL  
   → richiede [AWS-Schema-Conversion-Tool](AWS-Schema-Conversion-Tool.md) per convertire schema e codice

3. **Replica continua**  
   Mantiene database sincronizzati in tempo reale per operazioni di failover o analytics

---

## 🧩 Casi d’uso comuni

- Spostamento da database legacy verso database cloud-native (es. [Amazon-Aurora](Amazon-Aurora.md) o [Amazon-DynamoDB](Amazon-DynamoDB.md))
- Consolidamento di più database in uno solo
- Migrazione da ambienti on-premise a [Amazon-RDS](Amazon-RDS.md)
- Replica continua per disaster recovery o ambienti ibridi

---

## ✅ Vantaggi

- Nessun bisogno di interrompere l’operatività durante la migrazione
- **Servizio completamente gestito**
- Costi contenuti: si paga solo per il tempo di esecuzione
- Facile da configurare tramite la console [AWS](AWS.md) o CLI

---

## 🧪 Integrazione con altri strumenti

- **[AWS-Schema-Conversion-Tool](AWS-Schema-Conversion-Tool.md)**: per convertire gli schemi nei casi di migrazione eterogenea
- **[AWS-Migration-Hub](AWS-Migration-Hub.md)**: per monitorare l'avanzamento della migrazione

---

## 📘 Conclusione

AWS DMS è uno strumento potente e flessibile che consente di spostare dati critici nel cloud in modo sicuro e con downtime minimo, accelerando la modernizzazione del proprio stack tecnologico.
