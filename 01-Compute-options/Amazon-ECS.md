--> [AWS](/00-Intro/AWS.md)  -  [Compute Options](/01-Compute-options/AWS-Compute-Options.md)
# 🧱 Amazon ECS (Elastic Container Service)

![ecs](ecs.png)
## 📘 Cos'è e come funziona

**Amazon ECS** è un servizio completamente gestito che consente di **eseguire e orchestrare container Docker** su scala nel cloud AWS. Supporta due modalità operative: su istanze **[Amazon EC2](/01-Compute-options/Amazon-EC2.md)**, gestite dall’utente, oppure in modalità **serverless tramite [AWS Fargate](/01-Compute-options/AWS-Fargate.md)**, dove è AWS a gestire le risorse sottostanti. ECS semplifica il deployment, la gestione e il monitoraggio dei container, offrendo una profonda integrazione con l’ecosistema AWS.

![Ecs funz](ecs-functioning.png)

---

## ✨ Caratteristiche principali

- 🛠️ **Gestione cluster semplificata**: ECS gestisce automaticamente il posizionamento e l'esecuzione dei container su cluster
- 🔌 **Integrazione con Fargate**: esecuzione serverless senza provisioning di server o istanze EC2
- 🔐 **IAM integrato**: controllo degli accessi granulari per servizi e task containerizzati
- ⚖️ **Load balancing & Service discovery**: integrazione nativa con **ALB/NLB** e supporto per scoperta automatica dei servizi
- 📊 **Monitoraggio & logging**: integrazione con **Amazon CloudWatch**, **X-Ray** per tracing, e **CloudTrail** per audit

---

## ⚙️ Modalità di esecuzione

- **ECS on EC2**  
  - I container vengono eseguiti su **istanze EC2** all'interno del cluster  
  - L'utente è responsabile della gestione e del provisioning delle istanze sottostanti

- **ECS on Fargate**  
  - Modalità **serverless**, dove AWS gestisce provisioning, scalabilità e infrastruttura  
  - Ideale per team che vogliono concentrarsi solo sul codice e sui container

---

## 🚀 Use case comuni

- 🧩 Microservizi containerizzati  
- 🧠 Backend di applicazioni scalabili e modulari  
- 🔁 Batch processing o pipeline di dati in container  
- 🔄 Continuous Integration / Continuous Deployment (CI/CD)

---

## 💰 Pricing

Il costo di ECS dipende dalla modalità di esecuzione:

- **ECS on EC2**: non ha costi aggiuntivi per il servizio ECS stesso, si pagano solo le **istanze EC2** e le risorse utilizzate ([EBS](/02-Storage-services/Amazon-EBS.md), bandwidth, ecc.)
- **ECS on Fargate**: si paga solo per **vCPU e RAM allocati per ogni task**, con fatturazione al secondo
- **Servizi integrati**: altri costi possono derivare da ALB/NLB, CloudWatch, log storage, ecc.

---

## ✅ Vantaggi

- ✅ Orchestrazione container **semplice e nativamente integrata in AWS**
- ✅ Maggiore **sicurezza e isolamento** grazie all’integrazione con IAM e VPC
- ✅ Riduzione dell’**overhead operativo** grazie a Fargate
- ✅ **Scalabilità automatica** e alta disponibilità
- ✅ Integrazione perfetta con servizi come **CodePipeline**, **Secrets Manager**, **CloudWatch** e **ECR**

---

## 🔁 Confronti e link utili

👉 Qui confronto tra [EC2vsECSvsEKS](/01-Compute-options/EC2vsECSvsEKS.md)

---

## 📌 Conclusione

**Amazon ECS** è una scelta eccellente per i team che desiderano **eseguire container in modo scalabile e gestito**, con il vantaggio della **flessibilità tra gestione manuale (EC2) e serverless (Fargate)**. È particolarmente indicato per chi cerca una **soluzione meno complessa di Kubernetes**, ma altamente performante e integrata con gli strumenti AWS.

> “Con ECS, puoi orchestrare microservizi in modo semplice e sicuro — con o senza server.”
