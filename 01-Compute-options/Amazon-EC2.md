--> [AWS](AWS.md)  -  [Compute Options](AWS-Compute-Options.md)
# 🖥️ Amazon EC2 (Elastic Compute Cloud)

## 📘 Cos'è e come funziona

**Amazon EC2** è un servizio **IaaS (Infrastructure as a Service)** che consente di creare e gestire **istanze virtuali** nel cloud AWS. Fornisce **massima flessibilità** nella scelta di sistema operativo, configurazione hardware, storage, rete e criteri di sicurezza. EC2 permette agli utenti di controllare completamente l’ambiente, come se gestissero server fisici, ma con i vantaggi della scalabilità e automazione del cloud.

![Ec2](ec2.png)

Ci sono diverse tipologie di [storage da utilizzare insieme a EC2](EC2-Storage.md).

Ogni istanza EC2 è associata a una o più **Elastic Network Interface (ENI)**, ovvero schede di rete virtuali che permettono la comunicazione all'interno della [VPC](Amazon-VPC.md).
Un ENI contiene indirizzi IP (privati e opzionali pubblici), security group e una MAC address. 
Gli ENI possono essere usati per configurazioni avanzate di rete, come assegnare IP multipli, implementare failover o separare traffico applicativo su più interfacce.
A ogni istanza EC2 è assegnata una ENI primaria alla creazione, che non può essere modificata o mossa, mentre altre ENI secondarie possono essere staccate da un'istanza e essere attaccate a un'altra nella stessa subnet.

Un'**Amazon Machine Image (AMI)** contiene tutte le informazioni necessarie per avviare un'istanza, ovvero un **server virtuale nel cloud**. Quando lanci un'istanza, specifichi un'AMI da cui essa verrà creata. È possibile **avviare più istanze dalla stessa AMI** a seconda delle esigenze, oppure **utilizzare AMI diverse** per creare istanze con configurazioni differenti.


---

## ✨ Caratteristiche principali

- 📈 **Scalabilità**: possibilità di aumentare o ridurre rapidamente il numero di istanze in base al carico di lavoro
- 🔧 **Ampia gamma di istanze**: ottimizzate per calcolo, memoria, GPU, storage, burst e carichi misti
- 🔄 **Auto Scaling**: ridimensionamento automatico delle risorse in base alla domanda
- ⚖️ **Elastic Load Balancing ([ELB](Amazon-ELB.md))**: distribuisce automaticamente il traffico in entrata tra istanze EC2
- 📦 **AMI (Amazon Machine Images)**: immagini preconfigurate per lanciare rapidamente istanze con configurazioni note
- 🔐 **Sicurezza**: uso integrato di [VPC](Amazon-VPC.md), gruppi di sicurezza, ruoli [IAM](AWS-IAM.md) e chiavi SSH per la protezione dell’accesso e del traffico

![Autoscaling](EC2-autoscaling.png)

---
### 🧩 Tipi di istanze EC2

Amazon EC2 offre diversi tipi di istanze ottimizzate per specifiche esigenze di carico di lavoro:

- **General Purpose (es. t4g, m7i)**: bilanciano risorse di calcolo, memoria e rete. Ideali per applicazioni web, ambienti di sviluppo e database di piccole dimensioni.
- **Compute Optimized (es. c7g, c7i)**: offrono alte prestazioni di CPU, perfette per workload intensivi come server di gioco, high performance computing (HPC) e rendering.
- **Memory Optimized (es. r7g, x2idn)**: progettate per applicazioni che richiedono grande quantità di RAM, come database in-memory, analytics e cache.
- **Storage Optimized (es. i4i, im4gn)**: forniscono alta IOPS e bassa latenza su storage locale basato su SSD, adatte a database NoSQL, motori di ricerca e data warehouse.
- **Accelerated Computing (es. p5, inf2)**: dotate di GPU o acceleratori specializzati per machine learning, AI, elaborazione grafica o simulazioni scientifiche.

La scelta del tipo di istanza corretto consente di ottimizzare prestazioni e costi per ciascun carico di lavoro specifico.

---

## 🔒 Sicurezza

Amazon EC2 fornisce diversi strumenti per garantire sicurezza e isolamento:

- 🧱 **VPC (Virtual Private Cloud)** per l'isolamento di rete
- 🛡️ **Security Groups e Network ACLs** per controllare il traffico in entrata e uscita
- 🔑 **Chiavi SSH** per accesso sicuro alle istanze
- 🧑‍💼 **IAM Roles** per assegnare permessi granulari ai servizi in esecuzione sulle istanze
- 📜 **CloudTrail** per tracciare operazioni amministrative
- 🔐 **Crittografia** EBS e protezione del traffico con TLS per una maggiore sicurezza dei dati

---

## 🚀 Use case comuni

- 🌐 Hosting di applicazioni web scalabili
- 🧠 Backend per applicazioni enterprise complesse
- 🧮 Calcolo scientifico, finanziario o analitico ad alte prestazioni (HPC)
- 🧱 Esecuzione di software legacy con requisiti OS specifici o ambienti personalizzati

---

## 💰 Modelli di acquisto

- **On-Demand**  
  - Paghi per ogni ora o secondo di utilizzo, senza impegno  
  - Ideale per carichi variabili o sperimentazione

- **Reserved Instances (RI)**  
  - Impegno a 1 o 3 anni per ottenere uno sconto significativo  
  - Disponibili in tre varianti:
    - **Standard**: massimo sconto, nessuna flessibilità
    - **Convertible**: puoi cambiare tipo di istanza
    - **Scheduled**: prenotate per finestre temporali ricorrenti

- **Savings Plans** *(alternativa ai RI)*  
  - Impegno a livello di spesa oraria per ricevere sconti automatici su EC2, Fargate e Lambda  
  - Più flessibili e facili da gestire rispetto alle RI

- **Spot Instances**  
  - Capacità EC2 inutilizzata offerta a prezzo scontato fino al 90%  
  - Può essere interrotta da AWS con breve preavviso  
  - Perfette per carichi di lavoro flessibili, batch o test

- **Dedicated Hosts**  
  - Server fisico interamente dedicato a te  
  - Utile per conformità a requisiti di licensing (e.g., Bring Your Own Licencse - BYOL) o isolamento hardware

- **Dedicated Instances**  
  - Eseguite su hardware fisico dedicato, ma gestite da AWS  
  - Condividono l’hardware solo tra istanze dello stesso account

- **Capacity Reservations**  
  - Prenotazione di capacità in una zona di disponibilità specifica  
  - Garantisce la disponibilità, utile per ambienti mission-critical

- **EC2 Instance Fleets**  
  - Permette di combinare Spot, On-Demand e Reserved in un unico gruppo  
  - Ottimizza costi e disponibilità in base a vincoli definiti

- **Shared Tenancy (Default)**  
  - Istanze eseguite su hardware condiviso con altri clienti AWS  
  - Modalità predefinita per EC2, più economica e flessibile


---

## 🔁 Confronti e link utili

Per confrontare EC2 con altri servizi di container e orchestrazione AWS, vedi:

👉 [EC2vsECSvsEKS](EC2vsECSvsEKS.md)

---

## 📌 Conclusione

**Amazon EC2** è ideale per chi ha bisogno di **massimo controllo sull'infrastruttura virtuale**, desidera personalizzazione completa e vuole beneficiare della **scalabilità elastica del cloud**. È una soluzione versatile, adatta sia a workload persistenti che temporanei, legacy o moderni.

> “Con EC2, puoi costruire qualsiasi ambiente, dal server di test al cluster HPC distribuito — tutto con un click.”


