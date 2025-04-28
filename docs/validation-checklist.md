# Validation Checklist: Kubernetes Privilege Escalation Detection in Amazon EKS

This checklist validates that all steps of the lab were successfully implemented, ensuring realistic security detection and incident response workflows aligned with GRC controls.

---

## 1. Service Account Creation
- [ ] `kubectl get serviceaccount escalator -n dev-ops` shows service account exists.

## 2. Misconfigured ClusterRoleBinding Deployment
- [ ] `kubectl describe clusterrolebinding escalator-admin-binding` shows service account bound to `cluster-admin` role.

## 3. Pod Deployment Using Escalator SA
- [ ] `kubectl get pods -n dev-ops` shows `escalator-shell` pod is running.

## 4. Privilege Validation Inside Pod
- [ ] From inside the pod, `kubectl get secrets --all-namespaces` succeeds, confirming elevated privileges.

## 5. EKS Audit Logging Configuration
- [ ] EKS Control Plane audit logs are enabled and visible in CloudTrail logs.

## 6. CloudTrail Event Detection
- [ ] Amazon Athena query returns the `CreateClusterRoleBinding` or `UpdateClusterRoleBinding` event associated with escalator service account.

## 7. GuardDuty Finding Verification
- [ ] GuardDuty reports a "Kubernetes RBAC escalation" finding.

## 8. EventBridge Rule Execution
- [ ] EventBridge rule triggered by CloudTrail log event and Lambda function is invoked.

## 9. Lambda Remediation Validation
- [ ] AWS Lambda logs in CloudWatch show correct function execution upon RBAC escalation detection.

## 10. Security Hub Centralized Finding
- [ ] Security Hub aggregates and displays the incident finding from GuardDuty or Lambda.

## 11. Cleanup Verification
- [ ] `kubectl delete clusterrolebinding escalator-admin-binding`
- [ ] `kubectl delete ns dev-ops`
- [ ] No remaining escalated roles or resources in EKS cluster.

---

# Notes:
- **Screenshots** or **CLI outputs** are recommended for every validation step for audit trail purposes.
- **Optional**: Export Athena query results and GuardDuty finding into PDF format for additional documentation.
