--> [AWS](/00-Intro/AWS.md)  -  [Sicurezza](/09-Sicurezza-Compliance-Governance/Sicurezza-Compliance-Governance.md)
# 🛡️ AWS WAF (Web Application Firewall)

## 📘 Cos'è e come funziona

**AWS WAF** è un firewall per applicazioni web progettato per **proteggere le applicazioni da attacchi a livello HTTP/HTTPS (Layer 7)**, come SQL injection, cross-site scripting (XSS), bot, e altri attacchi comuni. 
È completamente gestito e si integra con diversi servizi AWS tra cui:
- **Amazon CloudFront**
- **Application Load Balancer (ALB)**
- **Amazon API Gateway**
- **AWS AppSync**

AWS WAF consente di **definire regole personalizzate** per controllare il traffico web e di applicare rapidamente aggiornamenti alle policy di sicurezza.

---

## ✨ Caratteristiche principali e vantaggi

- 📏 **Filtraggio del traffico HTTP/HTTPS** in base a IP, header, query string, URI, ecc.
- 🧠 **Managed Rule Groups** (regole gestite da AWS o vendor terzi)
- 🛡️ Protezione contro **attacchi OWASP Top 10**
- 🧩 **Integrazione con CloudFront, ALB, API Gateway**
- 🧠 **Bot Control e Account Takeover Prevention** (funzioni avanzate)
- 📊 **Visibilità e monitoraggio** con CloudWatch e AWS WAF logs

### ✅ Vantaggi

- Riduce il rischio di attacchi applicativi come SQL injection e XSS
- Facilita la **compliance** con standard di sicurezza
- È **scalabile** automaticamente e completamente **gestito**
- Permette **implementazione rapida** di protezioni tramite regole preconfigurate
- Offre **protezione specifica per API REST e GraphQL**

---

## 🚀 Use case comuni

- 🧱 Protezione di siti web e applicazioni pubbliche da attacchi noti
- 🔐 Protezione API pubbliche da abuso e accessi non autorizzati
- 🧠 Blocco di bot e crawler malevoli
- 🕵️‍♀️ Monitoraggio e logging del traffico web per audit e analisi
- 🧪 Implementazione di regole temporanee per mitigazione in tempo reale

---

## 💰 Pricing

Il prezzo di AWS WAF si basa su:

- Numero di **WebACL create**
- Numero di **regole attive per ACL**
- Volume di **richieste HTTP analizzate**

---

## 🔄 Confronto con altri servizi AWS

| Servizio AWS             | Differenze rispetto a AWS WAF                                 |
|--------------------------|---------------------------------------------------------------|
| **AWS Network Firewall** | Protezione a livello di rete (Layer 3/4)                      |
| **Security Groups**      | Filtrano solo traffico in ingresso/uscita a livello di istanza |
| **Shield Advanced**      | Protezione DDoS su più livelli, include WAF come componente   |
| **Amazon GuardDuty**     | Rilevamento delle minacce, non filtraggio attivo              |

---

## 📌 Conclusioni

**AWS WAF** è uno strumento essenziale per proteggere le applicazioni esposte su Internet. Offre un approccio flessibile e scalabile per mitigare le principali minacce web, migliorando la sicurezza a livello applicativo senza compromettere le prestazioni.

> “Proteggi il tuo sito non solo dalle intrusioni, ma anche dagli abusi — con AWS WAF.”

