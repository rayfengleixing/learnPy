create table diary(
	id int primary key auto_increment,
	weather varchar(50) not null,
	mood varchar(50) not null,
	content text not null,
	c_time datetime
)charset=utf8;


