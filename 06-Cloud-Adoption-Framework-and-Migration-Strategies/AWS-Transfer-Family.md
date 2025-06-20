--> [AWS](/00-Intro/AWS.md)  -  [Migration Strategies](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Strategies.md)
# 🔁 AWS Transfer Family

## Cos'è e come funziona

**AWS Transfer Family** è un servizio completamente gestito che consente di **trasferire file in modo sicuro** da e verso **Amazon S3 o Amazon EFS**, utilizzando protocolli standard come:

- **SFTP (Secure File Transfer Protocol)**
- **FTPS (File Transfer Protocol Secure)**
- **FTP (File Transfer Protocol)**

Questo servizio permette alle organizzazioni di **modernizzare i flussi di lavoro basati su file**, senza dover modificare le applicazioni o infrastrutture esistenti, offrendo una **migrazione trasparente verso il cloud** che non intacchi i flussi workflow in corso.

Gli utenti possono autenticarsi tramite:
- Directory Service (AD)
- Identity provider con SAML
- Database custom o Lambda

## Caratteristiche principali e vantaggi

- 🌐 **Supporto per protocolli standard** (SFTP, FTPS, FTP)
- 🗃️ **Integrazione nativa con S3 ed EFS**
- 🔒 **Sicurezza avanzata** con crittografia in transito e integrazione IAM
- 🧩 **Compatibilità con sistemi legacy**, senza dover riscrivere codice
- 📈 **Scalabilità automatica** per gestire carichi variabili
- 🕒 **Alta disponibilità e resilienza** in ambiente fully managed

## Use cases

- 🏦 **Scambio file con partner esterni** in settori come finanza, sanità e pubblica amministrazione
- 🏢 **Modernizzazione di flussi FTP legacy** mantenendo compatibilità con client esistenti
- 📂 **Caricamento dati ricorrente verso Amazon S3** (es. report, log, dati CSV)
- 🔄 **Integrazione con sistemi ERP** o applicazioni on-premise

## Sicurezza

- Supporta **autenticazione multifattoriale e crittografia** (TLS, SFTP, ecc.)
- È possibile **loggare accessi e operazioni** tramite AWS CloudTrail
- Si integra con **AWS KMS** per la gestione delle chiavi di crittografia
- Permette l'uso di **endpoint VPC** per mantenere il traffico all’interno della rete privata AWS

## Confronto con servizi simili in AWS

| Servizio                      | Differenza principale                                                |
|------------------------------|----------------------------------------------------------------------|
| [Amazon S3](/02-Storage-services/Amazon-S3.md)                    | S3 è lo storage sottostante, ma non offre nativamente un'interfaccia FTP/SFTP |
| AWS DataSync           | Ottimizzato per trasferimenti bulk e sincronizzazioni periodiche       |
| [AWS Snowball Edge](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Snowball-Edge.md)   | Usato per trasferimenti fisici o in ambienti offline                   |

**AWS Transfer Family** è la soluzione ideale per chi deve **mantenere flussi file-based** senza rinunciare ai vantaggi del cloud.

## Pricing

Il pricing di AWS Transfer Family si basa su:
- 📥 **Numero di connessioni attive**
- 📦 **Volume di dati trasferiti (per GB)**
- 🔐 Eventuali costi per **autenticazione e audit avanzati**

Non ci sono costi fissi per l’infrastruttura: **paghi solo per ciò che usi**, rendendolo adatto sia a flussi occasionali che ad alti volumi.

---
