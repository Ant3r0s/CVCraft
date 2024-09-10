from fpdf import FPDF
from PIL import Image

def obtener_datos():
    print("Por favor, rellena la siguiente información para crear tu CV:")
    
    nombre = input("Nombre completo: ")
    perfil = input("Perfil profesional: ")
    experiencia = input("Experiencia laboral: ")
    educacion = input("Educación: ")
    habilidades = input("Habilidades: ")
    contactos = input("Información de contacto: ")
    foto_path = input("Ruta de la foto o logo (deja en blanco si no deseas agregar una imagen): ")
    
    print("\nSelecciona el estilo del CV:")
    print("1. Serio")
    print("2. Sofisticado")
    print("3. Informal")
    estilo = input("Elige un número (1/2/3): ")
    
    return nombre, perfil, experiencia, educacion, habilidades, contactos, foto_path, estilo

def crear_pdf(nombre, perfil, experiencia, educacion, habilidades, contactos, foto_path, estilo):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Curriculum Vitae', 0, 1, 'C')
            self.ln(5)

        def chapter_title(self, title, estilo):
            if estilo == '1':  # Serio
                self.set_font('Arial', 'B', 14)
            elif estilo == '2':  # Sofisticado
                self.set_font('Times', 'B', 14)
            else:  # Informal
                self.set_font('Comic Sans MS', 'B', 14)
            self.cell(0, 10, title, 0, 1, 'L')
            self.ln(2)

        def chapter_body(self, body, estilo):
            if estilo == '1':  # Serio
                self.set_font('Arial', '', 12)
            elif estilo == '2':  # Sofisticado
                self.set_font('Times', '', 12)
            else:  # Informal
                self.set_font('Comic Sans MS', '', 12)
            self.multi_cell(0, 10, body)
            self.ln()

    pdf = PDF()
    pdf.add_page()

    # Agregar la imagen si se proporciona
    if foto_path:
        try:
            imagen = Image.open(foto_path)
            imagen = imagen.resize((40, 40))
            imagen.save('temp_img.jpg')
            pdf.image('temp_img.jpg', x=10, y=10, w=40)
        except Exception as e:
            print(f"Error al añadir la imagen: {e}")

    # Agregar contenido
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, nombre, 0, 1, 'C')
    pdf.ln(10)

    pdf.chapter_title('Perfil Profesional', estilo)
    pdf.chapter_body(perfil, estilo)

    pdf.chapter_title('Experiencia Laboral', estilo)
    pdf.chapter_body(experiencia, estilo)

    pdf.chapter_title('Educación', estilo)
    pdf.chapter_body(educacion, estilo)

    pdf.chapter_title('Habilidades', estilo)
    pdf.chapter_body(habilidades, estilo)

    pdf.chapter_title('Contactos', estilo)
    pdf.chapter_body(contactos, estilo)

    # Guardar el PDF
    pdf.output('CV.pdf')

if __name__ == "__main__":
    nombre, perfil, experiencia, educacion, habilidades, contactos, foto_path, estilo = obtener_datos()
    print("¿Deseas crear el CV con la información proporcionada? (sí/no)")
    confirmacion = input().strip().lower()

    if confirmacion == 'sí' or confirmacion == 'si':
        crear_pdf(nombre, perfil, experiencia, educacion, habilidades, contactos, foto_path, estilo)
        print("CV creado exitosamente y guardado como 'CV.pdf'.")
    else:
        print("Operación cancelada.")
