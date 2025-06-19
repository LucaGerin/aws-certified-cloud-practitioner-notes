--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🖥️ AWS Systems Manager Session Manager

## Cos'è e come funziona

**AWS Systems Manager Session Manager** è una funzionalità di **AWS Systems Manager** che consente di stabilire sessioni interattive sicure con le istanze EC2 (e non solo) **senza dover aprire porte, gestire chiavi SSH o accedere tramite bastion host**.

Le connessioni avvengono tramite la console AWS, la CLI o SDK, usando il protocollo HTTPS e sfruttando le policy IAM per controllare l'accesso. Session Manager consente così di eseguire comandi e script in tempo reale sulle istanze Linux e Windows, migliorando il controllo operativo e la sicurezza.

---

## Caratteristiche principali e vantaggi

- **Nessun accesso pubblico o SSH necessario**: elimina la necessità di porte aperte (come la 22 o la 3389).
- **Controllo basato su IAM**: gli accessi sono gestiti con policy granulari.
- **Audit completo con AWS CloudTrail e Amazon S3**: ogni sessione può essere tracciata, registrata e conservata.
- **Supporto multi-account e multi-regione**: utile in ambienti distribuiti e su larga scala.
- **Integrazione con Systems Manager Automation e Run Command**: migliora l’automazione e la gestione remota.

---

## Sicurezza

Session Manager migliora significativamente la postura di sicurezza:
- Elimina la necessità di **chiavi SSH** o **bastion host**.
- Le sessioni sono **crittografate** end-to-end.
- Le attività possono essere tracciate tramite **CloudTrail**, con output registrato su **Amazon S3** e/o **CloudWatch Logs**.
- L'accesso può essere limitato per utente, istanza, tag o tempo.

---

## Pricing

**AWS Session Manager è gratuito** come parte di **AWS Systems Manager**.

Tuttavia, potrebbero esserci costi associati ai servizi integrati:
- **CloudWatch Logs** per il log delle sessioni
- **Amazon S3** per l’archiviazione dell’output
- **AWS KMS** per la crittografia dei log, se utilizzata

---

## Confronto con tecnologie AWS simili

| Servizio | Differenze |
|----------|------------|
| **EC2 Instance Connect** | Richiede comunque l'accesso via SSH; Session Manager non lo fa. |
| **SSH tradizionale con bastion host** | Meno sicuro e più complesso da gestire rispetto a Session Manager. |
| **AWS Systems Manager Run Command** | Esegue comandi remoti senza aprire una sessione interattiva. Session Manager invece permette una shell interattiva. |
| **SSM Automation** | Utilizzato per flussi predefiniti; Session Manager è utile per interventi manuali in tempo reale. |

---

## Conclusione

**Session Manager** è uno strumento potente e sicuro per accedere e gestire istanze EC2 e altri nodi gestiti, eliminando completamente la necessità di infrastrutture di accesso remoto tradizionali. È ideale per ambienti con forti requisiti di sicurezza, compliance e auditabilità.
