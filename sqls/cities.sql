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

CREATE TABLE IF NOT EXISTS `nom_ciudades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(20) NOT NULL,
  `estado` varchar(20) NOT NULL,
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=92 ;

--
-- Dumping data for table `ciudades`
--

INSERT INTO `nom_ciudades` (`id`, `estado_id`, `ciudad`) VALUES
(1, '1 ', 'Aguascalientes'),
(2, '2', 'La Paz'),
(3, '2', 'Cabo San Lucas'),
(4, '3', 'Ensenada'),
(5, '3', 'Mexicali'),
(6, '3', 'Tijuana'),
(7, '4', 'Campeche'),
(8, '4', 'Cd. Del Carmen'),
(9, '5', 'Monclova'),
(10, '5', 'Piedras Negras'),
(11, '5', 'Saltillo'),
(12, '5', 'Torreón'),
(13, '6', 'Colima'),
(14, '6', 'Manzanillo'),
(15, '7', 'Arriaga'),
(16, '7', 'Comitán'),
(17, '7', 'San Cristobal'),
(18, '7', 'Tapachula'),
(19, '7', 'Tuxtla Gutierrez'),
(20, '8', 'Casas Grandes'),
(21, '8', 'Chihuahua'),
(22, '8', 'Cd. Juárez'),
(23, '8', 'H. del Parral'),
(24, '9', 'México'),
(25, '10', 'Durango'),
(26, '10', 'Lerdo'),
(27, '11', 'Guanajuato'),
(28, '11', 'León'),
(29, '12', 'Acapulco'),
(30, '12', 'Chilpancingo'),
(31, '12', 'Zihuatanejo'),
(32, '13', 'Pachuca'),
(33, '13', 'Tulancingo'),
(34, '14', 'Guadalajara'),
(35, '14', 'Huejucar'),
(36, '14', 'Lagos de Moreno'),
(37, '14', 'Ocotlán'),
(38, '14', 'Puerto Vallarta'),
(39, '15', 'Chapingo Texcoco'),
(40, '15', 'Toluca'),
(41, '16', 'Morelia'),
(42, '16', 'Lázaro Cárdenas'),
(43, '16', 'Uruapan'),
(44, '17', 'Cuernavaca'),
(45, '17', 'Cuautla'),
(46, '18', 'Tepic'),
(47, '19', 'Monterrey'),
(48, '20', 'Oaxaca'),
(49, '20', 'Salina Cruz'),
(50, '21', 'Puebla'),
(51, '21', 'Atlixco'),
(52, '21', 'Tehuacán'),
(53, '22', 'Querétaro'),
(54, '22', 'San Juan del Río'),
(55, '23', 'Cozumel'),
(56, '23', 'Chetumal'),
(57, '23', 'Cancún'),
(58, '23', 'Playa del Carmen'),
(59, '24', 'Río Verde'),
(60, '24', 'San Luis Potosí'),
(61, '24', 'Cd. Valles'),
(62, '24', 'Matehuala'),
(63, '25', 'Culiacán'),
(64, '25', 'Mazatlán'),
(65, '25', 'Guasave'),
(66, '25', 'Los Mochis'),
(67, '26', 'Guaymas'),
(68, '26', 'Hermosillo'),
(69, '26', 'Obregón'),
(70, '26', 'Navojoa'),
(71, '26', 'Nogales'),
(72, '27', 'Villahermosa'),
(73, '27', 'Comalcalco'),
(74, '28', 'Cd. Victoria'),
(75, '28', 'Tampico'),
(76, '28', 'Matamoros'),
(77, '28', 'Reynosa'),
(78, '28', 'Nuevo Laredo'),
(79, '29', 'Tlaxcala'),
(80, '30', 'Coatzacoalcos'),
(81, '30', 'Córdoba'),
(82, '30', 'Jalapa'),
(83, '30', 'Orizaba'),
(84, '30', 'Tuxpan'),
(85, '30', 'Poza Rica'),
(86, '30', 'Veracruz'),
(87, '31', 'Mérida'),
(88, '31', 'Progreso'),
(89, '31', 'Valladolid'),
(90, '32', 'Fresnillo'),
(91, '32', 'Zacatecas');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
