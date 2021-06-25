from aws_cdk import (
    core,
    aws_ssm as ssm,
)

class SsmParamsStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        XXXX_param = ssm.StringParameter(
            self,
            'alerts-email-parameter',
            type=ssm.ParameterType.STRING,
            tier=ssm.ParameterTier.STANDARD,
            description=f'descriptionofwhat_theparameterdoes',
            parameter_name=f'/my-repo/my-environment/my-stack/param_name',
            string_value=f'secret::iam::arn:do/not/steal-me.com/id/5611EAC0151',
        )


        import_XXXX_ssm_param = ssm.StringParameter.from_string_parameter_attributes(
            self,
            'imported-ssm-parameter',
            parameter_name=XXXX_param.parameter_name,
            simple_name=False,
        )

