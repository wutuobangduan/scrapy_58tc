The program is used to get car information from 58.com

The struct of table is :
    CREATE TABLE `sell_car_info` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(100) DEFAULT NULL COMMENT '标题',
        `car_config` varchar(255) DEFAULT NULL COMMENT '车辆配置',
        `name` varchar(50) DEFAULT NULL COMMENT '姓名',
        `telephone_num` varchar(150) DEFAULT NULL COMMENT '联系方式',
        `addrs` varchar(150) DEFAULT NULL COMMENT '地区',
        `current` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `release_time` varchar(50) NOT NULL DEFAULT '' COMMENT '发布时间',
        `temp_time` int(11) DEFAULT NULL,
        `prices` varchar(100) DEFAULT NULL COMMENT '价格',
        `is_seller` varchar(30) DEFAULT NULL COMMENT '商户或个人',
        `owner_readme` text COMMENT '车主自述',
        `img_src` varchar(150) DEFAULT NULL COMMENT '手机号图片地址',
        `info_src` varchar(50) DEFAULT NULL COMMENT '来源网站',
        `url` varchar(150) DEFAULT NULL COMMENT '该信息地址',
        `source` tinyint(1) DEFAULT '1' COMMENT '1:网络爬虫 2：o2o录入 0：共有的',
        PRIMARY KEY (`id`),
        UNIQUE KEY `url` (`url`),
        KEY `telephone_num` (`telephone_num`),
        KEY `info_src` (`info_src`),
        KEY `current` (`current`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
