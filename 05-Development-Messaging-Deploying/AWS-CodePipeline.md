--> [AWS](/00-Intro/AWS.md)  -  [Development, Messaging, and Deployment](/05-Development-Messaging-Deploying/Development-Messaging-and-Deployment.md)
# AWS CodePipeline

![codepipeline](codepipeline.png)

AWS CodePipeline è un servizio di integrazione e distribuzione continua (CI/CD) completamente gestito che automatizza le fasi di build, test e deployment del codice ogni volta che viene effettuata una modifica. Permette di orchestrare flussi di lavoro DevOps con integrazione profonda nei servizi AWS e in strumenti di terze parti.

![Code pipeline funzionamento](code-pipeline.png)
---

## 🧩 Caratteristiche principali

- **Orchestrazione CI/CD**: coordina servizi come [AWS CodeCommit](/05-Development-Messaging-Deploying/AWS-CodeCommit.md), [AWS CodeBuild](/05-Development-Messaging-Deploying/AWS-CodeBuild.md), [AWS CodeDeploy](/05-Development-Messaging-Deploying/AWS-CodeDeploy.md).
- **Automazione end-to-end**: dal commit al deployment.
- **Integrazione estesa**: supporta GitHub, Jenkins, [Amazon S3](/02-Storage-services/Amazon-S3.md), [AWS CloudFormation](/05-Development-Messaging-Deploying/AWS-CloudFormation.md), ecc.
- **Event-driven**: pipeline attivate da commit o push.
- **Alta disponibilità**: servizio completamente gestito da AWS.

---

## 🔄 Fasi di una pipeline tipica

1. **Source**: recupera il codice sorgente (es. [AWS CodeCommit](/05-Development-Messaging-Deploying/AWS-CodeCommit.md), GitHub, [Amazon S3](/02-Storage-services/Amazon-S3.md)).
2. **Build**: esegue la compilazione (es. [AWS CodeBuild](/05-Development-Messaging-Deploying/AWS-CodeBuild.md), Jenkins).
3. **Test** *(opzionale)*: esegue test automatici.
4. **Approval** *(opzionale)*: attende approvazione manuale.
5. **Deploy**: distribuisce l'applicazione (es. [AWS CodeDeploy](/05-Development-Messaging-Deploying/AWS-CodeDeploy.md), [Amazon ECS](/01-Compute-options/Amazon-ECS.md), [AWS CloudFormation](/05-Development-Messaging-Deploying/AWS-CloudFormation.md)).

---

## 🖇️ Integrazioni supportate

- **Source**: [AWS CodeCommit](/05-Development-Messaging-Deploying/AWS-CodeCommit.md), GitHub, GitHub Enterprise, Bitbucket, [Amazon S3](/02-Storage-services/Amazon-S3.md)
- **Build**: [AWS CodeBuild](/05-Development-Messaging-Deploying/AWS-CodeBuild.md), Jenkins
- **Deploy**: [AWS CodeDeploy](/05-Development-Messaging-Deploying/AWS-CodeDeploy.md), [Amazon ECS](/01-Compute-options/Amazon-ECS.md), [AWS CloudFormation](/05-Development-Messaging-Deploying/AWS-CloudFormation.md)
- **Approval**: step manuali via console o API
- **Custom Actions**: [AWS Lambda](/01-Compute-options/AWS-Lambda.md) per estensioni personalizzate

---

## 📦 Esempio di pipeline CI/CD

```plaintext
CodeCommit ──▶ CodeBuild ──▶ CodeDeploy ──▶ Prod
```

![aws CodePipeline](aws-codepipeline.png)

---

## 📝 Esempio di definizione pipeline (CloudFormation)

```yaml
Resources:
  MyPipeline:
    Type: AWS::CodePipeline::Pipeline
    Properties:
      RoleArn: arn:aws:iam::123456789012:role/CodePipelineRole
      Stages:
        - Name: Source
          Actions:
            - Name: SourceAction
              ActionTypeId:
                Category: Source
                Owner: AWS
                Provider: CodeCommit
                Version: 1
              OutputArtifacts:
                - Name: SourceOutput
              Configuration:
                RepositoryName: MyRepo
                BranchName: main
        - Name: Build
          Actions:
            - Name: BuildAction
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: 1
              InputArtifacts:
                - Name: SourceOutput
              OutputArtifacts:
                - Name: BuildOutput
              Configuration:
                ProjectName: MyBuildProject
```

---

## 🔐 Sicurezza e IAM

- Definire un **ruolo IAM** per CodePipeline con permessi su:
  - [AWS CodeCommit](/05-Development-Messaging-Deploying/AWS-CodeCommit.md) / [Amazon S3](/02-Storage-services/Amazon-S3.md)
  - [AWS CodeBuild](/05-Development-Messaging-Deploying/AWS-CodeBuild.md)
  - [AWS CodeDeploy](/05-Development-Messaging-Deploying/AWS-CodeDeploy.md) / [Amazon ECS](/01-Compute-options/Amazon-ECS.md) / [AWS CloudFormation](/05-Development-Messaging-Deploying/AWS-CloudFormation.md)
  - [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) / [Amazon SNS](/05-Development-Messaging-Deploying/Amazon-SNS.md) per notifiche

---

## 🔔 Notifiche e monitoraggio

- **[Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) Events**: per notificare cambiamenti di stato della pipeline.
- **[Amazon SNS](/05-Development-Messaging-Deploying/Amazon-SNS.md)** o [AWS Lambda](/01-Compute-options/AWS-Lambda.md): per notifiche custom (es. fallimento build, approvazione).
- **CloudTrail**: tracciamento attività API.

---

## ✅ Best Practices

- Mantieni pipeline modulari (una per branch o ambiente).
- Usa approvazioni manuali per il deploy in produzione.
- Automatizza i test nella fase di build.
- Versiona i template [AWS CloudFormation](/05-Development-Messaging-Deploying/AWS-CloudFormation.md) per infrastruttura.
- Abilita notifiche per monitorare l'esecuzione.

---

## 📌 Conclusioni

AWS CodePipeline è lo strumento ideale per automatizzare l'intero ciclo di vita del software nel cloud AWS. Permette di integrare codice, testarlo, distribuirlo e monitorarlo con flussi ripetibili, controllati e automatizzati, garantendo qualità e velocità nei rilasci.
