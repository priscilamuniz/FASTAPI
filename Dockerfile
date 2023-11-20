FROM python:3.12                        // de que imagen base de python
WORKDIR G:\My Drive\2. Data Science Henry\FastApi\main.py                         // quien es el dueño de la imagen
COPY                                     // copia de nuestro proyecto, el empaquetado
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]