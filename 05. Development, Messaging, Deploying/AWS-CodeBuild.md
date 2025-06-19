--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS CodeBuild

AWS CodeBuild è un servizio di integrazione continua **completamente gestito** che compila codice sorgente, esegue test e produce pacchetti software pronti per il deployment. È parte della suite di strumenti DevOps di AWS ed è pensato per funzionare in modo integrato con [AWS CodeCommit](AWS-CodeCommit.md), [AWS CodeDeploy](AWS-CodeDeploy.md), [AWS CodePipeline](AWS-CodePipeline.md) e altri servizi AWS.

---

## 🧩 Caratteristiche principali

- **Senza server**: non è necessario gestire alcuna infrastruttura.
- **Scalabilità automatica**: gestisce automaticamente più build in parallelo.
- **Supporto per ambienti personalizzati**: puoi usare immagini Docker personalizzate.
- **Fatturazione al secondo**: paghi solo per il tempo di esecuzione della build.
- **Integrazione con altri strumenti DevOps AWS**: CodeCommit, CodePipeline, CodeDeploy ecc.

---

## 🛠️ Flusso di lavoro tipico

1. **Commit del codice** nel repository (es. CodeCommit, GitHub).
2. **Trigger della build** tramite CodePipeline o webhook.
3. **Esecuzione di CodeBuild** con file `buildspec.yml`.
4. **Output**: artefatti di build (ZIP, JAR, Docker image, ecc.) caricati in [S3](Amazon-S3.md) o Elastic Container Registru (ECR).
5. **Deploy automatico** tramite [CodeDeploy](AWS-CodeDeploy.md), [ECS](Amazon-ECS.md), ecc.

![CodeBuild](codebuild.png)

---

## 📝 File buildspec.yml

Un file `buildspec.yml` definisce le fasi della build. Esempio:

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      java: corretto17
  build:
    commands:
      - echo "Compilo il progetto..."
      - mvn clean install
artifacts:
  files:
    - target/*.jar
```

---

## 🔐 Permessi IAM

Il ruolo di servizio di CodeBuild deve avere i permessi per accedere a:
- S3 (per leggere/scrivere artefatti)
- CodeCommit / GitHub (per scaricare il codice)
- [Amazon CloudWatch](Amazon-CloudWatch.md) Logs (per scrivere log)
- Altri servizi usati durante la build (es. ECR, Parameter Store)

---

## 📦 Esempio di utilizzo con CodePipeline

```plaintext
CodeCommit ──▶ CodePipeline ──▶ CodeBuild ──▶ Deploy
```

---

## ✅ Best Practices

- Versiona il file `buildspec.yml` nel repository.
- Usa parametri sicuri con [AWS Secrets Manager](AWS-Secrets-Manager.md).
- Abilita la crittografia degli artefatti.
- Monitora le build con [Amazon CloudWatch](Amazon-CloudWatch.md) Logs.

---

## 📌 Conclusioni

AWS CodeBuild è uno strumento potente per automatizzare il processo di build in un ambiente AWS-native. Grazie alla sua scalabilità, semplicità d’uso e integrazione con altri servizi, è un'ottima scelta per progetti cloud-native e pipeline CI/CD moderne.
