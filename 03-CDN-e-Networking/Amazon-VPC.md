--> [AWS](00-Intro/AWS.md)  -  [CDN e Networking](03-CDN-e-Networking/Rete-globale-AWS.md)
# Amazon VPC (Virtual Private Cloud)

**Amazon VPC** è un servizio che consente di lanciare risorse AWS (come EC2, RDS, Lambda) all'interno di una **rete virtuale isolata**, configurabile in modo simile a una rete tradizionale on-premises.

![VPC](aws-vpc.png)

---

## Cos'è e come funziona

Con Amazon VPC puoi creare una rete virtuale isolata logicamente nel cloud AWS. Questa rete è simile a una rete tradizionale che potresti gestire nel tuo data center, ma con i vantaggi dell'infrastruttura scalabile di AWS. Puoi definire intervalli di indirizzi IP, creare subnet, configurare tabelle di routing e impostare gateway di rete.

---

## Caratteristiche principali e vantaggi

- **Isolamento di rete:** Ogni VPC è logicamente separata da tutte le altre, anche quelle di altri account.
- **Controllo degli indirizzi IP:** Puoi definire intervalli CIDR personalizzati per subnet pubbliche e private.
- **Routing personalizzato:** Possibilità di configurare tabelle di routing, gateway Internet, gateway NAT e route peer.
- **Sicurezza granulare:** Controlli dettagliati tramite Security Groups (SG) e Network ACL (NACL).
- **Alta disponibilità:** Supporto multi-AZ per ridondanza e tolleranza ai guasti.
- **Supporto IPv6:** Oltre al supporto IPv4, è possibile abilitare indirizzamento IPv6 per maggiore scalabilità.

Una **VPC è progettata per estendersi su più Availability Zones all'interno della stessa regione**.
> 📝 Esempio: puoi creare 3 subnet in una VPC, ognuna in una diversa AZ della regione **eu-west-1** (es. eu-west-1a, eu-west-1b, eu-west-1c).

Le **subnet in AWS devono essere interamente contenute in una singola Availability Zone (AZ)**. Non possono estendersi su più AZ.

Una **subnet è pubblica** se:
- Ha una **route verso un Internet Gateway (IGW)** nella sua route table.
- Le istanze in quella subnet possono **comunicare direttamente con Internet** (se hanno un IP pubblico o Elastic IP).

Una **subnet è privata** se:
- **Non ha una route diretta verso l’Internet Gateway.**
- Le risorse al suo interno **non sono accessibili direttamente da Internet**.
- Per accedere all'esterno (es. per aggiornamenti), si usa un **NAT Gateway** o un **NAT instance** situato in una subnet pubblica.

---

## Componenti chiave di una VPC

| Componente                        | Descrizione                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------- |
| **Subnet**                        | Segmenti logici di una VPC in una specifica Availability Zone                 |
| **Internet Gateway (IGW)**        | Consente la connessione da/verso Internet per subnet pubbliche                |
| **NAT Gateway**                   | Permette alle istanze in subnet private di accedere a Internet in uscita      |
| **Route Table**                   | Definisce le regole di routing tra subnet e verso gateway esterni             |
| **Security Group**                | Firewall a livello istanza o gruppo di istanze nella VPC, con regole stateful |
| **Network ACL**                   | Firewall stateless a livello subnet, con regole di ingresso e uscita          |
| **VPC Peering / Transit Gateway** | Connessione tra VPC nella stessa o in diverse regioni                         |
| **Endpoint VPC**                 | Accesso privato ai servizi AWS senza passare da Internet.                  |
| **VPN Gateway / Direct Connect** | Connessioni sicure tra la VPC e ambienti on-premises.                      |

![VPC Architecture](VPC-Architecture.jpeg)

NB: Dopo aver avviato un'istanza all'interno di una VPC, puoi modificare i **security groups** associati all'istanza. Puoi cambiare i security groups di un'istanza **solo quando l'istanza si trova nello stato _in esecuzione_ (running) o _arrestato_ (stopped)**.

