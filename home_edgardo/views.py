from django.shortcuts import render


GENEROS = [
    {
        'id': 'accion',
        'nombre': 'Acción',
        'descripcion': 'Películas llenas de adrenalina, combates, persecuciones y emoción constante.'
    },
    {
        'id': 'animacion',
        'nombre': 'Animación',
        'descripcion': 'Grandes historias ilustradas para todas las edades, magia visual y aventuras inolvidables.'
    }
]

PELICULAS = {
    'accion': [
        {'titulo': 'Gladiador', 'anio': 2000, 'imagen': 'images/gladiador.jpg'},
        {'titulo': 'Mad Max: Furia en el Camino', 'anio': 2015, 'imagen': 'images/mad_max.jpg'},
        {'titulo': 'John Wick', 'anio': 2014, 'imagen': 'images/john_wick.jpg'},
        {'titulo': 'Duro de Matar', 'anio': 1988, 'imagen': 'images/duro_de_matar.jpg'},
        {'titulo': 'Misión Imposible: Fallout', 'anio': 2018, 'imagen': 'images/mision_imposible.jpg'},
        {'titulo': 'Batman: El Caballero de la Noche', 'anio': 2008, 'imagen': 'images/batman.jpg'},
        {'titulo': 'Matrix', 'anio': 1999, 'imagen': 'images/matrix.jpg'},
        {'titulo': 'Terminator 2', 'anio': 1991, 'imagen': 'images/terminator_2.jpg'},
        {'titulo': 'Top Gun: Maverick', 'anio': 2022, 'imagen': 'images/top_gun.jpg'},
        {'titulo': 'El Rescate', 'anio': 2020, 'imagen': 'images/rescate.jpg'},
    ],
    'animacion': [
        {'titulo': 'Toy Story', 'anio': 1995, 'imagen': 'images/toy_story.jpg'},
        {'titulo': 'El Rey León', 'anio': 1994, 'imagen': 'images/rey_leon.jpg'},
        {'titulo': 'Shrek', 'anio': 2001, 'imagen': 'images/shrek.jpg'},
        {'titulo': 'Buscando a Nemo', 'anio': 2003, 'imagen': 'images/nemo.jpg'},
        {'titulo': 'Los Increíbles', 'anio': 2004, 'imagen': 'images/increibles.jpg'},
        {'titulo': 'Up: Una Aventura de Altura', 'anio': 2009, 'imagen': 'images/up.jpg'},
        {'titulo': 'Coco', 'anio': 2017, 'imagen': 'images/coco.jpg'},
        {'titulo': 'Spider-Man: Un Nuevo Universo', 'anio': 2018, 'imagen': 'images/spiderman.jpg'},
        {'titulo': 'Intensamente', 'anio': 2015, 'imagen': 'images/intensamente.jpg'},
        {'titulo': 'Wall-E', 'anio': 2008, 'imagen': 'images/walle.jpg'},
    ]
}


def inicio(request):
    data = {
        'generos': GENEROS
    }
    return render(request, 'home_edgardo/inicio.html', data)


def peliculas_por_genero(request, genero_id):
    genero_encontrado = None
    for g in GENEROS:
        if g['id'] == genero_id:
            genero_encontrado = g
            break
            
    lista_peliculas = PELICULAS.get(genero_id, [])

    data = {
        'genero': genero_encontrado,
        'peliculas': lista_peliculas
    }
    return render(request, 'home_edgardo/peliculas.html', data)