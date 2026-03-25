CREATE DATABASE Project;
USE Project;

CREATE TABLE patient (
    p_number BIGINT PRIMARY KEY,
    p_name VARCHAR(100),
    p_email VARCHAR(100),
    p_city VARCHAR(50),
    p_age INT
);

CREATE TABLE doctor (
    d_number BIGINT PRIMARY KEY,
    d_name VARCHAR(100),
    d_email VARCHAR(100),
    d_city VARCHAR(50),
    d_address VARCHAR(100)
);

CREATE TABLE result (
    p_number BIGINT,
    result INT
);

CREATE TABLE recommendation (
    p_number BIGINT,
    d_number BIGINT
);