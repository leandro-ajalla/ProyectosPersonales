from bottle import run, route, request, template, redirect
import sqlite3

conn = sqlite3.connect('pedidos_soporte.db')
conn.execute('''DROP TABLE IF EXISTS pedidos;''')
conn.execute('''DROP TABLE IF EXISTS fallas;''')


conn.execute('''CREATE TABLE IF NOT EXISTS fallas
                (id             INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion     TEXT                NOT NULL)''')

conn.execute('''CREATE TABLE IF NOT EXISTS pedidos
                (id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                 fecha_carga        TEXT                NOT NULL,
                 id_equipo          VARCHAR(8)          NOT NULL,
                 id_falla           INTEGER             NOT NULL,
                 fecha_solucion     TEXT                        ,
                 empleado_it        VARCHAR(4)                  ,
                 FOREIGN KEY (id_falla) REFERENCES fallas(id))''')

conn.close()

@route('/')
def r_pedidos():
    return template('pedido-soporte.html')

@route('/pedido-soporte')
def pedido_soporte():
    id_equipo = request.GET.get('id_equipo','')
    falla = request.GET.get('tipo_falla','')
    conn = sqlite3.connect('pedidos_soporte.db')
    
    query = f"""INSERT INTO
                fallas (descripcion)
                VALUES ('{falla}');"""
    
    conn.execute(query)
    conn.commit()
    
    query = f"""SELECT MAX(id) FROM fallas"""
    
    resultado = conn.execute(query).fetchall()
    
    id_falla = resultado[0][0]
    
    query = f"""INSERT INTO
                pedidos (fecha_carga, id_equipo, id_falla, fecha_solucion, empleado_it)
                VALUES  (datetime('now','localtime'), '{id_equipo}', {id_falla}, NULL, NULL);"""
    
    conn.execute(query)
    conn.commit()
    conn.close()
    redirect('/')
        
@route('/consultas')
def get_pedidos():
    estado = request.GET.get('estado','pendiente')
    empleado = request.GET.get('empleado','')
    fecha_carga = request.GET.get('fecha_carga','')
    conn = sqlite3.connect('pedidos_soporte.db')
    
    query = f""""""
    if(estado == "pendiente"):
        query = f"""SELECT pedidos.fecha_carga, pedidos.id_equipo, fallas.id, pedidos.fecha_solucion, pedidos.empleado_it, fallas.descripcion FROM pedidos
                JOIN fallas ON pedidos.id_falla = fallas.id
                WHERE pedidos.fecha_solucion IS NULL"""
    elif(estado == "solucionado"):
        query = f"""SELECT pedidos.fecha_carga, pedidos.id_equipo, fallas.id, pedidos.fecha_solucion, pedidos.empleado_it, fallas.descripcion FROM pedidos
                JOIN fallas ON pedidos.id_falla = fallas.id
                WHERE pedidos.fecha_solucion IS NOT NULL"""
        
    if(empleado != ''):
        query = f"""SELECT pedidos.fecha_carga, pedidos.id_equipo, pedidos.fecha_solucion, pedidos.empleado_it, fallas.descripcion FROM pedidos
                JOIN fallas ON pedidos.id_falla = fallas.id
                WHERE pedidos.empleado_it = '{empleado}'"""
    if(fecha_carga != ''):
        query = f"""SELECT pedidos.fecha_carga, pedidos.id_equipo, pedidos.fecha_solucion, pedidos.empleado_it, fallas.descripcion pedidos
                JOIN fallas ON pedidos.id_falla = fallas.id
                WHERE fecha(pedidos.fecha_carga) = fecha('{fecha_carga}')"""
        
    resultado = conn.execute(query).fetchall()
    print (resultado)
    
    return template('consultas.html', estado = estado, empleado = empleado, fecha_carga = fecha_carga, resultado = resultado)

@route('/solucionado')
def dar_por_solucionado():
    id_solucion = request.GET.get('id','0')
    empleado = request.GET.get('itguy','')
    conn = sqlite3.connect('pedidos_soporte.db')
    
    query = f"""UPDATE pedidos
            SET empleado_it = '{empleado}',
            fecha_solucion = datetime('now','localtime')
            WHERE id = {id_solucion};"""
    
    conn.execute(query)
    conn.commit()
    conn.close()
    
    redirect (f"""/consultas?estado=solucionado""")
    
@route('/siguiente')
def siguiente_pedido():
    conn = sqlite3.connect('pedidos_soporte.db')
    
    query = f"""SELECT MIN(id)
                FROM pedidos
                WHERE pedidos.fecha_solucion IS NULL"""
    
    resultado = conn.execute(query).fetchall()
    
    siguiente_id = resultado[0][0]
    
    query = f"""SELECT pedidos.fecha_carga, pedidos.id_equipo, fallas.id, pedidos.fecha_solucion, pedidos.empleado_it, fallas.descripcion FROM pedidos
            JOIN fallas ON pedidos.id_falla = fallas.id
            WHERE pedidos.id = {siguiente_id}"""
    
    resultado = conn.execute(query).fetchall()
    
    return template('siguiente.html', resultado = resultado[0])

run(host='localhost', port=8081, debug=False)