--DROP TABLE "celebrities";
CREATE TABLE "celebrities" (
    id varchar(255), -- primary key,
    name varchar(255), -- '全名',
    url varchar(255), -- '豆瓣详情页地址',
    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--DROP TABLE "collects";
--CREATE TABLE "collects" (
--    id varchar(255), -- primary key,
--    name varchar(255), -- '全名',
--    url varchar(255), -- '豆瓣详情页地址',
--    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
--);