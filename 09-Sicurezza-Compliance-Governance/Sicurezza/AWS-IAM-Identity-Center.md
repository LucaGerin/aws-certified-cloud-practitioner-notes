--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)

# 👤 AWS IAM Identity Center (ex AWS SSO)

## Cos'è e come funziona

**AWS IAM Identity Center** (precedentemente noto come AWS Single Sign-On - SSO) è il servizio AWS che consente la **gestione centralizzata dell'accesso e dell'identità** per utenti e gruppi, sia all'interno di AWS che per applicazioni SaaS esterne.

Con IAM Identity Center puoi fornire agli utenti un **accesso federato e sicuro** a più account AWS (tramite [AWS Organizations](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Organizations.md)), ad applicazioni cloud (es. Salesforce, Microsoft 365), e a risorse locali, il tutto da **una sola console di accesso**.

Può integrarsi con directory esterne come **Active Directory, Okta, Azure AD**, oppure utilizzare la **directory integrata** per gestire utenti e gruppi in modo nativo.

---

## Caratteristiche principali e vantaggi

- **Accesso centralizzato a più account AWS** con ruoli predefiniti e controlli granulari
- **Single Sign-On (SSO)** per l’accesso a molteplici applicazioni cloud compatibili con SAML 2.0
- **Directory integrata o connessa** (Active Directory, IdP esterni via SCIM/SAML)
- **Console di accesso unificata** per utenti finali
- **Provisioning automatico degli utenti** (via SCIM)
- **Integrazione con IAM Roles** per la gestione dei permessi
- **Audit tramite AWS CloudTrail**

---

## Sicurezza

IAM Identity Center migliora la sicurezza grazie a:
- **Autenticazione federata** con supporto per MFA (Multi-Factor Authentication)
- **Gestione centralizzata degli accessi** basata su ruoli
- **Provisioning automatico degli utenti** tramite SCIM, riducendo errori manuali
- **Audit completo** di accessi e attività tramite AWS CloudTrail
- **Controllo granulare delle policy** con integrazione a IAM e AWS Organizations

---

## Pricing

**AWS IAM Identity Center è gratuito**.

Tuttavia:
- Potrebbero esserci **costi per i servizi integrati** (es. CloudTrail, Directory Service, o applicazioni di terze parti).
- Se usi una directory esterna (es. Active Directory su AWS Directory Service), potrebbero esserci **costi aggiuntivi** per quella directory.

---

## Confronto con tecnologie AWS simili

| Servizio | Differenze |
|----------|------------|
| **IAM standard** | IAM gestisce utenti e ruoli all’interno di un singolo account; IAM Identity Center fornisce SSO e gestione utenti centralizzata su più account. |
| **[AWS Organizations](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Organizations.md)** | Organizations organizza e collega più account AWS; IAM Identity Center gestisce chi accede e con quali permessi. |
| **[Cognito](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-Cognito.md)** | Cognito gestisce identità per applicazioni web/mobile (B2C); IAM Identity Center è per l’accesso a risorse aziendali (B2E). |
| **AWS Directory Service** | È una directory gestita (AD o Simple AD); IAM Identity Center può integrarsi con essa per autenticazione e provisioning. |

---

## Conclusione

**AWS IAM Identity Center** è lo strumento ideale per gestire **accessi centralizzati, sicuri e scalabili** in ambienti multi-account AWS e multi-applicazione. Offre un'esperienza utente coerente e un controllo amministrativo avanzato, riducendo la complessità e migliorando la sicurezza.
