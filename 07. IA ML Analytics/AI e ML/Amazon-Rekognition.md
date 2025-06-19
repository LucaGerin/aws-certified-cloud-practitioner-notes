--> [AWS](AWS.md)  -  [Intelligenza Artificiale e Machine Leraning](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# 👁️ Amazon Rekognition

## 📘 Cos’è e come funziona

**Amazon Rekognition** è un servizio AWS di **computer vision** basato su deep learning che consente di analizzare immagini e video per identificare oggetti, volti, scene, attività e contenuti inappropriati. 

Può essere integrato facilmente in applicazioni grazie a un set di API REST e SDK.

Il servizio è progettato per offrire funzionalità avanzate di riconoscimento visivo senza dover addestrare modelli personalizzati, rendendo accessibile la **visione artificiale** anche a sviluppatori non esperti di machine learning.

---

## ✨ Caratteristiche principali e vantaggi

- 🧠 **Rilevamento di oggetti e scene** (es. auto, edifici, animali, ecc.)
- 🧍 **Riconoscimento facciale**: individuazione, confronto, analisi delle emozioni, età stimata, presenza di occhiali, ecc.
- 🎥 **Analisi video in tempo reale o batch** tramite [Amazon Kinesis Video Streams](Amazon-Kinesis.md)
- 🧾 **Riconoscimento di testo** nelle immagini (OCR base)
- 🔞 **Rilevamento contenuti inappropriati** (nudità, violenza, ecc.)
- 🧬 **Creazione di collezioni facciali** per applicazioni di verifica identità
- 🔐 **Sicurezza integrata** con [AWS IAM](AWS-IAM.md), [AWS KMS](AWS-KMS.md), [Amazon VPC](Amazon-VPC.md)

**Vantaggi principali:**

- Totalmente **gestito e scalabile**
- Non serve esperienza in ML o CV
- Adatto a casi d’uso real-time e su grandi volumi
- Integrazione semplice con S3, Lambda, Step Functions, ecc.
- Riduce tempo e costo per analisi visiva rispetto allo sviluppo custom

---

## 🚀 Use case comuni / ideali

- 🛑 **Sorveglianza e sicurezza**: rilevamento intrusi, allarmi automatici
- 🧑‍💼 **Verifica identità** tramite riconoscimento facciale (es. accesso a sistemi)
- 🏪 **Retail**: analisi comportamenti clienti, demografia, tempo davanti agli scaffali
- 🧾 **Estrazione dati da immagini** di ricevute, fatture (OCR semplice)
- 📸 **Moderazione contenuti user-generated** su social network
- 🎞️ **Rilevamento di eventi o persone specifiche** in flussi video

---

## 💰 Pricing

Amazon Rekognition ha prezzi separati per **immagini** e **video**:

### 📷 Immagini
- **Riconoscimento oggetti e scene**: ~$0.001 per immagine
- **Riconoscimento facciale**: ~$0.001 per immagine
- **OCR (Text in Image)**: ~$0.001 per immagine
- **Moderazione contenuti**: ~$0.001 per immagine

### 🎥 Video
- **Analisi video (oggetti, volti, attività)**: ~$0.10 per minuto elaborato

🔹 Free Tier: 5.000 immagini al mese per 12 mesi (per alcune operazioni base)  

---

## 🔄 Confronto con altri servizi AWS

| Servizio                                | Finalità principale                     | Differenze rispetto a Rekognition                            |
|-----------------------------------------|------------------------------------------|--------------------------------------------------------------|
| [Amazon Textract](Amazon-Textract.md)   | Estrazione testo da documenti            | Focalizzato su PDF e formati documentali strutturati         |
| [Amazon Comprehend](Amazon-Comprehend.md) | Analisi del linguaggio naturale          | Elabora testo, non immagini o video                          |
| [Amazon Transcribe](Amazon-Transcribe.md) | Audio → testo                            | Riconosce parlato, non visivo                                |
| [Amazon Polly](Amazon-Polly.md)         | Testo → voce                             | Nessuna funzionalità visiva                                  |

---

## 📌 Conclusioni

**Amazon Rekognition** porta la potenza del **deep learning visivo** nelle mani degli sviluppatori, permettendo di automatizzare il riconoscimento facciale, la moderazione dei contenuti e l’analisi video con facilità. È lo strumento ideale per potenziare app, e-commerce, sicurezza e soluzioni smart con intelligenza visiva avanzata.

> “Dove l’occhio umano fatica, Rekognition vede.”
