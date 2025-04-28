# Lab 1: Kubernetes Privilege Escalation Detection & Response in Amazon EKS (GRC-Aligned)

This project simulates a real-world Kubernetes privilege escalation scenario within Amazon EKS, engineering automated detection and response workflows mapped to GRC control frameworks.

---

## 🎯 Learning Objectives

By completing this lab, you will be able to:
- Simulate privilege escalation attacks in Kubernetes.
- Detect suspicious RBAC role bindings using AWS-native services.
- Automate incident response actions using EventBridge and Lambda.
- Map technical activities to compliance frameworks (NIST 800-53, CIS Controls, ISO 27001).
- Generate audit-ready artifacts to demonstrate security control effectiveness.

---

## 🛠 AWS Services and Tools Used

- Amazon EKS (Kubernetes API)
- IAM Roles for Service Accounts (IRSA)
- Kubernetes RBAC
- AWS CloudTrail
- Amazon Athena
- AWS GuardDuty
- AWS EventBridge
- AWS Lambda
- AWS Security Hub
- OPA/Gatekeeper (optional policy enforcement)

---

## ⏳ Estimated Time to Complete
2–3 hours

---

## 💵 AWS Free Tier Usage

- EKS control plane logging: Free tier available
- CloudTrail management events: Free for 1 trail
- GuardDuty: 30-day free trial
- Athena: 1TB free per month query
- EventBridge and Lambda: Generous free tier limits

Estimated cost if running beyond free tier: **Less than $5/day**

---

## 📋 Prerequisites

- AWS account with administrative access
- AWS CLI and `kubectl` installed
- Basic familiarity with Kubernetes concepts (RBAC, ServiceAccounts)
- Git installed on your machine (optional for automation)

---

## 🏗️ Architecture Overview

This lab builds a real-world security detection pipeline:

1. Kubernetes misconfiguration occurs (privilege escalation via ClusterRoleBinding).
2. Amazon EKS generates audit logs sent to CloudTrail.
3. Athena queries detect escalation events.
4. GuardDuty detects abnormal Kubernetes behavior.
5. EventBridge triggers Lambda to automate incident response.
6. Findings are centralized in AWS Security Hub.

Diagram available: [Architecture Diagram](docs/architecture-diagram.png)

---

## 🧪 Lab Components

- **Step-by-Step Guide** – Manual setup instructions
- **Validation Checklist** – Ensure environment is configured correctly
- **Assessment Worksheet** – Document findings and lessons learned
- **Automation Scripts** – Deploy detection and response workflows
- **Architecture Diagram** – Visual representation of detection flow

---

## 📂 Deployment Options

- **Manual Implementation**: Full step-by-step lab for hands-on experience.
- **Semi-Automated Deployment**: Use provided scripts and templates for faster setup.

---

## 🧾 GRC Framework Mapping

| Framework  | Control Validated                              |
|------------------|-----------------------------------------------|
| **NIST 800-53** | AC-6, IR-4, AU-2, SI-4               |
| **CIS Controls v8** | 4.8, 5.3, 6.2, 8.7                   |
| **ISO 27001**  | A.9.4.1, A.12.4.1, A.16.1.5        |

---

## 📁 Repository Structure

