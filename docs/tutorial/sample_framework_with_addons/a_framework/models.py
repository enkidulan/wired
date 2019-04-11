"""
Models used in the core application.
Putting models in their own file is considered good practice for
code clarity. It also solves the problem of potential circular
imports.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from wired import ServiceContainer
from wired import factory
from wired import singleton
from wired import injected


@dataclass(frozen=True)
class Url:
    value: str


@dataclass(frozen=True)
class Resource:
    name: str
    title: str


@dataclass(frozen=True)
class Customer(Resource):
    pass


@dataclass(frozen=True)
class Settings:
    punctuation: str


@factory()
@dataclass(frozen=True)
class Request:
    container: ServiceContainer
    url: str = injected(Url, attr='value')


@factory()
@dataclass(frozen=True)
class Greeter:
    punctuation: str = injected(Settings, attr='punctuation')
    greeting: str = 'Hello'


@factory()
@dataclass(frozen=True)
class View:
    url: str = injected(Request, attr='url')
    customer_title: str = injected(Resource, attr='title')
    greeting: str = injected(Greeter, attr='greeting')
    punctuation: str = injected(Greeter, attr='punctuation')

    def __call__(self) -> str:
        return f'{self.url}: {self.greeting} {self.customer_title} {self.punctuation}'
