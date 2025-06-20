--> [AWS](00-Intro/AWS.md)  -  [Compute Options](01-Compute-options/AWS-Compute-Options.md)
# AWS CloudFormation
![cloudformation](CloudFormation.webp)

AWS CloudFormation è un servizio che consente di definire e gestire l’**infrastruttura come codice** (IaC) su AWS. Con CloudFormation, è possibile descrivere l'intera infrastruttura cloud tramite file di testo (YAML o JSON), in modo dichiarativo, ripetibile e versionabile.

---

## 🔧 Cos'è e come funziona

CloudFormation permette di modellare e provisionare le risorse AWS come **stack**: insiemi di risorse interdipendenti definite tramite un **template**. I template descrivono le risorse desiderate e CloudFormation si occupa di:

- Creare le risorse nell’ordine corretto
- Gestire le dipendenze tra risorse
- Applicare aggiornamenti in modo controllato (Change Sets)
- Effettuare rollback automatici in caso di errore

I template possono essere scritti in formato **YAML o JSON** e mantenuti sotto controllo versione, rendendo l’infrastruttura parte del ciclo di sviluppo software.

![cloudformation functioning](cloudformation-functioning.png)

---

## ⭐ Caratteristiche principali e vantaggi

- **Template dichiarativi:** Infrastruttura descritta come codice, leggibile e riutilizzabile.
- **Provisioning automatico:** AWS crea e configura tutte le risorse definite nel template.
- **Gestione dello stack:** Tutte le risorse sono trattate come un’entità unificata (stack), semplificando aggiornamenti e cancellazioni.
- **Rollback automatico:** In caso di errore nel provisioning, CloudFormation ripristina lo stato precedente.
- **Integrazione con CI/CD:** Funziona perfettamente con CodePipeline, CodeBuild, Jenkins, GitHub Actions, ecc.
- **Drift Detection:** Permette di rilevare modifiche manuali non conformi rispetto al template.
- **Supporto esteso:** Compatibile con la maggior parte dei servizi AWS (oltre 200 risorse supportate).

---

## 🚀 Use Cases

- **Deploy consistenti** su più ambienti (dev, test, prod) mantenendo standard e configurazioni identiche
- **Automazione completa del provisioning** e della configurazione di infrastrutture complesse
- **Standardizzazione tra team** tramite template condivisi
- **Audit e compliance** attraverso versionamento dell’infrastruttura
- **Disaster recovery e cloni ambientali**, replicando intere infrastrutture in pochi minuti

---

## 💰 Pricing

CloudFormation **non ha costi aggiuntivi** per l’utilizzo del servizio stesso. Si pagano solo le risorse AWS create dal template.

Eccezioni:
- **StackSets con amministrazione delegata**: in alcuni casi può essere applicato un costo per operazioni cross-account.
- **Third-party resource types** tramite il CloudFormation Registry: possono avere pricing specifici.

---

## 🔐 Sicurezza

- **Controlli IAM granulari:** È possibile definire chi può creare, aggiornare o cancellare stack e risorse.
- **Rollback sicuro:** In caso di fallimento, CloudFormation annulla automaticamente le modifiche.
- **Parametri cifrati:** Le variabili sensibili nei template (es. password) possono essere cifrate tramite AWS KMS.
- **Stack policy:** Permettono di proteggere risorse critiche da aggiornamenti accidentali

---

## 🔄 Confronto con servizi simili in AWS

| Servizio                  | Tipo                        | Quando usarlo                                               |
|---------------------------|-----------------------------|-------------------------------------------------------------|
| **CloudFormation**        | IaC nativo AWS              | Per IaC nativo, integrato, compatibile con quasi tutti i servizi |
| **CDK (Cloud Development Kit)** | IaC programmabile (TypeScript, Python, ecc.) | Per chi preferisce IaC imperativa con linguaggi reali        |
| **Terraform**             | IaC multi-cloud             | Per ambienti multi-cloud o con provider custom               |
| **Elastic Beanstalk**     | PaaS + IaC semplificato     | Per deployment rapidi senza gestire direttamente l’infrastruttura |

---

## 📊 Integrazioni e strumenti consigliati

- **CI/CD:** AWS CodePipeline, Jenkins, GitHub Actions, Bitbucket Pipelines
- **Gestione template:** AWS CloudFormation Designer, VS Code con estensione YAML + linter
- **Linting e validazione:** `cfn-lint`, `taskcat`, `cfn-guard`
- **Gestione parametrica:** Parameter Store, Secrets Manager, AWS KMS

---

## 📌 Best Practices

- Organizzare i template in moduli riutilizzabili
- Separare i template per ambiente o servizio (modularità)
- Utilizzare i **Change Set** per vedere l’impatto prima del deploy
- Evitare hardcoded values; preferire parametri, mapping e output
- Documentare i template con descrizioni chiare e commenti YAML
- Abilitare la **Drift Detection** periodicamente

---

AWS CloudFormation è lo strumento ideale per team DevOps e architetti cloud che vogliono standardizzare, automatizzare e versionare la loro infrastruttura AWS, riducendo errori manuali e aumentando la coerenza tra ambienti.
