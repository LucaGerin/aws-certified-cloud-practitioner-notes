--> [AWS](AWS.md)
# 🔐 Sicurezza, Compliance e Governance in AWS

## 📘 Introduzione

Nel cloud [AWS](AWS.md), la sicurezza, la conformità e la governance sono responsabilità condivise tra AWS e il cliente (Vedi [Shared Responsibility Model](Shared-Responsibility-Model.md)). 
AWS fornisce un'infrastruttura cloud **sicura per impostazione predefinita**, mentre il cliente è responsabile della **configurazione sicura e conforme** delle proprie risorse.

Il modello si basa su tre pilastri fondamentali:
- **Sicurezza (Security)**: protezione di dati, workload e identità.
- **Conformità (Compliance)**: aderenza a normative e standard (es. GDPR, ISO, HIPAA).
- **Governance**: visibilità, controllo e audit delle risorse e delle configurazioni.

Per supportare questi ambiti, AWS offre una vasta gamma di **servizi integrati**, classificabili in categorie specifiche.

---

## 🛡️ Servizi di Sicurezza

La sicurezza del cloud si basa su queste due domande:
- Chi ha accesso?
- Cosa può fare chi ha accesso?

Le aree da coprire sono:
- Gestione di identità e accesso
- Stewardship dei dati e crittografia
- Sicurezza del network
- Sicurezza delle applicazioni
- Compliance
- Security management

### 🔐 Principio del Least Privilege

Il **principio del minimo privilegio** (Least Privilege) è una best practice fondamentale nella sicurezza informatica e nella gestione degli accessi in AWS. Consiste nel garantire che **ogni utente, ruolo, servizio o applicazione abbia solo i permessi strettamente necessari** per svolgere le proprie funzioni, e niente di più.

Applicare questo principio riduce drasticamente la **superficie d’attacco** e limita i potenziali danni in caso di errore umano o compromissione. 
In AWS, questo si traduce nella scrittura di **policy IAM granulari**, nell’utilizzo di **ruoli temporanei** con **scadenze limitate** (es. con AWS STS), e nell’**audit regolare dei permessi** per rimuovere quelli non più necessari.

> “Meno accesso significa più sicurezza: concedi solo ciò che è richiesto, solo quando serve.”

---

### 👤 Identity & Access Management (IAM)

- **[AWS IAM](AWS-IAM.md)**: gestione di utenti, ruoli, policy di accesso
- **[AWS SCP](AWS-Service-Control-Policies.md)**: definizione di limiti ai permessi IAM a livello di account
- **[IAM Access Analyzer](IAM-Access-Analyzer.md)**: identifica accessi non intenzionali alle risorse
- **[IAM Policy Simulator](IAM-Policy-Simulator.md)**: testa le nuove policies IAM prima di concederle.
- **[AWS Cognito](AWS-Cognito.md)**: gestione identità utente per app web/mobile
- **AWS SSO ([IAM Identity Center](AWS-IAM-Identity-Center.md))**: gestione centralizzata identità e accessi
- **[AWS Systems Manager Session Manager](AWS-Systems-Manager-Session-Manager.md)**: gestione delle sessioni di accesso alle risorse

### 🔐 Protezione dei dati

La protezione dei dati si basa sulla crittografia dei dati salvati nelle risorse e l'utilizzo di protocolli sicuri come HTTPS (Che usa TLS - Transport Layer Security) per i dati in transito.
I servizi utili a questi propositi sono:
- **[AWS KMS](AWS-KMS.md) (Key Management Service)**: gestione delle chiavi di cifratura
- **[AWS Systems Manager Parameter Store](AWS-Systems-Manager-Parameter-Store.md)**: conserva parametri come username e password e gestisce l'accesso delle risorse a questi parametri.
- **[AWS Secrets Manager](AWS-Secrets-Manager.md)**: gestione sicura e avanzata di credenziali e segreti
- **[AWS Certificate Manager](AWS-Certificate-Manager.md)**: gestione di certificati SSL/TLS (Recupero, deploy, rinnovo)
- **[Amazon Macie](Amazon-Macie.md)**: rileva e protegge dati sensibili (es. PII) su S3

