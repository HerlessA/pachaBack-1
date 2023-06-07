CREATE DATABASE sv73265099
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table "customer_segment" (
	customer_segment_id smallint not null,
	customer_segment_name varchar(100) not null,
	primary key (customer_segment_id)
);

create table customer (
    customer_id int not null,
	customer_code varchar(255) not null,
	customer_name varchar(255) not null,
    customer_segment_id smallint not null,
	primary key (customer_id),
    foreign key (customer_segment_id) references customer_segment(customer_segment_id)
);

create table postal_code (
    postal_code_id int not null,
    postal_code_number varchar(255) not null,
	primary key (postal_code_id)
);

create table city (
	city_id int not null,
	city_name varchar(100) not null,
    postal_code_id int not null,
	primary key (city_id),
    foreign key (postal_code_id) references postal_code(postal_code_id)
);

create table state (
	state_id int not null,
	state_name varchar(100) not null,
    city_id int not null,
	primary key (state_id),
    foreign key (city_id) references city(city_id)
);

create table region (
	region_id smallint not null,
	region_name varchar(100) not null,
    state_id int not null,
	primary key (region_id),
    foreign key (state_id) references state(state_id)
);

create table product_sub_category (
	product_sub_category_id int not null,
	product_sub_category_name varchar(100) not null,
	primary key (product_sub_category_id)
);

create table product_category (
	product_category_id int not null,
	product_category_name varchar(100) not null,
    product_sub_category_id int not null,
    primary key (product_category_id),
    foreign key (product_sub_category_id) references product_sub_category(product_sub_category_id)
);

create table product (
    product_id int not null,
	product_code varchar(255) not null,
	product_name varchar(255) not null,
    product_category_id int not null,
    primary key (product_id),
    foreign key (product_category_id) references product_category(product_category_id)
);

create table ship_mode (
	ship_mode_id smallint not null,
	ship_mode_name varchar(100) not null,
	primary key (ship_mode_id)
);

create table "order"(
	order_id int not null,
    order_code varchar(255) not null,
    order_date date not null,
    ship_date date not null,
    ship_mode_id smallint not null,
    customer_id int not null,
    region_id smallint not null,
    primary key (order_id),
    foreign key (ship_mode_id) references ship_mode(ship_mode_id),
    foreign key (customer_id) references customer(customer_id),
    foreign key (region_id) references region(region_id)
);



















