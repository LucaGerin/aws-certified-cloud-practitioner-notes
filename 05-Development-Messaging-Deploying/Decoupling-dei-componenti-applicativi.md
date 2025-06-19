--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# Decoupling dei Componenti nelle Architetture Software

Il **decoupling** (disaccoppiamento) è una pratica architetturale che consiste nel ridurre le dipendenze dirette tra i componenti di un'applicazione, facilitando così la scalabilità, la manutenibilità e la resilienza del sistema.

---

## 🎯 Obiettivi del decoupling

- Rendere i componenti **indipendenti** tra loro
- Facilitare il **rilascio autonomo** dei moduli
- Ridurre il rischio di **cascading failure**
- Aumentare la **riusabilità del codice**
- Supportare **team distribuiti** su domini funzionali diversi

---

## 🔁 Tight Coupling vs Loose Coupling

| Caratteristica              | Tight Coupling                           | Loose Coupling                              |
|----------------------------|------------------------------------------|---------------------------------------------|
| Dipendenza                 | Alta                                     | Bassa                                       |
| Impatti ai cambiamenti     | Cambiare un componente impatta gli altri | Cambiamenti isolati                         |
| Testabilità                | Difficile da isolare                      | Più facile                                  |
| Esempio                    | Metodo che chiama direttamente un altro  | Comunicazione via coda/evento/notifica      |

### ❌ Tight Coupling

> Esempio: un servizio che istanzia e chiama direttamente un altro modulo con conoscenza della sua implementazione.

### ✅ Loose Coupling

> Esempio: un servizio che invia un messaggio a una coda, senza sapere chi lo consumerà.

---

## 🧩 Approcci di Integrazione tra Componenti

Esistono diversi modi per integrare i componenti di un sistema mantenendo un basso accoppiamento:

### 1. 📦 **Integrazione tramite codice (code-level)**

- Interfacce, API, dipendenze dirette
- Maggiore controllo, ma più accoppiamento
- Utile in progetti monolitici o microservizi strettamente correlati

### 2. 🔔 **Notifiche (pub-sub)**

- Uno o più componenti inviano **notifiche**
- I destinatari possono iscriversi per riceverle
- Nessuna aspettativa di risposta

🔧 [Amazon SNS](Amazon-SNS.md):
- Notifiche push asincrone
- Supporta fan-out su email, SMS, Lambda, SQS, HTTP

```plaintext
Producer ──▶ SNS Topic ──▶ [Email | Lambda | SQS]
```

### 3. 📨 **Code di messaggi (message queue)**

- Il produttore invia messaggi a una **coda**
- I consumatori elaborano i messaggi in modo asincrono
- Ottimo per bilanciare carico e gestire retry

🔧 [Amazon SQS](Amazon-SQS.md):
- Coda FIFO o Standard
- Decoupling forte tra producer e consumer
- Resilienza a errori temporanei

```plaintext
Producer ──▶ SQS ──▶ Consumer
```

### 4. 🧨 **Eventi (event-driven architecture)**

- I componenti pubblicano **eventi** su un bus/event bridge
- Gli handler si attivano **in risposta** agli eventi specifici
- I publisher non conoscono i subscriber → massimo disaccoppiamento

🔧 [Amazon EventBridge](Amazon-EventBridge.md):
- Bus di eventi fully managed
- Routing basato su regole
- Integrazione nativa con AWS e SaaS

```plaintext
Producer ──▶ EventBridge ──▶ [Lambda | Step Functions | SQS | SNS]
```

---

## 🏗️ Esempio di decoupling in AWS

```plaintext
[Service A]
   |
   └── (invio evento) ──▶ EventBridge
                           ├──▶ Lambda: aggiorna DB
                           ├──▶ SNS: invia notifica
                           └──▶ SQS: invia dati a sistema esterno
```

---

## ✅ Vantaggi del Loose Coupling

- **Manutenzione indipendente** dei servizi
- **Migliore gestione degli errori** (retry, dead letter queue)
- **Scalabilità orizzontale** dei consumer
- **Evoluzione indipendente** dei componenti
- **Tracciabilità** con sistemi di event logging

---

## 📌 Conclusioni

Il decoupling è una pratica essenziale nello sviluppo di architetture moderne, in particolare per microservizi e applicazioni cloud-native. Utilizzare servizi come [Amazon SQS](Amazon-SQS.md), [Amazon SNS](Amazon-SNS.md), ed [Amazon EventBridge](Amazon-EventBridge.md) permette di costruire sistemi flessibili, estendibili e resilienti, con una bassa dipendenza tra i componenti.

> "Disaccoppiare non significa semplificare: significa rendere il sistema più adattabile al cambiamento."
