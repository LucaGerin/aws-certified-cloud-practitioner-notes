--> [AWS](/00-Intro/AWS.md)
# ⚡ AWS Amplify

**AWS Amplify** è una piattaforma completa per lo **sviluppo di applicazioni web e mobile** che consente di creare, configurare e implementare backend serverless, oltre a fornire strumenti per l'integrazione diretta nel frontend.

## Cos'è e come funziona

AWS Amplify fornisce una CLI, una libreria JavaScript e una console web per aiutare gli sviluppatori a creare rapidamente applicazioni moderne. Con Amplify è possibile:

- Configurare backend (API, autenticazione, storage, hosting) con pochi comandi.
- Connettere app web/mobile (React, Angular, Vue, iOS, Android, Flutter) direttamente ai servizi AWS.
- Automatizzare la CI/CD e il deploy continuo delle app frontend.

Amplify si integra con servizi come [AWS AppSync](/Others/Amazon-AppSync.md), [Amazon Cognito](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Cognito.md), [Amazon S3](/02-Storage-services/Amazon-S3.md), [AWS Lambda](/01-Compute-options/AWS-Lambda.md) e [Amazon DynamoDB](/04-Database-services/Amazon-DynamoDB.md).

## Caratteristiche principali e vantaggi

- **CLI e toolchain moderna:** per creare e gestire ambienti cloud con pochi comandi.
    
- **Hosting e CI/CD:** per app statiche e single-page, con supporto per custom domain, SSL, branching Git.
    
- **Autenticazione semplificata:** integrazione con Amazon Cognito per login, registrazione e federazione.
    
- **Supporto multi-platform:** librerie client per JavaScript, Android, iOS, Flutter, React Native.
    
- **Backend componibile:** crea funzioni Lambda, API REST/GraphQL, database, file storage e notifiche push.
    
- **DataStore:** sincronizzazione offline/online automatica con supporto ai conflitti.
    

## Use cases

- **App mobile e web con backend serverless**
    
- **Prototipi rapidi** con deploy automatico da Git
    
- **Applicazioni offline-first** con DataStore
    
- **Autenticazione utenti federata e sicura**
    
- **App multiambiente (dev/test/prod)**
    

## Pricing

AWS Amplify ha un modello **pay-as-you-go**:

- **Hosting:** tariffato in base a build, storage e banda utilizzata.
    
- **Backend:** si paga per i servizi utilizzati (es. Cognito, S3, AppSync, Lambda).
    

È previsto un **livello gratuito** che include:

- 1000 build minuti/mese
    
- 5 GB di storage e 15 GB di banda mensili per l’hosting
    
- Livello gratuito standard dei servizi backend
    

## Sicurezza

La sicurezza in Amplify è ereditata dai servizi sottostanti:

- **Cognito** per autenticazione/autorizzazione
    
- **IAM** per la gestione dei permessi verso le risorse AWS
    
- **HTTPS** automatico per l’hosting
    

Supporta l'accesso granulare per utenti autenticati e guest, multi-tenancy e regole di sicurezza personalizzabili a livello di campo per AppSync.

## Confronto con servizi simili in AWS

|Servizio|Focus principale|Quando usarlo|
|---|---|---|
|AWS Amplify|Full-stack app web/mobile|Per frontend con backend integrato e deploy rapido|
|[AWS AppSync](/Others/Amazon-AppSync.md)|API GraphQL|Per aggregazione dati e real-time API|
|[Amazon API Gateway](/Others/Amazon-API-Gateway.md)|API REST o WebSocket|Per microservizi o API REST gestite separatamente|

## Conclusioni

AWS Amplify semplifica lo sviluppo e il deploy di applicazioni moderne, integrando strumenti frontend e backend in un'unica piattaforma. Ideale per startup, team agili e app mobile-first, sfrutta la potenza della [rete globale AWS](/03-CDN-e-Networking/Rete-globale-AWS.md) con un approccio rapido, modulare e sicuro.