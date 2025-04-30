![AWS](https://img.shields.io/badge/Built%20With-AWS-orange)
![EKS](https://img.shields.io/badge/Platform-EKS-blue)
![GRC Engineering](https://img.shields.io/badge/Focus-GRC%20Engineering-green)
![Incident Response](https://img.shields.io/badge/Use%20Case-Incident%20Response-red)
![Compliance Frameworks](https://img.shields.io/badge/Mapped%20to-NIST%20800--53%20%7C%20CIS%20Controls%20%7C%20ISO%2027001-brightgreen)

# AWS EKS Privilege Escalation Detection and Response Lab

This lab simulates a Kubernetes RBAC misconfiguration within Amazon EKS and demonstrates how to detect, respond, and document such incidents using AWS-native services. It aligns with key compliance frameworks such as NIST 800-53, CIS Controls v8, and ISO 27001.

## 📚 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Lab Components](#lab-components)
- [Deployment Instructions](#deployment-instructions)
- [Validation Checklist](#validation-checklist)
- [Outputs](#outputs)
- [GRC Framework Mapping](#grc-framework-mapping)
- [Cleanup](#cleanup)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## 🧭 Overview

This lab covers:

- Simulating a privilege escalation scenario via a misconfigured `ClusterRoleBinding` in EKS.
- Detecting escalation via CloudTrail logs, Athena queries, and GuardDuty.
- Automating response using AWS EventBridge and Lambda.
- Documenting the event with a validation checklist and assessment worksheet.

## 📐 Architecture

![Architecture Diagram](docs/architecture-diagram.png)

## ✅ Prerequisites

- AWS CLI and kubectl installed locally
- An active Amazon EKS cluster
- IAM permissions to deploy Lambda, EventBridge, GuardDuty, and Security Hub
- Athena and CloudTrail enabled
- CloudTrail logs sent to S3 and Athena query database configured
- Git installed to clone this repository

## 🧱 Lab Components

| Component | Purpose |
|:--|:--|
| `code/scripts/` | Athena SQL query, EventBridge rule, and Lambda remediation script |
| `manifests/` | Kubernetes RBAC misconfiguration and deployment manifests |
| `docs/` | Architecture diagram, validation checklist, assessment worksheet |
| `README.md` | Full documentation of the lab |

## 🚀 Deployment Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Runc9/eks-privilege-escalation-response-lab.git
cd eks-privilege-escalation-response-lab
```

### Step 2: Apply RBAC Misconfiguration

```bash
kubectl create namespace dev-ops
kubectl apply -f manifests/rbac-escalation.yaml
kubectl apply -f manifests/pod-deployment.yaml
```

### Step 3: Simulate Detection

- Run the `athena-query.sql` using the Athena Console or CLI to find RBAC escalation events.
- Confirm a GuardDuty finding is generated.
- EventBridge rule triggers Lambda response.

### Step 4: Review Outputs

- Check Lambda execution logs in CloudWatch.
- Verify Security Hub aggregates the incident.

## ✅ Validation Checklist

Available in `docs/validation-checklist.md`

Covers:

- RBAC misconfig deployed and detected
- GuardDuty finding generated
- EventBridge rule triggered
- Lambda executed and Security Hub notified

## 📤 Outputs

| Output | Description |
|:--|:--|
| GuardDuty Finding | Shows RBAC escalation risk |
| Lambda Logs | Evidence of automatic response |
| Security Hub Finding | Aggregated GRC-aligned incident evidence |
| Athena Query Results | CloudTrail-based detection of privilege escalation |

## 🛡️ GRC Framework Mapping

| Framework | Control | Validation Method |
|:--|:--|:--|
| NIST 800-53 | AC-6 (Least Privilege), IR-4 (Response) | Pod role analysis, Lambda |
| CIS Controls v8 | 4.8, 5.3, 8.7 | GuardDuty alerts, IAM constraints |
| ISO 27001 | A.9.4.1, A.12.4.1 | Log review and escalation handling |

## 🧹 Cleanup

```bash
kubectl delete namespace dev-ops
```

Optional:

- Remove EventBridge rule
- Disable Lambda
- Turn off Security Hub
- Delete Athena query output

## 🧰 Troubleshooting

| Issue | Fix |
|:--|:--|
| No GuardDuty findings | Ensure GuardDuty is enabled and EKS Control Plane logs are ingested |
| Lambda didn't trigger | Check EventBridge rule and Lambda permissions |
| Security Hub didn’t populate | Check integration, or push manually via Lambda |
| Pod failed to start | Confirm cluster role binding and service account |

## 📖 References

- [AWS GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [NIST 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/)
- [ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html)

## 🙌 Credit

Developed and maintained by [Runc9](https://github.com/Runc9)  
Built as part of a broader AWS Cloud Security GRC Engineering portfolio.