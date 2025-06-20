--> [AWS](/00-Intro/AWS.md)  -  [Intelligenza Artificiale e Machine Learning](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# 🗣️ Amazon Lex

## 🤖 Cos’è e come funziona

**Amazon Lex** è il servizio AWS di **costruzione di chatbot (interfacce conversazionali) e assistenti vocali intelligenti** usando il Natural Language Models, basato sulla stessa tecnologia usata da **Amazon Alexa**.  
Lex consente di creare facilmente interfacce conversazionali in linguaggio naturale per applicazioni web, mobile, IVR (sistemi telefonici), e dispositivi IoT.

Lex combina **Automatic Speech Recognition (ASR)** per trasformare l’audio in testo e **Natural Language Understanding (NLU)** per comprendere l’intento dell’utente. Il tutto è accessibile tramite interfaccia visuale o API e integrabile con altri servizi AWS come Lambda, [Amazon-Kendra](/07-IA-ML-Analytics/AI-e-ML/Amazon-Kendra.md), [Amazon-Polly](/07-IA-ML-Analytics/AI-e-ML/Amazon-Polly.md), CloudWatch, Cognito, ecc.

---

## ✨ Caratteristiche principali e vantaggi

- 🧠 **Comprensione linguistica avanzata**: rilevamento automatico di intenzioni (intents) e entità (slots) a partire da testo o parlato, usando Natural Language Understanding (NLU).
- 🔁 **Dialoghi multi-turno**: gestione di conversazioni complesse su più passaggi
- 🔄 **Integrazione con [AWS-Lambda](/01-Compute-options/AWS-Lambda.md)** per eseguire logica personalizzata in base alla conversazione
- 🎙️ **Supporto input vocale e testuale** (ASR + NLU)
- 🌐 **Interfaccia grafica per la creazione di bot** e integrazione web/mobile
- 🔐 **Autenticazione con Amazon Cognito** per controllare l’accesso utente
- 💬 **Omnicanale**: Lex può essere connesso a più piattaforme, come Amazon Connect, Facebook Messenger, Slack, Twilio e altri
- 📉 **Metriche e analisi con CloudWatch e CloudTrail**

**Vantaggi principali:**
- Semplifica la creazione di **chatbot intelligenti senza dover costruire un NLP da zero**
- Altamente **scalabile e completamente gestito**
- Perfetta integrazione con l'ecosistema AWS
- Supporta **multi-lingua**, incluso italiano

---

## 🚀 Use case comuni / ideali

- 🤖 **Chatbot per customer service** su siti web o app
- 📞 **Assistenti vocali per call center** (es. integrazione con Amazon Connect)
- 📱 **Interfacce conversazionali per mobile app**
- 🛒 **Bot per e-commerce** (supporto ordini, tracking, consigli)
- 🏛️ **Chatbot per enti pubblici o università** (FAQ, prenotazioni, informazioni)
- 🧑‍💻 **Supporto tecnico automatico** o helpdesk aziendale
- 🏥 **Prenotazioni sanitarie**, gestione pazienti, triage automatico

---

## 💰 Pricing

Amazon Lex è **pay-per-use**, con due tipi principali di chiamate:

| Tipo di interazione   | Prezzo indicativo                       |
|-----------------------|------------------------------------------|
| **Text request**      | ~$0.004 per richiesta                    |
| **Speech request**    | ~$0.0065 per richiesta (audio input)     |

🔹 Nessun costo fisso mensile: paghi solo per l'uso effettivo.  
🔹 10.000 richieste gratuite al mese per i primi 12 mesi (Free Tier).

---

## 🔄 Confronto con altri servizi AWS simili

| Servizio               | Finalità principale                            | Differenze rispetto a Lex                                     |
|------------------------|-------------------------------------------------|---------------------------------------------------------------|
| **[Amazon-Kendra](/07-IA-ML-Analytics/AI-e-ML/Amazon-Kendra.md)**      | Motore di ricerca semantico                    | Non gestisce dialoghi, ma cerca risposte da documenti         |
| **[Amazon-Polly](/07-IA-ML-Analytics/AI-e-ML/Amazon-Polly.md)**       | Sintesi vocale (text-to-speech)                | Si usa insieme a Lex per creare bot vocali                    |
| **[Amazon-Transcribe](/07-IA-ML-Analytics/AI-e-ML/Amazon-Transcribe.md)**  | Trascrizione vocale in testo                   | Solo speech-to-text, non interpreta intenzioni                |
| **[Amazon-Comprehend](/07-IA-ML-Analytics/AI-e-ML/Amazon-Comprehend.md)**  | NLP per analisi di sentiment, entità, ecc.     | Elabora testi, non supporta dialoghi                          |
| **[AWS-Lambda](/01-Compute-options/AWS-Lambda.md)**         | Funzioni serverless                            | Si usa per logica custom nei bot Lex                          |

---

## 📌 Conclusioni

**Amazon Lex** è la soluzione AWS ideale per creare **chatbot e assistenti vocali intelligenti**, con una configurazione semplice, potenza NLP avanzata e ottima integrazione con l’ecosistema AWS. È adatto per costruire esperienze conversazionali moderne, scalabili e multi-canale.

> “Dai voce e intelligenza alle tue applicazioni — con Amazon Lex.”
