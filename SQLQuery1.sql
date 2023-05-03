select * from UserInfo

insert UserAuth(Id, UserName, ISAuthenticated, Email) values('AE5CE941-DC01-11', 'LeMing', 1, 'dingjonghan@gmail.com')
insert UserPassword(UserId, HashString, EncriptedValue, SaltString) values('AE5CE941-DC01-11', 'abcd1234', '1234abcd', 'xyz')

select * from dbo.[Group]

select * from dbo.[UserPassword]

select * from dbo.[UserAuth] where Id = 'AE5CE941-DC01-11'

insert UserInfo(Id, UserName, FirstName, LastName, Email) values('A5E1EC42-F5FB-40','lmt1202', 'Le','Ming', 'dingjohan@gmail.com.vn')
