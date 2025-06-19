--> [AWS](AWS.md)  -  [Storage Services](AWS-Storage-Services.md)

# Opzioni di Storage per Amazon EC2

[Amazon EC2](Amazon-EC2.md) fornisce diverse opzioni di **archiviazione dati**, ciascuna con caratteristiche uniche in termini di **prestazioni**, **persistenza** e **casi d’uso**. Queste opzioni sono utilizzabili per ospitare sistemi operativi, database, dati applicativi, backup e molto altro.

---

## Tipi principali di storage per EC2

### 1. [Amazon EBS](Amazon-EBS.md) (Elastic Block Store)

- Archiviazione a blocchi **persistente**, ad alte prestazioni
- Funziona come un disco rigido virtuale collegato a un'istanza EC2
- Può essere **montato su una sola istanza EC2 alla volta**

#### Tipi di volumi EBS

- **gp3 / gp2** – SSD generico: bilanciamento tra prezzo e prestazioni (uso generico)
- **io2 / io1** – SSD con IOPS provisionato: adatto a database e carichi mission-critical
- **st1** – HDD ottimizzato per throughput: grandi volumi di dati sequenziali
- **sc1** – HDD a basso costo: per dati acceduti raramente

---

### 2. [Instance Store](Instance-Store.md) (storage effimero)

- Archiviazione **fisica locale** al server host EC2
- Prestazioni molto elevate, ma **non persistente**
- I dati vengono persi al riavvio o alla terminazione dell’istanza
- Ideale per cache temporanee, buffer e dati transitori

---

### 3. [Amazon EFS](Amazon-EFS.md) (Elastic File System)

- File system **condiviso** accessibile da più istanze EC2 anche in diverse AZ
- **Ridimensionamento automatico** dello spazio in base al contenuto
- Compatibile con protocollo NFSv4, ideale per ambienti distribuiti e containerizzati
- Disponibile anche con tier Infrequent Access per contenere i costi

---

### 4. [Amazon FSx](Amazon-FSx.md)

- File system completamente gestiti per casi d’uso specifici

  - **FSx for Windows File Server** – Compatibile con SMB e Active Directory
  - **FSx for Lustre** – Prestazioni elevate per [HPC](Machine-Learning.md), ML, genomica, rendering
  - **FSx for NetApp ONTAP** – Snapshot, deduplica, compressione avanzata
  - **FSx for OpenZFS** – Affidabile e ottimizzato per ambienti Unix/Linux

---

## 🔍 Confronto sintetico

| Opzione        | Persistenza | Accesso condiviso | Casi d'uso principali                            |
|----------------|-------------|--------------------|--------------------------------------------------|
| Amazon EBS     | ✅           | ❌                 | Sistemi operativi, database, applicazioni        |
| Instance Store | ❌           | ❌                 | Cache, buffer, dati temporanei                   |
| Amazon EFS     | ✅           | ✅                 | Microservizi, container, big data, ambienti CI/CD|
| Amazon FSx     | ✅           | ✅                 | File sharing, Windows, HPC, storage legacy       |

---

## 🧠 Considerazioni

- [Amazon EBS](Amazon-EBS.md) è lo storage più versatile e comunemente utilizzato con EC2.
- [Instance Store](Instance-Store.md) è utile per prestazioni I/O elevate su dati effimeri.
- [Amazon EFS](Amazon-EFS.md) è ideale in contesti multi-istanza e distribuiti.
- [Amazon FSx](Amazon-FSx.md) copre esigenze avanzate di compatibilità (Windows, ONTAP, Lustre).

La scelta migliore dipende da fattori come:  
✅ Necessità di persistenza  
✅ Tipo di carico di lavoro  
✅ Accesso concorrente  
✅ Costo

📎 Per un confronto con S3: [EC2 vs S3 Storage](EC2-storage-vs-S3-storage.md)
