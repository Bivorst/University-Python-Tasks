SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `music_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `music_db`;

CREATE TABLE `instruments` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `instruments` (`id`, `name`, `description`) VALUES
(1, 'Guitar', 'A string musical instrument usually played by plucking or strumming the strings with a pick or fingers. Widely used in rock, jazz, and blues.'),
(2, 'Drums', 'A percussion instrument consisting of a hollow body, usually covered with a skin or plastic membrane, played by striking. Important in genres like rock and jazz.'),
(3, 'Piano', 'A keyboard musical instrument in which strings are struck by hammers controlled by keys. Used in classical music, jazz, and pop music.'),
(4, 'Violin', 'A string instrument played with a bow. Known for its expressive sound and is an important instrument in classical orchestras.'),
(5, 'Bass Guitar', 'A string instrument with four strings, tuned lower than a regular guitar. Responsible for rhythm and harmony in rock, jazz, and pop music.'),
(6, 'Saxophone', 'A brass wind instrument often associated with jazz music. Produces a unique sound created by the vibration of a reed on the mouthpiece.'),
(7, 'Trumpet', 'A brass wind instrument with three valves, often used in jazz and classical music. Has a bright sound that is easily heard among other instruments.'),
(8, 'Flute', 'A wind instrument played by blowing air into a hole in the mouthpiece. Known for its bright and clear sound, used in classical music.'),
(9, 'Keyboards', 'An electronic musical instrument that uses keys to produce various sounds. Can imitate sounds of a piano, organ, or synthesizer.'),
(10, 'Cello', 'A string instrument larger than the violin, played with a bow. Important in classical music and known for its deep, rich sound.');

CREATE TABLE `songs` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `instruments` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `songs` (`id`, `name`, `genre`, `instruments`) VALUES
(1, 'Rapsodia Bohemia', 'Roc', 'Guitar, Drums, Piano'),
(2, 'Imagina', 'Pop', 'Piano, Guitar'),
(3, 'Hotel California', 'Roc', 'Guitar, Drums, Bass Guitar'),
(4, 'Humo sobre el agua', 'Roc', 'Guitar, Drums, Bass Guitar'),
(5, 'Toma cinco', 'Jazz', 'Saxophone, Drums, Piano'),
(6, 'Ayer', 'Pop', 'Guitar, Piano'),
(7, 'Qué mundo tan maravilloso', 'Jazz', 'Trumpet, Piano, Bass Guitar'),
(8, 'Relojes', 'Pop', 'Piano, Guitar, Drums'),
(9, 'Primavera de Vivaldi', 'Clásica', 'Violin, Cello, Piano'),
(10, 'Mi corazón seguirá latiendo', 'Pop', 'Piano, Violin, Guitar');

ALTER TABLE `instruments`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `songs`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `instruments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

ALTER TABLE `songs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;