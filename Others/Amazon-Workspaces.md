--> [AWS](/00-Intro/AWS.md)
# 💻 Amazon WorkSpaces

## 📘 Cos'è e come funziona

**Amazon WorkSpaces** è un servizio di desktop virtuali cloud che permette a utenti e team di accedere in sicurezza a un ambiente desktop completo da qualsiasi dispositivo.

## ✨ Caratteristiche principali e vantaggi

- Accesso sicuro da qualsiasi luogo
- Desktop Windows o Linux gestiti
- Fatturazione oraria o mensile
- Integrazione con AD e SSO
- Gestione centralizzata dei desktop
- 
## 🆚 Amazon WorkSpaces vs Amazon WorkSpaces Web

**Amazon WorkSpaces** è un servizio di **Desktop-as-a-Service (DaaS)** che fornisce agli utenti un **desktop virtuale completo**, persistente e personalizzabile, eseguito su macchine virtuali Windows o Linux. Gli utenti possono accedere al proprio ambiente desktop da qualsiasi dispositivo, con accesso a file, applicazioni locali e risorse aziendali, come se fossero su un PC tradizionale.

**Amazon WorkSpaces Web**, invece, è una soluzione più leggera che consente agli utenti di accedere in modo sicuro a **siti web e applicazioni web**, siti web interni e app SaaS, tramite un **browser gestito nel cloud**, senza distribuire o gestire desktop virtuali completi. 
Non offre storage o applicazioni locali, ma si concentra esclusivamente sull’**accesso sicuro via browser** a risorse aziendali.
> Workspaces web non è, come Workspaces, un servizio di Desktop-as-a-Service, ma permette di accedere a siti web interni o a software-as-a-service. 

Le prestazioni e le features offerte da Workspaces web sono diverse (inferiori) rispetto a utilizzare l'applicazione di Workspaces. Tuttavia, Workspaces web offe la possibilità di accedere più velocemente e facilmente ai desktop virtuali da diversi dispositivi e location.

In sintesi, WorkSpaces è pensato per chi ha bisogno di un vero desktop remoto, mentre WorkSpaces Web è adatto a utenti occasionali o a chi deve accedere solo a contenuti e strumenti web in modo sicuro.


## 🚀 Use case comuni/ideali

- Lavoro remoto e ibrido
- Call center distribuiti
- Sviluppo software isolato
- Ambienti temporanei per studenti o consulenti

## 💰 Pricing

- Pagamento mensile o orario
- Nessun costo di licenza upfront
- Include storage e rete

## 🔄 Confronto con servizi simili AWS

| Servizio AWS         | Differenze                          |
|----------------------|-------------------------------------|
| Amazon AppStream 2.0 | Streaming di singole applicazioni   |
| EC2 + Remote Desktop | Gestione completamente manuale      |
