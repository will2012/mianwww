DROP TABLE IF EXISTS `mian_category`;  
CREATE TABLE `mian_category` (  
	  `id` int(11) NOT NULL AUTO_INCREMENT,  
	  `category_name` varchar(1000) NOT NULL,
	  PRIMARY KEY (`id`)  
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;  
  
DROP TABLE IF EXISTS `mian_post`;  
CREATE TABLE `mian_post` (  
	  `id` int(11) NOT NULL AUTO_INCREMENT,  
	  `category_id` int(11), 
	  `post_title` varchar(1000) NOT NULL, 
	  `post_content` MEDIUMTEXT NOT NULL,
	  PRIMARY KEY (`id`)  
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;  
  


 insert into mian_category(category_name) values('c语言');
 insert into mian_category(category_name) values('linux');
 insert into mian_category(category_name) values('java');
 insert into mian_category(category_name) values('ios');
 insert into mian_category(category_name) values('android');
 insert into mian_category(category_name) values('c++');
  insert into mian_category(category_name) values('软件测试');
  commit;
  insert into mian_post(category_id, post_title, post_content) values(%s, %s, %s);
  select post_title,post_content from mian_post where category_id=? limit 0,20
  select * from mian_category;
  select * from mian_post;
create database mian default character set utf8;
