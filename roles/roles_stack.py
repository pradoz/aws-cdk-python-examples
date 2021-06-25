from aws_cdk import (
    core,
    aws_iam as iam,
)


class RolesStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a service role for ECS fargate
        ecs_fargate_role = iam.Role(
            self,
            'FargateTaskExecutionServiceRole',
            assumed_by=iam.ServicePrincipal('ecs-tasks.amazonaws.com'),

            # Attach a managed policy to a role we can use
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('Cust_AWSECSTaskExecutionRole')
            ],
        )

        # Add policies to the role for ECS fargate
        ecs_fargate_role.add_to_principal_policy(
            iam.PolicyStatement(
                effect = iam.Effect.ALLOW,
                resources = ['*'],
                actions = [
                  'ecr:GetAuthorizationToken',
                  'ecr:BatchCheckLayerAvailability',
                  'ecr:GetDownloadUrlForLayer',
                  'ecr:BatchGetImage',
                  'logs:CreateLogStream',
                  'logs:PutLogEvents'
                ]
            )
        )


