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

insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2122-db82-11ed-8c8f-70a6ccc4b566', N'Tăng', N'Huy Kiên', 'kienhuytang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2123-db82-11ed-be8f-70a6ccc4b566', N'Hà', N'Thành Anh Phi', 'phithanhanhha@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2124-db82-11ed-afec-70a6ccc4b566', N'Doãn', N'Luân Anh Nguyên', 'nguyenluananhdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2125-db82-11ed-b8ef-70a6ccc4b566', N'Vũ', N'Hào Nghĩa', 'nghiahaovu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2126-db82-11ed-82af-70a6ccc4b566', N'Doãn', N'Duy Anh Kiên', 'kienduyanhdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2127-db82-11ed-9c5d-70a6ccc4b566', N'Lý', N'Minh Anh Nghĩa', 'nghiaminhanhly@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2128-db82-11ed-bc8b-70a6ccc4b566', N'Đinh', N'Vinh Khanh', 'khanhvinhdinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e2129-db82-11ed-82ec-70a6ccc4b566', N'Lê', N'Ngọc Anh Công', 'congngocanhle@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e212a-db82-11ed-b8a6-70a6ccc4b566', N'Trần', N'Hùng Anh Danh', 'danhhunganhtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e212b-db82-11ed-958a-70a6ccc4b566', N'Phùng', N'Tấn Anh Khải', 'khaitananhphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e212c-db82-11ed-a1b6-70a6ccc4b566', N'Phạm', N'Ngọc Đức', 'ducngocpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e480d-db82-11ed-b26a-70a6ccc4b566', N'Phạm', N'Lộc Phát', 'phatlocpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e480e-db82-11ed-8f94-70a6ccc4b566', N'Phan', N'Phương Hiệp', 'hiepphuongphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e480f-db82-11ed-8652-70a6ccc4b566', N'Vũ', N'Thông Huy', 'huythongvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4810-db82-11ed-b9f5-70a6ccc4b566', N'Phùng', N'Phi Anh Duy', 'duyphianhphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4811-db82-11ed-b2d4-70a6ccc4b566', N'Vũ', N'Nghĩa Tâm', 'tamnghiavu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4812-db82-11ed-92fa-70a6ccc4b566', N'Trịnh', N'Hiếu Anh', 'anhhieutrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4813-db82-11ed-b565-70a6ccc4b566', N'Trịnh', N'Hậu Quân', 'quanhautrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4814-db82-11ed-b2fa-70a6ccc4b566', N'Trần', N'Hoàng Anh Kiệt', 'kiethoanganhtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4815-db82-11ed-bbe7-70a6ccc4b566', N'Hoàng', N'Thái Anh Tường', 'tuongthaianhhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4816-db82-11ed-9799-70a6ccc4b566', N'Doãn', N'Tài Khôi', 'khoitaidoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4817-db82-11ed-9bf6-70a6ccc4b566', N'Phạm', N'Nhựt Hùng', 'hungnhutpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4818-db82-11ed-9587-70a6ccc4b566', N'Lý', N'Lợi Khoa', 'khoaloily@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4819-db82-11ed-945d-70a6ccc4b566', N'Nhâm', N'Tấn Việt', 'viettannham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481a-db82-11ed-8df1-70a6ccc4b566', N'Tăng', N'Đông Anh Bảo', 'baodonganhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481b-db82-11ed-81f6-70a6ccc4b566', N'Vũ', N'Tân Ngọc', 'ngoctanvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481c-db82-11ed-99d1-70a6ccc4b566', N'Đỗ', N'Thanh Nhân', 'nhanthanhdo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481d-db82-11ed-9f5b-70a6ccc4b566', N'Huỳnh', N'Đức Anh Nhật', 'nhatducanhhuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481e-db82-11ed-b81b-70a6ccc4b566', N'Huỳnh', N'Hoàng Vĩ', 'vihoanghuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e481f-db82-11ed-a481-70a6ccc4b566', N'Hoàng', N'Quân Luân', 'luanquanhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4820-db82-11ed-b397-70a6ccc4b566', N'Đỗ', N'Cường Trọng', 'trongcuongdo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4821-db82-11ed-a5ec-70a6ccc4b566', N'Mạc', N'Khang Anh Thái', 'thaikhanganhmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4822-db82-11ed-9a96-70a6ccc4b566', N'Hồ', N'Quý Hùng', 'hungquyho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4823-db82-11ed-8bdc-70a6ccc4b566', N'Nguyễn', N'Tú Anh Trí', 'trituanhnguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4824-db82-11ed-b920-70a6ccc4b566', N'Tăng', N'Trọng Linh', 'linhtrongtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4825-db82-11ed-8cfb-70a6ccc4b566', N'Doãn', N'Quang Anh Quang', 'quangquanganhdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4826-db82-11ed-9341-70a6ccc4b566', N'Huỳnh', N'Ngọc Trọng', 'trongngochuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4827-db82-11ed-b682-70a6ccc4b566', N'Hoàng', N'Anh Tài', 'taianhhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4828-db82-11ed-8b0b-70a6ccc4b566', N'Trịnh', N'Vĩ Thành', 'thanhvitrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4829-db82-11ed-848f-70a6ccc4b566', N'Nhâm', N'Đông Đông', 'dongdongnham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482a-db82-11ed-85ba-70a6ccc4b566', N'Triệu', N'Tú Anh Hưng', 'hungtuanhtrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482b-db82-11ed-ab1c-70a6ccc4b566', N'Hoàng', N'Bảo Anh Thiện', 'thienbaoanhhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482c-db82-11ed-bf5e-70a6ccc4b566', N'Nhâm', N'Kỳ An', 'ankynham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482d-db82-11ed-8ac2-70a6ccc4b566', N'Nhâm', N'Khang Tiến', 'tienkhangnham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482e-db82-11ed-b9c2-70a6ccc4b566', N'Mạc', N'Tuấn Anh Nhân', 'nhantuananhmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e482f-db82-11ed-a7aa-70a6ccc4b566', N'Ngô', N'Trọng Trường', 'truongtrongngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4830-db82-11ed-95df-70a6ccc4b566', N'Mạc', N'Thuận Long', 'longthuanmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4831-db82-11ed-8081-70a6ccc4b566', N'Phan', N'Lâm Trung', 'trunglamphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4832-db82-11ed-b2b2-70a6ccc4b566', N'Phùng', N'Hưng Long', 'longhungphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4833-db82-11ed-a2aa-70a6ccc4b566', N'Mạc', N'Kha Khiêm', 'khiemkhamac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4834-db82-11ed-9de8-70a6ccc4b566', N'Nhâm', N'Phát Hùng', 'hungphatnham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4835-db82-11ed-bc3a-70a6ccc4b566', N'Huỳnh', N'Huy Anh Hòa', 'hoahuyanhhuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4836-db82-11ed-93f3-70a6ccc4b566', N'Thân', N'Tú Anh Thắng', 'thangtuanhthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4837-db82-11ed-8563-70a6ccc4b566', N'Ngô', N'Khanh Lộc', 'lockhanhngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4838-db82-11ed-971d-70a6ccc4b566', N'Ngô', N'Hùng Anh Khải', 'khaihunganhngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4839-db82-11ed-8916-70a6ccc4b566', N'Hồ', N'Tuấn Anh Nhân', 'nhantuananhho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483a-db82-11ed-a0c8-70a6ccc4b566', N'Trần', N'Vương Phương', 'phuongvuongtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483b-db82-11ed-bbe4-70a6ccc4b566', N'Hồ', N'Hùng Kỳ', 'kyhungho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483c-db82-11ed-9782-70a6ccc4b566', N'Huỳnh', N'Trí Dương', 'duongtrihuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483d-db82-11ed-ab1c-70a6ccc4b566', N'Thân', N'Duy Anh Sơn', 'sonduyanhthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483e-db82-11ed-87b9-70a6ccc4b566', N'Phùng', N'Vỹ Sơn', 'sonvyphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e483f-db82-11ed-8dd4-70a6ccc4b566', N'Phạm', N'Khanh Khánh', 'khanhkhanhpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4840-db82-11ed-b770-70a6ccc4b566', N'Hồ', N'Khanh Huy', 'huykhanhho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4841-db82-11ed-81ed-70a6ccc4b566', N'Đinh', N'Hoàng Anh Đạt', 'dathoanganhdinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4842-db82-11ed-8d2c-70a6ccc4b566', N'Trịnh', N'Việt Anh Lợi', 'loivietanhtrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4843-db82-11ed-bd4c-70a6ccc4b566', N'Ngô', N'Luân Anh Tín', 'tinluananhngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4844-db82-11ed-8849-70a6ccc4b566', N'Huỳnh', N'Hiệp Khoa', 'khoahiephuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4845-db82-11ed-b224-70a6ccc4b566', N'Ngô', N'Khiêm Triết', 'trietkhiemngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4846-db82-11ed-b1af-70a6ccc4b566', N'Tăng', N'Khang Hào', 'haokhangtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4847-db82-11ed-ae16-70a6ccc4b566', N'Đinh', N'Khôi Đức', 'duckhoidinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4848-db82-11ed-bc13-70a6ccc4b566', N'Đinh', N'Kha Hiệp', 'hiepkhadinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e4849-db82-11ed-b156-70a6ccc4b566', N'Mạc', N'Tâm Tường', 'tuongtammac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e484a-db82-11ed-a00b-70a6ccc4b566', N'Tăng', N'Mạnh Anh Hưng', 'hungmanhanhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e484b-db82-11ed-aba9-70a6ccc4b566', N'Thân', N'Hiển Dương', 'duonghienthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e484c-db82-11ed-a8b1-70a6ccc4b566', N'Hoàng', N'Khanh Kha', 'khakhanhhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e484d-db82-11ed-998e-70a6ccc4b566', N'Doãn', N'Trường Khiêm', 'khiemtruongdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e484e-db82-11ed-af17-70a6ccc4b566', N'Dương', N'Khiêm Bách', 'bachkhiemduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef1-db82-11ed-ab9f-70a6ccc4b566', N'Phạm', N'Vĩ Nguyên', 'nguyenvipham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef2-db82-11ed-ae74-70a6ccc4b566', N'Trịnh', N'Minh Thiện', 'thienminhtrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef3-db82-11ed-b243-70a6ccc4b566', N'Hồ', N'Nhân Đông', 'dongnhanho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef4-db82-11ed-af63-70a6ccc4b566', N'Trịnh', N'Quân Trí', 'triquantrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef5-db82-11ed-9562-70a6ccc4b566', N'Triệu', N'Khang Anh Mạnh', 'manhkhanganhtrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef6-db82-11ed-b5e6-70a6ccc4b566', N'Doãn', N'Luân Nhựt', 'nhutluandoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef7-db82-11ed-a745-70a6ccc4b566', N'Triệu', N'Văn Anh Đạt', 'datvananhtrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef8-db82-11ed-a623-70a6ccc4b566', N'Doãn', N'Tân Vũ', 'vutandoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6ef9-db82-11ed-83fe-70a6ccc4b566', N'Triệu', N'Tín Tâm', 'tamtintrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6efa-db82-11ed-b02a-70a6ccc4b566', N'Thân', N'Giang Kiệt', 'kietgiangthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6efb-db82-11ed-bcd8-70a6ccc4b566', N'Hà', N'Thành Anh Kỳ', 'kythanhanhha@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6efc-db82-11ed-82c3-70a6ccc4b566', N'Phạm', N'Vương Thông', 'thongvuongpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6efd-db82-11ed-b703-70a6ccc4b566', N'Vũ', N'Tài Vương', 'vuongtaivu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6efe-db82-11ed-9dae-70a6ccc4b566', N'Lý', N'Tuấn Anh Đức', 'ductuananhly@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6eff-db82-11ed-a735-70a6ccc4b566', N'Doãn', N'Kha Phúc', 'phuckhadoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f00-db82-11ed-bede-70a6ccc4b566', N'Võ', N'Tài Phú', 'phutaivo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f01-db82-11ed-b1fc-70a6ccc4b566', N'Trương', N'Tiến Anh Tài', 'taitienanhtruong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f02-db82-11ed-a559-70a6ccc4b566', N'Nguyễn', N'Phương Bình', 'binhphuongnguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f03-db82-11ed-83ef-70a6ccc4b566', N'Vũ', N'Quý Phú', 'phuquyvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f04-db82-11ed-b97b-70a6ccc4b566', N'Nguyễn', N'Lợi Tường', 'tuongloinguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f05-db82-11ed-b496-70a6ccc4b566', N'Trịnh', N'Đạt Anh Tâm', 'tamdatanhtrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f06-db82-11ed-8ac3-70a6ccc4b566', N'Đinh', N'Lộc Hải', 'hailocdinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('c54e6f07-db82-11ed-9317-70a6ccc4b566', N'Thân', N'Đông Anh Tài', 'taidonganhthan@cloudclass.software', GETDATE());

insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034a-db82-11ed-926c-70a6ccc4b566', N'Doãn', N'Di Tú', 'tudidoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034b-db82-11ed-b40a-70a6ccc4b566', N'Tăng', N'Vi Trà', 'travitang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034c-db82-11ed-82da-70a6ccc4b566', N'Dương', N'Tú Thủy', 'thuytuduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034d-db82-11ed-a300-70a6ccc4b566', N'Nhâm', N'Xuân Anh Lan', 'lanxuananhnham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034e-db82-11ed-a794-70a6ccc4b566', N'Đỗ', N'Thy Anh Nguyên', 'nguyenthyanhdo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001034f-db82-11ed-b7bf-70a6ccc4b566', N'Thân', N'Hồng Khuê', 'khuehongthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010350-db82-11ed-a273-70a6ccc4b566', N'Vũ', N'Tuệ Yến', 'yentuevu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010351-db82-11ed-bc7b-70a6ccc4b566', N'Mạc', N'Tuệ Anh Đào', 'daotueanhmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010352-db82-11ed-846a-70a6ccc4b566', N'Vũ', N'Lan Khuê', 'khuelanvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010353-db82-11ed-8b65-70a6ccc4b566', N'Đỗ', N'Hằng Thy', 'thyhangdo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010354-db82-11ed-a129-70a6ccc4b566', N'Võ', N'Nhiên Băng', 'bangnhienvo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010355-db82-11ed-9d6f-70a6ccc4b566', N'Doãn', N'Đan Anh Khanh', 'khanhdananhdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010356-db82-11ed-b786-70a6ccc4b566', N'Trần', N'Linh Thơ', 'tholinhtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010357-db82-11ed-bc5c-70a6ccc4b566', N'Doãn', N'Tú Dương', 'duongtudoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010358-db82-11ed-8315-70a6ccc4b566', N'Tăng', N'Minh Anh Nguyệt', 'nguyetminhanhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010359-db82-11ed-a273-70a6ccc4b566', N'Trương', N'Mai Thi', 'thimaitruong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035a-db82-11ed-822f-70a6ccc4b566', N'Ngô', N'Trâm Anh Nhàn', 'nhantramanhngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035b-db82-11ed-a2e4-70a6ccc4b566', N'Nguyễn', N'Hằng Băng', 'banghangnguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035c-db82-11ed-9bd0-70a6ccc4b566', N'Phạm', N'My Mẫn', 'manmypham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035d-db82-11ed-bf7b-70a6ccc4b566', N'Lý', N'Mỹ Anh Thi', 'thimyanhly@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035e-db82-11ed-b8fb-70a6ccc4b566', N'Đỗ', N'Thy Anh Vi', 'vithyanhdo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001035f-db82-11ed-8649-70a6ccc4b566', N'Doãn', N'Hân Anh Kim', 'kimhananhdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010360-db82-11ed-9a47-70a6ccc4b566', N'Phùng', N'Hồng Anh Chi', 'chihonganhphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010361-db82-11ed-bba5-70a6ccc4b566', N'Phùng', N'Hạnh Loan', 'loanhanhphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010362-db82-11ed-b585-70a6ccc4b566', N'Lê', N'Hồng Phương', 'phuonghongle@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010363-db82-11ed-947f-70a6ccc4b566', N'Trần', N'Hồng Anh Trang', 'tranghonganhtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010364-db82-11ed-aff8-70a6ccc4b566', N'Triệu', N'Trâm Nghi', 'nghitramtrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010365-db82-11ed-bf6c-70a6ccc4b566', N'Phan', N'Băng Giang', 'giangbangphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010366-db82-11ed-8ae4-70a6ccc4b566', N'Ngô', N'Tuệ Vi', 'vituengo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010367-db82-11ed-a008-70a6ccc4b566', N'Hoàng', N'Trinh Huyền', 'huyentrinhhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70010368-db82-11ed-8ed4-70a6ccc4b566', N'Mạc', N'Nghi Anh Huyền', 'huyennghianhmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a3f-db82-11ed-990f-70a6ccc4b566', N'Phan', N'Trang Anh Hương', 'huongtranganhphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a40-db82-11ed-a032-70a6ccc4b566', N'Phan', N'Tâm Anh Băng', 'bangtamanhphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a41-db82-11ed-8516-70a6ccc4b566', N'Đinh', N'Minh Vi', 'viminhdinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a42-db82-11ed-abfa-70a6ccc4b566', N'Vũ', N'Thy Anh Hà', 'hathyanhvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a43-db82-11ed-b532-70a6ccc4b566', N'Dương', N'Tuệ Hoa', 'hoatueduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a44-db82-11ed-be1f-70a6ccc4b566', N'Dương', N'Nhã Diễm', 'diemnhaduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a45-db82-11ed-97e1-70a6ccc4b566', N'Dương', N'Tú Hương', 'huongtuduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a46-db82-11ed-9cbc-70a6ccc4b566', N'Trương', N'Trâm Anh Trinh', 'trinhtramanhtruong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a47-db82-11ed-9c13-70a6ccc4b566', N'Nhâm', N'Hồng Mai', 'maihongnham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a48-db82-11ed-8c9d-70a6ccc4b566', N'Vũ', N'Lâm Dương', 'duonglamvu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a49-db82-11ed-afdc-70a6ccc4b566', N'Đinh', N'Tú Băng', 'bangtudinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4a-db82-11ed-9eab-70a6ccc4b566', N'Nguyễn', N'Thơ Yến', 'yenthonguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4b-db82-11ed-a9e6-70a6ccc4b566', N'Mạc', N'Tường Linh', 'linhtuongmac@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4c-db82-11ed-a455-70a6ccc4b566', N'Trần', N'Anh Phương', 'phuonganhtran@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4d-db82-11ed-a75a-70a6ccc4b566', N'Phạm', N'Trúc Dung', 'dungtrucpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4e-db82-11ed-9d4e-70a6ccc4b566', N'Huỳnh', N'Lan Anh Ngân', 'nganlananhhuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a4f-db82-11ed-b572-70a6ccc4b566', N'Hồ', N'Hà Tuyền', 'tuyenhaho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a50-db82-11ed-8ea0-70a6ccc4b566', N'Tăng', N'Dung Anh Nhã', 'nhadunganhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a51-db82-11ed-ad65-70a6ccc4b566', N'Triệu', N'Trân Tuệ', 'tuetrantrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a52-db82-11ed-9f13-70a6ccc4b566', N'Lê', N'Diệp Anh Hà', 'hadiepanhle@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a53-db82-11ed-a203-70a6ccc4b566', N'Tăng', N'Như Lan', 'lannhutang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a54-db82-11ed-b750-70a6ccc4b566', N'Phùng', N'Bích Dương', 'duongbichphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a55-db82-11ed-934a-70a6ccc4b566', N'Đinh', N'Thương Xuân', 'xuanthuongdinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a56-db82-11ed-adec-70a6ccc4b566', N'Đỗ', N'Ngân Oanh', 'oanhngando@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a57-db82-11ed-839b-70a6ccc4b566', N'Đinh', N'Quyên Thảo', 'thaoquyendinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a58-db82-11ed-bc30-70a6ccc4b566', N'Phùng', N'Vy Diệu', 'dieuvyphung@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a59-db82-11ed-a42e-70a6ccc4b566', N'Ngô', N'Giang Giang', 'gianggiangngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5a-db82-11ed-9862-70a6ccc4b566', N'Hoàng', N'Quyên Chi', 'chiquyenhoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5b-db82-11ed-b7a4-70a6ccc4b566', N'Phan', N'Như Anh Ân', 'annhuanhphan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5c-db82-11ed-a3d8-70a6ccc4b566', N'Hoàng', N'Thương Hạnh', 'hanhthuonghoang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5d-db82-11ed-b082-70a6ccc4b566', N'Vũ', N'Nga Thúy', 'thuyngavu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5e-db82-11ed-aba7-70a6ccc4b566', N'Võ', N'Kiều Anh Bích', 'bichkieuanhvo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a5f-db82-11ed-a56d-70a6ccc4b566', N'Trương', N'Huyền Anh Anh', 'anhhuyenanhtruong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a60-db82-11ed-9d20-70a6ccc4b566', N'Hồ', N'Ân Thắm', 'thamanho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a61-db82-11ed-8dbf-70a6ccc4b566', N'Huỳnh', N'Nghi Anh Phụng', 'phungnghianhhuynh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a62-db82-11ed-aaf6-70a6ccc4b566', N'Võ', N'Nhung Anh', 'anhnhungvo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a63-db82-11ed-aebb-70a6ccc4b566', N'Doãn', N'Kim Vân', 'vankimdoan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a64-db82-11ed-a715-70a6ccc4b566', N'Thân', N'Dương Hân', 'handuongthan@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a65-db82-11ed-bb7a-70a6ccc4b566', N'Phạm', N'Thùy Anh Mỹ', 'mythuyanhpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a66-db82-11ed-9335-70a6ccc4b566', N'Ngô', N'Tuệ Tuệ', 'tuetuengo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a67-db82-11ed-be15-70a6ccc4b566', N'Trương', N'Ngọc Hiếu', 'hieungoctruong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a68-db82-11ed-98d9-70a6ccc4b566', N'Lê', N'Yến Anh', 'anhyenle@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a69-db82-11ed-9078-70a6ccc4b566', N'Ngô', N'Lan Anh Diệu', 'dieulananhngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a6a-db82-11ed-9883-70a6ccc4b566', N'Lý', N'Trâm Thắm', 'thamtramly@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a6b-db82-11ed-8bbd-70a6ccc4b566', N'Hồ', N'Thi Như', 'nhuthiho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70012a6c-db82-11ed-95c4-70a6ccc4b566', N'Võ', N'Thy Anh Quân', 'quanthyanhvo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001511f-db82-11ed-bf4f-70a6ccc4b566', N'Tăng', N'Xuân Anh Nhàn', 'nhanxuananhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015120-db82-11ed-a57f-70a6ccc4b566', N'Nguyễn', N'Thy Anh Tú', 'tuthyanhnguyen@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015121-db82-11ed-aafd-70a6ccc4b566', N'Dương', N'Diệu Nhã', 'nhadieuduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015122-db82-11ed-a2b6-70a6ccc4b566', N'Lý', N'Tâm Anh Quyên', 'quyentamanhly@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015123-db82-11ed-9e3d-70a6ccc4b566', N'Hồ', N'Loan Thảo', 'thaoloanho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015124-db82-11ed-8428-70a6ccc4b566', N'Hà', N'Phương Anh Giang', 'giangphuonganhha@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015125-db82-11ed-9c4f-70a6ccc4b566', N'Tăng', N'Oanh Trà', 'traoanhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015126-db82-11ed-88cd-70a6ccc4b566', N'Triệu', N'Trúc Đào', 'daotructrieu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015127-db82-11ed-8025-70a6ccc4b566', N'Đinh', N'Nga Tường', 'tuongngadinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015128-db82-11ed-be1c-70a6ccc4b566', N'Dương', N'Lam Nga', 'ngalamduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015129-db82-11ed-922e-70a6ccc4b566', N'Tăng', N'Mỹ Như', 'nhumytang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512a-db82-11ed-98c2-70a6ccc4b566', N'Tăng', N'Diệp Anh Nguyệt', 'nguyetdiepanhtang@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512b-db82-11ed-b3a6-70a6ccc4b566', N'Hồ', N'Phụng Thương', 'thuongphungho@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512c-db82-11ed-b674-70a6ccc4b566', N'Phạm', N'Lam Anh Khuê', 'khuelamanhpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512d-db82-11ed-93fb-70a6ccc4b566', N'Trịnh', N'Trân Anh Hân', 'hantrananhtrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512e-db82-11ed-bf3f-70a6ccc4b566', N'Trịnh', N'Mi Nghi', 'nghimitrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('7001512f-db82-11ed-9cbe-70a6ccc4b566', N'Vũ', N'Hà Quân', 'quanhavu@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015130-db82-11ed-859f-70a6ccc4b566', N'Hà', N'Uyên Tường', 'tuonguyenha@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015131-db82-11ed-8607-70a6ccc4b566', N'Ngô', N'Quyên Hạnh', 'hanhquyenngo@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015132-db82-11ed-bf20-70a6ccc4b566', N'Dương', N'Kiều Vi', 'vikieuduong@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015133-db82-11ed-b845-70a6ccc4b566', N'Trịnh', N'An Anh Phụng', 'phungananhtrinh@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015134-db82-11ed-b55f-70a6ccc4b566', N'Phạm', N'Lam Anh Uyên', 'uyenlamanhpham@cloudclass.software', GETDATE());
insert UserInfo(Id, FirstName, LastName, Email, JoinedDate) values('70015135-db82-11ed-8681-70a6ccc4b566', N'Trương', N'Nguyên Tiên', 'tiennguyentruong@cloudclass.software', GETDATE());

