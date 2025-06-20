--> [AWS](00-Intro/AWS.md)  -  [Compute Options](01-Compute-options/AWS-Compute-Options.md)

# AWS Outposts

AWS Outposts è una soluzione **ibrida** che porta l'infrastruttura, i servizi e gli strumenti AWS direttamente **on-premises**. È pensata per aziende che vogliono estendere l'esperienza AWS nel proprio data center, mantenendo coerenza con il cloud pubblico.

---

## 🔧 Cos'è e come funziona

AWS Outposts consiste in **hardware fisico AWS** installato nei locali del cliente. Il servizio consente di eseguire servizi AWS (come EC2, ECS, EKS, RDS, ecc.) localmente, utilizzando:

- Le stesse **API AWS**
- La **console di gestione AWS**
- I tool CLI e SDK standard

Outposts si connette a una AWS Region per gestire provisioning, aggiornamenti, e integrazione con altri servizi cloud, ma è progettato per funzionare anche con **bassa connettività** o in modalità locale.

![outposts](outposts.png)

---

## ⭐ Caratteristiche principali e vantaggi

- **Hardware AWS gestito:** Fornito, installato, monitorato e aggiornato da AWS
- **Esperienza unificata:** Le applicazioni usano le stesse API e strumenti AWS, sia on-prem che nel cloud
- **Supporto per servizi familiari:** [EC2](01-Compute-options/Amazon-EC2.md), [EBS](02-Storage-services/Amazon-EBS.md), ECS, EKS, RDS, EMR, S3 on Outposts
- **Connettività ibrida:** Comunicazione sicura e veloce tra ambienti locali e AWS Region
- **Compliance e sovranità:** Ideale per aziende con requisiti normativi o di localizzazione dei dati
- **Monitoring e gestione centralizzati:** Integrazione con CloudWatch, Config, Systems Manager

---

## 🚀 Use Cases

- **Applicazioni a bassa latenza:** Come sistemi industriali, medici, o di streaming locale
- **Elaborazione e archiviazione di dati locali:** In contesti in cui i dati non possono lasciare il sito
- **Ambienti regolamentati:** Settori come finanza, sanità, pubblica amministrazione
- **Edge computing ibrido:** Estensione locale del cloud per pre-elaborazione o risposta immediata
- **Migrazione graduale al cloud:** Spostando carichi al cloud in modo incrementale e senza interruzioni

---

## 💰 Pricing

Il pricing di AWS Outposts si basa su:
- **Tipo di configurazione hardware scelto** (es. CPU, RAM, storage)
- **Durata del contratto** (1 o 3 anni)
- Opzioni **on-demand** o con **prenotazione anticipata**

I costi comprendono:
- Fornitura e gestione dell’hardware
- Accesso ai servizi AWS abilitati su Outposts
- Supporto operativo e aggiornamenti automatici

⚠️ I prezzi variano molto in base alla configurazione. È necessario richiedere un'offerta personalizzata da AWS.

---

## 🔐 Sicurezza

- **IAM per controllo accessi** coerente con l’ambiente AWS pubblico
- **Dati cifrati in transito e a riposo**, anche localmente
- **Conformità a standard di sicurezza** come ISO, SOC, HIPAA (a seconda della configurazione)
- **Segregazione fisica dei dati:** hardware dedicato installato presso il cliente
- **Logging centralizzato:** Integrazione con CloudTrail e CloudWatch Logs

---

## 🔄 Confronto con servizi simili in AWS

| Servizio            | Tipo                | Quando usarlo                                                  |
|---------------------|---------------------|----------------------------------------------------------------|
| **Outposts**        | Cloud ibrido on-prem| Quando servono servizi AWS locali per bassa latenza o compliance |
| **Local Zones**     | Estensione regionale| Per bassa latenza in città remote rispetto alla region principale |
| **Wavelength**      | Edge computing telco| Per app mobili ultra-low latency in reti 5G                     |
| **Snow Family**     | Edge computing/offline| Per ambienti disconnessi o mobili (es. navi, militare, campagne) |

---

## 📊 Integrazioni e strumenti consigliati

- **Deployment e provisioning:** CloudFormation, Terraform, AWS CDK
- **CI/CD:** CodePipeline, GitHub Actions, Jenkins
- **Monitoring:** Amazon CloudWatch, AWS Systems Manager
- **Networking ibrido:** AWS Direct Connect, VPN, Transit Gateway

---

## 📌 Best Practices

- Validare la necessità reale di una soluzione ibrida prima della scelta
- Pianificare attentamente la **rete ibrida** tra Outposts e AWS Region
- Monitorare la **capacità residua** dell’hardware per evitare limiti locali
- Utilizzare **tool IaC** per coerenza tra ambienti locali e cloud
- Tenere traccia delle **policy di sicurezza e accesso** locali e cloud

---

AWS Outposts è pensato per aziende che vogliono unire i benefici del cloud AWS alla **vicinanza fisica dei propri sistemi o dei propri dati**, senza rinunciare a scalabilità, sicurezza e automazione.
