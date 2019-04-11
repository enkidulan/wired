from typing import List

import venusian
from wired import ServiceRegistry, ServiceContainer

from a_framework import sample_interactions
from a_framework.models import Settings
from an_addon.models import Datastore


def app_bootstrap(settings: Settings) -> ServiceRegistry:
    # Make the registry
    registry = ServiceRegistry()

    # Store the settings in the registry so things later can
    # get to them.
    registry.register_singleton(settings, Settings)

    # Make a container to use during the initialization phase
    container: ServiceContainer = registry.create_container()

    # Scan for registrations
    scanner = venusian.Scanner(registry=registry, settings=settings, container=container)
    registry.register_singleton(scanner, venusian.Scanner)

    # Import the framework and initialize it
    import a_framework
    a_framework.setup(registry, container)

    # Import the add-on and initialize it
    import an_addon
    an_addon.setup(registry, container)

    # initialize an app
    setup(registry, container)

    return registry


def setup(registry: ServiceRegistry, container: ServiceContainer):
    """Initialize the features in the core application"""

    from . import models
    scanner = container.get(venusian.Scanner)
    scanner.scan(models)

    datastore: Datastore = container.get(Datastore)

    from a_framework.models import Customer
    datastore.customers['mary'] = Customer(name='mary', title='Mary')

    from .models import FrenchCustomer
    datastore.customers['henri'] = FrenchCustomer(name='henri', title='Henri')


def main():
    settings = Settings(punctuation='!!')
    registry = app_bootstrap(settings)
    greetings = sample_interactions(registry)
    assert greetings == [
        'mary: Hello Mary !!',
        'henri and FrenchView: Bonjour Henri !!']


if __name__ == '__main__':
    main()
