--> [AWS](AWS.md)  -  [Sicurezza](Sicurezza-Compliance-Governance.md)
# 🔒 AWS Service Control Policies (SCPs)

## 📘 Cos'è e come funziona

Le **Service Control Policies (SCPs)** sono delle policies a livello organizzativo, uno strumento chiave di **governance** all’interno di **AWS Organizations**, che permettono di **definire limiti ai permessi IAM** a livello di **account o unità organizzative (OU)**.

Una SCP **non concede permessi**, ma **limita l’insieme massimo delle azioni** che gli utenti e i ruoli IAM possono eseguire in un determinato account. Gli utenti devono **avere sia il permesso IAM che essere autorizzati dalla SCP** per poter eseguire un’azione.

---

## 🧩 Caratteristiche principali e vantaggi

- 🔐 **Controllo centralizzato** su ciò che gli account possono o non possono fare
- 🧱 **Imposizione di restrizioni forti** anche ai ruoli con privilegi elevati (incluso root)
- 🏢 Applicabili a **interi rami** della gerarchia di AWS Organizations (OU o account singoli)
- 🚫 Supporto a policy di tipo **"deny" esplicito o allow controllato**
- 🔄 **Policy JSON simili a quelle IAM**, ma con effetti a livello globale
- 🌍 Possibilità di limitare accessi per **regione, servizio, azione o risorsa**

---

## ✅ Vantaggi

- Migliora la **sicurezza** e previene l’uso involontario o malevolo di servizi
- Aiuta a garantire la **conformità normativa o aziendale**
- Permette di **bloccare servizi non approvati** (es. solo S3 e Lambda ammessi)
- Centralizza le policy senza doverle replicare in ogni account
- Utile per **bloccare azioni pericolose**, come la cancellazione di log o la disattivazione della MFA

---

## 🚀 Use case comuni

- ⛔ Bloccare l’uso di regioni AWS non autorizzate (es. `eu-west-1` only)
- 📦 Limitare gli account di sviluppo a pochi servizi approvati
- 🛡️ Impedire la disattivazione di AWS CloudTrail o la rimozione di bucket S3 log
- 🔄 Forzare l’uso del customer-managed KMS per l’encryption
- 💼 Applicare standard di sicurezza a tutta l'organizzazione (es. MFA obbligatoria)

---

## 💡 Esempio di SCP

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "s3:DeleteBucket",
      "Resource": "*"
    }
  ]
}
```

👉 Questa SCP **impedisce a chiunque di eliminare bucket S3**, anche se ha i permessi IAM per farlo.

---

## 📋 Considerazioni importanti

- Le SCP **non si applicano all’account root dell'organizzazione**
- Le SCP **funzionano solo su account all’interno di AWS Organizations**
- Le **SCP non hanno effetto** se l’account o l’OU non ha SCP abilitate
- Le **azioni negate con SCP** sovrascrivono qualsiasi permesso IAM

---

## 💰 Pricing

**Le SCP sono parte gratuita di AWS Organizations.** Non comportano costi diretti, ma possono influenzare l'uso di servizi che hanno costi (es. negare servizi a pagamento).

---

## 📌 Conclusioni

Le **Service Control Policies** rappresentano un potente meccanismo per garantire che gli account AWS operino entro i confini stabiliti dall’organizzazione. Consentono di imporre standard di sicurezza, prevenire errori e rafforzare la governance in ambienti multi-account.

> “Con le SCP puoi dire non solo *chi può fare cosa*, ma anche *cosa nessuno può fare* — nemmeno per errore.”

