# reflex-aws-ebs-encryption-by-default-deactivated
A Reflex Rule for enforcing EBS Volume encryption by default

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-ebs-encryption-by-default-deactivated:
      version: latest
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-ebs-encryption-by-default-deactivated" {
  source           = "github.com/cloudmitigator/reflex-aws-ebs-encryption-by-default-deactivated"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-ebs-encryption-by-default-deactivated/blob/master/LICENSE) 
