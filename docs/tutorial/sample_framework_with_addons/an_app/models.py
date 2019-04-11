"""
A custom add-on to our app which adds FrenchCustomer and
French Greeter.
"""
from dataclasses import dataclass

from wired import ServiceRegistry, ServiceContainer
from wired import factory
from wired import injected

from a_framework.models import (
    Customer, Greeter, Request, Resource, Settings, View,
)


@dataclass(frozen=True)
class FrenchCustomer(Customer):
    pass


@factory(for_=Greeter, context=FrenchCustomer)
@dataclass(frozen=True)
class FrenchGreeter(Greeter):
    greeting: str = 'Bonjour'


@factory(for_=View, context=FrenchCustomer)
@dataclass(frozen=True)
class FrenchView:
    container: ServiceContainer = injected(ServiceContainer)
    url: str = injected(Request, attr='url')
    customer_title: str = injected(Resource, attr='title')
    greeting: str = injected(Greeter, attr='greeting')
    punctuation: str = injected(Greeter, attr='punctuation')

    def __call__(self) -> str:
        return f'{self.url} and FrenchView: {self.greeting} {self.customer_title} {self.punctuation}'
