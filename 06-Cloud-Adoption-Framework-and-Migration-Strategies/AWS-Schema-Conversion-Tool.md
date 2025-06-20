--> [AWS](00-Intro/AWS.md)  -  [Migration Strategies](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Strategies.md)
# AWS Schema Conversion Tool (AWS SCT)

**AWS Schema Conversion Tool (SCT)** è un'applicazione desktop gratuita che consente di **convertire lo schema e i codici di database come procedure e funzioni** da motori commerciali (come Oracle, SQL Server) verso database open-source e cloud-native come [Amazon-Aurora](04-Database-services/Amazon-Aurora.md), PostgreSQL, MySQL, [Amazon-Redshift](Amazon-Redshift.md), ecc.

![sct usage](sct-usage.png)

---

## 🎯 Obiettivo

Facilitare la **modernizzazione dei database** riducendo i costi di licenza e migliorando la scalabilità con tecnologie cloud-native.

---

## 🧩 Caratteristiche principali

- **Conversione dello schema**: tabelle, indici, view, stored procedure
- Supporto per:
  - Oracle → [Amazon-Aurora](04-Database-services/Amazon-Aurora.md) PostgreSQL / MySQL
  - SQL Server → PostgreSQL / MySQL
  - Oracle → [Amazon-Redshift](Amazon-Redshift.md) (per data warehouse)
- Analizza la **complessità della conversione**
- Evidenzia codice **non compatibile** o che richiede modifica manuale
- Supporta conversione **completa o parziale** di schemi

---

## 🔄 Flusso di lavoro

1. Connetti al database sorgente (on-premises o cloud)
2. Connetti al database target ([Amazon-Aurora](04-Database-services/Amazon-Aurora.md), [Amazon-RDS](04-Database-services/Amazon-RDS.md), [Amazon-Redshift](Amazon-Redshift.md))
3. Esegui un’**analisi di compatibilità**
4. Converti lo schema e **esporta il DDL**
5. Migra i dati con [AWS-Database-Migration-Service](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Database-Migration-Service.md)

---

## 🔧 Esempio di componenti convertibili

- Tabelle e colonne
- Indici, vincoli e chiavi primarie
- Procedure e funzioni (compatibili)
- Trigger, sequence, view

---

## 📦 Integrazione con AWS DMS

AWS SCT può esportare i file per l’uso diretto in [AWS-Database-Migration-Service](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Database-Migration-Service.md), che si occupa del trasferimento effettivo dei dati in modo affidabile e con downtime minimo.

---

## 🔐 Sicurezza

- Nessuna connessione automatica a Internet
- Connessioni cifrate ai database
- Può essere eseguito **offline**, ideale per ambienti regolamentati

---

## ✅ Best Practices

- Inizia con un'**analisi di compatibilità**
- Identifica oggetti non convertibili automaticamente
- Convalida gli schemi convertiti prima del deploy
- Usa SCT in combinazione con [AWS-Database-Migration-Service](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Database-Migration-Service.md) per flussi completi

---

## 📌 Conclusioni

AWS Schema Conversion Tool è un alleato chiave per le aziende che vogliono **migrare database legacy verso soluzioni cloud-native** senza riscrivere tutto da zero. Automatizza la parte più complessa della migrazione: **la compatibilità tra motori SQL differenti**.

> “Modernizza il tuo database, non solo dove lo ospiti.”
