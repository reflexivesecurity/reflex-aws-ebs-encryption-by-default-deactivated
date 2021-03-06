""" Module for EBSEncryptionByDefaultDeactivated """

import json

import boto3
from reflex_core import AWSRule, subscription_confirmation


class EBSEncryptionByDefaultDeactivated(AWSRule):
    """ A Reflex Rule for enforcing EBS Volume encryption by default """

    client = boto3.client("ec2")

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        # No data from the event is required
        return

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        # Since the event occurred the account configuration is no longer
        # compliant and we need to take action.
        return False

    def remediate(self):
        """
        Fix the non-compliant resource so it conforms to the rule
        """
        self.client.enable_ebs_encryption_by_default()

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        if self.should_remediate():
            return "EBS Encryption by default was deactivated. It has been reactivated."
        return "EBS Encryption by default was deactivated."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = EBSEncryptionByDefaultDeactivated(event_payload)
    rule.run_compliance_rule()
