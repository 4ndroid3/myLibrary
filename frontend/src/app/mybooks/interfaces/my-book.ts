import { Libro } from "src/app/books/interfaces/book";

export interface MiLibro {
    id:               number;
    created_by:       number;
    libro:            Libro;
    estante:          Estante;
    created:          Date;
    modified:         Date;
    fecha_leido:      Date;
    updated_by:       number;
    url:              string;
}

export interface Estante {
    id:               number;
    created:          Date;
    modified:         Date;
    nombre:           string;
    private:          boolean;
    created_by:       number;
    updated_by:       number;
    url:              string;
}