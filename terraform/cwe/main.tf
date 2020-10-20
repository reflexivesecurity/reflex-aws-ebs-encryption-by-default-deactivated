module "cwe" {
  source      = "git::https://github.com/reflexivesecurity/reflex-engine.git//modules/cwe?ref=v2.1.2"
  name        = "EbsEncryptionByDefaultDeactivated"
  description = "A Reflex Rule for enforcing EBS Volume encryption by default"

  event_pattern = <<PATTERN
{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "ec2.amazonaws.com"
    ],
    "eventName": [
      "DisableEbsEncryptionByDefault"
    ]
  }
}
PATTERN

}
