--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🗂️ AWS Systems Manager Parameter Store

## 📘 Cos'è e come funziona

**AWS Systems Manager Parameter Store** è una funzionalità di **AWS Systems Manager** che permette di **archiviare e gestire in modo sicuro parametri di configurazione e segreti**, come variabili di ambiente, stringhe di connessione, ID API o chiavi crittografate.

I parametri possono essere semplici (plaintext) oppure protetti con **AWS KMS**. Sono accessibili da istanze EC2, Lambda, container, script e altre risorse, tramite **API, CLI o SDK AWS**, in modo sicuro e centralizzato.

---

## ✨ Caratteristiche principali e vantaggi

- 🔐 **Gestione sicura dei parametri**, con supporto alla crittografia (SecureString)
- 🔍 **Versionamento automatico** dei parametri
- 📅 **Audit e logging** con AWS CloudTrail
- 🔁 **Accesso programmatico** tramite API, SDK e CLI
- 📦 **Supporto a tag, path e gerarchie** per organizzare i parametri
- 🧩 **Integrazione con EC2, ECS, Lambda, CloudFormation e CodePipeline**

### ✅ Vantaggi

- Elimina l’hardcoding delle configurazioni nelle applicazioni
- Migliora la sicurezza nella gestione di segreti e chiavi
- Favorisce il deployment continuo (CI/CD) e la configurazione dinamica
- Accesso controllato tramite **IAM** (identity-based e resource-based policies)

---

## 🔑 Tipi di parametri

| Tipo           | Descrizione                                                 |
|----------------|-------------------------------------------------------------|
| **String**     | Valore in testo semplice                                    |
| **StringList** | Lista separata da virgole (utile per elenchi o whitelist)   |
| **SecureString** | Valore crittografato con AWS KMS                           |

---

## 🚀 Use case comuni

- 🔧 Gestione di **variabili di ambiente** per applicazioni Lambda o EC2
- 🔑 Archiviazione sicura di **token API o password**
- 🧪 Fornitura di configurazioni dinamiche per test e ambienti CI/CD
- 🛠️ Condivisione centralizzata di parametri tra team e microservizi
- 🧭 Parametrizzazione dei template CloudFormation o Terraform

---

## 💰 Pricing

- ✅ **Parametri standard**: gratuiti fino a 10.000 parametri.
- 💰 **Parametri avanzati**: a pagamento, includono maggiore capacità, TTL, notifiche, politiche di retention.
- 💡 **Crittografia con KMS**: soggetta ai costi di AWS KMS.


---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS              | Differenze rispetto a Parameter Store                           |
|---------------------------|------------------------------------------------------------------|
| **AWS Secrets Manager**   | Ottimizzato per gestire segreti con rotazione automatica         |
| **AWS KMS**               | Gestisce le chiavi, non i valori configurabili o segreti         |
| **AppConfig**             | Distribuzione controllata di configurazioni, ma dipende da Parameter Store|

---

### 🔍 Differenze principali con [Secrets Manager](AWS-Secrets-Manager.md)

| Caratteristica                  | Parameter Store                              | Secrets Manager                                      |
|--------------------------------|----------------------------------------------|------------------------------------------------------|
| **Scopo principale**           | Gestione di parametri e configurazioni       | Gestione e rotazione automatica di segreti          |
| **Rotazione automatica**       | ❌ Non supportata                             | ✅ Supportata (nativamente con Lambda)               |
| **Supporto a DB (RDS, ecc.)**  | ❌ No                                         | ✅ Sì, integrazione con RDS, Redshift, DocumentDB    |
| **Versionamento**              | ✅ Sì                                         | ✅ Sì                                                 |
| **Crittografia con KMS**       | ✅ Sì (SecureString)                          | ✅ Sì (default abilitato)                            |
| **Politiche di accesso IAM**   | ✅ Sì                                         | ✅ Sì                                                 |
| **Supporto a TTL, tag avanzati**| ✅ Solo con parametri avanzati               | ✅ Sì                                                 |
| **Interfaccia utente**         | Parte di Systems Manager                     | Servizio dedicato                                    |
| **Costo**                      | ✅ Gratuito per parametri standard (fino a 10.000) | 💰 A pagamento (per segreto/mese + chiamate API) |

---

## 📌 Conclusioni

**AWS Systems Manager Parameter Store** è uno strumento essenziale per la gestione **centralizzata, sicura e scalabile** dei parametri e delle configurazioni delle applicazioni. È una soluzione leggera e versatile per evitare l’hardcoding e migliorare l’agilità operativa e la sicurezza dei tuoi workload.

> “Configurazioni centralizzate, segreti protetti, deploy più intelligenti.”

