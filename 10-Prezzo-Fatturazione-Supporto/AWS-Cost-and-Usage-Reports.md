--> [AWS](/00-Intro/AWS.md)  -  [Prezzo, Fatturazione, Supporto](/10-Prezzo-Fatturazione-Supporto/Prezzo-Fatturazione-Supporto.md)
# 📄 AWS Cost and Usage Reports (CUR)

## 📘 Cos'è e come funziona

**AWS Cost and Usage Reports (CUR)** è lo strumento più **dettagliato** fornito da AWS per **esportare e analizzare i dati di costi e utilizzo** dell’infrastruttura cloud. CUR genera report CSV compressi che includono **tutte le transazioni di fatturazione**, fino al livello di singola risorsa e utilizzo orario.

I report vengono **salvati automaticamente in un bucket Amazon S3**, con aggiornamento giornaliero o mensile, e possono essere analizzati tramite strumenti come **Amazon Athena, Redshift, QuickSight o Excel**.

---

## ✨ Caratteristiche principali

- 🧾 Dati estremamente dettagliati (livello di risorsa, istanza, usage type)
- 📦 Esportazione automatica su S3 in formato CSV (compressi in GZIP)
- 🔄 Aggiornamento giornaliero o mensile
- 🎯 Supporta **tag**, account AWS Organizations, linked account, regioni, tipo di utilizzo
- 🔍 Può essere interrogato tramite **Athena** con query SQL
- 📈 Integrazione con **Amazon QuickSight** per dashboard interattive

---

## ✅ Vantaggi

- ✅ Massima visibilità e tracciabilità dei costi AWS
- ✅ Indispensabile per team FinOps e analisti finanziari
- ✅ Supporta audit, rendicontazione e allocazione per centro di costo
- ✅ Abilitato per ambienti multi-account tramite **AWS Organizations**
- ✅ Ottimo per integrazioni con sistemi di BI o cost management interni

---

## 🚀 Use case comuni

- 🧮 Creare report di chargeback per unità di business o progetti
- 📉 Identificare servizi sottoutilizzati e ottimizzare i costi
- 📊 Creare dashboard personalizzate dei costi in Power BI o QuickSight
- 🔎 Effettuare analisi predittive basate su dati di utilizzo reali
- 🛡️ Supportare audit o esigenze di compliance (es. GDPR, ISO)

---

## 🛠️ Come si configura

1. Vai su Billing Console
2. Seleziona **Cost and Usage Reports**
3. Clicca su "Create report"
4. Dai un nome al report, seleziona le opzioni (tag, granulosità, aggiornamento)
5. Scegli il bucket S3 di destinazione
6. (Opzionale) Abilita integrazione con **Athena** per analisi via SQL

---

## 💰 Pricing

- Il servizio **non ha costi diretti**.
- **Costo S3**: paghi solo lo storage degli oggetti CSV nel bucket (modesto)
- **Costo Athena / Redshift / QuickSight**: applicato se usi questi strumenti per interrogare o visualizzare i dati

---

## 🔄 Confronto con altri strumenti

| Strumento                     | Livello di dettaglio | Interattività | Finalità principale                 |
|------------------------------|----------------------|---------------|-------------------------------------|
| **Cost Explorer**            | Medio                | Alta          | Analisi visiva e rapida             |
| **AWS Budgets**              | Basso                | Alta (con alert) | Controllo e notifica sui limiti   |
| **Cost and Usage Reports**   | Molto alto           | Nessuna diretta | Analisi profonda e automatizzata   |
| **TCO Calculator**           | N/A (simulativo)     | N/A           | Stima costi pre-migrazione          |

---

## 📌 Conclusione

**AWS Cost and Usage Reports (CUR)** è lo **strumento definitivo per l’analisi dei costi AWS**, offrendo il massimo livello di dettaglio possibile. È ideale per grandi aziende, MSP e team FinOps che vogliono **automatizzare la reportistica**, **tracciare ogni spesa** e **ottimizzare il cloud con dati reali e affidabili**.

> “Quando ti servono numeri precisi al centesimo, CUR è la tua fonte di verità nel cloud.”

