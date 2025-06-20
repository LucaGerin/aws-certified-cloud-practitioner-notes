--> [AWS](/00-Intro/AWS.md)  -  [Prezzo, Fatturazione, Supporto](/10-Prezzo-Fatturazione-Supporto/Prezzo-Fatturazione-Supporto.md)
# 💸 AWS Budgets

## 📘 Cos'è e come funziona

**AWS Budgets** è un servizio che consente di **impostare soglie di spesa, utilizzo e risparmi** per monitorare e **controllare i costi** dei tuoi account AWS. 
Quando viene superato un budget definito, il sistema può rispondere in diversi modi, tra cui **inviare notifiche via email o SNS**, aiutandoti a reagire tempestivamente.

Puoi definire **budget mensili, trimestrali o annuali**, basati su **costi effettivi**, **costi previsti**, **utilizzo delle risorse**, oppure sui **crediti risparmio (Savings Plans, Reserved Instances)**.

---

## ✨ Caratteristiche principali

- 🧮 Budget su costi, utilizzo o risparmi
- 📆 Flessibilità nella frequenza: mensile, giornaliera, personalizzata
- 🛎️ Notifiche automatiche via **email o SNS**
- 💬 Integrazione con **AWS Chatbot** per notifiche su Slack o Teams
- 🧑‍💼 Supporta **account singoli o AWS Organizations**
- 📊 Dashboard dettagliata con confronto tra budget e costi effettivi

---

## ✅ Vantaggi

- ✅ **Controllo proattivo** delle spese in tempo reale
- ✅ **Prevenzione di sorprese** a fine mese
- ✅ Aiuta a rispettare limiti finanziari aziendali o di progetto
- ✅ Supporta l’**allocazione per centro di costo** grazie all’uso dei **tag**
- ✅ Utile per team FinOps, DevOps, e project management

---

## 🚀 Use case comuni

- 💰 Impostare un tetto mensile per ambienti di test o sviluppo
- 📈 Monitorare l’utilizzo di un servizio specifico (es. EC2, S3)
- 🧩 Tenere traccia del consumo di Savings Plans o RIs
- 🛑 Ricevere allerta se si superano soglie personalizzate di budget
- 🧑‍💼 Gestire il budget multi-account per un’intera organizzazione

---

## 💡 Tipologie di budget

| Tipo di Budget           | Cosa monitora                                      |
|--------------------------|-----------------------------------------------------|
| **Cost Budget**          | Spese AWS totali o per servizio                    |
| **Usage Budget**         | Quantità di risorse usate (es. ore EC2, GB S3)     |
| **Savings Plans Budget** | Percentuale di utilizzo dei Savings Plans          |
| **RI Utilization Budget**| Utilizzo delle Reserved Instances                  |
| **RI Coverage Budget**   | Copertura delle risorse con RIs                   |

---

## 💰 Pricing

- **Gratis** per i primi **2 budget attivi per account**
- **A pagamento** per più di 2 budget:
  - **0,01 USD** per budget attivo al giorno
  - Es: 10 budget attivi costano circa **3 USD/mese**


---

## 🔄 Integrazione con altri strumenti

| Strumento                | Integrazione |
|--------------------------|--------------|
| **Cost Explorer**        | Per vedere l’andamento storico delle spese |
| **Pricing Calculator**   | Per stimare costi futuri da confrontare con il budget |
| **AWS Organizations**    | Per assegnare budget ai vari account o OU |
| **AWS Chatbot**          | Per ricevere alert su Slack o Teams |

---

## 📌 Conclusione

**AWS Budgets** è un alleato fondamentale per la **gestione finanziaria del cloud**, permettendoti di restare sempre **in controllo della spesa**, evitare sorprese e supportare una **strategia FinOps efficace**.

> “Con AWS Budgets, la tua spesa cloud non sfugge mai di mano.”

