-- TABLE
CREATE TABLE Ages
(
   id_a                 int not null,
   age                  int,
   primary key (id_a)
);
CREATE TABLE demo (ID integer primary key, Name varchar(20), Hint text );
CREATE TABLE Names
(
   id_n                 int not null,
   name                 char(10),
   primary key (id_n)
);
CREATE TABLE Positions
(
   id_p                 int not null,
   position             char(10),
   primary key (id_p)
);
CREATE TABLE Salary
(
   id_s                 int not null,
   id_n                 int,
   id_p                 int,
   id_a                 int,
   salary               float,
   primary key (id_s),
   constraint FK_Relationship_1 foreign key (id_n)
      references Names (id_n) on delete restrict on update restrict,
   constraint FK_Relationship_2 foreign key (id_s)
      references Surnames (id_s) on delete restrict on update restrict,
   constraint FK_Relationship_3 foreign key (id_p)
      references Positions (id_p) on delete restrict on update restrict,
   constraint FK_Relationship_4 foreign key (id_a)
      references Ages (id_a) on delete restrict on update restrict
);
CREATE TABLE Surnames
(
   id_s                 int not null,
   surname              char(10),
   primary key (id_s)
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
