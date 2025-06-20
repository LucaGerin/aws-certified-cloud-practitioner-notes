--> [AWS](/00-Intro/AWS.md)
# 🔄 AWS AppSync

**AWS AppSync** è un servizio completamente gestito che semplifica lo sviluppo di API GraphQL scalabili, sicure e in tempo reale, integrandosi facilmente con servizi AWS come [Amazon DynamoDB](/04-Database-services/Amazon-DynamoDB.md), [AWS Lambda](/01-Compute-options/AWS-Lambda.md) e [Amazon OpenSearch Service](/07-IA-ML-Analytics/Analytics/Amazon-OpenSearch.md).
Permette agli sviluppatori di creare connessioni tra le loro applicazioni e serizi con GraphQL e pub/sub APIs sicure, serverless e ad alte prestazioni.

![AppSync functioning](appsync.png)

## Cos'è e come funziona

AWS AppSync consente di creare API GraphQL che aggregano dati da più origini, esponendoli in un unico endpoint. L'esecuzione delle query e mutazioni viene definita tramite **resolver**, che possono essere collegati a fonti dati come database NoSQL, funzioni Lambda o motori di ricerca. AppSync supporta anche **subscription** per comunicazioni in tempo reale, ideali per applicazioni collaborative o con aggiornamenti live.

## Caratteristiche principali e vantaggi

- **API GraphQL gestite:** provisioning, scaling e gestione automatizzati.
    
- **Supporto in tempo reale:** con le subscription puoi ricevere aggiornamenti automatici sui client connessi.
    
- **Integrazione con AWS:** AppSync si integra facilmente con DynamoDB, Lambda, RDS (tramite Aurora Serverless), OpenSearch e S3.
    
- **Controllo accessi avanzato:** supporta [AWS IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md), Amazon Cognito, OpenID Connect e API Key.
    
- **Caching integrato:** per migliorare la latenza e ridurre il carico sulle fonti dati.
    
- **Sincronizzazione offline:** per app mobili con supporto automatico al caching locale e sync una volta riconnessi.
    

## Use cases

- **App mobili e web interattive:** con sincronizzazione in tempo reale (chat, dashboard, collaborazioni live).
    
- **Aggregazione dati:** da più fonti con un'unica API.
    
- **App offline-first:** con sincronizzazione dati automatica alla riconnessione.
    
- **Data lake explorer:** con query verso dati in [Amazon OpenSearch Service](/07-IA-ML-Analytics/Analytics/Amazon-OpenSearch.md).
    

## Pricing

AWS AppSync ha un modello di **pay-as-you-go** basato su:

- Numero di richieste (query, mutazioni, subscription).
    
- Dati trasferiti tramite subscription.
    
- Cache abilitata (se usata).
    

È disponibile un **livello gratuito** che include 250.000 query/mutazioni al mese, 250.000 messaggi di subscription e 1 milione di risoluzioni da cache per 12 mesi.

## Sicurezza

AppSync supporta diversi meccanismi di autenticazione e autorizzazione:

- [AWS IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md): per integrazione con ruoli e policy AWS.
    
- Amazon Cognito: per utenti finali federati e gestiti.
    
- OpenID Connect: per provider esterni.
    
- API Key: per prototipi o accesso pubblico controllato.
    

Tutte le comunicazioni sono protette tramite HTTPS e le policy possono essere applicate a livello di campo nelle query GraphQL.

## Confronto con servizi simili in AWS

|Servizio|Tipo di API|Quando usarlo|
|---|---|---|
|AWS AppSync|GraphQL|Per esigenze di aggregazione, real-time o mobile|
|Amazon API Gateway|REST o WebSocket|Per API RESTful o integrazioni HTTP classiche|
|AWS Amplify API|REST/GraphQL|Per app mobili con integrazione diretta lato client|

## Conclusioni

AWS AppSync è la scelta ideale per applicazioni moderne che richiedono aggiornamenti in tempo reale, aggregazione da più origini e supporto offline. La sua integrazione nativa con altri servizi della [rete globale AWS](/03-CDN-e-Networking/Rete-globale-AWS.md) consente di creare API scalabili e resilienti con minimo sforzo operativo.