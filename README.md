
# sceptre-aws-resolver
[![PyPI version](https://badge.fury.io/py/sceptre-aws-resolver.svg)](https://badge.fury.io/py/sceptre-aws-resolver)
![Build badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiNlZwTFptVGM4ZTB3NTY0SkZNb2xyMWVac2JLR3IwOVpJTWtLblVCR2NXNGJZbHREdUh4M0NGTWlKV3M3cHk1Q2pXbEJ6eFVYM3ZVN0JxUVZPRUtUN1AwPSIsIml2UGFyYW1ldGVyU3BlYyI6IjluZVpUK1c0MmVCbEFHZXgiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

[Sceptre](https://github.com/cloudreach/sceptre) resolver for any AWS API.

Format: `!aws client_name::operation_name::optional_parameter_in_dict_format::optional_jmespath_expression_to_filter_output`.

Examples:
- Return call to STS [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) in string format: `!aws sts::get_caller_identity`
- Get current UserId: `!aws sts::get_caller_identity::::UserId`
- Read a systems manager parameter and return its value: `!aws ssm::get_parameter::'Name':'your-param-name'::Parameter.Value`
- Read a systems manager parameter and return its **decrypted** value if necessary: `!aws ssm::get_parameter::'Name':'your-secret-param','WithDecryption':True::Parameter.Value`

See the jmespath package for query examples:

https://pypi.org/project/jmespath/

Released under the simplified BSD licence. See [LICENCE.txt](LICENCE.txt) for details.

Thanks to the https://github.com/zaro0508/sceptre-date-resolver project for providing the boilerplate.
