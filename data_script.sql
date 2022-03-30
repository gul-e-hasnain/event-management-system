--CUSTOMER--
INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(101, 'AHEMD', 4230106532875, 03315256493, 'ahmed56@gmail.com', 'DHA, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(102, 'SALMAN', 4230104558761, 03315566793, 'salman12@gmail.com', 'Korangi, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(103, 'ASAD', 4230101532988, 03215256799, 'asad76@gmail.com', 'Nazimabad, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(104, 'HASNAIN', 4230106522877, 03115259993, 'hasnain99@gmail.com', 'Garden East ,KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(105, 'MURSALEEN', 4230106552815, 03205256693, 'ms45@gmail.com', 'Garden West, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(106, 'SAIMA', 4230106533871, 03315256001, 'saima33@gmail.com', 'Saddar, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(107, 'KAINAT', 4230106558311, 03315259999, 'kainat43@gmail.com', 'Saddar, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(108, 'NOOR', 4230146588871, 03325256251, 'noor56@gmail.com', 'DHA, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(109, 'BILAL', 4230233663386, 03315256661, 'bilal89@gmail.com', 'Nazimabad, KARACHI');

INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerNIC, CustomerContact, CustomerEmail, CustomerAddress)
VALUES(110, 'ARSHAD', 4230186533879, 03315254231, 'arshad22@gmail.com', 'Gulshan, KARACHI');


--Employee--
INSERT INTO Employee(EmployeeID, EmployeeName, EmployeeEmail, EmployeeContact, EmployeeAddress, EmployeeHiredate, EmployeeSalary)
VALUES(1001, 'AQSA NAZ', 'aqsanaz03@gmail.com', 03123782841, 'Gulshan e Iqbal, Karchi', TO_DATE('01-Jan-2021','DD-MON-YYYY'), 80000);

INSERT INTO Employee(EmployeeID, EmployeeName, EmployeeEmail, EmployeeContact, EmployeeAddress, EmployeeHiredate, EmployeeSalary)
VALUES(1002, 'GUL E HASNAIN', 'gulehasnain03@gmail.com', 03313802395, 'Garden West, Karchi', TO_DATE('22-Jan-2021','DD-MON-YYYY'), 75000);

INSERT INTO Employee(EmployeeID, EmployeeName, EmployeeEmail, EmployeeContact, EmployeeAddress, EmployeeHiredate, EmployeeSalary)
VALUES(1003, 'AHTISHAM', 'mahtisham@gmail.com', 03148003018, 'DHA, Karchi', TO_DATE('31-Jan-2021','DD-MON-YYYY'), 75000);

INSERT INTO Employee(EmployeeID, EmployeeName, EmployeeEmail, EmployeeContact, EmployeeAddress, EmployeeHiredate, EmployeeSalary)
VALUES(1004, 'ASAD ALI NAJEEB', 'asadali03@gmail.com', 03217625465, 'Nazimabad, Karchi', TO_DATE('8-Mar-2021','DD-MON-YYYY'), 50000);

INSERT INTO Employee(EmployeeID, EmployeeName, EmployeeEmail, EmployeeContact, EmployeeAddress, EmployeeHiredate, EmployeeSalary)
VALUES(1005, 'ROHA RAFAQAT', 'roharafaqat76@gmail.com', 03317885657, 'Gulshan e iqbal, Karchi', TO_DATE('15-Jun-2021','DD-MON-YYYY'), 40000);

--Venue--
INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(101, 'Medallion Banquet', 'Shahra-e-Faisal, Karachi', 800, 03217643822, 70000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(102, 'Redisson Banquet', 'Defense View, Phase 1, Karachi', 1000, 03229643462, 75000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(103, 'Paradise Banquet', 'Gulistan-e-Johar Munawar Chorangi, Karachi', 500, 03331355356, 40000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(104, 'Victoria Banquet', 'Main Shahrah-e-Faisal, Karachi ', 700, 03145263746, 50000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(105, 'Courtyard Banquet', 'Main Alamgir Road, Bahadurabad Karachi', 650, 03158737643, 75000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(106, 'The Meadows Banquet', 'Block 14 Gulistan-e-Johar Karachi', 1200, 03327634582, 60000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(107, 'Arena Club Karsaz', 'Karsaz Road, Karachi', 1500, 03329914367, 100000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(108, 'Pearl Continental', 'Club Road, Civil Lines, Karachi', 2000, 03154354822, 120000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(109, 'Karachi Marriott Hotel', 'Abdullah Haroon Rd, Civil Lines Karachi', 1600, 03313876543, 100000);

INSERT INTO VENUE(VenueID, VenueName, VenueAddress, VenueCapacity, VenueContact, VenueCost)
VALUES(110, 'Majestic Banquet', 'M.A.M.C.H Society Main Shahrah-e-Faisal, Karachi', 1200, 03213425876, 90000);


--VENDOR--
INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(10, 'ARHAM FOODS', 03134526757, 'MEHMODABAD, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(20, 'STUDENT BIRYANI', 03124429751, 'GULSHAN E IQBAL, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(30, 'QILA FOODS', 03156529753, 'BAHADURABAD, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(40, 'HENSON FOODS', 03157899401, 'FB Area Block-21, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(50, 'AHMED FOOD LIMITED', 03359356123, 'ABDULAH AHMED ROAD, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(60, 'EAT FOODS', 03146036163, 'GLASS TOWER CLIFTON, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(70, 'CITY FOODS', 03327125924, 'SADDAR PREEDY QUATERS, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(80, 'KASHIF FOODS', 03349167243, 'GULSHAN E IQBAL, KARACHI');

INSERT INTO VENDOR(VendorID, VendorName, VendorContact, VendorAddress)
VALUES(90, 'FOOD MASTER GROUPS', 03116835619, 'GULISTAN E JOHAR, KARACHI');


--decoration--
INSERT INTO Decoration(DecorationID, DecorationType, DecorationCost)
VALUES(10, 'CLASSIC', 15000);

INSERT INTO Decoration(DecorationID, DecorationType, DecorationCost)
VALUES(20, 'ROYAL', 20000);

INSERT INTO Decoration(DecorationID, DecorationType, DecorationCost)
VALUES(30, 'PLATINUM', 25000);

INSERT INTO Decoration(DecorationID, DecorationType, DecorationCost)
VALUES(40, 'PREMIUM', 30000);


--SERVICE--
INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(10, 'DJ', 10000);

INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(20, 'CHAIR', 50);

INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(30, 'TABLE', 50);

INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(40, 'CARPETS', 5000);

INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(50, 'STAGE', 6000);

INSERT INTO SERVICE(ServiceID, ServiceName, ServiceCost)
VALUES(60, 'PHOTOGRAPHER', 15000);

-------------------------------
--Event Type--
INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(10, 'BIRTHDAY PARTY');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(20, 'MARRIGE');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(30, 'MEHENDI');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(40, 'RECEPTION');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(50, 'FAREWELL PARTY');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(60, 'CONCERT');

INSERT INTO EventType(EventTypeID, EventTypeName)
VALUES(70, 'QAWALI NIGHT');


--food--
INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(10, 'CHICKEN BIRYANI',80 ,20);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(20, 'BEEF BIRYANI', 100, 20);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(30, 'BEEF PULAO', 100, 20);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(40, 'CHICKEN TIKKA', 140, 10);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(50, 'CHICKEN BOTI', 160, 10);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(60, 'BEEF KABAB', 160, 10);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(70, 'KHEER', 100, 30);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(80, 'RAS MALAI', 100, 30);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(90, 'ICE CREAM', 50 ,30);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(100, 'GULAB JAMUN', 20 ,70);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(110, 'CHAPLI KABAB', 40 ,50);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(120, 'COLD DRINK', 35 ,60);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(130, 'RAITA', 30 ,60);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(140, 'SALAD', 25 ,60);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(150, 'NAN', 10 ,60);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(160, 'MUTTON KORMA', 120 ,70);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(170, 'MUTTON BIRYANI', 120 ,70);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(180, 'CHICKEN KARHAI', 120 ,80);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(190, 'BEEF KARHAI', 150 ,80);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(200, 'MUTTON KARHAI', 180 ,80);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(210, 'PASTRY', 30 ,90);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(220, 'CHINESE RICE WITH GRAVY', 120 ,40);

INSERT INTO FOOD(ItemID, ItemName, ItemUnitCost,VendorID)
VALUES(230, 'SINGAPORIAN RICE', 150 ,40);

--EVENT--
INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1001, 10, 10, TO_DATE('02-MAR-2021', 'DD-MON-YYYY'), 400, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 107), 104, 1003);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1002, 70, 20, TO_DATE('10-MAR-2021', 'DD-MON-YYYY'), 800, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 101), 105, 1001);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1003, 40, 20, TO_DATE('12-APR-2021', 'DD-MON-YYYY'), 600, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 105), 101, 1002);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1004, 50, 30, TO_DATE('25-APR-2021', 'DD-MON-YYYY'), 500, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 109), 108, 1005);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1005, 20, 30, TO_DATE('05-MAY-2021', 'DD-MON-YYYY'), 900, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 102), 110, 1004);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1006, 60, 40, TO_DATE('17-MAY-2021', 'DD-MON-YYYY'), 1000, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 110), 102, 1003);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1007, 30, 10, TO_DATE('17-MAY-2021', 'DD-MON-YYYY'), 500, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 103), 103, 1001);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1008, 20, 30, TO_DATE('17-MAY-2021', 'DD-MON-YYYY'), 800, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 101), 106, 1002);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1009, 40, 40, TO_DATE('17-MAY-2021', 'DD-MON-YYYY'), 1200, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 108), 107, 1004);

