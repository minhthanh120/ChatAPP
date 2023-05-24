select * from UserInfo

insert UserAuth(Id, UserName, ISAuthenticated, Email) values('AE5CE941-DC01-11', 'LeMing', 1, 'dingjonghan@gmail.com')
insert UserPassword(UserId, HashString, EncriptedValue, SaltString) values('AE5CE941-DC01-11', 'abcd1234', '1234abcd', 'xyz')

select * from dbo.[Group]

select * from dbo.[UserPassword]

select * from dbo.[UserAuth] where Id = 'AE5CE941-DC01-11'

insert UserInfo(Id, UserName, FirstName, LastName, Email) values('A5E1EC42-F5FB-40','lmt1202', 'Le','Ming', 'dingjohan@gmail.com.vn')
CREATE database CHATAPP

-- Select rows from a Table or View '[A]' in schema '[dbo]'
SELECT * FROM [dbo].[AspNetUsers]
WHERE /* add search conditions here */
GO

-- Delete rows from table '[TableName]' in schema '[dbo]'

-- Select rows from a Table or View '[Messages]' in schema '[dbo]'
delete from [dbo].[Messages]
WHERE SenderId ='143b6740-1bea-4031-94a4-ee433b0aa51b'
DELETE FROM [dbo].[AspNetUsers]
WHERE Email = 'thinhtang123@gmail.com'
GO

DECLARE @id NVARCHAR(MAX)
set @id = '2a4d62e8-ec3d-4d42-b25b-5dd0e5a59289'
DELETE UserInfo WHERE Id = @id
DELETE AspNetUsers  WHERE AspNetUsers.Id = @id