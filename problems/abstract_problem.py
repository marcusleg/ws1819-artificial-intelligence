from abc import ABC, abstractmethod, abstractstaticmethod
from typing import List


class AbstractState(ABC):

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def get_actions(self):
        pass

    @abstractmethod
    def is_goal_state(self) -> bool:
        pass


class AbstractProblem(ABC):
    """Formalization of an abstract problem"""

    @abstractstaticmethod
    def create_initial_state() -> AbstractState:
        pass
