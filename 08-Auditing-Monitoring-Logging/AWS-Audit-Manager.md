--> [AWS](00-Intro/AWS.md)  -  [Auditing, Monitoring, Logging](08-Auditing-Monitoring-Logging/Auditing-Monitoring-Logging.md)
# 🛡️ AWS Audit Manager

## 📘 Cos’è e come funziona

**AWS Audit Manager** è un servizio gestito che aiuta le organizzazioni a **preparare audit di conformità** in modo continuo e automatico. 
Automatizza la raccolta delle **evidenze necessarie per soddisfare requisiti normativi**, framework di sicurezza o standard interni, riducendo il carico manuale associato agli audit.

Audit Manager lavora integrandosi con altri servizi AWS (come **CloudTrail**, **Config**, **Security Hub**, **IAM**, ecc.) per raccogliere in tempo reale **prove oggettive** delle attività e configurazioni effettuate nel tuo ambiente cloud.

Audit manager centralizza i dati di audit da AWS Config e dai servizi di sicurezza.
Trova le cause alla radice della non compliance e genera reports.

Include anche dei framework di auditing pre-costruiti.

---

## ✨ Caratteristiche principali e vantaggi

- 📚 **Framework integrati** pronti all’uso (es. GDPR, ISO 27001, SOC 2, HIPAA, NIST 800-53)
- 🔄 **Raccolta automatica delle evidenze** da oltre 50 servizi AWS
- 🛠️ **Framework personalizzati** per le policy aziendali interne
- 📁 **Dashboard e report di conformità** organizzati per controllo
- 🔗 **Collegamento diretto a risorse e metadati** (es. chi ha fatto cosa, quando)
- 📆 **Tracciamento cronologico** delle evidenze raccolte

---

## 🧩 Come funziona

1. **Scelta del framework di conformità** (predefinito o personalizzato)
2. **Creazione di un assessment (valutazione)** basata su quel framework
3. **Audit Manager raccoglie automaticamente le evidenze tecniche** da AWS
4. Gli utenti possono allegare **evidenze manuali** (es. documenti, policy esterne)
5. I risultati vengono **organizzati per controllo** e sono pronti per l'audit formale

> 🛠️ Le evidenze vengono tracciate e versionate nel tempo, per garantire **integrità e affidabilità** durante tutto il ciclo di vita di un audit.

![Audit manager](audit-manager.png)

---

## 🚀 Use case comuni

- ✅ **Preparazione automatica per certificazioni** (SOC 2, ISO 27001, PCI-DSS, ecc.)
- 🧾 **Gestione continua della conformità** in ambienti multi-account
- 📄 **Riduzione del lavoro manuale** nella raccolta di prove tecniche
- 📋 **Supporto a team di sicurezza, governance, risk e compliance**
- 🔒 **Integrazione in flussi DevSecOps**

---

## 💰 Pricing

Il costo di AWS Audit Manager si basa su:

- **Numero di controlli attivi per account al mese**
- **Evidenze raccolte automaticamente**
- **Framework attivi**

Prezzo base:
- ~$1.50 per controllo attivo per account al mese
- ~Costo aggiuntivo per esportazione o uso avanzato


---

## 🔄 Integrazione con altri servizi AWS

| Servizio             | Integrazione                                      |
|----------------------|---------------------------------------------------|
| **CloudTrail**       | Traccia le attività API per evidenze operative    |
| **AWS Config**       | Fornisce lo storico delle configurazioni risorse  |
| **IAM**              | Raccoglie policy, permessi e ruoli                |
| **Security Hub**     | Evidenze relative alla postura di sicurezza       |
| **S3**               | Archiviazione documenti e evidenze manuali        |

---

## 📌 Conclusioni

**AWS Audit Manager** consente di trasformare il processo di auditing da reattivo a **continuo e automatizzato**, facilitando la conformità con le normative e riducendo i tempi, i costi e gli errori umani nella raccolta delle evidenze. È uno strumento essenziale per chi deve dimostrare affidabilità, sicurezza e governance nel cloud AWS.

> “Con Audit Manager, l’audit non è più un evento: diventa un processo continuo.”
