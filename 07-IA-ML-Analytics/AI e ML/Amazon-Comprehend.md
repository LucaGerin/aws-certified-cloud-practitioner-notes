--> [AWS](AWS.md)  -  [Intelligenza Artificiale e Machine Learning](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)

# 🧠 Amazon Comprehend

## 📘 Cos’è e come funziona

**Amazon Comprehend** è un servizio AWS di **Natural Language Processing (NLP)** che usa **machine learning** per estrarre insight e significati da testi non strutturati, **senza bisogno di addestrare modelli manualmente**.

Comprehend analizza documenti, frasi o paragrafi scritti in linguaggio naturale per identificare:
- **Entità** (nomi, organizzazioni, luoghi, ecc.)
- **Sentiment** (positivo, negativo, neutro, misto)
- **Frasi chiave**
- **Lingua del testo**
- **Relazioni tra entità**
- **Classificazione dei documenti**

Il tutto può essere integrato facilmente in applicazioni tramite **API REST**, SDK o servizi AWS come Lambda, S3, [Amazon Translate](Amazon-Translate.md), [Amazon Textract](Amazon-Textract.md), Kinesis e [Amazon SageMaker](Amazon-SageMaker.md).

---

## ✨ Caratteristiche principali e vantaggi

- 🔍 **Entity Recognition**: identifica nomi di persone, aziende, luoghi, date, ecc.
- 😊 **Sentiment Analysis**: valuta il tono di email, recensioni, messaggi clienti
- 📌 **Keyword Extraction**: estrae automaticamente concetti chiave da un testo
- 🧾 **Document Classification**: assegna tag tematici a documenti
- 🌐 **Language Detection**: rileva automaticamente la lingua in input
- 🧬 **Custom classification e entity recognition**: puoi addestrare modelli personalizzati
- 🔁 **Batch processing e integrazione con S3**

**Vantaggi principali:**

- ✅ Completamente gestito e serverless
- 🔠 Supporta più lingue (tra cui inglese, spagnolo, tedesco, francese, italiano)
- ⚡ Alta precisione su molti casi d’uso aziendali comuni
- 💡 Nessuna conoscenza ML richiesta per iniziare
- 🔌 Facile integrazione con pipeline ETL e servizi AI AWS

---

## 🚀 Use case comuni / ideali

Comprehend può essere usato per processare del testo, scorpire frasi chiave, argomenti, identificare lingue, eseguire sentiment analysis, e ricerca intelligente nel testo o tra documenti.

- 💬 **Analisi di feedback clienti** da sondaggi, social media, email, recensioni
- 🧑‍⚖️ **Analisi documenti legali o medici** (con entità personalizzate)
- 🧾 **Classificazione automatica** di email o ticket di supporto
- 🏢 **Rilevamento tendenze di mercato** da notizie e articoli
- 🌐 **Traduzione + analisi sentiment** di contenuti multilingua (via [Amazon Translate](Amazon-Translate.md))
- 🧠 **Raggruppamento di dati non strutturati** per insight aziendali

---

## 💰 Pricing

Amazon Comprehend ha un modello **pay-per-use**, basato su caratteri analizzati:

| Funzione                  | Prezzo indicativo                     |
|---------------------------|----------------------------------------|
| **Analisi standard**      | ~$1.00 per 1000 blocchi da 100 caratteri |
| **Custom classification** | ~$3.50 per 1000 blocchi da 100 caratteri |
| **Training personalizzato** | ~per ora, in base all’istanza utilizzata |
| **S3 batch jobs**         | Prezzo per job + caratteri processati |

🔹 È disponibile un **Free Tier** per i primi 12 mesi:  
- 50.000 caratteri/mese per tutte le API standard

---

## 🔄 Confronto con altri servizi AWS simili

