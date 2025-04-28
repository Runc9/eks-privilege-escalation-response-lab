-- Athena query to detect suspicious Kubernetes RBAC escalation events
SELECT
  eventTime,
  eventName,
  userIdentity.sessionContext.sessionIssuer.userName AS serviceAccountName,
  requestParameters.roleRef.name AS roleName,
  awsRegion,
  sourceIPAddress
FROM
  cloudtrail_logs_database_name.cloudtrail_logs_table_name
WHERE
  eventSource = 'eks.amazonaws.com'
  AND eventName IN ('CreateClusterRoleBinding', 'UpdateClusterRoleBinding')
  AND eventTime > current_timestamp - interval '7' day
ORDER BY
  eventTime DESC
