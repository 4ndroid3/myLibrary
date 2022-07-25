export interface Libro {
    id:               number;
    created_by:       number;
    genero:           Genero[];
    autor:            Autor;
    img_cover:        string;
    created:          Date;
    modified:         Date;
    nombre:           string;
    anio_publicacion: number;
    hojas:            number;
    updated_by:       null;
}
export interface Autor {
    id:       number;
    created:  Date;
    modified: Date;
    nombre:   string;
    apellido: string;
    pais:     string;
}
export interface Genero {
    id:       number;
    created:  Date;
    modified: Date;
    nombre:   string;
}
