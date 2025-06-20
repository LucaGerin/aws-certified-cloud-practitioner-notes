--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🧾 AWS License Manager

## Cos'è e come funziona

**AWS License Manager** è un servizio che consente alle organizzazioni di gestire in modo centralizzato le licenze software, sia per prodotti acquistati tramite AWS Marketplace che per software on-premises o di terze parti (BYOL – Bring Your Own License).

Con License Manager, puoi definire regole per l’utilizzo delle licenze, monitorare la conformità e prevenire l’uso eccessivo o non autorizzato. Il servizio si integra nativamente con AWS e con strumenti di virtualizzazione comuni come Amazon EC2 e AWS Systems Manager.

![License manager](license-manager.png)

### Funzionalità principali:
- Definizione di regole di utilizzo (numero massimo di istanze, tipo di licenza, regione, etc.)
- Monitoraggio automatico delle istanze che utilizzano licenze
- Blocco preventivo di utilizzi non conformi
- Reporting e auditing continuo

---

## Caratteristiche principali e vantaggi

- **Conformità automatizzata**: riduce il rischio di non conformità con le licenze software.
- **Centralizzazione**: gestione da un'unica console di tutte le licenze, anche in ambienti multi-account tramite AWS Organizations.
- **Prevenzione degli abusi**: le regole possono bloccare l’avvio di istanze non conformi.
- **Visibilità completa**: report dettagliati sull’utilizzo attuale delle licenze e sulle violazioni.
- **Integrazione con AWS Marketplace**: semplifica la gestione delle licenze acquistate direttamente dal Marketplace.

---

## Sicurezza

AWS License Manager utilizza **IAM** per controllare l'accesso alle operazioni e consente la configurazione di **policy granulari**. Inoltre, si integra con **AWS CloudTrail** per fornire audit trail completi su tutte le operazioni legate alle licenze.

Le regole di licenza definite possono essere enforce e propagate automaticamente tra gli account collegati, garantendo una gestione coerente e sicura.

---

## Pricing

**AWS License Manager è gratuito**. Non ci sono costi aggiuntivi per l’uso del servizio.

Tuttavia, eventuali **costi derivanti dalle licenze software** (ad esempio Microsoft, Oracle, SAP) restano a carico del cliente e sono soggetti ai termini del fornitore.

---

## Confronto con tecnologie AWS simili

| Servizio | Differenza rispetto a License Manager |
|----------|----------------------------------------|
| **AWS Service Catalog** | Aiuta a distribuire stack pre-approvati, ma non gestisce direttamente le licenze. |
| **AWS Systems Manager Inventory** | Raccoglie dati sulle istanze, ma non impone o monitora le regole di licenza. |
| **AWS Organizations** | Gestisce la struttura multi-account; License Manager si integra con essa per estendere le policy di licenza. |
| **AWS Config** | Permette auditing delle configurazioni, ma non gestisce regole specifiche per licenze software. |

---

## Conclusione

**AWS License Manager** è uno strumento essenziale per aziende che vogliono **mantenere il controllo e la conformità** nell’uso di software su AWS, riducendo i rischi legali e ottimizzando l'utilizzo delle licenze. Grazie all’integrazione con altri servizi AWS, si adatta facilmente a infrastrutture distribuite e multi-account.
