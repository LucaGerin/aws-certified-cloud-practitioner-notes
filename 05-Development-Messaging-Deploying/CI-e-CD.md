--> [AWS](/00-Intro/AWS.md)  -  [Development, Messaging, and Deployment](/05-Development-Messaging-Deploying/Development-Messaging-and-Deployment.md)
# Introduzione a CI/CD

## Cos'è CI/CD?

**CI/CD** è l'acronimo di **Continuous Integration** e **Continuous Delivery/Deployment**, una pratica DevOps che automatizza le fasi di integrazione, testing e rilascio del software. L’obiettivo è **aumentare la velocità di sviluppo**, **ridurre gli errori** e **garantire qualità costante** nel software distribuito.

![CI e CD](CI-CD.png)

---

## Continuous Integration (CI)

### Definizione

La **Continuous Integration** è la pratica di integrare frequentemente (di solito più volte al giorno) le modifiche al codice in un repository condiviso, dove vengono automaticamente compilate e testate.

### Obiettivi

- Rilevare bug precocemente
- Evitare "integration hell"
- Avere sempre un build funzionante
- Promuovere collaborazione continua tra sviluppatori

### Elementi chiave

- Repository centralizzato (es. Git)
- Build automatici (es. AWS CodeBuild, Jenkins)
- Test automatizzati (unitari, di integrazione)
- Feedback immediato

---

## Continuous Delivery (CD)

### Definizione

La **Continuous Delivery** estende la CI includendo l'automazione del processo di rilascio del software fino all'ambiente di staging o pre-produzione. Il rilascio in produzione può avvenire con un'azione manuale.

### Benefici

- Rilasci rapidi e frequenti
- Riduzione del rischio di errore umano
- Ambiente sempre pronto per la produzione

---

## Continuous Deployment

### Definizione

La **Continuous Deployment** è un ulteriore passo oltre la Continuous Delivery: ogni modifica che supera i test viene **rilasciata automaticamente in produzione** senza intervento umano.

### Quando usarla

- In ambienti cloud-native e altamente automatizzati
- Con test e rollback robusti
- Per prodotti che richiedono aggiornamenti frequenti

---

## Pipeline CI/CD

Una pipeline CI/CD è una **catena automatizzata** di fasi che includono:

1. **Commit** del codice nel repository
2. **Build** e compilazione
3. **Test automatici**
4. **Deploy in staging** (Continuous Delivery)
5. **Deploy in produzione** (Continuous Deployment)

Esempio di pipeline:

```plaintext
[Developer Commit]
      ↓
[Build & Unit Test]
      ↓
[Integration Test]
      ↓
[Staging Deploy]
      ↓
[Production Deploy]
```
