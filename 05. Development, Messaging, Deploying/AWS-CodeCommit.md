--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS CodeCommit

AWS CodeCommit è un servizio di controllo versione completamente gestito che consente di ospitare repository Git privati in modo sicuro e scalabile all'interno di AWS. 

È progettato per integrarsi perfettamente con altri strumenti DevOps come [AWS CodeBuild](AWS-CodeBuild.md), [AWS CodeDeploy](AWS-CodeDeploy.md) e [AWS CodePipeline](AWS-CodePipeline.md).

![codecommit](codecommit.png)

---

## 🧩 Caratteristiche principali

- **Completamente gestito**: non serve gestire server Git.
- **Sicuro**: integrazione con [IAM](AWS-IAM.md) per controllo accessi granulare.
- **Scalabile**: supporta repository di qualsiasi dimensione.
- **Alta disponibilità**: ridondanza automatica su più zone di disponibilità.
- **Integrazione nativa** con [AWS CodePipeline](AWS-CodePipeline.md), [Amazon CloudWatch](Amazon-CloudWatch.md), [AWS Lambda](AWS-Lambda.md), ecc.

---

## 🚀 Flusso di lavoro tipico

1. **Crea un repository** CodeCommit.
2. **Clona** il repository sul tuo computer locale.
3. **Esegui modifiche** e fai commit nel repository.
4. **Push** delle modifiche.
5. **Trigger automatici** tramite webhook, [AWS Lambda](AWS-Lambda.md) o pipeline CI/CD.

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

I trigger possono attivare [AWS Lambda](AWS-Lambda.md), [Amazon SNS](Amazon-SNS.md), [Amazon SQS](Amazon-SQS.md), ecc.

---

## ✅ Best Practices

- Usa branch per feature e pull request per collaborare in sicurezza.
- Automatizza i test con trigger su push.
- Proteggi i branch principali con policy [IAM](AWS-IAM.md).
- Tieni sotto controllo i permessi e ruoli.

---

## 📌 Conclusioni

AWS CodeCommit è un'alternativa scalabile e sicura a GitHub o GitLab self-hosted, ideale per ambienti AWS-centrici. Consente un controllo totale dell’infrastruttura, mantenendo le funzionalità classiche di Git e aggiungendo la potenza dell’integrazione nativa AWS.
