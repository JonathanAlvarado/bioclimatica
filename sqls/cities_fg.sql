-- phpMyAdmin SQL Dump
-- version 3.5.8.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 17, 2014 at 07:37 PM
-- Server version: 5.5.34-0ubuntu0.13.04.1
-- PHP Version: 5.4.9-4ubuntu2.4

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `calcio73_nom020`
--

-- --------------------------------------------------------

--
-- Table structure for table `ciudades`
--

CREATE TABLE IF NOT EXISTS `ciudades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(20) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  `kref_3niv` float NOT NULL,
  `kref_mas3niv_techo` float NOT NULL,
  `kref_mas3niv_pared` float NOT NULL,
  `temp_int` int(11) NOT NULL,
  `temp_sup_int` int(11) NOT NULL,
  `temp_techo` int(11) NOT NULL,
  `temp_mmN` int(11) NOT NULL,
  `temp_mmE` int(11) NOT NULL,
  `temp_mmO` int(11) NOT NULL,
  `temp_mmS` int(11) NOT NULL,
  `temp_mlN` int(11) NOT NULL,
  `temp_mlE` int(11) NOT NULL,
  `temp_mlO` int(11) NOT NULL,
  `temp_mlS` int(11) NOT NULL,
  `temp_trluz_domo` int(11) NOT NULL,
  `temp_ventN` int(11) NOT NULL,
  `temp_ventE` int(11) NOT NULL,
  `temp_ventO` int(11) NOT NULL,
  `temp_ventS` int(11) NOT NULL,
  `fgtd` int(11) NOT NULL,
  `fg_mN` int(11) NOT NULL,
  `fg_mE` int(11) NOT NULL,
  `fg_mO` int(11) NOT NULL,
  `fg_mS` int(11) NOT NULL,
  `barrera_vapor` char(2) DEFAULT NULL,
  `latitud` varchar(10) NOT NULL,
  `zona_termica` char(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=92 ;

--
-- Dumping data for table `ciudades`
--

INSERT INTO `ciudades` (`id`, `fgtd`, `fg_mN`, `fg_mE`, `fg_mO`, `fg_mS`) VALUES
(1, 274, 91, 137, 146, 118),
(2, 322, 70, 159, 164, 131),
(3, 322, 70, 159, 164, 131),
(4, 322, 70, 159, 164, 131),
(5, 322, 70, 159, 164, 131),
(6, 322, 70, 159, 164, 131),
(7, 284, 95, 152, 133, 119),
(8, 284, 95, 152, 133, 119),
(9, 322, 70, 159, 164, 131),
(10, 322, 70, 159, 164, 131),
(11, 322, 70, 159, 164, 131),
(12, 322, 70, 159, 164, 131),
(13, 274, 91, 137, 146, 118),
(14, 274, 91, 137, 146, 118),
(15, 272, 102, 140, 134, 114),
(16, 272, 102, 140, 134, 114),
(17, 272, 102, 140, 134, 114),
(18, 272, 102, 140, 134, 114),
(19, 272, 102, 140, 134, 114),
(20, 322, 70, 159, 164, 131),
(21, 322, 70, 159, 164, 131),
(22, 322, 70, 159, 164, 131),
(23, 322, 70, 159, 164, 131),
(24, 272, 102, 140, 134, 114),
(25, 322, 70, 159, 164, 131),
(26, 322, 70, 159, 164, 131),
(27, 274, 91, 137, 146, 118),
(28, 274, 91, 137, 146, 118),
(29, 274, 91, 137, 146, 118),
(30, 274, 91, 137, 146, 118),
(31, 274, 91, 137, 146, 118),
(32, 272, 102, 140, 134, 114),
(33, 272, 102, 140, 134, 114),
(34, 274, 91, 137, 146, 118),
(35, 274, 91, 137, 146, 118),
(36, 274, 91, 137, 146, 118),
(37, 274, 91, 137, 146, 118),
(38, 274, 91, 137, 146, 118),
(39, 274, 91, 137, 146, 118),
(40, 274, 91, 137, 146, 118),
(41, 274, 91, 137, 146, 118),
(42, 274, 91, 137, 146, 118),
(43, 274, 91, 137, 146, 118),
(44, 274, 91, 137, 146, 118),
(45, 274, 91, 137, 146, 118),
(46, 274, 91, 137, 146, 118),
(47, 274, 91, 137, 146, 118),
(48, 272, 102, 140, 134, 114),
(49, 272, 102, 140, 134, 114),
(50, 272, 102, 140, 134, 114),
(51, 272, 102, 140, 134, 114),
(52, 272, 102, 140, 134, 114),
(53, 274, 191, 137, 146, 118),
(54, 274, 191, 137, 146, 118),
(55, 284, 95, 152, 133, 119),
(56, 284, 95, 152, 133, 119),
(57, 284, 95, 152, 133, 119),
(58, 284, 95, 152, 133, 119),
(59, 274, 91, 137, 146, 118),
(60, 274, 91, 137, 146, 118),
(61, 274, 91, 137, 146, 118),
(62, 274, 91, 137, 146, 118),
(63, 322, 70, 159, 164, 131),
(64, 322, 70, 159, 164, 131),
(65, 322, 70, 159, 164, 131),
(66, 322, 70, 159, 164, 131),
(67, 322, 70, 159, 164, 131),
(68, 322, 70, 159, 164, 131),
(69, 322, 70, 159, 164, 131),
(70, 322, 70, 159, 164, 131),
(71, 322, 70, 159, 164, 131),
(72, 272, 102, 140, 134, 114),
(73, 272, 102, 140, 134, 114),
(74, 272, 102, 140, 134, 114),
(75, 272, 102, 140, 134, 114),
(76, 272, 102, 140, 134, 114),
(77, 272, 102, 140, 134, 114),
(78, 272, 102, 140, 134, 114),
(79, 272, 102, 140, 134, 114),
(80, 272, 102, 140, 134, 114),
(81, 272, 102, 140, 134, 114),
(82, 272, 102, 140, 134, 114),
(83, 272, 102, 140, 134, 114),
(84, 272, 102, 140, 134, 114),
(85, 272, 102, 140, 134, 114),
(86, 272, 102, 140, 134, 114),
(87, 284, 95, 152, 133, 119),
(88, 284, 95, 152, 133, 119),
(89, 284, 95, 152, 133, 119),
(90, 274, 91, 137, 146, 118),
(91, 274, 91, 137, 146, 118);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
