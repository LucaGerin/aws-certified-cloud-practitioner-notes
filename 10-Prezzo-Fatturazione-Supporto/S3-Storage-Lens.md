--> [AWS](00-Intro/AWS.md)  -  [Prezzo, Fatturazione, Supporto](10-Prezzo-Fatturazione-Supporto/Prezzo-Fatturazione-Supporto.md)
# 🔍 Amazon S3 Storage Lens

## 📘 Cos'è e come funziona

**Amazon S3 Storage Lens** è una funzionalità di analisi e monitoraggio progettata per offrire **visibilità approfondita sull’utilizzo dello storage S3**, supportando le organizzazioni nell’**ottimizzazione dei costi** e nella **gestione efficiente dei dati**.

S3 Storage Lens fornisce **dashboard preconfigurate** e report dettagliati su metriche come l’utilizzo per bucket, classi di storage, tendenze di crescita, oggetti non versionati, oggetti obsoleti, e altro ancora. È **nativamente integrato in S3** e **supporta ambienti multi-account** tramite AWS Organizations.

---

## ✨ Caratteristiche principali

- 📊 **Dashboard interattiva** direttamente dalla console S3
- 🧩 **Metriche granulari** a livello di bucket, account, regione, prefisso
- 🧠 **Raccomandazioni automatiche** per ottimizzare costi e prestazioni
- 🏢 Supporta **multi-account** via AWS Organizations
- 📥 Possibilità di **esportare i dati su S3** per ulteriori analisi (es. con Athena o QuickSight)
- 🛡️ Metriche su **versioning, replication, oggetti inattivi**, e compliance

---

## ✅ Vantaggi

- ✅ Migliora la **visibilità sull’utilizzo dello storage**
- ✅ Aiuta a **identificare sprechi** e ottimizzare i costi
- ✅ Supporta decisioni su **tiering, lifecycle policy e retention**
- ✅ Facile da configurare e integrato nativamente in AWS
- ✅ Utile per audit, governance e report interni

---

## 🚀 Use case comuni

- 📉 Identificare bucket con storage inutilizzato o oggetti vecchi
- 🧊 Trovare dati candidati alla transizione verso classi “cold” (Glacier, IA)
- 🧑‍💼 Supportare team finance con report dettagliati su uso e crescita
- 🧾 Facilitare la creazione di policy di **data lifecycle e retention**
- 📈 Monitorare la crescita dello storage a livello organizzativo

---

## 🧪 Tipi di metriche disponibili

| Tipo di metrica              | Esempi                          |
|------------------------------|----------------------------------|
| Utilizzo                     | GB totali, per classe, per bucket |
| Oggetti                      | Totale oggetti, non versionati   |
| Tendenze                     | Crescita settimanale/mensile     |
| Costi potenziali (stima)     | Storage inefficiente, IA non usato |
| Accessibilità                | Oggetti pubblici o non criptati  |

---

## 💰 Pricing

- **Versione base**: gratuita, con metriche standard
- **Versione avanzata**: a pagamento, include metriche aggiuntive e possibilità di **esportare i dati su S3**

---

## 🔄 Confronto con altri strumenti

| Strumento AWS          | Differenze |
|------------------------|------------|
| **S3 Inventory**       | Lista oggetti e metadati, non offre visualizzazione o raccomandazioni |
| **S3 Lifecycle**       | Esegue azioni automatiche ma non fornisce metriche o consigli |
| **Cost Explorer**      | Analizza costi globali, non specifico per lo storage S3 |
| **Storage Lens**       | Strumento completo per visibilità, analisi e raccomandazioni su S3 |

---

## 📌 Conclusione

**Amazon S3 Storage Lens** è lo strumento ideale per **monitorare, analizzare e ottimizzare** il tuo utilizzo di Amazon S3. Ti aiuta a prendere decisioni più informate sulla gestione del ciclo di vita dei dati, migliorare la governance e **contenere i costi di storage nel cloud**.

> “Non puoi ottimizzare ciò che non puoi misurare. S3 Storage Lens ti mostra dove risparmiare.”

