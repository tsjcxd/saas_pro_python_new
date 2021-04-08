SET NAMES utf8mb4;
DROP DATABASE IF EXISTS `test_db`;
CREATE DATABASE IF NOT EXISTS `test_db` DEFAULT CHARACTER SET utf8mb4;
USE `test_db`;

DROP TABLE IF EXISTS `create_brand_member_card`;
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
  `comments` varchar(255),
  `expected` varchar(255),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='创建品牌下的会员卡';

INSERT INTO `create_brand_member_card` VALUES(0,2,'品牌期限卡333',1,3,1,1,'2021-04-07',"2021-04-30",FALSE,2,null,'[{"id": 0, "unit": 2, "num": 100, "rally_price": 0.1, "frozen_day": 100, "gift_unit": 10}]','[2,1]','','在可用期限内不限次数','','{}',1,'[]','[]','','');

DROP TABLE IF EXISTS `create_shop_staff`;
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
