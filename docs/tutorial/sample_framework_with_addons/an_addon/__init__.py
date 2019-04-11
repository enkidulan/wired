"""Datastore add-on"""

import venusian
from wired import ServiceRegistry, ServiceContainer
from a_framework.models import Url
from a_framework.models import Resource

from .models import Datastore


def datastore_factory(container: ServiceContainer) -> Resource:
    """ Custom factory that gets a Datastore instance """

    # Presumes that "url" is in the container
    ds: Datastore = container.get(Datastore)
    url: Url = container.get(Url)
    context: Resource = ds.customers[url.value]
    return context


def overwrite_resource_factory(registry: ServiceRegistry):
    from a_framework.models import Resource as BaseResource

    registry.register_factory(datastore_factory, BaseResource)


def setup(registry: ServiceRegistry, container: ServiceContainer):
    """Initialize the features in the add-on"""

    from . import models
    scanner = container.get(venusian.Scanner)
    scanner.scan(models)

    overwrite_resource_factory(registry)
