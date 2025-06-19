--> [AWS](AWS.md)  -  [CDN e Networking](Rete-globale-AWS.md)
# AWS Direct Connect

**AWS Direct Connect** è un servizio che consente di stabilire una **connessione di rete dedicata** tra la propria infrastruttura on-premise e AWS. Questo collegamento può offrire prestazioni di rete più coerenti, **ridurre la latenza** e **abbattere i costi di trasferimento dati** rispetto a una connessione Internet tradizionale.

![Direct connect example](direct.png)

---

## Cos'è e come funziona

AWS Direct Connect permette di bypassare Internet pubblico creando un **collegamento fisico privato** tra l'infrastruttura dell'organizzazione e AWS. Questo avviene tramite una connessione in fibra ottica che collega il proprio data center a un **Direct Connect location**, dove è presente l’infrastruttura AWS.

Il traffico di rete può poi essere instradato:
- verso servizi pubblici AWS (es. [Amazon S3](Amazon-S3.md), [Amazon DynamoDB](Amazon-DynamoDB.md)),
- oppure verso VPC privati tramite [Amazon VPC](Amazon-VPC.md) o [AWS Transit Gateway](AWS-Transit-Gateway.md).

![Direct connect](direct-connect.png)

---

## Caratteristiche principali e vantaggi

- **Bassa latenza e prestazioni costanti**: la connessione dedicata garantisce minore variabilità e ritardi rispetto a Internet.
- **Alta banda**: fino a 100 Gbps, adatta a workload intensivi.
- **Riduzione dei costi di uscita**: il trasferimento dati verso AWS ha tariffe più basse rispetto al normale egress su Internet.
- **Maggiore sicurezza**: connessione privata, può essere combinata con **MACsec** per crittografia a livello 2.
- **Affidabilità migliorata**: meno soggetta a congestione, e integrabile con [AWS VPN](AWS-VPN.md) per resilienza.

---

## Componenti e architettura

| Componente         | Descrizione                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Connection**     | Collegamento fisico alla location Direct Connect.                           |
| **Virtual Interface (VIF)** | Interfacce virtuali per instradare traffico: Private VIF, Public VIF, Transit VIF. |
| **Router Cliente** | Apparato BGP lato on-premises per stabilire la connessione.                 |

### Tipi di Virtual Interface (VIF)

- **Private VIF**: per connettersi a una o più [VPC](Amazon-VPC.md).
- **Public VIF**: per raggiungere servizi pubblici AWS (es. S3, EC2 pubblici).
- **Transit VIF**: per accedere a più VPC tramite [AWS Transit Gateway](AWS-Transit-Gateway.md).

---

## Use cases

- **Migrazione dati** su larga scala e backup in tempo reale.
- **Disaster recovery** con replica cross-region e connessioni sempre attive.
- **Applicazioni sensibili alla latenza**, es. trading finanziario, real-time analytics.
- **Integrazione ibrida**: estensione sicura e performante della rete on-premise su AWS.
- **Accesso diretto** ai servizi pubblici AWS in modo sicuro e senza passare da Internet.

Per confrontarlo con AWS VPN: [AWS Direct-Connect VS AWS VPN](AWS-Direct-Connect-VS-AWS-VPN.md)

---

## Pricing

I costi sono calcolati su base:

- **Capacità della connessione**: 1, 10 o 100 Gbps.
- **Ore di utilizzo della porta**.
- **Dati trasferiti verso AWS**:
  - *Ingress (da on-premises a AWS)*: gratuito.
  - *Egress (da AWS a on-premises)*: tariffa ridotta rispetto all’Internet pubblico.

> La configurazione è gratuita, ma il provisioning di porte e il trasferimento dati sono soggetti a costi.

---

## Sicurezza

- Il traffico viaggia su una **linea dedicata**, isolata dal traffico pubblico.
- È possibile abilitare **MACsec** per crittografia livello 2 tra apparati.
- Si può usare in combinazione con [AWS VPN](AWS-VPN.md) per creare soluzioni di alta disponibilità.
- La sessione BGP con autenticazione protegge l'instradamento del traffico.
- Integrazione completa con [Amazon VPC](Amazon-VPC.md), [IAM](AWS-IAM.md), e [CloudWatch](Amazon-CloudWatch.md) per visibilità e controllo.

Aggiungere una connessione VPN sopra Direct Connect vuol dire **cifrare** anche il traffico che già passa nel canale fisico. In questo modo si garantisce crittografia end-to-end e si proteggono i dati da ccessi non autorizzati anche all'interno del collegamento fisico.

---

## Confronto con servizi simili in AWS

| Servizio           | Caratteristiche principali                                                |
|--------------------|----------------------------------------------------------------------------|
| **[AWS Direct Connect](AWS-Direct-Connect.md)** | Connessione fisica privata, alta larghezza di banda, latenza costante. |
| **[AWS VPN](AWS-VPN.md)**               | Connessione IPsec over Internet, più facile e veloce da configurare.         |
| **[Transit Gateway](AWS-Transit-Gateway.md)**   | Hub centralizzato per collegare più VPC e connessioni Direct Connect/VPN.    |

---

## Considerazioni finali

AWS Direct Connect è una soluzione ideale per le organizzazioni che richiedono una connessione **coerente, ad alte prestazioni e sicura** tra i propri ambienti locali e il cloud AWS. È particolarmente utile per **ambienti ibridi**, applicazioni mission-critical e scenari di **replica dati** ad alta velocità.
