--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# Amazon EventBridge

**Amazon EventBridge** è un servizio di bus eventi completamente gestito che consente di costruire **architetture event-driven** scalabili e disaccoppiate. Supporta l'integrazione di servizi [AWS](AWS.md), SaaS e applicazioni custom, permettendo il routing dinamico di eventi verso più target.

> Un **Evento** è la rappresentazione di un cambio di stato.

Un evento spedito a un event bridge può triggerare una o più azioni in risposta.
EventBridge può essere usato anche per schedulare eventi in determinati momenti.

![eventbridge](eventbridge.png)

---

## 🧩 Caratteristiche principali

- **Event bus fully-managed**: riceve, filtra e inoltra eventi in tempo reale.
- **Routing basato su regole**: indirizza eventi a target in base a pattern JSON.
- **Supporta eventi da**:
  - Servizi AWS (es. [Amazon EC2](Amazon-EC2.md), [Amazon S3](Amazon-S3.md), [AWS Lambda](AWS-Lambda.md), [Amazon CloudWatch](Amazon-CloudWatch.md), [AWS CloudTrail](Amazon-CloudTrail.md)) 
  - Applicazioni personalizzate
  - Applicazioni SaaS (es. Auth0, Zendesk)
- **Integrazione profonda** con [AWS Lambda](AWS-Lambda.md), [AWS Step Functions](AWS-Step-Functions.md), [Amazon SNS](Amazon-SNS.md), [Amazon SQS](Amazon-SQS.md), [Amazon Kinesis](Amazon-Kinesis.md), API Gateway, ecc.
- **Schema Registry opzionale**: per validare e condividere eventi.

---

## 📦 Architettura

```plaintext
[Service A] ─▶ EventBridge ─▶ [Target 1: Lambda]
                            └▶ [Target 2: SQS]
                            └▶ [Target 3: Step Functions]
```

- **Event Source**: chi genera l’evento (es. [Amazon EC2](Amazon-EC2.md), un'app custom, un servizio SaaS).
- **Event Bus**: canale dove transitano gli eventi (default, custom, partner).
- **Rule**: filtra gli eventi in base al contenuto per mandarli al target giusto.
- **Target**: una azione da eseguire in risposta ([AWS Lambda](AWS-Lambda.md), [Amazon SQS](Amazon-SQS.md), [Amazon SNS](Amazon-SNS.md), ecc.)

---

## 🛠️ Esempi pratici

### Evento custom da applicazione

```json
{
  "Source": "com.miaazienda.ordine",
  "DetailType": "NuovoOrdine",
  "Detail": {
    "ordineId": "1234",
    "cliente": "Mario Rossi"
  }
}
```

### Creazione di una regola via AWS CLI

```bash
aws events put-rule \
  --name RegolaNuovoOrdine \
  --event-pattern '{"source": ["com.miaazienda.ordine"], "detail-type": ["NuovoOrdine"]}'
```

### Aggiunta target Lambda

```bash
aws events put-targets \
  --rule RegolaNuovoOrdine \
  --targets "Id"="TargetLambda","Arn"="arn:aws:lambda:region:account-id:function:GestioneOrdine"
```

---

## 🧠 Differenze rispetto a [Amazon SNS](Amazon-SNS.md) e [Amazon SQS](Amazon-SQS.md)

| Caratteristica        | EventBridge                   | SNS                         | SQS                         |
|-----------------------|-------------------------------|-----------------------------|-----------------------------|
| Pattern               | Event routing (filtro su JSON) | Pub/Sub (broadcast)         | Queue (pull-based)         |
| Fan-out               | ✔ (multi-target + filtri)     | ✔ (broadcast a subscriber)  | ✖ (uno per consumer)       |
| Supporto SaaS         | ✔ Sì                          | ✖ No                         | ✖ No                        |
| Trasporto             | Eventi                        | Messaggi                    | Messaggi                   |
| Usato per             | Architetture event-driven     | Notifiche push              | Buffering + decoupling     |

---

## 🔐 Sicurezza

- Accesso gestito tramite [IAM](AWS-IAM.md) policy
- Controllo su chi può:
  - Pubblicare eventi
  - Creare bus e regole
  - Leggere da Schema Registry
- Integrazione con [AWS CloudTrail](Amazon-CloudTrail.md) e [Amazon CloudWatch Logs](Amazon-CloudWatch.md)

---

## ✅ Best Practices

- Usa nomi coerenti per `source` e `detail-type` per eventi custom.
- Centralizza il **bus custom** per eventi di dominio.
- Definisci pattern specifici per evitare routing non intenzionale.
- Configura **DLQ** per target che falliscono.
- Abilita **archiviazione degli eventi** se serve audit o replay.

---

## 📌 Conclusioni

Amazon EventBridge è il cuore di un’architettura moderna basata su eventi. Grazie alla sua capacità di orchestrare servizi AWS e SaaS, offre **alta flessibilità, disaccoppiamento e reattività**. È ideale per sistemi modulari, scalabili e facili da estendere.

> “Con EventBridge, ogni cambiamento diventa un’opportunità per reagire in tempo reale.”
