from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return '''
   
    <html>    
        <style>
            body {
                background-color: grey;
                color: rgb(161, 158, 158);
                font-style: italic;
                font-family: Georgia; text-align: justify;
            }
            h1 {
                text-align: center;
                text-decoration: underline;
                color: black
            } 
            #container {
                display: flex;
            }
            #text {
                background-image: url('/static/background.jpg');
                background-size: cover;
                float: right;
                width: 83%;
                height: 100vh;
                padding: 1em;
                color: None;
                line-height: 1.25
            }        
            #buttons {
                background-color: red;
                width: 17%;
                padding: 1em;
                text-align: left;
                font-size: 18px;
            }            
            button {
                line-height: 1.5em;
                font-size: 18px;
                text-align: left;   
            }

        </style> 

        <head>
            <title>ICAR WEB</title>
        <head>
        <h1 style="">__________  ICAR - Ingeniería Civil Argentina. __________ </h1>
        <body>        
            <div id="container">
                <div id="buttons">
                    <a href="/system_operation" target="_blank" style="position: absolute; top: 65px; left: 8px; height=80px; width: 190px; background-color: transparent; color: white; padding: 5px;" onmouseover="this.style.backgroundColor='blue'" onmouseout="this.style.backgroundColor='transparent'">1. Detalles de operación del sistema</a>
                    <a href="/panel_brochure" target="_blank" style="position: absolute; top: 125px; left: 8px; height=80px; width: 190px; background-color: transparent; color: white; padding: 5px;" onmouseover="this.style.backgroundColor='blue'" onmouseout="this.style.backgroundColor='transparent'">2. Folleto de paneles</a>
                    <a href="/investor_brochure" target="_blank" style="position: absolute; top: 165px; left: 8px; height=80px; width: 190px; background-color: transparent; color: white; padding: 5px;" onmouseover="this.style.backgroundColor='blue'" onmouseout="this.style.backgroundColor='transparent'">3. Folleto de inversores</a>
                    <button onclick="window.open(\'/static/company_data.html\', \'_blank\', \'height=400,width=300\')" style="position: absolute; top: 245px; left: 12px; height=500 width: 190px; border: none; text-decoration: underline; background-color: transparent; color: white; padding: 5px;" onmouseover="this.style.backgroundColor='blue'" onmouseout="this.style.backgroundColor='transparent'"> Contacto</button>
                </div>

                <div id="text">
                <p>Bienvenido y gracias por visitar nuestro sitio web de venta de Paneles Solares e Inversores CC/CA.</p>
                <p>&nbsp;&nbsp;Las energías alternativas son fuentes de energía renovable que se utilizan para producir electricidad, calor y combustibles. A diferencia de los combustibles fósiles como el petróleo, el carbón y el gas natural, que son finitos y tienen un impacto negativo en el medio ambiente, las energías alternativas son fuentes limpias e inagotables.</p>
                <p>&nbsp;&nbsp;Algunos ejemplos de energías alternativas son la energía solar, eólica, hidroeléctrica, geotérmica, de biomasa y de residuos. Estas energías pueden ser utilizadas para satisfacer las necesidades de energía en hogares, empresas e industrias, y su uso tiene numerosos beneficios.</p>
                <p>&nbsp;&nbsp;En primer lugar, las energías alternativas son sostenibles y no agotan los recursos naturales, lo que las hace una opción más viable a largo plazo que los combustibles fósiles. Además, el uso de energías alternativas reduce la dependencia de los combustibles importados, lo que mejora la seguridad energética y reduce la vulnerabilidad a las fluctuaciones de los precios del petróleo.</p>
                <p>&nbsp;&nbsp;En segundo lugar, las energías alternativas son más limpias y tienen un menor impacto ambiental que los combustibles fósiles. Al reducir las emisiones de gases de efecto invernadero y otros contaminantes, las energías alternativas contribuyen a combatir el cambio climático y mejoran la calidad del aire y del agua.</p>
                <p>&nbsp;&nbsp;En tercer lugar, el uso de energías alternativas puede generar empleo y estimular el crecimiento económico. La inversión en energías alternativas crea puestos de trabajo en sectores como la fabricación, la instalación y el mantenimiento de equipos de energía renovable, lo que beneficia a las comunidades locales y a la economía en general.</p>
                <p>&nbsp;&nbsp;En resumen, el uso de energías alternativas es una opción sostenible, limpia y económicamente viable para satisfacer las necesidades de energía en hogares, empresas e industrias. Con una inversión adecuada en tecnologías de energía renovable y una mayor conciencia sobre los beneficios de estas energías, podemos avanzar hacia un futuro más limpio y sostenible.</p>
                <p><br></p>

                <p>&nbsp;&nbsp;La <span style="font-size:larger; color:yellow; text-decoration: underline;">Energía Solar</span>  es una de las fuentes de energía renovable más populares y con mayor crecimiento en todo el mundo. Esta forma de energía aprovecha la luz solar y la convierte en electricidad a través de paneles solares. Una vez que se han instalado los paneles solares, la energía solar producida es gratuita y rentable a largo plazo. La energía solar es perfecta 
                    para utilizada en zonas remotas donde no existe acceso a la red eléctrica y reduce la dependencia de combustibles fósiles. En resumen, la energía solar es una forma de energía limpia, renovable y rentable que ofrece múltiples beneficios ambientales y económicos. Es la fuente con mayor crecimiento en todo el mundo. 
                    Una vez que se han instalado los paneles solares, la energía solar producida es gratuita y rentable a largo plazo. La energía solar es perfecta para utilizada en zonas remotas donde no existe acceso a la red eléctrica y puede contribuir a reducir 
                    la dependencia de combustibles fósiles.</p>   
                </div>
            </div>
        </body>
    </html>
    '''

@app.route('/alternative_energy')
def alternative_energy():
    return app.send_static_file('alternative_energy.pdf')

@app.route('/system_operation')
def system_operation():
    return app.send_static_file('Funcionamiento.pdf')

@app.route('/panel_brochure')
def panel_brochure():
    return app.send_static_file('PANEL.pdf')

@app.route('/investor_brochure')
def investor_brochure():
    return app.send_static_file('INVERSOR.pdf')

if __name__ == '__main__':
    app.run()
