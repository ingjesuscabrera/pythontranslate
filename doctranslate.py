#pip install googletrans==4.0.0-rc1
from googletrans import Translator

def translate_document(input_file, output_file, source_lang, target_lang):
    try:
        # Leer el contenido del archivo de entrada
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Crear una instancia del traductor
        translator = Translator()

        # Traducir el contenido del documento
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)

        # Guardar la traducción en el archivo de salida
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text.text)

        print(f"Documento traducido de {source_lang} a {target_lang} y guardado en {output_file}")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Ejemplo de uso
translate_document('documento.txt', 'documento_traducido.txt', 'en', 'es')
