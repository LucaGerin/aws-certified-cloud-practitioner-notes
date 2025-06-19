--> [AWS](AWS.md)  -  [CDN e Networking](Rete-globale-AWS.md)
# Amazon CloudFront

![cloudfront logo](cloudfront-logo.png)
**Amazon CloudFront** è il servizio di [[Content-Delivery-Networks]] offerto da AWS. Distribuisce contenuti web e applicativi con **bassa latenza** e **elevata velocità**, migliorando l’esperienza utente a livello globale.

Funziona salvando i file **in cache** in più data centers, chiamati **Edge Locations**. Quando uno User richiede qualcosa, questo gli è fornito dalla Edge Location più vicina che ne dispone.

## 🔍 Cos'è e come funziona

CloudFront distribuisce i contenuti da **edge location** geograficamente vicine all'utente finale, migliorando così le prestazioni e riducendo la latenza.  
Supporta oggetti statici (come file in [Amazon S3](Amazon-S3.md)) e contenuti dinamici, integrandosi con altri servizi AWS come [Amazon EC2](Amazon-EC2.md), [Elastic Load Balancing](Amazon-ELB.md), [Amazon Route 53](Amazon-Route-53.md) e [AWS Lambda](AWS-Lambda.md) tramite **Lambda@Edge**.

La rete è progettata per resilienza, throughput elevato e routing intelligente, sfruttando la [rete globale AWS](Rete-globale-AWS.md).

![cloudfront](cloudfront.jpg)

---

## ⚙️ Caratteristiche principali e vantaggi

- **Caching intelligente** dei contenuti in edge location.
- **Lambda@Edge** per logica personalizzata in prossimità dell’utente.
- **Supporto per HTTP/2, HTTP/3, TLS 1.3**.
- **Protezione DDoS automatica** inclusa tramite AWS Shield Standard.
- **Origin failover** per alta disponibilità automatica.
- **Controllo dell’accesso** tramite signed URL, signed cookie
- Restrizioni geografiche con **CloudFront Geo Restriction**.
- **Compressione automatica** per risparmio di banda.
- **Integrazione con WAF** per protezione applicativa.

---

## 💡 Use Cases

- Hosting di siti web statici o dinamici globali.
- Distribuzione veloce di contenuti video e media.
- API acceleration per applicazioni mobile e SPA.
- Download di software, giochi e aggiornamenti.
- Streaming video (live e on-demand).
- Mitigazione di attacchi e protezione da overload.

---

## 💰 Pricing

Il modello di pricing si basa su:

- **Data transfer out** (per GB), con prezzo variabile per area geografica.
- **Numero di richieste HTTP/HTTPS**.
- **Lambda@Edge** (tempo di esecuzione e invocazioni).
- **Invalidazioni oltre la soglia gratuita**.
- **Log delivery opzionale**.

> Incluso nel Free Tier: 1 TB di dati trasferiti + 1 milione di richieste HTTP/HTTPS al mese.

---

## 🔐 Sicurezza

- **TLS** con supporto fino a 1.3.
- **Certificati SSL/TLS** gestiti via [AWS Certificate Manager](AWS-Certificate-Manager.md).
- **Controllo accessi avanzato** (signed URL/cookie, geo-blocking).
- **Protezione automatica da attacchi** DDoS con [AWS Shield](AWS-Shield.md).
- **Integrazione diretta con [AWS WAF](AWS-WAF.md)** per difesa contro SQLi, XSS, ecc.
- Logging tramite CloudWatch e access log su [Amazon S3](Amazon-S3.md).

---

## 🔁 Confronto con servizi simili in AWS

| Servizio                                      | Scopo principale                             | Differenze con CloudFront                                       |
|-----------------------------------------------|-----------------------------------------------|------------------------------------------------------------------|
| [Amazon S3](Amazon-S3.md)                     | Object storage                                | CloudFront distribuisce i contenuti di S3 con caching e CDN      |
| [AWS Global Accelerator](AWS-Global-Accelerator.md) | Ottimizzazione del routing IP                 | Migliora il routing TCP/UDP ma non fa caching o distribuzione   |
| [Amazon Route 53](Amazon-Route-53.md)         | DNS ad alte prestazioni                       | Si occupa della risoluzione DNS, non della distribuzione contenuti |

---

## 🌐 Integrazione con la rete globale AWS

CloudFront si appoggia all'infrastruttura di [rete globale AWS](Rete-globale-AWS.md). per:

- Raggiungere utenti in bassa latenza ovunque nel mondo.
- Usare edge location come punti di ingresso locali.
- Ottimizzare il percorso dei pacchetti verso le origini configurate.

---

## ✅ Conclusione

Amazon CloudFront è la soluzione AWS ideale per distribuire contenuti su scala globale in modo **veloce, sicuro e scalabile**.  
Grazie alla **profonda integrazione con l’ecosistema AWS**, è un pilastro nelle architetture moderne ad alte prestazioni.