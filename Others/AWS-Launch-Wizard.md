--> [AWS](00-Intro/AWS.md)
# 🚀 AWS Launch Wizard

## Cos'è e come funziona

**AWS Launch Wizard** è un servizio che **semplifica e automatizza il provisioning di applicazioni complesse** su AWS, guidando l’utente attraverso una procedura passo-passo per distribuire architetture complete, ottimizzate e pronte all'uso.  
Supporta applicazioni aziendali come **Microsoft SQL Server, SAP, Active Directory, Amazon Elastic Kubernetes Service (EKS)** e altre, eliminando la necessità di configurazioni manuali complesse.

Durante il processo di deployment, Launch Wizard consente di:
- Definire i requisiti tecnici e parametri (capacità, storage, rete, ecc.)
- Ricevere una **stima dei costi** prima dell’avvio
- Lanciare e configurare automaticamente risorse come **EC2, EBS, VPC, IAM** e altro
- Salvare le configurazioni come **template riutilizzabili**

## Caratteristiche principali e vantaggi

- ⚙️ **Automazione end-to-end** del deployment di soluzioni complesse
- 🧩 **Integrazione con altri servizi AWS** (EC2, Systems Manager, CloudFormation, ecc.)
- 📊 **Stima dei costi** in tempo reale prima del provisioning
- 🔄 **Template personalizzabili e riutilizzabili**
- 🔒 Supporta best practices AWS per **sicurezza e resilienza**
- 🧠 **Riduce errori manuali** e curva di apprendimento per utenti meno esperti

## Use cases

- 🏢 Deployment rapido e coerente di ambienti **SAP** o **SQL Server** in ambienti enterprise
- 🧪 Creazione di ambienti di test/staging per **applicazioni complesse**
- 🧱 Standardizzazione dei processi di provisioning in team DevOps
- 🧑‍💼 Facilitare il lavoro di team IT o system integrator nel configurare ambienti AWS

## Sicurezza

- Le risorse sono lanciate in base ai **principi di least privilege** tramite IAM.
- Supporta deployment in VPC privati e configurazioni **Multi-AZ** per alta disponibilità.
- Permette di **monitorare e gestire** l'ambiente con Amazon CloudWatch e Systems Manager.

## Confronto con servizi simili in AWS

| Servizio                      | Differenza principale                                   |
|------------------------------|----------------------------------------------------------|
| [AWS CloudFormation](05-Development-Messaging-Deploying/AWS-CloudFormation.md)         | Richiede la scrittura e manutenzione di template YAML/JSON |
| [Elastic Beanstalk](05-Development-Messaging-Deploying/AWS-Elastic-Beanstalk.md)           | Ottimizzato per app web, non per applicazioni enterprise complesse |
| [AWS Application Migration Service](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Application-Migration-Service.md) | Si concentra sulla migrazione lift-and-shift, non su nuovi deployment |

Launch Wizard è ideale quando serve **un approccio guidato e interattivo** per distribuire ambienti enterprise su AWS, senza doversi preoccupare dei dettagli infrastrutturali.

## Pricing

**AWS Launch Wizard non comporta costi aggiuntivi** per l'utilizzo del servizio stesso.  
Paghi solo le **risorse AWS sottostanti** (EC2, EBS, RDS, ecc.) che vengono lanciate durante il provisioning. Prima della creazione, viene comunque mostrata una **stima dettagliata dei costi**.

---
