--> [AWS](AWS.md)  -  [Compute Options](AWS-Compute-Options.md)
## AWS Batch

**AWS Batch** è un servizio completamente gestito che consente di eseguire **lavori batch** su scala nel cloud AWS. 
Automatizza la gestione dell'infrastruttura necessaria per eseguire job in batch, comprese code, ambienti di calcolo, pianificazione e scalabilità, permettendo agli utenti di concentrarsi sull'elaborazione dei dati piuttosto che sulla gestione dei server.

---

### 📁 Cos'è e come funziona

AWS Batch consente di definire ed eseguire **job batch** (singoli compiti o insiemi di compiti) tramite:

- **Job definition**: specifica come eseguire un job (immagine Docker, vCPU, memoria, variabili d'ambiente).
    
- **Queue (coda)**: i job vengono inviati alla coda in attesa di essere eseguiti.
    
- **Compute environment**: specifica le risorse su cui eseguire i job (EC2 On-Demand, Spot o AWS Fargate).
    

AWS Batch gestisce lo **scheduling** dei job in base a priorità, dipendenze e risorse disponibili, e scala automaticamente l'infrastruttura necessaria.

Quando si utilizzano **Spot Instances** in AWS Batch per ridurre i costi, è importante considerare la possibilità di interruzioni. Per minimizzare l’impatto di tali interruzioni, è possibile implementare un meccanismo di **checkpointing** nei job: in questo modo, l'applicazione salva periodicamente il proprio stato e, in caso di interruzione della Spot Instance, può riprendere da dove si era fermata su una nuova istanza. Sebbene aumentare il prezzo d'offerta possa ridurre la probabilità di interruzioni, non le elimina del tutto e può comportare costi più elevati.

---

### ✅ Vantaggi

- **Completamente gestito**: non richiede provisioning manuale di server o cluster.
- **Scalabilità automatica**: aumenta o riduce dinamicamente le risorse compute.
- **Integrazione nativa con Docker**: esegue container con semplicità.
- **Supporto per EC2 e Fargate**: flessibilità nella scelta dell'infrastruttura.
- **Supporto per job dipendenti**: esecuzione sequenziale o parallela con dipendenze.
- **Costi ottimizzati**: compatibile con istanze Spot per risparmio economico.

---

### 🧠 Use cases

- **Elaborazione scientifica** e simulazioni numeriche.
- **Rendering video e immagini**.
- **Processamento di dati e log in batch**.
- **Preprocessing e training per Machine Learning**.
- **ETL (Extract, Transform, Load)** per data warehouse.

---

### 🔄 Confronto con altri servizi AWS

|Servizio AWS|Differenze principali|
|---|---|
|[AWS Lambda](AWS-Lambda.md)|Per job brevi ed eventi real-time. Timeout massimo di 15 minuti.|
|[Amazon ECS](Amazon-ECS.md) / [EKS](Amazon-EKS.md)|Richiedono gestione più manuale di cluster container.|
|[Step Functions](AWS-Step-Functions.md)|Orchestrazione di workflow. Può gestire job Batch ma non li esegue.|

---

### 🔒 Sicurezza

- **IAM roles** per controllare i permessi dei job.
    
- **Esecuzione in ambienti VPC isolati**.
    
- **Integrazione con Amazon CloudWatch** per log, metriche e allarmi.
    
- **Supporto per ECR privati** per la gestione sicura delle immagini container.
    

---

### 💸 Pricing

AWS Batch **non ha costi aggiuntivi**: si paga solo per le **risorse compute sottostanti**, in particolare:

- Istanze EC2 On-Demand o Spot (per secondi/minuti di utilizzo).
    
- Task Fargate (in base a vCPU e memoria).
    
- Storage e trasferimento dati se necessario (es. Amazon S3, EFS).
    

Utilizzando istanze Spot, è possibile ottenere un risparmio significativo rispetto alle istanze On-Demand.

---

Vuoi aggiungere un esempio pratico o una sezione sulla configurazione iniziale?