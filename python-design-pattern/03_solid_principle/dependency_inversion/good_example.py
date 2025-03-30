from abc import ABCMeta, abstractmethod

class User:
    pass

class UserService(metaclass=ABCMeta):
    @abstractmethod
    def create(self , user : User):
        pass
    
    def findById(self , id : str):
        pass
    
class UserRdbRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self , user : User):
        pass
    
    @abstractmethod
    def findById(self , id : str):
        pass

class UserController:
    def __init__(self , userService : UserService):
        self.__userService = userService

    def create(self, user: User) -> User:
        return self.__userService.create(user)

    def findById(self, id: str) -> User:
        return self.__userService.findById(id)
    

class UserServiceImp(UserService):
    def __init__(self , userRepository : UserRdbRepository):
        self.__userRepository = userRdbRepository

    def create(self, user: User) -> User:
        return self.__userRepository.create(user)

    def findById(self, id: str) -> User:
        return self.__userRepository.findById(id)


class UserRdbRepositoryImp(UserRdbRepository):
    def create(self, user: User) -> User:
        print("RDB")
        return user

    def findById(self, id: str) -> User:
        print(f"ID: {id} is True")
        return User()


if __name__ == "__main__":
    
    userRdbRepository = UserRdbRepositoryImp()
    userService = UserServiceImp(userRdbRepository) # DI
    user_controller = UserController(userService)
    user_controller.findById("123")
    