select * from dbo.[group]

SELECT * from UserInfo

select * from JoinedMember

DELETE JoinedMember
delete dbo.[group]

insert dbo.[Group](Id,GroupName, CreatedTime, CreatorId) values(NEWID(), N'Nhóm hỗ trợ giáo viên', GETDATE(), N'70015125-db82-11ed-9c4f-70a6ccc4b566')
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'70015125-db82-11ed-9c4f-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'7001034d-db82-11ed-a300-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'7001034e-db82-11ed-a794-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'70012a66-db82-11ed-9335-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'70012a67-db82-11ed-be15-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8', N'70015120-db82-11ed-a57f-70a6ccc4b566', GETDATE())

insert dbo.[Group](Id,GroupName, CreatedTime, CreatorId) values(NEWID(), N'Nhóm hỗ trợ sinh viên', GETDATE(), N'70015135-db82-11ed-8681-70a6ccc4b566')
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015135-db82-11ed-8681-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015125-db82-11ed-9c4f-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001034d-db82-11ed-a300-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001034e-db82-11ed-a794-70a6ccc4b566', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a42-db82-11ed-abfa-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a43-db82-11ed-b532-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a44-db82-11ed-be1f-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a45-db82-11ed-97e1-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a46-db82-11ed-9cbc-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a47-db82-11ed-9c13-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a48-db82-11ed-8c9d-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a49-db82-11ed-afdc-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4a-db82-11ed-9eab-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4b-db82-11ed-a9e6-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4c-db82-11ed-a455-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4d-db82-11ed-a75a-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4e-db82-11ed-9d4e-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a4f-db82-11ed-b572-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a50-db82-11ed-8ea0-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a51-db82-11ed-ad65-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a52-db82-11ed-9f13-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a53-db82-11ed-a203-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a54-db82-11ed-b750-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a55-db82-11ed-934a-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a56-db82-11ed-adec-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a57-db82-11ed-839b-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a58-db82-11ed-bc30-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a59-db82-11ed-a42e-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5a-db82-11ed-9862-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5b-db82-11ed-b7a4-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5c-db82-11ed-a3d8-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5d-db82-11ed-b082-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5e-db82-11ed-aba7-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a5f-db82-11ed-a56d-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a60-db82-11ed-9d20-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a61-db82-11ed-8dbf-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a62-db82-11ed-aaf6-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a63-db82-11ed-aebb-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a64-db82-11ed-a715-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a65-db82-11ed-bb7a-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a66-db82-11ed-9335-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a67-db82-11ed-be15-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a68-db82-11ed-98d9-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a69-db82-11ed-9078-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a6a-db82-11ed-9883-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a6b-db82-11ed-8bbd-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70012a6c-db82-11ed-95c4-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001511f-db82-11ed-bf4f-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015120-db82-11ed-a57f-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015121-db82-11ed-aafd-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015122-db82-11ed-a2b6-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015123-db82-11ed-9e3d-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015124-db82-11ed-8428-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015126-db82-11ed-88cd-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015127-db82-11ed-8025-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015128-db82-11ed-be1c-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'70015129-db82-11ed-922e-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001512a-db82-11ed-98c2-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001512b-db82-11ed-b3a6-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001512c-db82-11ed-b674-70a6ccc4b566', GETDATE());
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477', N'7001512d-db82-11ed-93fb-70a6ccc4b566', GETDATE());

