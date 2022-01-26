#======================================================================================
#======================================================================================
#Librerias utilizadas
#Pandas - Limpieza, filtrado de DataFrames
#Streamlit - Interfaz gráfica
import pandas as pd
import streamlit as st

from google.oauth2.service_account import Credentials
from gspread_pandas import Spread, Client

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#Evaluar las listas dentro del DataFrame
from ast import literal_eval
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#Listas para utilizas en el documento
#Empresa/Hub
e_hub = sorted(["EasyGo","Lets Advertise","Administración","RRHH","TPP","TPP Extreme","TPP Fénix","TPP ULTRA","TOM"])
#--------------------------------------------------------------------------------------
#Puestos registrados
nombre_puesto = sorted(['Gerente Contable y Auditor Regional','Asistente Contable','Intendencia y Mensajería','Jefe Local de Contabilidad','Programador/a','Encargado del Dpto. de IT ','Asistente de IT', 'Project Manager','Front-End Developer','Asesor Comercial','Gerente de Desarrollo, Easy Go','Diseñador/a Gráfico/a','Asistente Lets Advertise','SEO','Gerente de Medios','Científico de Datos','Gerente de Recursos Humanos','Asistente de Recursos Humanos','Asistente TOM','Social Media Manager','Ejecutiva de Cuentas','Asistente de Cuentas','Gerente de División TOM','Trafficker','Gerente de Ventas','Gerente de División TPP','Gerente de Operaciones','Gerente Financiero Administrativo','Gerente Comercial','Gerente de Nuevos Negocios','Copywritter'])
#--------------------------------------------------------------------------------------
#Nombres de las columnas nuevo documento
name_columns = ["Nombres", "Apellidos", "Género", "Fecha de Nacimiento","Empresa/Hub", "Email", "Puesto", "Lugar Diversificado", "Nombre Diversificado", "Estado Diversificado", "Lugar Licenciatura", "Nombre Licenciatura", "Estado Licenciatura", "Semestre", "Lugar Maestría/Posgrado", "Nombre Maestría/Posgrado", "Estado Maestría/Posgrado", "Lugar Cursos/Diplomados/Certificaciones", "Nombre Cursos/Diplomados/Certificaciones", "Estado Cursos/Diplomados/Certificaciones", "Completo"]
#--------------------------------------------------------------------------------------
#Nombres de las columnas nuevo documento
#name_columns = ["Nombres", "Apellidos", "Género", "Fecha de Nacimiento","Empresa/Hub", "Email", "Puesto", "Lugar Diversificado", "Nombre Diversificado", "Estado Diversificado", "Lugar Licenciatura", "Nombre Licenciatura", "Estado Licenciatura", "Lugar Maestría/Posgrado", "Nombre Maestría/Posgrado", "Estado Maestría/Posgrado", "Lugar Cursos/Diplomados/Certificaciones", "Nombre Cursos/Diplomados/Certificaciones", "Estado Cursos/Diplomados/Certificaciones", "Completo"]
#--------------------------------------------------------------------------------------
#Configuración de la página para que esta sea ancha
st.set_page_config(layout="wide")
#--------------------------------------------------------------------------------------
#Configuración para ocultar menu de hamburguesa y pie de página
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html = True)
#st.write(st.secrets["s_g"])
#--------------------------------------------------------------------------------------
#Session state
if 'df_filtro' not in st.session_state:
    st.session_state.df_filtro = pd.DataFrame(columns = name_columns)
#======================================================================================
#======================================================================================
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_info(st.secrets["s_g"], scopes=scope)
client = Client(scope=scope, creds=credentials)
spread = Spread("Output_Form", client=client)

df = spread.sheet_to_df().reset_index()
#st.write(spread_df.reset_index())
#======================================================================================
#======================================================================================
if 'df_general' not in st.session_state:
    st.session_state.df_general = pd.DataFrame(columns = name_columns)
if 'lugar_d' not in st.session_state:
    st.session_state.lugar_d = []
if 'lugar_l' not in st.session_state:
    st.session_state.lugar_l = []
if 'lugar_m' not in st.session_state:
    st.session_state.lugar_m = []
if 'lugar_c' not in st.session_state:
    st.session_state.lugar_c = []
#======================================================================================
if 'titulo_d' not in st.session_state:
    st.session_state.titulo_d = []
if 'titulo_l' not in st.session_state:
    st.session_state.titulo_l = []
if 'titulo_m' not in st.session_state:
    st.session_state.titulo_m = []
if 'titulo_c' not in st.session_state:
    st.session_state.titulo_c = []
#======================================================================================
if 'e_d' not in st.session_state:
    st.session_state.e_d = []
if 'e_l' not in st.session_state:
    st.session_state.e_l = []
if 'e_m' not in st.session_state:
    st.session_state.e_m = []
if 'e_c' not in st.session_state:
    st.session_state.e_c = []

if 'e_ll' not in st.session_state:
    st.session_state.e_ll = []
