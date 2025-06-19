--> [AWS](AWS.md)  -  [Prezzo, Fatturazione, Supporto](Prezzo-Fatturazione-Supporto.md)
# 🔄 Amazon S3 Lifecycle

## 📘 Cos'è e come funziona

**Amazon S3 Lifecycle** è una funzionalità che consente di **automatizzare la gestione dei dati** nei bucket S3, attraverso **regole che spostano o eliminano oggetti** in base alla loro età o stato.

Le regole Lifecycle permettono di ottimizzare i costi spostando automaticamente gli oggetti tra **classi di storage** (es. da S3 Standard a Glacier) o **eliminandoli** quando non sono più necessari. Questo è particolarmente utile per gestire grandi volumi di dati con pattern di accesso prevedibili nel tempo.

NB: Le richieste di transizione tra classi di storage possono avere un costo, in quanto consistono in richieste GET/PUT tra la source e la target class.

---

## 🧩 Funzionalità principali

- 📦 **Transizione automatica** degli oggetti verso classi di storage a costo più basso:
  - S3 Standard → S3 Standard-IA → S3 Glacier → Glacier Deep Archive
- 🧹 **Eliminazione automatica** degli oggetti dopo un certo numero di giorni
- 📂 Applicabile su:
  - L’intero bucket
  - Un prefisso (es. `/logs/`)
  - Un tag (es. `project=demo`)
- 📅 Azioni programmabili:
  - Giorni dalla creazione dell’oggetto
  - Giorni dall’ultima versione (per versioning)

---

## ✅ Vantaggi

- ✅ **Riduzione dei costi** automatica e continua
- ✅ Gestione **senza intervento manuale** per grandi volumi di dati
- ✅ Ottimo per **log, backup, archivi**, e dati temporanei
- ✅ Supporto a scenari di **data retention** e conformità

---

## 🚀 Use case comuni

- 🧾 Spostare i log applicativi su **Glacier** dopo 30 giorni
- 🧊 Archiviare immagini non più consultate su **Deep Archive** dopo 180 giorni
- 🗑️ Eliminare automaticamente i backup temporanei dopo 7 giorni
- 📦 Gestire file di grandi dimensioni, poco consultati, con transizione graduale verso storage freddo

---

## 🧪 Esempio di regola Lifecycle

```json
{
  "Rules": [
    {
      "ID": "LogArchiveRule",
      "Prefix": "logs/",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
```

Questa regola sposta i file nella cartella `logs/` in **Glacier dopo 30 giorni** e li **elimina dopo 1 anno**.

---

## 🛠️ Integrazione con altri strumenti

- **S3 Intelligent-Tiering**: alternativa per chi non vuole gestire manualmente il ciclo di vita
- **S3 Storage Lens**: analizza e consiglia ottimizzazioni anche basate sul tempo di accesso
- **Cost Explorer**: verifica i risparmi ottenuti dopo l’attivazione delle regole

---

## 📌 Conclusione

**S3 Lifecycle** è uno strumento potente per **ottimizzare i costi** di archiviazione su AWS, automatizzando la gestione del ciclo di vita dei dati. È ideale per ambienti con grandi quantità di dati che diventano meno rilevanti nel tempo, come **log, backup e archivi storici**.

> “Lascia che S3 gestisca i tuoi dati in modo intelligente: meno accessi, meno costi.”

