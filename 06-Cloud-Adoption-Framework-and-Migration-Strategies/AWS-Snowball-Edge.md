--> [AWS](AWS.md)  -  [Migration Strategies](AWS-Migration-Strategies.md)
# AWS Snowball

**AWS Snowball** è un dispositivo fisico fornito da Amazon Web Services progettato per trasferimenti di dati su larga scala in modo sicuro ed efficiente. Fa parte della famiglia di servizi [AWS-Snow](AWS-Snow.md) (insieme a [AWS-Snowcone](AWS-Snowcone.md) e [AWS-Snowmobile](AWS-Snowmobile.md)) e viene utilizzato principalmente per spostare grandi quantità di dati verso o da AWS, specialmente quando la larghezza di banda di rete è limitata o il trasferimento online sarebbe troppo lento o costoso.

![snowball](snowball.jpeg)

---

## 🧊 Caratteristiche principali

- **Alta capacità**: può trasferire fino a **80 TB (Snowball Edge Storage Optimized)** per dispositivo.
- **Resistente e sicuro**: progettato per resistere a urti e vibrazioni, con protezione fisica e crittografia integrata.
- **Crittografia dei dati**: usa la crittografia **AES-256** e le chiavi di crittografia sono gestite tramite [AWS-KMS](AWS-KMS.md).
- **Import/export offline**: ideale per grandi volumi di dati da caricare su [Amazon-S3](Amazon-S3.md) o scaricare da esso.
- **Edge computing**: alcune versioni di Snowball (come **Snowball Edge**) supportano l'esecuzione di applicazioni locali tramite [AWS-Lambda](AWS-Lambda.md) o [Amazon-EC2](Amazon-EC2.md).

---

## 📦 Tipi di Snowball

| Nome dispositivo          | Capacità (fino a) | Funzionalità principali                             |
|---------------------------|-------------------|-----------------------------------------------------|
| Snowball Edge Storage     | 80 TB             | Trasferimento dati, NFS, edge computing             |
| Snowball Edge Compute     | 42 TB             | Edge computing con GPU opzionale                    |
| [AWS-Snowcone](AWS-Snowcone.md)          | 8 TB              | Ultra portatile, alimentabile tramite batteria USB  |
| [AWS-Snowmobile](AWS-Snowmobile.md)      | 100 PB            | Trasferimento a livello exabyte tramite camion      |

---

## 🔁 Come funziona

1. **Ordina** un dispositivo tramite la console AWS.
2. **AWS spedisce** il dispositivo fisico all'indirizzo specificato.
3. **Carica i dati** sul dispositivo tramite software locale (Snowball Client o NFS).
4. **Spedisci il dispositivo** ad AWS tramite corriere.
5. **AWS carica i dati** nel tuo bucket [Amazon-S3](Amazon-S3.md).
6. **I dati vengono cancellati** automaticamente dal dispositivo al termine del caricamento.

---
### 🏭 AWS Snowball Edge come storage locale

Anche se **AWS Snowball Edge** è noto principalmente per il **trasferimento dati offline** (spedizione fisica verso AWS), può anche essere utilizzato come **dispositivo di storage e calcolo locale** in ambienti remoti o con connettività limitata, come fabbriche, impianti industriali o basi isolate.

In questo contesto, Snowball Edge può essere **collegato alla rete locale** e fungere da **NAS (Network Attached Storage)**, consentendo a dispositivi e server di **scrivere dati direttamente sul dispositivo** utilizzando protocolli standard.  
Il protocollo supportato per il trasferimento file è **NFSv3 (Network File System versione 3)**, che garantisce compatibilità con molteplici sistemi IoT e industriali.

Questa funzionalità permette di:
- ✅ Raccogliere e archiviare localmente dati da sensori e sistemi industriali
- ⚙️ Eseguire analisi o preprocessing direttamente sul dispositivo
- 🚚 Spedire i dati successivamente ad AWS in modo sicuro e ad alta capacità

> 📌 In sintesi: Snowball Edge **non è solo per l'import/export dati**, ma può operare come **infrastruttura edge completa**, compatibile con protocolli come **NFSv3** per l'integrazione in rete locale.


---

## 🛠️ Casi d'uso

- Migrazione iniziale a AWS
- Backup e archiviazione offline
- Raccolta dati da ambienti remoti (come navi o cantieri)
- Elaborazione dati in ambienti con connettività limitata

---

## 🔐 Sicurezza

- Tutti i dati sono crittografati automaticamente durante il trasferimento.
- Le chiavi non sono memorizzate nel dispositivo.
- Il dispositivo si autodistrugge in caso di manomissione rilevata.

---

> ⚠️ **Nota:** AWS Snowball è pensato per trasferimenti su larga scala. Per trasferimenti minori, soluzioni come AWS-DataSync o AWS-Transfer-Family potrebbero essere più adatte.
