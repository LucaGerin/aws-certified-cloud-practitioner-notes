--> [AWS](AWS.md)  -  [Intelligenza Artificiale e Machine Learning](Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# 🔍 Amazon Kendra

## 📘 Cos'è e come funziona

**Amazon Kendra** è un servizio AWS di **ricerca intelligente (intelligent search)** basato su **machine learning** che consente agli utenti di cercare informazioni **all'interno di documenti aziendali** distribuiti su più fonti, esprimendo domande in linguaggio naturale.  
A differenza della classica ricerca per parole chiave, Kendra comprende **l'intento dell’utente** e restituisce risultati più accurati, anche da frasi complesse e domande in linguaggio naturale.

Può essere integrato in portali web, app aziendali, intranet e chatbot, e può connettersi a sorgenti dati come, per esempio, **SharePoint, S3, FSx, Salesforce, Box, Dropbox, Confluence, RDS, OneDrive, Github**, ecc.  
Supporta dati semi-strutturati e non strutturati, in formati come HTML, XML, PDF, CSV, Microsoft Office, etc.

![Kendra](Amazon-Kendra.png)

---

## ✨ Caratteristiche principali e vantaggi

- 🧠 **Ricerca semantica e ML-powered**: supporta domande in linguaggio naturale, tipo “Quali sono i benefici per i dipendenti part-time?”
- 🔌 **Connettori nativi**: supporto out-of-the-box per le principali fonti di dati aziendali
- 📎 **Comprensione del contenuto**: estrazione intelligente da documenti PDF, Word, HTML, e altro
- 🗂️ **Indexing avanzato**: indicizzazione di file strutturati e non strutturati, supporto OCR per immagini e scansioni
- 🛡️ **Sicurezza integrata**: controllo accessi granulare, search result filtering in base a ruoli
- ⚙️ **Facile integrazione**: API REST, SDK, e widget UI incorporabili in app web o mobile
- 🧪 **Test e valutazione integrati**: puoi testare facilmente le query e migliorare la qualità delle risposte

**Vantaggi principali:**

- Esperienza di ricerca **simile a Google**, ma sui tuoi dati privati
- Riduzione dei tempi spesi nella **ricerca manuale di documenti**
- Alta precisione anche in ambienti con molti documenti eterogenei
- Funziona bene anche su **piccoli dataset**, grazie all’uso del ML preaddestrato

---

## 🚀 Use case comuni / ideali

- 🔍 **Ricerca documentale interna** in aziende, enti pubblici, università
- 📁 **Accesso centralizzato alla conoscenza** aziendale distribuita su più repository
- 👩‍💻 **Supporto a team HR, legale o tecnico** per trovare policy, contratti, manuali
- 🧑‍⚕️ **Healthcare e ricerca scientifica**: interrogare archivi medici o paper clinici
- 🤖 **Chatbot e assistenti virtuali** con capacità di Q&A su documenti aziendali
- 🏛️ **Pubblica amministrazione**: trasparenza e accesso a regolamenti, bandi, delibere

Esempio di domande che si possono fare a Kendra:
- Chi, Cosa, dove, quando?
- Quando è la scadenza entro la quale va completata questa cosa?
- Domande descrittive come: "Come faccio a fare questa cosa, qual è la procedura?"
La risposta può essere un paragrafo o un intero documento.

---

## 💰 Pricing

Amazon Kendra ha due modalità di pricing principali:

### 1. **Enterprise Edition**
- Costo fisso mensile per:
  - 1 indice (fino a 100.000 documenti)
  - Include 1 Kendra index e 1 data source connector
  - Scalabile aggiungendo altri documenti o sorgenti

### 2. **Developer Edition** (per test e ambienti non-produttivi)
- Prezzo ridotto
- Funzionalità limitate (1.000 documenti, 1 utente alla volta)

🔹 **Componenti fatturati:**
- Numero di documenti indicizzati
- Numero di query effettuate (in alcuni piani)
- Storage e throughput


---

## 🔄 Confronto con altri servizi AWS simili

| Servizio                                  | Finalità principale                          | Differenze rispetto a Kendra                                   |
|-------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------|
| **[Amazon-Elasticsearch](Amazon-OpenSearch.md) / OpenSearch** | Ricerca full-text, log e metriche     | Più tecnico, ricerca keyword-based, meno semantica              |
| **[Amazon-Lex](Amazon-Lex.md)**           | Costruzione di chatbot e voicebot             | Focalizzato su dialogo, ma non ricerca documentale              |
| **[Amazon-Athena](Amazon-Athena.md)**     | Query SQL su dati in S3                       | Per analisi dati strutturati, non semantico/documentale         |
| **[Amazon-QuickSight](Amazon-QuickSight.md)** | Business Intelligence e visualizzazione dati | Visualizzazione KPI, non progettato per ricerca documenti       |
| **[Amazon-Comprehend](Amazon-Comprehend.md)** | Analisi linguistica e sentiment               | Utile per NLP, non per costruire motori di ricerca              |

---

## 📌 Conclusioni

**Amazon Kendra** è la soluzione ideale per aziende che vogliono **rendere accessibile la propria conoscenza interna** in modo semplice, intelligente e potente. Con capacità semantiche e supporto per linguaggio naturale, Kendra riduce drasticamente il tempo speso a cercare le informazioni giuste nei documenti aziendali.

> “Non si tratta solo di cercare parole: si tratta di capire le domande e trovare le risposte.”
