--> [AWS](/00-Intro/AWS.md)  -  [CDN e Networking](/03-CDN-e-Networking/Rete-globale-AWS.md)
# 🔐 AWS VPN

**AWS VPN (Virtual Private Network)** consente di stabilire **connessioni sicure** tra una rete on-premise o un client remoto e una [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md) tramite Internet.  
AWS offre due soluzioni principali:

- **AWS Site-to-Site VPN**
- **AWS Client VPN**

---

## ⚙️ Cos'è e come funziona

AWS VPN consente di stabilire tunnel VPN cifrati che attraversano Internet per connettere ambienti esterni (on-premise o client remoti) alla rete AWS.  
Permette di estendere in modo sicuro reti aziendali locali nel cloud, mantenendo la privacy e la sicurezza dei dati in transito.

![vpn](aws-vpn.png)

---

## ✨ Caratteristiche principali e vantaggi

- **Connessioni criptate** tramite protocolli IPsec o TLS
- **Alta disponibilità** grazie alla ridondanza dei tunnel Site-to-Site
- **Integrazione nativa con AWS IAM**, Directory Service, CloudWatch
- **Autenticazione flessibile** per Client VPN (certificati, SAML, AD)
- **Routing dinamico (BGP)** per configurazioni più flessibili
- **Split tunneling** supportato su Client VPN per ottimizzazione del traffico
- **Scalabilità** per piccoli team fino a grandi organizzazioni distribuite

---

## 🧱 Tipi di VPN

### 🔁 1. AWS Site-to-Site VPN

Permette di connettere una rete aziendale on-premise con una [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md) tramite un tunnel IPsec.

**Architettura:**

| Componente            | Descrizione                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Customer Gateway (CGW)** | Dispositivo fisico o software lato on-premise per stabilire la connessione |
| **Virtual Private Gateway (VGW)** | Gateway VPN gestito da AWS, associato alla [VPC](/03-CDN-e-Networking/Amazon-VPC.md)                  |
| **Tunnel VPN IPsec**  | Due tunnel ridondanti per alta disponibilità                                |

**Caratteristiche:**

- Routing statico o BGP dinamico
- Supporto per [AWS Transit Gateway](/03-CDN-e-Networking/AWS-Transit-Gateway.md)
- IPsec Fase 1 e Fase 2 configurabili

---

### 👤 2. AWS Client VPN

Servizio gestito che consente a **utenti remoti** di accedere in modo sicuro a risorse AWS tramite connessione OpenVPN.

**Caratteristiche:**

- Supporta autenticazione tramite:
  - AWS Directory Service
  - Certificati client
  - Federazione SAML
- Supporto per split-tunneling
- Scalabilità automatica e alta disponibilità
- Controllo granulari con IAM e Security Groups


![vpn confronto](vpn.png)

---

## 💼 Use cases

- Connessione sicura tra ambienti on-premise e [Amazon VPC](/03-CDN-e-Networking/Amazon-VPC.md)
- Accesso remoto degli utenti a sistemi aziendali su AWS
- Supporto per architetture ibride
- Soluzioni di disaster recovery e replica tra ambienti distribuiti

Per un confronto approfondito tra VPN e altre opzioni di connessione, vedi: [AWS Direct Connect vs AWS VPN](/03-CDN-e-Networking/AWS-Direct-Connect-VS-AWS-VPN.md)

---

## 🛠️ Flusso di configurazione (Site-to-Site VPN)

1. Creare un **Customer Gateway** in AWS
2. Creare un **Virtual Private Gateway** e associarlo alla [VPC](/03-CDN-e-Networking/Amazon-VPC.md)
3. Creare una **VPN Connection**
4. Configurare il router/firewall on-premise con parametri IPsec
5. Monitorare i tunnel e verificare la connettività

---

## 💰 Pricing

I costi di AWS VPN includono:

- **Costo orario** per ogni connessione VPN attiva
- **Costo per traffico dati outbound** (i dati in ingresso sono gratuiti)

Client VPN ha un pricing separato, basato su:

- Numero di endpoint associati
- Ore di connessione attiva

---

## 🛡️ Sicurezza

- Tunnel VPN **cifrati** con IPsec (Site-to-Site) o TLS/OpenVPN (Client VPN)
- Integrazione con **[IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)** per controllo accessi utente
- **Monitoraggio con CloudWatch** dei tunnel e delle connessioni
- **Log di connessione e diagnostica** per auditing e compliance
- Supporto per autenticazione multi-fattore e sistemi aziendali

---

## 🔁 Confronto con altri servizi simili in AWS

| Caratteristica           | AWS Site-to-Site VPN | AWS Client VPN         | [AWS Direct Connect](/03-CDN-e-Networking/AWS-Direct-Connect.md) |
|--------------------------|----------------------|-------------------------|---------------------------------------------|
| Tipo di connessione      | Rete aziendale       | Utente individuale      | Connessione fisica                          |
| Latenza                  | Variabile (Internet) | Variabile (Internet)    | Bassa e stabile                             |
| Crittografia             | ✅ IPsec              | ✅ TLS/OpenVPN           | ✅ (opzionale con MACsec)                   |
| Costo di setup           | Basso                 | Basso                   | Alto (infrastruttura dedicata)             |
| Resilienza               | Alta (tunnel doppi)   | Alta (scalabilità auto) | Alta (dedicata)                            |

---

## 📌 Conclusione

AWS VPN è una soluzione **sicura, flessibile e facile da implementare** per estendere reti on-premise o abilitare l’accesso remoto alle risorse AWS.  
Supporta sia esigenze aziendali distribuite che accessi individuali, adattandosi a diversi modelli di connettività ibrida e remota.
