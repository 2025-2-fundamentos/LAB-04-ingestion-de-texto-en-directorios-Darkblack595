# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    from pathlib import Path
    import pandas as pd
    import re
    
    frases_sentimiento_test = []
    frases_sentimiento_train = []

    # Directorio principal, aqui hay que crear la carpeta "output"
    main_directory = Path.cwd() / "files"

    # Creamos las referencias a las carpetas de test y train
    train_directory = main_directory / "input/input/train"
    test_directory = main_directory / "input/input/test"
    

    # Iteramos sobre los archivos en las carpetas para extraer las frases y nombres de los sentimientos

    for dir in train_directory.iterdir():
        for file in dir.iterdir():
            frases_sentimiento_train.append((file.read_text(), dir.parts[-1]))
    
    for dir in test_directory.iterdir():
        for file in dir.iterdir():
            frases_sentimiento_test.append((file.read_text(), dir.parts[-1]))

    # Creamos los dataframes

    test_dataframe = pd.DataFrame({
        "phrase":[frase for frase, _ in frases_sentimiento_test],
        "target":[sentimiento for _, sentimiento in frases_sentimiento_test]
    })

    train_dataframe = pd.DataFrame({
        "phrase":[frase for frase, _ in frases_sentimiento_train],
        "target":[sentimiento for _, sentimiento in frases_sentimiento_train]
    })

    # Creamos la carpeta "output" si no existe
    output_directory = main_directory / "output"
    output_directory.mkdir(parents=True, exist_ok=True)

    # Guardamos los dataframes como CSV en la carpeta output
    test_dataframe.to_csv(output_directory / "test_dataset.csv", index=False)
    train_dataframe.to_csv(output_directory / "train_dataset.csv", index=False)

    return None
