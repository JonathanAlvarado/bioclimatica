-- phpMyAdmin SQL Dump
-- version 3.5.8.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 17, 2014 at 06:34 PM
-- Server version: 5.5.34-0ubuntu0.13.04.1
-- PHP Version: 5.4.9-4ubuntu2.4

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `nom020`
--

-- --------------------------------------------------------

--
-- Table structure for table `ciudades`
--

CREATE TABLE IF NOT EXISTS `cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(20) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=92 ;

--
-- Dumping data for table `ciudades`
--

INSERT INTO `cities` (`id`, `state`, `city`) VALUES
(1, 'Aguascalientes ', 'Aguascalientes'),
(2, 'Baja California Sur', 'La Paz'),
(3, 'Baja California Sur', 'Cabo San Lucas'),
(4, 'Baja California', 'Ensenada'),
(5, 'Baja California', 'Mexicali'),
(6, 'Baja California', 'Tijuana'),
(7, 'Campeche', 'Campeche'),
(8, 'Campeche', 'Cd. Del Carmen'),
(9, 'Coahuila', 'Monclova'),
(10, 'Coahuila', 'Piedras Negras'),
(11, 'Coahuila', 'Saltillo'),
(12, 'Coahuila', 'TorreÃ³n'),
(13, 'Colima', 'Colima'),
(14, 'Colima', 'Manzanillo'),
(15, 'Chiapas', 'Arriaga'),
(16, 'Chiapas', 'ComitÃ¡n'),
(17, 'Chiapas', 'San Cristobal'),
(18, 'Chiapas', 'Tapachula'),
(19, 'Chiapas', 'Tuxtla Gutierrez'),
(20, 'Chihuahua', 'Casas Grandes'),
(21, 'Chihuahua', 'Chihuahua'),
(22, 'Chihuahua', 'Cd. JuÃ¡rez'),
(23, 'Chihuahua', 'H. del Parral'),
(24, 'D.F.', 'MÃ©xico'),
(25, 'Durango', 'Durango'),
(26, 'Durango', 'Lerdo'),
(27, 'Guanajuato', 'Guanajuato'),
(28, 'Guanajuato', 'LeÃ³n'),
(29, 'Guerrero', 'Acapulco'),
(30, 'Guerrero', 'Chilpancingo'),
(31, 'Guerrero', 'Zihuatanejo'),
(32, 'Hidalgo', 'Pachuca'),
(33, 'Hidalgo', 'Tulancingo'),
(34, 'Jalisco', 'Guadalajara'),
(35, 'Jalisco', 'Huejucar'),
(36, 'Jalisco', 'Lagos de Mor.'),
(37, 'Jalisco', 'OcotlÃ¡n'),
(38, 'Jalisco', 'Puerto Vallarta'),
(39, 'MÃ©xico', 'Chapingo Texc.'),
(40, 'MÃ©xico', 'Toluca'),
(41, 'MichoacÃ¡n', 'Morelia'),
(42, 'MichoacÃ¡n', 'LÃ¡zaro CÃ¡rdenas'),
(43, 'MichoacÃ¡n', 'Uruapan'),
(44, 'Morelos', 'Cuernavaca'),
(45, 'Morelos', 'Cuautla'),
(46, 'Nayarit', 'Tepic'),
(47, 'Nuevo LeÃ³n', 'Monterrey'),
(48, 'Oaxaca', 'Oaxaca'),
(49, 'Oaxaca', 'Salina Cruz'),
(50, 'Puebla', 'Puebla'),
(51, 'Puebla', 'Atlixco'),
(52, 'Puebla', 'TehuacÃ¡n'),
(53, 'QuerÃ©taro', 'QuerÃ©taro'),
(54, 'Queretaro', 'San Juan del RÃ­o'),
(55, 'Quintana Roo', 'Cozumel'),
(56, 'Quintana Roo', 'Chetumal'),
(57, 'Quintana Roo', 'CancÃºn'),
(58, 'Quintana Roo', 'Playa del Carmen'),
(59, 'San Luis PotosÃ­', 'RÃ­o Verde'),
(60, 'San Luis PotosÃ­', 'San Luis PotosÃ­'),
(61, 'San Luis PotosÃ­', 'Cd. Valles'),
(62, 'San Luis PotosÃ­', 'Matehuala'),
(63, 'Sinaloa', 'CuliacÃ¡n'),
(64, 'Sinaloa', 'MazatlÃ¡n'),
(65, 'Sinaloa', 'Guasave'),
(66, 'Sinaloa', 'Los Mochis'),
(67, 'Sonora', 'Guaymas'),
(68, 'Sonora', 'Hermosillo'),
(69, 'Sonora', 'ObregÃ³n'),
(70, 'Sonora', 'Navojoa'),
(71, 'Sonora', 'Nogales'),
(72, 'Tabasco', 'Villahermosa'),
(73, 'Tabasco', 'Comalcalco'),
(74, 'Tamaulipas', 'Cd. Victoria'),
(75, 'Tamaulipas', 'Tampico'),
(76, 'Tamaulipas', 'Matamoros'),
(77, 'Tamaulipas', 'Reynosa'),
(78, 'Tamaulipas', 'Nuevo Laredo'),
(79, 'Tlaxcala', 'Tlaxcala'),
(80, 'Veracruz', 'Coatzacoalcos'),
(81, 'Veracruz', 'CÃ³rdoba'),
(82, 'Veracruz', 'Jalapa'),
(83, 'Veracruz', 'Orizaba'),
(84, 'Veracruz', 'Tuxpan'),
(85, 'Veracruz', 'Poza Rica'),
(86, 'Veracruz', 'Veracruz'),
(87, 'YucatÃ¡n', 'MÃ©rida'),
(88, 'YucatÃ¡n', 'Progreso'),
(89, 'YucatÃ¡n', 'Valladolid'),
(90, 'Zacatecas', 'Fresnillo'),
(91, 'Zacatecas', 'Zacatecas');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