select * from dbo.[JoinedMember]  GRoupID where memberId = N'3622BBFB-EE0A-47'

insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8',  N'3622BBFB-EE0A-47', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'E4B262D9-B49D-43DF-819B-E31C0BE73477',  N'3622BBFB-EE0A-47', GETDATE())

insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'EB06F381-A911-45',  N'3622BBFB-EE0A-47', GETDATE())
insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'78A212DB-926A-4828-85A3-E62E94A2CDF8',  N'3622BBFB-EE0A-47', GETDATE())

SELECT * from dbo.[Group]

select DISTINCT(GroupId) from JoinedMember 

select * from JoinedMember WHERE GroupId = '78A212DB-926A-4828-85A3-E62E94A2CDF8'

select * from JoinedMember WHERE MemberId = '7001034d-db82-11ed-a300-70a6ccc4b566'
DELETE JoinedMember

insert JoinedMember(Id, GroupId, MemberId, JoinedTime) VALUES(NEWID(), N'EB06F381-A911-45',  N'3622BBFB-EE0A-47', GETDATE())

insert MESSAGE (Id, Content, CreatedTime, GroupId, SenderId) VALUES (NEWID(), N'Báo tiếng thái viết bằng tiếng việt', GETDATE(), '78A212DB-926A-4828-85A3-E62E94A2CDF8', '3622BBFB-EE0A-47')
select * from [Message]