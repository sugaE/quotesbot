--CREATE DATABASE quotesbot;

--DROP TABLE IF EXISTS "movies";
CREATE TABLE "movies" (
    id varchar(255) UNIQUE primary key,
    cover_url varchar(255), -- '海报',
    original_title varchar(255), -- '标题',
    title varchar(255), -- '标题中文翻译',
    url varchar(255), -- '豆瓣详情页地址',

    -- directors varchar(255), --  '导演' from table celebrities
    -- writers varchar(255), -- '编剧' from table celebrities
    -- actors varchar(255), -- '演员' from table celebrities

    rating_value float,
    rating_count int,
    stats_5 float,
    stats_4 float,
    stats_3 float,
    stats_2 float,
    stats_1 float,
    wish_count int,
    doing_count int,
    done_count int,
    -- following int,

    -- cate_id int,
    -- cate_name varchar(255),
    type varchar(255),
    subtype varchar(255),
    tags varchar(255), -- 动画 / 奇幻 / 冒险
    -- tags_ugc varchar(255), -- 动画 / 奇幻 / 冒险
    genres varchar(255), -- ["动画", "同性"]
    -- website varchar(255), -- 官方网站
    countries varchar(255), -- 制片国家/地区: ["日本"]
    languages varchar(255), -- 语言 ["日语"]
    pub_date DATE, -- '首播时间', ["2014-10-29(日本)"]
    pub_region varchar(255), -- '首播地点', ["2014-10-29(日本)"]
    episodes_count int, --集数: 13
    durations varchar(255), --["26分钟"]
    -- imdb var char(255), -- IMDb链接: tt10112240
    last_episode_number varchar(255),
--    release_date Date,
--    aka varchar(255), -- Json.dump ["ハイブリッドチャイルド"]
    -- card_subtitle varchar(255), -- "2014 / 日本 / 动画 同性 / 福田道生 / 冈本信彦 平川大辅"
    comment_count int, -- 短评数
    review_count int, -- 影评数
    intro varchar(1000),

    is_released bit,
    is_restrictive bit,
    is_show bit,
    is_tv bit,

    -- recommendations varchar(500), -- id join

    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);


--DROP TABLE IF EXISTS "my_collect";
CREATE TABLE "my_collect" (
    id varchar(255) UNIQUE primary key,
    movie_id varchar(255),

--    mark float, -- '我的豆瓣评分',
    create_time DATE, -- '我的豆瓣评分日期',
    comment varchar(1000), -- 短评
--    done_index
--    is_private

--    rating_count int,
--    rating_max int,
--    rating_star_count int,
    rating float, -- value

    status varchar(255),
    tags varchar(255), -- ["谎言", "人性"]
--    vote_count

    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

--DROP TABLE IF EXISTS "movie_alias";
CREATE TABLE "movie_alias" (
	"movie_id"	varchar(255) NOT NULL,
	"alia"	varchar(255) NOT NULL,
	FOREIGN KEY("movie_id") REFERENCES "movies"("id"),
	UNIQUE("movie_id","alia")
);


--DROP TABLE IF EXISTS "tags";
CREATE TABLE "tags" (
    id varchar(255) UNIQUE primary key ,
    name varchar(255)
)

--DROP TABLE IF EXISTS "celebrities";
CREATE TABLE "celebrities" (
    id varchar(255) UNIQUE primary key, -- primary key,
    name varchar(255), -- '全名',
    url varchar(255), -- '豆瓣详情页地址',
    abstract varchar(255),
    cover_url varchar(255),
    latin_name varchar(255),
    title varchar(255),

    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);


--DROP TABLE IF EXISTS "movie_celebrities";
CREATE TABLE "movie_celebrities" (
	"movie_id"	varchar(255),
	"celebrity_id"	varchar(255),
	"role"	varchar(255),

	UNIQUE("movie_id","celebrity_id"),
	FOREIGN KEY("celebrity_id") REFERENCES "celebrities"("id"),
	FOREIGN KEY("movie_id") REFERENCES "movies"("id")
);