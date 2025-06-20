--> [AWS](00-Intro/AWS.md)  -  [Compute Options](01-Compute-options/AWS-Compute-Options.md)
# 🚢 AWS Fargate

![Fargate logo](fargate.webp)

## 📘 Cos'è e come funziona

**AWS Fargate** è un **motore di calcolo serverless per container**, integrato con **Amazon [ ECS](01-Compute-options/Amazon-ECS.md) ed [EKS](01-Compute-options/Amazon-EKS.md)**, che permette di eseguire container senza dover gestire direttamente l’infrastruttura sottostante (server o istanze EC2). AWS si occupa automaticamente del provisioning, del bilanciamento e della scalabilità delle risorse necessarie all’esecuzione dei task containerizzati.

![fargate functioning](fargate-functioning.png)

---

## ✨ Caratteristiche principali

- 🧩 **Serverless**: nessun provisioning o gestione manuale dei server  
- 🔗 **Integrazione nativa**: funziona con Amazon ECS e Amazon EKS  
- 📈 **Scalabilità automatica**: CPU e memoria assegnate dinamicamente per ogni task  
- 🔒 **Isolamento per task**: ogni task è isolato a livello di runtime per maggiore sicurezza  
- 💰 **Billing preciso**: si paga solo per le risorse effettivamente utilizzate (CPU e RAM)

---

## ✅ Vantaggi

- ✅ Riduzione dell'**overhead operativo**  
- ✅ **Maggiore sicurezza**, senza accesso diretto a istanze EC2  
- ✅ Integrazione facile con strumenti DevOps e pipeline CI/CD  
- ✅ Ideale per workload **imprevedibili o dinamici**  

---

## 🚀 Use case comuni

- ⚙️ Esecuzione di microservizi containerizzati  
- 📡 API serverless  
- 🔄 Elaborazione dati o stream temporanei  
- ⏱️ Workload on-demand o schedulati

---

## 🔒 Sicurezza

- 🔐 Ogni task è **isolato a livello di runtime** e non condivide risorse con altri
- 🧑‍💼 Supporta **IAM Task Role** per autorizzazioni granulari dei container
- 🌐 Compatibile con **VPC**, security group e subnet private per isolamento di rete
- ✅ Integrazione con **CloudWatch Logs**, **AWS Secrets Manager**, e **KMS** per audit, gestione segreti e crittografia
- 🛡️ Nessun accesso root alle istanze: superficie d’attacco ridotta

---

## 🔄 Differenze con ECS/EKS su EC2

| Caratteristica           | ECS/EKS su EC2              | ECS/EKS con Fargate       |
|--------------------------|-----------------------------|---------------------------|
| Gestione server          | Necessaria                  | Non necessaria            |
| Auto scaling             | Manuale/da configurare      | Automatico                |
| Provisioning risorse     | Manuale                     | Automatico                |
| Costi                    | Più complessi da prevedere  | Più semplici e trasparenti|

---

## 📌 Conclusione

**AWS Fargate** è la soluzione ideale per chi cerca la **semplicità del serverless** abbinata alla **potenza e portabilità dei container**. Elimina la complessità operativa della gestione dei nodi sottostanti, offrendo allo stesso tempo flessibilità, sicurezza e integrazione completa con l'ecosistema AWS.

> “Con Fargate, pensi solo al container. Al resto ci pensa AWS.”