#======================================================================================
#======================================================================================
st.title("Cualquier otra imagen...")
st.image("https://imgur.com/dcNy0eA")
st.markdown("***")
st.subheader("Agregar información colaborador")
add_user = st.expander("Formulario", expanded = False)
with add_user:
    st.markdown("###### Información general")
    c_1, c_2, c_3 = st.columns(3)
    nombres = c_1.text_input("Nombres")
    apellidos = c_2.text_input("Apellidos")
    genero = c_3.selectbox("Género", ["F", "M"])
    fecha = c_1.date_input("Fecha de nacimiento - YY/MM/DD")
    empresa = c_2.multiselect("Empresa/Hub", e_hub)
    email = c_3.text_input("Correo Electrónico")
    puesto = c_1.multiselect("Puesto", nombre_puesto)
    #===================================================================
    #===================================================================
    st.markdown("###### Educación")
    c_4, c_5, c_6, c_7 = st.columns(4)
    with c_4:
        with st.form("Diversificado", clear_on_submit = True):
            st.markdown("###### Diversificado")
            st.markdown("######  ")
            lugar_d = st.text_input("Lugar")
            titulo_d = st.text_input("Título obtenido")
            e_d = st.selectbox("Estado", ["Terminado", "Cierre de Pensum", "En Curso"])
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            if st.form_submit_button("Agregar"):
                st.session_state.lugar_d.append(lugar_d)
                st.session_state.titulo_d.append(titulo_d)
                st.session_state.e_d.append(e_d)
    with c_5:
        with st.form("Licenciatura", clear_on_submit = True):
            st.markdown("###### Licenciatura")
            st.markdown("######  ")
            lugar_l = st.text_input("Lugar")
            titulo_l = st.text_input("Título obtenido")
            e_l = st.selectbox("Estado", ["N/A","Terminado", "Cierre de Pensum", "En Curso"])
            semestre = st.number_input("Semestre", 0, 12)
            if st.form_submit_button("Agregar"):
                st.session_state.lugar_l.append(lugar_l)
                st.session_state.titulo_l.append(titulo_l)
                st.session_state.e_l.append(e_l)
                st.session_state.e_ll.append(semestre)
    with c_6:
        with st.form("Maestria", clear_on_submit = True):
            st.markdown("###### Maestría/Posgrado")
            st.markdown("######  ")
            lugar_m = st.text_input("Lugar")
            titulo_m = st.text_input("Título obtenido")
            e_m = st.selectbox("Estado", ["N/A","Terminado", "Cierre de Pensum", "En Curso"])
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            if st.form_submit_button("Agregar"):
                st.session_state.lugar_m.append(lugar_m)
                st.session_state.titulo_m.append(titulo_m)
                st.session_state.e_m.append(e_m)
    with c_7:
        with st.form("Cursos", clear_on_submit = True):
            st.markdown("###### Cursos/Diplomados/Certificaciones")
            lugar_c = st.text_input("Lugar")
            titulo_c = st.text_input("Nombre")
            e_c = st.selectbox("Estado", ["N/A","Terminado", "En Curso"])
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            if st.form_submit_button("Agregar"):
                st.session_state.lugar_c.append(lugar_c)
                st.session_state.titulo_c.append(titulo_c)
                st.session_state.e_c.append(e_c)
    #===================================================================
    #===================================================================
    c_i = st.selectbox("Información Completa", ["No", "Si"])
    #st.write(st.session_state.lugar_c)
    #st.write(st.session_state.titulo_c)
    #===================================================================
    #===================================================================
    if st.button("Guardar Información", key = 1):
        df = spread.sheet_to_df()
        df_append = pd.DataFrame([[nombres, apellidos, genero, fecha, empresa, email, puesto, st.session_state.lugar_d, st.session_state.titulo_d, st.session_state.e_d, st.session_state.lugar_l, st.session_state.titulo_l, st.session_state.e_l, st.session_state.e_ll, st.session_state.lugar_m, st.session_state.titulo_m, st.session_state.e_m, st.session_state.lugar_c, st.session_state.titulo_c, st.session_state.e_c, c_i]], columns = name_columns)
        df = pd.concat([df, df_append], axis = 0)
        spread.df_to_sheet(df, index = False)



        st.session_state.lugar_d = []
        st.session_state.titulo_d = []
        st.session_state.e_d = []
        st.session_state.lugar_l = []
        st.session_state.titulo_l = []
        st.session_state.e_l = []
        st.session_state.e_ll = []
        st.session_state.lugar_m = []
        st.session_state.titulo_m = []
        st.session_state.e_m = []
        st.session_state.lugar_c = []
        st.session_state.titulo_c = []
        st.session_state.e_c = []
        st.balloons()
    #placeholder = st.empty()
    #input = placeholder.text_input('text')
    #click_clear = st.button('clear text input', key=1)
    #if click_clear:
        #input = placeholder.text_input('text', value='', key=1)
#======================================================================================
#======================================================================================
