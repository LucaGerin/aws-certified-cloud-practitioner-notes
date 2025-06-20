--> [AWS](/00-Intro/AWS.md)
# 🌐 Amazon API Gateway

**Amazon API Gateway** è un servizio completamente gestito che consente di creare, pubblicare, monitorare e proteggere API RESTful, WebSocket e HTTP su larga scala, facilitando l'integrazione tra client e backend in ambienti cloud-native.

![API Gateway](api-gateway.png)

## Cos'è e come funziona

Amazon API Gateway funge da front-end per applicazioni serverless, microservizi o back-end tradizionali, permettendo ai client di comunicare con servizi come [AWS Lambda](/01-Compute-options/AWS-Lambda.md), [Amazon EC2](/01-Compute-options/Amazon-EC2.md), [Amazon Kinesis](/07-IA-ML-Analytics/Analytics/Amazon-Kinesis.md), o backend esterni. Gestisce il routing delle richieste, l'autenticazione, la throttling, il caching e la trasformazione dei payload (ad esempio da JSON a XML).

Supporta tre tipi di API:

- **REST API:** adatte per applicazioni con requisiti avanzati di gestione e trasformazione.
    
- **HTTP API:** leggere e ottimizzate per prestazioni e costi, ideali per integrazioni semplici.
    
- **WebSocket API:** per comunicazioni bidirezionali in tempo reale.
    

## Caratteristiche principali e vantaggi

- **Integrazione con AWS Lambda** e altri servizi
    
- **Gestione traffico:** rate limiting, burst limit, throttling
    
- **Caching e accelerazione delle risposte**
    
- **Monitoring e logging:** integrazione con [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md)
    
- **Supporto per CORS e autorizzazioni complesse**
    
- **Custom domain e versioning API**
    

## Use cases

- **Back-end per applicazioni mobili o web**
    
- **Accesso sicuro a microservizi**
    
- **Real-time messaging con WebSocket API**
    
- **Gestione di API pubbliche o partner**
    
- **Creazione di gateway unificato per più backend**
    

## Pricing

Il prezzo dipende dal tipo di API:

- **REST API:** si paga per milioni di chiamate, cache e traffico dati
    
- **HTTP API:** più economiche, adatte per carichi moderni
    
- **WebSocket API:** basate su connessioni attive e messaggi scambiati
    

È disponibile un **livello gratuito** mensile: 1 milione di chiamate HTTP o REST API e 1 milione di messaggi WebSocket.

## Sicurezza

Amazon API Gateway supporta diversi meccanismi di autenticazione:

- **[Amazon Cognito](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Cognito.md):** gestione utenti e federazione
    
- **IAM:** accesso controllato tramite ruoli/policy AWS
    
- **JWT/OpenID Connect:** token personalizzati da identity provider esterni
    
- **API Key:** per accesso controllato o rate limit personalizzati
    

Supporta anche WAF per la protezione da attacchi comuni (SQL injection, XSS, etc.)

## Confronto con servizi simili in AWS

|Servizio|Tipo di API|Quando usarlo|
|---|---|---|
|Amazon API Gateway|REST, HTTP, WebSocket|Per gateway API completo e sicuro|
|[AWS AppSync](/Others/Amazon-AppSync.md)|GraphQL|Per aggregazione dati e API real-time|
|[AWS Amplify API](/Others/AWS-Amplify.md)|REST/GraphQL|Per sviluppo rapido frontend con backend gestito|

## Conclusioni

Amazon API Gateway è il punto di ingresso ideale per costruire API moderne, sicure e scalabili. Offre un'integrazione fluida con l'intero ecosistema AWS e permette di implementare architetture serverless o microservizi in modo efficiente, sfruttando la [rete globale AWS](/03-CDN-e-Networking/Rete-globale-AWS.md).