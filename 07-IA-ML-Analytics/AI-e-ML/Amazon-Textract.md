--> [AWS](/00-Intro/AWS.md)  -  [Intelligenza Artificiale e Machine Leraning](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# 📄 Amazon Textract

## 📘 Cos’è e come funziona

**Amazon Textract** è un servizio AWS di **Optical Character Recognition (OCR) intelligente** che utilizza il machine learning per estrarre automaticamente testo, tabelle, moduli e dati strutturati da documenti scansionati, immagini e PDF. A differenza dell'OCR tradizionale, Textract comprende la struttura del documento, identificando ad esempio campi chiave e tabelle.

## ✨ Caratteristiche principali e vantaggi

- Riconoscimento avanzato di **testo stampato e manoscritto**, da immagini, scansioni, pdf, tabelle, forms
- Supporta il riconoscimento di sia testo stampato che scritto a mano
- Estrazione automatica di **moduli** e **tabelle**
- Supporto per **query personalizzate**
- Integrazione con altri servizi AWS (S3, Lambda, Comprehend, ecc.)
- Scalabilità automatica per grandi volumi di documenti

## 🚀 Use case comuni / ideali

- Elaborazione automatica di documenti di identificazione come carte di identità o passaporti
- Elaborazione automatica di **moduli fiscali e legali**
- Digitalizzazione di **archivi cartacei**
- Gestione documentale nel settore **sanitario o finanziario**
- Automazione in processi **back-office**

## 💰 Pricing

- Detect Document Text: ~$0.0015 per pagina
- Analyze Document (moduli): ~$0.05 per pagina
- Analyze Document (tabelle): ~$0.015 per pagina
- Free Tier disponibile


## 🔄 Confronto con altri servizi AWS

| Servizio                             | Differenze rispetto a Textract              |
| ------------------------------------ | ------------------------------------------- |
| [Rekognition](/07-IA-ML-Analytics/AI-e-ML/Amazon-Rekognition.md) | Riconosce immagini e oggetti, non testo     |
| [Comprehend](/07-IA-ML-Analytics/AI-e-ML/Amazon-Comprehend.md)   | Analizza testo esistente, non estrae da PDF |
| [Transcribe](/07-IA-ML-Analytics/AI-e-ML/Amazon-Transcribe.md)   | Elabora audio, non documenti visivi         |
