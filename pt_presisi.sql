-- MariaDB dump 10.17  Distrib 10.4.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: pt_presisi
-- ------------------------------------------------------
-- Server version	10.5.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bekerja`
--

DROP TABLE IF EXISTS `bekerja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bekerja` (
  `id_proyek` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `namaProyek` varchar(50) DEFAULT NULL,
  `deadline` datetime DEFAULT NULL,
  PRIMARY KEY (`id_proyek`,`nama`),
  KEY `nama` (`nama`),
  KEY `namaProyek` (`namaProyek`),
  CONSTRAINT `bekerja_ibfk_1` FOREIGN KEY (`id_proyek`) REFERENCES `proyek` (`ID_proyek`),
  CONSTRAINT `bekerja_ibfk_2` FOREIGN KEY (`nama`) REFERENCES `pekerja` (`nama`),
  CONSTRAINT `bekerja_ibfk_3` FOREIGN KEY (`namaProyek`) REFERENCES `proyek` (`namaProyek`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bekerja`
--

LOCK TABLES `bekerja` WRITE;
/*!40000 ALTER TABLE `bekerja` DISABLE KEYS */;
INSERT INTO `bekerja` VALUES ('2b2','Holly','Proyek Milestone 3','2020-11-23 23:59:59');
/*!40000 ALTER TABLE `bekerja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pekerja`
--

DROP TABLE IF EXISTS `pekerja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pekerja` (
  `ID_telegram` varchar(40) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `divisi` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_telegram`),
  UNIQUE KEY `nama_unik_const` (`nama`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pekerja`
--

LOCK TABLES `pekerja` WRITE;
/*!40000 ALTER TABLE `pekerja` DISABLE KEYS */;
INSERT INTO `pekerja` VALUES ('1','Holly','HR'),('2','Denny','HR'),('3','Alya','Sekretaris'),('4','Shofu','Sekretaris');
/*!40000 ALTER TABLE `pekerja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `progress` (
  `id_proyek` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `namaProyek` varchar(50) DEFAULT NULL,
  `progress` varchar(100) DEFAULT NULL,
  `waktuprogress` datetime NOT NULL,
  PRIMARY KEY (`id_proyek`,`nama`,`waktuprogress`),
  KEY `nama` (`nama`),
  KEY `namaProyek` (`namaProyek`),
  CONSTRAINT `progress_ibfk_1` FOREIGN KEY (`nama`) REFERENCES `bekerja` (`nama`),
  CONSTRAINT `progress_ibfk_2` FOREIGN KEY (`namaProyek`) REFERENCES `bekerja` (`namaProyek`),
  CONSTRAINT `progress_ibfk_3` FOREIGN KEY (`id_proyek`) REFERENCES `bekerja` (`id_proyek`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress`
--

LOCK TABLES `progress` WRITE;
/*!40000 ALTER TABLE `progress` DISABLE KEYS */;
INSERT INTO `progress` VALUES ('2b2','Holly','Proyek Milestone 3','Menginisialisasi basis data baru','2020-11-22 22:28:43'),('2b2','Holly','Proyek Milestone 3','Menginisialisasi basis data 2.0 baru juga tapi ngetes','2020-11-22 22:28:55'),('2b2','Holly','Proyek Milestone 3','Menginisialisasi basis data 3.0 baru juga tapi ngetes ketiga kali huehueheeh','2020-11-22 22:29:10');
/*!40000 ALTER TABLE `progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyek`
--

DROP TABLE IF EXISTS `proyek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proyek` (
  `ID_proyek` varchar(15) NOT NULL,
  `namaProyek` varchar(50) NOT NULL,
  `deskripsi` varchar(200) DEFAULT NULL,
  `startdate` datetime DEFAULT NULL,
  `deadline` datetime DEFAULT NULL,
  `jenisProyek` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_proyek`),
  UNIQUE KEY `namaProyek` (`namaProyek`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyek`
--

LOCK TABLES `proyek` WRITE;
/*!40000 ALTER TABLE `proyek` DISABLE KEYS */;
INSERT INTO `proyek` VALUES ('1a1','Proyek Berjalan Bersama','Proyek ini menjadi sebuah data inisialisasi di dalam sebuah database sql blablabla gatau nulis apa lagi','2020-11-22 22:24:01','2020-11-24 23:59:59','inisialisasi data'),('2b2','Proyek Milestone 3','Proyek ini menjadi sebuah data inisialisasi kedua yey semangat gais nugasnya','2020-11-22 22:24:48','2020-11-23 23:59:59','inisialisasi data');
/*!40000 ALTER TABLE `proyek` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-22 22:45:35
