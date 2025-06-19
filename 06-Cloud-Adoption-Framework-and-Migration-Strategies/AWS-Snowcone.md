--> [AWS](AWS.md)  -  [Migration Strategies](AWS-Migration-Strategies.md)
# ❄️ AWS Snowcone

## 📘 Cos'è e come funziona

**AWS Snowcone** è il dispositivo più piccolo della famiglia [AWS-Snow](AWS-Snow.md), progettato per il **trasferimento e l'elaborazione sicura dei dati** in ambienti remoti, mobili o con connettività limitata. È ideale per scenari dove la portabilità e la resistenza sono fondamentali. 
Supporta anche **funzionalità di edge computing** con [Amazon-EC2](Amazon-EC2.md) e AWS-IoT-Greengrass integrati, permettendo l’elaborazione locale prima del trasferimento in cloud.

![snowcone](snowcone.jpg)

---

## 📦 Caratteristiche principali

- **Peso**: circa 2,1 kg
- **Capacità**: fino a 8 TB di storage SSD utilizzabile
- **Dimensioni**: simili a una lunchbox
- **Sicurezza**: crittografia a 256-bit con chiavi gestite tramite [AWS-KMS](AWS-KMS.md)
- **Resistente**: progettato per ambienti difficili e trasporti intensivi
- **Funziona offline**: perfetto per sedi remote senza accesso Internet
- **Compute integrato**: supporta [Amazon-EC2](Amazon-EC2.md) e AWS-IoT-Greengrass localmente

---

## 🚀 Use case comuni

- **Trasferimento dati** da sedi remote verso [Amazon-S3](Amazon-S3.md)
- **Backup sul campo** per cantieri, ospedali mobili, forze militari
- **Edge computing** in ambienti privi di connessione stabile
- **Data collection** da dispositivi IoT
- **Supporto per droni, spedizioni, ospedali, industria pesante**

---

## 🔧 Funzionalità tecniche

| Funzione                | Dettagli                                |
|-------------------------|-----------------------------------------|
| Storage                 | SSD crittografato, ~8 TB utilizzabili   |
| Compute                 | EC2 (1 vCPU, 4 GB RAM), IoT Greengrass  |
| Connessioni             | Ethernet, USB-C                         |
| Formato                 | Portatile, senza ventole                |
| Energia                 | Compatibile con alimentazione standard o veicoli |

---

## 🔐 Sicurezza

- **Crittografia a 256-bit** always-on
- **Chiavi crittografiche** generate e gestite in [AWS-KMS](AWS-KMS.md)
- **Protezione fisica** contro manomissione
- **Blocco automatico** del dispositivo in caso di furto/sabotaggio
- I dati vengono cancellati automaticamente una volta completato l’upload verso AWS (data wipe)

---

## 💰 Pricing

- Pagamento a **giornata di utilizzo** del dispositivo
- **Spedizione** a carico del cliente (può variare)
- **Importazione dei dati in AWS è gratuita**
- Nessun costo se il dispositivo viene restituito in tempo (entro i 10 giorni gratuiti standard)

---

## 🧪 Flusso tipico di utilizzo

1. Ordina un dispositivo Snowcone da AWS Console
2. Ricevi fisicamente il dispositivo
3. Copia i dati tramite CLI o client (Snowball client)
4. Spedisci il dispositivo ad AWS
5. I dati vengono caricati su [Amazon-S3](Amazon-S3.md)
6. Il dispositivo viene cancellato e pronto per riutilizzo

---

## ✅ Best Practices

- Etichetta e organizza i dati in cartelle logiche per una gestione più semplice
- Crea hash/checksum prima e dopo il trasferimento per validare l’integrità
- Proteggi il dispositivo fisicamente durante l’utilizzo sul campo
- Pianifica il riutilizzo in rotazione se usato in progetti continui

---

## 🔄 Snowcone vs Snowball vs Snowmobile

| Dispositivo   | Capacità           | Portabilità      | Adatto per                 |
|---------------|--------------------|------------------|----------------------------|
| Snowcone      | ~8 TB              | Altissima        | Edge, ambienti remoti      |
| [AWS-Snowball-Edge](AWS-Snowball-Edge.md) Edge | 80–100 TB          | Media            | Migrazioni dati, compute   |
| [AWS-Snowmobile](AWS-Snowmobile.md)    | Fino a 100 PB      | Nessuna (camion) | Data center su larga scala |

---

## 📌 Conclusione

**AWS Snowcone** è la soluzione perfetta per l'**elaborazione e il trasferimento sicuro dei dati** in scenari dove spazio, peso e connettività sono limitati. Sia per backup sul campo, operazioni militari o ambienti industriali, Snowcone porta la potenza del cloud **letteralmente ovunque**.

> “Quando il cloud deve andare dove nessuna rete arriva, Snowcone è la risposta.”
