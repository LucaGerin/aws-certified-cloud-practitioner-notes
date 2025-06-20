--> [AWS](00-Intro/AWS.md)  -  [Development, Messaging, and Deployment](05-Development-Messaging-Deploying/Development-Messaging-and-Deployment.md)
# AWS CodeCommit

AWS CodeCommit è un servizio di controllo versione completamente gestito che consente di ospitare repository Git privati in modo sicuro e scalabile all'interno di AWS. 

È progettato per integrarsi perfettamente con altri strumenti DevOps come [AWS CodeBuild](05-Development-Messaging-Deploying/AWS-CodeBuild.md), [AWS CodeDeploy](05-Development-Messaging-Deploying/AWS-CodeDeploy.md) e [AWS CodePipeline](05-Development-Messaging-Deploying/AWS-CodePipeline.md).

![codecommit](codecommit.png)

---

## 🧩 Caratteristiche principali

- **Completamente gestito**: non serve gestire server Git.
- **Sicuro**: integrazione con [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) per controllo accessi granulare.
- **Scalabile**: supporta repository di qualsiasi dimensione.
- **Alta disponibilità**: ridondanza automatica su più zone di disponibilità.
- **Integrazione nativa** con [AWS CodePipeline](05-Development-Messaging-Deploying/AWS-CodePipeline.md), [Amazon CloudWatch](08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md), [AWS Lambda](01-Compute-options/AWS-Lambda.md), ecc.

---

## 🚀 Flusso di lavoro tipico

1. **Crea un repository** CodeCommit.
2. **Clona** il repository sul tuo computer locale.
3. **Esegui modifiche** e fai commit nel repository.
4. **Push** delle modifiche.
5. **Trigger automatici** tramite webhook, [AWS Lambda](01-Compute-options/AWS-Lambda.md) o pipeline CI/CD.

---

## 🔐 Sicurezza e permessi

- **IAM**: controllo dettagliato degli accessi (utente, ruolo, policy).
- **HTTPS o SSH**: per l’accesso al repository.
- **Trigger**: puoi eseguire azioni automatiche in risposta agli eventi (es. push, pull request).

---

## 💻 Esempi di comandi Git

```bash
git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/NomeRepo
git add .
git commit -m "Prima commit"
git push origin main
```

---

## 📝 Abilitare i trigger

Puoi configurare i **trigger** su eventi come:
- Push
- Pull request create/chiuse
- Merge completati

I trigger possono attivare [AWS Lambda](01-Compute-options/AWS-Lambda.md), [Amazon SNS](05-Development-Messaging-Deploying/Amazon-SNS.md), [Amazon SQS](05-Development-Messaging-Deploying/Amazon-SQS.md), ecc.

---

## ✅ Best Practices

- Usa branch per feature e pull request per collaborare in sicurezza.
- Automatizza i test con trigger su push.
- Proteggi i branch principali con policy [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md).
- Tieni sotto controllo i permessi e ruoli.

---

## 📌 Conclusioni

AWS CodeCommit è un'alternativa scalabile e sicura a GitHub o GitLab self-hosted, ideale per ambienti AWS-centrici. Consente un controllo totale dell’infrastruttura, mantenendo le funzionalità classiche di Git e aggiungendo la potenza dell’integrazione nativa AWS.
