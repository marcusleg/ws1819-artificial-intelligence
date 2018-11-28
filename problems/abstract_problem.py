from abc import ABC, abstractmethod, abstractstaticmethod
from typing import List


class AbstractProblemState(ABC):
    """Formalization of an abstract problem"""

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()

    @abstractstaticmethod
    def create_initial_state() -> 'AbstractProblemState':
        pass

    @abstractmethod
    def get_actions(self):
        pass

    def heuristic(self) -> int:
        return None

    @abstractmethod
    def is_goal_state(self) -> bool:
        pass
