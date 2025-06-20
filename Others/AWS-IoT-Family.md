--> [AWS](/00-Intro/AWS.md)
# 📡 AWS IoT

**AWS IoT** è una suite di servizi cloud che consente ai dispositivi connessi (sensori, attuatori, oggetti smart) di interagire in modo sicuro e scalabile con applicazioni e altri servizi AWS.

## Cos'è e come funziona

AWS IoT consente ai dispositivi di connettersi al cloud, raccogliere dati, elaborare eventi in tempo reale, e interagire con applicazioni o altri dispositivi. I dispositivi possono pubblicare e sottoscrivere messaggi tramite un broker MQTT sicuro e integrarsi facilmente con altri servizi AWS come [AWS Lambda](/01-Compute-options/AWS-Lambda.md), [Amazon Kinesis](/07-IA-ML-Analytics/Analytics/Amazon-Kinesis.md) e [Amazon S3](/02-Storage-services/Amazon-S3.md).

## Caratteristiche principali e vantaggi

- **Connessione sicura:** supporto per TLS, X.509, autenticazione mutual TLS e policy granulari.
    
- **Gestione dei dispositivi:** registrazione, organizzazione e gestione a larga scala di dispositivi.
    
- **Elaborazione edge:** con AWS IoT Greengrass puoi eseguire codice localmente su dispositivi.
    
- **Regole automatizzate:** AWS IoT Rules Engine per elaborare e inoltrare i dati in tempo reale.
    
- **Machine Learning integrato:** facile integrazione con [Amazon SageMaker](07-IA-ML-Analytics/AI e ML/Amazon-SageMaker.md) e altri servizi ML.
    
- **Monitoraggio e logging:** integrazione con [Amazon CloudWatch](/08-Auditing-Monitoring-Logging/Amazon-CloudWatch.md) e [AWS CloudTrail](/08-Auditing-Monitoring-Logging/Amazon-CloudTrail.md).
    

## Use cases

- **Smart home:** gestione di dispositivi domestici connessi come termostati, luci, e serrature.
    
- **Manifattura industriale:** monitoraggio macchinari e predizione guasti con dati IoT.
    
- **Healthcare:** raccolta e analisi dati da dispositivi indossabili.
    
- **Agricoltura:** monitoraggio ambientale e automazione dell'irrigazione.
    
- **Automotive:** telemetria veicolare, aggiornamenti OTA (over-the-air), e tracciamento.
    

## Pricing

AWS IoT adotta un modello di **pay-as-you-go**, in base a:

- Numero di messaggi inviati e ricevuti.
    
- Numero di connessioni attive.
    
- Utilizzo di funzionalità avanzate come Device Defender, Greengrass, Analytics.
    

I costi variano in base al servizio specifico (es. IoT Core, IoT SiteWise, IoT Events). È disponibile un **livello gratuito** per AWS IoT Core con 2.250.000 messaggi al mese per 12 mesi.

## Sicurezza

La sicurezza è al centro dei servizi AWS IoT:

- Certificati X.509 per l'autenticazione.
    
- Policy granulari per l'autorizzazione.
    
- Audit e monitoraggio continui tramite AWS IoT Device Defender.
    
- Supporto per crittografia end-to-end.
    

## Servizi AWS IoT principali

### AWS IoT Core

Permette ai dispositivi connessi di comunicare in modo sicuro con applicazioni cloud e tra loro. Supporta MQTT, HTTPS e WebSocket. Include funzionalità per gestire certificati, policy di accesso e motore di regole per elaborazione eventi.

### AWS IoT Greengrass

Consente ai **dispositivi edge** di eseguire localmente funzioni AWS Lambda, di messaggistica per comunicare, sincronizzare i dati con il cloud anche offline. Ideale per scenari con latenza bassa o connettività intermittente. E' indicato per scenari in cui c'è poca connettività e conviene processare i dati localmente per questioni di distanza. 
Per scenari con devices che si trovano in posizioni molto dislocate, è preferibile IoT Core.

### AWS IoT SiteWise

Serve per raccogliere, archiviare e analizzare dati industriali da macchinari su scala. Consente di modellare asset, definire metriche e creare dashboard per monitoraggio e analisi.

### AWS IoT Analytics

Un servizio completamente gestito che consente di eseguire analisi complesse su grandi volumi di dati IoT. Supporta query SQL, pipeline di elaborazione e integrazione con strumenti ML come Jupyter Notebook.

### AWS IoT Device Defender

Fornisce strumenti per migliorare la sicurezza dei dispositivi IoT. Include funzionalità di auditing, monitoraggio continuo, rilevamento anomalie e definizione policy di sicurezza.

## Confronto tra i servizi AWS IoT

|Servizio|Focus principale|Quando usarlo|
|---|---|---|
|AWS IoT Core|Connessione dispositivi e messaggistica|Uso generale per connessione e scambio dati|
|AWS IoT Greengrass|Elaborazione edge|Se vuoi eseguire codice localmente sui dispositivi|
|AWS IoT SiteWise|Raccolta e analisi dati industriali|Per ambienti di produzione e fabbriche|
|AWS IoT Analytics|Analisi di grandi volumi di dati IoT|Quando hai bisogno di insight dai dati IoT|
|AWS IoT Device Defender|Sicurezza e monitoraggio dispositivi|Per audit, conformità e rilevamento anomalie|

## Altri servizi e integrazioni utili

- [Amazon Kinesis Data Firehose](/07-IA-ML-Analytics/Analytics/Amazon-Kinesis.md) per lo streaming dei dati.
    
- [AWS Lambda](/01-Compute-options/AWS-Lambda.md) per la gestione eventi serverless.
    
- [Amazon DynamoDB](/04-Database-services/Amazon-DynamoDB.md) e Amazon Timestream per la memorizzazione dati temporali.
    

## Conclusioni

I servizi AWS IoT permettono di realizzare soluzioni scalabili, sicure e intelligenti per dispositivi connessi in una vasta gamma di settori. Grazie alla loro integrazione con la [rete globale AWS](/03-CDN-e-Networking/Rete-globale-AWS.md), consentono l'elaborazione dati a bassa latenza e con alta affidabilità.