--> [AWS](AWS.md)  -  [Prezzo, Fatturazione, Supporto](Prezzo-Fatturazione-Supporto.md)
# 📊 AWS Cost Anomaly Detector

## Cos'è e come funziona

**AWS Cost Anomaly Detector** è un servizio gestito che consente di **identificare automaticamente variazioni anomale nei costi e nell'utilizzo dei servizi AWS**, aiutando a individuare rapidamente spese impreviste o fuori controllo.

Il servizio utilizza **modelli di machine learning** personalizzati in base allo storico di spesa dell'account o dell'organizzazione. 
Dopo aver configurato un “monitor” e una “subscription”, AWS analizza continuamente i dati e invia **notifiche automatiche via email o [Amazon SNS](Amazon-SNS.md)** quando rileva anomalie significative.

## Caratteristiche principali e vantaggi

- ✅ **Monitoraggio automatico dei costi** senza necessità di impostare soglie manuali
- 🤖 **Modelli ML adattivi** che apprendono dai tuoi pattern di spesa
- 📬 **Notifiche proattive** in tempo reale via email o SNS
- 📈 Integrazione con **AWS Cost Explorer** per l’analisi dettagliata delle anomalie
- 🔄 Supporto per **monitoraggio a livello di account, servizio, linked account e tag**

## Use cases

- 🔍 **Rilevamento di errori di configurazione** (es. risorse lasciate attive per errore)
- 🛑 **Prevenzione di spese impreviste** causate da bug o carichi anomali
- 🧾 **Monitoraggio multi-account** in ambienti AWS Organizations
- 🧠 **Supporto al FinOps** per analisi predittive e miglioramento della governance dei costi

## Sicurezza

- Tutti i dati sono **crittografati in transito e a riposo**.
- Il servizio rispetta le policy IAM: puoi controllare **chi può creare, modificare o visualizzare i monitor** e le notifiche.
- Le notifiche possono essere inviate in modo sicuro tramite **Amazon SNS**, anche verso sistemi esterni o integrati in flussi DevOps.

## Confronto con servizi simili in AWS

| Servizio                      | Funzione principale                                      | Differenza principale                                          |
|------------------------------|----------------------------------------------------------|----------------------------------------------------------------|
| [AWS Budgets](AWS-Budgets.md)               | Impostare budget con soglie personalizzate               | Richiede soglie fisse definite manualmente                    |
| [Cost Explorer](AWS-Cost-Explorer.md)       | Analisi grafica e reportistica sui costi                 | Non invia notifiche automatiche in caso di anomalie           |
| [Billing Conductor](Billing-Conductor.md)   | Gestione avanzata della fatturazione per gruppi          | Focalizzato sulla riassegnazione dei costi, non sulle anomalie |

**Cost Anomaly Detector** si distingue per la **capacità predittiva e autonoma** nel rilevare problemi, senza bisogno di configurare soglie o logiche statiche.

## Pricing

**AWS Cost Anomaly Detector è gratuito.** Non ci sono costi per creare monitor o ricevere notifiche.  
Tuttavia, potrebbero esserci **costi per l’uso di Amazon SNS** se vengono inviate notifiche tramite SMS o verso endpoint esterni.

---
