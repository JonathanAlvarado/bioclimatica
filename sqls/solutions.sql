SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `nom_soluciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=95 ;

--
-- Dumping data for table `nom_soluciones`
--

INSERT INTO `nom_soluciones` (`descripcion`, `tipo`) VALUES
('Concreto base', 'techo'),
('Foamular sobre losa 1 pulg.', 'techo'),
('Foamular sobre losa 1.5 pulg.', 'techo'),
('Foamular sobre losa 2 pulg.', 'techo'),
('Foamular sobre losa 2.5 pulg.', 'techo'),
('Foamular bajo losa interior 1 ', 'techo'),
('Foamular bajo losa interior 1.', 'techo'),
('Foamular bajo losa interior 2 ', 'techo'),
('Foamular bajo losa interior 2.', 'techo'),
('Plafón Corrido PCR- 8', 'techo'),
('Plafón Corrido PCR-11', 'techo'),
('Plafón Corrido PCR-13', 'techo'),
('Plafón Corrido PCR-19', 'techo'),
('Plafón Corrido PCR-30', 'techo'),
('Vigueta base', 'techo'),
('Foamular sobre losa 1 pulg.', 'techo'),
('Foamular sobre losa 1.5 pulg.', 'techo'),
('Foamular sobre losa 2 pulg.', 'techo'),
('Foamular sobre losa 2.5 pulg.', 'techo'),
('Foamular bajo losa interior 1 ', 'techo'),
('Foamular bajo losa interior 1.', 'techo'),
('Foamular bajo losa interior 2 ', 'techo'),
('Foamular bajo losa interior 2.', 'techo'),
('Plafón Corrido PCR- 8', 'techo'),
('Plafón Corrido PCR-11', 'techo'),
('Plafón Corrido PCR-13', 'techo'),
('Plafón Corrido PCR-19', 'techo'),
('Plafón Corrido PCR-30', 'techo'),
('Poliestireno base', 'techo'),
('Foamular sobre losa 1 pulg.', 'techo'),
('Foamular sobre losa 1.5 pulg.', 'techo'),
('Foamular sobre losa 2 pulg.', 'techo'),
('Foamular sobre losa 2.5 pulg.', 'techo'),
('Foamular bajo losa interior 1 ', 'techo'),
('Foamular bajo losa interior 1.', 'techo'),
('Foamular bajo losa interior 2 ', 'techo'),
('Foamular bajo losa interior 2.', 'techo'),
('Plafón Corrido PCR- 8', 'techo'),
('Plafón Corrido PCR-11', 'techo'),
('Plafón Corrido PCR-13', 'techo'),
('Plafón Corrido PCR-19', 'techo'),
('Plafón Corrido PCR-30', 'techo'),
('Ventana base', 'ventana'),
('Ventana claro de 3mm', 'ventana'),
('Ventana claro de 6mm', 'ventana'),
('Ventana doble claro 3mm/6mm aire', 'ventana'),
('Ventana doble claro 6mm/6mm aire', 'ventana'),
('Ventana doble claro 3mm/13mm aire', 'ventana'),
('Ventana doble claro 6mm/13mm aire', 'ventana'),
('Piso ventilado concreto', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Piso ventilado Vigueta Bovedil', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Piso ventilado Vigueta Bovedil', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 1', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Foamular bajo piso ventilado 2', 'piso'),
('Muro concreto 10 cm', 'muro'),
('Muro lambrín R8', 'muro'),
('Foamular con tabla de yeso 1 p', 'muro'),
('Foamular con tabla de yeso 1.5', 'muro'),
('Foamular con tabla de yeso 2 p', 'muro'),
('Foamular con tabla de yeso 2.5', 'muro'),
('Foamular exterior 1 pulg.', 'muro'),
('Foamular exterior 1.5 pulg.', 'muro'),
('Foamular exterior 2 pulg.', 'muro'),
('Foamular exterior 2.5 pulg.', 'muro'),
('Muro block 10 cm', 'muro'),
('Muro lambrí­n R8', 'muro'),
('Foamular con tabla de yeso 1 p', 'muro'),
('Foamular con tabla de yeso 1.5', 'muro'),
('Foamular con tabla de yeso 2 p', 'muro'),
('Foamular con tabla de yeso 2.5', 'muro'),
('Foamular exterior 1 pulg.', 'muro'),
('Foamular exterior 1.5 pulg.', 'muro'),
('Foamular exterior 2 pulg.', 'muro'),
('Foamular exterior 2.5 pulg.', 'muro'),
('Muro ladrillo 10 cm', 'muro'),
('Muro lambrín R8', 'muro'),
('Foamular con tabla de yeso 1 p', 'muro'),
('Foamular con tabla de yeso 1.5', 'muro'),
('Foamular con tabla de yeso 2 p', 'muro'),
('Foamular con tabla de yeso 2.5', 'muro'),
('Foamular exterior 1 pulg.', 'muro'),
('Foamular exterior 1.5 pulg.', 'muro'),
('Foamular exterior 2 pulg.', 'muro'),
('Foamular exterior 2.5 pulg.', 'muro');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;