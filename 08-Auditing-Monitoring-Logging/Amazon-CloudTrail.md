
--> [AWS](00-Intro/AWS.md)  -  [Auditing, Monitoring, Logging](08-Auditing-Monitoring-Logging/Auditing-Monitoring-Logging.md)
# AWS CloudTrail

**AWS CloudTrail** è un servizio completamente gestito che consente di registrare, monitorare e analizzare **eventi API** relativi alle attività degli utenti e dei servizi AWS.  Se registrate da CloudTrail, queste chiamate API possono aiutare, per esempio, a ricostruire quello che è successo.

CloudTrail uno strumento chiave per garantire **audit, sicurezza e conformità** nei workload AWS.

![trail example](trail-example.png)

---

## 🧩 Caratteristiche principali

- **Tracciamento delle chiamate API** su quasi tutti i servizi AWS
- **Log dettagliati** di chi ha fatto cosa, quando, da dove e con quali parametri
- **Conservazione automatica** dei log in S3
- **Integrazione con CloudWatch Logs, EventBridge, Athena**
- **Supporto per organizzazioni multi-account**
- **Log di gestione, dati e insight su attività sospette**

---

## 🚀 Come funziona

1. CloudTrail intercetta ogni chiamata API fatta tramite:
   - Console AWS
   - AWS CLI
   - SDK/API
2. I dati vengono registrati come eventi in formato JSON
3. Gli eventi possono essere:
   - Salvati in un bucket S3
   - Inviati in tempo reale a CloudWatch Logs
   - Analizzati con Athena o EventBridge

---

## 🔍 Esempio di evento registrato

```json
{
  "eventTime": "2024-05-27T10:15:00Z",
  "eventName": "RunInstances",
  "userIdentity": {
    "type": "IAMUser",
    "userName": "dev-user"
  },
  "sourceIPAddress": "192.0.2.1",
  "awsRegion": "eu-west-1",
  "requestParameters": { ... },
  "responseElements": { ... }
}
```

---

## 🛠️ Tipi di eventi

- **Management events**: creazione, modifica o cancellazione di risorse (es. `CreateBucket`, `StartInstances`)
- **Data events** *(opzionale)*: accessi a oggetti (es. `GetObject` su S3, `Invoke` su Lambda)
- **Insight events** *(opzionale)*: identificano attività insolite (es. accessi anomali, escalation di privilegi)

---

## 📦 Modalità di distribuzione

- **Trail singolo (regionale o globale)**
- **Organizational Trail**: per abilitare CloudTrail su tutti gli account di un'organizzazione AWS Organizations

---

## 🔐 Sicurezza

- I log sono scritti in un bucket S3 scelto dall’utente (meglio se con crittografia KMS)
- È possibile abilitare:
  - **Log file validation** (integrità SHA-256 + firma digitale)
  - **Access logging** al bucket S3
  - **Crittografia dei log** con **AWS KMS**

---

## 📈 Integrazioni utili

- **CloudWatch Logs**: per alert in tempo reale
- **Amazon Athena**: query SQL sui file di log (tramite tabella predefinita)
- **AWS EventBridge**: reagire a eventi specifici
- **AWS Security Hub**: centralizzare gli alert di sicurezza

---

## ✅ Best Practices

- **Attiva almeno un trail globale** che copra tutte le regioni
- **Conserva i log in S3 con lifecycle policy**
- **Abilita la validazione dei file di log**
- **Limita l'accesso al bucket S3 CloudTrail con [IAM](09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) policy restrittive**
- **Usa CloudTrail Insights per rilevare attività anomale**

---

## 📌 Conclusioni

AWS CloudTrail è uno strumento fondamentale per la **visibilità e l'audit delle operazioni nel cloud AWS**. È indispensabile per garantire conformità normativa, investigare problemi di sicurezza e mantenere il controllo sull'infrastruttura.

> “In AWS, se è successo, è stato registrato da CloudTrail.”
