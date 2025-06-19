--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# AWS Step Functions

**AWS Step Functions** è un servizio serverless che consente di orchestrare flussi di lavoro (workflow) per coordinare servizi AWS e applicazioni custom. Utilizza **macchine a stati (state machine)** per eseguire compiti complessi come sequenze, branching, retry, parallelo e timeout in modo visivo, affidabile e scalabile.

![Step functions example](step.png)

---

## 🧩 Caratteristiche principali

- **Orchestrazione visiva** di servizi AWS e microservizi: permettono di visualizzare e orchestrare una applicazione serverless.
- **Supporto per flussi di lavoro sequenziali, paralleli, condizionali**
- **Gestione automatica di retry, timeout, catch**: permettono di attivare e seguire automaticamente ogni step.
- **Compatibile con [AWS Lambda](AWS-Lambda.md), [Amazon ECS](Amazon-ECS.md), [Amazon SQS](Amazon-SQS.md), [Amazon DynamoDB](Amazon-DynamoDB.md), [Amazon SageMaker](Amazon-SageMaker.md), [AWS Glue](AWS-Glue.md)**, ecc.
- **Monitoraggio integrato** con console visuale, [Amazon CloudWatch](Amazon-CloudWatch.md) e CloudTrail
- **Supporta Standard e Express Workflows**
- **Logging**: Tracciano ogni step e ogni suo stato

![Step function example](step-functions-visualization.png)

---

## 🔄 Tipi di workflow

| Tipo              | Standard                         | Express                          |
|-------------------|----------------------------------|----------------------------------|
| Durata            | Fino a 1 anno                    | Fino a 5 minuti                  |
| Throughput        | Basso-medio                      | Alto (event-driven, streaming)  |
| Prezzo            | Per transizione                  | Per durata (ms)                 |
| Use case tipici   | Orchestrazione batch, ETL, ML    | API backend, IoT, eventi rapidi |

---

## 🔧 Struttura di uno State Machine (JSON)

```json
{
  "Comment": "Esempio semplice",
  "StartAt": "PassoIniziale",
  "States": {
    "PassoIniziale": {
      "Type": "Pass",
      "Result": "Ciao Step Functions!",
      "End": true
    }
  }
}
```

---

## 🛠️ Stati principali supportati

- `Pass`: passa dati avanti senza modificarli
- `Task`: esegue un'azione (es. Lambda, ECS, Glue)
- `Choice`: ramifica il flusso in base a condizioni
- `Wait`: attende per tempo o data specifica
- `Parallel`: esegue stati in parallelo
- `Map`: applica una logica a una lista di elementi
- `Fail`, `Succeed`: termina il flusso con esito negativo o positivo

---

## 🎯 Use case comuni

- Orchestrazione di funzioni [AWS Lambda](AWS-Lambda.md) con flussi condizionali
- Automatizzazione di pipeline **ETL/ELT**
- Coordinamento tra Amazon API Gateway, [Amazon SQS](Amazon-SQS.md), [Amazon DynamoDB](Amazon-DynamoDB.md)
- Gestione processi **di approvazione** o **processi umani**
- **Training ML** e orchestrazione con [Amazon SageMaker](Amazon-SageMaker.md) o [AWS Glue](AWS-Glue.md)

![Step function example](step-functions.png)

---

## 🔐 Sicurezza

- [Amazon IAM](AWS-IAM.md) controlla chi può eseguire, modificare o visualizzare uno state machine
- I Task devono avere **ruoli [IAM](AWS-IAM.md) appropriati** per accedere ai servizi usati
- Loggabile tramite **CloudTrail** per audit

---

## 📈 Monitoraggio e debug

- **AWS Console Step Functions**: visualizzazione grafica del flusso e dei singoli step
- [Amazon CloudWatch](Amazon-CloudWatch.md) Logs: per output dettagliato e metriche
- CloudTrail: traccia chi ha avviato, modificato o fallito uno step

---

## ✅ Best Practices

- Usa **Express Workflows** per eventi ad alta frequenza e brevi
- Spezza flussi molto lunghi in sottoprocessi riutilizzabili
- Gestisci errori con blocchi `Retry` e `Catch`
- Centralizza i log su [Amazon CloudWatch](Amazon-CloudWatch.md) e abilita la tracciabilità
- Testa i flussi con input simulati prima del deployment

---

## 📌 Conclusioni

AWS Step Functions è uno strumento potente per gestire processi complessi e automatizzati su AWS. Grazie all’orchestrazione visiva, alla scalabilità nativa e all’integrazione con molti servizi, consente di costruire architetture robuste, resilienti e manutenibili in modo semplice e modulare.

> “Con Step Functions, ogni passo del tuo workflow è sotto controllo.”
