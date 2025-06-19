--> [AWS](AWS.md)

# 🌟 AWS Lightsail

## Cos'è e come funziona

AWS Lightsail è un servizio cloud semplificato progettato per offrire server virtuali facili da usare, con costi prevedibili e configurazioni predefinite. È pensato per sviluppatori, piccoli team, studenti e aziende che desiderano distribuire rapidamente applicazioni web, siti WordPress, ambienti di sviluppo o progetti pilota senza la complessità dei servizi infrastrutturali più avanzati di AWS.

Con Lightsail, gli utenti possono scegliere tra istanze Linux o Windows, piani preconfigurati con risorse specifiche (CPU, RAM, storage SSD) e stack applicativi pronti all'uso. Il provisioning è semplice e avviene tramite una console utente molto intuitiva, con pochi clic.

## Caratteristiche principali e vantaggi

- **Semplicità**: interfaccia utente chiara e immediata, adatta anche a chi non ha esperienza con AWS.
- **Prezzi prevedibili**: piani mensili fissi che includono calcolo, storage, e traffico di rete.
- **Distribuzione rapida**: è possibile lanciare un'applicazione o un sito in pochi minuti.
- **Stack preconfigurati**: supporto per CMS (come WordPress), ambienti LAMP, Node.js, e altri.
- **Gestione integrata**: DNS, snapshot automatici, firewall e monitoraggio basilare inclusi.

## Sicurezza

Lightsail include funzionalità di sicurezza come firewall personalizzabili per controllare il traffico in entrata e in uscita e l’accesso SSH protetto tramite chiavi. Inoltre, supporta i certificati SSL/TLS per abilitare connessioni HTTPS sicure. I backup possono essere automatizzati tramite snapshot manuali o programmati, migliorando la resilienza dell’ambiente.

## Pricing

Lightsail utilizza un modello di pricing semplice e trasparente basato su pacchetti mensili. I piani partono da pochi dollari al mese e includono una quantità fissa di risorse (CPU, RAM, storage SSD e trasferimento dati). I costi extra si applicano solo se si superano le soglie incluse nel piano. È anche disponibile un piano gratuito limitato per i primi 3 mesi (solo per nuove istanze).

## Confronto con servizi simili in AWS

Rispetto ad Amazon EC2, Lightsail è molto più semplice da usare ma offre meno flessibilità e scalabilità. 
EC2 è ideale per applicazioni complesse o distribuite che richiedono personalizzazione avanzata delle risorse, mentre Lightsail si rivolge a progetti più piccoli e standardizzati. Inoltre, rispetto a servizi come Elastic Beanstalk, Lightsail offre maggiore controllo manuale sull'infrastruttura ma meno automazione del ciclo di vita delle applicazioni.

In sintesi, AWS Lightsail è la scelta ideale per chi desidera un'esperienza cloud semplificata e a basso costo, senza rinunciare alla potenza dell’infrastruttura AWS.

### 🚀 AWS Lightsail: Wizard e Upgrade verso EC2

AWS Lightsail offre un'esperienza semplificata grazie a wizard intuitivi che guidano l'utente nella creazione di server virtuali, database gestiti, container, e load balancer. 
Questi wizard permettono di avviare rapidamente un ambiente preconfigurato scegliendo sistema operativo, stack applicativo (es. WordPress, LAMP) e risorse desiderate. 
Quando un progetto cresce, Lightsail consente l'**upgrade a EC2** tramite un'apposita funzione di esportazione, che converte un'istanza Lightsail in un'AMI e la rende disponibile in [Amazon EC2](Amazon-EC2.md) per una gestione più avanzata e scalabile.

