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


@singleton()
@dataclass(frozen=True)
class Datastore:
    customers: Dict[str, Customer] = field(default_factory=dict)
