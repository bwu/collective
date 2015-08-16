CREATE TABLE `collective`.`follow` (
  `user_id` int(11) unsigned NOT NULL,
  `follow_user_id` int(11) unsigned NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`, `follow_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;