-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-11-2021 a las 00:16:26
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tp inmobilaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `barrios`
--

CREATE TABLE `barrios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(140) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `barrios`
--

INSERT INTO `barrios` (`id`, `nombre`) VALUES
(1, 'almagro'),
(2, 'balvanera'),
(3, 'boedo'),
(4, 'caballito'),
(5, 'flores'),
(6, 'san telmo'),
(7, 'palermo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fotos`
--

CREATE TABLE `fotos` (
  `id` int(11) NOT NULL,
  `alternativo` varchar(140) NOT NULL,
  `link` varchar(140) NOT NULL,
  `propiedad_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fotos`
--

INSERT INTO `fotos` (`id`, `alternativo`, `link`, `propiedad_id`) VALUES
(1, 'Depto alquiler almagro 2 ambientes', '/Deptoalquileralmagro2ambientes.jpg', 8),
(2, 'Depto venta almagro 3 ambientes', '/Deptoventaalmagro3ambientes.jpg', 2),
(3, 'Depto alquiler balvanera 2 ambientes', '/Deptoalquilerbalvanera2ambientes.jpg', 9),
(4, 'Depto venta balvanera 3 ambientes', '/Deptoventabalvanera3ambientes.jpg', 3),
(5, 'Depto alquiler boedo 2 ambientes', '/Deptoalquilerboedo2ambientes.jpg', 10),
(6, 'Depto venta boedo 3 ambientes', '/Deptoventaboedo3ambientes.jpg', 4),
(7, 'Depto alquiler caballito 2 ambientes', '/Deptoalquilercaballito2ambientes.jpg', 11),
(8, 'Depto venta caballito 3 ambientes', '/Deptoventacaballito3ambientes.jpg', 5),
(9, 'Depto alquiler flores 2 ambientes', '/Deptoalquilerflores2ambientes.jpg', 12),
(10, 'Depto venta flores 3 ambientes', '/Deptoventaflores3ambientes.jpg', 6),
(11, 'Depto alquiler temporal palermo monoambiente', '/Deptoalquilertemporalpalermomonoambiente.jpg', 14),
(12, 'Depto alquiler temporal san telmo monoambiente', '/Deptoalquilertemporalsantelmomonoambiente.jpg', 15),
(13, 'venta san telmo dpto 3 ambientes', '/ventasantelmodpto3ambientes.jpg', 7),
(14, 'Depto alquiler palermo 2 ambientes', '/Deptoalquilerpalermo2ambientes.jpg', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operaciones`
--

CREATE TABLE `operaciones` (
  `id` int(11) NOT NULL,
  `tipo` varchar(140) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operaciones`
--

INSERT INTO `operaciones` (`id`, `tipo`) VALUES
(1, 'alquiler'),
(2, 'alquiler temporal'),
(3, 'venta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operaciones_personas`
--

CREATE TABLE `operaciones_personas` (
  `id` int(11) NOT NULL,
  `operacion_id` int(11) NOT NULL,
  `persona_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operaciones_personas`
--

INSERT INTO `operaciones_personas` (`id`, `operacion_id`, `persona_id`) VALUES
(1, 1, 2),
(2, 1, 4),
(3, 3, 1),
(4, 2, 9),
(5, 2, 5),
(6, 3, 10),
(7, 1, 8),
(8, 3, 6),
(9, 1, 3),
(10, 3, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operaciones_propiedades`
--

CREATE TABLE `operaciones_propiedades` (
  `id` int(11) NOT NULL,
  `propiedad_id` int(11) NOT NULL,
  `operacion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operaciones_propiedades`
--

INSERT INTO `operaciones_propiedades` (`id`, `propiedad_id`, `operacion_id`) VALUES
(1, 4, 3),
(2, 15, 2),
(3, 6, 3),
(4, 12, 1),
(5, 2, 3),
(6, 11, 1),
(7, 3, 3),
(8, 10, 1),
(9, 7, 3),
(10, 5, 3),
(11, 14, 2),
(12, 9, 1),
(13, 13, 1),
(14, 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(140) NOT NULL,
  `telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `nombre`, `telefono`) VALUES
(1, 'leandro', 49684245),
(2, 'alexis', 48963185),
(3, 'sebastian', 96563256),
(4, 'aryan', 85452365),
(5, 'maria', 23657896),
(6, 'rose', 32156985),
(7, 'vanesa', 12361263),
(8, 'romina', 39827150),
(9, 'liam', 98215685),
(10, 'melany', 14257436);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propiedades`
--

CREATE TABLE `propiedades` (
  `id` int(11) NOT NULL,
  `direccion` varchar(140) NOT NULL,
  `metros` int(11) NOT NULL,
  `descripcion` text NOT NULL,
  `barrio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `propiedades`
--

INSERT INTO `propiedades` (`id`, `direccion`, `metros`, `descripcion`, `barrio_id`) VALUES
(2, 'colombres 55', 30, 'venta dpto 3 ambientes\r\n2 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\nterraza', 1),
(3, 'ecuador 311', 30, 'venta dpto 3 ambientes\r\n2 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\nterraza', 2),
(4, 'av boedo 456', 30, 'venta dpto 3 ambientes\r\n2 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\nterraza', 3),
(5, 'rosario 345', 30, 'venta dpto 3 ambientes\r\n2 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\nterraza', 4),
(6, 'av lafuente 26', 30, 'venta dpto 3 ambientes\r\n2 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\nterraza', 5),
(7, 'peru 565', 29, 'venta dpto 3 ambientes\n2 dormitorio\n1 baño\nliving-comedor\ncocina\nterraza', 6),
(8, 'yapeyu 345', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina', 1),
(9, 'sarmiento 345', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina', 2),
(10, 'maza 890', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\n', 3),
(11, 'doblas 34', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\n', 4),
(12, 'av nazca 356', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\n', 5),
(13, 'segui 567', 25, 'alquiler dpto 2 ambientes\r\n1 dormitorio\r\n1 baño\r\nliving-comedor\r\ncocina\r\n', 7),
(14, 'salguero 3008', 0, 'alquiler temporal dpto monoambiente\r\n1 dormitorio\r\n1 baño\r\ncocina\r\n', 7),
(15, 'av independencia 456', 20, 'alquiler temporal dpto monoambiente\r\n1 dormitorio\r\n1 baño\r\ncocina\r\n', 6);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `barrios`
--
ALTER TABLE `barrios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fotos`
--
ALTER TABLE `fotos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `propiedad_id` (`propiedad_id`);

--
-- Indices de la tabla `operaciones`
--
ALTER TABLE `operaciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `operaciones_personas`
--
ALTER TABLE `operaciones_personas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `operacion_id` (`operacion_id`),
  ADD KEY `persona_id` (`persona_id`);

--
-- Indices de la tabla `operaciones_propiedades`
--
ALTER TABLE `operaciones_propiedades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `operacion_id` (`operacion_id`),
  ADD KEY `propiedad_id` (`propiedad_id`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `propiedades`
--
ALTER TABLE `propiedades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `barrio_id` (`barrio_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `barrios`
--
ALTER TABLE `barrios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `fotos`
--
ALTER TABLE `fotos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `operaciones`
--
ALTER TABLE `operaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `operaciones_personas`
--
ALTER TABLE `operaciones_personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `operaciones_propiedades`
--
ALTER TABLE `operaciones_propiedades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `propiedades`
--
ALTER TABLE `propiedades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `fotos`
--
ALTER TABLE `fotos`
  ADD CONSTRAINT `fotos_ibfk_1` FOREIGN KEY (`propiedad_id`) REFERENCES `propiedades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `operaciones_personas`
--
ALTER TABLE `operaciones_personas`
  ADD CONSTRAINT `operaciones_personas_ibfk_1` FOREIGN KEY (`operacion_id`) REFERENCES `operaciones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `operaciones_personas_ibfk_2` FOREIGN KEY (`persona_id`) REFERENCES `personas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `operaciones_propiedades`
--
ALTER TABLE `operaciones_propiedades`
  ADD CONSTRAINT `operaciones_propiedades_ibfk_1` FOREIGN KEY (`operacion_id`) REFERENCES `operaciones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `operaciones_propiedades_ibfk_2` FOREIGN KEY (`propiedad_id`) REFERENCES `propiedades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `propiedades`
--
ALTER TABLE `propiedades`
  ADD CONSTRAINT `propiedades_ibfk_1` FOREIGN KEY (`barrio_id`) REFERENCES `barrios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
