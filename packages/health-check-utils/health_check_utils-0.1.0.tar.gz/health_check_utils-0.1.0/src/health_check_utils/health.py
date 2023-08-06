from dataclasses import dataclass
from functools import wraps
from typing import Callable


@dataclass
class HealthStatus:
    """
    Helper class for representing health status of an application. Will
    be updated by the health_check decorator and used in the response
    of a health check route.
    """

    _healthy: bool = True

    @property
    def status_msg(self) -> str:
        """Status message corresponding to health status."""
        return "healthy" if self.healthy else "unhealthy"

    @property
    def status_code(self) -> int:
        """Status code corresponding to health status."""
        return 200 if self.healthy else 500

    @property
    def healthy(self) -> bool:
        """Getter for _healthy."""
        return self._healthy

    @healthy.setter
    def healthy(self, new_val: bool) -> None:
        """Setter for _healthy."""
        self._healthy = new_val


def health_check(health_status: HealthStatus) -> Callable:
    """
    Decorator for updating a global health status for
    health check route.

    :param health_status: Global health status to be updated

    :return: Decorated function
    """

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                retval = function(*args, **kwargs)
                health_status.healthy = True
                return retval
            except Exception as e:
                health_status.healthy = False
                raise

        return wrapper

    return decorator