from pydantic import BaseModel


class UserInfoBase(BaseModel):
    user_id : str
    #unique_genuserid : str
    user_fullname : str
    user_display_pic : str | None = None

class UserCreate(UserInfoBase):
    mail_id : str
    user_password : str

class UserRetrieval(UserInfoBase):

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    user_id : str
    user_password : str


""" 

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

 """