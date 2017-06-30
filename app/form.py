from flask_wtf import FlaskForm
from wtforms import SelectField


class LoadFile(FlaskForm):
    bank_select = SelectField(u'Banks', choices=[
                    ('Aval', 'Аваль'),
                    ('Avangard', 'Авангард'),
                    ('Bsbbank', 'БСБ Банк'),
                    ('Centercredit', 'Центр Кредит'),
                    ('Privat', 'Приват'),
                    ('Procreditbank', 'ПроКредит Банк'),
                    ('Vtb', 'ВТБ'),
                    ('BsbbankForeign', 'БСБ Банк Валюта'),
                    # ('Alfa', 'Альфа Банк'),
                    ('Oshchad', 'ОщадБанк'),
                    ('UkrExim', 'УркЕкзим'),
                    ('PaymentSystem', 'Платіжні системи')])