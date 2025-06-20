--> [AWS](/00-Intro/AWS.md)  -  [Auditing, Monitoring, Logging](/08-Auditing-Monitoring-Logging/Auditing-Monitoring-Logging.md)
# ⚙️ AWS Config

## 📘 Cos'è e come funziona

**AWS Config** è un servizio completamente gestito che consente di **monitorare, registrare e valutare le configurazioni** delle risorse AWS nel tempo. 
Il suo obiettivo principale è aiutare le organizzazioni a mantenere il controllo sulle modifiche infrastrutturali, garantire la **conformità** con policy interne o normative esterne (anche confrontandole in modo continuativo con modelli di standard e regolatori), e facilitare il **troubleshooting**.

AWS Config crea uno **storico dettagliato** delle configurazioni delle risorse, consentendo di rispondere facilmente a domande come:
- Qual era la configurazione di questa risorsa ieri?
- Chi ha modificato questa istanza e quando?
- Queste risorse rispettano i requisiti di sicurezza definiti?

Utilizza le raccomandazioni definite in precedenza per creare regole personalizzate da utilizzare nelle configurazioni. Identifica le risorse che non rispettano queste regole e crea allerte per gli amministratori per notificarglielo.
**NB:** Non sta imponendo queste regole, ma sta facendo audit riguardo a se sono rispettate o no.
->  AWS Config sfrutta regole predefinite o personalizzate per avvisare gli amministratori quando vengono rilevate risorse non conformi.

---

## ✨ Caratteristiche principali e vantaggi

- 📜 **Registrazione continua delle modifiche** su centinaia di tipi di risorse AWS
- 🔍 **Storico completo delle configurazioni**, consultabile nel tempo
- 📏 **Valutazione della conformità** tramite **regole predefinite o personalizzate**
- 🔁 **Notifiche automatiche** tramite Amazon SNS o EventBridge per ogni variazione rilevata
- 🏢 **Integrazione con AWS Organizations** per il monitoraggio multi-account
- 🔐 **Supporto a evidenze di audit** per framework di conformità (es. PCI-DSS, GDPR, HIPAA)

---

## 🚀 Use case comuni

- 🛡️ **Compliance e governance**: monitorare la conformità con regole aziendali o normative (es. “tutti i bucket S3 devono essere cifrati”)
- 🧠 **Troubleshooting avanzato**: capire quali modifiche hanno portato a un malfunzionamento
- 📝 **Audit e tracciabilità**: produrre evidenze di sicurezza e configurazione
- 🔄 **Change management**: analizzare l’impatto delle modifiche infrastrutturali nel tempo

---

## 🔧 Regole e valutazioni di conformità

AWS Config utilizza un **motore di regole** per verificare se le risorse sono conformi a determinati requisiti. Puoi usare:

- 🧩 **Regole gestite da AWS** (es. `s3-bucket-public-read-prohibited`)
- 🧑‍💻 **Regole personalizzate** usando AWS Lambda (per logiche più complesse)
- 📊 **Dashboard di conformità** per visualizzare lo stato attuale delle risorse

Le valutazioni possono essere **continue** o programmate, e i risultati vengono archiviati per ogni risorsa valutata.

---

## 💰 Pricing

Il prezzo di AWS Config si basa su:

- Numero di **risorse registrate** ($0.003 per risorsa per regione al mese)
- Numero di **valutazioni di conformità** ($0.001 per ogni valutazione)
- Eventuali **Snapshot** o **conservazione dati** in S3/Config Recorder

---

## 🧰 Integrazione con altri servizi

- 🔄 **AWS CloudTrail**: per collegare modifiche di configurazione con le chiamate API che le hanno causate
- 📦 **Amazon S3**: per archiviare gli snapshot di configurazione
- 🧠 **AWS Audit Manager**: per raccogliere evidenze di conformità automaticamente
- 🧩 **EventBridge**: per innescare azioni automatiche quando le risorse diventano non conformi

---

## 📌 Conclusioni

**AWS Config** è uno strumento essenziale per ogni architettura ben gestita su AWS, poiché fornisce visibilità, controllo e tracciabilità sulle risorse nel tempo. È particolarmente utile in ambienti regolamentati, infrastrutture complesse e progetti che richiedono auditability.

> “Con AWS Config, sai sempre **chi ha cambiato cosa, quando, e se è conforme** alle tue policy.”
