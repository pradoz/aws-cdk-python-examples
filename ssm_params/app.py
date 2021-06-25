#!/usr/bin/env python3
import os

from aws_cdk import core

from ssm_params.ssm_params_stack import SsmParamsStack


app = core.App()

REGION = 'us-east-1'
ENV = core.Environment(region=REGION)
SsmParamsStack(app, "SsmParamsStack")

app.synth()
