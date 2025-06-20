--> [AWS](/00-Intro/AWS.md)  -  [Intelligenza Artificiale e Machine Leraning](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# 🎙️ Amazon Transcribe

## 📘 Cos’è e come funziona

**Amazon Transcribe** è un servizio di **riconoscimento vocale automatico (ASR)**, speech-to-text, che converte **audio in testo**. Supporta trascrizioni **in tempo reale o batch**, con identificazione di altoparlanti, punteggiatura automatica e rimozione di Personally Identifiable Information (PII).

## ✨ Caratteristiche principali e vantaggi

- Supporto per più **lingue e accenti**
- **Trascrizione live (streaming)** o asincrona (file)
- Riconoscimento **speaker** (identificazione dei parlanti)
- **Redazione automatica** di dati sensibili
- Integrazione con servizi come **S3, Lambda, Connect**

## 🚀 Use case comuni / ideali

- **Analisi conversazioni call center**
- **Sottotitolazione automatica** di contenuti video
- **Trascrizione di webinar, podcast e riunioni**
- **Documentazione medica e legale**
- Creazione di appunti da meetings

## 💰 Pricing

- ~$0.0004 per secondo (~$0.024 al minuto)
- Prezzi aggiuntivi per redazione o modelli personalizzati
- Free Tier: 60 minuti/mese per 12 mesi

## 🔄 Confronto con altri servizi AWS

| Servizio            | Differenze rispetto a Transcribe                |
|---------------------|--------------------------------------------------|
| [Polly](07-IA-ML-Analytics/AI e ML/Amazon-Polly.md)   | Fa il contrario: converte testo in voce         |
| [Comprehend](07-IA-ML-Analytics/AI e ML/Amazon-Comprehend.md)   | Analizza testo, ma non lo genera da audio       |
| [Kendra](07-IA-ML-Analytics/AI e ML/Amazon-Kendra.md)     | Indicizzazione testi, non elaborazione audio    |
