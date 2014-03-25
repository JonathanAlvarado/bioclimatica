SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

-- --------------------------------------------------------

--
-- Table structure for table `nom_soluciones_detalles`
--

CREATE TABLE IF NOT EXISTS `nom_soluciones_detalles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material` varchar(40) NOT NULL,
  `tipo_porcion` varchar(30) NOT NULL,
  `valorR` float NOT NULL,
  `se` float NOT NULL,
  `coeficiente_sombreado` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=95 ;

--
-- Dumping data for table `soluciones_usuario`
--

INSERT INTO `soluciones_usuario` (`id`, `material`, `tipo_porcion`, `valorR`, `se`, `coeficiente_sombreado`) VALUES
(1, 'Concreto', 'techo', 0.3229, 1, 1),
(2, 'Concreto', 'techo', 1.4763, 1, 1),
(3, 'Concreto', 'techo', 1.9647, 1, 1),
(4, 'Concreto', 'techo', 2.4532, 1, 1),
(5, 'Concreto', 'techo', 2.9417, 1, 1),
(6, 'Concreto', 'techo', 1.2998, 1, 1),
(7, 'Concreto', 'techo', 1.7883, 1, 1),
(8, 'Concreto', 'techo', 2.2767, 1, 1),
(9, 'Concreto', 'techo', 2.7652, 1, 1),
(10, 'Concreto', 'techo', 1.8036, 1, 1),
(11, 'Concreto', 'techo', 2.325, 1, 1),
(12, 'Concreto', 'techo', 2.6854, 1, 1),
(13, 'Concreto', 'techo', 3.7754, 1, 1),
(14, 'Concreto', 'techo', 5.6316, 1, 1),
(15, 'Vigueta-Bovedilla de concreto', 'techo', 0.7433, 1, 1),
(16, 'Vigueta-Bovedilla de concreto', 'techo', 1.8967, 1, 1),
(17, 'Vigueta-Bovedilla de concreto', 'techo', 2.3852, 1, 1),
(18, 'Vigueta-Bovedilla de concreto', 'techo', 2.8737, 1, 1),
(19, 'Vigueta-Bovedilla de concreto', 'techo', 3.3621, 1, 1),
(20, 'Vigueta-Bovedilla de concreto', 'techo', 1.7203, 1, 1),
(21, 'Vigueta-Bovedilla de concreto', 'techo', 2.2087, 1, 1),
(22, 'Vigueta-Bovedilla de concreto', 'techo', 2.6972, 1, 1),
(23, 'Vigueta-Bovedilla de concreto', 'techo', 3.1857, 1, 1),
(24, 'Vigueta-Bovedilla de concreto', 'techo', 2.224, 1, 1),
(25, 'Vigueta-Bovedilla de concreto', 'techo', 2.7455, 1, 1),
(26, 'Vigueta-Bovedilla de concreto', 'techo', 3.1059, 1, 1),
(27, 'Vigueta-Bovedilla de concreto', 'techo', 4.1959, 1, 1),
(28, 'Vigueta-Bovedilla de concreto', 'techo', 6.052, 1, 1),
(29, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 1.0131, 1, 1),
(30, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 2.1665, 1, 1),
(31, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 2.6549, 1, 1),
(32, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 3.1434, 1, 1),
(33, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 3.6319, 1, 1),
(34, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 1.99, 1, 1),
(35, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 2.2087, 1, 1),
(36, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 2.9669, 1, 1),
(37, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 3.4554, 1, 1),
(38, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 2.4937, 1, 1),
(39, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 3.0152, 1, 1),
(40, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 3.3756, 1, 1),
(41, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 4.4656, 1, 1),
(42, 'Vigueta-Bovedilla de poliestireno expand', 'techo', 6.3218, 1, 1),
(43, 'Base', 'ventana', 5.319, 1, 1),
(44, 'Sencillo claro de 3mm', 'ventana', 5.894, 1, 1),
(45, 'Sencillo claro de 6mm', 'ventana', 5.778, 1, 1),
(46, 'Doble claro 3mm/6mm aire', 'ventana', 3.159, 1, 1),
(47, 'Doble claro 6mm/6mm aire', 'ventana', 3.094, 1, 1),
(48, 'Doble claro 3mm/13mm aire', 'ventana', 2.716, 1, 1),
(49, 'Doble claro 6mm/13mm aire', 'ventana', 2.665, 1, 1),
(50, 'Concreto', 'piso Ventilado', 0.2615, 1, 1),
(51, 'Concreto', 'piso Ventilado', 1.2385, 1, 1),
(52, 'Concreto', 'piso Ventilado', 1.7269, 1, 1),
(53, 'Concreto', 'piso Ventilado', 2.2154, 1, 1),
(54, 'Concreto', 'piso Ventilado', 2.7038, 1, 1),
(55, 'Vigueta-Bovedilla de concreto', 'piso Ventilado', 0.682, 1, 1),
(56, 'Vigueta-Bovedilla de concreto', 'piso Ventilado', 1.6589, 1, 1),
(57, 'Vigueta-Bovedilla de concreto', 'piso Ventilado', 2.1474, 1, 1),
(58, 'Vigueta-Bovedilla de concreto', 'piso Ventilado', 2.6358, 1, 1),
(59, 'Vigueta-Bovedilla de concreto', 'piso Ventilado', 3.1243, 1, 1),
(60, 'Vigueta-Bovedilla de poliestireno expand', 'piso Ventilado', 0.9517, 1, 1),
(61, 'Vigueta-Bovedilla de poliestireno expand', 'piso Ventilado', 1.9286, 1, 1),
(62, 'Vigueta-Bovedilla de poliestireno expand', 'piso Ventilado', 2.4171, 1, 1),
(63, 'Vigueta-Bovedilla de poliestireno expand', 'piso Ventilado', 2.9056, 1, 1),
(64, 'Vigueta-Bovedilla de poliestireno expand', 'piso Ventilado', 3.394, 1, 1),
(65, 'Concreto', 'muro masivo', 0.2764, 1, 1),
(66, 'Concreto', 'muro ligero', 1.436, 1, 1),
(67, 'Concreto', 'muro ligero', 1.2969, 1, 1),
(68, 'Concreto', 'muro ligero', 1.7854, 1, 1),
(69, 'Concreto', 'muro ligero', 2.2738, 1, 1),
(70, 'Concreto', 'muro ligero', 2.7623, 1, 1),
(71, 'Concreto', 'muro ligero', 1.2533, 1, 1),
(72, 'Concreto', 'muro ligero', 1.7418, 1, 1),
(73, 'Concreto', 'muro ligero', 2.2303, 1, 1),
(74, 'Concreto', 'muro ligero', 2.7187, 1, 1),
(75, 'Block de concreto', 'muro masivo', 0.3989, 1, 1),
(76, 'Block de concreto', 'muro ligero', 1.5585, 1, 1),
(77, 'Block de concreto', 'muro ligero', 1.4194, 1, 1),
(78, 'Block de concreto', 'muro ligero', 1.9079, 1, 1),
(79, 'Block de concreto', 'muro ligero', 2.3963, 1, 1),
(80, 'Block de concreto', 'muro ligero', 2.8848, 1, 1),
(81, 'Block de concreto', 'muro ligero', 1.3759, 1, 1),
(82, 'Block de concreto', 'muro ligero', 1.8643, 1, 1),
(83, 'Block de concreto', 'muro ligero', 2.3528, 1, 1),
(84, 'Block de concreto', 'muro ligero', 2.8412, 1, 1),
(85, 'Ladrillo', 'muro masivo', 0.368, 1, 1),
(86, 'Ladrillo', 'muro ligero', 1.5276, 1, 1),
(87, 'Ladrillo', 'muro ligero', 1.3885, 1, 1),
(88, 'Ladrillo', 'muro ligero', 1.877, 1, 1),
(89, 'Ladrillo', 'muro ligero', 2.3654, 1, 1),
(90, 'Ladrillo', 'muro ligero', 2.8539, 1, 1),
(91, 'Ladrillo', 'muro ligero', 1.3449, 1, 1),
(92, 'Ladrillo', 'muro ligero', 1.8334, 1, 1),
(93, 'Ladrillo', 'muro ligero', 2.3219, 1, 1),
(94, 'Ladrillo', 'muro ligero', 2.8103, 1, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;