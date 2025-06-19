--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS CodeDeploy

AWS CodeDeploy è un servizio **completamente gestito** che automatizza il deployment di applicazioni su istanze [Amazon EC2](Amazon-EC2.md), server on-premise, [AWS Lambda](AWS-Lambda.md) e [Amazon ECS](Amazon-ECS.md). Consente rilasci controllati, rollback automatici e integrazione con CI/CD.

---

## 🧩 Caratteristiche principali

- **Supporto multi-target**: [EC2](Amazon-EC2.md), on-premise, [Lambda](AWS-Lambda.md), [ECS](Amazon-ECS.md).
- **Deployment automatizzato**: aggiornamenti senza interruzioni.
- **Rollback automatico** in caso di errore.
- **Controllo del traffico** durante il deploy (canary, linear, all-at-once).
- **Integrazione CI/CD** con [AWS CodePipeline](AWS-CodePipeline.md), GitHub, Jenkins, ecc.

---

## 🚀 Flusso di lavoro EC2/on-premise

1. App caricata in [Amazon S3](Amazon-S3.md) o GitHub.
2. Deployment avviato tramite CodeDeploy.
3. CodeDeploy esegue uno script definito in `appspec.yml`.
4. L'app viene aggiornata e monitorata.

![codedeploy](codedeploy.jpg)

---

## 🛠️ Flusso per Lambda

1. CodeDeploy crea una nuova versione della funzione [AWS Lambda](AWS-Lambda.md).
2. Distribuisce gradualmente il traffico.
3. Se tutto va bene → 100% traffico sulla nuova versione.
4. Se ci sono errori → rollback automatico.

---

## 📝 File appspec.yml (esempio EC2)

```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /home/ec2-user/app
hooks:
  BeforeInstall:
    - location: scripts/before_install.sh
      timeout: 180
  AfterInstall:
    - location: scripts/after_install.sh
  ApplicationStart:
    - location: scripts/start_server.sh
```

---

## 🔐 Permessi IAM

- Il ruolo di servizio deve poter accedere a:
  - [Amazon EC2](Amazon-EC2.md) (o Lambda/ECS)
  - [Amazon S3](Amazon-S3.md) (per leggere i pacchetti)
  - [Amazon CloudWatch](Amazon-CloudWatch.md) (per logging)
  - Auto Scaling (se usato con gruppi)

---

## 📦 Strategie di deployment

- **All-at-once**: tutto aggiornato insieme.
- **Rolling**: aggiornamenti a gruppi di istanze.
- **Canary**: piccolo gruppo test, poi rollout completo.
- **Linear**: aggiornamenti incrementali in percentuale.

---

## ✅ Best Practices

- Usa `appspec.yml` versione-controllato nel repository.
- Testa i tuoi script di deploy in un ambiente di staging.
- Monitora ogni deployment con [Amazon CloudWatch](Amazon-CloudWatch.md) e [Amazon SNS](Amazon-SNS.md).
- Usa [AWS CodePipeline](AWS-CodePipeline.md) per orchestrare l'intero ciclo CI/CD.

---

## 📌 Conclusioni

AWS CodeDeploy è uno strumento potente per distribuire applicazioni in modo controllato e affidabile. La sua flessibilità e integrazione con altri servizi AWS lo rendono una scelta eccellente per ambienti cloud-native e ibridi.
