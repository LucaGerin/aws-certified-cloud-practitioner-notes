# AWS Service Catalog

AWS Service Catalog consente alle organizzazioni di creare, gestire e distribuire cataloghi di prodotti IT approvati per l'uso su AWS. Questi prodotti possono includere risorse come macchine virtuali, database, architetture complete e servizi personalizzati.

## Cos'è e come funziona

Con AWS Service Catalog, gli amministratori possono centralizzare la gestione dei prodotti IT e imporre controlli di governance. 

I prodotti vengono definiti come stack [AWS CloudFormation](/01-Compute-options/AWS-Cloud-Formation.md) (IaaC) e pubblicati in cataloghi accessibili agli utenti finali tramite la console AWS o interfacce personalizzate. 

Gli utenti possono sfogliare i cataloghi, lanciare e gestire prodotti senza dover conoscere i dettagli tecnici sottostanti.

![Service Catalog](/09-Sicurezza-Compliance-Governance/img/AWS-Service-Catalog.png)

### Funzionamento principale:

- Gli **amministratori IT** creano e pubblicano i prodotti.
- Gli **utenti finali** accedono al catalogo e avviano i prodotti secondo le configurazioni approvate.
- Il tutto avviene con visibilità e controllo su compliance, costi e sicurezza.

## Use cases

- **Provisioning standardizzato**: le aziende possono fornire ai team un set approvato di risorse AWS, evitando configurazioni non conformi.
- **Ambienti di sviluppo self-service**: gli sviluppatori possono accedere a stack predefiniti per creare ambienti in pochi clic.
- **Gestione multi-account**: ideale per grandi aziende che gestiscono più account AWS tramite [AWS Organizations](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Organizations.md).
- **Automazione di deployment**: integrato con AWS CodePipeline e AWS CloudFormation per CI/CD controllata.
    

## Sicurezza

- **Controllo degli accessi con IAM**: gli amministratori possono limitare chi può accedere, creare o modificare i prodotti nel catalogo.
    
- **Audit e logging**: integra con [AWS CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md) per tenere traccia delle operazioni.
    
- **Conformità aziendale**: aiuta a garantire che tutte le risorse distribuite siano conformi agli standard IT dell'organizzazione.
    

## Pricing

L'utilizzo di AWS Service Catalog non ha costi aggiuntivi. Si pagano solo le risorse AWS sottostanti (come EC2, S3, RDS, ecc.) che vengono lanciate tramite i prodotti del catalogo.

## Confronto con servizi simili in AWS

| Caratteristica                    | AWS Service Catalog                       | [AWS CloudFormation](/01-Compute-options/AWS-Cloud-Formation.md) | [AWS Control Tower](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Control-Tower.md) |
| --------------------------------- | ----------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Scopo principale                  | Catalogo di prodotti IT per utenti finali | Definizione e provisioning di infrastruttura                     | Gestione multi-account con guardrail                                                                  |
| Interfaccia utente                | Sì (console dedicata per utenti finali)   | No (template JSON/YAML via console/CLI)                          | Sì (dashboard centrale)                                                                               |
| Governance e approvazioni         | Sì                                        | No                                                               | Sì                                                                                                    |
| Supporto a modelli personalizzati | Sì (via CloudFormation)                   | Sì                                                               | Limitato ai blueprint disponibili                                                                     |
| Integrazione con IAM              | Sì                                        | Sì                                                               | Sì                                                                                                    |

## Conclusione

AWS Service Catalog è ideale per organizzazioni che vogliono fornire ai team un modo sicuro, standardizzato e controllato per distribuire risorse su AWS, migliorando la governance e riducendo il rischio operativo.