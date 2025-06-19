--> [AWS](AWS.md)  -  [Development, Messaging, and Deployment](Development-Messaging-and-Deployment.md)
# Infrastructure as Code (IaC)

**Infrastructure as Code (IaC)** è una pratica DevOps che consiste nel **definire e gestire l’infrastruttura IT tramite file di configurazione**, invece che configurarla manualmente tramite console o CLI.

![IaC](IaC.png)

---

## 🎯 Obiettivi principali

- **Automazione** dell’infrastruttura
- **Versionamento** delle modifiche (come per il codice)
- **Ripetibilità** e coerenza nei deployment
- **Collaborazione** tra team Dev e Ops
- **Provisioning veloce** e rollback sicuro

---

## 🧩 Componenti principali

- **Template di configurazione**: descrivono risorse e relazioni (es. file YAML, JSON, HCL)
- **Tool di provisioning**: interpretano i template e interagiscono con il provider (es. AWS)
- **State management**: mantengono lo stato reale dell'infrastruttura

---

## 🛠️ Esempi di strumenti IaC

| Strumento       | Linguaggio         | Provider      | Note                         |
|-----------------|--------------------|---------------|------------------------------|
| **[CloudFormation](AWS-CloudFormation.md)** | YAML / JSON        | Solo AWS      | 100% AWS-native              |
| **Terraform**       | HCL (HashiCorp)     | Multi-cloud   | Stato gestito esternamente   |
| **Pulumi**          | TypeScript, Python  | Multi-cloud   | Uso di linguaggi di programmazione reali |
| **CDK** (AWS)       | TypeScript, Python  | Solo AWS      | Abstraction su CloudFormation |

---

## 🔐 Vantaggi di IaC

- Deploy consistenti su più ambienti
- Riduzione errori manuali
- Rollback e controllo versioni con Git
- Maggiore velocità di rilascio
- Integrazione con CI/CD pipeline

---

## 🧪 Esempio base (Terraform)

```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "nome-bucket-demo"
  acl    = "private"
}
```

---

## 📌 Conclusioni

Infrastructure as Code è alla base delle architetture cloud moderne. Permette ai team di trattare l’infrastruttura come software, migliorando automazione, controllo e collaborazione.

> “Se l’infrastruttura è codice, allora la tua infrastruttura è testabile, revisionabile e versionabile.”

Il servizio Amazon dedicato a IaC è [AWS CloudFormation](AWS-CloudFormation.md).
