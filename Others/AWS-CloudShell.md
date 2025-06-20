--> [AWS](/00-Intro/AWS.md)
# AWS CloudShell

**AWS CloudShell** è un ambiente shell basato su browser, preconfigurato e sicuro, disponibile direttamente dalla Console AWS. Consente di eseguire comandi della CLI AWS, gestire risorse, scrivere script, e accedere a strumenti di sviluppo senza dover configurare nulla in locale.

---

## 🧩 Caratteristiche principali

- **Ambiente shell preconfigurato**: con AWS CLI, Python, Node.js, Docker, Git, e altri strumenti.
- **Accesso istantaneo**: si avvia con un click dalla Console AWS.
- **Archiviazione persistente**: 1 GB gratuito per utente (per regione).
- **Sicurezza integrata**: usa le credenziali [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) dell'utente corrente.
- **Supporto multi-regione**: CloudShell è disponibile in varie regioni AWS.

---

## 🚀 Come iniziare

1. Accedi alla Console AWS
2. Clicca sull’icona **CloudShell** nella barra in alto (simbolo terminale `>`).
3. Si apre un terminale in una nuova finestra del browser.
4. Inizia a usare comandi CLI per gestire le risorse AWS.

---

## 🛠️ Esempi di utilizzo

```bash
# Controllare la versione CLI
aws --version

# Elencare i bucket S3
aws s3 ls

# Accedere a un'istanza EC2 con Session Manager
aws ssm start-session --target <instance-id>

# Clonare un repository CodeCommit
git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/NomeRepo
```

---

## 📁 Gestione file

- Ogni utente ha una **directory home** persistente: `~/`
- I file salvati rimangono disponibili tra una sessione e l’altra.
- Puoi caricare e scaricare file tramite l’interfaccia browser.

---

## 🔐 Sicurezza

- Le azioni eseguite in CloudShell **rispettano le policy [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md)** assegnate all’utente.
- Nessuna chiave di accesso è necessaria: viene usato il **profilo [IAM](/09-Sicurezza-Compliance-Governance/Sicurezza/AWS-IAM.md) temporaneo** della sessione.
- L’ambiente è isolato per ogni utente e per ogni regione.

---

## 📦 Software preinstallato

- AWS CLI v2
- Git
- Docker (solo client, non daemon)
- Node.js, Python, Java, Go, Ruby
- Vim, nano, tmux, curl, wget
- Pacchetti Python (`boto3`, `awscli`, ecc.)

Puoi installare anche pacchetti aggiuntivi (ma saranno temporanei fino al riavvio):

```bash
pip install nome-pacchetto --user
```

---

## ✅ Best Practices

- Usa CloudShell per task rapidi e gestione interattiva.
- Evita carichi di lavoro prolungati: sessione inattiva scade dopo 20 minuti.
- Mantieni script utili nella home per riutilizzarli facilmente.
- Non usare CloudShell per produzione o automazione continua: usa Lambda, EC2 o container.

---

## 📌 Conclusioni

AWS CloudShell è lo strumento perfetto per amministratori, sviluppatori e DevOps che vogliono gestire risorse AWS rapidamente e in sicurezza, senza configurazioni locali. È ideale per test, troubleshooting, script veloci e formazione.
