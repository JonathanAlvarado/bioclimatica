-- phpMyAdmin SQL Dump
-- version 3.5.8.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 17, 2014 at 08:15 PM
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
-- Table structure for table `soluciones`
--

CREATE TABLE IF NOT EXISTS `soluciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `valorR` float NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `tipo_porcion` varchar(30) NOT NULL,
  `se` float NOT NULL,
  `coeficiente_sombreado` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `soluciones`
--

INSERT INTO `soluciones` (`id`, `descripcion`) VALUES
(1, 'Ejemplo Muro'),
(2, 'Ejemplo Losa'),
(3, 'Ejemplo Vidrio'),
(4, 'Ejemplo Puerta Madera'),
(5, 'Ejemplo Domo'),
(6, 'Ejemplo Muro Aislado'),
(7, 'Ejemplo Losa Aislada'),
(8, 'Ejemplo Ventana Doble'),
(9, 'Ejemplo Muro No Homogeneo'),
(10, 'Ejemplo Piso');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
