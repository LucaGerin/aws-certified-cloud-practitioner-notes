--> [AWS](/00-Intro/AWS.md)  -  [CDN e Networking](/03-CDN-e-Networking/Rete-globale-AWS.md)
# Content Delivery Network (CDN)

Una **Content Delivery Network (CDN)** è una rete di server distribuiti geograficamente che lavorano insieme per consegnare contenuti (file statici, video, immagini, pagine web, ecc.) agli utenti finali in modo rapido, affidabile e sicuro.

## Obiettivo di una CDN

- **Ridurre la latenza:** Il contenuto è servito dal server più vicino all’utente che contiene il contenuto richiesto.
- **Migliorare le prestazioni:** Il caricamento delle pagine è più veloce.
- **Gestire picchi di traffico:** Distribuisce il carico su più server, scalabilità automatica senza creare disruptions.
- **Aumentare l’affidabilità e la reliability:** Ridondanza geografica e failover automatico.
- **Protezione:** Spesso include firewall, protezione DDoS e crittografia TLS.
- **Global Reach:** più istanze EC2 possono accedere un [EFS](/02-Storage-services/Amazon-EFS.md) simultaneamente.

## Come funziona una CDN

1. Un utente richiede una risorsa (es. immagine, file, pagina HTML).
    
2. La richiesta viene inoltrata al server CDN più vicino.
    
3. Se il contenuto è già in cache, viene servito immediatamente.
    
4. Altrimenti, la CDN lo recupera dall’origine (es. server web o storage) e lo memorizza per future richieste.
    

## Tipologie di contenuti distribuiti

- Contenuti **statici**: immagini, CSS, JavaScript, PDF, video
    
- Contenuti **dinamici** (con ottimizzazioni avanzate)
    
- Aggiornamenti software e file scaricabili
    
- Streaming live e on-demand
    

## Vantaggi principali

|Vantaggio|Descrizione|
|---|---|
|Bassa latenza|I contenuti sono erogati dalla posizione più vicina|
|Scalabilità|Gestione efficace di grandi volumi di traffico|
|Sicurezza|TLS, WAF, protezione DDoS integrabili|
|Affidabilità|Alta disponibilità grazie a nodi multipli|

## Esempi di fornitori CDN

- Cloudflare
    
- Akamai
    
- Fastly
    
- StackPath
    
- Google Cloud CDN
    
- Azure CDN
    
- **Amazon CloudFront** (servizio CDN di AWS)
    

➡️ Per chi utilizza l'infrastruttura AWS, il servizio CDN dedicato è **[Amazon CloudFront](/03-CDN-e-Networking/Amazon-CloudFront.md)**, che vedremo in dettaglio nel documento dedicato.
