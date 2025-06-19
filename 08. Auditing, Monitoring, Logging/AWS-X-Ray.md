--> [AWS](AWS.md)  -  [Auditing, Monitoring, Logging](Auditing-Monitoring-Logging.md)
# AWS X-Ray

**AWS X-Ray** è un servizio di **tracing distribuito** che consente di analizzare e visualizzare il comportamento delle applicazioni distribuite, aiutando gli sviluppatori a identificare colli di bottiglia, errori e problemi di performance.

---

## 🧩 Caratteristiche principali

- **Tracing end-to-end** delle richieste attraverso più servizi AWS e microservizi
- **Raccolta di segmenti e subsegmenti** per identificare errori e latenze
- **Visualizzazione grafica del flusso delle chiamate**
- Supporto per applicazioni serverless, containerizzate, e su EC2
- Integrazione con servizi AWS come **API Gateway, Lambda, ECS, EC2, Elastic Beanstalk**
- **Annotazioni e metadati personalizzati** per analisi avanzate

---

## 🚀 Come funziona

1. Una richiesta utente attraversa vari componenti dell'applicazione (es. API Gateway → Lambda → DynamoDB).
2. Ogni componente strumentato genera **segmenti** o **subsegmenti** che descrivono il lavoro svolto.
3. I dati vengono raccolti e inviati a X-Ray.
4. X-Ray **ricostruisce il percorso della richiesta** e lo visualizza graficamente con dettagli su latenza, errori, retry, eccezioni, ecc.

---

## 🛠️ Componenti principali

- **Segment**: rappresenta una singola richiesta elaborata da un servizio (es. una funzione Lambda)
- **Subsegment**: dettaglio di operazioni interne (es. una query su DynamoDB)
- **Trace**: l’insieme completo dei segmenti per una singola richiesta
- **Sampling**: per controllare quali richieste vengono tracciate (default: 1 al secondo + 5% extra)

---

## 📦 Integrazione con altri servizi AWS

| Servizio         | Integrazione supportata    |
|------------------|----------------------------|
| **Lambda**       | Integrato automaticamente  |
| **API Gateway**  | Basta attivare il tracing  |
| **ECS / EC2**    | Richiede X-Ray daemon      |
| **Elastic Beanstalk** | Supportato con configurazione automatica |

---

## 📋 Esempio di codice (Python – Boto3 + SDK)

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

@xray_recorder.capture('processa-dati')
def handler(event, context):
    # codice dell’applicazione
    xray_recorder.put_annotation("utente", "MarioRossi")
    return {"statusCode": 200, "body": "OK"}
```

---

## 📈 Monitoraggio e analisi

- Visualizzazione grafica dei trace nella console X-Ray
- Filtri per:
  - Latenza alta
  - Errori
  - Cold start
  - Anomalie su specifici servizi
- Integrazione con **CloudWatch** e **CloudTrail**

---

## 🔐 Sicurezza

- [IAM](AWS-IAM.md) roles per concedere accesso a X-Ray (es. `AWSXRayDaemonWriteAccess`)
- Crittografia in transito e a riposo
- Supporto per redazione di dati sensibili

---

## ✅ Best Practices

- Usa X-Ray per tracciare le richieste tra servizi
- Abilita sampling per ridurre costi e dati inutili
- Inserisci annotazioni per filtrare e analizzare i trace
- Configura dashboard con CloudWatch per allarmi su latenza/errori
- Integra con strumenti CI/CD per verificare regressioni di performance

---

## 📌 Conclusioni

AWS X-Ray è uno strumento potente per ottenere **visibilità completa** delle applicazioni distribuite su AWS. Aiuta a rilevare colli di bottiglia, a migliorare la latenza e a comprendere il comportamento delle richieste utente in ambienti complessi.

> “Con X-Ray non hai più una black box — ogni richiesta lascia le sue tracce.”
