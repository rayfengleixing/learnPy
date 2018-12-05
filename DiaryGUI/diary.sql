create table diary(
	id int primary key auto_increment,
	title varchar(50) not null,
	mood varchar(20) not null,
	weather varchar(20) not null,
	category varchar(20) not null,
	content text not null,
	c_time datetime
)charset=utf8;

