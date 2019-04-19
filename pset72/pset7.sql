-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: pset7
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `id` int(10) NOT NULL,
  `action` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `time` datetime NOT NULL,
  `symbol` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shares` int(10) NOT NULL,
  `amount` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (8,'BUY','2015-09-09 21:29:52','IBM',2,290),(8,'BUY','2015-09-09 21:33:27','MS',34,1148),(8,'BUY','2015-09-09 21:39:29','AAPL',23,2533),(14,'BUY','2015-09-12 11:15:06','FREE',20,6),(14,'BUY','2015-09-12 11:15:22','GOOG',1,626),(14,'BUY','2015-09-12 11:15:37','MS',6,204),(14,'BUY','2015-09-12 11:27:55','MS',67,2277),(14,'BUY','2015-09-12 11:29:49','AAPL',23,2627),(14,'BUY','2015-09-12 11:37:09','AAPL',23,2627),(14,'BUY','2015-09-12 11:45:04','AAPL',12,1371),(14,'BUY','2015-09-12 11:47:49','AAPL',12,1371),(14,'SELL','2015-09-12 11:48:13','AAPL',12,1371),(14,'BUY','2015-09-12 20:35:03','AAPL',3,343),(14,'SELL','2015-09-12 20:36:44','AAPL',3,343),(14,'BUY','2015-09-14 07:23:19','AAPL',2,228),(14,'BUY','2015-09-14 07:23:21','AAPL',2,228),(14,'BUY','2015-09-14 07:23:59','MS',23,782),(14,'BUY','2015-09-14 07:24:39','FB',12,1105),(14,'BUY','2015-09-14 07:26:36','HR',23,516),(14,'BUY','2015-09-14 07:27:21','KE',34,374),(14,'SELL','2015-09-14 07:45:08','AAPL',4,457),(14,'BUY','2015-09-14 07:45:27','AAP',23,4021),(3,'BUY','2015-09-14 19:06:57','FB',34,3139),(3,'SELL','2015-09-14 19:07:59','FREE',67,18);
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio`
--

DROP TABLE IF EXISTS `portfolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio` (
  `id` int(10) NOT NULL,
  `symbol` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shares` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`,`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio`
--

LOCK TABLES `portfolio` WRITE;
/*!40000 ALTER TABLE `portfolio` DISABLE KEYS */;
INSERT INTO `portfolio` VALUES (3,'FB',34),(3,'ms',76),(5,'free',5),(6,'fb',6),(6,'free',6),(6,'goog',6),(8,'AAPL',25),(8,'fb',112),(8,'free',4),(8,'GE',20),(8,'goog',79),(8,'IBM',8),(8,'ms',1610),(14,'AAP',23),(14,'FB',12),(14,'HR',23),(14,'KE',34),(14,'MS',23);
/*!40000 ALTER TABLE `portfolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `cash` decimal(65,4) unsigned DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'belindazeng','','$1$50$oxJEDBo9KDStnrhtnSzir0',10000.0000),(2,'caesar','','$1$50$GHABNWBNE/o4VL7QjmQ6x0',10000.0000),(3,'jharvard','kelvinkaluorji@yahoo.com','$1$TxdCyShA$m5a8POvmjdMmmkwrxlqTs/',6879.7510),(4,'malan','','$1$50$lJS9HiGK6sphej8c4bnbX.',10000.0000),(5,'rob','','$1$HA$l5llES7AEaz8ndmSo5Ig41',10000.0000),(6,'skroob','kelvinkaluorji@yahoo.com','$1$50$euBi4ugiJmbpIbvTTfmfI.',10000.0000),(7,'zamyla','','$1$50$uwfqB45ANW.9.6qaQ.DcF.',10000.0000),(14,'kelvin','orjikalukelvin@gmail.com','$1$.nTAJ1dz$l2crVs5appP7vavh56md1.',3202.6500);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-24 13:05:30