INSERT INTO EVENT(EventID, EventTypeID, DecorationID, EventDate, NoOfGuest, EventAdvancePayment, CustomerID, EmployeeID)
VALUES(1010, 70, 10, TO_DATE('17-MAY-2021', 'DD-MON-YYYY'), 1000, (SELECT VENUECOST*0.50 FROM VENUE WHERE VENUEID = 106), 109, 1005);

--FOOD DETAIL--
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001,10, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001,210, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001,120, 600);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001, 140, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001,130, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001,160, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1001, 150, 200);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1002, 20, 500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1002, 40, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1002, 60, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1002, 90, 800);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1002, 120, 1000);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 230, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 200, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 150, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 110, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 140, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1003, 120, 800);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 30, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 40, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 60, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 100, 500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 150, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 120, 650);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1004, 190, 200);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 20, 500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 60, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 70, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 90, 500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 120, 1000);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 140, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 150, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1005, 200, 150);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1006, 10, 1000);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1006, 120, 1200);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 20, 250);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 80, 300);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 50, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 120, 750);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 150, 100);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1007, 180, 150);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 220, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 110, 500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 120, 1000);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 150, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 140, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 130, 50);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 90, 800);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1008, 160, 300);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 30, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 230, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 180, 400);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 60, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 40, 200);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 100, 800);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 120, 1500);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 140, 100);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1009, 150, 300);

INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1010, 20, 1000);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1010, 80, 800);
INSERT INTO FOODDETAIL(EventID, ItemID, ItemQuantity)
VALUES(1010, 120, 1200);


--SERVICE DETAIL--
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1001,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1001,30);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1002,40);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1002,50);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1003,10);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1003,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1003,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1003,50);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1004,10);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1004,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1004,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1004,50);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1005,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1005,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1005,50);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1005,60);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1006,10);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1006,50);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1007,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1007,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1007,50);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1008,10);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1008,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1008,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1008,50);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1008,60);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1009,20);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1009,30);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1009,50);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1009,60);

INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1010,10);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1010,50);
INSERT INTO SERVICEDETAIL(EventID, ServiceID)
VALUES(1010,40);

--EventDetail--
INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1001, 107, 215250);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1002, 101, 328000);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1003, 105, 307800);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1004, 109, 344900);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1005, 102, 648900);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1006, 110, 258000);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1007, 103, 221400);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1008, 108, 518250);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1009, 101, 378750);

INSERT INTO EVENTDETAIL(EventID, VenueID, EventTotalCost)
VALUES(1010, 106, 318000);



--USER--
INSERT INTO USERS(Username, password, UserID)
VALUES('gulehasnain', 'gulehasnain', 1002);

INSERT INTO USERS(Username, password, UserID)
VALUES('aqsanaz', 'aqsanaz', 1001);

INSERT INTO USERS(Username, password, UserID)
VALUES('ahtisham', 'ahtisham', 1003);

INSERT INTO USERS(Username, password, UserID)
VALUES('asadali', 'asadali', 1004);

INSERT INTO USERS(Username, password, UserID)
VALUES('roha', 'roha', 1005);

INSERT INTO USERS(Username, password, UserID)
Values('admin', 'admin', 1000);

commit;















