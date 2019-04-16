import logging
from ast import literal_eval

import jmespath
from sceptre.resolvers import Resolver


class Aws(Resolver):
    """
    Docs: https://github.com/jeshan/sceptre-aws-resolver
    """

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        super(Aws, self).__init__(*args, **kwargs)

    def resolve(self):
        # self.argument, self.stack
        arg_list = self.argument.split('::')
        service = arg_list[0]
        operation = arg_list[1]
        expression = None
        parsed_args = {}
        if len(arg_list) > 2 and arg_list[2]:
            args = arg_list[2]
            parsed_args = literal_eval("{" + args + "}")
        if len(arg_list) > 3 and arg_list[3]:
            expression = arg_list[3]
        # noinspection PyStatementEffect
        self.stack.template  # just to initialise the connection manager
        result = self.stack.connection_manager.call(service, operation, parsed_args)
        if expression:
            result = jmespath.search(expression, result)
        return str(result)
