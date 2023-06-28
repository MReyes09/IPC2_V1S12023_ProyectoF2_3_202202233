from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/get_Usuarios', methods = ['GET'])

def get_Usuarios():

    try:

        if request.method == "GET":

            retorno = {
                "usuario": [
                        {
                        "rol": "cliente",
                        "nombre": "Alex",
                        "apellido": "Johnson",
                        "telefono": "555123456",
                        "correo": "alex.johnson@example.com",
                        "contrasena": "alexpass123"
                    },
                    {
                        "rol": "administrador",
                        "nombre": "Emily",
                        "apellido": "Davis",
                        "telefono": "555987654",
                        "correo": "emily.davis@example.com",
                        "contrasena": "emilypassword"
                    },
                    {
                        "rol": "cliente",
                        "nombre": "Michael",
                        "apellido": "Brown",
                        "telefono": "555567890",
                        "correo": "michael.brown@example.com",
                        "contrasena": "mikepass789"
                    }
                ]
            }
        else: 
            retorno = {'mensaje': 'Error en la peticion, metodo incorrecto'}
        
        return jsonify(retorno)
    
    except:

        return {'mensaje': 'Error interno del servidor', "status": 500}

@app.route('/get_Peliculas', methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno = {
                "categoria": [
                {
                    "nombre": "Aventura",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Las momias del faraon",
                                "director": "Luc Besson",
                                "anio": "2010",
                                "fecha": "2023-02-05",
                                "hora": "19:30",
                                "imagen": "https://es.web.img2.acsta.net/medias/nmedia/18/78/77/56/19477844.jpg",
                                "precio": "52"
                            },
                            {
                                "titulo": "Aladdin",
                                "director": "Chad Stahelski",
                                "anio": "2019",
                                "fecha": "2023-06-06",
                                "hora": "20:00",
                                "imagen": "https://m.media-amazon.com/images/M/MV5BMjQ2ODIyMjY4MF5BMl5BanBnXkFtZTgwNzY4ODI2NzM@._V1_FMjpg_UX1000_.jpg",
                                "precio": "55"
                            }
                        ]
                    }
                },
                {
                    "nombre": "Infantil",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Sing 2",
                                "director": "Garth Jenningsr",
                                "anio": "2021",
                                "fecha": "2023-04-05",
                                "hora": "14:30",
                                "imagen": "https://www.universalpictures.com.ar/tl_files/content/movies/sing2/posters/01.jpg",
                                "precio": "75"
                            },
                            {
                                "titulo": "spirited away",
                                "director": "Hayao Miyazaki",
                                "anio": "2001",
                                "fecha": "2023-07-07",
                                "hora": "21:15",
                                "imagen": "https://cinematecadebogota.gov.co/sites/default/files/styles/318_x_460/public/afiches/screen_shot_2021-07-30_at_4.18.59_pm.png?itok=9pijB2o2",
                                "precio": "82"
                            }
                        ]
                    }
                    }
            ]}
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/get_Cine', methods = ["GET"])
def get_Cine():
    try:
        if request.method == "GET":
            retorno = {
                "cine": [
                    {
                    "nombre": "Cine DEF",
                    "salas": {
                        "sala": [
                        {
                            "numero": "#USACIPC2_202212333_1",
                            "asientos": "100"
                        },
                        {
                            "numero": "#USACIPC2_202212333_2",
                            "asientos": "80"
                        },
                        {
                            "numero": "#USACIPC2_202212333_3",
                            "asientos": "120"
                        }
                        ]
                    }
                    },
                    {
                    "nombre": "Cine GHI",
                    "salas": {
                        "sala": [
                        {
                            "numero": "#USACIPC2_202223344_1",
                            "asientos": "80"
                        },
                        {
                            "numero": "#USACIPC2_202223344_2",
                            "asientos": "60"
                        },
                        {
                            "numero": "#USACIPC2_202223344_3",
                            "asientos": "100"
                        }
                        ]
                    }
                },
                {
                    "nombre": "Cine JKL",
                    "salas": {
                        "sala": [
                        {
                            "numero": "#USACIPC2_202236699_1",
                            "asientos": "120"
                    },
                    {
                            "numero": "#USACIPC2_202236699_2",
                            "asientos": "90"
                        },
                        {
                            "numero": "#USACIPC2_202236699_3",
                            "asientos": "150"
                        }
                        ]
                    }
                    }
                ]
            }

        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}    
        return retorno
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/get_Tarjeta', methods = ["GET"])
def get_Tarjeta():
    try:
        if request.method == "GET":
            retorno = {
                "tarjeta": [
                    {
                    "tipo": "Debito",
                    "numero": "1111222233334444",
                    "titular": "Alex Johnson",
                    "fecha_expiracion": "2025-06-30"
                    },
                    {
                    "tipo": "Credito",
                    "numero": "5555666677778888",
                    "titular": "Emily Davis",
                    "fecha_expiracion": "2023-11-15"
                    },
                    {
                    "tipo": "Debito",
                    "numero": "9999000011112222",
                    "titular": "Michael Brown",
                    "fecha_expiracion": "2024-09-12"
                    }
                ]
            }

        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}    
        return retorno
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)