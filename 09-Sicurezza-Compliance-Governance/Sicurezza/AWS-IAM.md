--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# AWS IAM (Identity and Access Management)

## 📘 Cos’è e come funziona

**AWS IAM (Identity and Access Management)** è il servizio di AWS che consente di **gestire in modo sicuro utenti, ruoli, gruppi e permessi** per accedere alle risorse AWS. È uno dei componenti fondamentali per costruire ambienti cloud sicuri e governabili, lavorando in ambito [Sicurezza di AWS](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md).

IAM permette di:
- **Autenticare** identità (utenti, applicazioni, servizi)
- **Autorizzare** l’accesso alle risorse, tramite **policy dettagliate**

IAM è un servizio gratuito, integrato nativamente in ogni account AWS.

**NB:** dando dei permessi si creano delle long-lasting access keys, che vanno attenzionate dal punto di vista della sicurezza in quanto potrebbero portare a vulnerabilità.

![IAM example](/09-Sicurezza-Compliance-Governance/img/iam-example.png)

---

## ✨ Caratteristiche principali e vantaggi

- 👤 **Gestione utenti e gruppi**: crea identità per persone o sistemi con accesso controllato.
- 🧾 **Policy granulari**: definisci cosa può essere fatto, su quali risorse e in quali condizioni.
- 🔁 Permette di definire
	- **Gruppi**: consentono di raggruppare gli utenti e assegnare loro dei permessi tutti assieme.
	- **Ruoli IAM**: consentono accesso **temporaneo** ad **applicazioni, servizi o utenti esterni**.
- 📄 **[IAM Policy Simulator](/09-Sicurezza-Compliance-Governance/Sicurezza/IAM-Policy-Simulator.md)**: verifica l’effetto delle policy prima di applicarle.
- 📜 **Supporto al principio del least privilege**: solo i permessi minimi e necessari.
- 🔐 **Multi-Factor Authentication (MFA)**: aggiunge un ulteriore livello di sicurezza.
- 🧠 **[Access Analyzer](/09-Sicurezza-Compliance-Governance/Sicurezza/IAM-Access-Analyzer.md)**: individua risorse accessibili pubblicamente o da altri account.

---

## 🧾 Permessi granulari: significato e vantaggi

Di default, gli utenti su AWS (a parte *root*) non hanno permessi su nessuna risorsa. 
Dare **permessi granulari** significa concedere accessi **precisi e specifici** alle risorse AWS, limitando ogni utente o ruolo **solo alle azioni strettamente necessarie**, su **singole risorse** o in **contesti ben definiti** (es. solo lettura su un bucket S3, solo scrittura su una tabella DynamoDB, solo da una certa [VPC](/03-CDN-e-Networking/Amazon-VPC.md) o regione).

I vantaggi di usare permessi granulari includono:
- 🔐 Migliore **sicurezza**: riduce la superficie d’attacco
- 🧩 Maggiore **controllo e tracciabilità**
- 🚫 Minori rischi di **errori o abusi accidentali**
- 🛡️ Supporta il principio del **least privilege**

Questa pratica è fondamentale in ambienti cloud complessi, dove un eccesso di permessi può facilmente causare **falle di sicurezza**, **violazioni di compliance** o **perdite di dati**.

Esempio di permesso, in JSON, che permette qualunque azione su un bucket [S3](/02-Storage-services/Amazon-S3.md) e sui file al suo interno:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-s3-bucket",
        "arn:aws:s3:::my-s3-bucket/*"
      ]
    }
  ]
}
```

Le policies IAM possono essere applicate a singoli user o a gruppi di user. Utilizzare i gruppi è in genere una bona idea perchè permette di avere dei gruppicon determinate autorizzazioni a cui aggiungere o togliere utenti, senza dover definire i permessi per ogni singolo utente.

Oltre che a utenti o gruppi, le IAM policies possono essere associate a dei **Ruoli IAM**, che possono essere assunti da utenti o da applicazioni.
Uno dei vantaggi dei ruoli è anche che routano le loro *IAM access keys* automaticamente.

---
## 🚀 Use case comuni/ideali di IAM

- ✅ Creare account separati per team o utenti con permessi limitati
- 🔐 Proteggere l’accesso a S3, EC2, Lambda, DynamoDB, ecc.
- 🔄 Delegare accesso tra servizi AWS (es. EC2 → S3) tramite ruoli
- 🤝 Integrare utenti esterni tramite SAML, OIDC o federazione
- 📊 Auditing e sicurezza tramite CloudTrail + IAM logs

---

## 🧱 Componenti principali

| Componente      | Descrizione                                                                 |
|------------------|------------------------------------------------------------------------------|
| **User**         | Identità per una persona o applicazione con accesso diretto                 |
| **Group**        | Collezione logica di utenti con policy condivise                            |
| **Role**         | Identità temporanea, usata da servizi, applicazioni, utenti esterni         |
| **Policy**       | Documento JSON che definisce i permessi concessi o negati                   |
| **Access Key**   | Coppia chiave pubblica/privata per accesso programmatico                    |
| **STS**          | Servizio per credenziali temporanee (Security Token Service)                |

---

## 🛡️ Best practice IAM

- 🔒 Abilita MFA su root e utenti privilegiati
- ✂️ Applica il principio del minimo privilegio
- 📅 Ruota periodicamente le access key
- 🧪 Usa il Policy Simulator per testare le policy
- 🚫 Evita di usare l’utente root per operazioni quotidiane
- 📊 Monitora l’uso delle policy con **IAM Access Analyzer**

---

## 💰 Pricing

**AWS IAM è gratuito.**
Si paga solo per l’utilizzo dei servizi AWS protetti da IAM, non per la gestione di utenti o policy.

---

## 📌 Conclusioni

**AWS IAM** è il cuore della **sicurezza e del controllo degli accessi** in AWS. Una gestione efficace di IAM è essenziale per costruire ambienti cloud **sicuri, flessibili e governabili**, proteggendo dati e risorse da accessi non autorizzati.

Insieme a AWS IAM, è utile usare un tool come [IAM Access Analyzer](/09-Sicurezza-Compliance-Governance/Sicurezza/IAM-Access-Analyzer.md), che permette di identificare risorse con accesso esterno, validare le policies IAM, e generare policies IAM in base all'uso.