| Servizio               | Finalità principale                          | Differenze rispetto a Comprehend                             |
|------------------------|-----------------------------------------------|--------------------------------------------------------------|
| **[Amazon Translate](Amazon-Translate.md)**   | Traduzione testi multilingua                  | Comprehend può essere usato dopo la traduzione per analisi   |
| **[Amazon Textract](Amazon-Textract.md)**    | Estrae testo da PDF e immagini                | Textract estrae testo, Comprehend lo interpreta              |
| **[Amazon Kendra](Amazon-Kendra.md)**      | Motore di ricerca semantico                   | Comprehend analizza testi, Kendra li rende ricercabili       |
| **[Amazon Lex](Amazon-Lex.md)**         | Chatbot e NLU interattiva                     | Lex interpreta intenti da utenti, Comprehend testi generici  |
| **[Amazon SageMaker](Amazon-SageMaker.md)**   | Addestramento ML personalizzato               | Più flessibile ma più complesso e meno automatizzato         |

---

## 📌 Conclusioni

**Amazon Comprehend** è lo strumento ideale per **estrarre automaticamente significato e insight da testi non strutturati**, in modo scalabile e intelligente. Dalla sentiment analysis alla classificazione documentale, offre una suite NLP potente e integrabile in ogni architettura cloud-native.

> “Amazon Comprehend trasforma parole in conoscenza, automaticamente.”

---

## 🆚 Amazon Comprehend e Amazon Textract

**[Amazon Textract](Amazon-Textract.md)** e **Amazon Comprehend** sono due servizi AWS che operano su **tipi di dati diversi** e svolgono ruoli complementari nel trattamento delle informazioni testuali.

- **Amazon Textract** si occupa di **estrarre testo strutturato e non strutturato da documenti visivi** (come PDF, immagini scansionate, moduli, ricevute). È ideale quando il testo è "nascosto" in un'immagine o in un documento cartaceo digitalizzato e va trasformato in dati leggibili da sistemi informatici.

- **Amazon Comprehend**, invece, **analizza testo già esistente** (in formato digitale) per **estrarre significato e insight**, come entità nominate, frasi chiave, sentiment, lingua e classificazione. È utile per l’analisi semantica di email, recensioni, articoli o documentazione.

In sintesi:
- Textract → Estrae il **cosa** c’è scritto in un documento.
- Comprehend → Interpreta **cosa significa** quel testo.

> 💡 Spesso i due servizi sono usati insieme: **Textract estrae il testo** da documenti scansionati e **Comprehend lo analizza** per ricavare insight utili.


---

### 🧠 Derivati di Amazon Comprehend

Oltre al servizio standard di **Amazon Comprehend** per l'elaborazione del linguaggio naturale (NLP), AWS offre versioni **specializzate per settori verticali**, che ampliano le capacità del servizio base adattandole a contesti specifici:

- 🏥 **Amazon Comprehend Medical**: estrae automaticamente **informazioni cliniche** da testi medici non strutturati, come diagnosi, farmaci, dosaggi, sintomi e condizioni. Utile per **cartelle cliniche elettroniche**, ricerca biomedica e flussi di lavoro sanitari.
- 🧾 **Amazon Comprehend for Insurance** *(anteprima)*: ottimizzato per comprendere documenti assicurativi, riconoscendo **termini di polizza, coperture, sinistri e responsabilità**.
- ⚖️ **Amazon Comprehend for Legal** *(anteprima o custom NLP con Comprehend Custom)*: progettato per analizzare **contratti e documenti legali**, estraendo clausole, obblighi e soggetti coinvolti.
- 🧪 **Comprehend Custom**: consente di **addestrare modelli NLP personalizzati** per casi d'uso specifici (es. riconoscere entità proprietarie o categorie aziendali) partendo da un dataset fornito dall'utente.

Queste estensioni permettono di applicare il potere dell’NLP in contesti complessi dove la terminologia e la struttura del linguaggio richiedono **modelli preaddestrati o altamente personalizzati**.

