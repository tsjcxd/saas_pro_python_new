SET NAMES utf8mb4;
CREATE DATABASE IF NOT EXISTS `test_db` DEFAULT CHARACTER SET utf8mb4;
USE `test_db`;

--CREATE TABLE `hotdb_datanode` (
--  `datanode_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
--  `datanode_name` varchar(50) NOT NULL DEFAULT '',
--  `datanode_type` int(10) unsigned NOT NULL DEFAULT 0 COMMENT '0:M-S; 1:MGR',
--  PRIMARY KEY (`datanode_id`),
--  UNIQUE KEY `unique_idx_datanodename` (`datanode_name`)
--) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='HOTDB的数据节点信息(Data node information of HotDB)';

CREATE TABLE `create_brand_member_card` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `card_type` int(10) NOT NULL,
  `card_name` varchar(255) NOT NULL,
  `support_member_num` tinyint(10) NOT NULL,
  `admission_range` int(10) NOT NULL,
  `price_setting` int(10) NOT NULL,
  `support_sales` int(10) NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NOT NULL,
  `is_transfer` int(10) NOT NULL,
  `unit` int(10) NOT NULL,
  `num` int(10) DEFAULT NULL,
  `price_gradient` json not NULL,
  `sell_type` json not NULL,
  `card_introduction` varchar(250) DEFAULT NULL,
  `special_note` VARCHAR(250) DEFAULT NULL,
  `card_contents` VARCHAR(250) NOT NULL DEFAULT '',
  `card_bg` JSON DEFAULT NULL,
  `publish_channel` int(10) NOT NULL,
  `admission_shop_list` JSON DEFAULT NULL,
  `sell_shop_list`JSON DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='创建品牌下的会员卡';

CREATE TABLE `create_shop_staff` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mobile` varchar(250) NOT NULL,
  `sex` int(250) NOT NULL,
  `nickname` varchar(250) NOT NULL,
  `identity` varchar(250) DEFAULT NULL,
  `department_id` varchar(250) NOT NULL,
  `role_id` json NOT NULL,
  `entry_date` varchar(250) DEFAULT NULL,
  `shop_id` varchar(250) NOT NULL,
  `is_permission` varchar(250) DEFAULT NULL,
  `image_avatar` json DEFAULT NULL,
  `image_face` json DEFAULT NULL,
  `country_code_id` varchar(250) DEFAULT NULL,
  `id_type` varchar(250) DEFAULT NULL,
  `comments` varchar(250) DEFAULT NULL,
  `expected` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='创建门店员工';



commit;