Di default, AWS mette a disposizione 200 Network ACLs per gni VPC, che si estende sopra più AZ.
Ogni VPC supporta fino a 200 tabelle di routing.

---

## Use cases

- Creazione di ambienti isolati per sviluppo, test e produzione
- Segmentazione di rete tra livelli applicativi (web, app, DB)
- Accesso sicuro a servizi AWS e on-premises (tramite VPN o Direct Connect)
- Integrazione con servizi di sicurezza come AWS WAF e GuardDuty

---
## Pricing

- **VPC base:** gratuita.
- **NAT Gateway:** tariffato a ore e per GB di dati.
- **Indirizzi IP pubblici:** a pagamento.
- **VPC Peering:** si paga il traffico dati tra VPC.
- **IPAM avanzato:** a pagamento (la versione base è gratuita).

---

## Integrazione con altri servizi AWS

- **EC2:** Le istanze risiedono in subnet definite nella VPC
- **RDS:** I database possono essere isolati in subnet private
- **Elastic Load Balancing:** Distribuisce il traffico su istanze all’interno della VPC
- **Lambda:** Può essere connessa a VPC per accedere a risorse private

---

## Vantaggi

- Controllo totale sulla rete
- Personalizzazione di sicurezza, accessi e topologia
- Compatibilità con ambienti ibridi (VPN/Direct Connect)
- Supporto per architetture moderne e scalabili

Amazon VPC è il **fondamento della rete AWS**, essenziale per costruire ambienti cloud sicuri, scalabili e interconnessi.

Amazon VPC ti consente di creare una rete virtuale isolata all'interno di AWS, dove puoi:

- Definire **indirizzi IP privati**, subnet pubbliche/private
- Gestire routing, firewall, accessi VPN/Direct Connect
- Connettere e proteggere risorse come EC2, RDS, Lambda
- Segmentare la tua infrastruttura per ambienti (prod, test, dev)

La VPC è il punto di partenza per ogni progetto cloud orientato alla sicurezza, al controllo e alla configurazione personalizzata della rete.


## 🛡️ Sicurezza nelle AWS VPC

Le **Virtual Private Cloud (VPC)** offrono un controllo completo sull'ambiente di rete virtuale, inclusa la **sicurezza del traffico interno ed esterno**. 
All'interno di una VPC, il traffico tra istanze può essere **cifrato utilizzando TLS o IPsec** (è crittografato di default), specialmente quando coinvolge servizi come EC2, RDS o servizi cross-VPC tramite VPC Peering o Transit Gateway.

### 🔒 Strumenti di sicurezza nativi

- **Security Groups**: firewall virtuali **stateful** associati a istanze EC2 (instance level), che **controllano le connessioni in ingresso e in uscita** basate su porta, protocollo e IP.
- **Network ACLs (NACLs)**: liste di controllo degli accessi **stateless**, applicate **opzionalmente**, a livello di subnet (subnet level), che regolano in modo esplicito il traffico **in entrata e in uscita**.
- **VPC Flow Logs**: raccolgono informazioni sul traffico IP in entrata e uscita per analisi di sicurezza e auditing.
- **Routing personalizzato**: per isolare subnet e controllare il traffico verso Internet o servizi condivisi.

### 🧩 Altri strumenti di sicurezza integrabili

- **[AWS Network Firewall](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Network-Firewall.md)**: firewall gestito a livello di VPC per filtrare traffico stateless e stateful, con regole avanzate su IP, dominio, applicazioni, ecc.
- **[AWS WAF](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-WAF.md)**: protezione a livello applicativo (Layer 7), utile per filtrare richieste HTTP verso ALB, API Gateway e CloudFront.
- **[AWS Shield](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Shield.md)**: protezione contro attacchi DDoS.
- **AWS Route 53 Resolver DNS Firewall**: controllo sul traffico DNS in uscita per bloccare domini sospetti.
- **PrivateLink / Endpoint Gateway**: per accedere ai servizi AWS o privati **senza uscire su Internet**, mantenendo il traffico nella rete AWS.

