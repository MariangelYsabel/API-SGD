CREATE TABLE IF NOT EXISTS `Artista` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Album` (
	`id` integer primary key NOT NULL UNIQUE,
	`titulo` TEXT NOT NULL,
	`ano_publicacion` INTEGER NOT NULL,
	`artista_id` INTEGER NOT NULL,
FOREIGN KEY(`artista_id`) REFERENCES `Artista`(`id`)
);
CREATE TABLE IF NOT EXISTS `Cancion` (
	`id` integer primary key NOT NULL UNIQUE,
	`titulo` TEXT NOT NULL,
	`duracion` INTEGER NOT NULL,
	`album_id` INTEGER NOT NULL,
FOREIGN KEY(`album_id`) REFERENCES `Album`(`id`)
);

FOREIGN KEY(`artista_id`) REFERENCES `Artista`(`id`)
FOREIGN KEY(`album_id`) REFERENCES `Album`(`id`)