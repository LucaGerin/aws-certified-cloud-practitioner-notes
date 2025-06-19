--> [AWS](app://obsidian.md/AWS.md) - [Compliance e Governance](Sicurezza-Compliance-Governance.md)
# 🏢 AWS Organizations

## 📘 Cos'è e come funziona

**AWS Organizations** è un servizio gratuito che consente di **gestire centralmente più account AWS**, automatizzando la governance, la sicurezza e la conformità attraverso un’unica struttura gerarchica.  

Grazie a Organizations è possibile **creare e organizzare account** in **unità organizzative (OUs)**, applicare **policy centralizzate**, condividere risorse tra accounts e allo stesso tempo limitare l'accesso alle risorse divise tra accounts, e abilitare servizi cross-account come **consolidated billing**, **[SCPs](AWS-Service-Control-Policies.md)**, **Firewall Manager**, **[Security Hub](AWS-Security-Hub.md)**, e molti altri.

![Organization](organization.png)

-  Una Organizational Unit (OU) può avere solo un parent
- Un account può appertenere e essere associato a solo una Organizational Unit (OU) alla volta

---

## 🧩 Caratteristiche principali e vantaggi

- 🏗️ **Struttura gerarchica personalizzabile** di account e OUs
- 💰 **Fatturazione consolidata** per tutti gli account
- 🛡️ **Service Control Policies (SCPs)** per limitare azioni IAM a livello account o OU
- 🔄 **Automazione della creazione account** tramite API e CloudFormation StackSets
- 📦 Integrazione con servizi di sicurezza come **Firewall Manager**, **Config**, **Security Hub**, **GuardDuty**, ecc.
- 🧾 Migliore gestione di **compliance e auditing multi-account**
- 📍 Supporto per **AWS Control Tower**, per ambienti multi-account gestiti

---

## ✅ Vantaggi

- ✅ **Centralizzazione della governance e delle policy**
- ✅ **Controllo granularizzato** sugli accessi e sulle azioni possibili per ciascun account
- ✅ **Separazione dei workload** (produzione, sviluppo, test) in ambienti isolati
- ✅ **Ottimizzazione dei costi** grazie alla fatturazione consolidata
- ✅ **Miglior conformità** ai requisiti aziendali e normativi
- ✅ **Sicurezza migliorata** attraverso SCP e ruoli di accesso cross-account

---

## 🚀 Use case comuni

- 🏢 Gestione multi-account per aziende con team separati o workload diversi
- 🧪 Separazione ambienti di test/dev/prod in account distinti
- 🔐 Implementazione di policy di sicurezza centralizzate (non modificabili da dentro gli accounts!)
- 💼 Consolidamento delle spese e report di utilizzo per ciascun account
- 🛠️ Automazione nella creazione e configurazione degli account via API
- Applicazione di Config Rules a tutte le risorse dell'organizzazione o a gruppi di accounts, non solo a singoli acconts

---

## 💰 Pricing

**AWS Organizations è gratuito**.  
Tuttavia, i servizi che **si integrano** con Organizations (es. GuardDuty, Config, Security Hub, ecc.) possono avere costi associati.


---

## 🔄 Confronto con altri strumenti AWS

| Servizio AWS         | Differenze rispetto a AWS Organizations                             |
|----------------------|-----------------------------------------------------------------------|
| **IAM**              | Gestisce identità all’interno di un singolo account                  |
| **Control Tower**    | Usa Organizations per creare e gestire ambienti multi-account con automazione |
| **Firewall Manager** | Applica policy di sicurezza cross-account solo con Organizations     |
| **Billing console**  | Mostra costi, ma non centralizza gestione policy o account           |

---

## 📌 Conclusioni

**AWS Organizations** è lo strumento fondamentale per chi gestisce ambienti multi-account in AWS. Permette di unire flessibilità, separazione dei carichi e **governance centralizzata**, facilitando la **scalabilità, la sicurezza e la conformità** dell’infrastruttura cloud.

> “Organizzare gli account è il primo passo per costruire un cloud aziendale sicuro e scalabile.”

