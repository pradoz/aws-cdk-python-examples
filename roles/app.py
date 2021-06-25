#!/usr/bin/env python3
import os

from aws_cdk import (
    core,
)

from roles.roles_stack import RolesStack


app = core.App()

REGION = 'us-east-1'
ENV = core.Environment(region=REGION)

RolesStack(app, "RolesStack", env=ENV)

app.synth()
