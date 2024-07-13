create table Ages
(
   id_a                 int not null,
   age                  int,
   primary key (id_a)
);

create table Names
(
   id_n                 int not null,
   name                 char(10),
   primary key (id_n)
);

create table Prem
(
   id_p                 int not null,
   prem                 int,
   primary key (id_p)
);

create table Surnames
(
   id_s                 int not null,
   surname              char(10),
   primary key (id_s)
);

create table Salary
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
      references Prem (id_p) on delete restrict on update restrict,
   constraint FK_Relationship_4 foreign key (id_a)
      references Ages (id_a) on delete restrict on update restrict
);
