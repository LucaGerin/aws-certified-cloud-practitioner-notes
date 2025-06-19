# AWS (Amazon Web Services)

## Che cos'è AWS?

Amazon Web Services (AWS) è una piattaforma di [Cloud](Cloud.md) computing fornita da Amazon. Offre un'ampia gamma di servizi on-demand tramite internet, come elaborazione, storage, database, machine learning, e strumenti di sviluppo.

![Logo AWS](aws.png)

AWS è una delle piattaforme più diffuse per costruire, distribuire e gestire applicazioni moderne in cloud.

AWS adotta il suo [Shared Responsibility Model](Shared-Responsibility-Model.md) per definire le responsabilità in temi di sicurezza e governance dell'utente e del cloud.

La progettazione utilizzando servizi AWS segue il [Well Architected Framework](Well-Architected-Framework.md).

---
## ☁️ I sei vantaggi del Cloud Computing

AWS identifica sei vantaggi fondamentali dell’utilizzo del **cloud computing** rispetto a un’infrastruttura tradizionale on-premise:

1. **Trade capital for variable expense** – Elimini i grandi investimenti iniziali (Capital Expenditure - CAPEX) in favore di un **modello a consumo** (Operational Exprenditure - OPEX), pagando solo ciò che usi.
2. **Benefit from massive economies of scale** – AWS aggrega milioni di clienti, consentendo di accedere a **prezzi più bassi** rispetto a quanto sarebbe possibile ottenere in autonomia.
3. **Stop guessing capacity** – Puoi **scalare automaticamente** (Scale on Demand Model) in base alla domanda reale, evitando sovraccarichi o sprechi.
4. **Increase speed and agility** – Con pochi clic puoi **provisionare risorse in minuti**, accelerando l’innovazione e i cicli di sviluppo.
5. **Stop spending money on running and maintaining data centers** – AWS si occupa della **gestione fisica dell’infrastruttura**, liberando tempo e risorse.
6. **Go global in minutes** – Puoi **distribuire workload in tutto il mondo** sfruttando la rete globale di regioni e zone di disponibilità AWS.

> Questi sei vantaggi aiutano le aziende a diventare più **agili, economiche e resilienti**, spostando il focus dalla gestione dell'infrastruttura all’innovazione.

---
## ☁️ Benefici della migrazione al cloud AWS

1. **Flexibility**  
   AWS consente di scegliere sistemi operativi, database e linguaggi di programmazione, permettendo di adattare l'ambiente alle esigenze specifiche delle applicazioni.

2. **Ease of Use**  
   La piattaforma AWS facilita l'hosting sicuro e rapido delle applicazioni, sia nuove che esistenti, attraverso strumenti come la AWS Management Console.

3. **Scalability**  
   Grazie a servizi come Elastic Load Balancing e Auto Scaling, le risorse possono essere adattate dinamicamente in base alla domanda, garantendo prestazioni ottimali.

4. **High Performance**  
   AWS offre un'infrastruttura globale affidabile che assicura un funzionamento efficiente delle applicazioni, migliorando l'allineamento tra utilizzo delle applicazioni e performance aziendali.

5. **Security**  
   Con un approccio end-to-end, AWS implementa misure di sicurezza fisiche e software per proteggere l'infrastruttura IT, garantendo la protezione dei dati aziendali.

6. **Cost-Effectiveness**  
   Il modello di pricing di AWS permette di pagare solo per le risorse effettivamente utilizzate, eliminando la necessità di investimenti in hardware e riducendo i costi operativi.

7. **Reliability**  
   L'infrastruttura di AWS è progettata per essere altamente disponibile e resiliente, assicurando la continuità operativa delle applicazioni.

8. **Elasticity and Agility**  
   Le risorse IT possono essere rapidamente adattate alle esigenze aziendali, evitando il sovraprovisioning e permettendo un'innovazione più rapida.

9. **Operational Resilience**  
   La migrazione ad AWS offre un ambiente IT più sicuro e meno soggetto a rischi, migliorando la resilienza delle operazioni aziendali.

10. **Data Storage**  
    AWS fornisce soluzioni di storage flessibili e scalabili, permettendo l'accesso ai dati da diversi dispositivi e località, con un modello di pagamento basato sull'utilizzo.

## Svantaggi

- Complessità iniziale.
- Costi non sempre facili da stimare.
- Dipendenza dal fornitore (vendor lock-in).

---
### 🌍 Struttura geografica di Amazon Web Services (AWS)

