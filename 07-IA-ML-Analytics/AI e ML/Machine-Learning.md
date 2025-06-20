--> [AWS](/00-Intro/AWS.md)  -  [Intelligenza Artificiale e Machine Leraning](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md)
# Introduzione al Machine Learning

## 🤖 Cos'è il Machine Learning?

Il **Machine Learning (ML)** è una branca dell'intelligenza artificiale che consente ai sistemi di **apprendere automaticamente dai dati**, migliorando le proprie prestazioni su un compito senza essere esplicitamente programmati. Invece di seguire istruzioni rigide, un modello ML apprende **pattern statistici** dai dati e li utilizza per fare previsioni, classificazioni o raccomandazioni.

---

## 📈 Tipi principali di Machine Learning

| Tipo                  | Descrizione                                                             | Esempi comuni                         |
|-----------------------|-------------------------------------------------------------------------|---------------------------------------|
| **Supervised Learning**   | Il modello impara da dati etichettati (input + output noti)              | Classificazione email, regressione prezzi |
| **Unsupervised Learning** | Il modello cerca pattern nascosti nei dati non etichettati               | Segmentazione clienti, clustering     |
| **Reinforcement Learning** | Il modello apprende tramite interazione e ricompense/penalità             | Robotica, gaming, ottimizzazione      |
| **Self-supervised / Semi-supervised** | Impara da dati parzialmente etichettati o con segnali interni   | NLP, Visione artificiale avanzata     |

---

## 🔁 Workflow tipico in un progetto di Machine Learning

![ML workflow](img/ML-workflow.png)

Un progetto ML segue un ciclo strutturato, che può essere suddiviso in **7 fasi principali**:

### 1. 📥 Raccolta e accesso ai dati

- Acquisizione da fonti come: database, API, file CSV, IoT, scraping, log, ecc.
- Archiviazione su: file locali, cloud (es. Amazon S3), data warehouse (es. Redshift)

### 2. 🧹 Pulizia e preparazione dei dati (Data Preprocessing)

- Rimozione valori nulli, outlier, ridondanze
- Feature engineering: creazione, trasformazione, normalizzazione delle variabili
- Encoding di variabili categoriche (one-hot, label encoding)
- Split dei dati: **train / validation / test**

### 3. 🔍 Esplorazione e analisi dei dati (EDA)

- Visualizzazioni (distribuzioni, correlazioni, istogrammi)
- Statistiche descrittive
- Identificazione di pattern o anomalie
- Analisi della bilanciatura delle classi

### 4. 🧠 Scelta e addestramento del modello

- Selezione dell'algoritmo: regressione, classificazione, clustering, deep learning, ecc.
- Addestramento su dataset di training
- Ottimizzazione con **cross-validation**

### 5. 🛠️ Tuning e ottimizzazione

- Tuning degli **iperparametri** con grid search, random search, bayesian optimization
- Valutazione performance con metriche appropriate:
  - Accuracy, Precision, Recall, F1, AUC (classificazione)
  - MSE, RMSE, R² (regressione)
- Evitare overfitting/underfitting

### 6. 🚀 Deploy del modello

- Modello esportato e distribuito come:
  - API REST (es. Flask, FastAPI, SageMaker endpoint)
  - Microservizio containerizzato (es. Docker + ECS/EKS)
  - In batch su pipeline ETL (es. Glue, Airflow, EMR)

### 7. 📊 Monitoraggio e manutenzione

- Monitoraggio drift del modello (cambi nei dati o prestazioni)
- Logging delle predizioni e feedback degli utenti
- Aggiornamento periodico con nuovi dati (retraining)
- Automazione con **MLOps pipelines**

---

## 📚 Esempio pratico (Supervised Learning - classificazione email)

1. Raccolta dati: dataset con email e label “spam”/“non spam”
2. Preprocessing: rimozione stopwords, stemming, vettorizzazione (TF-IDF)
3. Addestramento: classificatore Naive Bayes o Random Forest
4. Valutazione: precisione, recall, matrice di confusione
5. Deploy: API Flask con modello salvato in pickle
6. Monitoraggio: conteggio predizioni, log errori

---

## 🛠️ Tool e tecnologie comuni

| Categoria             | Strumenti                                          |
|-----------------------|----------------------------------------------------|
| Linguaggi             | Python, R, Julia                                   |
| Librerie ML           | scikit-learn, XGBoost, LightGBM, TensorFlow, PyTorch |
| Notebook              | Jupyter, Google Colab, SageMaker Studio            |
| Visualizzazione       | matplotlib, seaborn, Plotly, Power BI              |
| MLOps                 | MLflow, Kubeflow, SageMaker Pipelines, Vertex AI   |
| Cloud                 | AWS, GCP, Azure                                     |

---

## 📌 Conclusioni

Il Machine Learning non è solo una tecnologia, ma un **processo iterativo** che richiede conoscenza dei dati, competenze statistiche e infrastrutture adeguate. Capire bene il **workflow ML** ti aiuta a sviluppare modelli più robusti, spiegabili e pronti per l’uso in produzione.

> “Il Machine Learning inizia con i dati, ma si realizza con un ciclo continuo di apprendimento e miglioramento.”

Il principale tool fornito da amazon per il Ml è **[Amazon SageMaker](07-IA-ML-Analytics/AI e ML/Amazon-SageMaker.md)**, ma ce ne sono anche [altri](/07-IA-ML-Analytics/Intelligenza-artificiale-Machine-Learning-e-Analytics.md).
