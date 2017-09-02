/*
Navicat MySQL Data Transfer

Source Server         : MySQL57
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : reboot15

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-09-02 17:34:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `role` int(2) unsigned DEFAULT '0',
  `phone` char(16) DEFAULT NULL,
  `job` char(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('4', 'admin', '123456', '1', null, null);
INSERT INTO `user` VALUES ('8', 'tailoryang', '', '0', '12345678', '77');
INSERT INTO `user` VALUES ('15', '123', '', '0', '123478', '22');
SET FOREIGN_KEY_CHECKS=1;