> In una VPC ben protetta, ogni livello — dal flusso di rete fino all'accesso applicativo — è gestito con strumenti specifici per garantire **visibilità, isolamento e reazione proattiva** agli incidenti.

## Confronto con servizi simili in AWS

| Servizio                 | Descrizione                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Amazon VPC**           | Rete virtuale isolata e personalizzabile nel cloud.                         |
| **[AWS Transit Gateway](03-CDN-e-Networking/AWS-Transit-Gateway.md)**  | Hub centralizzato per la connessione di più VPC e ambienti on-prem.         |
| **AWS VPC Lattice**      | Connettività e gestione del traffico tra servizi su VPC e account multipli. |
| **AWS PrivateLink**      | Connessione privata ai servizi senza passare da Internet.                   |

---
## 🌐 Collegare più VPC in AWS

In AWS, è possibile collegare più **VPC (Virtual Private Cloud)** per consentire la comunicazione tra risorse distribuite in reti isolate. Esistono diversi metodi per farlo:

- **VPC Peering**: crea una connessione diretta tra due VPC, anche in account diversi, permettendo il routing del traffico tra di esse. È semplice da configurare ma non supporta il transito (i pacchetti non possono passare da una VPC a un'altra tramite una terza).
- **AWS Transit Gateway**: consente la connessione di più VPC e gateway on-premises nella stessa regione tramite un hub centralizzato. È scalabile e adatto a infrastrutture complesse con decine o centinaia di VPC. Non è però adatto a connessioni **dirette** tra VPC.
- **PrivateLink**: permette l'accesso sicuro a servizi AWS specifici tra VPC, senza esporre le reti attraverso IP pubblici o peering.
- **VPN o Direct Connect**: per collegare VPC con ambienti on-premises, utilizzando tunnel crittografati o connessioni dedicate.

La scelta del metodo dipende da fattori come la scalabilità, la sicurezza, la complessità della rete e i requisiti di transito del traffico.

---
### 🔌 Elastic Network Interface (ENI)

Un'**Elastic Network Interface (ENI)** è un componente virtuale di rete che rappresenta una **scheda di rete virtuale** all'interno di una Amazon VPC. 
Ogni ENI può essere associata a un'istanza [EC2](01-Compute-options/Amazon-EC2.md) e include attributi come **indirizzo IP privato, IP pubblico (opzionale), MAC address, security group** e sottorete. 

Puoi collegare più ENI a un'istanza EC2 (in base al tipo), associando più IP, permettendo scenari avanzati come **failover, gestione multilivello del traffico o network appliances, migliorare la redundancy**. 
Le ENI possono anche essere spostate tra istanze (tranne la ENI primaria di un'istanza), facilitando **alta disponibilità** e **ripristino rapido** in caso di guasti.


---
### 🔗 Interface VPC Endpoint

Un **Interface VPC Endpoint** consente di connettere privatamente la tua Amazon VPC a servizi AWS supportati (come S3, DynamoDB, SSM, ecc.) **tramite un'interfaccia di rete (ENI)**, senza passare per Internet o NAT Gateway. 
Viene creato come una **Elastic Network Interface (ENI)** in una subnet specifica, con un indirizzo IP privato e accesso diretto al servizio AWS. 

Questa configurazione migliora la **sicurezza, latenza e affidabilità**, e supporta anche **PrivateLink**, che consente di esporre servizi personalizzati ad altri account o VPC in modo sicuro e scalabile.

✅ *Ideale per: ambienti con requisiti di sicurezza elevati o senza accesso pubblico a Internet.*


---
Amazon VPC è il fondamento della rete AWS, essenziale per costruire ambienti cloud sicuri, scalabili e interconnessi. È il punto di partenza per ogni progetto cloud orientato alla sicurezza, al controllo e alla configurazione personalizzata della rete.