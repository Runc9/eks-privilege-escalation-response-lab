import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function triggered by EventBridge Rule when a suspicious ClusterRoleBinding is created.
    Logs the detection and prepares for future automated remediation actions.
    """

    # Log the incoming event for forensic purposes
    logger.info("Received event: %s", json.dumps(event))

    # Example: extract important fields (like who created the role binding)
    detail = event.get('detail', {})
    event_name = detail.get('eventName', 'UnknownEvent')
    user_identity = detail.get('userIdentity', {}).get('arn', 'UnknownUser')

    logger.warning(f"Detected suspicious Kubernetes event: {event_name} by {user_identity}")

    # Placeholder: Future action could delete the misconfigured ClusterRoleBinding
    # Example:
    # eks_client = boto3.client('eks')
    # response = eks_client.delete_cluster_role_binding(...)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Privilege escalation detection handled successfully')
    }
