--> [AWS](/00-Intro/AWS.md)  -  [CDN e Networking](/03-CDN-e-Networking/Rete-globale-AWS.md)
# 🌐 AWS Global Accelerator

**AWS Global Accelerator** è un servizio di rete che migliora la disponibilità, la performance e l'affidabilità delle applicazioni globali indirizzando il traffico utente attraverso la [rete globale AWS](/03-CDN-e-Networking/Rete-globale-AWS.md).  
Utilizza le **Edge Location** per trovare i percorsi ottimali attraverso i quali mandare i dati agli endpoint regionali.

NB: I file non sono salvati in cache.

AWS Global Accelerator è adatto soprattutto per applicazioni che non utilizzano HTTP/S, come VoIP, MTTQ e gaming, mentre per migliorare le prestazioni dei contenuti basati su HTTP, come applicazioni web dinamiche, immagini e video, la rete Amazon usa [Amazon CloudFront](/03-CDN-e-Networking/Amazon-CloudFront.md).

---

## ⚙️ Cos'è e come funziona

AWS Global Accelerator assegna **indirizzi IP statici globali** e utilizza l’infrastruttura globale AWS per ottimizzare il percorso del traffico in entrata, instradandolo automaticamente verso la **regione AWS più performante e disponibile**.

I pacchetti vengono deviati dalla rete pubblica e trasportati lungo il backbone AWS fino alla regione ideale, migliorando affidabilità, resilienza e latenza.

![Global Accelerator](global-accelerator.png)

---

## ✨ Caratteristiche principali e vantaggi

- **IP statici globali**: L'utente interagisce sempre con gli stessi IP, semplificando configurazioni DNS, firewall, e whitelist.
- **Instradamento intelligente**: Il traffico è diretto dinamicamente alla regione o all’endpoint più performante e vicino.
- **Failover automatico**: Se un endpoint diventa non disponibile, il traffico viene reindirizzato in tempo reale, senza interruzioni.
- **Riduzione della latenza**: Il traffico attraversa la rete AWS anziché Internet pubblico.
- **Supporto per vari endpoint**:
  - [Application Load Balancer](/03-CDN-e-Networking/Amazon-ELB.md)
  - [Network Load Balancer](/03-CDN-e-Networking/Amazon-ELB.md)
  - [Amazon EC2](/01-Compute-options/Amazon-EC2.md)
  - Elastic IP associati a EC2 o NLB
- **Monitoraggio integrato**: Compatibile con [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) per metriche e log.
- **Sicurezza e affidabilità**:
  - Protezione da DDoS integrata nella rete AWS
  - Routing resiliente basato su performance
  - Supporto per TLS end-to-end con i bilanciatori di carico

---

## 💼 Use cases

- Applicazioni globali con utenti distribuiti e sensibili alla latenza
- Ottimizzazione delle performance di API e backend worldwide
- Failover multi-regione e alta disponibilità
- Eventi ad alto traffico con accesso concorrente
- Integrazione in soluzioni di disaster recovery

---

## 💰 Pricing

Il prezzo di AWS Global Accelerator è composto da:

- **Costo fisso orario per acceleratore** attivo
- **Costo per gigabyte** di dati accelerati attraverso la rete AWS

Il pricing è generalmente più elevato rispetto a servizi regionali, ma giustificato dal miglioramento prestazionale e dalla resilienza globale.

---

## 🛡️ Sicurezza

- Utilizza la rete AWS con protezione DDoS integrata
- I dati viaggiano lungo un percorso privato e controllato
- Supporta TLS per la crittografia del traffico
- Completamente integrabile con [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), [WAF](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-WAF.md) e firewall esterni

---

## 🔁 Confronto con servizi simili in AWS

| Caratteristica                    | AWS Global Accelerator | [Amazon CloudFront](/03-CDN-e-Networking/Amazon-CloudFront.md)              |
|----------------------------------|------------------------------------------------------|--------------------------------------------------------|
| Livello OSI                      | Rete (TCP/UDP)                                       | Applicazione (HTTP/HTTPS)                             |
| Caching                          | ❌ No                                                 | ✅ Sì                                                  |
| Supporto IP statici              | ✅ Sì                                                 | ❌ No                                                  |
| Tipi di traffico                 | Qualsiasi TCP/UDP                                     | Solo HTTP/HTTPS                                       |
| Adatto per                      | API, ALB, NLB, EC2                                   | Contenuti statici e dinamici, file multimediali       |

---

## 🧭 Conclusione

AWS Global Accelerator è ideale per applicazioni distribuite globalmente che richiedono:

- **Routing intelligente e automatico**
- **Bassa latenza costante a livello mondiale**
- **Alta disponibilità e failover immediato**

Offre una **esperienza utente coerente**, riduce i tempi di risposta e protegge le applicazioni da guasti e congestione Internet. È una **componente fondamentale** per chi vuole performance di rete avanzate e globali nel cloud AWS.
