CREATE TABLE Student (
	std_id decimal PRIMARY KEY AUTOINCREMENT,
	name string,
	email string,
	password string,
	semester decimal,
	contact decimal,
	cgpa float
);

CREATE TABLE Course (
	course_id decimal,
	credit decimal,
	faculty decimal,
	section decimal PRIMARY KEY AUTOINCREMENT,
	capacity decimal,
	std_id decimal,
	class_time datetime
);

CREATE TABLE Complain (
	complain_id decimal PRIMARY KEY AUTOINCREMENT,
	std_id decimal PRIMARY KEY AUTOINCREMENT,
	message string,
	time datetime
);

CREATE TABLE Course_reg (
	std_id decimal,
	course_id decimal,
	limit decimal
);

CREATE TABLE Lost_Found (
	lost_found_id decimal PRIMARY KEY AUTOINCREMENT,
	std_id decimal,
	item string,
	category string
);

CREATE TABLE Coursed_difficulty (
	course_id decimal,
	difficulty decimal
);

CREATE TABLE Faculty_eval (
	std_id decimal,
	course_id decimal,
	rating decimal,
	comment string
);

