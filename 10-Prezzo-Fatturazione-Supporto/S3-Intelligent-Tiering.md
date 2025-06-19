--> [AWS](AWS.md)  -  [Prezzo, Fatturazione, Supporto](Prezzo-Fatturazione-Supporto.md)
# 🧠 Amazon S3 Intelligent-Tiering

## 📘 Cos'è e come funziona

**Amazon S3 Intelligent-Tiering** è una classe di storage progettata per **ottimizzare automaticamente i costi** quando non si conosce con precisione il **pattern di accesso ai dati**.  

S3 Intelligent-Tiering **sposta automaticamente gli oggetti singoli tra diversi livelli di storage** (detti **tiers**, uno a *frequent access* e uno *infrequent access*) in base alla frequenza di accesso, **senza impatti sulle performance** e **senza dover scrivere policy manuali o Lifecycle rules**.

Il monitoraggio e il tiering avvengono **in background**, ed è particolarmente utile per carichi di lavoro con accesso **imprevedibile o variabile**.

---

## 🧩 Tiers disponibili

| Tier                          | Caratteristiche                             | Destinazione automatica |
|-------------------------------|----------------------------------------------|--------------------------|
| **Frequent Access**           | Default quando un oggetto è caricato         | —                        |
| **Infrequent Access (IA)**    | Dopo 30 giorni senza accesso                 | ✅                        |
| **Archive Instant Access**    | Dopo 90 giorni senza accesso                 | ✅                        |
| **Archive Access**            | Accesso in minuti, costo minimo              | ✅ (facoltativo)         |
| **Deep Archive Access**       | Accesso in ore, costo ancora più basso       | ✅ (facoltativo)         |

> L’utente può **abilitare o disabilitare** i livelli più freddi (Archive e Deep Archive) a seconda delle esigenze.

---

## ✅ Vantaggi

- ✅ **Riduzione automatica dei costi** in base al comportamento reale degli oggetti
- ✅ Nessuna necessità di gestire policy Lifecycle manualmente
- ✅ Nessun impatto sulle performance o disponibilità
- ✅ Ideale per ambienti con **pattern di accesso imprevedibili**
- ✅ Supporta il **monitoraggio dettagliato dell’accesso** con costi contenuti

---

## 💰 Pricing

Il pricing di S3 Intelligent-Tiering si basa su:

- 💾 Costo per GB/mese diverso per ciascun tier
- 🔍 Costo mensile per monitoraggio e tiering automatizzato (gratuito per oggetti < 128 KB)
- 📤 Costi di richiesta e recupero applicabili solo per i livelli *Archive*

---

## 🚀 Use case ideali

- 🧩 Dati con accesso **non prevedibile** (es. file scientifici, media, log compressi)
- 🧪 Data lakes, archivi storici, collezioni non frequentemente consultate
- 🗂️ Progetti in cui i dati vengono caricati e usati sporadicamente nel tempo
- 📦 Organizzazioni che vogliono ridurre i costi senza gestire policy manuali

---

## 🔄 Confronto con altre classi S3

| Classe S3              | Gestione tiering | Costo base | Adatta a |
|------------------------|------------------|------------|----------|
| **Standard**           | Nessuna          | Alto       | Accesso frequente e continuo |
| **Standard-IA / One Zone-IA** | Manuale con Lifecycle | Medio | Dati freddi |
| **Intelligent-Tiering**| Automatizzata    | Dinamico   | Accesso variabile o imprevedibile |
| **Glacier / Deep Archive** | Manuale o Lifecycle | Basso / Molto basso | Archivi a lungo termine |

---

## 📌 Conclusione

**Amazon S3 Intelligent-Tiering** è la soluzione perfetta per chi vuole **ottimizzare i costi di storage senza perdere tempo nella gestione manuale**. Automatizza lo spostamento dei dati tra livelli "hot" e "cold", offrendo **prestazioni costanti**, **risparmi concreti** e **flessibilità totale**.

> “Non sai quando userai i tuoi dati? S3 Intelligent-Tiering lo scopre per te — e ti fa risparmiare.”

