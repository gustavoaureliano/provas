class Estilos:
    estilobtn = """
    QPushButton {
        background-color: #004040;
        color: white;
        font: bold;
        font-size: 26px;
        border-radius: 5px;
        padding: 10px 15px;
    }
    QPushButton:hover {
        background-color: #005050;
        color: white;
    }
    QPushButton:pressed {
        background-color: #008080;
        color: #EEEEEE;
    }
    """

    estiloNumAlternativa = """
    QLabel { 
        border: 1px solid black;
        border-radius: 26px;
        background-color: #004040;
        color: white;
    }
    """

    estiloBtnAlternativa = """
    QPushButton, QRadioButton { 
        border: 1px solid black;
        border-radius: 5px;
        background-color: white;
        color: black;
    }
    QRadioButton::indicator {
        width: px;
        height: 0px;
        background-color: blue;
    }
    QPushButton:hover, QRadioButton:hover { 
        border: 1px solid black;
        border-radius: 5px;
        background-color: #DDDFDD;
        color: black;
    }
    QRadioButton:pressed, QRadioButton:checked, QPushButton:checked { 
        border: 1px solid black;
        border-radius: 5px;
        background-color: #004040;
        color: white;
    }
    """

    estiloAlternativa = """
    QLabel { 
        border: 1px solid black;
        border-radius: 5px;
        background-color: white;
        color: black;
    }
    """