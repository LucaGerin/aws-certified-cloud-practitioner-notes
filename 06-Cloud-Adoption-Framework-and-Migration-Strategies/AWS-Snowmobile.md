--> [AWS](00-Intro/AWS.md)  -  [Migration Strategies](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Strategies.md)
# 🚛 AWS Snowmobile

**AWS Snowmobile** è un servizio di trasferimento dati su larga scala offerto da [AWS](00-Intro/AWS.md) per aiutare le organizzazioni a **migrare enormi quantità di dati (fino a 100 petabyte)** verso il cloud in modo sicuro, fisico e gestito. Utilizza un **camion attrezzato** con uno storage container sicuro, letteralmente trasportato nel tuo data center per caricare i dati offline.

![snowmobile](snowmobile.png)

---

## 🚛 Cos'è AWS Snowmobile?

- Un **rimorchio da 45 piedi (13 metri)** che funge da enorme dispositivo di archiviazione
- Progettato per trasferire **decine di petabyte in una sola volta**
- Viene spedito **fisicamente al data center del cliente**, dove i dati vengono copiati all'interno
- Una volta completato il caricamento, il camion ritorna ad [AWS](00-Intro/AWS.md) per caricare i dati su [Amazon-S3](02-Storage-services/Amazon-S3.md)

---

## 🧩 Caratteristiche principali

- Capacità di trasferimento: **fino a 100 PB per unità**
- **Crittografia a 256 bit** dei dati con chiavi gestite da [AWS-KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)
- **Sicurezza fisica** avanzata: container rinforzato, monitoraggio GPS, personale armato, protezioni anti-manomissione
- **Integrazione con [Amazon-S3](02-Storage-services/Amazon-S3.md)** per la migrazione dei dati

---

## 🛠️ Quando usarlo?

[AWS-Snowmobile](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Snowmobile.md) è ideale per aziende che hanno:

- **Exabyte di dati da migrare**, non trasferibili via rete in tempi ragionevoli
- Dati archiviati in **data center legacy** o su **storage tape**
- Requisiti di **conformità o sicurezza** che limitano la migrazione tramite internet
- Scadenze strette per lo **spegnimento di infrastrutture on-premises**

---

## ⏱️ Confronto con il trasferimento via rete

| Metodo             | Tempo per 1PB (con 1 Gbps) | Tempo con Snowmobile |
|--------------------|----------------------------|------------------------|
| Rete 1 Gbps        | ~3 mesi                    | Pochi giorni           |
| Snowmobile         | N/A                        | 1-2 settimane per 100PB|

> 💡 Snowmobile è **oltre 100 volte più veloce** del trasferimento via Internet in molti scenari reali.

---

## 🔐 Sicurezza

- **Crittografia**: dati cifrati a 256-bit
- **Chiavi [AWS-KMS](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-KMS.md)**: le chiavi possono essere gestite dal cliente
- **Controlli fisici**: personale di sicurezza, veicoli blindati, sorveglianza
- **Tracking in tempo reale** del camion

---

## 📦 Alternativa più piccola: AWS-Snowball

Se hai meno di 10 PB, considera [AWS-Snowball-Edge](06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Snowball-Edge.md):
- Snowball Edge: fino a 80 TB per dispositivo
