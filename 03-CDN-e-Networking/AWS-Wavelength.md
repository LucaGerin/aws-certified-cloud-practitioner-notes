--> [AWS](00-Intro/AWS.md)  -  [CDN e Networking](03-CDN-e-Networking/Rete-globale-AWS.md)
# 📡 AWS Wavelength

## Cos'è e come funziona

**AWS Wavelength** è un servizio che estende i servizi di AWS fino al bordo (edge) delle reti 5G dei provider di telecomunicazioni, avvicinando la potenza del cloud alle applicazioni mobili che richiedono **latenza ultra-bassa**.

Wavelength permette di **eseguire carichi di lavoro direttamente all'interno della rete 5G**, eliminando la latenza dovuta al transito verso regioni AWS tradizionali. Gli sviluppatori possono distribuire istanze EC2, EBS, VPC, e altri servizi in zone Wavelength, come se fossero in una zona di disponibilità standard.

---

## Caratteristiche principali e vantaggi

- **Latenza inferiore a 10 millisecondi** per applicazioni mobili e IoT
- **Distribuzione geografica strategica** nelle reti 5G di partner come Verizon, Vodafone, SK Telecom, e KDDI
- **Integrazione nativa con servizi AWS** (IAM, CloudWatch, CloudFormation, ecc.)
- **Supporto per casi d’uso real-time** come AR/VR, veicoli autonomi, giochi multiplayer, telemedicina

---

## Use cases

- **Giochi in streaming ultra-reattivi**
- **Realtà aumentata e virtuale**
- **Video analytics in tempo reale**
- **Veicoli connessi e smart transportation**
- **Robotica e automazione industriale**

---

## Sicurezza

Wavelength eredita i meccanismi di sicurezza dell'infrastruttura AWS:
- Gestione degli accessi tramite **IAM**
- **Isolamento di rete** tramite Amazon VPC e security group
- **Crittografia dei dati** in transito e a riposo
- **Monitoraggio e logging** tramite CloudWatch e CloudTrail

---

## Pricing

Il modello di pricing per **AWS Wavelength** è simile a quello di **EC2 e EBS**:
- Si paga per le **istanze EC2** lanciate in una zona Wavelength
- Si paga lo **storage EBS** e il traffico dati in uscita
- Nessun costo aggiuntivo specifico per l'uso della zona Wavelength

---

## Confronto con tecnologie AWS simili

| Servizio | Differenza rispetto a Wavelength |
|----------|----------------------------------|
| **AWS Local Zones** | Local Zones estende AWS vicino a grandi città; Wavelength porta AWS all’interno delle reti 5G per latenza ancora più bassa. |
| **AWS Outposts** | Outposts porta l’infrastruttura AWS on-premises; Wavelength si integra invece direttamente con le reti mobile dei provider. |
| **AWS Edge Locations / CloudFront** | Le edge location distribuiscono contenuti, non eseguono carichi di lavoro generici come Wavelength. |

---

## Conclusione

**AWS Wavelength** è pensato per applicazioni che richiedono **latenza ultra-bassa e connettività mobile avanzata**, offrendo agli sviluppatori la possibilità di eseguire carichi di lavoro vicinissimi all’utente finale grazie all’integrazione diretta con le reti 5G dei provider partner. È una soluzione strategica per modernizzare esperienze mobili ed edge-critical.