Amazon Web Services (AWS) è strutturato in una gerarchia geografica per garantire **scalabilità, affidabilità e bassa latenza**. 
Alla base ci sono le **regioni**, ognuna rappresentante un'area geografica distinta (es. `eu-west-1` per l'Irlanda). 
Ogni regione contiene almeno **tre o più Availability Zones (AZs)**, che sono **data center fisicamente separati** ma interconnessi a bassa latenza. 
Le **Local Zones** estendono le regioni principali per avvicinare risorse di calcolo e storage a grandi aree urbane, mentre le **[Wavelength](AWS-Wavelength.md) Zones** portano i servizi AWS ancora più vicino agli utenti finali attraverso le reti 5G degli operatori. 
Infine, le **Edge Locations** sono distribuite in tutto il mondo e usate principalmente da servizi come Amazon CloudFront (CDN) per fornire **contenuti in cache** con la minima latenza possibile.

![Availability Zones](availabilityzones.png)

I fattori da tenere in considerazione quando si sceglie una Regione includono:
- La vicinanza con i possibili clienti
- Il pricing
- I servizi che sono disponibili (o non lo sono) in una regione
- La compliance con regole di data governance e requisiti legali

### 🔒 Tipi di Availability e loro relazione con le zone

AWS offre diversi livelli di **availability** (disponibilità) per adattarsi a vari scenari di tolleranza ai guasti. 
Il concetto di availability in AWS si basa sulla **ridondanza geografica e la distribuzione intelligente** delle risorse.
Le **Availability Zones (AZs)** sono il livello chiave per costruire architetture ad alta disponibilità: distribuendo istanze o servizi su più AZ, un'applicazione può continuare a funzionare anche in caso di guasto in una zona specifica. 
I servizi che richiedono la **massima disponibilità**, come [Amazon RDS](Amazon-RDS.md) o [Elastic Load Balancing](Amazon-ELB.md), supportano la replica o il failover tra AZ. 
Alcuni servizi, come [S3](Amazon-S3.md) o [DynamoDB](Amazon-DynamoDB.md), sono **region-wide by design**, quindi replicano automaticamente i dati su più AZ all'interno della stessa regione. 
Le **Local Zones** possono essere usate per bassa latenza ma non offrono lo stesso livello di resilienza delle AZ, mentre le **Edge Locations** servono contenuti statici e non ospitano infrastruttura di calcolo resiliente. 


---
## 🚀 Servizi su AWS

### 🧠 Fondamentali
- 📦 [AWS Compute Options](AWS-Compute-Options.md)
- 💾 [AWS Storage Services](AWS-Storage-Services.md)
- 🌐 [Rete globale AWS](Rete-globale-AWS.md)
- 🛡️ [AmazonVPC](Amazon-VPC.md)
- 🗄️ [AWS Databases](AWS-Databases.md)

### 🧰 Sviluppo e Deployment
- 🛠️ [Development, Messaging, and Deployment Technology and Services](Development-Messaging-and-Deployment.md)

### 🚚 Migrazione e Adozione Cloud
- 📘 [Cloud Adoption Framework](Cloud-Adoption-Framework.md)  
- 🔁 [Migration Strategies](AWS-Migration-Strategies.md)

### 📊 Analisi e Intelligenza Artificiale
- 🤖 [Intelligenza Artificiale, Machine Learning e Analytics su AWS](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)

### 🔍 Monitoraggio e Sicurezza
- 📈 [Auditing, Monitoring e Logging](Auditing-Monitoring-Logging.md)
- 🔐 [Sicurezza, Compliance e Governance](Sicurezza-Compliance-Governance.md)

### 💰 Costi e Supporto
- 💳 [Prezzo, Fatturazione e Supporto in AWS](Prezzo-Fatturazione-Supporto.md)

---

## 🧩 Altri servizi o argomenti

- 💻 [AWS CloudShell](AWS-CloudShell.md)
- ☎️ [Amazon Connect](Amazon-Connect.md)
- 🖥️ [Amazon Workspaces](Amazon-Workspaces.md)
- 📺 [Amazon AppStream](Amazon-AppStream.md)
- 🔄 [Amazon AppSync](Amazon-AppSync.md)
- 🚀 [Amazon Amplify](AWS-Amplify.md)
- 📡 [Servizi della famiglia IoT](AWS-IoT-Family.md)
- 📱 [Device Farm](AWS-Device-Farm)
- 🌉 [API Gateway](Amazon-API-Gateway.md)
- 🧙 [Launch Wizard](AWS-Launch-Wizard.md)
- 🌟 [LightSail](AWS-LightSail.md)


## Certificazioni

AWS rende disponibili diverse certificazioni per gli esperti.
La certificazione base da cui partire prima di studiare per certificazioni di più alto livello è la [AWS Certified Cloud Practitioner (CLF C02)](AWS-Certified-Cloud-Practitioner-(CLF-C02).md)