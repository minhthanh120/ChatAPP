select * from UserInfo

insert UserAuth(Id, UserName, ISAuthenticated, Email) values('AE5CE941-DC01-11', 'LeMing', 1, 'dingjonghan@gmail.com')
insert UserPassword(UserId, HashString, EncriptedValue, SaltString) values('AE5CE941-DC01-11', 'abcd1234', '1234abcd', 'xyz')

select * from dbo.[Group]