### Protezione delle reti
- **[AWS Network Firewall](AWS-Network-Firewall.md)**: Permette di definire regole complesse sul traffico rete da e verso una [VPC](Amazon-VPC.md).
- **[AWS WAF](AWS-WAF.md)**: firewall per proteggere applicazioni web
- **[AWS Shield](AWS-Shield.md)**: protezione da attacchi DDoS
- **[AWS Firewall Manager](AWS-Firewall-Manager.md)**: per gestire in modo centralizzato da un unico servizio la sicurezza del network
### 🧠 Rilevamento minacce e risposta

- **[AWS Security Hub](AWS-Security-Hub.md)**: aggregazione e punteggio degli eventi di sicurezza
- **[Amazon GuardDuty](Amazon-GuardDuty.md)**: rilevamento minacce e comportamenti anomali
- **[Amazon Inspector](Amazon-Inspector.md)**: scansione vulnerabilità EC2, Lambda, ECR
- **[Amazon Detective](Amazon-Detective.md)**: investiga gli eventi di sicurezza isolando gli eventi utili e cercando le cause

![Comparison of some security services](security-comparison.png)

**NB:** Per migliorare la sicurezza ci sono risorse da utilizzare:
- AWS Cloud security: una "wiki" per informazioni sulla sicurezza in AWS
- AWS Security Blog: per una prospettiva da parte degli esperti e sulle novità
- AWS Marketplace: per trovare soluzioni di sicurezza già costruite e collaudate

---
Un account in AWS è un insieme di risorse a cui degli utenti possono accedere. Gli account sono utilizzati, secondo best practice, dalle aziende per differenziare i gruppi di risorse che solo alcuni utenti devono vedere.
Per gestire più account in modo centralizzato, si può utilizzare [AWS Organizations](AWS-Organizations.md)

---

## 📋 Servizi per la Compliance

- **[AWS Artifact](AWS-Artifact.md)**: accesso a report di conformità, certificazioni e documentazione legale, per uso interno e per provare esternamente la compliance
- **[AWS Audit Manager](AWS-Audit-Manager.md)**: raccolta automatica delle evidenze per audit (SOC 2, GDPR, ISO)
- **[AWS Config](AWS-Config.md)**: valutazione continua della conformità delle risorse alle regole definite e continua registrazione dei cambiamenti alle configurazioni delle risorse.
- **[AWS Organizations](AWS-Organizations.md) + [SCPs](AWS-Service-Control-Policies.md)**: applicazione di policy di sicurezza a livello multi-account
- **[AWS Control Tower](AWS-Control-Tower.md)**: creazione di landing zone sicure e conformi
- **[AWS Well-Architected Tool](AWS-Well-Architected-Tool.md)**: valutazione di workload rispetto alle best practice (incluse sicurezza e governance)

**NB:** AWS si assicura che gli standard di compliance (ne supporta più di 140) siano soddisfatti solo nella sua parte dello [Shared Responsibility Model][Shared-Responsibility-Model.md]

**NB:** Non tutti i servizi AWS soddisfano tutti gli standard (e.g., per lo standard FIPS 40-2 level 3, [KMS](AWS-KMS.md) non va bene e deve essere sostituito da [AWS CloudHSM](AWS-CloudHSM.md))

---

## 📊 Servizi di Governance


- **[AWS CloudTrail](Amazon-CloudTrail.md)**: tracciamento di tutte le chiamate API e attività su AWS
- **[AWS Config](AWS-Config.md)**: storico delle configurazioni delle risorse (già citato in compliance)
- **AWS Service Catalog**: controllo su quali risorse possono essere create dagli utenti
- **[AWS Budgets](AWS-Budgets.md) e [Cost Explorer](AWS-Cost-Explorer.md)**: controllo dei costi per evitare sprechi non autorizzati
- **[AWS License Manager](AWS-License-Manager.md)**: gestione e tracciamento delle licenze software
- **[AWS Resource Access Manager](AWS-RAM.md) (RAM)**: condivisione sicura di risorse tra account

---

## 📌 Conclusione

AWS mette a disposizione un ecosistema completo di servizi per realizzare ambienti cloud **sicuri, conformi e governati**. Utilizzare questi strumenti in combinazione consente di:

- **Proteggere i dati sensibili**
- **Limitare gli accessi in modo granulare**
- **Automatizzare la conformità**
- **Garantire visibilità e tracciabilità delle attività**

> “In AWS, sicurezza non è un’opzione: è una strategia integrata e continua.”
