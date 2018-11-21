from abc import ABC, abstractmethod, abstractstaticmethod
from typing import List


class AbstractState(ABC):

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()


class AbstractAction(ABC):

    @abstractstaticmethod
    def execute(state: AbstractState) -> AbstractState:
        pass


class AbstractProblem(ABC):
    """Formalization of an abstract problem"""

    @abstractstaticmethod
    def create_initial_state() -> AbstractState:
        pass

    @abstractstaticmethod
    def get_actions() -> List[AbstractAction]:
        pass

    @abstractstaticmethod
    def is_goal_state(state: AbstractState) -> bool:
        pass
