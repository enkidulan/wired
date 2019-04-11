from typing import List

import venusian
from wired import ServiceRegistry, ServiceContainer


def setup(registry: ServiceRegistry, container: ServiceContainer):
    """Initialize the features in the add-on"""

    from . import models
    scanner = container.get(venusian.Scanner)
    scanner.scan(models)


def process_request(registry: ServiceRegistry, url_value: str) -> str:
    """ Given URL (customer name), make a Request to handle interaction """

    from a_framework.models import (
        Resource,
        View,
        Url
    )

    # Make the container that this request gets processed in
    container = registry.create_container()

    # Put the url into the container
    url = Url(value=url_value)
    container.set(url, Url)

    # Create a Request using the factory
    # request = container.get(Request)

    # Get the context
    context = container.get(Resource)

    # Create a View to generate the greeting
    view = container.get(View, context=context)

    # Generate a response
    response = view()

    return response


def sample_interactions(registry: ServiceRegistry) -> List[str]:
    """ Pretend to do a couple of customer interactions """

    return [
        process_request(registry, url)
        for url in ('mary', 'henri')
    ]
