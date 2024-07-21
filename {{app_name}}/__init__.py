"""Module for {{app_name}}."""

from ..{{app_name}} import controllers, urls{% if db %}, dependencies, services{% endif %}

__all__ = ("controllers", "urls"{% if db %}, "dependencies", "services"{% endif %})
