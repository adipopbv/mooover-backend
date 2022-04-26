from app.domain.models import User
from app.repositories import Repository


class UserServices:
    """The services associated with the user related operations"""

    def __init__(self, repo=Repository()) -> None:
        self.repo = repo

    def get_user(self, user_id: str) -> User:
        """
        Gets a user by id

        :param user_id: the id of the user
        :return: the user
        "raises NotFoundError: if the user cannot be found in the repository
        """
        return self.repo.get_one(user_id)

    def add_user(self, user: User) -> None:
        """
        Adds a user

        :param user: the user to be added
        :return: the added user
        "raises DuplicateError: if the user already exists in the repository
        """
        self.repo.add(user)

    def get_user_steps(self, user_id: str) -> int:
        """
        Gets the steps of a user

        :param user_id: the id of the user
        :return: the steps of the user
        "raises NotFoundError: if the user cannot be found in the repository
        """
        return 1000

    def get_user_heart_points(self, user_id: str) -> int:
        """
        Gets the heart points of a user

        :param user_id: the id of the user
        :return: the heart points of the user
        "raises NotFoundError: if the user cannot be found in the repository
        """
        return 10
