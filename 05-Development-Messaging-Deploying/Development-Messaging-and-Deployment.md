--> [AWS](00-Intro/AWS.md)
# AWS Development, Messaging, and Deployment Services and Technologies

## Introduzione

AWS offre un ecosistema completo di servizi per supportare lo **sviluppo software**, la **messaggistica tra sistemi** e il **deployment scalabile** di applicazioni. Questi strumenti consentono a sviluppatori e team DevOps di costruire, testare, distribuire e far comunicare i propri servizi cloud in modo rapido, sicuro ed efficiente.

---

## 🛠️ Development Services

Questi servizi aiutano gli sviluppatori a scrivere, testare, monitorare e gestire il ciclo di vita del software direttamente nel cloud.

### Principali servizi:

- **[AWS Cloud9](05-Development-Messaging-Deploying/AWS-Cloud9.md)**: IDE basato su browser per scrivere, eseguire e fare debug del codice.
- **[AWS CodeCommit](05-Development-Messaging-Deploying/AWS-CodeCommit.md)**: Servizio di controllo versione completamente gestito, compatibile con Git.
- **[AWS CodeBuild](05-Development-Messaging-Deploying/AWS-CodeBuild.md)**: Compila codice sorgente, esegue test e produce pacchetti pronti per il deployment.
- **[AWS CodeDeploy](05-Development-Messaging-Deploying/AWS-CodeDeploy.md)**: Automatizza il deployment di applicazioni su EC2, Lambda, o on-premise.
- **[AWS CodePipeline](05-Development-Messaging-Deploying/AWS-CodePipeline.md)**: Gestione del ciclo di rilascio con pipeline CI/CD completamente automatizzate.
- **AWS X-Ray**: Tracciamento e debugging delle applicazioni distribuite per identificare colli di bottiglia e errori.
- **AWS Fault Injection Simulator**: Strumento di chaos engineering per testare la resilienza delle applicazioni.
- **[AWS CodeArtifact](05-Development-Messaging-Deploying/AWS-CodeArtifact.md)**: Repository di pacchetti software completamente gestito.

---

## ✉️ Messaging Services

Questi servizi forniscono canali affidabili, asincroni e scalabili per lo scambio di messaggi tra componenti software, microservizi o sistemi distribuiti.

### Principali servizi:

- **[Amazon SQS](05-Development-Messaging-Deploying/Amazon-SQS.md)** (Simple Queue Service): Coda di messaggi completamente gestita per decoupling tra servizi.
- **[Amazon SNS](05-Development-Messaging-Deploying/Amazon-SNS.md)** (Simple Notification Service): Sistema di messaggistica publish/subscribe con notifiche push e email.
- **Amazon MQ**: Broker di messaggistica gestito compatibile con ActiveMQ e RabbitMQ.
- **[Amazon EventBridge](05-Development-Messaging-Deploying/Amazon-EventBridge.md)**: Bus di eventi per integrazione tra applicazioni SaaS, AWS e on-premise.
- **AWS AppSync**: API GraphQL serverless con supporto per real-time data updates.
- **[AWS Step Functions](05-Development-Messaging-Deploying/AWS-Step-Functions.md)**: Coordinazione di servizi tramite workflow visivi e stati.

---

## 🚀 Deployment & Orchestration Services

Questi strumenti aiutano a gestire e orchestrare il deployment delle applicazioni in ambienti cloud, garantendo scalabilità e disponibilità.

### Principali servizi:

- **[AWS Elastic Beanstalk](05-Development-Messaging-Deploying/AWS-Elastic-Beanstalk.md)**: Piattaforma PaaS per il deployment automatico di applicazioni web.
- **[AWS CloudFormation](05-Development-Messaging-Deploying/AWS-CloudFormation.md)**: Infrastructure as Code per la creazione di stack cloud tramite modelli YAML/JSON.
- **[AWS CodeDeploy](05-Development-Messaging-Deploying/AWS-CodeDeploy.md)**: Automatizza l'aggiornamento di applicazioni in modo sicuro e controllato.
- **[Amazon ECS](01-Compute-options/Amazon-ECS.md)** (Elastic Container Service): Orchestrazione di container Docker su scala.
- **[Amazon EKS](01-Compute-options/Amazon-EKS.md)** (Elastic Kubernetes Service): Servizio gestito per eseguire cluster Kubernetes.
- **[AWS Lambda](01-Compute-options/AWS-Lambda.md)**: Esecuzione di codice serverless in risposta a eventi senza provisioning di server.
- **AWS Amplify**: Toolkit completo per sviluppo, hosting e CI/CD di applicazioni web e mobile.

---

L'ampio ventaglio di servizi AWS per lo sviluppo, la messaggistica e il deployment permette di costruire pipeline CI/CD moderne, sistemi basati su eventi e architetture serverless. Utilizzando questi strumenti in modo sinergico, le organizzazioni possono accelerare l’innovazione e aumentare la resilienza delle proprie applicazioni cloud-native.



