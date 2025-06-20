--> [AWS](00-Intro/AWS.md)  -  [Storage Services](02-Storage-services/AWS-Storage-Services.md)
# Differenza tra EC2 Storage e Amazon S3

Capire la differenza tra lo **storage di EC2** e **Amazon S3** è fondamentale per progettare un'infrastruttura cloud efficiente. Di seguito un confronto chiaro e dettagliato.

---

## 📦 1. Tipologia di storage

|Aspetto|EC2 ([EBS](02-Storage-services/Amazon-EBS.md) / Instance Store / EFS)|Amazon S3|
|---|---|---|
|**Tipo di storage**|Blocco (EBS), File (EFS), Temporaneo (Instance Store)|Oggetti (Object Storage)|
|**Accesso**|Montato su istanza EC2 (via file system)|Tramite API, SDK o URL|
|**Persistenza**|EBS/EFS: sìInstance Store: no|Sì|
|**Condivisione tra istanze**|EBS: noEFS: sìInstance Store: no|Sì (globale, pubblico/privato configurabile)|

---

## 🛠️ 2. Uso tipico

|Caso d’uso|EC2 Storage|Amazon S3|
|---|---|---|
|Disco per sistema operativo|✅ (EBS)|❌|
|Database|✅ (EBS con IOPS elevati)|❌ (non adatto a I/O randomico frequente)|
|File system condiviso|✅ (EFS)|❌ (non è un file system nativo)|
|Backup / archiviazione|⚠️ (possibile, ma costoso)|✅ (ottimale e a basso costo)|
|Upload/download file|❌|✅|
|Big data / data lake|⚠️ (possibile con EBS + Hadoop)|✅ (ideale con Athena, Glue, EMR)|
|Hosting sito statico|❌|✅|

---

## 💡 Differenze chiave in sintesi

|Fattore|EC2 Storage|Amazon S3|
|---|---|---|
|**Granularità**|Blocchi/dischi/file|Oggetti (con metadati)|
|**Accesso**|Montato (mount point)|HTTP/HTTPS via API|
|**Performance**|Più adatto a I/O basso-latenza|Ottimo per throughput sequenziale|
|**Scalabilità automatica**|❌ Manuale o configurata (Auto Scaling)|✅ Automatica|
|**Costo**|Più alto (soprattutto per IOPS)|Più economico (specialmente Glacier)|
|**Persistenza**|Sì (EBS/EFS), No (Instance Store)|Sì (alta durabilità: 11 9s)|

---

## ✅ Quando usare cosa?

|Hai bisogno di...|Usa...|
|---|---|
|Un disco persistente per EC2|Amazon EBS|
|Un file system condiviso tra istanze EC2|Amazon EFS|
|Storage temporaneo e veloce|Instance Store|
|Archiviazione di backup, log, immagini, media, big data|Amazon S3|
|Accesso globale e scalabilità illimitata|Amazon S3|

---

Amazon S3 e gli storage EC2 (EBS, [EFS](02-Storage-services/Amazon-EFS.md), Instance Store) rispondono a esigenze molto diverse. La scelta giusta dipende da: **tipo di dati, frequenza di accesso, performance richieste, costi e condivisione tra istanze**.