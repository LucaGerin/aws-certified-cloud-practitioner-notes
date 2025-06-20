--> [AWS](/00-Intro/AWS.md)  -  [Migration Strategies](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Strategies.md)
# AWS Application Migration Service (MGN)

## ⚙️ Cos'è AWS MGN?

AWS Application Migration Service (MGN) consente di **migrare automaticamente server fisici, virtuali o cloud-based** verso AWS con **minimo downtime**. È la soluzione preferita per migrazioni "lift and shift", usata per migrare applicazioni che vanno su server fisici, virtuali, o altri cloud provider o altre regioni o account AWS verso un cloud AWS.

![MGN](MGN.webp)

---

## 🔧 Caratteristiche principali

- **Replica continua** dei dati dal sistema sorgente verso [AWS](/00-Intro/AWS.md)
- **Test senza interruzioni** prima del cutover finale
- **Automazione del provisioning** delle istanze [Amazon EC2](/01-Compute-options/Amazon-EC2.md)
- **Riduzione dei downtime** e rischio di errori umani

---

## 🧑‍💻 Casi d'uso ideali

- Migrazione di ambienti on-premise
- Consolidamento di data center
- Spostamento di workload legacy su [Amazon EC2](/01-Compute-options/Amazon-EC2.md)

---

## ✅ Vantaggi

- Nessuna necessità di riscrivere l'applicazione
- Integrazione con [AWS Migration Hub](/06-Cloud-Adoption-Framework-and-Migration-Strategies/AWS-Migration-Hub.md)
- Supporto a diverse piattaforme (Windows, Linux, VMware, ecc.)
