# from flask_wtf import FlaskForm
# from wtforms import SelectField
# from wtforms.validators import Required
#
#
# class LoadFile(FlaskForm):
#     bank_select = SelectField('Bank', validators=[Required()])



from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Required


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
                    ('Alfa', 'Альфа Банк'),
                    ('Oshchad', 'ОщадБанк'),
                    ('UkrExim', 'УркЕкзим'),
                    ('PaymentSystem', 'Платіжні системи')])