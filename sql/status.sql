CREATE TABLE `status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `msg` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `date` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;