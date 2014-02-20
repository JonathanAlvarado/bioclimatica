-- phpMyAdmin SQL Dump
-- version 3.5.8.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 17, 2014 at 08:16 PM
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

INSERT INTO `soluciones` (`id`, `valorR`, `tipo`, `tipo_porcion`, `se`, `coeficiente_sombreado`) VALUES
(1, 0.35, 'Muro', 'Muro Masivo', 1, 1),
(2, 0.35, 'Techo', 'Techo', 1, 1),
(3, 0.2, 'Muro', 'Ventana', 1, 1),
(4, 0.5, 'Muro', 'Muro Masivo', 0, 1),
(5, 0.25, 'Techo', 'Domo', 1, 0.59),
(6, 1.32, 'Muro', 'Muro Masivo', 1, 1),
(7, 1.32, 'Techo Aislado', 'Techo', 1, 1),
(8, 0.2, 'Muro', 'Ventana', 1, 0.55),
(9, 2.78, 'Muro', 'Muro Masivo', 1, 1),
(10, 0.24, 'Piso', 'Superficie Inferior', 1, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
