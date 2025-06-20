--> [AWS](00-Intro/AWS.md) 
# La Rete Globale di AWS

La **rete globale AWS** è una delle più estese e avanzate infrastrutture di rete private al mondo. Collega in modo sicuro e ad alte prestazioni tutte le **regioni AWS**, le **Availability Zones**, le **edge location** e i **data center** globali, offrendo **bassa latenza**, **alta disponibilità** e una **sicurezza end-to-end** per tutti i servizi AWS.

![Rete globale](global-infrastructure.png)

La rete globale è strutturata gerarchicamente in:

- **Regioni**: sono aree geografiche distinte, distribuite in tutto il mondo. Ogni regione contiene 3 o più Availability Zones (AZ) fisicamente separate ma vicine tra loro e collegate per garantire bassa latenza e alta disponibilità.
- **Availability Zones (AZ)**: consistono in uno o più data center distinti con alimentazione, rete e connettività ridondanti. Servono per distribuire carichi di lavoro in modo ad alta disponibilità e tolleranza ai guasti all'interno di una regione.
- **Local Zones**: sono estensioni di una regione AWS che posizionano servizi di calcolo, storage e database più vicino agli utenti finali in aree metropolitane per ridurre ulteriormente la latenza.
- **Edge Locations**: sono siti periferici distribuiti a livello globale utilizzati principalmente dai servizi di Content Delivery Network (CDN) come Amazon CloudFront, per fornire contenuti in modo rapido e sicuro agli utenti finali.


---

## 🌐 Caratteristiche principali

- **Backbone privato mondiale:** collegamenti in fibra ottica a capacità elevata tra regioni, zone di disponibilità ed edge location.
- **Alta disponibilità e tolleranza ai guasti:** progettata per garantire continuità operativa anche in caso di guasti di rete o disastri regionali.
- **Bassa latenza predicibile:** trasporto dei dati ottimizzato rispetto all'uso di Internet pubblico.
- **Sicurezza nativa:** crittografia del traffico, isolamento fisico delle reti, segmentazione del traffico, autenticazione e autorizzazione tramite [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md).

---

## 🚀 Servizi che sfruttano la rete globale AWS

### 📦 [Amazon CloudFront](03-CDN-e-Networking/Amazon-CloudFront.md) – CDN globale

- [Content Delivery Network](03-CDN-e-Networking/Content-Delivery-Networks.md) che distribuisce contenuti (HTML, CSS, media, API) tramite oltre 400 edge location in tutto il mondo.
- Sfrutta la rete AWS per fornire i contenuti dal nodo geograficamente più vicino all'utente finale.

### 🌍 [AWS Global Accelerator](03-CDN-e-Networking/AWS-Global-Accelerator.md)

- Ottimizza il traffico IP globale verso endpoint applicativi come [Amazon EC2](01-Compute-options/Amazon-EC2.md), [ALB](03-CDN-e-Networking/Amazon-ELB.md) (Application Load Balancer) e [NLB](03-CDN-e-Networking/Amazon-ELB.md) (Network Load Balancer)..
- Garantisce prestazioni costanti anche in caso di guasti o congestione tramite failover automatico e routing intelligente.

### 🧭 [Amazon Route 53](03-CDN-e-Networking/Amazon-Route-53.md)

- Servizio [Domain Name System (DNS)](03-CDN-e-Networking/Domain-Name-System.md)  altamente disponibile e scalabile.
- Utilizza la rete privata AWS per instradare il traffico verso le risorse con **minima latenza** e **failover geografico**.

### 🔌 [AWS Direct Connect](03-CDN-e-Networking/AWS-Direct-Connect.md)

- Connessione privata e dedicata tra ambienti on-premises e AWS, bypassando Internet.
- Migliora la **larghezza di banda**, la **sicurezza** e la **stabilità della rete**.

### 🔐 [AWS VPN](03-CDN-e-Networking/AWS-VPN.md)

- Crea connessioni sicure tra la rete on-premise e una [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md) attraverso tunnel IPsec.
- Dopo l’ingresso nella rete AWS, il traffico sfrutta il backbone globale.

### 🔁 [AWS Transit Gateway](03-CDN-e-Networking/AWS-Transit-Gateway.md) (con peering inter-regionale)

- Connette centinaia di [VPC](03-CDN-e-Networking/Amazon-VPC.md) e ambienti on-premises tra più regioni, utilizzando la rete AWS in modo **centralizzato** ed efficiente.

### 🚀 Amazon S3 Transfer Acceleration

- Aumenta la velocità di trasferimento verso i bucket [Amazon S3](02-Storage-services/Amazon-S3.md), soprattutto da località geografiche lontane.
- I dati viaggiano sulla rete globale AWS tramite edge location distribuite.

### 📡 [AWS Wavelength](03-CDN-e-Networking/AWS-Wavelength.md)

- Estende i servizi AWS all’interno delle reti 5G dei provider, riducendo drasticamente la latenza per applicazioni mobili e edge.
- Consente di eseguire carichi di lavoro direttamente nel bordo della rete, sfruttando l’integrazione con [Amazon EC2](01-Compute-options/Amazon-EC2.md), [VPC](03-CDN-e-Networking/Amazon-VPC.md) e altri servizi AWS.


---

## 💡 Vantaggi della rete AWS

- **Prestazioni prevedibili e stabili** a livello globale
- **Minor latenza** e miglioramento delle performance applicative
- **Sicurezza superiore** rispetto a Internet pubblico (isolation, monitoring, [AWS Shield](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Shield.md), [AWS WAF](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-WAF.md))
- **Riduzione dei costi di ritrasmissione** e perdita di pacchetti
- **Affidabilità integrata** in servizi come [Amazon RDS](04-Database-services/Amazon-RDS.md), [Elastic Load Balancing](03-CDN-e-Networking/Amazon-ELB.md), e [Elastic Disaster Recovery](02-Storage-services/Elastic-Disaster-Recovery.md)

---

## 🧱 Amazon VPC: il punto di partenza per la rete AWS

Tutte le risorse AWS che utilizzano la rete (come [Amazon EC2](01-Compute-options/Amazon-EC2.md), [RDS](04-Database-services/Amazon-RDS.md), [ECS](01-Compute-options/Amazon-ECS.md) o [EKS](01-Compute-options/Amazon-EKS.md)) vengono create all'interno di una **Amazon VPC** (Virtual Private Cloud).

Una [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md) consente di definire una rete virtuale isolata e personalizzabile nel cloud, con controllo completo su:

- Indirizzamento IP
- Subnet pubbliche/private
- Routing interno
- Configurazioni di sicurezza (NACL, Security Group)

> **Quando usarla**: ogni volta che si vogliono isolare ambienti, applicare segmentazione di rete, connettersi a data center on-premises, o creare architetture multi-tier sicure e scalabili.

Tutte le comunicazioni su Internet, tramite VPN o tra VPC in regioni diverse, **passano attraverso la rete globale AWS partendo dalla tua VPC**.

---

## 🔗 Considerazioni finali

La rete globale AWS è molto più di una semplice infrastruttura: è un **fattore abilitante** per architetture moderne, distribuite e resilienti. Consente ai clienti di raggiungere utenti finali con **minima latenza** e **massima affidabilità**, ottimizzando costi e prestazioni.

Per creare reti isolate, scalabili e configurabili all’interno della rete AWS, è possibile utilizzare il servizio [Amazon VPC](03-CDN-e-Networking/Amazon-VPC.md), che permette il provisioning completo di reti private virtuali.
