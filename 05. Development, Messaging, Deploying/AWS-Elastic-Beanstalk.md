--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS Elastic Beanstalk

**AWS Elastic Beanstalk** è un servizio PaaS ([Platform as a Service](Tipi-di-servizi-cloud.md)) che consente il **deployment automatico e la gestione di applicazioni** nel cloud AWS, senza dover configurare manualmente l’infrastruttura sottostante. È pensato per sviluppatori che vogliono concentrarsi sul codice, non sulla gestione di server, reti o load balancer.

![Beanstalk](bean.png)

---

## 🧩 Caratteristiche principali

- **Deployment semplificato** di applicazioni web, senza bisogno di configurare l'infrastruttura sottostante.
- **Supporta diversi linguaggi**: Java, .NET, PHP, Python, Ruby, Go, Node.js, Docker
- **Gestione automatica dell’infrastruttura**: [Amazon EC2](Amazon-EC2.md), [Elastic Load Balancing](Amazon-ELB.md), Auto Scaling, [Amazon RDS](Amazon-RDS.md), [Amazon S3](Amazon-S3.md)
- **Ambienti preconfigurati** con stack comuni
- **Aggiornamenti gestiti**, health check e rollback automatici
- **Monitoraggio integrato** con [Amazon CloudWatch](Amazon-CloudWatch.md)

Permette di far arrivare la propria piattaforma sul mercato velocemente, dispiegandola rapidamente e in maniera facile su AWS.

---

## 🚀 Come funziona

1. Scrivi il tuo codice
2. Comprimi il progetto in un archivio `.zip` (oppure usa Git)
3. Crea un'applicazione Elastic Beanstalk tramite Console, CLI o API
4. Elastic Beanstalk esegue il provisioning delle risorse e distribuisce il codice
5. Monitora, scala e aggiorna l'app con pochi click

![Bean example](bean-example.jpeg)

---

## 📦 Stack supportati

| Linguaggio       | Versioni Supportate             |
|------------------|---------------------------------|
| Node.js          | LTS, Amazon Linux 2             |
| Python           | 3.x su Amazon Linux 2           |
| Java             | 8, 11, 17                        |
| .NET             | Core e Framework (Windows)      |
| PHP              | 7.x, 8.x                         |
| Ruby             | 2.x, 3.x                         |
| Go               | Variabile, tramite Docker       |
| Docker           | Contenitori custom              |

---

## 🛠️ Esempio di deployment (con EB CLI)

```bash
# Inizializza il progetto
eb init -p node.js nome-app

# Crea ambiente di test
eb create nome-env

# Distribuisci l'app
eb deploy

# Controlla lo stato
eb status

# Apri nel browser
eb open
```

---

## 📈 Monitoraggio e gestione

- **Elastic Beanstalk Console**: dashboard visuale dell’ambiente
- **[Amazon CloudWatch](Amazon-CloudWatch.md) Logs**: per debug e analisi performance
- **Configurazione ambiente**: tramite `.ebextensions` o console
- **Health checks**: automatici e configurabili
- **Auto scaling**: automatico in base al carico

---

## 🔐 Sicurezza

- Supporto per **[Amazon VPC](Amazon-VPC.md)**, [IAM](AWS-IAM.md), SSL, Security Group
- Possibilità di usare [Amazon RDS](Amazon-RDS.md) e [Amazon S3](Amazon-S3.md) in ambienti isolati
- Crittografia dati a riposo e in transito
- Possibilità di accedere all'istanza [Amazon EC2](Amazon-EC2.md) per il debug

---

## ✅ Use case ideali

- Web application standard con stack conosciuto
- Deployment rapido di ambienti demo o staging
- Startup o team piccoli senza un DevOps dedicato
- Applicazioni containerizzate (via Docker)

ESEMPIO:
Elastic Beanstalk può essere utilizzato per distribuire rapidamente e facilmente un'applicazione web Java, incluso il provisioning delle istanze [Amazon EC2](Amazon-EC2.md) necessarie per eseguire l'applicazione, la configurazione di un [Elastic Load Balancer](Amazon-ELB.md) e persino l'installazione di Apache Tomcat. Infatti, Elastic Beanstalk supporta applicazioni che utilizzano le seguenti tecnologie: Java, .NET, PHP, Node.js, Python, Ruby, Go, Apache Tomcat, Docker e altre ancora.

---
## 📊 Elastic Beanstalk vs CloudFormation

**AWS Elastic Beanstalk** è una piattaforma PaaS che semplifica il deployment e la gestione di applicazioni web, gestendo automaticamente provisioning, bilanciamento del carico, scaling e monitoraggio. 
Al contrario, **AWS CloudFormation** è uno strumento IaC (Infrastructure as Code) che permette di definire in modo dichiarativo qualsiasi infrastruttura AWS, offrendo massima flessibilità ma richiedendo una maggiore conoscenza tecnica. 
In sintesi, Elastic Beanstalk è ideale per chi cerca automazione e semplicità, mentre CloudFormation è pensato per architetture complesse e completamente personalizzabili.


---

## ✅ Best Practices

- Versiona la tua configurazione con `.ebextensions`
- Usa ambienti separati per dev/test/prod
- Automatizza il deployment con [AWS CodePipeline](AWS-CodePipeline.md) o GitHub Actions
- Monitora l’health dell’ambiente regolarmente
- Effettua snapshot prima di aggiornamenti major

---

## 📌 Conclusioni

AWS Elastic Beanstalk è la scelta ideale per chi cerca un **servizio gestito che semplifichi il deployment di applicazioni web** su AWS. Offre la potenza dell’infrastruttura cloud combinata con la semplicità di una piattaforma PaaS, permettendo a team di ogni dimensione di lanciare rapidamente applicazioni scalabili e affidabili.

> “Con Beanstalk, il tuo codice incontra il cloud — senza stress da provisioning.”
