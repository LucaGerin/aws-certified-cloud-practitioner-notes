--> [AWS](/00-Intro/AWS.md)  -  [Prezzo, Fatturazione, Supporto](/10-Prezzo-Fatturazione-Supporto/Prezzo-Fatturazione-Supporto.md)
# 🧾 AWS Billing Conductor

## 📘 Cos'è e come funziona

**AWS Billing Conductor (ABC)** è un servizio che consente di **personalizzare la presentazione dei costi e dell’utilizzo tra account AWS**. È pensato per organizzazioni che usano **[AWS Organizations](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Organizations.md)** e desiderano gestire la **fatturazione interna** in modo più flessibile e trasparente.

Con Billing Conductor, puoi creare delle **"billing groups"** (gruppi di account), applicare **prezzi personalizzati**, ridefinire l’allocazione dei costi e generare **report dettagliati di showback e chargeback**, senza influenzare la fatturazione ufficiale da AWS verso l'account principale.

---

## ✨ Caratteristiche principali

- 🧑‍💼 **Billing Groups**: raggruppa più account per gestirli insieme
- 🧾 **Rate & Pricing Models**: definisci tariffe personalizzate o sconti interni
- 📦 **Line Item Adjustments**: modifica la presentazione di singole voci di costo
- 📊 **Usage and Cost Reports personalizzati**: visione filtrata dei costi per gruppo
- 🔐 Non influisce sulla **fatturazione reale AWS**: è solo a fini interni

---

## ✅ Vantaggi

- ✅ Supporta **showback/chargeback accurato** tra team, dipartimenti o clienti
- ✅ Crea **modelli di pricing interni** realistici e trasparenti
- ✅ Aiuta MSP e reseller a **comunicare costi chiari** ai clienti
- ✅ Semplifica la **rendicontazione multi-account**
- ✅ Integra con **AWS Cost and Usage Reports (CUR)**

---

## 🚀 Use case comuni

- 🧮 Chargeback interno verso dipartimenti aziendali
- 📈 Showback per analisi FinOps e responsabilizzazione dei team
- 🧾 MSP e rivenditori che vogliono rappresentare prezzi custom ai clienti
- 🧩 Divisione dei costi tra ambienti di sviluppo, test e produzione

---

## 💰 Pricing

- **Servizio gratuito**
- Paghi solo per l'uso dei servizi sottostanti (es. S3 per esportazione dati, CUR, ecc.)

---

## 🛠️ Come si configura

1. Attiva **AWS Organizations** e **Cost and Usage Reports (CUR)**
2. Accedi a Billing Conductor da console AWS
3. Crea i tuoi **Billing Groups** e definisci le regole di pricing
4. Visualizza o esporta i **report personalizzati**

---

## 🔄 Integrazione con altri strumenti AWS

| Strumento                    | Integrazione |
|-----------------------------|--------------|
| **[AWS Organizations](/09-Sicurezza-Compliance-Governance/Compliance-e-Governance/AWS-Organizations.md)**       | Gestione multi-account e OU                    |
| **[AWS Cost and Usage Reports (CUR)](/10-Prezzo-Fatturazione-Supporto/AWS-Cost-and-Usage-Reports.md)** | Fonte dei dati di costo e utilizzo           |
| **[AWS Budgets](/10-Prezzo-Fatturazione-Supporto/AWS-Budgets.md)**             | Allerta sui budget definiti per billing group |
| **[AWS Cost Explorer](/10-Prezzo-Fatturazione-Supporto/AWS-Cost-Explorer.md)**       | Analisi delle spese personalizzate             |

---

## 📌 Conclusione

**AWS Billing Conductor** è uno strumento avanzato per la **personalizzazione e la gestione interna della fatturazione AWS**, utile per aziende complesse, MSP e ambienti multi-team. Offre trasparenza, controllo e flessibilità nella distribuzione e comunicazione dei costi cloud.

> “Con Billing Conductor, la tua fattura interna riflette la realtà della tua organizzazione.”

