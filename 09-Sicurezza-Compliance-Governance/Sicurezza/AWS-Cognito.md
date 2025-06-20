--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🔐 Amazon Cognito

**Amazon Cognito** è un servizio gestito che fornisce autenticazione, autorizzazione e gestione utenti per applicazioni web e mobile. Permette agli sviluppatori di aggiungere facilmente funzionalità di sign-up, login e controllo accessi.

![Cognito](img/cognito.png)

## Cos'è e come funziona

Amazon Cognito si basa su due componenti principali:

- **User Pools:** per gestire directory utenti e flussi di autenticazione degli utenti.
    
- **Identity Pools:** per assegnare ruoli IAM ad utenti autenticati (o guest) e fornire accesso temporaneo alle risorse AWS.
    

Supporta autenticazione tramite:

- Login diretto (email/password)
    
- Provider social (Google, Facebook, Apple)
    
- Provider federati tramite SAML o OpenID Connect
    

Può essere integrato con [AWS Amplify](/Others/AWS-Amplify.md), [API Gateway](/Others/Amazon-API-Gateway.md), [AWS AppSync](/Others/Amazon-AppSync.md) e altri servizi per garantire l’accesso sicuro e granulare alle risorse cloud.

## Caratteristiche principali e vantaggi

- **Autenticazione completa:** login, registrazione, verifica email/SMS, recupero password
    
- **Federazione utenti:** social login e SAML
    
- **Autorizzazioni granulari:** basate su ruoli IAM
    
- **Multi-factor authentication (MFA)**
    
- **Trigger personalizzabili:** con [AWS Lambda](/01-Compute-options/AWS-Lambda.md) per ogni fase del flusso utente
    
- **Integrazione con OAuth 2.0 e OpenID Connect**
    

## Use cases

- **Login per app web/mobile**
    
- **Federazione utenti aziendali tramite SAML**
    
- **Controllo accessi per API AWS**
    
- **Accesso guest con autorizzazioni limitate**
    

## Pricing

Amazon Cognito offre un **livello gratuito**:

- 50.000 utenti attivi mensili per User Pools
    
- 10 GB di storage profili utente
    
- 50.000 chiamate al mese tramite Identity Pools
    

Oltre il free tier, i costi dipendono dal numero di utenti attivi mensili (MAUs), dal traffico di autenticazione e dalle funzionalità opzionali (es. SMS, Lambda triggers).

## Sicurezza

Cognito supporta:

- MFA con SMS o app di autenticazione
    
- Crittografia dei dati in transito e a riposo
    
- Policy di password personalizzabili
    
- Audit tramite [AWS CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md)
    

Con Identity Pools, fornisce **token temporanei firmati** che limitano l'accesso ai servizi AWS secondo ruoli IAM definiti.

## Confronto con servizi simili in AWS

|Servizio|Focus principale|Quando usarlo|
|---|---|---|
|Amazon Cognito|Login utenti e accesso AWS|Per autenticazione diretta e federata|
|[AWS IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)|Accesso tra risorse AWS|Per utenti tecnici, ruoli di sistema|
|[Amazon API Gateway](/Others/Amazon-API-Gateway.md) + JWT|Autenticazione tramite token|Se si usa un provider esterno|

## Conclusioni

Amazon Cognito è la soluzione ideale per gestire l’identità degli utenti in modo sicuro, scalabile e conforme, integrandosi perfettamente con altri servizi della rete globale AWS. 
Consente agli sviluppatori di concentrarsi sull’applicazione, lasciando ad AWS la complessità dell'autenticazione e autorizzazione.