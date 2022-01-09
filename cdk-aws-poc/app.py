from aws_cdk import (
    core,
    aws_lambda,
    aws_apigatewayv2,
    aws_apigatewayv2_integrations,
)


class HelloHttpApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = aws_lambda.Function(
            self, 'HelloHttpApiLambda',
            handler='lambda-handler.handler',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.from_asset('lambda'),
        )

        my_api = aws_apigatewayv2.HttpApi(self, 'HelloHttpApi')
        api_integration = aws_apigatewayv2_integrations.LambdaProxyIntegration(
            handler=my_lambda,
        )

        my_api.add_routes(
            path="/hello",
            methods=[aws_apigatewayv2.HttpMethod.GET],
            integration=api_integration,
        )


app = core.App()
HelloHttpApiStack(app, "HelloHttpApiStack")
app.synth()
