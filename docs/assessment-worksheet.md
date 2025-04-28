# Assessment Worksheet: Kubernetes Privilege Escalation Detection Lab

---

## 1. Objective
Simulate privilege escalation in Amazon EKS and engineer a detection and response workflow mapped to real-world GRC controls.

---

## 2. Screenshots and Evidence

| Step | Screenshot/Link | Notes |
|:---|:---|:---|
| Service Account Created | (Attach Screenshot) | - |
| ClusterRoleBinding Applied | (Attach Screenshot) | Validate that escalator is bound to cluster-admin. |
| Pod Running as Escalator SA | (Attach Screenshot) | - |
| Privileged Access Tested | (Attach Screenshot) | `kubectl get secrets --all-namespaces` successful |
| EKS Audit Logs Enabled | (Attach Screenshot) | CloudTrail shows audit logs |
| Athena Query Execution | (Attach Screenshot) | Query returns RoleBinding events |
| GuardDuty Finding | (Attach Screenshot) | Kubernetes RBAC escalation detected |
| EventBridge Rule Triggered | (Attach Screenshot) | EventBridge execution log |
| Lambda Execution Verified | (Attach Screenshot) | CloudWatch logs show successful remediation |
| Security Hub Alert Recorded | (Attach Screenshot) | Security Hub aggregates findings |

---

## 3. Reflections

- What did you learn about Kubernetes IAM and RBAC security models?
- How can automated detection improve real-world GRC readiness?
- What gaps were discovered in the detection pipeline?
- How would you scale this for production environments?
- How would you report this incident to an audit or compliance team?

---

## 4. GRC Framework Mapping (Quick Reference)

| Framework | Control | Validated Through |
|:--|:--|:--|
| NIST 800-53 | AC-6 (Least Privilege) | RBAC enforcement |
| NIST 800-53 | IR-4 (Incident Response) | Lambda automated remediation |
| CIS Controls v8 | 4.8, 5.3 | Audit logs, privilege restriction |
| ISO 27001 | A.9.4.1, A.12.4.1 | Access control validation, logging |

---

## 5. Completion Sign-off

- [ ] All steps completed and validated.
- [ ] All artifacts documented.
- [ ] Reflection and control mapping completed.

**Signed:** Runc9  
**Date:** (Enter today's date)
