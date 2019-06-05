from pubnub.callbacks import SubscribeCallback
import importlib


# Ready to listen pubnub events
class Listener(SubscribeCallback):
    def status(self, pub_nub, status):
        pass

    def message(self, pub_nub, message):
        # module name like commands.channel
        module = message.message['module']

        # class name like Channel
        name = message.message['name']

        # method name from class like change
        method = message.message['method']

        # params/arguments to method like {foo: 'bar'}
        params = message.message['params']

        # instance a class from module name and class name
        ModuleClass = getattr(importlib.import_module(module), name)

        # instance method from instanced class
        build = getattr(ModuleClass, method)

        # call method with params arguments
        build(params)
