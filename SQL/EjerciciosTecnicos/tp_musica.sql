-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-11-2021 a las 08:15:44
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
-- Base de datos: `tp musica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artistas`
--

CREATE TABLE `artistas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(140) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `artistas`
--

INSERT INTO `artistas` (`id`, `nombre`) VALUES
(1, 'Romeo Santos'),
(2, 'Tini'),
(3, 'La nueva luna'),
(4, 'Bad Bunny'),
(5, 'Damas Gratis'),
(6, 'Lali'),
(7, 'Callejeros'),
(8, 'Ataque 77'),
(9, 'Karol G'),
(10, 'Prince Royce');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artistas_canciones`
--

CREATE TABLE `artistas_canciones` (
  `id` int(11) NOT NULL,
  `artista_id` int(11) NOT NULL,
  `cancion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `artistas_canciones`
--

INSERT INTO `artistas_canciones` (`id`, `artista_id`, `cancion_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 8, 11),
(4, 8, 12),
(5, 4, 16),
(6, 4, 15),
(7, 7, 10),
(8, 7, 9),
(9, 5, 3),
(10, 5, 4),
(11, 9, 14),
(12, 9, 13),
(13, 6, 8),
(14, 6, 7),
(15, 3, 17),
(16, 10, 18),
(17, 2, 6),
(18, 2, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canciones`
--

CREATE TABLE `canciones` (
  `id` int(11) NOT NULL,
  `titulo` varchar(140) NOT NULL,
  `precio` int(11) NOT NULL,
  `descripcion` varchar(140) NOT NULL,
  `ritmo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `canciones`
--

INSERT INTO `canciones` (`id`, `titulo`, `precio`, `descripcion`, `ritmo_id`) VALUES
(1, 'Propuesta indecente', 100, 'Romeo Santos', 5),
(2, 'Eres mia', 200, 'Romeo Santos', 5),
(3, 'La pollera colorada', 50, 'Damas Gratis', 1),
(4, 'Menea para mi', 60, 'Damas Gratis', 1),
(5, 'Te quiero mas', 80, 'Tini', 4),
(6, 'Mienteme', 120, 'Tini', 4),
(7, 'Pa que me quieres', 90, 'Lali', 4),
(8, 'Una na', 90, 'Lali', 4),
(9, 'Imposible', 70, 'Callejeros', 3),
(10, '9 de julio', 75, 'Callejeros', 3),
(11, 'Hacelo por mi', 85, 'Ataque 77', 3),
(12, 'Chance', 65, 'Ataque 77', 3),
(13, 'Ocean', 150, 'Karol G', 2),
(14, 'Culpables', 100, 'Karol G', 2),
(15, 'Amorfoda', 90, 'Bad Bunny', 2),
(16, 'Vete', 75, 'Bad Bunny', 2),
(17, 'Y ahora te vas', 85, 'La nueva luna', 1),
(18, 'Darte un beso', 65, 'Prince Royce', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ritmos`
--

CREATE TABLE `ritmos` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(140) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ritmos`
--

INSERT INTO `ritmos` (`id`, `descripcion`) VALUES
(1, 'cumbia'),
(2, 'reggaeton'),
(3, 'rock'),
(4, 'pop'),
(5, 'bachata');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `artistas`
--
ALTER TABLE `artistas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `artistas_canciones`
--
ALTER TABLE `artistas_canciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `relacion_artista` (`artista_id`),
  ADD KEY `relacion_cancion` (`cancion_id`);

--
-- Indices de la tabla `canciones`
--
ALTER TABLE `canciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `relacion_ritmo` (`ritmo_id`);

--
-- Indices de la tabla `ritmos`
--
ALTER TABLE `ritmos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `artistas`
--
ALTER TABLE `artistas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `artistas_canciones`
--
ALTER TABLE `artistas_canciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `canciones`
--
ALTER TABLE `canciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `ritmos`
--
ALTER TABLE `ritmos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `artistas_canciones`
--
ALTER TABLE `artistas_canciones`
  ADD CONSTRAINT `relacion_artista` FOREIGN KEY (`artista_id`) REFERENCES `artistas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `relacion_cancion` FOREIGN KEY (`cancion_id`) REFERENCES `canciones` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `canciones`
--
ALTER TABLE `canciones`
  ADD CONSTRAINT `relacion_ritmo` FOREIGN KEY (`ritmo_id`) REFERENCES `ritmos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
