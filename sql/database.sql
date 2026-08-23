CREATE TABLE Device_Type ( 
    Type_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Type_Name VARCHAR2(50) NOT NULL
);

CREATE TABLE Device (
    Device_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Name VARCHAR2(100) NOT NULL,
    IP_Address VARCHAR2(45) NOT NULL,
    MAC_Address VARCHAR2(17) NOT NULL UNIQUE,
    Status VARCHAR2(20) DEFAULT 'Unknown',
    Type_ID NUMBER
);

CREATE TABLE Connection (
    Connection_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Source_Device_ID NUMBER NOT NULL,
    Destination_Device_ID NUMBER NOT NULL,
    Connection_Type VARCHAR2(50) NOT NULL, 
Network_ID number 
);

CREATE TABLE Network(
    Network_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Network_ Name varchar2(20) 
);

-- 2. Add Foreign Keys

ALTER TABLE Device
ADD CONSTRAINT FK_Device_DeviceType
FOREIGN KEY (Type_ID) REFERENCES Device_Type(Type_ID) ON DELETE SET NULL;

ALTER TABLE Connection
ADD CONSTRAINT FK_Connection_SourceDevice
FOREIGN KEY (Source_Device_ID) REFERENCES Device(Device_ID) ON DELETE CASCADE;

ALTER TABLE Connection
ADD CONSTRAINT FK_Connection_DestDevice
FOREIGN KEY (Destination_Device_ID) REFERENCES Device(Device_ID) ON DELETE CASCADE;

ALTER TABLE Connection
ADD CONSTRAINT FK_Connection_Network
FOREIGN KEY (Network_ID) REFERENCES Network (Network_ID ) ON DELETE CASCADE;

Insert Device Types

INSERT INTO Device_Type (Type_Name)
VALUES ('Router');

INSERT INTO Device_Type (Type_Name)
VALUES ('Switch');

INSERT INTO Device_Type (Type_Name)
VALUES ('Server');

INSERT INTO Device_Type (Type_Name)
VALUES ('Access Point');

INSERT INTO Device_Type (Type_Name)
VALUES ('PC');

INSERT INTO Device_Type (Type_Name)
VALUES ('Modem');                                         

INSERT INTO Device_Type (Type_Name)
VALUES ('FireWall');

COMMIT;