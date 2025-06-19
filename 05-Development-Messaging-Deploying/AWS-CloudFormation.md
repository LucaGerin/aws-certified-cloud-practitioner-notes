--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS CloudFormation

**AWS CloudFormation** è un servizio AWS che permette di **creare, aggiornare e gestire risorse AWS** in modo dichiarativo, attraverso file di configurazione YAML o JSON. È uno strumento chiave per l’implementazione dell’[Infrastructure as Code (IaC)](Infrastructure-as-Code.md) su AWS.

![use of cloud formation](cloudformation-cli.png)

---
## 🧩 Caratteristiche principali

- **Provisioning automatico** di risorse ([Amazon EC2](Amazon-EC2.md), [Amazon S3](Amazon-S3.md), [IAM](AWS-IAM.md), [Amazon RDS](Amazon RDS.md), [AWS Lambda](AWS-Lambda.md), ecc.)
- **File dichiarativi** in YAML o JSON che costruiscono le risorse come codice.
- **Gestione come stack**: risorse raggruppate e trattate come un’unità
- **Change set**: pre-visualizza modifiche prima del deployment
- **Supporto per macro e template annidati**
- **Drift detection**: identifica differenze tra template e infrastruttura reale

---

## 🚀 Come funziona

1. Scrivi un **template** in YAML o JSON che definisce l'infrastruttura e le risorse
2. Caricalo via Console, CLI o SDK
3. CloudFormation interpreta il template
4. CloudFormation effettua le API calls necessarie per creare le risorse definite
5. Lo stack è creato
6. Gestisci aggiornamenti, rollback e cambiamenti con sicurezza

![Cloud formation funzionamento](cloud-formation.png)

![Workflow](cloudformation-workflow.png)

---

## 🔧 Esempio semplice (YAML)

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Crea un bucket S3

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: mio-bucket-demo
      ...
```

---

## Benefici di usare CloudFormation

- L'infrastruttura creata è consistente perché il processo è automtizzato
- Veloce e efficiente per il tempo necessario
- Facile da usare

---

## 🛠️ Comandi utili (AWS CLI)

```bash
# Creare uno stack
aws cloudformation create-stack \
  --stack-name mio-stack \
  --template-body file://template.yaml

# Aggiornare lo stack
aws cloudformation update-stack \
  --stack-name mio-stack \
  --template-body file://template.yaml

# Eliminare lo stack
aws cloudformation delete-stack --stack-name mio-stack
```

---

## 🔐 Sicurezza e gestione

- Usa **IAM roles** per controllare le azioni eseguibili da CloudFormation
- I parametri e output possono essere criptati con [AWS KMS](AWS-KMS.md)
- Abilita **rollback on failure** per evitare stati inconsistenti

---

## ✅ Use case comuni

- Deploy automatico di ambienti dev/test/prod
- Provisioning di stack serverless ([AWS Lambda](AWS-Lambda.md))
- Gestione multi-account tramite StackSet
- Clonazione di ambienti per disaster recovery o testing

---

## ✅ Best Practices

- Usa YAML per leggibilità
- Versiona i template con Git
- Usa parametri e output per la modularità
- Testa con `change sets` prima dell’update
- Isola stack per ambienti diversi (es. dev, test, prod)

---

## 📌 Conclusioni

AWS CloudFormation è lo strumento IaC nativo per AWS, potente e flessibile. Automatizza la creazione e gestione di ambienti cloud, supporta l'integrazione con pipeline CI/CD, ed è essenziale per una governance solida e ripetibile.

> “Con CloudFormation, l’infrastruttura diventa un file — leggibile, revisionabile e riproducibile.”
